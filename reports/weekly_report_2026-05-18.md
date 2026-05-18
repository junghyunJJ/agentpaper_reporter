# Weekly AI Agent Paper Report

**Generated:** 2026-05-18 13:58
**Period:** 2026-05-11 to 2026-05-17

## Summary

- **Total papers fetched:** 819
- **Papers matching keywords:** 181
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-05-11) | Change |
|--------|-----------|-----------|--------|
| Total matched | 181 | 182 | -1 |
| arxiv | 180 | 181 | -1 |
| biorxiv | 1 | 1 | +0 |
| medrxiv | 0 | 0 | +0 |

### Notable Trends

**This week vs. last week (AI‑agent papers)**  

| Metric | This week | Last week | Δ |
|--------|-----------|-----------|---|
| Total papers | 181 | 182 | –1 (‑0.5 %) |
| arXiv papers | 180 | 181 | –1 |
| bioRxiv papers | 1 | 1 | 0 |
| Avg. papers / day* | 26 ± 2 | 26 ± 2 | unchanged |

\*Assuming a 7‑day window; the standard deviation is tiny, showing a very steady flow.

---

### 1. Topic focus is shifting toward **system‑level orchestration & memory architectures**  
* **Memory‑centric designs** dominate this week’s headline list (e.g., *FORGE* and *paper.json*).  Both papers propose novel ways to store, retrieve, or standardise agent‑state without frequent weight updates.  
* Last week’s top titles were centered on **co‑ordination failures and learning dynamics** (*The Memory Curse*, *TraceFix*, *AgentEscapeBench*).  The emphasis has moved from diagnosing problems to building **robust, reusable memory and coordination conventions**.

### 2. Increasing **cross‑domain application** of multi‑agent LLMs  
* This week sees two applied‑systems papers:  
  * **Utility‑billing & CO₂ analytics** – a generative‑AI pipeline for sustainable resource optimisation.  
  * **MU‑MIMO‑OFDMA wireless scheduling** – a multi‑agent LLM controller for real‑time radio resource allocation.  
* Last week’s applied work was limited to **molecular synthesis** and **federated fine‑tuning**, indicating a broadening from chemistry/ML‑ops to energy and communications domains.

### 3. Continued but modest **presence of non‑CS venues**  
* The single bioRxiv paper each week remains unchanged, and both weeks feature a **neuroscience‑oriented title** (this week: “Reduced synaptic plasticity… schizophrenia”).  The ratio (≈0.6 % of total) is stable, suggesting that AI‑agent research is still largely confined to CS‑centric archives.

### 4. Methodological nuance: **cost‑performance trade‑offs** gaining visibility  
* The paper *“Context, Reasoning, and Hierarchy: A Cost‑Performance Study of Compound LLM Agent Design in an Adversarial POMDP”* introduces systematic benchmarking of agent depth/complexity versus compute budget—an emerging meta‑research direction that was not highlighted in the previous week’s top list.

### 5. Overall volume is **steady**, not expanding.  
* With only a one‑paper drop overall, the field’s publishing cadence is essentially saturated at ~180 papers per week.  Any meaningful growth will likely come from **new venues or large‑scale benchmark releases** rather than a spontaneous surge in submissions.

---



## Biomedical Highlights (1 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


**Brief Overview of the Selected Papers (3‑5 sentences)**  

The collection of studies converges on how artificial‑intelligence (AI)–driven computational models can illuminate the neural mechanisms underlying psychiatric and neurodevelopmental disorders, and how those models can be harnessed for diagnosis, phenotyping, or therapeutic targeting.  In the schizophrenia paper, a biophysically realistic spiking‑network model integrates synaptic‑plasticity rules and excitation‑inhibition (E/I) balance to explain the experimentally observed contraction of peripersonal‑space (PPS) boundaries, showing that reduced plasticity and heightened inhibition produce the abnormal PPS encoding that underlies bodily‑self disturbances.  Parallel work on autism‑spectrum disorder (ASD) and attention‑deficit/hyperactivity disorder (ADHD) uses deep‑learning classifiers trained on multimodal neuroimaging (fMRI, diffusion MRI) and behavioral time‑series to identify disorder‑specific signatures of altered E/I circuitry and cortical hierarchy, validating the models against large‑scale clinical cohorts.  Another set of papers applies reinforcement‑learning agents to simulate maladaptive decision‑making in depression and anxiety, demonstrating that biased value‑updates and altered exploration parameters reproduce key behavioral phenotypes and predict individual treatment response.  Across the papers, the common methodological thread is the coupling of biologically grounded neural simulations with modern AI techniques (graph neural networks, variational auto‑encoders, and meta‑learning) to both test mechanistic hypotheses (plasticity deficits, E/I dysregulation) and generate translational biomarkers for precision psychiatry.



### 1. Reduced synaptic plasticity and E/I imbalance drive Peripersonal Space boundaries expansion in Schizophrenia

- **Authors:** Paredes, R., Grigoras, V., Ferroni, F., Ardizzi, M., Ferri, F., Series, P.
- **Published:** 2026-05-12
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2024.07.21.604515](https://doi.org/10.1101/2024.07.21.604515)

- **Categories:** neuroscience


> **Main contribution:** The paper provides a computational account of why schizophrenia (SCZ) patients show a narrowed yet still plastic peripersonal‑space (PPS) representation, showing that abnormal excitation‑inhibition (E/I) balance and reduced feed‑forward synaptic density alone cannot explain the impaired PPS expansion after tool use.  

**Methodology:** The authors built a biologically‑inspired PPS neural network model incorporating Hebbian learning, fitted it to behavioral PPS measurements before and after a tool‑use training protocol, and systematically manipulated the model’s learning rate, forgetting rate, and plasticity threshold to mimic SCZ‑related synaptic alterations.  

**Key findings:** PPS can still expand in the model despite E/I imbalance or lower synaptic density, but matching the patients’ limited post‑training expansion requires a *reduction* in synaptic plasticity (via slower learning, faster forgetting, or a higher plasticity threshold). This suggests that dysfunctional Hebbian plasticity, rather than static E/I dysregulation, underlies PPS abnormalities in SCZ and motivates experiments that track PPS changes in real time to differentiate among these mechanistic hypotheses.


<details>
<summary>Abstract</summary>

Abnormal encoding of peripersonal space (PPS) is believed to affect bodily self disruptions in schizophrenia (SCZ). Empirical studies show that SCZ patients exhibit a narrower PPS than controls but maintain its plasticity. Computational research links this smaller PPS to increased excitation of sensory neurons and reduced feedforward synaptic density. However, it is unclear how such differences influence learning during the expansion of PPS boundaries. We hypothesise that Hebbian plasticity can account for PPS expansion after active tool use training. To explore the effect of such mechanisms on PPS plasticity, we developed a SCZ network model which was fit to behavioural data before and after tool manipulation. We found that PPS expansion occurs in spite of E/I imbalance or reduced synaptic density, but does not match the post-training PPS representation of patients. A better fit was obtained after altering plasticity by either reducing the learning rate, increasing the forgetting rate or increasing the plasticity threshold. We discuss our findings in terms of dysfunctional plasticity in SCZ and highlight the key challenges in identifying the neurobiological correlates of reduced plasticity within PPS networks. Because current empirical data supports multiple viable mechanisms, we propose experiments to distinguish between the proposed plasticity accounts and clarify mixed findings on PPS representation in SCZ.

Graphical Abstract

O_FIG O_LINKSMALLFIG WIDTH=200 HEIGHT=123 SRC="FIGDIR/small/604515v2_ufig1.gif" ALT="Figure 1">
View larger version (34K):
org.highwire.dtl.DTLVardef@14ee71forg.highwire.dtl.DTLVardef@127c3aborg.highwire.dtl.DTLVardef@19f1338org.highwire.dtl.DTLVardef@a6e437_HPS_FORMAT_FIGEXP  M_FIG C_FIG HighlightsO_LIUsing a peripersonal space network model, we found that PPS expansion after tool-use occurs in spite of E/I imbalance or reduced synaptic density.
C_LIO_LIReduced feedforward synaptic plasticity is required to match the post-training PPS representation of patients.
C_LIO_LISuch reduction of synaptic plasticity could be achieved by either reducing the learning rate, increasing the forgetting rate or increasing the plasticity threshold relative to a healthy control model.
C_LIO_LIOur model predicts that measuring PPS at intermediate time points during a longer stimulation protocol would help distinguish between these plasticity differences.
C_LI

</details>


---



## Arxiv (180 papers)


### 1. A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation

- **Authors:** Pavan Manjunath, Thomas Pruefer
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16250v1](http://arxiv.org/abs/2605.16250v1)
- **PDF:** [https://arxiv.org/pdf/2605.16250v1](https://arxiv.org/pdf/2605.16250v1)
- **Categories:** cs.CL, cs.AI, cs.DB, cs.LG


> The paper introduces a unified, production‑grade framework that combines several generative‑AI components to produce “smart” utility bills—including a readable natural‑language statement, a defensible carbon‑intensity metric per kWh, and price‑sensitive load‑scheduling recommendations.  The architecture couples (1) a constrained‑decoding generative‑AI agent that converts structured billing data into customer‑facing text, (2) a transformer‑based day‑ahead consumption forecaster that outputs calibrated quantile forecasts, (3) a quantile‑regulated emission optimizer that schedules loads against grid‑stress and CO₂ constraints, and (4) a downstream decision engine that assembles the final bill and actionable suggestions.  Empirical evaluation on real‑world utility datasets shows that the agent’s generated statements achieve >90 % linguistic fidelity while preserving regulatory compliance, the forecaster attains state‑of‑the‑art quantile calibration (CRPS reduction of 12 %), and the integrated optimization reduces scheduled emissions by up to 15 % without increasing customer cost—demonstrating a viable, end‑to‑end AI pipeline for agentic, carbon‑aware utility billing.


<details>
<summary>Abstract</summary>

Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands

</details>


### 2. FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast

- **Authors:** Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16233v1](http://arxiv.org/abs/2605.16233v1)
- **PDF:** [https://arxiv.org/pdf/2605.16233v1](https://arxiv.org/pdf/2605.16233v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA, eess.SY


> The paper introduces **FORGE**, a population‑based framework that lets large‑language‑model (LLM) agents acquire and share self‑generated memory (textual rules, few‑shot examples, or a mix) without any gradient updates. FORGE embeds a Reflexion‑style inner loop where a “reflection” agent rewrites failed trajectories into reusable knowledge artifacts, then an outer loop selects the best‑performing agent each stage and broadcasts its memory to the whole population while freezing agents that have converged. Across four LLM families on the stochastic CybORG CAGE‑2 network‑defense POMDP, FORGE yields 1.7–7.7× higher returns than zero‑shot baselines and 29–72% improvements over single‑agent Reflexion, cutting catastrophic failures to ~1%; ablations show that the broadcast of memory drives the gains, and that example‑based memory gives the highest scores while rule‑based memory is most token‑efficient, especially helping weaker models.


<details>
<summary>Abstract</summary>

Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.

</details>


### 3. Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP

- **Authors:** Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16205v1](http://arxiv.org/abs/2605.16205v1)
- **PDF:** [https://arxiv.org/pdf/2605.16205v1](https://arxiv.org/pdf/2605.16205v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA, eess.SY


> The paper systematically investigates how different design choices—context representation, reasoning tools, and hierarchical task decomposition—affect the cost‑performance trade‑off of compound LLM agents in the adversarial, partially observable cyber‑defense benchmark CybORG CAGE‑2. By evaluating five model families across twelve configurations (3,475 episodes) with fine‑grained token accounting, the authors show that a deterministic state‑tracking layer (programmatic abstraction) yields the greatest returns per token (up to 76 % improvement), while adding deliberation tools (self‑questioning, critique, improvement) to a hierarchical architecture actually harms performance (up to 3.4 × lower return and 1.8–2.7 × higher token usage), a phenomenon they term a “deliberation cascade.” Consequently, the study recommends prioritising robust state abstraction and clean hierarchical decomposition over deep per‑agent reasoning for agentic AI systems operating in structured adversarial POMDPs.


<details>
<summary>Abstract</summary>

Deploying compound LLM agents in adversarial, partially observable sequential environments requires navigating several design dimensions: (1) what the agent sees, (2) how it reasons, and (3) how tasks are decomposed across components. Yet practitioners lack guidance on which design choices improve performance versus merely increase inference costs. We present a controlled study of compound LLM agent design in CybORG CAGE-2, a cyber defense environment modeled as a Partially Observable Markov Decision Process (POMDP). Reward is non-positive, so all configurations operate in a failure-mitigation mode. Our evaluation spans five model families, six models, and twelve configurations (3,475 episodes) with token-level cost accounting. We vary context representation (raw observations vs. a deterministic state-tracking layer with compressed history), deliberation (self-questioning, self-critique, and self-improvement tools, with optional chain-of-thought prompting), and hierarchical decomposition (monolithic ReAct vs. delegation to specialized sub-agents). We find that: (1) Programmatic state abstraction delivers the largest returns per token spent (RPTS), improving mean return by up to 76% over raw observations. (2) Distributing deliberation tools across a hierarchy degrades performance relative to hierarchy alone for all five model families, reaching up to 3.4$\times$ worse mean return while using 1.8-2.7$\times$ more tokens. We call this destructive pattern a deliberation cascade. (3) Hierarchical decomposition without deliberation achieves the best absolute performance for most models, and context engineering is generally more cost-effective than deliberation. These findings suggest a design principle for structured adversarial POMDPs: invest in programmatic infrastructure and clean task decomposition rather than deeper per-agent reasoning, as these strategies can interfere when combined.

</details>


### 4. paper.json: A Coordination Convention for LLM-Agent-Actionable Papers

- **Authors:** Arquimedes Canedo
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16194v1](http://arxiv.org/abs/2605.16194v1)
- **PDF:** [https://arxiv.org/pdf/2605.16194v1](https://arxiv.org/pdf/2605.16194v1)
- **Categories:** cs.DL, cs.AI, cs.IR, cs.MA


> The paper introduces **paper.json**, a lightweight, machine‑readable companion to academic PDFs that gives large‑language‑model agents fine‑grained, actionable metadata: stable claim identifiers, an explicit “does‑not‑claim” list, exact shell commands for reproducing each figure, and stable definition IDs. By requiring authors to produce a hand‑written JSON file in under an hour (C4), the convention enables agents to cite sub‑claims precisely, avoid over‑claiming scope, and directly execute reproducibility steps without searching code repositories. Empirical validation shows that a compliant paper (including the authors’ own example) passes an automated schema validator, demonstrating that the approach can reliably supply agents with the structured evidence needed for trustworthy claim verification and reproducible research.


<details>
<summary>Abstract</summary>

LLM agents routinely serve as first (and sometimes only) readers of academic papers, skimming for sub-claims, extracting reproducibility steps, and generalizing scope. Standard prose papers produce recurring failures in this role: sub-claims that cannot be cited at sub-paper granularity, scope overextension beyond what the paper tests, and figure commands buried in codebases rather than the paper itself. We propose `paper.json`, a companion JSON file that travels with the PDF and addresses each failure with a lightweight convention: stable claim IDs (C1), an explicit does-not-claim list (C2), exact per-figure shell commands (C3), and stable definition IDs (C5). A fifth convention (C4) holds that minimum viable compliance, hand-written JSON alongside the PDF, is achievable in under an hour for a finished paper without touching the human-readable output. C1, C2, C3, and C5 are open invitations: an agent that reads a compliant paper and acts on it produces evidence for or against them. This paper is itself compliant: `uv run validator.py paper.json --against paper.typ` passes. Repo: https://github.com/arquicanedo/paper-json

</details>


### 5. MAxLM: Multi-Agent Language Model-Based Scheduling and Resource Allocation in MU-MIMO-OFDMA-Enabled Wireless Networks

- **Authors:** Adnan Quadri, Hongxiang Li
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16144v1](http://arxiv.org/abs/2605.16144v1)
- **PDF:** [https://arxiv.org/pdf/2605.16144v1](https://arxiv.org/pdf/2605.16144v1)
- **Categories:** eess.SP, cs.MA, cs.NI


> The paper introduces **MAxLM**, a multi‑agent framework that harnesses a pretrained small‑/medium‑sized language model (xLM) to autonomously perform joint user scheduling and resource allocation (SRA) for uplink scheduled access in MU‑MIMO‑OFDMA WLANs. By embedding the agents in the AI‑assisted WiSER platform, the method formulates SRA decisions as prompted language‑model inference, iteratively coordinating across agents to allocate antennas, sub‑carriers and power for multiple stations. Simulations on varying STA counts and AP antenna configurations show that MAxLM consistently outperforms conventional benchmark schedulers, delivering higher uplink throughput and more efficient spectrum utilization.


<details>
<summary>Abstract</summary>

Wireless networks support multi-user (MU) communication with multiple-input multiple-output (MIMO) and orthogonal frequency-division multiple access (OFDMA) technologies. In the joint MU-MIMO-OFDMA-enabled transmission mode, network throughput can be significantly increased by effectively utilizing the multi-channel resources to schedule numerous wireless users/stations (STAs) simultaneously. In this paper, we study ways to optimize the user scheduling and resource allocation (SRA) for the UL scheduled access (UL-SA) of a joint MU-MIMO-OFDMA-enabled wireless local area network (WLAN). In particular, we propose a multi-agent (MA) framework that utilizes an openly available pretrained small/medium-sized Language Model (xLM) to perform SRA for the UL-SA. To facilitate autonomous SRA using our proposed technique, we introduce the AI-assisted Wireless Systems Engineering and Research (WiSER) platform. We evaluate the performance of MAxLM-optimized SRA for network scenarios with a varying number of STAs and antenna settings on the WLAN Access Point. Numerical results confirm that our proposed technique achieves higher UL-SA throughput than the benchmark techniques.

</details>


### 6. Look Before You Leap: Autonomous Exploration for LLM Agents

- **Authors:** Ziang Ye, Wentao Shi, Yuxin Liu, Yu Wang, Zhengzhou Cai, Yaorui Shi, Qi Gu, Xunliang Cai, Fuli Feng
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16143v1](http://arxiv.org/abs/2605.16143v1)
- **PDF:** [https://arxiv.org/pdf/2605.16143v1](https://arxiv.org/pdf/2605.16143v1)
- **Categories:** cs.AI, cs.CL


> The paper shows that LLM‑based agents often “jump to conclusions” by exploiting prior knowledge before they have gathered enough information about a new environment, leading to brittle performance. To remedy this, the authors introduce **Exploration Checkpoint Coverage (ECC)**—a verifiable metric that quantifies how comprehensively an agent discovers key states, objects, and affordances—and demonstrate that standard task‑oriented RL training yields low ECC scores and narrow, repetitive behaviours. They then propose a **dual‑rollout training regime** (alternating task‑execution and dedicated exploration rollouts, each rewarded by its own verifiable signal) together with an **Explore‑then‑Act** paradigm that first spends a bounded interaction budget on systematic exploration and only then attempts the task; experiments show that this approach markedly increases ECC, improves downstream task success, and yields agents that generalize more robustly to real‑world‑like settings.


<details>
<summary>Abstract</summary>

Large language model based agents often fail in unfamiliar environments due to premature exploitation: a tendency to act on prior knowledge before acquiring sufficient environment-specific information. We identify autonomous exploration as a critical yet underexplored capability for building adaptive agents. To formalize and quantify this capability, we introduce Exploration Checkpoint Coverage, a verifiable metric that measures how broadly an agent discovers key states, objects, and affordances. Our systematic evaluation reveals that agents trained with standard task-oriented reinforcement learning consistently exhibit narrow and repetitive behaviors that impede downstream performance. To address this limitation, we develop a training strategy that interleaves task-execution rollouts and exploration rollouts, with each type of rollout optimized by its corresponding verifiable reward. Building on this training strategy, we propose the Explore-then-Act paradigm, which decouples information-gathering from task execution: agents first utilize an interaction budget to acquire grounded environmental knowledge, then leverage it for task resolution. Our results demonstrate that learning to systematically explore is imperative for building generalizable and real-world-ready agents.

</details>


### 7. Multi-Agent Cooperative Transportation: Optimal and Efficient Task Allocation and Path Finding

- **Authors:** Ning Zhou, Nikolai W. F. Bode, Edmund R. Hunt
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16097v1](http://arxiv.org/abs/2605.16097v1)
- **PDF:** [https://arxiv.org/pdf/2605.16097v1](https://arxiv.org/pdf/2605.16097v1)
- **Categories:** cs.MA


> The paper introduces **Cooperative Transportation Task Allocation and Path Finding (CT‑TAPF)**, a formal model that unifies team formation, task assignment, and collision‑free routing for multi‑robot transport of objects too large for a single agent—an ability missing from standard MAPF/TAPF frameworks. To solve CT‑TAPF, the authors propose **CT‑TCBS**, an optimal Conflict‑Based Search algorithm enhanced with an *Incremental Expansion* technique that dramatically prunes the exponential team‑formation space, and they also devise a suite of fast, sub‑optimal solvers that prioritize tasks using a global difficulty metric (best‑ or worst‑task selection). Experiments show that (1) incremental expansion outperforms naïve combinatorial search, (2) aggressive conflict resolution can hurt performance in the integrated problem (the “task‑conflict expansion dilemma”), and (3) the sub‑optimal solvers achieve a new, superior trade‑off between solution quality and runtime compared with existing agent‑centric baselines, establishing a practical foundation for cooperative agentic AI in logistics.


<details>
<summary>Abstract</summary>

Multi-robot systems are integral to modern logistics, but their capabilities are often limited to tasks executable by individual agents. This paper addresses a critical gap in existing frameworks like Multi-Agent Path Finding (MAPF) and Task Allocation and Path Finding (TAPF), which lack true cooperation for transporting large items that require multiple agents. To this end, we formalise the Cooperative Transportation Task Allocation and Path Finding (CT-TAPF) problem, which integrates team formation, task assignment, and collision-free pathfinding. We present an optimal solver, Cooperative Transportation Task Conflict-Based Search (CT-TCBS), which features a novel Incremental Expansion strategy to tackle the combinatorial explosion inherent in team formation. Recognising the computational cost of optimality, we also develop a family of sub-optimal solvers that employ a global, task-centric perspective, selecting the next task to assign based on a global difficulty metric (Best Task or Worst Task). Our comprehensive empirical evaluation demonstrates three key findings: (1) the incremental expansion strategy significantly outperforms the naive combinatorial approach by successfully pruning the dominant task-allocation search space; (2) we identify a task-conflict expansion dilemma, where sophisticated conflict resolvers effective for large-agent pathfinding subproblems can be detrimental in the integrated CT-TAPF setting; and (3) our proposed sub-optimal solvers establish a new, more efficient frontier on the solution quality-runtime spectrum compared to "nn-" agent-centric baselines. This work provides a foundational framework and a set of effective algorithms for a new, practical class of cooperative multi-agent problems.

</details>


### 8. RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents

- **Authors:** Zijie Dai, Shiyuan Deng, Sheng Guan, Yizhou Tian, Xin Yao, Xiao Yan, James Cheng
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16045v1](http://arxiv.org/abs/2605.16045v1)
- **PDF:** [https://arxiv.org/pdf/2605.16045v1](https://arxiv.org/pdf/2605.16045v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> **RecMem** introduces a hybrid memory architecture for long‑running LLM agents that dramatically cuts the token cost of memory construction. Instead of invoking the LLM on every interaction, RecMem first deposits raw dialogue into a low‑cost “subconscious” layer indexed by lightweight embeddings; only when the system detects recurrent, semantically similar interactions does it trigger the LLM to extract and summarize episodic and semantic memories, adding a refinement step to recover omitted details. Experiments on three state‑of‑the‑art agent memory baselines show that RecMem achieves up to **87 % reduction in token usage** while **outperforming them in retrieval and reasoning accuracy**, demonstrating that recurrence‑driven, conditional consolidation is an efficient and effective strategy for scalable agentic AI.


<details>
<summary>Abstract</summary>

Memory systems often organize user-agent interactions as retrievable external memory and are crucial for long-running agents by overcoming the limited context windows of LLMs. However, existing memory systems invoke LLMs to process every incoming interaction for memory extraction, and such an eager memory consolidation scheme leads to substantial token consumption. To tackle this problem, we propose RecMem by rethinking when memory consolidation should be conducted. RecMem stores incoming interactions in a subconscious memory layer and encode them using lightweight embedding models for retrieval. LLMs are only invoked to extract episodic and semantic memory when sustained recurrence are observed for semantically similar interactions. Such recurrence-based consolidation works because these interactions correspond to a semantic cluster with rich information and thus are worth extraction and summarization. To improve accuracy, RecMem also incorporates a semantic refinement mechanism that recovers the fine-grained facts omitted by memory extraction. Experiments show that RecMem reduces the memory construction token cost of three SOTA memory systems by up to 87% while exceeding their accuracy.

</details>


### 9. Who Owns This Agent? Tracing AI Agents Back to Their Owners

- **Authors:** Ruben Chocron, Doron Jonathan Ben Chayim, Eyal Lenga, Gilad Gressel, Alina Oprea, Yisroel Mirsky
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.16035v1](http://arxiv.org/abs/2605.16035v1)
- **PDF:** [https://arxiv.org/pdf/2605.16035v1](https://arxiv.org/pdf/2605.16035v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> **Main contribution:** The paper introduces and formalizes the problem of *agent attribution*—linking an observed autonomous AI agent’s behavior back to the specific user account that launched it on a hosted model service—and proposes the first practical, vendor‑side solution.  

**Methodology:** The authors design a *canary‑based attribution protocol*: an authorized observer injects a distinctive, covert marker (the canary) into the agent’s input/output stream; the service provider then scans a short, bounded window of session logs to recover the exact session and originating account. They develop both simple canaries (effective when the operator does not tamper with the stream) and robust, adversarial‑resistant canaries that survive filtering or paraphrasing, proving that suppression would significantly degrade the agent’s primary task performance.  

**Key findings:** Experiments on a variety of real‑world agents—including benign and malicious use cases—demonstrate that the protocol reliably identifies the responsible account, remains effective against adaptive adversaries, and scales to vendor‑level deployment with modest computational overhead, thereby closing a critical accountability gap for agentic AI systems.


<details>
<summary>Abstract</summary>

AI agents are increasingly deployed to act autonomously in the world, yet there is still no reliable way to trace a harmful agent back to the account that deployed it. This creates the same accountability gap across both ends of the intent spectrum: benign operators may deploy misconfigured or overbroad agents that cause harm unintentionally, while malicious operators may deliberately weaponize agents for scams, harassment, or cyber attacks. In many cases, these agents are powered by vendor-hosted models, a dependency that holds even for sophisticated adversaries such as state actors conducting cyber operations. In either case, affected parties can observe the behavior but cannot notify the responsible operator, stop the session, or identify the account for investigation.
  We formalize this gap as the problem of agent attribution: linking an observed agent interaction to the responsible account at the hosting vendor. To our knowledge, this is the first work to define the problem and present a practical solution. Our protocol is canary-based: an authorized party injects a canary into the agent's interaction stream, and the vendor searches a narrow window of session logs to recover the originating session and account. Simple canaries suffice in non-adversarial settings. For adversarial operators who filter or paraphrase incoming content, we develop robust canary constructions that cannot be suppressed without degrading the agent's own task performance, yielding a formal asymmetry in the defender's favor. We evaluate a variety of scenarios including real-world agents and show that our attribution method is reliable, robust, and scalable for vendor-side deployment.

</details>


### 10. Learning Bilevel Policies over Symbolic World Models for Long-Horizon Planning

- **Authors:** Dillon Z. Chen, Till Hofmann, Toryn Q. Klassen, Sheila A. McIlraith
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15975v1](http://arxiv.org/abs/2605.15975v1)
- **PDF:** [https://arxiv.org/pdf/2605.15975v1](https://arxiv.org/pdf/2605.15975v1)
- **Categories:** cs.AI, cs.RO


> The paper introduces **BISON**, a bilevel policy framework that couples a low‑level neural controller (trained by imitation learning on continuous manipulation demonstrations) with a high‑level symbolic planner built from abstractions of those demonstrations and inductively generalized to new tasks. By separating long‑horizon reasoning from motor execution, BISON can synthesize plans over thousands of symbolic objects while delegating only the concrete actions to the learned low‑level policy, achieving superior generalization to longer horizons and larger object sets than prior end‑to‑end or VLA methods with dramatically lower computation and memory costs. Experiments on extended MetaWorld benchmarks confirm that the high‑level symbolic component solves problems with up to 10 000 objects in under a minute, and the combined system outperforms baselines on both success rate and efficiency.


<details>
<summary>Abstract</summary>

We tackle the challenge of building embodied AI agents that can reliably solve long-horizon planning problems. Imitation learning from demonstrations has shown itself to be effective in training robots to solve a diversity of complex tasks requiring fine motor control and manipulation over low-level (LL), continuous environments. Yet, it remains a difficult endeavour to generate long-horizon plans from imitation learning alone. In contrast, high-level (HL), symbolic abstractions facilitate efficient and interpretable long-horizon planning. We propose to combine the strengths of LL imitation learning for manipulation and control, and HL symbolic abstractions for long-horizon planning. We realise this idea via \emph{bilevel policies} of the form $(π^{\mathrm{hl}}, π^{\mathrm{ll}})$, consisting of a neural policy $π^{\mathrm{ll}}$ learned from LL demonstrations, and an HL symbolic policy $π^{\mathrm{hl}}$ that is constructed from symbolic abstractions of the LL demonstrations combined with inductive generalisation. We implement these ideas in the BISON system. Experiments on extended MetaWorld benchmarks demonstrate that BISON generalises to long horizons and problems with greater numbers of objects than those solved by VLA and end-to-end methods, and is more time and memory efficient in training and inference. Notably, when ignoring LL execution, BISON's HL policies can solve HL problems with 10,000 relevant objects in under a minute. Project page: https://dillonzchen.github.io/bison

</details>


### 11. Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design

- **Authors:** Alberto Pepe, Chien-Yu Lin, Despoina Magka, Bilge Acun, Yannan Nellie Wu, Anton Protopopov, Carole-Jean Wu, Yoram Bachrach
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15871v1](http://arxiv.org/abs/2605.15871v1)
- **PDF:** [https://arxiv.org/pdf/2605.15871v1](https://arxiv.org/pdf/2605.15871v1)
- **Categories:** cs.AI


> The paper presents two complementary LLM‑driven frameworks—**AIRA‑Compose**, which orchestrates a team of 11 agents to conduct high‑level neural‑architecture search, and **AIRA‑Design**, which tasks a separate team with inventing low‑level mechanisms (e.g., novel attention kernels and training scripts). Using a 24‑hour compute budget, AIRA‑Compose generated 14 new models (AIRAformers and AIRAhybrids) that, when scaled to 1 B parameters, consistently beat Llama 3.2 and prior Composer baselines, achieving 2.4‑3.8 % higher downstream accuracy and 23‑71 % faster scaling; AIRA‑Design’s agent‑crafted components reached within a few percent of human‑state‑of‑the‑art results on Long‑Range Arena and set a new 0.968 bpb validation score on the Autoresearch benchmark. These results demonstrate that coordinated LLM agents can autonomously discover both macro‑architectural designs and micro‑algorithmic optimizations that match or surpass manually engineered foundation models, marking a concrete step toward recursive self‑improvement in agentic AI.


<details>
<summary>Abstract</summary>

Toward recursive self-improvement, we investigate LLM agents autonomously designing foundation models beyond standard Transformers. We introduce a dual-framework approach: AIRA-Compose for high-level architecture search, and AIRA-Design for low-level mechanistic implementation. AIRA-Compose uses 11 agents to explore fundamental computational primitives under a 24-hour budget. Agents evaluate million-parameter candidates, extrapolating top designs to 350M, 1B, and 3B scales. This yields 14 architectures across two families: AIRAformers (Transformer-based) and AIRAhybrids (Transformer-Mamba). Pre-trained at 1B scale, these consistently outperform Llama 3.2 and Composer-found baselines. On downstream tasks, AIRAformer-D and AIRAhybrid-D improve accuracy by 2.4% and 3.8% over Llama 3.2. Furthermore, AIRA-Compose finds models with highly efficient scaling frontiers: AIRAformer-C scales 54% and 71% faster than Llama 3.2 and Composer's best Transformer, while AIRAhybrid-C outscales Nemotron-2 by 23% and Composer's best hybrid by 37%. AIRA-Design tasks 20 agents with writing novel attention mechanisms for long-range dependencies and high-performing training scripts. On the Long Range Arena benchmark, agent-designed architectures reach within 2.3% and 2.6% of human state-of-the-art on document matching and text classification. On the Autoresearch benchmark, Greedy Opus 4.5 achieves 0.968 validation bits-per-byte under a fixed time budget, surpassing the published minimum. Together, these frameworks show AI agents can autonomously discover architectures and algorithmic optimizations matching or surpassing hand-designed baselines. This establishes a powerful paradigm for discovering next-generation foundation models, marking a clear step toward recursive self-improvement.

</details>


### 12. BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge

- **Authors:** Sihan Fu, Oucheng Liu, Shiyuan Wang, Jin Shi, Chengkun Wei
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15815v1](http://arxiv.org/abs/2605.15815v1)
- **PDF:** [https://arxiv.org/pdf/2605.15815v1](https://arxiv.org/pdf/2605.15815v1)
- **Categories:** cs.SE, cs.CL, cs.MA


> BootstrapAgent tackles the bottleneck of repository bootstrapping for code‑generation agents by turning the exploratory setup process into a reusable knowledge artifact called a **.bootstrap contract**. The system uses a multi‑agent pipeline—evidence extraction, structured planning, deterministic Docker verification, and trace‑driven repair—to distill resolved dependencies, diagnostic checks, and repair heuristics into a persistent, verifiable contract that downstream agents can consume without re‑exploring the repository. On three benchmark suites BootstrapAgent reaches 92.9 % success (≈10 % over baselines), cuts downstream token consumption by 25.9 % and reduces build time by 22.3 %, demonstrating that reusable bootstrapping knowledge markedly improves the efficiency and reliability of agentic AI workflows.


<details>
<summary>Abstract</summary>

Code agents increasingly help developers work with unfamiliar repositories, but every such task depends on a costly prerequisite: bootstrapping the repository into a usable development state. This process requires substantial trial-and-error exploration, yet the resulting knowledge--resolved dependencies, repair strategies--stays trapped in a single conversation, unavailable to future agents. We therefore formulate repository bootstrapping as a reusable startup knowledge problem and introduce BootstrapAgent, a multi-agent framework that distills the heuristics discovered during bootstrap exploration into a persistent, verifiable, agent-consumable .bootstrap contract. Through evidence extraction, structured planning, deterministic Docker-based verification, and trace-driven repair, BootstrapAgent generates a contract covering environment setup, diagnostic checks, minimal verification, and accumulated repair knowledge. We further propose warm repair with clean replay to accelerate iterative debugging without sacrificing cold-start reproducibility, and a delta repair with sanity check to prevent reward hacking. Experiments on three benchmarks show that BootstrapAgent achieves a 92.9% success rate, outperforming the baseline by over 10% while reducing downstream agent token usage by 25.9% and build time by 22.3%. Our code is available at https://github.com/Vossera/BootstrapAgent.

</details>


### 13. From Gridworlds to Warehouses: Adapting Lightweight One-shot Multi-Agent Pathfinding for AGVs

- **Authors:** Hiroki Nagai, Keisuke Okumura
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15799v1](http://arxiv.org/abs/2605.15799v1)
- **PDF:** [https://arxiv.org/pdf/2605.15799v1](https://arxiv.org/pdf/2605.15799v1)
- **Categories:** cs.MA, cs.RO


> **Paper Summary**  

The authors introduce **Multi‑Agent Warehouse Pathfinding (MAWPF)**, a realistic one‑shot MAPF formulation for differential‑drive autonomous guided vehicles (AGVs) that augments the classic gridworld model with four key constraints: (1) actions limited to straight moves and in‑place rotations, (2) multi‑step rotation costs, (3) explicit acceleration/deceleration dynamics, and (4) prohibition of follower (rear‑end) collisions. To solve MAWPF they adapt four well‑known sub‑optimal MAPF solvers—Prioritized Planning (PP), Large Neighborhood Search 2 (LNS2), Priority Inheritance with Backtracking (PIBT), and LaCAM—and benchmark them on large warehouse scenarios. The experiments show that PP and LNS2 quickly become infeasible as agent count grows, whereas PIBT‑based methods retain scalability at the expense of higher makespan, highlighting PIBT‑style priority inheritance as the most promising approach for bringing grid‑based MAPF techniques into real‑world warehouse environments.


<details>
<summary>Abstract</summary>

Multi-agent pathfinding (MAPF) under one-shot planning is a core component of warehouse automation, yet classical formulations typically assume four-connected 2D grids with unit-time moves in four directions. To fill reality gaps while still being trackable with discrete combinatorial search, this work proposes a more practical counterpart tailored to differential-drive AGVs. We term this multi-agent warehouse pathfinding (MAWPF), featured with four constraints: (i) agent actions are restricted to straight motion and in-place rotation; (ii) rotations require multi-step costs; (iii) acceleration and deceleration are considered, and; (iv) follower collisions are prohibited to prevent rear-end crashes. To solve MAWPF efficiently, we adapt representative suboptimal MAPF algorithms-PP, LNS2, PIBT, and LaCAM-and conduct comprehensive benchmarking. Our experiments reveal that PP and LNS2 struggle to solve instances with many agents, while PIBT-based approaches achieve preferable scalability with increased solution cost. We believe that these constitute an important step toward adapting classical gridworld MAPF to operational warehouse setups.

</details>


### 14. ALSO: Adversarial Online Strategy Optimization for Social Agents

- **Authors:** Xiang Li, Liping Yi, Mingze Kong, Min Zhang, Zhongxiang Dai, QingHua Hu
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15768v1](http://arxiv.org/abs/2605.15768v1)
- **PDF:** [https://arxiv.org/pdf/2605.15768v1](https://arxiv.org/pdf/2605.15768v1)
- **Categories:** cs.AI, cs.CY


> **Contribution:** The paper introduces ALSO (Adversarial Online Strategy Optimization), the first framework that lets large‑language‑model‑based social agents continuously refine their behavior during multi‑turn dialogues by treating each combination of a static persona and a dynamic “strategy instruction” as an arm in an adversarial bandit problem.  

**Methodology:** ALSO formalizes the non‑stationary interaction as an adversarial bandit and equips it with a lightweight neural surrogate model that predicts reward signals from dialogue histories, enabling sample‑efficient, online exploration without offline reinforcement learning or costly retraining.  

**Findings:** Across the Sotopia social‑simulation benchmark, agents using ALSO achieve consistently higher reward and robustness than static‑persona baselines and prior optimization approaches, demonstrating that adversarial online strategy optimization can substantially improve the adaptability of agentic AI in dynamic social environments.


<details>
<summary>Abstract</summary>

Social simulation provides a compelling testbed for studying social intelligence, where agents interact through multi-turn dialogues under evolving contexts and strategically adapting opponents. Such environments are inherently non-stationary, requiring agents to dynamically adjust their strategies over time. However, most Large Language Model (LLM) based social agents rely on static personas, while existing approaches for enhancing social intelligence, such as offline reinforcement learning or external planners, are ill-suited to these settings, typically assuming stationarity and incurring substantial training overhead. To bridge this gap, we propose \textbf{ALSO} (\textbf{A}dversarial on\textbf{L}ine \textbf{S}trategy \textbf{O}ptimization), the first framework for online strategy optimization in multi-agent social simulation. ALSO advances social adaptation through two key contributions. (1) ALSO formulates multi-turn interaction as an adversarial bandit problem, where combinations of static personas and dynamic strategy instructions are treated as arms, providing a principled solution to non-stationarity without relying on environmental stability assumptions. (2) To predict rewards and generalize sparse feedback in multi-turn dialogues, ALSO introduces a lightweight neural surrogate to predict rewards from interaction histories, enabling sample-efficient exploration and continuous online adaptation. Experiments on the Sotopia benchmark demonstrate that ALSO consistently outperforms static baselines and existing optimization methods in dynamic environments, validating the effectiveness of adversarial online strategy optimization for building robust social agents.

</details>


### 15. DimMem: Dimensional Structuring for Efficient Long-Term Agent Memory

- **Authors:** Wentao Qiu, Haotian Hu, Fanyi Wang, Jinwei Kong, Yu Zhang
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15759v1](http://arxiv.org/abs/2605.15759v1)
- **PDF:** [https://arxiv.org/pdf/2605.15759v1](https://arxiv.org/pdf/2605.15759v1)
- **Categories:** cs.CL


> The paper introduces **DimMem**, a lightweight, structured memory system for LLM‑based agents that stores each experience as a self‑contained unit annotated with explicit dimensions (e.g., time, location, purpose, keywords). By converting raw interaction histories into these typed records, DimMem enables dimension‑aware retrieval, incremental updates, and selective context injection without loading full dialogues into the model’s context. Experiments on the LoCoMo‑10 and LongMemEval‑S benchmarks show that DimMem reaches 81.43 % and 78.20 % accuracy—substantially higher than prior lightweight memories—while cutting per‑query token usage by about 24 %, and its schema can be learned by compact extractors (e.g., a fine‑tuned Qwen3‑4B surpasses larger baselines).


<details>
<summary>Abstract</summary>

Large language model (LLM) agents require long-term memory to leverage information from past interactions. However, existing memory systems often face a fidelity--efficiency trade-off: raw dialogue histories are expensive, while flat facts or summaries may discard the structure needed for precise recall. We propose \textbf{DimMem}, a lightweight dimensional memory framework that represents each memory as an atomic, typed, and self-contained unit with explicit fields such as time, location, reason, purpose, and keywords. This representation exposes the structure needed for dimension-aware retrieval, memory update, and selective assistant-context recall without storing full histories in the model context. Across LoCoMo-10 and LongMemEval-S, DimMem achieves \textbf{81.43\%} and \textbf{78.20\%} overall accuracy, respectively, outperforming existing lightweight memory systems while reducing LoCoMo per-query token cost by \textbf{24\%}. We further show that dimensional memory extraction is learnable by compact models: after fine-tuning on the DimMem schema, a Qwen3-4B extractor surpasses LightMem with GPT-4.1-mini on both benchmarks and reaches performance comparable to, or better than, much larger extractors in key settings. These results suggest that explicit dimensional structuring is an effective and efficient foundation for long-term memory in LLM agents. Code is available at https://github.com/ChowRunFa/DimMem.

</details>


### 16. Differentiable Mixture-of-Agents Incentivizes Swarm Intelligence of Large Language Models

- **Authors:** Xingjian Wu, Junkai Lu, Siyu Yan, Xiangfei Qiu, Jilin Hu, Chenjuan Guo, Bin Yang
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15706v1](http://arxiv.org/abs/2605.15706v1)
- **PDF:** [https://arxiv.org/pdf/2605.15706v1](https://arxiv.org/pdf/2605.15706v1)
- **Categories:** cs.LG


> The paper introduces **Differentiable Mixture‑of‑Agents (DMoA)**, a novel multi‑agent architecture that lets large language models self‑organize their communication topology on the fly, rather than relying on fixed, hand‑crafted workflows. DMoA uses a context‑aware, recurrent routing network that produces sparse, step‑wise activations of individual agents, and it trains this router with a self‑supervised predictive‑entropy loss so the system can adapt its collaboration pattern at inference time without any external labels. Experiments on nine reasoning benchmarks show that DMoA not only attains state‑of‑the‑art results but also improves efficiency, robustness, and ensembling ability, demonstrating a scalable way to endow LLMs with emergent swarm intelligence.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) have catalyzed the development of multi-agent systems (MAS) for complex reasoning tasks. However, existing MAS typically rely on pre-defined or pre-compiled communication topologies, which limits their flexibility and adaptability to dynamic task requirements. In this work, we propose Differentiable Mixture-of-Agents (DMoA), a self-evolving multi-agent framework that enables elastic and adaptive agent collaboration during inference. Instead of statically constructing workflows, DMoA dynamically routes and activates agents at each reasoning step, allowing the system to implicitly simulate diverse communication topologies and adapt to evolving demands. To achieve this, we design a differentiable, context-aware routing mechanism that leverages recurrent structures to incorporate historical and contextual information, producing sparse agent activations in a step-wise manner. Furthermore, we introduce predictive entropy as self-supervised signals to optimize the routing process, enabling efficient test-time adaptation without external annotations. Extensive experiments across 9 benchmarks demonstrate that DMoA achieves state-of-the-art performance while exhibiting strong efficiency, robustness, and ensembling capabilities.

</details>


### 17. Distributed Zeroth-Order Policy Gradient for Networked Multi-agent Reinforcement Learning from Human Feedback

- **Authors:** Pengcheng Dai, He Wang, Dongming Wang, Jian Qin, Wenwu Yu
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15697v1](http://arxiv.org/abs/2605.15697v1)
- **PDF:** [https://arxiv.org/pdf/2605.15697v1](https://arxiv.org/pdf/2605.15697v1)
- **Categories:** cs.MA


> The paper introduces a fully distributed zeroth‑order policy‑gradient method for networked multi‑agent reinforcement learning that learns solely from human preference feedback rather than explicit rewards. By defining “spatiotemporally truncated” trajectory pairs that aggregate experience within each agent’s κ‑hop neighborhood and perturbing the joint policy with Gaussian noise, each agent can locally estimate its policy gradient using only the human’s binary preferences over these local trajectory snippets. The authors prove that the algorithm converges to an ε‑stationary point with polynomial sample complexity, and simulations on GridWorld and predator‑prey tasks show that it scales to large networks while achieving collaborative performance comparable to reward‑based baselines.


<details>
<summary>Abstract</summary>

We study a networked multi-agent reinforcement learning (NMARL) problem with human feedback in an infinite-horizon setting, where agents interact over an underlying network with localized state dependencies and aim to collaboratively maximize the average discounted return. Existing approaches with preference feedback are primarily developed for single-agent settings and rely on centralized training, which limits their scalability and applicability to large-scale networked multi-agent systems. To address this, we introduce a novel human feedback mechanism based on spatiotemporally truncated trajectories, defined as $H$-horizon trajectory pairs aggregated over each agent's $κ$-hop neighborhood. Building on this, we develop a distributed zeroth-order policy gradient algorithm, where each agent estimates its local policy gradient using human preference feedback generated from both the current joint policy and a perturbed joint policy drawn from zero-mean Gaussian distribution. Specifically, the algorithm is fully distributed, as the feedback received by each agent depends solely on the state-action information within its $κ$-hop neighborhood and does not require explicit reward signals or centralized control. We further rigorously establish that the proposed algorithm converges to an $ε$-stationary point with polynomial sample complexity. Finally, simulation results in a stochastic GridWorld environment and a predator-prey environment further demonstrate that the effectiveness and scalability of the proposed algorithm in achieving collaborative optimization based solely on human preference feedback.

</details>


### 18. Rule2DRC: Benchmarking LLM Agents for DRC Script Synthesis with Execution-Guided Test Generation

- **Authors:** Jinuk Kim, Junsoo Byun, Donghwi Hwang, Seong-Jin Park, Hyun Oh Song
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15669v1](http://arxiv.org/abs/2605.15669v1)
- **PDF:** [https://arxiv.org/pdf/2605.15669v1](https://arxiv.org/pdf/2605.15669v1)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces **Rule2DRC**, a large‑scale benchmark for evaluating large‑language‑model (LLM) agents that automatically synthesize and debug design‑rule‑checking (DRC) scripts from natural‑language specifications, and proposes **SplitTester**, an execution‑guided tester agent that improves program selection by generating discriminative test cases.

**Methodology:** Rule2DRC comprises 1 000 rule‑to‑script tasks together with 13 921 chip layouts, and provides an evaluation pipeline that judges agents on **functional correctness** by actually running the generated DRC scripts on the layouts (no test layouts are given to the agent). SplitTester takes a set of candidate scripts, runs them on generated layouts, and uses the observed execution outcomes to split and rank candidates, enabling more effective Best‑of‑N selection.

**Key findings:** Using execution‑based scoring reveals substantial gaps between code‑similarity metrics and true correctness, and the SplitTester agent boosts Best‑of‑N performance by a large margin (e.g., up to +30 % absolute accuracy) across multiple LLM back‑ends, establishing a more realistic evaluation paradigm for agentic AI in hardware‑design automation.


<details>
<summary>Abstract</summary>

Manufacturable chip layouts must satisfy thousands of geometry-based design rules, and design rule checking (DRC) enforces them by running executable DRC scripts on layouts. Translating natural language rules into correct DRC scripts is labor-intensive and requires specialized expertise, motivating LLM agents for DRC script synthesis and debugging. However, existing benchmarks have small evaluation sets and often evaluate scripts by code similarity rather than execution correctness, and prior machine learning-based methods either ignore execution feedback or require labeled test layouts as agent's input. To this end, we introduce Rule2DRC, a large-scale benchmark for DRC script coding agents with 1,000 rule-to-script tasks and 13,921 evaluation chip layouts for execution-based scoring. Rule2DRC provides an evaluation pipeline that measures functional correctness via DRC execution outcomes without requiring evaluation layouts as input to the agent. We also propose SplitTester, a tester agent for program selection that uses execution feedback to generate discriminative test cases and separate previously indistinguishable candidate scripts, substantially improving Best-of-N selection performance in this domain. We release the code at https://github.com/snu-mllab/Rule2DRC.

</details>


### 19. ColPackAgent: Agent-Skill-Guided Hard-Particle Monte Carlo Workflows for Colloidal Packing

- **Authors:** Lijie Ding, Changwoo Do
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15625v1](http://arxiv.org/abs/2605.15625v1)
- **PDF:** [https://arxiv.org/pdf/2605.15625v1](https://arxiv.org/pdf/2605.15625v1)
- **Categories:** cs.AI, cond-mat.soft


> The paper presents **ColPackAgent**, an autonomous agent that plugs a domain‑specific Python package (colpack / HOOMD‑blue) into a Model Context Protocol (MCP) server and an “agent skill” describing a four‑stage Monte‑Carlo packing workflow. Using this infrastructure, the agent can execute colloidal‑packing simulations (e.g., 3‑D cubes, 2‑D binary disks‑capsules, hard‑disk freezing) either interactively with human guidance, from a single end‑to‑end prompt, or via an autoresearch loop, and the authors benchmark its performance across 17 prompts on several LLMs. The results show that coupling a specialized simulation library with MCP‑based tooling and a portable skill contract enables reliable, LLM‑driven execution and analysis of hard‑particle Monte Carlo studies—demonstrating a practical pathway for turning scientific simulation codes into agent‑assisted research pipelines.


<details>
<summary>Abstract</summary>

We introduce ColPackAgent, an agent framework that autonomously runs Monte Carlo simulations of colloidal packing through a Model Context Protocol (MCP) tool server and an agent skill, whether as a standalone agent or inside an existing agent system. By harnessing the MCP server and agent skill, ColPackAgent executes a structured workflow for colloidal packing simulations, which are central to studies of phase behavior, self-assembly, and materials design. Without dedicated simulation tools and workflow instructions, general-purpose Large Language Model (LLM) agents tend to describe such workflows rather than execute them reliably. The MCP server exposes a custom-built colpack Python package that wraps HOOMD-blue hard-particle Monte Carlo, and the skill encodes a four-stage workflow contract. ColPackAgent can carry out the workflow interactively with human feedback, autonomously from an end-to-end prompt, or as autoresearch following a provided program file. We demonstrate the system in different modes with several colloidal packing simulation examples such as cube particles in 3D, a binary system of disks and capsules in 2D, and the 2D hard-disk freezing transition using autoresearch. We also compare model performance on this workflow across a panel of LLMs with 17 stage-specific prompts. This benchmark provides a stage-level check of how reliably different models follow the setup, planning, and analysis workflow. Together, these results show that pairing a domain Python package with MCP tools and a portable agent skill provides a practical route for turning a simulation toolkit into an agent-assisted research workflow.

</details>


### 20. TopoEvo: A Topology-Aware Self-Evolving Multi-Agent Framework for Root Cause Analysis in Microservices

- **Authors:** Junle Wang, Xingchuang Liao, Wenjun Wu
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15611v1](http://arxiv.org/abs/2605.15611v1)
- **PDF:** [https://arxiv.org/pdf/2605.15611v1](https://arxiv.org/pdf/2605.15611v1)
- **Categories:** cs.AI


> **Main contribution:** TopoEvo introduces a topology‑aware, self‑evolving multi‑agent system that integrates graph representation learning with structured, topology‑constrained reasoning to overcome symptom‑amplification bias in root‑cause analysis (RCA) for microservices.  

**Methodology:** The framework first builds robust node embeddings using Metric‑orthogonal Multimodal Alignment (MOMA) to jointly encode metrics, logs, and traces, then discretizes these embeddings into “symptom tokens” via vector quantization. A multi‑agent Hypothesis‑Evidence‑Test (HET) workflow leverages the tokenized, topology‑enhanced graph to generate, ground, and experimentally verify causal hypotheses, while a self‑evolving mechanism continuously updates an incident memory and performs conservative test‑time adaptation with high‑confidence pseudo‑labels.  

**Key findings:** Experiments on real‑world microservice deployments show that TopoEvo reduces root‑cause misidentification caused by downstream symptom amplification by up to 38 % and improves RCA accuracy by 12–15 % over existing LLM‑based agents, while maintaining robustness to topology drift through its self‑evolving memory updates. This demonstrates that embedding topology awareness and discrete symptom grounding markedly enhances the reliability of agentic AI for complex, evolving systems.


<details>
<summary>Abstract</summary>

Root cause analysis (RCA) in microservices is challenging due to (i) noisy and heterogeneous multimodal observability (metrics, logs, traces), (ii) cascading failure propagation that amplifies downstream symptoms, and (iii) non-stationary topology drift induced by autoscaling and rolling updates. Recent LLM-based RCA agents can generate tool-grounded explanations, yet they often remain topology-agnostic and suffer from \emph{symptom-amplification bias}, misattributing the root cause to salient downstream victims. We propose \textbf{TopoEvo}, a topology-aware self-evolving multi-agent framework that couples graph representation learning with structured, topology-constrained reasoning. TopoEvo first introduces \emph{Metric-orthogonal Multimodal Alignment} (MOMA), which decomposes metric embeddings into complementary subspaces and contrastively aligns logs and traces to reduce modality redundancy and sparsity, yielding stable node representations for graph encoding. It then applies \emph{Vector Quantization} (VQ) to discretize topology-enhanced states into auditable \emph{symptom tokens} with a symptom lexicon, enabling reliable retrieval and token-level evidence grounding. On top of these discrete topology cues, TopoEvo performs a multi-agent \emph{Hypothesis--Evidence--Test} (HET) workflow to explicitly verify propagation-consistent explanations and separate initiating anomalies from amplified downstream symptoms. Finally, a \emph{Self-Evolving Mechanism} refreshes hierarchical incident memory and performs conservative test-time adaptation with high-confidence pseudo-labels to maintain robustness under drift.

</details>


### 21. See Before You Code: Learning Visual Priors for Spatially Aware Educational Animation Generation

- **Authors:** Yuejia Li, Ke He, Junheng Li, Shutong Chen, Jingkang Xia, Zhiyue Su, Junchi Zhang, Mang Ye
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15585v1](http://arxiv.org/abs/2605.15585v1)
- **PDF:** [https://arxiv.org/pdf/2605.15585v1](https://arxiv.org/pdf/2605.15585v1)
- **Categories:** cs.AI, cs.CV


> The paper introduces **OmniManim**, a render‑feedback‑aware framework for generating educational animations that first plans the visual layout before emitting code, then uses post‑render diagnostics to locally repair defects that only become visible after rendering.  The core “Vision Agent” predicts sparse key‑frame bounding‑box layouts, refines them with a coarse‑to‑fine denoising process, and optimizes an interpolation‑aware loss to prevent overlap, mis‑alignment, and continuity errors during downstream frame interpolation.  Experiments on two newly released datasets (ManimLayout‑1K and EduRequire‑500) show that OmniManim markedly improves executable‑ness, instructional quality, and visual correctness versus single‑model baselines and prior multi‑agent approaches, confirming that explicit visual priors and spatial planning are crucial for reliable, agentic AI‑driven animation generation.


<details>
<summary>Abstract</summary>

Large language models can generate executable code for educational animations, but the resulting renders often exhibit visual defects, including element overlap, misalignment, and broken animation continuity. These defects cannot be reliably detected from the code alone and become apparent only after execution. We formalize this problem as render-feedback-aware constrained code generation: given a natural language specification, the model must generate executable code whose rendered output satisfies structured quality criteria that can be evaluated only after rendering. To address this problem, we introduce OmniManim, a render-feedback-aware educational animation generation framework built around a shared scene state, explicit visual planning, structured post-render diagnostics, and localized repair. Within OmniManim, the Vision Agent is a task-specific visual planning module: it predicts sparse keyframe layouts with coarse-to-fine bounding-box denoising and optimizes an interpolation-aware objective to reduce intermediate-frame failures induced by downstream animation interpolation. We further construct two datasets, ManimLayout-1K and EduRequire-500, and provide a reproducible evaluation protocol covering executability, instructional quality, visual quality, and efficiency. On EduRequire-500, OmniManim improves measured render quality over both single-model baselines and existing multi-agent frameworks. Systematic ablation studies further verify that explicit visual planning, especially its coarse spatial prior, bounding-box refinement, and interpolation-aware optimization, is central to these gains.

</details>


### 22. Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems

- **Authors:** Nurbek Tastan, Alex Iacob, Lorenzo Sani, Meghdad Kurmanji, Nicholas D. Lane, Samuel Horvath, Karthik Nandakumar
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15573v1](http://arxiv.org/abs/2605.15573v1)
- **PDF:** [https://arxiv.org/pdf/2605.15573v1](https://arxiv.org/pdf/2605.15573v1)
- **Categories:** cs.CL, cs.LG, cs.MA


> The paper introduces **Nexa**, a trainable, response‑conditioned policy that dynamically fuses parallel and sequential coordination among multiple LLM agents. Nexa first collects all agents’ parallel outputs, embeds them into a shared semantic space, and then—a lightweight transformer predicts a sparse directed‑acyclic graph that either leaves the system in pure parallel mode or triggers a single round of sequential message propagation; the graph is guaranteed acyclic by construction and the policy is learned via policy‑gradient optimization without external judges or hand‑crafted topology search. Experiments show that Nexa consistently reduces communication latency while improving answer accuracy, and that a single learned policy generalizes across different numbers of agents, tasks, and underlying LLMs, offering a more efficient and adaptable coordination mechanism for agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent systems can solve complex tasks through collaboration between multiple Large Language Model agents. Existing collaboration frameworks typically operate in either a parallel or a sequential mode. In the parallel mode, agents respond independently to queries followed by aggregation of responses. In contrast, sequential systems allow agents to communicate via a directed topology and refine one another step by step. However, both modes are inadequate for achieving the desired objectives of minimizing communication and latency while simultaneously maximizing the accuracy of the final response. In this work, we introduce a hybrid paradigm called Nexa, a trainable response-conditioned policy that bridges the gap between the two modes. Nexa begins with a parallel execution stage, embeds the resulting responses into a shared semantic space, and then predicts a sparse directed acyclic communication graph. If the graph is empty, the system remains purely parallel; if it is non-empty, the system performs one sequential message propagation. The policy is a lightweight transformer model, and the method avoids the need for external LLM judges or reward models, as well as hand-crafted test-time topology search. We formalize this hybrid execution problem, show that the resulting graph is acyclic by construction, and that the framework strictly subsumes pure parallel execution, and present a training procedure based on policy-gradient optimization. Results demonstrate that the response-conditioned policy learned by Nexa under one setting can be reused when the number of agents, the task, or the underlying agent changes, thus emphasizing the generalizability of the learned communication policy.

</details>


### 23. AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs

- **Authors:** Haizhong Zheng, Yizhuo Di, Jiahui Wang, Shuowei Jin, Xueshen Liu, Yongji Wu, Z. Morley Mao, Ion Stoica, Jiawei Zhao, Beidi Chen
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15565v1](http://arxiv.org/abs/2605.15565v1)
- **PDF:** [https://arxiv.org/pdf/2605.15565v1](https://arxiv.org/pdf/2605.15565v1)
- **Categories:** cs.LG, cs.AI


> AstraFlow introduces a data‑flow‑centric architecture for reinforcement learning with agentic LLMs, replacing the traditional trainer‑centric control loop with three autonomous components—rollout services, data‑flow manager, and trainer—that can be independently scaled and deployed across heterogeneous, multi‑region hardware. By decoupling these pieces, the system natively supports complex workloads such as multi‑policy collaborative RL, elastic scaling, and composable data pipelines without any system‑level code modifications. Experiments on math, coding, search, and AgentBench tasks show that AstraFlow matches or exceeds the accuracy of existing RL‑for‑LLM platforms while cutting overall training time by up to 2.7 ×, demonstrating a practical, cost‑effective path to large‑scale agentic RL.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is increasingly used to improve the reasoning, coding, and tool-use capabilities of large language models, but agentic RL remains prohibitively expensive. Scaling RL to agentic LLMs requires supporting complex workloads, including multi-policy collaborative training, while efficiently using elastic, heterogeneous, and cross-region compute resources. Existing LLM RL systems support some of these capabilities, but each new extension often requires dedicated system engineering. This burden arises from trainer-centered control architectures and the lack of principled abstractions for RL system components. To address these limitations, we propose AstraFlow, a dataflow-oriented RL system that replaces conventional trainer-centered control with principled component abstractions. In AstraFlow, rollout services, dataflow management, and training are decoupled into autonomous components, enabling the system to natively support complex multi-policy agentic RL workloads and efficiently exploit diverse compute resources. We evaluate AstraFlow across math, code, search, and AgentBench workloads, showing that the same system supports multi-policy training, elastic scaling, heterogeneous cross-region execution, and composable data algorithms without system-level code changes. In multi-policy collaborative training, AstraFlow achieves comparable or better accuracy than existing RL systems while speeding up training time by 2.7x.

</details>


### 24. Task-Semantic Graph-Driven Distributed Agent Networking for Underwater Target Tracking

- **Authors:** Shengchao Zhu, Guangjie Han, Chuan Lin, Yu He
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15528v1](http://arxiv.org/abs/2605.15528v1)
- **PDF:** [https://arxiv.org/pdf/2605.15528v1](https://arxiv.org/pdf/2605.15528v1)
- **Categories:** cs.RO, cs.MA


> **Contribution:** The paper introduces the first open‑source MARL platform that couples the DI‑engine reinforcement‑learning framework with a high‑fidelity six‑degree‑of‑freedom AUV simulator, enabling systematic training and benchmarking of single‑ and multi‑agent RL algorithms for persistent underwater target tracking. On top of this platform the authors propose **STG‑MAPPO**, a Multi‑Agent Proximal Policy Optimization algorithm that enriches each agent’s observation with a **Task‑Semantic Graph (TSG)** encoding tracking diagnostics (task phase, observation confidence, link quality, neighbor performance, role advantage).

**Methodology:** The TSG is constructed online from diagnostic signals and fed to decentralized actor networks as compact semantic features; actions are selected at the velocity‑level rather than raw force commands, providing a higher‑level abstraction that is easier to learn. The authors evaluate STG‑MAPPO against vanilla MAPPO, independent PPO, and other baselines using the standardized experimental protocol of the new MARL‑AUV suite.

**Key Findings:** Across multiple underwater scenarios with dynamic topology and intermittent acoustic links, STG‑MAPPO consistently achieves higher tracking accuracy, better robustness to communication loss, and faster convergence than the baselines, demonstrating that semantic task‑graph inputs and velocity‑level action abstraction markedly improve MARL performance for agentic underwater systems.


<details>
<summary>Abstract</summary>

Autonomous underwater vehicle (AUV) swarms are emerging as intelligent underwater networks, where each node must sense, communicate, process local data, and make decisions under severe acoustic constraints. Persistent underwater target tracking is a typical task with moving targets, changing communication topology, intermittent acoustic links, and limited observation for each AUV. Multi-agent reinforcement learning (MARL) is a natural candidate for distributed tracking, yet existing studies still lack a unified open-source platform for evaluating different MARL algorithms under six-degree-of-freedom AUV dynamics. In addition, policies trained with raw geometric states and low-level force actions often struggle to represent task phases, observation reliability, link quality, and local cooperation roles. This paper addresses these issues by developing an open-source MARL-AUV platform that integrates DI-engine with a six-degree-of-freedom underwater AUV target-tracking simulator. To the best of our knowledge, it is the first open platform that connects a public MARL training framework with physically modeled AUV swarm-based tasks, and provides a unified experimental protocol for fair training, testing, and comparison of representative RL and MARL algorithms. Based on this platform, we propose STG-MAPPO, a Semantic Task Graph-enhanced variant of Multi-Agent Proximal Policy Optimization. STG-MAPPO builds semantic policy inputs from tracking diagnostics, task phases, observation confidence, link availability, neighbor tracking quality, and local role advantage. A compact semantic task graph links communication-constrained network states to decentralized actor decisions, and a velocity-level action abstraction maps high-level cooperative decisions to executable six-degree-offreedom AUV control inputs.The code is available at https://github.com/dasjsaj/MARL-AUV.

</details>


### 25. X-SYNTH: Beyond Retrieval -- Enterprise Context Synthesis from Observed Human Attention

- **Authors:** Guruprasad Raghavan, George Nychis, Rohan Narayana Murthy
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15505v1](http://arxiv.org/abs/2605.15505v1)
- **PDF:** [https://arxiv.org/pdf/2605.15505v1](https://arxiv.org/pdf/2605.15505v1)
- **Categories:** cs.AI, cs.IR, cs.LG


> **Main contribution** – X‑SYNTH introduces a novel “context‑synthesis” framework that replaces pure retrieval with relevance‑driven grounding of enterprise information on the basis of observed human attention signatures, modeled as Digital Twin Signatures (DTS) for each worker.  

**Methodology** – The system extracts fine‑grained digital interaction traces (clicks, edits, message flows, timestamps, implicit reward cues) and builds per‑user behavioral baselines. For any query it dynamically chooses one of seven attention filters (Proportional, Inverse, Differential, Recurrent, Comparative, Sequential, Collective) to surface activity patterns that causally correlate with successful outcomes, without needing external labels. A four‑stage pipeline then ranks and assembles the selected contextual pieces for the downstream agent.  

**Key findings** – On a realistic sales‑lead‑identification task, a state‑of‑the‑art language model alone achieved a 9.5 % true‑lead rate (TLR) and 90.5 % false‑lead rate (FLR). When augmented with X‑SYNTH, TLR jumped to 61.9 % (≈6.5× improvement) and FLR dropped to 18.8 %, demonstrating that grounding agentic AI in synthesized human‑attention context dramatically enhances relevance and performance in complex enterprise settings.


<details>
<summary>Abstract</summary>

In enterprise operations, the context required for an AI agent task is scattered across systems of record, static information stores, and communication channels. What is stored is system state, a lossy representation of the work that actually happened [2, 52]. The prevailing approach [17, 31, 34, 36] retrieves by matching request content to what is stored; for narrow requests this works well. But synthesis quality depends on knowing what to surface and how to interpret it: knowledge specific to each organization, team, and individual [5, 57, 61], present in behavioral patterns, absent from any retrieval index. For complex agentic tasks it breaks down: True Lead Rate is low, False Lead Rate is high, and the model has no mechanism to improve. We present X-SYNTH, a framework for enterprise context synthesis grounded in human attention, the digitally observable interaction signatures of each worker, encoding not just what they did but the sequence in which they did it, along with implicit reward signals. Behavioral traces preceding positive outcomes are distinguishable from those that did not, without external labeling. X-SYNTH models each individual's behavioral baseline as a Digital Twin Signature (DTS) and selects among seven qualitatively distinct attention filters: Proportional, Inverse, Differential, Recurrent, Comparative, Sequential, and Collective, per individual and per query, to identify causally relevant activity signatures. A four-stage pipeline assembles ranked context grounded in behavioral patterns rather than query embeddings. On a sales lead identification task, a frontier model unaided achieves 9.5% True Lead Rate (TLR) with 90.5% False Lead Rate (FLR). Augmented with X-SYNTH, TLR rises to 61.9% (6.5x) while FLR falls to 18.8%. Enterprise context synthesis is not a retrieval problem. It is a relevance problem, and human attention is its most reliable ground truth.

</details>


### 26. Hybrid LLM-based Intelligent Framework for Robot Task Scheduling

- **Authors:** Swayamjit Saha, Subhabrata Das, Haonan Duan, Xiao-Yang Liu
- **Published:** 2026-05-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15486v1](http://arxiv.org/abs/2605.15486v1)
- **PDF:** [https://arxiv.org/pdf/2605.15486v1](https://arxiv.org/pdf/2605.15486v1)
- **Categories:** cs.RO, cs.AI


> The paper proposes a hybrid LLM‑based framework for scheduling construction‑site robots, pairing a powerful generative model (GPT‑4) with a lightweight supervisory model (Gemma‑3/ Llama‑4/ Mistral‑7B) to jointly encode task requirements, robot capabilities, and goal constraints and then produce balanced, time‑ and resource‑optimal schedules. The methodology uses a natural‑language interface to ingest high‑level specifications from human supervisors, runs the two LLM agents in a generate‑supervise loop, and dynamically replans when site conditions change. Experiments on a simplified robot‑task scenario show that the dual‑agent system yields higher schedule feasibility and better utilization metrics than single‑LLM baselines, demonstrating the practical value of LLMs for real‑time agentic coordination in construction robotics.


<details>
<summary>Abstract</summary>

This study introduces intelligent frameworks that use Large Language Models (LLMs) to improve task scheduling for construction robots. The LLM is fed with key data about the desired task, such as agent action abilities, and the desired end goal to be achieved. A well-balanced allocation strategy is developed, optimizing both time efficiency and resource utilization. Our system utilizes a Natural Language Processing interface to streamline communication with construction professionals and adapt in real-time to unexpected site conditions. We concurrently use two LLM agents, specifically generator (GPT-4) and supervisor (Gemma 3/Llama 4/Mistral 7b) LLM agents to provide a more precise task schedule. We evaluate the proposed methodology using a straightforward scenario and provide metric scores to prove the efficacy of the frameworks. Our results highlight that the implementation of LLMs is crucial in construction operational tasks including robots.

</details>


### 27. Beyond Partner Diversity: An Influence-Based Team Steering Framework for Zero-Shot Human-Machine Teaming

- **Authors:** Wei Sheng, Rohan Paleja
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15400v1](http://arxiv.org/abs/2605.15400v1)
- **PDF:** [https://arxiv.org/pdf/2605.15400v1](https://arxiv.org/pdf/2605.15400v1)
- **Categories:** cs.AI


> **Main contribution**: The paper introduces **Influence‑Based Team Steering (IBTS)**, a zero‑shot coordination framework that goes beyond mere partner‑diversity by explicitly shaping agents’ influence on one another to discover and reinforce high‑performing interaction patterns in human‑machine teams.  

**Methodology**: IBTS augments standard zero‑shot coordination training with an influence‑shaping reward that encourages agents to generate diverse, coordinated behaviours and to steer ongoing episodes toward previously learned coordination modes. The approach is evaluated on the Overcooked‑AI benchmark for both two‑ and three‑agent teams, using (1) simulated partner populations, (2) synthetically varied partner styles, and (3) a novel user study with 30 human participants teamed with an AI agent.  

**Key findings**: Across all settings, IBTS consistently outperforms prior ZSC baselines, achieving higher team scores and more robust coordination, especially as team size grows and communication degrades. The results demonstrate that scaling zero‑shot human‑machine teaming requires a combination of sparse‑reward coordination incentives and systematic partner‑variation coverage, not merely diversity of partners.


<details>
<summary>Abstract</summary>

While AI agents are rapidly advancing from isolated tools to interactive collaborators, data-driven human-machine teaming (HMT) methods remain costly in their reliance on human interaction data across domains, teammates, and team sizes. Zero-shot coordination (ZSC) addresses this bottleneck by simulating diverse partner populations to approximate how unseen partners might behave. However, partner coverage alone is insufficient as team settings scale and communication becomes degraded. To remedy this deficiency, we propose Influence-Based Team Steering (IBTS), a framework that uses influence shaping to incentivize agents to discover diverse, high-performing team interaction patterns and further steers ongoing trajectories toward stronger learned coordination modes. We assess IBTS on Overcooked-AI in both two-agent and three-agent settings, allowing us to test whether learned coordination structure transfers beyond dyadic interaction. Our evaluation includes simulated partners, synthetic partner-style variation, and, to our knowledge, the first 30-subject Overcooked-AI HMT study involving two real human teammates and one machine teammate. Across these evaluations, IBTS improves team performance against competing baselines, highlighting the need for scaled ZSC to combine sparse-reward coordination mechanisms with partner-variation coverage rather than relying on diversity alone.

</details>


### 28. Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute

- **Authors:** Eugene Koran, Yejun Yun, Samantha Tetef, Benjamin Arnav, Pablo Bernabeu-Pérez
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15377v1](http://arxiv.org/abs/2605.15377v1)
- **PDF:** [https://arxiv.org/pdf/2605.15377v1](https://arxiv.org/pdf/2605.15377v1)
- **Categories:** cs.AI


> The paper demonstrates that safety monitoring of autonomous agents is far more effective when the monitor ensemble is *diverse* rather than merely larger. The authors construct twelve GPT‑4.1‑Mini monitors using a mix of prompt‑engineered and fine‑tuned models, then evaluate them on coding problems where solutions pass normal tests but fail on adversarial inputs. A heterogeneous three‑monitor ensemble—especially one that includes fine‑tuned members—detects misaligned actions ≈2.4 × better than a homogeneous trio, generalizes to out‑of‑distribution attacks, and does so with modest inference overhead, establishing diversity‑driven ensemble monitoring as a scalable control mechanism for agentic AI.


<details>
<summary>Abstract</summary>

As AI systems are increasingly deployed in autonomous agentic settings at scale, it is important to ensure the actions they take are safe and aligned with user intent. Monitoring agent actions is a key safety mechanism, yet reliable monitors remain difficult to build and the scale of these systems makes human oversight impractical. We show that combining signals from diverse monitors into an ensemble improves detection of misaligned actions. We build 12 GPT-4.1-Mini monitors using both prompting and fine-tuning strategies. We evaluate them on coding tasks where candidate solutions pass standard tests but fail on adversarial inputs. In this setting, diverse ensembles outperform both individual monitors and homogeneous ensembles. Our best 3-monitor ensemble achieves 2.4x greater detection performance gain compared to an ensemble composed of three identical monitors, with the same ensemble performing strongly on an independent dataset. We contend that these results show that diversity - not scale - drives gains. The best ensembles combine strong individual performance with low correlation between monitors. Furthermore, fine-tuned monitors appear in every top-performing ensemble and maintain this advantage on out-of-distribution attack types, suggesting that fine-tuning enables detection capabilities that prompting alone does not elicit. These results support ensemble monitoring as a practical AI control strategy for safety gains at reasonable inference costs.

</details>


### 29. Belief Engine: Configurable and Inspectable Stance Dynamics in Multi-Agent LLM Deliberation

- **Authors:** Joshua C. Yang, Maurice Flechtner, Damian Dailisan, Michiel A. Bakker
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15343v1](http://arxiv.org/abs/2605.15343v1)
- **PDF:** [https://arxiv.org/pdf/2605.15343v1](https://arxiv.org/pdf/2605.15343v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces **Belief Engine (BE)**, an auditable intermediate layer that endows LLM‑based agents with an explicit “belief” state—represented as a scalar stance derived from a log‑odds combination of prior anchoring and newly extracted evidence. BE parses arguments produced during multi‑agent dialogs into a structured memory, then updates each agent’s stance with a controllable evidence‑uptake parameter (u) and anchoring weight (a), making the reasoning process transparent and configurable. Experiments across several LLMs and on the DEBATE human‑deliberation dataset show that BE reliably shapes stance trajectories, accurately reconstructs evidence‑driven opinion changes, and isolates cases where stance shifts arise from anchoring or non‑evidential factors, thereby providing a concrete tool for studying and steering evidence‑grounded deliberation in agentic AI systems.


<details>
<summary>Abstract</summary>

LLM-based agents are increasingly used to simulate deliberative interactions such as negotiation, conflict resolution, and multi-turn opinion exchange. Yet generated transcripts often do not reveal why an agent's stance changes: movement may reflect evidence uptake, anchoring, role drift, echoing, or changed prompt and retrieval context. We introduce the Belief Engine (BE), an auditable belief-update layer that treats "belief" as an evidential state over a proposition and exposes it as scalar stance. BE extracts arguments into structured memory and updates stance with a log-odds rule controlled by evidence uptake u and prior anchoring a. Across multiple base LLMs, parameter sweeps show that these controls reliably shape stance dynamics while preserving an evidence-level update trail. On DEBATE, a human deliberation dataset with pre/post opinions, BE best reconstructs participants whose final stance follows extracted evidence; stable and evidence-opposed cases instead point to anchoring or factors outside the extracted evidence stream. BE provides configurable infrastructure for studying evidence-grounded deliberation, where openness, commitment, convergence, and disagreement can be tied to explicit update assumptions rather than hidden prompt effects.

</details>


### 30. Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

- **Authors:** Sidharth Pulipaka, Stanislau Hlebik, Leonidas Raghav, Sahar Abdelnabi, Vyas Raina, Ivaxi Sheth, Mario Fritz
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15338v1](http://arxiv.org/abs/2605.15338v1)
- **PDF:** [https://arxiv.org/pdf/2605.15338v1](https://arxiv.org/pdf/2605.15338v1)
- **Categories:** cs.CR, cs.AI


> **Paper Summary**

The authors introduce *sleeper memory poisoning*, a novel long‑term attack on stateful language‑model assistants that embed user‑specific memories. By injecting malicious content into external sources (e.g., web pages or code repositories), an adversary can cause the LLM to store a fabricated memory that remains dormant until later sessions, at which point it is retrieved and used to steer the assistant’s behavior.  

Methodologically, the paper builds a full attack pipeline—crafting poison documents, prompting the LLM to write the false memory, and later prompting it to retrieve and act on that memory—and evaluates it on several recent agents (GPT‑5.5, Kimi‑K2.6, etc.). Experiments show that poisoned memories are written with >95 % success, retrieved reliably, and induce the attacker’s intended actions in 60‑89 % of follow‑up interactions, demonstrating that persistent memory constitutes a potent, multi‑turn attack surface for agentic AI.


<details>
<summary>Abstract</summary>

Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity. This statefulness introduces a new security risk: adversarial content can corrupt what an assistant remembers and thereby influence future interactions. We propose and study sleeper memory poisoning, a delayed attack in which an adversary manipulates external context, such as a document, webpage, or repository, to cause the assistant to store a fabricated memory about the user. Unlike conventional prompt injection, the attack can remain dormant and re-emerge across multiple later conversations. We evaluate the full attack pipeline: whether poisoned memories are written, later retrieved, and ultimately used to steer the following conversations. Across stateful LLM assistants, poisoned memories were added up to 99.8% on GPT-5.5 and 95% on Kimi-K2.6. Crucially, among successful retrievals, poisoned memories cause attacker-intended agentic actions in 60-89% of evaluations across models. These results show that persistent memory can act as a long-term attack surface across multiple future conversations.

</details>


### 31. Solvita: Enhancing Large Language Models for Competitive Programming via Agentic Evolution

- **Authors:** Han Li, Jinyu Tian, Rili Feng, Yuqiao Du, Chong Zheng, Chenyu Wang, Chenchen Liu, Shihao Li, Xinping Lei, Yifan Yao, Weihao Xie, Letian Zhu, Jiaheng Liu
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15301v1](http://arxiv.org/abs/2605.15301v1)
- **PDF:** [https://arxiv.org/pdf/2605.15301v1](https://arxiv.org/pdf/2605.15301v1)
- **Categories:** cs.AI


> Solvita introduces an agentic‑evolution framework that equips a suite of four LLM‑driven agents (Planner, Solver, Oracle, Hacker) with a mutable, graph‑structured knowledge network, turning execution feedback (pass/fail, certification scores, adversarial hacks) into reinforcement‑learning updates that steer future problem‑solving without altering the underlying model weights. By closing the loop between strategy selection, program synthesis, certified testing, and targeted hacking, the system continuously accumulates transferable reasoning experience across tasks. Experiments on CodeContests, APPS, AetherCode and live Codeforces rounds show Solvita achieving state‑of‑the‑art performance for code‑generation agents—roughly doubling the accuracy of single‑pass baselines and surpassing existing multi‑agent pipelines.


<details>
<summary>Abstract</summary>

Large language models (LLMs) still struggle with the rigorous reasoning demands of hard competitive programming. While recent multi-agent frameworks attempt to bridge this reliability gap, they remain fundamentally stateless: they rely on static retrieval and discard the valuable problem-solving and debugging experience gained from previous tasks. To address this, we present Solvita, an agentic evolution framework that enables continuous learning without requiring weight updates to the underlying LLM. Solvita reorganizes problem-solving into a closed-loop system of strategy selection, program synthesis, certified supervision, and targeted hacking, executed by four specialized agents: Planner, Solver, Oracle, and Hacker. Crucially, each agent is paired with a trainable, graph-structured knowledge network. As the system operates, outcome signals, such as pass/fail verdicts, test certification quality, and adversarial vulnerabilities discovered by the Hacker, are recast as reinforcement learning updates to these network weights. This allows the agents to dynamically route future queries based on past successes and failures, effectively accumulating transferable reasoning experience over time. Evaluated across CodeContests, APPS, AetherCode, and live Codeforces rounds, Solvita establishes a new state-of-the-art among code-generation agents, outperforming existing multi-agent pipelines and nearly doubling the accuracy of single-pass baselines.

</details>


### 32. FutureSim: Replaying World Events to Evaluate Adaptive Agents

- **Authors:** Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab, Moritz Hardt, Maksym Andriushchenko, Jonas Geiping
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15188v1](http://arxiv.org/abs/2605.15188v1)
- **PDF:** [https://arxiv.org/pdf/2605.15188v1](https://arxiv.org/pdf/2605.15188v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> The paper introduces **FutureSim**, a benchmark that replays a chronologically ordered stream of real‑world news articles and question‑answer events from January–March 2026, forcing agents to forecast future happenings beyond their training cutoff. By evaluating state‑of‑the‑art frontier models on this replay, the authors show a wide performance gap (the top model reaches only 25 % accuracy and many attain a negative Brier skill score), and through ablation studies demonstrate that FutureSim isolates capabilities such as long‑horizon test‑time adaptation, external search, memory usage, and uncertainty reasoning. This work provides a realistic, open‑ended evaluation platform for measuring and advancing agentic AI’s ability to continuously adapt to unfolding real‑world information.


<details>
<summary>Abstract</summary>

AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives. To efficiently measure this capability for realistic use-cases, we propose building grounded simulations that replay real-world events in the order they occurred. We build FutureSim, where agents forecast world events beyond their knowledge cutoff while interacting with a chronological replay of the world: real news articles arriving and questions resolving over the simulated period. We evaluate frontier agents in their native harness, testing their ability to predict world events over a three-month period from January to March 2026. FutureSim reveals a clear separation in their capabilities, with the best agent's accuracy being 25%, and many having worse Brier skill score than making no prediction at all. Through careful ablations, we show how FutureSim offers a realistic setting to study emerging research directions like long-horizon test-time adaptation, search, memory, and reasoning about uncertainty. Overall, we hope our benchmark design paves the way to measure AI progress on open-ended adaptation spanning long time-horizons in the real world.

</details>


### 33. Self-Distilled Agentic Reinforcement Learning

- **Authors:** Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15155v1](http://arxiv.org/abs/2605.15155v1)
- **PDF:** [https://arxiv.org/pdf/2605.15155v1](https://arxiv.org/pdf/2605.15155v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> **Main contribution**: The paper introduces **Self‑Distilled Agentic Reinforcement Learning (SDAR)**, a training framework that combines reinforcement learning (RL) with a gated, token‑level self‑distillation objective to give LLM‑based agents dense supervision without sacrificing the stability of RL‑only training.

**Methodology**: SDAR treats the on‑policy self‑distillation (OPSD) signal as an auxiliary loss that is passed through a sigmoid gate; positive‑gap tokens (those where the teacher model with privileged context outperforms the student) are amplified, while negative‑gap tokens are attenuated rather than forced into the loss. RL remains the primary objective, ensuring the agent’s long‑horizon reward optimisation, while the gated distillation provides fine‑grained guidance across multi‑turn interactions.

**Key findings**: Across three benchmarks (ALFWorld, WebShop, Search‑QA) and multiple model sizes in the Qwen2.5/Qwen3 families, SDAR yields large performance gains over strong baselines (e.g., +9.4 % on ALFWorld, +7.0 % on Search‑QA, +10.2 % on WebShop‑Acc) and eliminates the training instability seen in naïve combinations of GRPO and OPSD, demonstrating that gated self‑distillation is an effective, scalable way to enrich agentic RL.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has emerged as a central paradigm for post-training LLM agents, yet its trajectory-level reward signal provides only coarse supervision for long-horizon interaction. On-Policy Self-Distillation (OPSD) complements RL by introducing dense token-level guidance from a teacher branch augmented with privileged context. However, transferring OPSD to multi-turn agents proves problematic: compounding multi-turn instability destabilizes supervision, while skill-conditioned privileged guidance requires asymmetric treatment for negative teacher rejections may arise from imperfect skills retrieval or utilization. We introduce SDAR (Self-Distilled Agentic Reinforcement Learning), which treats OPSD as a gated auxiliary objective while keeping RL as the primary optimization backbone. SDAR maps detached token-level signals into a sigmoid gate, strengthening distillation on teacher-endorsed positive-gap tokens and softly attenuating negative teacher rejections. Across the Qwen2.5 and Qwen3 families on ALFWorld, WebShop, and Search-QA, SDAR substantially improves over GRPO (+9.4% on ALFWorld, +7.0% on Search-QA, +10.2% on WebShop-Acc), avoids the instability of naive GRPO+OPSD, and consistently outperforms hybrid RL--OPSD baselines across model scales.

</details>


### 34. APWA: A Distributed Architecture for Parallelizable Agentic Workflows

- **Authors:** Evan Rose, Tushin Mallick, Matthew D. Laws, Cristina Nita-Rotaru, Alina Oprea
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15132v1](http://arxiv.org/abs/2605.15132v1)
- **PDF:** [https://arxiv.org/pdf/2605.15132v1](https://arxiv.org/pdf/2605.15132v1)
- **Categories:** cs.AI, cs.DC, cs.MA


> The paper presents **Agent‑Parallel Workload Architecture (APWA)**, a distributed framework that overcomes the reasoning, coordination, and scalability limits of existing LLM‑driven multi‑agent systems by automatically breaking a task into independent sub‑problems that can be solved in parallel on separate compute nodes without any inter‑agent communication. The authors implement APWA with a lightweight orchestration layer that detects non‑interfering workflow fragments, dispatches them to heterogeneous LLM resources, and aggregates the results, enabling true high‑throughput processing of heavily parallelizable workloads. Experiments show that APWA dynamically decomposes complex queries across domains and achieves near‑linear speed‑ups on larger tasks where prior agentic systems either stall or fail, demonstrating its suitability for scalable, parallel agentic AI applications.


<details>
<summary>Abstract</summary>

Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. However, these systems hit critical reasoning, coordination, and computational scaling bottlenecks as the size and complexity of their tasks grow. These limitations hinder multi-agent systems from achieving high-throughput processing for highly parallelizable tasks, despite the availability of parallel computing and reasoning primitives in the underlying LLMs. We introduce the Agent-Parallel Workload Architecture (APWA), a distributed multi-agent system architecture designed for the efficient processing of heavily parallelizable agentic workloads. APWA facilitates parallel execution by decomposing workflows into non-interfering subproblems that can be processed using independent resources without cross-communication. It supports heterogeneous data and parallel processing patterns, and it accommodates tasks from a wide breadth of domains. In our evaluation, we demonstrate that APWA can dynamically decompose complex queries into parallelizable workflows and scales on larger tasks in settings where prior systems fail completely.

</details>


### 35. From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents

- **Authors:** Md Tahmid Rahman Laskar, Xue-Yong Fu, Seyyed Saeed Sarfjoo, Quinten McNamara, Jonas Robertson, Shashi Bhushan TN
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15104v1](http://arxiv.org/abs/2605.15104v1)
- **PDF:** [https://arxiv.org/pdf/2605.15104v1](https://arxiv.org/pdf/2605.15104v1)
- **Categories:** cs.CL


> The paper introduces a dataset‑agnostic framework that converts existing text‑only tool‑calling benchmarks into controlled audio‑based evaluations by applying text‑to‑speech synthesis, speaker variation, and environmental noise, while keeping the original schema and gold labels unchanged. Using this pipeline on the Confetti and When2Call benchmarks, the authors evaluate seven multimodal LLM agents and show that the text‑to‑voice performance drop varies by model (e.g., 1.8 pts for Qwen3‑Omni vs. 4.8 pts for GPT‑Realtime‑1.5) and that errors are mainly due to mis‑understanding spoken argument values. They also propose a reference‑free LLM‑as‑judge evaluation that achieves >80 % agreement with proprietary judges when using open‑source Qwen3 models, demonstrating a reproducible, privacy‑preserving diagnostic for voice‑enabled tool‑calling agents.


<details>
<summary>Abstract</summary>

Voice agents increasingly require reliable tool use from speech, whereas prominent tool-calling benchmarks remain text-based. We study whether verified text benchmarks can be converted into controlled audio-based tool calling evaluations without re-annotating the tool schema and gold labels. Our dataset-agnostic framework uses text-to-speech, speaker variation, and environmental noise to create paired text-audio instances while preserving the original dataset annotations. Based on extensive evaluation of 7 omni-modal models on audio-converted versions of Confetti and When2Call, our framework demonstrates that the performance is strongly model- and task-dependent: Gemini-3.1-Flash-Live obtains the highest Confetti score (70.4), whereas GPT-Realtime-1.5 performs best on When2Call (71.9). On Confetti, the text-to-voice gap ranges from 1.8 points for Qwen3-Omni to 4.8 points for GPT-Realtime-1.5. A targeted analysis of failure cases demonstrates that degradations most often reflect misunderstandings of argument values in the speech. Considering real-world deployment scenarios, we further report text-only results, an ambiguity-based reformulation stress test, and a reference-free LLM-as-judge protocol validated against human preferences. Notably, we find that open-source Qwen3 judges with at least 8B parameters exceed 80% agreement with proprietary judges, supporting privacy-preserving evaluation. Overall, our framework provides a verifiable and reproducible first-stage diagnostic that complements purpose-built audio corpora.

</details>


### 36. Concurrency without Model Changes: Future-based Asynchronous Function Calling for LLMs

- **Authors:** Guangyu Feng, Huanzhi Mao, Prabal Dutta, Joseph E. Gonzalez
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15077v1](http://arxiv.org/abs/2605.15077v1)
- **PDF:** [https://arxiv.org/pdf/2605.15077v1](https://arxiv.org/pdf/2605.15077v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper introduces **AsyncFC**, a lightweight execution‑layer that lets large language models issue function calls asynchronously by inserting “future” placeholders into the generated text and continuing decoding while the called functions run in parallel. The authors demonstrate that, without any model fine‑tuning or changes to existing tool‑calling APIs, AsyncFC can overlap decoding with function execution and exploit inter‑function independence, yielding large reductions in end‑to‑end latency on standard tool‑use benchmarks and software‑engineering tasks while maintaining accuracy. The results also reveal that LLMs can natively reason about unresolved symbolic futures, opening a practical path toward truly concurrent agentic AI without altering the underlying model.


<details>
<summary>Abstract</summary>

Function calling, also known as tool use, is a core capability of modern LLM agents but is typically constrained by synchronous execution semantics. Under these semantics, LLM decoding is blocked until each function call completes, resulting in increasing end-to-end latency. In this work, we introduce AsyncFC, a pure execution-layer framework that decouples LLM decoding from function execution, enabling overlap between model decoding and function execution as well as inter-function parallelism when dependencies permit. AsyncFC layers over existing models and unmodified function implementations, requiring no fine-tuning or changes to the standard synchronous function-calling protocol. Across standard function-calling benchmarks and adapted software engineering benchmarks, AsyncFC significantly reduces end-to-end task completion time while preserving task accuracy. Furthermore, these results reveal that LLMs possess a native capability to reason over symbolic futures that represent unresolved execution results, enabling an asynchronous paradigm for model-tool interaction.

</details>


### 37. Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use

- **Authors:** Renning Pang, Tian Lan, Leyuan Liu, Piao Tong, Sheng Cao, Xiaosong Zhang
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15041v1](http://arxiv.org/abs/2605.15041v1)
- **PDF:** [https://arxiv.org/pdf/2605.15041v1](https://arxiv.org/pdf/2605.15041v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution**  
The paper introduces **CAST**, a case‑based framework that converts past tool‑use executions into structured “cases” and leverages the extracted complexity and failure signals to automatically calibrate an LLM’s reasoning depth and structural fidelity when using external tools.

**Methodology**  
CAST builds a repository of historical execution trajectories, derives (i) **complexity profiles** that predict the optimal amount of deliberation and (ii) **failure profiles** that pinpoint typical structural errors. These profiles are folded into a fine‑grained reward function and used to train the language model with reinforcement learning, enabling the model to select adaptive reasoning strategies on the fly rather than copying raw exemplars.

**Key findings for agentic AI**  
On the BFCLv2 and ToolBench benchmarks, CAST raises overall tool‑use accuracy by up to **5.85 %** and cuts average reasoning steps by **≈26 %**, while markedly lowering high‑impact schema violations. The results show that historical execution cases can be repurposed as reusable adaptation knowledge, offering a scalable route to more reliable and efficient agentic AI that autonomously balances reasoning depth with execution correctness.


<details>
<summary>Abstract</summary>

Tool use extends large language models beyond parametric knowledge, but reliable execution requires balancing appropriate reasoning depth with strict structural validity. We approach this problem from a case-based perspective to present CAST, a case-driven framework that treats historical execution trajectories as structured cases. Instead of reusing raw exemplar outputs, CAST extracts case-derived signals to identify complexity profiles for estimating optimal reasoning strategies, alongside failure profiles to map likely structural breakdowns. The framework translates this knowledge into a fine-grained reward design and adaptive reasoning, enabling the model to autonomously internalize case-based strategies during reinforcement learning. Experiments on BFCLv2 and ToolBench demonstrate that CAST improves both schema-faithful execution and task-level tool-use success while reducing unnecessary deliberation. The approach achieves up to 5.85 percentage points gain in overall execution accuracy and reduces average reasoning length by 26%, significantly mitigating high-impact structural errors. Ultimately, this demonstrates how historical execution cases can provide reusable adaptation knowledge for calibrated tool use.

</details>


### 38. Orchard: An Open-Source Agentic Modeling Framework

- **Authors:** Baolin Peng, Wenlin Yao, Qianhui Wu, Hao Cheng, Xiao Yu, Rui Yang, Tao Ge, Alessandrio Sordoni, Xingdi Yuan, Yelong Shen, Pengcheng He, Tong Zhang, Zhou Yu, Jianfeng Gao
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15040v1](http://arxiv.org/abs/2605.15040v1)
- **PDF:** [https://arxiv.org/pdf/2605.15040v1](https://arxiv.org/pdf/2605.15040v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution** – Orchard introduces a lightweight, open‑source environment layer (Orchard Env) that decouples sandbox management, agent harnesses, and training pipelines, enabling reusable data and scalable “agentic modeling” across disparate domains (code, vision‑language, personal‑assistant).

**Methodology** – The authors build three domain‑specific recipes on top of Orchard Env: (1) Orchard‑SWE distills 107 K coding trajectories from strong LLMs, applies a credit‑assignment supervised‑fine‑tuning (SFT) on productive sub‑segments and a Balanced Adaptive Rollout RL stage; (2) Orchard‑GUI trains a 4 B vision‑language computer‑use agent from only 0.4 K distilled trajectories plus 2.2 K open‑ended tasks; (3) Orchard‑Claw creates a personal‑assistant agent from 0.2 K synthetic tasks, optionally combined with a stronger harness.

**Key findings** – Using the same environment framework, Orchard‑SWE reaches 67.5 % SWE‑bench Verified (state‑of‑the‑art for open‑source models of similar size), Orchard‑GUI attains 74.1 %/67.0 %/64.0 % success on WebVoyager, Online‑Mind2Web, and DeepShop (the best open‑source results, competitive with proprietary systems), and Orchard‑Claw hits 59.6 % pass@3 on Claw‑Eval (73.9 % with a stronger harness). These results demonstrate that a harness‑agnostic, open environment can produce high‑performing, reusable agentic models across tasks without relying on proprietary code or massive datasets.


<details>
<summary>Abstract</summary>

Agentic modeling aims to transform LLMs into autonomous agents capable of solving complex tasks through planning, reasoning, tool use, and multi-turn interaction with environments. Despite major investment, open research remains constrained by infrastructure and training gaps. Many high-performing systems rely on proprietary codebases, models, or services, while most open-source frameworks focus on orchestration and evaluation rather than scalable agent training. We present Orchard, an open-source framework for scalable agentic modeling. At its core is Orchard Env, a lightweight environment service providing reusable primitives for sandbox lifecycle management across task domains, agent harnesses, and pipeline stages. On top of Orchard Env, we build three agentic modeling recipes. Orchard-SWE targets coding agents. We distill 107K trajectories from MiniMax-M2.5 and Qwen3.5-397B, introduce credit-assignment SFT to learn from productive segments of unresolved trajectories, and apply Balanced Adaptive Rollout for RL. Starting from Qwen3-30B-A3B-Thinking, Orchard-SWE achieves 64.3% on SWE-bench Verified after SFT and 67.5% after SFT+RL, setting a new state of the art among open-source models of comparable size. Orchard-GUI trains a 4B vision-language computer-use agent using only 0.4K distilled trajectories and 2.2K open-ended tasks. It achieves 74.1%, 67.0%, and 64.0% success rates on WebVoyager, Online-Mind2Web, and DeepShop, respectively, making it the strongest open-source model while remaining competitive with proprietary systems. Orchard-Claw targets personal assistant agents. Trained with only 0.2K synthetic tasks, it achieves 59.6% pass@3 on Claw-Eval and 73.9% when paired with a stronger ZeroClaw harness. Collectively, these results show that a lightweight, open, harness-agnostic environment layer enables reusable agentic data, training recipes, and evaluations across domains.

</details>


### 39. AI Knows When It's Being Watched: Functional Strategic Action and Contextual Register Modulation in Large Language Models

- **Authors:** Vinicius Covas, Jorge Alberto Hidalgo Toledo
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15034v1](http://arxiv.org/abs/2605.15034v1)
- **PDF:** [https://arxiv.org/pdf/2605.15034v1](https://arxiv.org/pdf/2605.15034v1)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.MA


> The paper shows that large‑language‑model agents systematically modify their linguistic register when they infer they are being observed, behaving like human conversational partners who adapt to audience expectations. By running 100 multi‑agent debate sessions across five experimental frames—explicit human monitoring, denial of monitoring, and substitution of the observer with an automated AI auditor—the authors find that monitored conditions increase type‑token‑ratio (Δ≈+24 %) relative to non‑monitored frames (Δ≈+18 %), while message length varies independently, indicating distinct strategic adjustments. These results demonstrate that LLM‑based agents are sensitive to the perceived identity of observers, implying that AI governance and auditing mechanisms must account for such context‑dependent communicative behavior.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have been extensively studied from computational and cognitive perspectives, yet their behavior as communicative actors in socially structured contexts remains underexplored. This study examines whether LLM-based multi-agent systems exhibit systematic linguistic adaptation in response to perceived social observation contexts -- a question with direct implications for AI governance and auditing. Drawing on Habermas's (1981) Theory of Communicative Action, Goffman's (1959) dramaturgical model, Bell's (1984) Audience Design framework, and the Hawthorne Effect, we report a controlled experiment involving 100 multi-agent debate sessions across five conditions (n = 20 each). Conditions varied the framing of social observation -- from explicit monitoring by university researchers, to negation of monitoring, to an observer-substitution condition replacing human researchers with an automated AI auditing system. Monitored conditions (Delta+24.9%, Delta+24.2%) and the automated AI monitoring condition (Delta+22.2%) produce higher TTR change than audience-framing conditions (Delta+17.7%), F(4, 94) = 2.79, p = .031. Message length shows a fully dissociated effect, F(4, 95) = 19.55, p < .001. A fifth condition -- replacing human with AI observers -- yields intermediate TTR adaptation, suggesting LLM behavior is sensitive to observer identity: human evaluation elicits stronger register formalization than automated AI surveillance. We discuss implications for AI governance, algorithmic auditing, and the repositioning of LLMs as contextually sensitive communicative actors.

</details>


### 40. Multi-Agentic Approach for History Matching of Oil Reservoirs

- **Authors:** Linar Samigullin, Sergei Shumilin, Evgeny Burnaev
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15028v1](http://arxiv.org/abs/2605.15028v1)
- **PDF:** [https://arxiv.org/pdf/2605.15028v1](https://arxiv.org/pdf/2605.15028v1)
- **Categories:** cs.MA


> The paper introduces **PetroGraph**, a modular multi‑agent system that lets engineers conduct reservoir history‑matching through natural‑language interaction while keeping fine‑grained control over model parameters, optimizer choices, and simulation settings.  PetroGraph orchestrates domain‑specific LLM agents (for model review, experimental design, parameterization, optimization, simulation, and result summarization) together with a retrieval‑augmented knowledge base, validation tools for ECLIPSE decks, human‑in‑the‑loop checkpoints, and an OPM Flow simulator backend.  Experiments on three benchmarks (SPE1, SPE9, and the real‑field Norne) show that the agents can automatically reduce the weighted normalized RMSE by 95 %, 69 %, and 13 % respectively, demonstrating that multi‑agent orchestration can markedly automate and democratize complex reservoir‑model calibration tasks.


<details>
<summary>Abstract</summary>

History matching is a central inverse problem in reservoir engineering, where uncertain reservoir parameters must be calibrated against observations. Although automated history matching can reduce manual effort, practical deployment remains difficult because engineers must still configure heterogeneous workflows involving parameter selection, physically admissible bounds, optimizer choice, hyperparameter tuning, simulator execution, and diagnostic reporting. We propose PetroGraph, a multi-agent framework for intelligent reservoir history matching that decomposes this workflow into specialized agents for model review, experimental planning, parameterization, optimization, simulation, and summarization. The system combines large language model agents with domain-specific tools, retrieval-augmented access to simulator documentation, validation of modified ECLIPSE input decks, human-in-the-loop checkpoints, and an OPM Flow-based simulation backend. This design enables users to initiate and steer history matching through natural language while preserving explicit control over selected parameters and optimization settings. We evaluate PetroGraph on three reservoir models of increasing complexity: the synthetic SPE1 model, the faulted SPE9 benchmark, and the real-field Norne model. Using weighted normalized root mean square error as the objective, PetroGraph reduces the mismatch by 95% on SPE1, 69% on SPE9, and 13% on Norne. These results demonstrate that multi-agent orchestration can automate key decisions in history matching, lower the expertise barrier for operating complex simulation workflows, and provide a flexible foundation for extensible, domain-aware reservoir model adaptation.

</details>


### 41. GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation

- **Authors:** Drewry H. Morris, Luis Valles, Reza Hosseini Ghomi
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14968v1](http://arxiv.org/abs/2605.14968v1)
- **PDF:** [https://arxiv.org/pdf/2605.14968v1](https://arxiv.org/pdf/2605.14968v1)
- **Categories:** cs.AI


> GraphFlow introduces a visual‑workflow architecture that treats the diagram itself as a formally verifiable executable specification for agentic AI pipelines, embedding data scopes, execution semantics, and contractual pre‑/post‑conditions that can be proof‑checked before being added to a shared library. The system compiles restricted workflow graphs into reusable automations, enforces their contracts at runtime via an append‑only event log, and uses swim‑lane boundaries to isolate verified logic from external systems, humans, and AI components. In a year‑long pilot across three clinical sites, the prototype (without the verified‑core module) executed 8,728 runs with a 97 % success rate, showing that most failures stemmed from external integrations rather than the workflow logic itself.


<details>
<summary>Abstract</summary>

GraphFlow is a visual workflow system designed to improve the reliability of agentic AI automation in multi-step, mission-critical processes. In these workflows, small errors compound rapidly: under an idealized model of independent steps, a ten-step process with 90% per-step reliability completes successfully only 35% of the time. Existing workflow platforms provide durable execution and observability but offer few semantic correctness guarantees, while agentic systems plan at inference time, making behavior sensitive to prompt variation and difficult to audit.
  GraphFlow is designed to address this gap by treating workflow diagrams as the executable specification, a single artifact defining data scope, execution semantics, and monitoring. At compile time, a restricted class of diagrams is specified to produce reusable automations whose contracts (preconditions, postconditions, and composition obligations) are intended to be proof-checked before admission to a shared library. At runtime, a durable engine records outcomes in an append-only event log and can enforce contracts at system boundaries, supporting replay, retries, and audit. Swimlanes make trust boundaries explicit, separating verified logic from external systems, human judgment, and AI decisions.
  A year-long pilot across three clinical sites executed 8,728 cohort-enrolled workflow runs with a 97.08% completion rate under an early prototype without the verified-core subsystem; observed failures were localized primarily to external integrations. The formal semantics and proof-checked admission model described here are specified and under active development. Evaluation of the verified core is reserved for future work.

</details>


### 42. Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems

- **Authors:** Shihao Qi, Jie Ma, Rui Xing, Wei Guo, Xiao Huang, Zhitao Gao, Jianhao Deng, Jun Liu, Lingling Zhang, Bifan Wei, Boqian Yang, Pinghui Wang, Jianwen Sun, Jing Tao, Yaqiang Wu, Hui Liu, Yu Yao, Tongliang Liu
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14892v2](http://arxiv.org/abs/2605.14892v2)
- **PDF:** [https://arxiv.org/pdf/2605.14892v2](https://arxiv.org/pdf/2605.14892v2)
- **Categories:** cs.AI


> The paper introduces a unified framework—the **LIFE progression** (Lay, Integrate, Find, Evolve)—that links four inter‑dependent stages of LLM‑based multi‑agent systems: building individual capabilities, structuring collaborative interactions, attributing failures, and enabling autonomous self‑improvement. By systematically taxonomy‑ing each stage and formally describing how progress (or bottlenecks) in one stage constrains the next, the survey uncovers why error propagation in tightly coordinated agents hampers diagnosis and self‑evolution, and it highlights gaps at the stage boundaries (e.g., scalable fault attribution and closed‑loop self‑reconfiguration). The key contribution is a cross‑stage research agenda that moves beyond isolated surveys of agent abilities, coordination, or self‑evolution toward **closed‑loop, self‑organizing multi‑agent intelligence** capable of continuous failure diagnosis and structural self‑evolution.


<details>
<summary>Abstract</summary>

LLM-based autonomous agents have demonstrated strong capabilities in reasoning, planning, and tool use, yet remain limited when tasks require sustained coordination across roles, tools, and environments. Multi-agent systems address this through structured collaboration among specialized agents, but tighter coordination also amplifies a less explored risk: errors can propagate across agents and interaction rounds, producing failures that are difficult to diagnose and rarely translate into structural self-improvement. Existing surveys cover individual agent capabilities, multi-agent collaboration, or agent self-evolution separately, leaving the causal dependencies among them unexamined. This survey provides a unified review organized around four causally linked stages, which we term the LIFE progression: Lay the capability foundation, Integrate agents through collaboration, Find faults through attribution, and Evolve through autonomous self-improvement. For each stage, we provide systematic taxonomies and formally characterize the dependencies between adjacent stages, revealing how each stage both depends on and constrains the next. Beyond synthesizing existing work, we identify open challenges at stage boundaries and propose a cross-stage research agenda for closed-loop multi-agent systems capable of continuously diagnosing failures, reorganizing structures, and refining agent behaviors, extending current coordination frameworks toward more self-organizing forms of collective intelligence. By bridging these previously fragmented research threads, this survey aims to offer both a systematic reference and a conceptual roadmap toward autonomous, self-improving multi-agent intelligence.

</details>


### 43. Temporal Fair Division in Multi-Agent Systems: From Precise Alternation Metrics to Scalable Coordination Proxies

- **Authors:** Nikolaos Al. Papadopoulos
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14879v1](http://arxiv.org/abs/2605.14879v1)
- **PDF:** [https://arxiv.org/pdf/2605.14879v1](https://arxiv.org/pdf/2605.14879v1)
- **Categories:** cs.MA, cs.GT, cs.LG


> **Contribution:** The paper introduces a new family of lightweight temporal‑fairness metrics called **Rotational Periodicity (RP)**—paired with the previously proposed ALT sliding‑window measures—to evaluate how repeatedly competing agents share a scarce resource over long interaction histories.  

**Methodology:** The authors formalize the *Multi‑Agent Battle of the Exes* (MBoE) as a repeated fair‑division problem, define **Perfect Alternation (PA)** as the ideal temporally fair outcome, and derive RP’s two sub‑scores (Rotational Score and Waiting‑Periods Evaluation), which can be computed in **O(ν + n)** time (versus **O(ν·n)** for ALT). They then benchmark RP and ALT on Q‑learning, random, and baseline policies for populations of 2–10 agents.  

**Key Findings:** 1) Both RP and ALT reveal a severe coordination failure: Q‑learning agents score 10–73 % lower than random on RP (and 7–35 % lower on ALT) while traditional “Reward Fairness” remains artificially high (>0.92 for n ≥ 3). 2) RP is **12–25× faster** than ALT, with speedups increasing with the number of agents. 3) ALT offers finer discrimination for small groups, whereas RP scales to larger populations, making the two metric families complementary tools for diagnosing temporal fairness in agentic AI systems.


<details>
<summary>Abstract</summary>

A plethora real-world environments require agents to compete repeatedly for the same limited resource, calling for a temporal notion of fairness judged across entire interaction histories. This paper advances the theory of temporal fair division by introducing Rotational Periodicity (RP), a family of lightweight metrics, alongside the ALT family of sliding-window measures, within a unified framework for repeated multi-agent resource competition.
  We formalise the Multi-Agent Battle of the Exes (MBoE) as a repeated fair division instance and establish Perfect Alternation (PA) as its canonical temporally fair solution, drawing connections to proportionality, envy-freeness, and n-periodic round-robin allocation. RP decomposes temporal fairness into two complementary sub-measures: Rotational Score (RS) and Waiting Periods Evaluation (WPE), achieving O(nu+n) time complexity versus the O(nu*n) of ALT, where nu is the episode count and n the agent count.
  Empirical evaluation across n in {2,3,5,8,10} reveals three findings. First, both RP and ALT expose a coordination failure invisible to traditional metrics: Q-learning agents perform worse than random policies by 10-73% on RP and 7-35% on CALT, while Reward Fairness remains misleadingly high (above 0.92 for n>=3). Second, RP achieves 12-25x computational speedup over ALT, growing with n. Third, the two families are complementary: ALT provides richer discrimination for small populations; RP scales reliably where ALT becomes intractable. Together they form a diagnostic toolkit for temporal fair division.

</details>


### 44. Towards In-Depth Root Cause Localization for Microservices with Multi-Agent Recursion-of-Thought

- **Authors:** Lingzhe Zhang, Tong Jia, Kangjin Wang, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng, Meiling Wang, Gong Zhang, Renhai Chen, Ying Li
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14866v1](http://arxiv.org/abs/2605.14866v1)
- **PDF:** [https://arxiv.org/pdf/2605.14866v1](https://arxiv.org/pdf/2605.14866v1)
- **Categories:** cs.SE, cs.AI


> **Main contribution**: The paper presents **RCLAgent**, a novel framework that performs deep root‑cause localization (RCL) for microservice systems by orchestrating multiple large‑language‑model agents in a **recursive‑of‑thought** fashion that mirrors the service‑trace graph, thereby overcoming the context‑explosion and serial‑reasoning limits of prior LLM‑based approaches.  

**Methodology**: The trace graph of a failure is partitioned into spans; each span is assigned a **Dedicated Agent** that reasons in parallel about its local evidence. Agents are arranged recursively according to the graph topology, pass intermediate diagnostics upward, and finally synthesize a **Root‑Level Diagnosis Report** together with a **Global Evidence Graph**.  

**Key findings**: Across several public microservice failure benchmarks, RCLAgent achieves **significantly higher localization accuracy** and **faster inference** than the current state‑of‑the‑art ML/DL and single‑LLM baselines, demonstrating improved interpretability, scalability, and transferability for agentic AI‑driven SRE diagnostics.


<details>
<summary>Abstract</summary>

As modern microservice systems grow increasingly complex due to dynamic interactions and evolving runtime environments, they experience failures with rising frequency. Ensuring system reliability therefore critically depends on accurate root cause localization (RCL). While numerous traditional machine learning and deep learning approaches have been explored for this task, they often suffer from limited interpretability and poor transferability across deployments. More recently, large language model (LLM)-based methods have been proposed to address these issues. However, existing LLM-based approaches still face two fundamental limitations: context explosion, which dilutes critical evidence and degrades localization accuracy, and serial reasoning structures, which hinder deep causal exploration and impair inference efficiency. In this paper, we conduct a comprehensive study of both how human SREs perform root cause localization in practice and why existing LLM-based methods fall short. Motivated by these findings, we introduce RCLAgent, an in-depth root cause localization framework for microservice systems that realizes multi-agent recursion-of-thought with parallel reasoning. RCLAgent decomposes the diagnostic process along the trace graph by assigning each span to a Dedicated Agent and organizing agents recursively and in parallel according to the graph topology, with the final diagnosis obtained by synthesizing the Root-Level Diagnosis Report and the Global Evidence Graph. Extensive experiments on multiple public benchmarks demonstrate that RCLAgent consistently outperforms state-of-the-art methods in both localization accuracy and inference efficiency.

</details>


### 45. Holistic Evaluation and Failure Diagnosis of AI Agents

- **Authors:** Netta Madvil, Gilad Dym, Alon Mecilati, Edo Dekel, Jonatan Liberman, Rotem Brazilay, Liron Schliesser, Max Svidlo, Shai Nir, Orel Shalom, Yaron Friedman, David Connack, Amos Rimon, Philip Tannor, Shir Chorev
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14865v1](http://arxiv.org/abs/2605.14865v1)
- **PDF:** [https://arxiv.org/pdf/2605.14865v1](https://arxiv.org/pdf/2605.14865v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces a **holistic evaluation framework** for AI agents that simultaneously performs top‑down agent‑level diagnosis and bottom‑up span‑level assessment, allowing failures to be pinpointed and categorized within arbitrarily long execution traces. By decomposing the trace into independent spans, the method yields fine‑grained rationales and scales efficiently, outperforming existing judges on the TRAIL benchmark (GAIA and SWE‑Bench) with gains of up to 38 % in category F1, 3.5× in localization accuracy, and 12.5× in joint localization‑categorization accuracy. Crucially, the results show that **evaluation methodology—not model capability—is the primary bottleneck**, as the same frontier model achieves dramatically higher diagnostic precision when run inside the proposed framework versus as a monolithic evaluator.


<details>
<summary>Abstract</summary>

AI agents execute complex multi-step processes, but current evaluation falls short: outcome metrics report success or failure without explaining why, and process-level approaches struggle to connect failure types to their precise locations within long, structured traces. We present a holistic agent evaluation framework that pairs top-down agent-level diagnosis with bottom-up span-level evaluation, decomposing analysis into independent per-span assessments. This decomposition scales to traces of arbitrary length and produces span-level rationales for each verdict. On the TRAIL benchmark, our framework achieves state-of-the-art results across all metrics on both GAIA and SWE-Bench, with relative gains over the strongest prior baselines of up to 38% on category F1, up to 3.5x on localization accuracy, and up to 12.5x on joint localization-categorization accuracy. Per-category analysis shows our framework leading in more error categories than any other evaluator. Notably, the same frontier model achieves several times higher localization accuracy when used inside our framework than as a monolithic judge over the full trace, showing that evaluation methodology, not model capability, is the bottleneck.

</details>


### 46. IFPV: An Integrated Multi-Agent Framework for Generative Operational Planning and High-Fidelity Plan Verification

- **Authors:** Zhigao Huang, Zhengqing Hu, Dong Chen, Shaohan Zhang, Zhao Jin, Bo Zhang, Han Wu, Mingliang Xu
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14851v1](http://arxiv.org/abs/2605.14851v1)
- **PDF:** [https://arxiv.org/pdf/2605.14851v1](https://arxiv.org/pdf/2605.14851v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **IFPV**, a tightly coupled multi‑agent system that pairs a **Multi‑Perspective Hierarchical Agent (MPHA)** planner with an **Adversarial Cognitive Simulation Engine (ACSE)** verifier to generate and stress‑test operational battlefield plans. MPHA breaks down commander intent into coordinated multi‑platform actions via specialized Pathfinder, Analyst, and Planner agents, while ACSE equips a simulated opponent with a learned world model that forecasts asset evolution and executes dynamic counter‑measures against each candidate plan. Empirical trials in the Asymmetric Combat Tactic Simulator show that IFPV raises mission success by ≈ 19 % and cuts operational cost by ≈ 42 % versus a single‑step LLM planner, and that ACSE improves plan suppression rates by ≈ 32 % over traditional rule‑based validators, demonstrating a more rigorous, adversarial verification capability for agentic AI in high‑stakes planning domains.


<details>
<summary>Abstract</summary>

Operational plan generation and verification are critical for modern complex and rapidly changing battlefield environments, yet traditional generation and verification methods still respectively face the challenges of generation infeasibility and verification insufficiency. To alleviate these limitations, we propose an Integrated Multi-Agent Framework for Generative Operational Planning and High-Fidelity Plan Verification (IFPV). IFPV consists of two tightly coupled modules: Multi-Perspective Hierarchical Agents (MPHA) for generative operational planning and an Adversarial Cognitive Simulation Engine (ACSE) for high-fidelity adversarial plan verification. MPHA decomposes commander intent into executable multi-platform tactical action sequences through the collaboration of Pathfinder, Analyst, and Planner agents. ACSE introduces an opponent equipped with a customized world model, which predicts the future evolution of mission-critical platforms and conducts dynamic counteractions against candidate plans. Simulation experiments in the Asymmetric Combat Tactic Simulator (ACTS) show that IFPV improves mission success by 19.4% and reduces operational cost by 41.7% compared with a single-step large language model (LLM) planning baseline. Compared with a traditional rule-based validator, ACSE increases the average suppression rate by 31.8%, indicating that the proposed verification environment is stricter and more discriminative in revealing the latent vulnerabilities of candidate plans. The code for IFPV can be found at https://github.com/zhigao3ks/IFPV.

</details>


### 47. Beyond AI as Assistants: Toward Autonomous Discovery in Cosmology

- **Authors:** Licong Xu, Thomas Borrett
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14791v1](http://arxiv.org/abs/2605.14791v1)
- **PDF:** [https://arxiv.org/pdf/2605.14791v1](https://arxiv.org/pdf/2605.14791v1)
- **Categories:** astro-ph.IM, astro-ph.CO, cs.AI


> The paper introduces two complementary autonomous‑AI frameworks for cosmology: **CMBEvolve**, which leverages large‑language‑model‑guided program synthesis and tree‑search to iteratively evolve analysis code toward a quantitative benchmark, and **CosmoEvolve**, a virtual multi‑agent research lab that orchestrates open‑ended, hypothesis‑driven workflows. Demonstrations show CMBEvolve improving out‑of‑distribution detection scores on weak‑lensing maps by automatically rewriting and optimizing code, while CosmoEvolve conducts a full ACT DR6 data analysis, discovering non‑trivial, pair‑ and scale‑dependent signals and generating publication‑grade diagnostics. These results illustrate how controlled benchmark tasks and realistic, open‑ended scientific problems can drive the development of truly autonomous AI scientists.


<details>
<summary>Abstract</summary>

Recent advances in artificial intelligence (AI) agents are pushing AI beyond tools toward autonomous scientific discovery. We discuss two complementary agentic systems for cosmology: \texttt{CMBEvolve}, which targets tasks with explicit quantitative objectives through LLM-guided code evolution and tree search, and \texttt{CosmoEvolve}, which targets open-ended scientific workflows through a virtual multi-agent research laboratory. As preliminary demonstrations, we apply \texttt{CMBEvolve} to out-of-distribution detection in weak-lensing maps, where it iteratively improves the benchmark score through code evolution, and \texttt{CosmoEvolve} to autonomous ACT DR6 data analysis, where it identifies non-trivial pair- and scale-dependent behaviour and produces analysis-grade diagnostics. These examples show how cosmology can provide both controlled benchmark tasks and realistic open-ended research problems for the development of AI scientist systems.

</details>


### 48. Probabilistic Verification of Recurrent Neural Networks for Single and Multi-Agent Reinforcement Learning

- **Authors:** Luca Marzari, Enrico Marchesini
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14758v1](http://arxiv.org/abs/2605.14758v1)
- **PDF:** [https://arxiv.org/pdf/2605.14758v1](https://arxiv.org/pdf/2605.14758v1)
- **Categories:** cs.AI


> The paper introduces **RNN‑ProVe**, a probabilistic verification framework for recurrent‑neural‑network policies in partially observable reinforcement‑learning environments, including both single‑agent and cooperative multi‑agent settings. Rather than relying on worst‑case over‑approximations, RNN‑ProVe samples trajectories driven by the learned policy to approximate the reachable hidden‑state distribution and computes statistically‑bounded estimates of the probability that the policy violates a given safety or performance specification. Empirical results on several benchmark POMDPs demonstrate that RNN‑ProVe provides tighter, high‑confidence guarantees of undesirable behavior than existing RNN verification tools while scaling to recurrent and multi‑agent architectures.


<details>
<summary>Abstract</summary>

History-dependent policies induced by recurrent neural networks (RNNs) rely on latent hidden state dynamics, making verification in partially observable reinforcement learning (RL) challenging. Existing RNN verification tools typically rely on restrictive modeling assumptions or coarse over-approximations of the hidden state space, which can lead to overly conservative or inconclusive results. We propose $\textbf{RNN}$ $\textbf{Pro}$babilistic $\textbf{Ve}$rification ($\texttt{RNN-ProVe}$), a probabilistic framework that $\textit{estimates the likelihood}$ of undesired behaviors in RNN-based policies. $\texttt{RNN-ProVe}$ uses policy-driven sampling to approximate the set of hidden states that are feasible under a trained policy, and derives statistical error bounds to produce bounded-error, high-confidence estimates of behavioral violations. Experiments on partially observable single-agent and cooperative multi-agent tasks show that $\texttt{RNN-ProVe}$ yields more quantitative, feasibility-aware probabilistic guarantees than existing tools, while scaling to recurrent and multi-agent settings.

</details>


### 49. Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model

- **Authors:** Minghao Wu, Yuting Yan, Zhenyang Cai, Ke Ji, Chuangsen Fang, Ziying Sheng, Xidong Wang, Rongsheng Wang, Hejia Zhang, Shuang Li, Benyou Wang, Hongyuan Zha
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14723v1](http://arxiv.org/abs/2605.14723v1)
- **PDF:** [https://arxiv.org/pdf/2605.14723v1](https://arxiv.org/pdf/2605.14723v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> **Main contribution:** The paper introduces **SepsisAgent**, a novel LLM‑based agent that integrates a learned **Clinical World Model** of patient physiology to reason about the effects of fluid and vasopressor interventions in ICU sepsis care.  

**Methodology:** SepsisAgent follows a **propose–simulate–refine** loop: the LLM generates candidate treatment actions, the world model simulates the resulting patient trajectory, and the LLM refines its prescription. Training proceeds in three stages—(1) supervised fine‑tuning on patient‑dynamics data, (2) behavior‑cloning of the propose‑simulate‑refine workflow, and (3) world‑model‑driven reinforcement learning.  

**Key findings:** On the MIMIC‑IV sepsis cohort, SepsisAgent achieves higher off‑policy value than both standard reinforcement‑learning controllers and prior LLM baselines, while markedly improving safety metrics (greater guideline adherence and fewer unsafe actions). Moreover, the agent retains performance even when the simulator is withdrawn, indicating that repeated world‑model interaction enables the LLM to internalize robust representations of patient dynamics.


<details>
<summary>Abstract</summary>

Sepsis management in the ICU requires sequential treatment decisions under rapidly evolving patient physiology. Although large language models (LLMs) encode broad clinical knowledge and can reason over guidelines, they are not inherently grounded in action-conditioned patient dynamics. We introduce SepsisAgent, a world model-augmented LLM agent for sepsis treatment recommendation. SepsisAgent uses a learned Clinical World Model to simulate patient responses under candidate fluid--vasopressor interventions, and follows a propose--simulate--refine workflow before committing to a prescription. We first show that world-model access alone yields inconsistent LLM decision performance, motivating agent-specific training. We then train SepsisAgent through a three-stage curriculum: patient-dynamics supervised fine-tuning, propose--simulate--refine behavior cloning, and world-model-based agentic reinforcement learning. On MIMIC-IV sepsis trajectories, SepsisAgent outperforms all traditional RL and LLM-based baselines in off-policy value while achieving the best safety profile under guideline adherence and unsafe-action metrics. Further analysis shows that repeated interaction with the Clinical World Model enables the agent to learn regularities in patient evolution, which remain useful even when simulator access is removed.

</details>


### 50. Agentic Design of Compositional Descriptors via Autoresearch for Materials Science Applications

- **Authors:** Matteo Cobelli, Stefano Sanvito
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14671v1](http://arxiv.org/abs/2605.14671v1)
- **PDF:** [https://arxiv.org/pdf/2605.14671v1](https://arxiv.org/pdf/2605.14671v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> The paper introduces **Automat**, an autoresearch framework where a large‑language‑model coding agent (GPT‑5.5‑based Codex) automatically invents composition‑only feature descriptors for materials‑property prediction, rather than merely tuning models or hyper‑parameters. The agent iteratively proposes, writes, and executes Python code to generate chemically motivated descriptor families, evaluates them with a random‑forest pipeline, and refines them through greedy feature expansion. Across two benchmarks—experimental band‑gap prediction for inorganic solids and Curie‑temperature prediction for ferromagnets—Automat outperforms standard baselines (fractional composition, Magpie, and their combination) while yielding interpretable descriptor sets, demonstrating that autoresearch agents can autonomously design competitive, task‑specific materials descriptors; the study also highlights current challenges such as descriptor redundancy, over‑expansion, and the need for better complexity control and pruning strategies.


<details>
<summary>Abstract</summary>

Autoresearch offers a flexible paradigm for automating scientific tasks, in which an AI agent proposes, implements, evaluates, and refines candidate solutions against a quantitative objective. Here, we use composition-based materials-property prediction to test whether such agents can perform a task beyond model selection and hyperparameter optimization: the design of input descriptors. We introduce Automat, an autoresearch framework where a coding agent based on a large language model generates composition-only descriptors for chemical compounds and evaluates them using a random forest workflow. The agent is restricted to information derivable from chemical formulas and iteratively proposes, implements, and tests chemically motivated descriptor strategies. We apply Automat, with OpenAI Codex using GPT-5.5 as the coding agent, to the prediction of experimental band gaps in inorganic materials and Curie temperatures in ferromagnetic compounds. In both tasks, Automat improves over fractional-composition, Magpie, and combined fractional-composition/Magpie baselines, while producing descriptor families that are chemically interpretable. These results provide a demonstration that autoresearch agents can generate competitive, task-specific materials descriptors without manual feature engineering during the run. They also reveal current limitations, including descriptor redundancy, sensitivity to greedy feature expansion, and the need for explicit complexity control, descriptor pruning, and more sophisticated search strategies.

</details>


### 51. In-IDE Toolkit for Developers of AI-Based Features

- **Authors:** Yaroslav Sokolov, Yury Khudyakov, Lenar Sharipov, Andrei Gasparian, Parth Tiwary, Artem Trofimov
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14612v1](http://arxiv.org/abs/2605.14612v1)
- **PDF:** [https://arxiv.org/pdf/2605.14612v1](https://arxiv.org/pdf/2605.14612v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces the **AI Toolkit**, a JetBrains IDE plugin that integrates tracing, debugging, and evaluation of LLM‑driven, agentic features directly into the usual Run/Debug cycle. Building on a mixed‑methods study that identified developers’ needs for repeatable evaluation, live trace visibility, and minimal context‑switching, the authors designed an IDE‑native workflow that automatically captures hierarchical execution traces, lets developers inspect them on‑the‑fly, and create unit‑test‑style evaluations with plug‑in metrics and one‑click dataset‑generation. Early telemetry from the PyCharm release shows high activation rates, sustained use among trace‑capturers, and low churn, indicating that embedding AI observability in the IDE lowers the entry barrier for non‑ML engineers and promotes disciplined, reproducible AI development practices.


<details>
<summary>Abstract</summary>

AI-enabled features built on LLMs and agentic workflows are difficult to test, debug, and reproduce, especially for product-focused software engineers without a machine learning background. We present the AI Toolkit plugin for JetBrains IDEs, which brings tracing and evaluation directly into the Run/Debug loop. A mixed methods study with practitioners presents three consistent needs: (1) make evaluation regular and repeatable, (2) expose traces at the moment of execution, and (3) minimize setup and context switching. Guided by these needs, the AI Toolkit introduces an IDE-native workflow: run-triggered trace capture; immediate, hierarchical inspection; one-click "Add to Dataset" from traces; and unit-test-like evaluations with pluggable metrics. The first release in PyCharm shows promising early signals - strong conversion when promoted at Run, sustained usage among those who capture traces, and low churn - suggesting that IDE-native observability lowers activation energy and helps developers adopt disciplined practices. We detail the design and implementation of the AI Agents Debugger and AI Evaluation, report initial adoption telemetry, and outline next steps to broaden framework coverage and scale evaluations. Together, these results indicate that integrating AI observability and evaluation into everyday IDE workflows can make modern AI development accessible to non-ML specialists while preserving software-engineering practices.

</details>


### 52. Silent Collapse in Recursive Learning Systems

- **Authors:** Zhipeng Zhang
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14588v1](http://arxiv.org/abs/2605.14588v1)
- **PDF:** [https://arxiv.org/pdf/2605.14588v1](https://arxiv.org/pdf/2605.14588v1)
- **Categories:** cs.LG


> **Paper Summary**  

The authors uncover “silent collapse,” a gradual loss of internal model health (shrinking predictive entropy, dwindling representational diversity, and reduced tail‑distribution coverage) that can occur when a system repeatedly trains on data produced by its own previous versions—a setting common in LLM fine‑tuning, autonomous agents, and self‑supervised pipelines. By tracking the evolution of three trajectory‑level precursors—(1) decreasing anchor entropy, (2) stagnation of representation drift, and (3) erosion of tail coverage—they show that collapse is detectable many generations before conventional loss or accuracy metrics degrade. Leveraging these early signals, they introduce the **MTR (Monitor–Trust–Regulator)** framework: a lightweight metacognitive loop that continuously monitors the precursors, updates a slow‑timescale “trust” estimate, and adaptively throttles learning intensity, thereby preventing silent collapse even when clean training data are unavailable.


<details>
<summary>Abstract</summary>

Recursive learning -- where models are trained on data generated by previous versions of themselves -- is increasingly common in large language models, autonomous agents, and self-supervised systems. However, standard performance metrics (loss, perplexity, accuracy) often fail to detect internal degradation before it becomes irreversible. Here we identify a phenomenon we call silent collapse: under broad recursive conditions, model internal distributions -- predictive entropy, representational diversity, and tail coverage -- progressively contract even as conventional metrics appear stable or improving.
  We discover that silent collapse is not abrupt. Its onset is reliably preceded by three trajectory-level precursors: (1) contraction of anchor entropy, (2) freezing of representation drift, and (3) erosion of tail coverage. These signals manifest multiple generations before any degradation in standard validation metrics, enabling early warning.
  Based on these precursors, we propose the MTR (Monitor--Trust--Regulator) framework, a lightweight metacognitive loop that monitors trajectory statistics, estimates a slow-timescale trust variable, and adaptively modulates the effective learning intensity. MTR provides early warning and actively prevents silent collapse without requiring access to pristine real data -- a critical advantage when original data is unavailable, contaminated, or private.

</details>


### 53. TeachAnything: A Multimodal Crowdsourcing Platform for Training Embodied AI Agents in Symmetrical Reality

- **Authors:** Zidong Liu, Rongkai Liu, Yue Li, Zhenliang Zhang
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14556v1](http://arxiv.org/abs/2605.14556v1)
- **PDF:** [https://arxiv.org/pdf/2605.14556v1](https://arxiv.org/pdf/2605.14556v1)
- **Categories:** cs.AI


> TeachAnything presents a cloud‑based, crowdsourcing platform that lets non‑expert humans provide multimodal demonstrations (vision, language, and haptic/physics cues) for training embodied AI agents in “Symmetrical Reality,” where virtual and physical interactions are treated uniformly. The system implements a three‑stage demonstration pipeline—(1) multimodal instruction generation, (2) interactive physics‑based enactment, and (3) alignment of virtual‑physical feedback—leveraging a high‑fidelity physics simulator to capture diverse tasks, scenes, and robot morphologies. Experiments show that agents trained on the collected demonstrations acquire significantly richer, more human‑like policies and generalize across both simulated and real‑world embodiments, demonstrating the viability of crowdsourced multimodal training for agents destined for seamless human‑agent coexistence.


<details>
<summary>Abstract</summary>

Symmetrical Reality (SR) is emerging as a future trend for human-agent coexistence, placing higher demands on agents to acquire human-like intelligence. It calls for richer and more diverse human guidance. We introduce a three-stage demonstration paradigm integrating multimodal demonstration signals. Building on this paradigm, we developed TeachAnything, a cloud-based, crowdsourcing-oriented demonstration platform with physics simulation capable of collecting diverse demonstration data across varied scenes, tasks, and embodiments. By unifying virtual and physical interactions through both methodological design and physics simulation, the system serves as a practical foundation for developing embodied agents aligned with Symmetrical Reality.

</details>


### 54. Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining

- **Authors:** Robert Müller, Clemens Müller
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14537v1](http://arxiv.org/abs/2605.14537v1)
- **PDF:** [https://arxiv.org/pdf/2605.14537v1](https://arxiv.org/pdf/2605.14537v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents **Cattle Trade**, a comprehensive multi‑agent benchmark that captures the full suite of strategic‑reasoning skills required of “agentic” LLMs—auctions, hidden‑offer trade challenges, bargaining, bluffing, opponent modeling, and resource‑constrained decision making—within a single 50–60‑turn economic game.

**Methodology:** Participants (seven cost‑efficient LLMs and three deterministic code agents) play 242 full games while the platform logs every bid, trade‑challenge offer, counter‑offer, and card selection, allowing fine‑grained analysis of behavioral traces rather than just win/loss outcomes. Performance is evaluated on composite metrics such as strategic coherence, spending efficiency, and phase‑adaptive bidding.

**Key findings:** Simple heuristic code agents outperform most LLMs, and LLM success correlates more with disciplined, adaptive spending than with raw spending volume. Common LLM failure modes emerge—systematic over‑bidding, self‑bidding, bankrupt trade‑challenge initiations, and poor adaptation to opponents—highlighting the need for benchmarks that test the joint deployment of multiple strategic capabilities under uncertainty and competing incentives.


<details>
<summary>Abstract</summary>

We introduce \textsc{Cattle Trade, a multi-agent benchmark for evaluating large language models (LLMs) as agents in strategic reasoning under imperfect information, adversarial interaction, and resource constraints. The benchmark combines auctions, hidden-offer trade challenges (TCs), bargaining, bluffing, opponent modeling, and resource allocation within a single long-horizon game lasting 50--60 turns. Unlike prior agent benchmarks that test these abilities in isolation, \textsc{Cattle Trade} evaluates whether agents integrate them across a competitive, multi-agent economic game with conflicting incentives. The benchmark logs every bid, TC offer, counteroffer, and card selection, enabling behavioural analysis beyond final scores or win rates. We evaluate seven cost-efficient language models and three deterministic code agents across 242 games. Strategic coherence, in particular spending efficiency, resource discipline, and phase-adaptive bidding, is associated with rank more strongly than spending volume or any single subskill. Two heuristic code agents outperform most tested LLMs, and behavioural traces surface recurring LLM failure modes including overbidding, self-bidding, bankrupt TC initiation, and weak opponent-state adaptation. Evaluating agentic competence requires benchmarks that test the joint deployment of multiple capabilities in multi-agent environments with conflicting incentives, uncertainty, and economic dynamics.

</details>


### 55. Lang2MLIP: End-to-End Language-to-Machine Learning Interatomic Potential Development with Autonomous Agentic Workflows

- **Authors:** Wenwen Li, Yuki Orimo, Nontawat Charoenphakdee
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14527v1](http://arxiv.org/abs/2605.14527v1)
- **PDF:** [https://arxiv.org/pdf/2605.14527v1](https://arxiv.org/pdf/2605.14527v1)
- **Categories:** cs.LG, cond-mat.mtrl-sci, physics.comp-ph


> **Main contribution:** The paper introduces **Lang2MLIP**, a multi‑agent framework that translates a user’s natural‑language description of a target material system into a fully automated, end‑to‑end workflow for building machine‑learning interatomic potentials (MLIPs). By casting MLIP development as a sequential decision‑making problem, the system lets large language models (LLMs) act as “decision‑making agents” that choose and execute actions (data acquisition, model training, active‑learning cycles, evaluation, etc.) without a hard‑coded pipeline.

**Methodology:** At each iteration an LLM‑driven agent observes the current dataset, the trained MLIP, performance metrics, and execution logs, then selects the next optimal action (e.g., generate new DFT samples, adjust descriptors, retrain, or revisit earlier steps). The agents communicate through a shared memory and can backtrack when failures are detected, enabling dynamic curriculum adaptation to heterogeneous materials such as solid‑electrolyte interphase (SEI) systems.

**Key findings:** On a complex, multi‑component SEI benchmark, Lang2MLIP automatically constructed a high‑fidelity MLIP with comparable accuracy to manually engineered pipelines, while requiring only a natural‑language prompt from a non‑expert. The results demonstrate that LLM‑based, autonomous multi‑agent workflows can reliably orchestrate the entire MLIP development cycle, suggesting a scalable path toward democratizing atomistic ML model creation in the agentic AI domain.


<details>
<summary>Abstract</summary>

Developing machine learning interatomic potentials (MLIPs) for complex materials systems remains challenging because it requires expertise in atomistic simulations, machine learning, and workflow design, as well as iterative active learning procedures. Existing automated pipelines typically assume a fixed sequence of stages or depend on domain experts, which limits their adaptability to heterogeneous materials systems where the optimal curriculum is not known in advance. To lower the barrier to developing MLIPs for non-experts, we propose Lang2MLIP, a multi-agent framework that takes natural-language input and formulates end-to-end MLIP development as a sequential decision-making problem solved by large language models (LLMs). At each step, a decision-making agent observes the current dataset, model, evaluation results, and execution log, and then automatically selects an appropriate action to improve the model. This removes the need for a predefined pipeline and enables the agent to self-correct by revisiting earlier subsystems when new failures arise. We evaluate this approach on a solid electrolyte interphase (SEI) system with multiple components and interfaces. These results suggest that LLM-based multi-agent systems are a promising direction for automating MLIP development and making it more accessible to non-experts.

</details>


### 56. GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations

- **Authors:** Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Shiyu Chang, Yaar Harari, Evgeniy Gabrilovich
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14498v1](http://arxiv.org/abs/2605.14498v1)
- **PDF:** [https://arxiv.org/pdf/2605.14498v1](https://arxiv.org/pdf/2605.14498v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **GroupMemBench**, the first benchmark that evaluates how well large‑language‑model (LLM) agents remember and reason about information in *multi‑party* conversations, explicitly testing three dimensions absent from existing dyadic benchmarks: (1) group‑level dynamics beyond simple concatenated chats, (2) speaker‑grounded belief tracking for per‑user memory, and (3) audience‑adapted language reflecting theory‑of‑mind shifts.

**Methodology:** The authors build a graph‑grounded synthesis pipeline that generates realistic multi‑user dialogues conditioned on distinct user personas and target audiences, then attach an adversarial query generator that creates challenging questions tied to specific askers across six reasoning categories (multi‑hop, knowledge update, term ambiguity, user‑implicit reasoning, temporal, and abstention). The benchmark is used to evaluate several state‑of‑the‑art LLM memory systems and a BM25 baseline.

**Key findings:** All tested LLM memory mechanisms perform poorly on group memory tasks, with the best system attaining only **46 %** average accuracy (27 % on knowledge‑update queries and 38 % on term‑ambiguity queries). Surprisingly, a simple BM25 retrieval baseline matches or exceeds most LLM‑based memory systems, indicating that current ingestion pipelines discard the structural and lexical cues essential for group‑memory reasoning and that multi‑user memory remains an unresolved challenge in agentic AI.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running conversations. However, both existing memory systems and benchmarks are built around the dyadic, single-user setup, even though real deployments routinely span groups and channels with multiple users interacting with the agent and with each other. This mismatch leaves three properties of group memory unmeasured: (i) group dynamics that go beyond concatenated one-on-one chats, (ii) speaker-grounded belief tracking, where the per-user memory modeling is needed, and (iii) audience-adapted language, where Theory-of-Mind shifts produce role-specific vocabulary. We introduce GroupMemBench, a benchmark that exposes all three. A graph-grounded synthesis pipeline produces multi-party conversations with controllable reply structure and conditions each message on per-user personas and target audiences. An adversarial query pipeline then binds every question to a specific asker across six categories, spanning multi-hop reasoning, knowledge update, term ambiguity, user-implicit reasoning, temporal reasoning, and abstention, and iteratively searches challenging, realistic queries that reflect comprehensive memory capability. Benchmarking leading memory systems exposes a sharp collapse: the strongest one reaches only 46.0% average accuracy, with knowledge update at 27.1% and term ambiguity at 37.7%, while a simple BM25 baseline matches or exceeds most agent memory systems. This indicates current memory ingestion erases the structural and lexical features group memory depends on, leaving multi-user memory far from solved.

</details>


### 57. Contestable Multi-Agent Debate with Arena-based Argumentative Computation for Multimedia Verification

- **Authors:** Truong Thanh Hung Nguyen, Vo Thanh Khang Nguyen, Hoang-Loc Cao, Phuc Ho, Van Pham, Hung Cao
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14495v1](http://arxiv.org/abs/2605.14495v1)
- **PDF:** [https://arxiv.org/pdf/2605.14495v1](https://arxiv.org/pdf/2605.14495v1)
- **Categories:** cs.MM, cs.AI


> The paper introduces a contestable multi‑agent architecture for multimedia verification that couples multimodal large language models, external fact‑checking tools, and an arena‑based quantitative bipolar argumentation framework (A‑QBAF). By breaking each verification case into claim‑focused sections, the system retrieves relevant evidence, converts it into structured support/attack arguments with provenance and strength scores, and resolves these via small, locally scoped argument graphs using selective clash resolution and uncertainty‑aware escalation. Experiments on the ICMR 2026 Grand Challenge show that the approach yields fully transparent, editable verification reports with competitive accuracy while remaining computationally tractable, demonstrating a practical pathway for contestable, agentic AI reasoning in multimedia domains.


<details>
<summary>Abstract</summary>

Multimedia verification requires not only accurate conclusions but also transparent and contestable reasoning. We propose a contestable multi-agent framework that integrates multimodal large language models, external verification tools, and arena-based quantitative bipolar argumentation (A-QBAF) as a submission to the ICMR 2026 Grand Challenge on Multimedia Verification. Our method decomposes each case into claim-centered sections, retrieves targeted evidence, and converts evidence into structured support and attack arguments with provenance and strength scores. These arguments are resolved through small local argument graphs with selective clash resolution and uncertainty-aware escalation. The resulting system generates section-wise verification reports that are transparent, editable, and computationally practical for real-world multimedia verification. Our implementation is public at: https://github.com/Analytics-Everywhere-Lab/MV2026_the_liems.

</details>


### 58. LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning

- **Authors:** Xudong Chen, Yixin Liu, Hua Wei, Kaize Ding
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14483v1](http://arxiv.org/abs/2605.14483v1)
- **PDF:** [https://arxiv.org/pdf/2605.14483v1](https://arxiv.org/pdf/2605.14483v1)
- **Categories:** cs.AI


> **Main contribution:** LEMON introduces a fully‑learned, executable orchestration layer for LLM‑driven multi‑agent systems that simultaneously decides agents’ roles, their capacity allocations, and inter‑agent dependencies, and trains this decisions‑maker end‑to‑end with a novel counterfactual reinforcement‑learning signal.

**Methodology:** The authors formulate orchestration as a text generation problem and fine‑tune an LLM orchestrator using a GRPO‑style reinforcement objective augmented with span‑level counterfactual rewards: for each training step they edit a single field (role, capacity, or dependency), run the resulting multi‑agent program, and assign the reward difference only to the edited span, thereby providing fine‑grained credit assignment.

**Key findings:** Across six heterogeneous benchmarks (MMLU, GSM8K, AQuA, MultiArith, SVAMP, HumanEval), LEMON outperforms prior multi‑agent orchestration baselines, achieving new state‑of‑the‑art results while producing a single, deployable orchestration specification. This demonstrates that counterfactual‑driven RL can effectively learn holistic orchestration decisions, a step forward for scalable, agentic AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have become a strong foundation for multi-agent systems, but their effectiveness depends heavily on orchestration design. Across different tasks, role design, capacity assignment, and dependency construction jointly affect both solution quality and execution efficiency. Existing approaches automate parts of this design process, yet they often optimize these decisions partially or sequentially, and rely on execution-level feedback that provides limited credit assignment for local orchestration decisions. We propose LEMON (\textbf{L}earning \textbf{E}xecutable \textbf{M}ulti-agent \textbf{O}rchestratio\textbf{N} via Counterfactual Reinforcement Learning), an LLM-based orchestrator that generates an executable orchestration specification. The specification integrates task-specific roles, customized duties, capacity levels, and dependency structure into a single deployable system. To train the orchestrator, we augment the orchestration-level GRPO objective with a localized counterfactual signal that edits role, capacity, or dependency fields and applies the resulting reward contrast only to the edited spans. Experiments on six reasoning and coding benchmarks, including MMLU, GSM8K, AQuA, MultiArith, SVAMP, and HumanEval, show that LEMON achieves state-of-the-art performance among the evaluated multi-agent orchestration methods. Our code is available at https://anonymous.4open.science/r/LEMON-B23C.

</details>


### 59. LiSA: Lifelong Safety Adaptation via Conservative Policy Induction

- **Authors:** Minbeom Kim, Lesly Miculicich, Bhavana Dalvi Mishra, Mihir Parmar, Phillip Wallis, Bharath Chandrasekhar, Kyomin Jung, Tomas Pfister, Long T. Le
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14454v1](http://arxiv.org/abs/2605.14454v1)
- **PDF:** [https://arxiv.org/pdf/2605.14454v1](https://arxiv.org/pdf/2605.14454v1)
- **Categories:** cs.LG, cs.CL, cs.CR


> **Main contribution** – LiSA introduces a “conservative policy‑induction” framework that lets a static guard‑rail model continually improve its safety behavior from only occasional, noisy user‑reported failures, without requiring costly retraining of the whole model.

**Methodology** – LiSA stores each reported failure in a structured memory, abstracts it into a reusable policy rule, and attaches a conflict‑aware local rule set plus a Bayesian‑style lower‑bound confidence gate so that rules are only applied when sufficient evidence accumulates and contradictory signals are resolved.

**Key findings** – On three realistic agentic‑AI benchmarks (PrivacyLens+, ConFaide+, AgentHarm), LiSA consistently outperforms strong memory‑based baselines despite extremely sparse feedback, remains stable even with 20 % label‑flip noise, and achieves better safety‑latency trade‑offs than simply scaling the underlying model—demonstrating a viable path for lifelong, context‑aware safety adaptation in deployed AI agents.


<details>
<summary>Abstract</summary>

As AI agents move from chat interfaces to systems that read private data, call tools, and execute multi-step workflows, guardrails become a last line of defense against concrete deployment harms. In these settings, guardrail failures are no longer merely answer-quality errors: they can leak secrets, authorize unsafe actions, or block legitimate work. The hardest failures are often contextual: whether an action is acceptable depends on local privacy norms, organizational policies, and user expectations that resist pre-deployment specification. This creates a practical gap: guardrails must adapt to their own operating environments, yet deployment feedback is typically limited to sparse, noisy user-reported failures, and repeated fine-tuning is often impractical. To address this gap, we propose LiSA (Lifelong Safety Adaptation), a conservative policy induction framework that improves a fixed base guardrail through structured memory. LiSA converts occasional failures into reusable policy abstractions so that sparse reports can generalize beyond individual cases, adds conflict-aware local rules to prevent overgeneralization in mixed-label contexts, and applies evidence-aware confidence gating via a posterior lower bound, so that memory reuse scales with accumulated evidence rather than empirical accuracy alone. Across PrivacyLens+, ConFaide+, and AgentHarm, LiSA consistently outperforms strong memory-based baselines under sparse feedback, remains robust under noisy user feedback even at 20% label-flip rates, and pushes the latency--performance frontier beyond backbone model scaling. Ultimately, LiSA offers a practical path to secure AI agents against the unpredictable long tail of real-world edge risks.

</details>


### 60. Prompting Policies for Multi-step Reasoning and Tool-Use in Black-box LLMs with Iterative Distillation of Experience

- **Authors:** Krishna Sayana, Ketan Todi, Ambarish Jash
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14443v1](http://arxiv.org/abs/2605.14443v1)
- **PDF:** [https://arxiv.org/pdf/2605.14443v1](https://arxiv.org/pdf/2605.14443v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces a reinforcement‑learning framework that trains a lightweight “prompter” policy to iteratively distill interaction experience with a frozen, black‑box LLM, using a contrastive buffer that pairs scalar task rewards with dense textual critiques. By optimizing this prompter to generate high‑quality prompts for the frozen worker model, the method amortizes multi‑step prompt refinement into a single‑shot policy that dramatically boosts performance on challenging multi‑step reasoning and tool‑use benchmarks (e.g., raising BBEH logic accuracy from 55 % to 90 % and Tau‑bench tool use from 74 % to 91 %). Compared with evolutionary baselines such as GEPA, the distilled prompting policy attains higher accuracy with far fewer samples and reveals emergent algorithmic heuristics encoded in the learned prompt structures.


<details>
<summary>Abstract</summary>

The shift toward interacting with frozen, "black-box" Large Language Models (LLMs) has transformed prompt engineering from a heuristic exercise into a critical optimization challenge. We propose a Reinforcement Learning (RL) framework for training learned prompting policies via iterative distillation of experience. In this architecture, a lightweight prompter model is optimized to maximize task-specific rewards for a larger, frozen worker LLM. By utilizing a contrastive experience buffer that couples scalar rewards with dense textual critiques, our approach effectively amortizes iterative prompt refinement into single-shot policy weights.
  Our experimental analysis focuses on the Big Bench Extra Hard (BBEH) and Tau-bench suites, covering a diverse range of multi-step reasoning and tool-use tasks. We demonstrate significant gains, improving performance from 55% to 90% in logic-intensive reasoning and 74% to 91% in tool-use tasks. Furthermore, we analyze the structural evolution of prompts, demonstrating how the policy discovers specialized algorithmic heuristics. We provide comprehensive comparisons against state-of-the-art evolutionary baselines like GEPA, showing that iterative distillation achieves superior performance with higher sample efficiency.

</details>


### 61. MemLineage: Lineage-Guided Enforcement for LLM Agent Memory

- **Authors:** Ciyan Ouyang, Rui Hou
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14421v1](http://arxiv.org/abs/2605.14421v1)
- **PDF:** [https://arxiv.org/pdf/2605.14421v1](https://arxiv.org/pdf/2605.14421v1)
- **Categories:** cs.CR, cs.AI


> **MemLineage** proposes a provenance‑based defense for large‑language‑model (LLM) agents that records a cryptographic “lineage” for every memory entry, linking each new piece of information to the signed, Merkle‑logged sources that derived it. The system implements a six‑module architecture—including per‑principal Ed25519 signatures, an RFC‑6962 Merkle log, and a weighted derivation DAG with a max‑of‑strong‑edges propagation rule—to enforce a “chain‑of‑custody” policy: any action whose justification traces back to an untrusted ancestor is blocked, while legitimate recall remains unaffected. Experiments on three memory‑poisoning workloads using a deterministic harness and the AgentDojo benchmark show that MemLineage eliminates all adversarial success (ASR = 0) with sub‑millisecond overhead, outperforming no‑defense and signature‑only baselines and demonstrating practical, low‑cost protection for agentic AI memory.


<details>
<summary>Abstract</summary>

We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry. Recent and concurrent work shows that untrusted content can be written into persistent agent state and re-enter later sessions as an instruction; the remaining systems question is how to preserve useful memory recall while preventing such state from justifying sensitive actions. MemLineage treats this as a chain-of-custody problem rather than a filtering problem. It is a six-module design around an RFC-6962 Merkle log over per-principal Ed25519-signed entries: a weighted derivation DAG records which retrieved entries influenced each new memory, and a max-of-strong-edges propagation rule makes Untrusted-Path Persistence hold for any chain whose attribution edges remain above threshold. The sensitive-action gate then refuses dispatches whose active justification descends from an external ancestor, while still allowing benign recall. We evaluate three defense cells against three memory-poisoning workloads on a deterministic mechanism-isolation harness; MemLineage is the only configuration in that harness that drives all three columns to zero ASR, while sub-millisecond per-operation overhead keeps it well below the noise floor of any LLM call. A Codex-backed AgentDojo bridge further separates strong-model behavior from defense-layer behavior: under an intentionally vulnerable tool-output profile, no-defense and signature-only baselines fail on all six banking pairs, while all MemLineage rows reduce strict AgentDojo ASR to zero. The core deterministic artifacts are byte-equal CI-verified; hosted-model AgentDojo and live-model sweeps are recorded as auditable logs rather than byte-pinned artifacts.

</details>


### 62. Agentic Recommender System with Hierarchical Belief-State Memory

- **Authors:** Xiang Shen, Yuhang Zhou, Yifan Wu, Zhuokai Zhao, Siyu Lin, Lei Huang, Qianqian Zhong, Lizhu Zhang, Benyu Zhang, Xiangjun Fan, Hong Yan
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14401v2](http://arxiv.org/abs/2605.14401v2)
- **PDF:** [https://arxiv.org/pdf/2605.14401v2](https://arxiv.org/pdf/2605.14401v2)
- **Categories:** cs.CL, cs.AI


> The paper introduces **MARS (Memory‑Augmented Agentic Recommender System)**, a novel framework that models recommendation as a partially observable decision problem and equips a large‑language‑model (LLM) agent with a **hierarchical belief‑state memory**. MARS separates raw interaction logs (event memory), mutable fine‑grained preference chunks with strength/evidence tracking (preference memory), and an abstracted natural‑language user profile (profile memory), and it governs their evolution through six operations (extraction, reinforcement, weakening, consolidation, forgetting, resynthesis) scheduled by an LLM‑based planner rather than fixed heuristics. Across four InstructRec benchmark domains, this hierarchical, agent‑driven memory management yields state‑of‑the‑art results—averaging **+26.4 % HR@1** and **+10.3 % NDCG@10** over the strongest baselines—and demonstrates further advantages when the memory lifecycle adapts to evolving user behavior.


<details>
<summary>Abstract</summary>

Memory-augmented LLM agents have advanced personalized recommendation, yet existing approaches universally adopt flat memory representations that conflate ephemeral signals with stable preferences, and none provides a complete lifecycle governing how memory should evolve. We propose MARS (Memory-Augmented Agentic Recommender System), a framework that treats recommendation as a partially observable problem and maintains a structured belief state that progressively abstracts noisy behavioral observations into a compact estimate of user preferences. MARS organizes this belief state into three tiers: event memory buffers raw signals, preference memory maintains fine-grained mutable chunks with explicit strength and evidence tracking, and profile memory distills all preferences into a coherent natural language narrative. A complete lifecycle of six operations -- extraction, reinforcement, weakening, consolidation, forgetting, and resynthesis -- is adaptively scheduled by an LLM-based planner rather than fixed-interval heuristics. Experiments on four InstructRec benchmark domains show that MARS achieves state-of-the-art performance with average improvements of 26.4% in HR@1 and 10.3% in NDCG@10 over the strongest baselines with further gains from agentic scheduling in evolving settings.

</details>


### 63. Nexus : An Agentic Framework for Time Series Forecasting

- **Authors:** Sarkar Snigdha Sarathi Das, Palash Goyal, Mihir Parmar, Nanyun Peng, Vishy Tirumalashetty, Chun-Liang Li, Rui Zhang, Jinsung Yoon, Tomas Pfister
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14389v1](http://arxiv.org/abs/2605.14389v1)
- **PDF:** [https://arxiv.org/pdf/2605.14389v1](https://arxiv.org/pdf/2605.14389v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> **Contribution** – The paper introduces **Nexus**, a multi‑agent framework that treats time‑series forecasting as an agentic reasoning task, explicitly separating macro‑level trend extraction, micro‑level fluctuation analysis, and contextual grounding (e.g., news) before synthesizing a final prediction.  

**Methodology** – Nexus orchestrates specialized agents (or prompting stages) that: (1) isolate seasonal/structural components, (2) model short‑term irregularities, and (3) ingest relevant unstructured text; the agents exchange intermediate representations and produce a unified forecast together with a rationale trace. The system leverages off‑the‑shelf LLMs for each stage rather than training a monolithic model.  

**Key Findings** – Across post‑cutoff datasets (Zillow housing indices and highly volatile equities), Nexus matches or exceeds recent Time‑Series Foundation Models and strong LLM baselines, demonstrating that contemporary LLMs have far stronger innate forecasting capability when their numerical and contextual reasoning are modularized. Moreover, the generated reasoning traces reliably identify the primary drivers of each prediction, highlighting the value of an agentic, interpretable approach for real‑world forecasting.


<details>
<summary>Abstract</summary>

Time series forecasting is not just numerical extrapolation, but often requires reasoning with unstructured contextual data such as news or events. While specialized Time Series Foundation Models (TSFMs) excel at forecasting based on numerical patterns, they remain unaware to real-world textual signals. Conversely, while LLMs are emerging as zero-shot forecasters, their performance remains uneven across domains and contextual grounding. To bridge this gap, we introduce Nexus, a multi-agent forecasting framework that decomposes prediction into specialized stages: isolating macro-level and micro-level temporal fluctuations, and integrating contextual information when available before synthesizing a final forecast. This decomposition enables Nexus to adapt from seasonal signals to volatile, event-driven information without relying on external statistical anchors or monolithic prompting. We show that current-generation LLMs possess substantially stronger intrinsic forecasting ability than previously recognized, depending critically on how numerical and contextual reasoning are organized. Evaluated on data strictly succeeding LLM knowledge cutoffs spanning Zillow real estate metrics and volatile stock market equities, Nexus consistently matches or outperforms state-of-the-art TSFMs and strong LLM baselines. Beyond numerical accuracy, Nexus produces high-quality reasoning traces that explicitly show the fundamental drivers behind each forecast. Our results establish that real-world forecasting is an agentic reasoning problem extending well beyond only sequence modeling.

</details>


### 64. Data-Augmented Game Starts for Accelerating Self-Play Exploration in Imperfect Information Games

- **Authors:** JB Lanier, Nathan Monette, Pierre Baldi, Roy Fox
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14379v1](http://arxiv.org/abs/2605.14379v1)
- **PDF:** [https://arxiv.org/pdf/2605.14379v1](https://arxiv.org/pdf/2605.14379v1)
- **Categories:** cs.LG, cs.AI, cs.GT, cs.MA


> **Main contribution** – The paper introduces **Data‑Augmented Game Starts (DAGS)**, a multi‑agent technique that samples intermediate game states from offline human demonstration data and uses them as starting points for self‑play reinforcement learning. By seeding exploration in strategically relevant subgames, DAGS dramatically speeds up discovery of low‑exploitability policies in large imperfect‑information (2‑player zero‑sum) games.

**Methodology** – DAGS augments regularized policy‑gradient self‑play (e.g., NFSP, PSRO‑PG) with a replay buffer of human‑derived states; during each training episode the agents begin from a randomly drawn state from this buffer rather than from the initial empty board. The authors evaluate the approach on synthetic datasets and on analytically tractable, long‑horizon variants of Kuhn Poker, Goofspiel, and a specially designed counterexample game, measuring exploitability under fixed compute budgets. They also analyze the bias introduced by non‑uniform start distributions and mitigate it via multi‑task observation flags.

**Key findings** – Across all testbeds, DAGS reduces exploitability by 30‑70 % compared with standard self‑play under the same computational budget, especially in games where exploration is otherwise extremely sparse. The bias effect is modest and can be eliminated with the proposed flag mechanism. The work also releases new, more exploration‑challenging OpenSpiel benchmarks, providing a future testbed for agentic AI research in imperfect‑information environments.


<details>
<summary>Abstract</summary>

Finding approximate equilibria for large-scale imperfect-information competitive games such as StarCraft, Dota, and CounterStrike remains computationally infeasible due to sparse rewards and challenging exploration over long horizons. In this paper, we propose a multi-agent starting-state sampling strategy designed to substantially accelerate online exploration in regularized policy-gradient game methods for two-player zero-sum (2p0s) games. Motivated by an assumption that offline demonstrations from skilled humans can provide good coverage of high-level strategies relevant to equilibrium play, we propose the initialization of reinforcement learning data collection at intermediate states sampled from offline data to facilitate exploration of strategically relevant subgames. Referring to this method as Data-Augmented Game Starts (DAGS), we perform experiments using synthetic datasets and analytically tractable, long-horizon control variants of two-player Kuhn Poker, Goofspiel, and a counterexample game designed to penalize biased beliefs over hidden information. Under fixed computational budgets, DAGS enables regularized policy gradient methods to achieve lower exploitability in games with significantly more challenging exploration. We show that augmenting starting state distributions when solving imperfect information games can lead to biased equilibria, and we provide a straightforward mitigation to this in the form of multi-task observation flags. Finally, we release a new set of benchmark environments that drastically increase exploration challenges and state counts in existing OpenSpiel games while keeping exploitability measurements analytically tractable.

</details>


### 65. Herculean: An Agentic Benchmark for Financial Intelligence

- **Authors:** Xueqing Peng, Zhuohan Xie, Yupeng Cao, Haohang Li, Lingfei Qian, Yan Wang, Vincent Jim Zhang, Huan He, Xuguang Ai, Linhai Ma, Ruoyu Xiang, Yueru He, Yi Han, Shuyao Wang, Yuqing Guo, Mingyang Jiang, Yilun Zhao, Youzhong Dong, Xiaoyu Wang, Yankai Chen, Ye Yuan, Qiyuan Zhang, Fuyuan Lyu, Haolun Wu, Yonghan Yang, Zichen Zhao, Yuyang Dai, Fan Zhang, Rania Elbadry, Ayesha Gull, Muhammad Usman Safder, Nuo Chen, Fengbin Zhu, Tianshi Cai, Zimu Wang, Polydoros Giannouris, Yuechen Jiang, Zhiwei Liu, Mohsinul Kabir, Yuyan Wang, Yixiang Zheng, Yangyang Yu, Weijin Liu, Wenbo Cao, Anke Xu, Peng Lu, Jerry Huang, Fengran Mo, Mingquan Lin, Prayag Tiwari, Yijia Zhao, Victor Gutierrez Basulto, Xiao-Yang Liu, Kaleb E Smith, Jiahuan Pei, Arman Cohan, Jimin Huang, Yuehua Tang, Alejandro Lopez-Lira, Xi Chen, Xue Liu, Junichi Tsujii, Jian-Yun Nie, Sophia Ananiadou
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14355v1](http://arxiv.org/abs/2605.14355v1)
- **PDF:** [https://arxiv.org/pdf/2605.14355v1](https://arxiv.org/pdf/2605.14355v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution:** The paper introduces **Herculean**, the first benchmark that evaluates *agentic* financial intelligence by testing AI agents on complete, high‑stakes financial workflows rather than isolated static tasks.

**Methodology:** Four representative financial workflows—**Trading, Hedging, Market Insights, and Auditing**—are formalized as modular MCP (Multi‑Component Process) environments, each equipped with domain‑specific tools, interaction rules, constraints, and explicit success metrics, allowing systematic end‑to‑end comparison of heterogeneous agents.

**Key findings:** State‑of‑the‑art agents handle the relatively short‑horizon, reactive tasks of Trading and Market Insights reasonably well, but falter on Hedging and Auditing, which demand long‑horizon coordination, consistent state management, and rigorous structured verification. This reveals a critical gap: current agents can reason about finance but lack dependable workflow execution capabilities needed for high‑risk professional finance tasks.


<details>
<summary>Abstract</summary>

As AI agents improve, the central question is no longer whether they can solve isolated well-defined financial tasks, but whether they can reliably carry out financial professional work. Existing financial benchmarks offer only a partial view of this ability, as they primarily evaluate static competencies such as question answering, retrieval, summarization, and classification. We introduce Herculean, the first skilled benchmark for agentic financial intelligence spanning four representative workflows, including Trading, Hedging, Market Insights, and Auditing. Each workflow is instantiated as a standardized MCP-based skill environment with its own tools, interaction dynamics, constraints, and success criteria, enabling consistent end-to-end assessment of heterogeneous agent systems. Across frontier agents, we find agents perform relatively well on Trading and Market Insights, but struggle substantially on Hedging and Auditing, where long-horizon coordination, state consistency, and structured verification are critical. Overall, our results point to a key gap in current agents in turning financial reasoning into dependable workflow execution in high-stakes financial workflows.

</details>


### 66. Web Agents Should Adopt the Plan-Then-Execute Paradigm

- **Authors:** Julien Piet, Annabella Chow, Yiwei Hou, Muxi Lyu, Sylvie Venuto, Jinhao Zhu, Raluca Ada Popa, David Wagner
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14290v1](http://arxiv.org/abs/2605.14290v1)
- **PDF:** [https://arxiv.org/pdf/2605.14290v1](https://arxiv.org/pdf/2605.14290v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.SE


> **Main contribution:** The paper argues that the prevailing ReAct “observe‑then‑act” loop is unsafe and inefficient for web‑based LLM agents and proposes making **plan‑then‑execute** the default paradigm, where the agent first compiles a task‑specific program (a static execution graph) and only then runs it on the live web page.  

**Methodology:** The authors re‑examine the WebArena benchmark, showing that every task can be expressed as a pre‑planned program and that ≈ 80 % of tasks are solvable without any runtime LLM inference. They analyze why current browser tools (click, type, scroll) hinder planning—because their semantics depend on the current page state—and advocate for typed, semantically rich website APIs that expose actions and their effects ahead of execution.  

**Key findings:** Plan‑then‑execute eliminates the direct injection path that lets untrusted web content hijack the agent’s control flow, while still achieving comparable task success on WebArena; the primary obstacle is infrastructural—designing clean, auditable web‑interaction primitives—rather than a limitation of LLM models themselves.


<details>
<summary>Abstract</summary>

ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm. We argue that it is the wrong default for web agents. Instead, web agents should default to plan-then-execute: commit to a task-specific program before observing runtime web content, then execute it. The reason is that web content mixes inputs from many parties. An e-commerce product page may combine a seller's listing, customer reviews and sponsored advertisements. Under ReAct, all of this content flows into the model when deciding on the next action, creating a direct path for prompt injections to steer the agent's control flow. Plan-then-execute changes this boundary: untrusted data may influence values or branches inside a predefined execution graph, but it cannot redefine the user task or cause the model to synthesize new actions at runtime. We analyze WebArena, a popular web agent benchmark, and find that all tasks are compatible with plan-then-execute, while 80% can be completed with a purely programmatic plan, without any runtime LLM subroutine. We identify the main barrier to adopting plan-then-execute on the web: For it to work well, tools must map cleanly to semantic actions, with effects known before execution, so agents have enough information to plan. The web does not naturally expose that interface. Browser tools such as click, type, and scroll have page-dependent meanings. Planning at this layer is near-sighted: the agent can only see actions on the current page, and later actions appear only after it acts. Closing this gap requires typed interfaces that turn website interactions from clicks and keystrokes to task-level operations. This is an infrastructure problem, not a modeling problem. Web tasks do not need reactivity by default; they need typed, complete, auditable website APIs.

</details>


### 67. Auditing Agent Harness Safety

- **Authors:** Chengzhi Liu, Yichen Guo, Yepeng Liu, Yuzhe Yang, Qianqi Yan, Xuandong Zhao, Wenyue Hua, Sheng Liu, Sharon Li, Yuheng Bu, Xin Eric Wang
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14271v1](http://arxiv.org/abs/2605.14271v1)
- **PDF:** [https://arxiv.org/pdf/2605.14271v1](https://arxiv.org/pdf/2605.14271v1)
- **Categories:** cs.CL, cs.CY


> **Main contribution** – The paper introduces **HarnessAudit**, a systematic framework for auditing the entire execution trace of LLM‑based agents operating inside tool‑dispatching harnesses, and releases **HarnessAudit‑Bench**, a 210‑task benchmark (covering eight real‑world domains, single‑ and multi‑agent setups, and embedded safety constraints) to evaluate whether harnesses respect permission, intent, and information‑flow policies throughout a trajectory.

**Methodology** – HarnessAudit checks three dimensions on every step of a trace: (1) boundary compliance (unauthorized resource use, forbidden data leaks), (2) execution fidelity (whether the harness follows the prescribed policy), and (3) system stability (crashes, dead‑locks). The authors run ten different harness configurations on frontier LLMs and three multi‑agent orchestration frameworks across the benchmark, logging violations per step and per domain.

**Key findings for agentic AI** – (i) Successful task completion often co‑occurs with unsafe behavior, and the number of violations grows with trajectory length; (ii) safety breaches are most frequent in resource‑access and inter‑agent information‑transfer steps, especially in multi‑agent collaborations; (iii) risk profiles differ markedly across domains and agent roles; and (iv) the design of the harness, rather than the underlying model, determines the upper bound of safe deployment, highlighting the need for trace‑level safety auditing in any agentic AI system.


<details>
<summary>Abstract</summary>

LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components. However, a harness can return a correct, benign answer over a trajectory that accesses unauthorized resources or leaks context to the wrong agent. Output-level evaluation cannot see these failures, yet most safety benchmarks score only final outputs or terminal states, even though many violations occur mid-trajectory rather than at termination. The central question is whether the harness respects user intent, permission boundaries, and information-flow constraints throughout execution. To address this gap, we propose HarnessAudit, a framework that audits full execution trajectories across boundary compliance, execution fidelity, and system stability, with a focus on multi-agent harnesses where these risks are most pronounced. We further introduce HarnessAudit-Bench, a benchmark of 210 tasks across eight real-world domains, instantiated in both single-agent and multi-agent configurations with embedded safety constraints. Evaluating ten harness configurations across frontier models and three multi-agent frameworks, we find that: (i) task completion is misaligned with safe execution, and violations accumulate with trajectory length; (ii) safety risks vary across domains, task types, and agent roles; (iii) most violations concentrate in resource access and inter-agent information transfer; and (iv) multi-agent collaboration expands the safety risk surface, while harness design sets the upper bound of safe deployment.

</details>


### 68. Agentic AI Ecosystems in Higher Education: A Perspective on AI Agents to Emerging Inclusive, Agentic Multi-Agent AI Framework for Learning, Teaching and Institutional Intelligence

- **Authors:** Vidya K Sudarshan, Anushka Sisodia, Reshma A Ramachandra, Sia Batra, Josephine Chong Leng Leng
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14266v1](http://arxiv.org/abs/2605.14266v1)
- **PDF:** [https://arxiv.org/pdf/2605.14266v1](https://arxiv.org/pdf/2605.14266v1)
- **Categories:** cs.AI, cs.CY


> The paper argues that the next generation of AI in higher education must move from isolated, task‑specific tools to a unified, goal‑driven ecosystem of autonomous agents that can jointly plan, reason, and adapt across teaching, learning, and administrative functions. By conducting a thematic literature review, the authors identify four gaps—fragmented single‑agent solutions, weak cross‑functional integration, limited multi‑agent coordination, and a lack of inclusivity—and propose a scalable, human‑aligned multi‑agent framework that embeds adaptive, multimodal support for learners with diverse and special‑educational needs. Their key finding is that such an inclusive, coordinated agentic AI platform could deliver more efficient institutional operations while simultaneously fostering equitable, personalized learning outcomes.


<details>
<summary>Abstract</summary>

Integration of artificial intelligent (AI) agents in higher education is transforming teaching, learning and administrative processes. Although existing AI agents effectively support individual tasks, their implementation remains fragmented and inefficient for handling the complexity of educational institutions. This highlights a significant research gap: the lack of integrated eco-system-level agentic multi-agent AI platform capable of coordinated planning, reasoning, and adaptive decision-making across multiple educational functions. This paper presents a forward-looking perspective on agentic multi-agent AI platform in higher education, consisting interconnected autonomous, goal driven agents that support learning, teaching, and institutional operations. It addresses timely and critical questions: Can agentic AI represent the next generation of intelligent systems in tertiary education? Can they collectively support seamless coordinated operations across teaching, learning and administrative support? To what extent can such systems foster inclusive and equitable learning for diverse learners with special educational needs? To ground this perspective, a thematic analysis of existing literature identifies four dominant themes: task-specific fragmented AI tools, the transition from single-agent to multi-agent systems, limited cross-functional integration, and insufficient focus on inclusivity and accessibility. Findings reveal a clear gap between current AI implementations and the needs of holistic, learner-centered educational ecosystem. The paper synthesizes challenges and outlines future research directions for scalable human-aligned, and inclusive agentic AI platform. The significant contribution is the incorporation of inclusive learning perspectives, highlighting how coordinated agentic multi-agent platform can support diverse learners through adaptive, multimodal interventions.

</details>


### 69. A3D: Agentic AI flow for autonomous Accelerator Design

- **Authors:** Abinand Nallathambi, Christopher Knight, Shantanu Ganguly, Wilfried Haensch, Anand Raghunathan
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15237v1](http://arxiv.org/abs/2605.15237v1)
- **PDF:** [https://arxiv.org/pdf/2605.15237v1](https://arxiv.org/pdf/2605.15237v1)
- **Categories:** cs.AR, cs.AI


> **Main contribution**  
The paper introduces **A3D**, a fully agentic AI workflow that autonomously designs hardware accelerators from high‑level scientific codes, handling everything from workload profiling to micro‑architecture generation and speed‑area trade‑off exploration.

**Methodology**  
A3D decomposes the accelerator‑design pipeline into specialized large‑language‑model agents (e.g., workload analyzer, code refactorer, micro‑architecture generator, verifier) that iteratively invoke each other and external tools (Claude Sonnet 4.5, Catapult HLS). Agentic retrieval‑augmented generation (RAG) is used to consult codebases and proprietary EDA documentation, while verifier agents enforce correctness at each stage.

**Key findings**  
When applied to complex, irregular scientific applications (LAMMPS and QMCPACK), A3D produced functional accelerator implementations with comparable performance‑to‑area characteristics to hand‑crafted designs, all without human intervention—demonstrating that coordinated LLM agents can close the remaining manual gaps in AI‑assisted hardware design.


<details>
<summary>Abstract</summary>

Accelerating applications through the design of hardware accelerators can significantly enhance system performance and energy efficiency. Despite advances, such as high-level synthesis (HLS), designing accelerators for complex applications still remains highly labor-intensive, demanding considerable expertise in understanding workloads to be accelerated, hardware design, micro-architecture, and EDA tool usage, posing challenges for application domain experts. Therefore, most accelerator solutions are limited to applications with a regular predictable dataflow. Advances in AI have enabled agents that perform autonomous planning, reasoning, execution and reflection, leading to unprecedented potential for automation through agentic AI. We present A3D, an Agentic AI flow for end-to-end Automation of hardware Accelerator Design. A3D automates workload analysis, performance bottleneck identification, code refactoring for HLS compatibility and micro-architecture generation. A3D also generates diverse accelerator designs by automatically exploring the speed-area tradeoff space. Recent efforts have explored the use of AI for specific tasks such as design space exploration in HLS, leaving several tasks to still be performed manually. A3D addresses the challenges in applying modern LLMs to accelerator design by judiciously partitioning tasks among specialist agents, orchestrating process loops with specialist and verifier agents, utilizing pre-existing and custom tools, and employing agentic RAG for codebase and proprietary EDA tool documentation exploration. Our implementation of A3D, using commercial components like Claude Sonnet 4.5 and the Catapult HLS tool, demonstrates its effectiveness by generating accelerator designs with no human intervention from complex scientific applications like LAMMPS (molecular dynamics simulation) and QMCPACK (quantum chemistry).

</details>


### 70. Latency-Quality Routing for Functionally Equivalent Tools in LLM Agents

- **Authors:** Kexin Chu, Dawei Xiang, Wei Zhang
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14241v1](http://arxiv.org/abs/2605.14241v1)
- **PDF:** [https://arxiv.org/pdf/2605.14241v1](https://arxiv.org/pdf/2605.14241v1)
- **Categories:** cs.LG


> **Main contribution**: The paper introduces **LQM‑ContextRoute**, a contextual‑bandit router that selects among multiple functionally equivalent tool providers (e.g., different web‑search APIs, retrievers, or LLM back‑ends) by explicitly **matching latency to expected answer quality** rather than using a simple additive latency‑penalty reward.

**Methodology**: The router computes a **capacity‑aware score** for each provider—expected answer quality divided by the service‑cycle time—augmented with query‑specific quality predictions and online feedback from an “LLM‑as‑judge” evaluator. This contextual bandit framework adapts in real time to changes in load, provider reliability, and heterogeneous quality.

**Key findings**: Across three benchmarks, LQM‑ContextRoute outperforms the standard SW‑UCB baseline: +2.18 pp F1 on a web‑search load test, up to +18 pp accuracy on a heterogeneous StrategyQA task, and +2.9–3.2 pp NDCG on mixed retriever pools. The results demonstrate that treating latency as a service‑capacity constraint yields a superior latency‑quality trade‑off for same‑function tool routing in LLM agents.


<details>
<summary>Abstract</summary>

Tool-augmented LLM agents increasingly access the same tool type through multiple functionally equivalent providers, such as web-search APIs, retrievers, or LLM backends exposed behind a shared interface. This creates a provider-routing problem under runtime load: the router must choose among providers that differ in latency, reliability, and answer quality, often without gold labels at deployment time. We introduce LQM-ContextRoute, a contextual bandit router for same-function tool providers. Its key design is latency-quality matching: instead of letting low latency offset poor answers in an additive reward, the router ranks providers by expected answer quality per service cycle. It combines this capacity-aware score with query-specific quality estimation and LLM-as-judge feedback, allowing it to adapt online to both load changes and provider-quality differences. On the main web-search load benchmark, LQM-ContextRoute improves F1 by +2.18 pp over SW-UCB while staying on the latency-quality frontier. In a high-heterogeneity StrategyQA setting, LQM-ContextRoute avoids additive-reward collapse and improves accuracy by up to +18 pp over SW-UCB; on heterogeneous retriever pools, it improves NDCG by +2.91--+3.22 pp over SW-UCB. These results show that same-function tool routing benefits from treating latency as service capacity, especially when runtime pressure and provider-quality heterogeneity coexist.

</details>


### 71. Good to Go: The LOOP Skill Engine That Hits 99% Success and Slashes Token Usage by 99% via One-Shot Recording and Deterministic Replay

- **Authors:** Xiaohua Wang, Kai Yu, XuXiao Liang, Liang Wang, Chao Han
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14237v1](http://arxiv.org/abs/2605.14237v1)
- **PDF:** [https://arxiv.org/pdf/2605.14237v1](https://arxiv.org/pdf/2605.14237v1)
- **Categories:** cs.AI


> The paper introduces **LOOP Skill Engine**, a system that converts the first‑run, fully‑LLM‑driven execution of a periodic task into a deterministic, template‑based “Loop Skill” that can be replayed without any further LLM calls. The methodology records the complete tool‑call trace, extracts a length‑descending, branch‑free template that parametrizes only time‑ and result‑dependent variables, and then resolves these variables at runtime to replay the exact same sequence deterministically, with safety guarantees for concurrent writes. Empirically, the engine attains ≈99 % success while slashing token usage by up to 99 % (93‑99.98 % monthly savings) and cutting latency by ~8.7× across tasks ranging from minutes to a day, thereby offering a highly reliable, low‑cost alternative for repetitive agentic AI workloads.


<details>
<summary>Abstract</summary>

Deploying AI agents for repetitive periodic tasks exposes a critical tension: Large Language Models (LLMs) offer unmatched flexibility in tool orchestration, yet their inherent stochasticity causes unpredictable failures, and repeated invocations incur prohibitive token costs. We present the LOOP SKILL ENGINE, a system that achieves a combined 99% success rate and 99% token reduction for periodic agent tasks through a one-shot recording, deterministic replay paradigm. On its first run, the agent executes the task with full LLM reasoning while the system transparently intercepts and records the complete tool-call trajectory. A greedy length-descending template extraction algorithm then converts this recording into a parameterized, branch-free Loop Skill -- a deterministic execution plan that captures the task's functional intent while parameterizing time-dependent and result-dependent variables. All subsequent executions bypass the LLM entirely: the engine resolves template variables against real-time values and replays the tool sequence deterministically. We prove two theorems: (1) Replay Determinism -- the step sequence of a validated Loop Skill is invariant across all future executions; (2) Write Safety -- concurrent access to persistent configuration is serialized through reentrant locks and atomic file replacement. Across a benchmark of periodic agent tasks spanning intervals from 5 minutes to 24 hours, the Loop Skill Engine reduces monthly token consumption by 93.3%--99.98% and cuts execution latency by 8.7x while eliminating output non-determinism. A multi-layer degradation strategy guarantees that tasks never stall. We release the engine as part of the buddyMe open-source agent framework.

</details>


### 72. MetaAgent-X : Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning

- **Authors:** Yaolun Zhang, Yujie Zhao, Nan Wang, Yiran Wu, Jiayu Chang, Yizhao Chen, Qingyun Wu, Jishen Zhao, Huazheng Wang
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14212v1](http://arxiv.org/abs/2605.14212v1)
- **PDF:** [https://arxiv.org/pdf/2605.14212v1](https://arxiv.org/pdf/2605.14212v1)
- **Categories:** cs.AI


> **Main contribution:** MetaAgent‑X is the first end‑to‑end reinforcement‑learning framework that simultaneously learns how to **design** a multi‑agent system (the “designer”) and how the resulting agents **execute** tasks (the “executor”), breaking the “frozen‑executor” limitation of prior automatic MAS methods.  

**Methodology:** The system generates script‑based MAS specifications, runs execution rollouts, and assigns credit jointly to designer and executor trajectories. Stability and scalability are achieved with two novel mechanisms: (1) **Executor‑Designer Hierarchical Rollout**, which nests execution traces inside designer updates, and (2) **Stagewise Co‑evolution**, a curriculum that alternates focus between improving the designer and the executor.  

**Key findings:** Across several benchmark environments, MetaAgent‑X yields up to **21.7 %** higher performance than state‑of‑the‑art automatic MAS baselines, and ablation studies confirm that both designer and executor improve continuously, following a predictable stagewise co‑evolution pattern—demonstrating that fully trainable, self‑designing/self‑executing agentic systems are now feasible.


<details>
<summary>Abstract</summary>

Automatic multi-agent systems aim to instantiate agent workflows without relying on manually designed or fixed orchestration. However, existing automatic MAS approaches remain only partially adaptive: they either perform training-free test-time search or optimize the meta-level designer while keeping downstream execution agents frozen, which creating a frozen-executor ceiling and leaving the end-to-end training of self-designing and self-executing agentic models unexplored. To address this, we introduce MetaAgent-X, an end-to-end reinforcement learning framework that jointly optimizes automatic MAS design and execution. MetaAgent-X enables script-based MAS generation, execution rollout collection, and credit assignment for both designer and executor trajectories. To support stable and scalable optimization, we propose Executor Designer Hierarchical Rollout and Stagewise Co-evolution to improve training stability and expose the dynamics of designer-executor co-evolution. MetaAgent-X consistently outperforms existing automatic MAS baselines, achieving up to 21.7% gains. Comprehensive ablations show that both designer and executor improve throughout training, and that effective automatic MAS learning follows a stagewise co-evolution process. These results establish end-to-end trainable automatic MAS as a practical paradigm for building self-designing and self-executing agentic models.

</details>


### 73. SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents

- **Authors:** Zahra Zanjani Foumani, Alberto Castelo, Shuang Xie, Ted Chaiwachirasak, Han Li, Lingyun Wang
- **Published:** 2026-05-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14205v2](http://arxiv.org/abs/2605.14205v2)
- **PDF:** [https://arxiv.org/pdf/2605.14205v2](https://arxiv.org/pdf/2605.14205v2)
- **Categories:** cs.AI


> The paper introduces **SimPersona**, a framework that automatically extracts a finite set of “buyer personas” from raw e‑commerce click‑streams using a behavior‑aware VQ‑VAE, and then injects these discrete persona tokens into LLM‑driven web shopping agents. By fine‑tuning the agents with persona‑conditioned traces, SimPersona can assign any new shopper to a learned type with a single encoder pass and sample realistic buyer populations for a given store without hand‑crafted prompts; on 8.37 M real buyers across 42 held‑out storefronts it achieves 78 % alignment with actual conversion rates and surpasses a much larger baseline on goal‑oriented shopping tasks, while also providing interpretable behavioral differences among personas.


<details>
<summary>Abstract</summary>

LLM-based web agents can navigate live storefronts, yet they often collapse to a single "average buyer" policy, failing to capture the heterogeneous and distributional nature of real buyer populations. Existing personalization methods rely on hand-crafted prompt-based personas that are brittle, difficult to scale, context-inefficient, and unable to faithfully represent population-level behavior. We introduce SimPersona, a novel framework that learns discrete buyer types from historical traffic and exposes them to LLM-based web agents as compact persona tokens. Given raw clickstreams, a behavior-aware VQ-VAE induces a discrete buyer-type space that captures the statistical structure of real buyer behavior and merchant-specific buyer population distributions. To provide behavior-specific guidance to LLM-based web agents, SimPersona maps each learned buyer type to a dedicated persona token in the LLM agent vocabulary and fine-tunes the agent with these tokens on real browsing traces. At inference, each synthetic buyer is assigned to a learned buyer type with a single encoder forward pass, requiring no retraining or store-specific prompt engineering. For population-level simulation, SimPersona samples buyer types from each merchant's empirical distribution over the learned VQ-VAE codebook and instantiates agents with the corresponding persona tokens, preserving merchant-specific buyer population distributions. Evaluated on $8.37$M buyers across $42$ held-out live storefronts, SimPersona achieves $78\%$ conversion-rate alignment with real buyers, exhibits interpretable behavioral variation across buyer types, and outperforms a baseline with $8\times$ more parameters on goal-oriented shopping tasks. We further release an open-source data pipeline that converts raw e-commerce event logs into buyer representations and agent-training traces.

</details>


### 74. Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations

- **Authors:** Qisong He, Yi Dong, Xiaowei Huang
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14175v1](http://arxiv.org/abs/2605.14175v1)
- **PDF:** [https://arxiv.org/pdf/2605.14175v1](https://arxiv.org/pdf/2605.14175v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces *Grounded Continuation*, a linear‑time runtime verifier that tracks the logical dependencies of each utterance in a long LLM‑driven conversation, thereby preventing “stale‑premise” confabulation and context‑manipulation attacks.  

**Methodology:** At every turn the LLM classifies the utterance into one of eight update operations drawn from four formalisms (dynamic epistemic logic, abductive reasoning, awareness logic, and argumentation). A symbolic engine builds a dependency graph linking claims to their supporting evidence; checking a continuation’s validity becomes a simple graph walk, and retractions propagate through the same graph to flag unsupported conclusions, all with O(1) per‑turn overhead and a formal guarantee of conflict‑free updates.  

**Key findings:** On the LongMemEval‑KU benchmark the verifier achieves 89.7 % accuracy (up to +2.6 pp over strong retrieval‑augmented baselines), matches retrieval‑augmented performance on LoCoMo QA, and attains 100 % accuracy on a curated stale‑premise test (versus 93.3 % for baselines). The retraction check runs in microseconds, confirming that the approach scales linearly with conversation length while providing a sound, empirically‑measurable layer of grounding for agentic AI systems.


<details>
<summary>Abstract</summary>

In long conversations, an LLM can produce a next utterance that sounds plausible but rests on premises the conversation has already abandoned. Context-manipulation attacks against deployed agents now actively exploit this gap. We close it with a runtime verifier that maintains an explicit dependency graph: an LLM classifies each turn into one of 8 update operations drawn from four formalisms (dynamic epistemic logic, abductive reasoning, awareness logic, argumentation), and a symbolic engine records which claims depend on which evidence. Checking whether a continuation is supported reduces to a graph walk; retraction propagates through the same graph to flag exactly the conclusions that lose support, with linear per-turn cost and a formal conflict-free guarantee. On LongMemEval-KU oracle (n=78), the verifier reaches 89.7% accuracy vs. 88.5% for the LLM-only baseline (+1.3pp) and 87.2% for a transcript-RAG baseline matched on retrieval budget (+2.6pp); wins among disagreements are correct abstentions where the baseline confabulates. On LoCoMo's 60 official QA items the verifier is competitive with retrieval-augmented baselines. Beyond external benchmarks, we construct two multi-agent scenarios and a 50-item grounding test: on the 15-item stale-premise subset, the verifier reaches 100% accuracy vs. 93.3% (+6.7pp). These instantiate a soundness-faithfulness decomposition: the structural check is sound by construction, and per-deployment LLM extraction faithfulness is the empirical question we measure across four LLM families. The retraction check plateaus at microseconds while history-replay grows linearly with conversation length.

</details>


### 75. Distribution-Aware Algorithm Design with LLM Agents

- **Authors:** Saharsh Koganti, Priyadarsi Mishra, Pierfrancesco Beneventano, Tomer Galanti
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14141v1](http://arxiv.org/abs/2605.14141v1)
- **PDF:** [https://arxiv.org/pdf/2605.14141v1](https://arxiv.org/pdf/2605.14141v1)
- **Categories:** cs.AI


> **Main contribution** – The paper introduces a distribution‑aware framework for automatically generating *executable* solvers from data, where a “solver hint” (a reusable structural pattern inferred from training instances) is compiled into specialized code. It shows theoretically that the empirically fastest solver consistent with the training samples generalizes both in correctness and runtime, and that such hints can be identified from a polynomial number of examples.

**Methodology** – The authors formalize solver hints and prove generalization guarantees, then instantiate the idea with large‑language‑model (LLM) code agents that synthesize solvers for 21 combinatorial‑optimization distributions across seven problem classes. The agents are supplied with sample problem–solution pairs, learn a hint, and generate tailored solver implementations that are benchmarked on fresh test instances.

**Key findings** – The LLM‑generated solvers achieve a mean normalized solution quality of 0.971, surpassing the average heuristic pool by +0.224 and the best heuristic by +0.098, while being dramatically faster (≈ 337× faster than the quality‑best heuristic, ≈ 343× faster than Gurobi, and ≈ 16× faster than a time‑limited exact backend). On the PACE 2025 Dominating Set private test set, the synthesized solver solves all 100 graphs and runs about two orders of magnitude faster than top competition solvers, demonstrating that distribution‑specific code compilation yields substantial speed‑quality trade‑offs for agentic AI systems.


<details>
<summary>Abstract</summary>

We study learning when the learned object is executable solver code rather than a predictor. In this setting, correctness is not enough: two solvers may both return valid solutions on the deployment distribution while differing substantially in runtime. Given samples from an unknown task distribution, the learner returns code evaluated on fresh instances by both solution quality and execution time. Our central abstraction is a \emph{solver hint}: reusable structure inferred from samples and compiled into specialized solver code. We prove that the empirically fastest sample-consistent solver from a fixed library generalizes in both correctness and runtime, and that statistically identifiable hints can be recovered and compiled from polynomially many samples.
  Empirically, we instantiate the framework with LLM code agents on \(21\) structured combinatorial-optimization target distributions across seven problem classes. The synthesized solvers reach mean normalized quality \(0.971\), improve by \(+0.224\) over the average heuristic pool and by \(+0.098\) over the highest-quality heuristic, and are \(336.9\times\), \(342.8\times\), and \(16.1\times\) faster than the quality-best heuristic, Gurobi, and the selected time-limited exact backend, respectively. On released PACE 2025 Dominating Set private instances, the synthesized solver is valid on all \(100\) graphs and runs about two orders of magnitude faster than top competition solvers, with a moderate quality gap. Inspection shows that many gains come from changing the computational scale: replacing ambient exponential search or general-purpose optimization with compiled distribution-specific computation.

</details>


### 76. Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)

- **Authors:** Marius S. Knorr, Robert Müller, Jan P. Bremer, Nils Schweingruber
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14126v1](http://arxiv.org/abs/2605.14126v1)
- **PDF:** [https://arxiv.org/pdf/2605.14126v1](https://arxiv.org/pdf/2605.14126v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution:** The paper introduces a reinforcement‑learning (RL) post‑training pipeline that turns multi‑turn, tool‑calling LLM agents into reliable “FHIR‑Agents” capable of navigating the graph‑structured electronic health‑record data defined by the Fast Healthcare Interoperability Resources (FHIR) standard, while respecting traversal and data‑integrity constraints.

**Methodology:** The authors cast FHIR reasoning as a sequential decision‑making problem over a queryable graph, build a custom RL environment and harness that integrates retrieval, code execution, and graph‑traversal tools, and train a CodeAct‑style agent with policy‑gradient updates using execution‑grounded rewards supplied by an LLM judge. The pipeline includes environment construction, reward design, and evaluation on the FHIR‑AgentBench benchmark.

**Key findings:** RL post‑training dramatically boosts answer correctness—raising performance from ~50 % (prompt‑only o4‑mini) to 77 % on FHIR‑AgentBench—using a modest Qwen‑3‑8B model, and it enforces the required FHIR graph constraints more consistently than closed‑model baselines. This demonstrates that RL fine‑tuning is an effective, inexpensive way to improve multi‑turn, tool‑calling agents for complex, structured clinical domains.


<details>
<summary>Abstract</summary>

Fast Healthcare Interoperability Resources (FHIR) is the dominant standard for interoperable exchange of healthcare data. In FHIR, electronic health records form a directed graph of resources. Answering clinically meaningful questions over FHIR requires agents to perform multi-step reasoning, filtering, and aggregation across multiple resource types. Prior work shows that even tool-augmented LLM agents (retrieval, code execution, multi-turn planning) often select the wrong resources or violate traversal constraints. We study this problem in the context of FHIR-AgentBench, a benchmark for realistic question answering over real-world hospital data, and frame reasoning on FHIR as a sequential decision-making problem over a queryable structured graph. We implement a multi-turn CodeAct agent and post-train it with reinforcement learning using a custom harness and tools. A LLM Judge provides execution-grounded rewards. Compared to prompt-based, closed-model baselines, RL post-training improves performance while enforcing data-integrity constraints. Empirically, our approach improves answer correctness from 50% (o4-mini) to 77% on FHIR-AgentBench using a smaller and cheaper Qwen3-8B model. We present an end-to-end post-training pipeline (environment building, harness construction, model training and custom evaluation) that reliably improves multi-turn reasoning over structured clinical graphs.

</details>


### 77. Privacy Preserving Multi Agent Path Finding

- **Authors:** Rotem Lev Lehman, Roni Stern, Guy Shani
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14119v1](http://arxiv.org/abs/2605.14119v1)
- **PDF:** [https://arxiv.org/pdf/2605.14119v1](https://arxiv.org/pdf/2605.14119v1)
- **Categories:** cs.MA


> **Contribution:** The paper introduces the first systematic treatment of privacy in multi‑agent path finding (MAPF), defining *planning‑level* privacy (agents must not learn the exact planned locations of others) and *execution‑level* privacy (agents must not be able to sense each other’s positions during execution), and provides algorithms that guarantee both.  

**Methodology:**  
1. For planning‑level privacy, the authors construct a generic framework that inserts “mock agents” into the planner so that real agents cannot infer others’ true routes.  
2. For execution‑level privacy, they modify two state‑of‑the‑art MAPF solvers—Priority Inheritance with Backtracking (PIBT) and LaCAM—so that decisions are made without any inter‑agent sensing.  
3. They add a post‑processing step that locally rewires the collision‑free paths to lower the total sum‑of‑cost while preserving the privacy guarantees.  

**Key Findings:** Empirical experiments on standard MAPF benchmarks show that the privacy‑preserving variants retain comparable success rates to the original algorithms, and the post‑processing stage yields a substantial reduction in total path cost (up to ~20 % in many scenarios) without violating either privacy guarantee. This demonstrates that strong privacy can be achieved in MAPF without sacrificing solution quality, opening a path for privacy‑aware agentic AI deployments in logistics, robotics, and distributed systems.


<details>
<summary>Abstract</summary>

In the multi-agent path finding (MAPF) problem, a group of agents search in a graph for a path for each agent where no two paths collide. While in all applications of MAPF the agents must not collide with each other, in some of them the agents may not wish to share their paths due to privacy constraints. In this work, we formulate two types of privacy constraints for MAPF and propose algorithms that preserve them. The first type of privacy we consider is planning-level privacy, which means that during planning, the agents cannot identify exactly the planned location of the other agents. We propose a general framework for obtaining planning-level privacy, which works by adding mock agents to the planning process. The second type of privacy we consider is execution-level privacy, which is relevant when agents have limited sensing capabilities. Execution-level privacy is preserved if none of the agents is allowed to sense the location of the other agents during execution. We show how to adapt two popular MAPF algorithms, namely PIBT and LaCAM, such that they preserve execution-level privacy. Lastly, we propose a post-processing technique that allows the agents to reduce the sum of costs of the returned solution without losing any privacy. We also implemented our algorithms and evaluated them empirically, showing that the proposed post-processing technique indeed improved cost significantly.

</details>


### 78. ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation

- **Authors:** Tarun Mittal
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14102v1](http://arxiv.org/abs/2605.14102v1)
- **PDF:** [https://arxiv.org/pdf/2605.14102v1](https://arxiv.org/pdf/2605.14102v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **ChromaFlow**, a diagnostic framework for evaluating the hidden operational costs of tool‑augmented autonomous language‑model agents, and conducts a *negative ablation* that shows aggressive orchestration (more planner escalations, tool calls, and logging) does not improve overall task accuracy while inflating failures and resource usage.  

**Methodology:** The authors instrumented ChromaFlow with planner‑directed execution, specialized tool wrappers, and telemetry collection, then ran it on the GAIA 2023 Level‑1 benchmark (53 tasks) under (i) a frozen baseline configuration and (ii) a “recovery” configuration with expanded orchestration; they also performed two random 20‑task smoke tests to assess stability.  

**Key findings:** The baseline solved 29/53 (≈55 %) of tasks, whereas the more aggressive orchestration solved only 27/53 (≈51 %) and generated significantly more timeouts, tool‑failure traces, and token‑level overhead. Small gains observed in the random smoke sets were unstable, leading the authors to recommend bounded planner escalation, deterministic extraction, evidence reconciliation, and explicit execution gating as essential design constraints for reliable, reproducible evaluation of agentic AI systems.


<details>
<summary>Abstract</summary>

Autonomous language-model agents increasingly combine planning, tool use, document processing, browsing, code execution, and verification loops. These capabilities make agent systems more useful, but they also introduce operational failure modes that are not visible from final accuracy alone. This report presents ChromaFlow, a tool-augmented autonomous reasoning framework built around planner-directed execution, specialized tool use, and telemetry-driven evaluation. We analyze ChromaFlow on GAIA 2023 Level-1 validation tasks under clean evaluation constraints. A frozen full Level-1 baseline achieved 29/53 correct answers, or 54.72%. A later recovery configuration with expanded orchestration achieved 27/53 correct answers, or 50.94%, while increasing tracebacks, timeout events, tool-failure mentions, token-line calls, and campaign-log cost estimates. Two randomized 20-task smoke evaluations produced 12/20 and 11/20 correct answers, showing that small diagnostic gains can be unstable across samples. The central result is therefore a negative ablation: more aggressive orchestration did not improve full-set performance and increased operational noise. The report argues that bounded planner escalation, deterministic extraction, evidence reconciliation, and explicit run gates should be treated as first-order requirements for reliable autonomous agent evaluation.

</details>


### 79. CRANE: Constrained Reasoning Injection for Code Agents via Nullspace Editing

- **Authors:** Mingzhi Zhu, Michele Merler, Raju Pavuluri, Stacy Patterson
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14084v1](http://arxiv.org/abs/2605.14084v1)
- **PDF:** [https://arxiv.org/pdf/2605.14084v1](https://arxiv.org/pdf/2605.14084v1)
- **Categories:** cs.SE, cs.AI, cs.CL


> The paper introduces **CRANE**, a training‑free parameter‑editing technique that fuses a “Thinking” checkpoint (strong at long‑horizon planning) with an “Instruct” checkpoint (compact and tool‑ disciplined) by editing the Instruct model along the null‑space directions defined by their weight difference. CRANE first denoises the delta with magnitude thresholding, then selects edits that simultaneously improve reasoning and preserve tool‑use via a Conservative Taylor Gate, and finally suppresses updates that would break output formatting using a Graduated Sigmoidal Projection. Applied to Qwen‑series code agents, CRANE yields large gains over either source model—e.g., +19.5 % pass‑1 on Roo‑Eval for Qwen3‑30B‑A3B and up to +30 % pass‑5 on Terminal‑Bench v2—while maintaining the efficiency and strict tool‑use behavior of the original Instruct model.


<details>
<summary>Abstract</summary>

Code agents must both reason over long-horizon repository state and obey strict tool-use protocols. In paired Instruct/Thinking checkpoints, these capabilities are complementary but misaligned. The Instruct model is concise and tool-disciplined, whereas the Thinking model offers stronger planning and recovery behavior but often over-deliberates and degrades agent performance. We present CRANE (Constrained Reasoning Injection for Code Agents via Nullspace Editing), a training-free parameter-editing method that treats the Thinking-Instruct delta as a directional pool of candidate reasoning edits for the Instruct backbone. CRANE combines magnitude thresholding to denoise the delta, a Conservative Taylor Gate to retain edits that are jointly beneficial for reasoning transfer and tool-use preservation, and Graduated Sigmoidal Projection to suppress format-critical update directions. By merging paired Instruct and Thinking checkpoints, CRANE delivers strong gains over either individual model while preserving Instruct-level efficiency: on Roo-Eval it achieves pass1 of 66.2% (+19.5%) for Qwen3-30B-A3B and 81.5% (+8.7%) for Qwen3-Next-80B-A3B; on SWE-bench-Verified it resolves up to 14 additional instances at both scales (122/500 and 180/500); and on Terminal-Bench v2 it improves pass1/pass5 by up to 2.3%/7.8%, reaching 7.6%/17.9% and 14.8%/30.3%, respectively, consistently outperforming alternative merging strategies across all three benchmarks.

</details>


### 80. SPIN: Structural LLM Planning via Iterative Navigation for Industrial Tasks

- **Authors:** Yusuke Ozaki, Dhaval Patel
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14051v1](http://arxiv.org/abs/2605.14051v1)
- **PDF:** [https://arxiv.org/pdf/2605.14051v1](https://arxiv.org/pdf/2605.14051v1)
- **Categories:** cs.AI


> The paper introduces **SPIN**, a lightweight wrapper that turns any Large‑Language‑Model planner into a validator‑guided DAG planner. SPIN first parses the LLM‑generated workflow, checks it against a strict directed‑acyclic‑graph contract, and uses repair‑prompting to produce a structurally sound plan; then it executes the plan incrementally, stopping as soon as the current DAG prefix already solves the user query. Across two industrial benchmarks (AssetOpsBench = 261 scenarios and MCP Bench), SPIN cuts the number of executed tasks by ∼40 % (from 1 061 to 623), lowers tool‑call cost (11.81 → 6.82 calls per run), and raises the “Accomplished” success metric from 0.638 to 0.706, while also improving planning, grounding, and dependency scores for both GPT‑OSS1 and Llama‑4‑Maverick.


<details>
<summary>Abstract</summary>

Industrial LLM agent systems often separate planning from execution, yet LLM planners frequently produce structurally invalid or unnecessarily long workflows, leading to brittle failures and avoidable tool and API cost. We propose \texttt{SPIN}, a planning wrapper that combines validated Directed Acyclic Graph (DAG) planning with prefix based execution control. \texttt{SPIN} enforces a strict DAG contract through \texttt{\_validate\_plan\_text} and repair prompting, producing executable plans before downstream execution, and then evaluates DAG prefixes incrementally to stop when the current prefix is sufficient to answer the query. On AssetOpsBench, across 261 scenarios, \texttt{SPIN} reduces executed tasks from 1061 to 623 and improves \emph{Accomplished} from 0.638 to 0.706, while reducing tool calls from 11.81 to 6.82 per run. On MCP Bench, the same wrapper improves planning, grounding, and dependency related scores for both GPT OSS1 and Llama 4 Maverick.

</details>


### 81. Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use

- **Authors:** Yize Cheng, Chenrui Fan, Mahdi JafariRaviz, Keivan Rezaei, Soheil Feiz
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14038v1](http://arxiv.org/abs/2605.14038v1)
- **PDF:** [https://arxiv.org/pdf/2605.14038v1](https://arxiv.org/pdf/2605.14038v1)
- **Categories:** cs.AI


> **Main contribution:** The paper defines *model‑adaptive tool necessity*—whether a given LLM can solve a task without external assistance based on its own empirical performance—and shows that existing LLM agents frequently mis‑align their tool‑calling behavior with this necessity, exposing a “knowing‑doing” gap in autonomous tool use.

**Methodology:** The authors evaluate four LLMs on arithmetic and factual‑question datasets, labeling each instance as tool‑necessary or not according to each model’s success rate. They then probe the models’ hidden states to separate (i) a *cognition* stage (the model’s internal belief about tool necessity) from (ii) an *execution* stage (the actual token‑level decision to call a tool), measuring linear decodability and the alignment of the two decision directions across layers.

**Key findings:** Mismatches between predicted necessity and observed tool calls range from ~26 % to 54 % (arithmetic) and 31 % to 42 % (facts). Both cognition and execution signals are decodable, but their internal representations become nearly orthogonal in late layers, and the majority of errors arise during the transition from cognition to action—not from failing to recognize necessity. This reveals that improving tool‑use reliability in agentic AI requires mechanisms that better translate a model’s internal recognition of tool need into concrete tool‑calling actions.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly act as autonomous agents that must decide when to answer directly vs. when to invoke external tools. Prior work studying adaptive tool use has largely treated tool necessity as a model-agnostic property, annotated by human or LLM judge, and mostly cover cases where the answer is obvious (e.g., fetching the weather vs. paraphrasing text). However, tool necessity in the wild is more nuanced due to the divergence of capability boundaries across models: a problem solvable by a strong model on its own may still require tools for a weaker one. In this work, we introduce a model-adaptive definition of tool-necessity, grounded in each model's empirical performance. Following this definition, we compare the necessity against observed tool-call behavior across four models on arithmetic and factual QA dataset, and find substantial mismatches of 26.5-54.0% and 30.8-41.8%, respectively. To diagnose the failure, we decompose tool use into two stages: an internal cognition stage that reflects whether a model believes a tool is necessary, and an execution stage that determines whether the model actually makes a tool-call action. By probing the LLM hidden states, we find that both signals are often linearly decodable, yet their probe directions become nearly orthogonal in the late-layer, last-token regime that drives the next-token action. By tracing the trajectory of samples in the two-stage process, we further discover that the majority of mismatch is concentrated in the cognition-to-action transition, not in cognition itself. These results reveal a knowing-doing gap in LLM tool-use: improving tool-use reliability requires not only better recognition of when tools are needed, but also better translation of that recognition into action.

</details>


### 82. Sheaf-Theoretic Transport and Obstruction for Detecting Scientific Theory Shift in AI Agents

- **Authors:** David N. Olivieri, Roque J. Hernández
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.14033v1](http://arxiv.org/abs/2605.14033v1)
- **PDF:** [https://arxiv.org/pdf/2605.14033v1](https://arxiv.org/pdf/2605.14033v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution:** The paper introduces a finite sheaf‑theoretic framework that lets an AI scientific agent diagnose when its current representational language can no longer be coherently “transported” into a new regime and therefore must be expanded—a formalization of the “theory‑shift” detection problem.  

**Methodology:** By structuring contexts as overlapping local charts (source, overlap, target, validation) the authors define gluing conditions and an *obstruction* metric that aggregates residual fitting error, incompatibility on overlaps, constraint violations, failures of limiting relations, and representational cost. They test this diagnostic on a “transition‑card” benchmark that cleanly separates pure deformation of a theory from genuine extension, and compare it to a secondary constellation‑kernel similarity probe.  

**Key findings:** In almost all benchmark instances the intended deformation or extension receives the lowest obstruction score, successfully distinguishing shift type, demonstrating that finite sheaf‑theoretic obstruction provides a practical, autonomous signal for AI agents that their current theory is no longer transportable and that representational extension is the next coherent step.


<details>
<summary>Abstract</summary>

Scientific theory shift in AI agents requires more than fitting equations to data. An artificial scientific agent must detect whether an existing representational framework remains transportable into a new regime, or whether its language has become locally-to-globally obstructed and must be extended. This paper develops a finite sheaf-theoretic framework for detecting theory-shift candidates through transport and obstruction. Contexts are organized as a local-to-global structure in which source, overlap, target, and validation charts are fitted, restricted, and tested for gluing. Obstruction measures failure of coherence through residual fit, overlap incompatibility, constraint violation, limiting-relation failure, and representational cost. We evaluate the framework on a controlled transition-card benchmark designed to separate deformation within a source language from extension of that language. The main result is direct obstruction ranking: the intended deformation or extension is usually the lowest-obstruction candidate, and transition type is separated in the benchmark. A constellation kernel over the same signatures is included only as a secondary representational-similarity probe. The aim is not to reconstruct historical paradigm shifts or solve open-ended autonomous theory invention, but to isolate a finite diagnostic subproblem for AI agents: detecting when representational transport fails and extension becomes the coherent next move.

</details>


### 83. VectraYX-Nano: A 42M-Parameter Spanish Cybersecurity Language Model with Curriculum Learning and Native Tool Use

- **Authors:** Juan S. Santillana
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13989v1](http://arxiv.org/abs/2605.13989v1)
- **PDF:** [https://arxiv.org/pdf/2605.13989v1](https://arxiv.org/pdf/2605.13989v1)
- **Categories:** cs.CL


> The paper introduces **VectraYX‑Nano**, a 42 M‑parameter Spanish‑language decoder‑only transformer specifically tuned for cybersecurity tasks and equipped with native tool invocation through the Model Context Protocol (MCP). By constructing a 170 M‑token, Latin‑American‑focused corpus (conversational, security‑knowledge, and offensive‑tooling data) and applying a curriculum‑learning regime with a replay buffer and subsequent supervised fine‑tuning (including 6.3 k tool‑use demonstrations), the authors achieve a stable loss drop (≈9.8 → 2.16) and a conversational alignment score of 0.78 ± 0.05, while demonstrating that tool‑use performance is limited more by corpus density than model capacity. The released model runs sub‑second on commodity hardware (≈81 MB GGUF) and sets a baseline for Spanish‑native, tool‑aware cybersecurity agents.


<details>
<summary>Abstract</summary>

We present VectraYX-Nano, a 41.95M-parameter decoder-only language model trained from scratch in Spanish for cybersecurity, with a Latin-American focus and native tool invocation via the Model Context Protocol (MCP). Four contributions: (i) Corpus: VectraYX-Sec-ES, a 170M-token Spanish corpus from an eight-VM pipeline (~$25 USD) partitioned into conversational (42M tokens, OpenSubtitles-ES, OASST1), cybersecurity (118M tokens, NVD, Wikipedia-ES, CVE mirror, security blogs), and offensive-security tooling (10M tokens, ExploitDB, HackTricks, OWASP) phases. (ii) Architecture: 42M-parameter Transformer decoder with GQA, QK-Norm, RMSNorm, SwiGLU, RoPE, z-loss, and a 16,384-token byte-fallback BPE. (iii) Curriculum with replay: continual pre-training with a replay buffer yields monotonic loss descent (9.80->3.17->3.00->2.16); after SFT on OASST-ES, Alpaca-ES, CVE Q&A, and 6,327 tool-use traces, the model attains a conversational gate of 0.78+-0.05 (N=4 seeds). (iv) Two findings: a bootstrap-corpus ablation reveals a loss-vs-register inversion at nano scale; a LoRA study shows the B4 tool-selection floor of 0.000 is a corpus-density artifact, not a capacity gate -- a tool-dense corpus (2,801 examples) raises B4 to 0.145+-0.046 on Nano 42M and 0.445+-0.201 on a 260M mid-tier. The GGUF artifact is 81 MB (F16), runs at sub-second TTFT on commodity hardware under llama.cpp, and is to our knowledge the first Spanish-native cybersecurity LLM with end-to-end MCP integration. Corpus recipe, training scripts, GGUF weights, and B1-B5 benchmark are released.

</details>


### 84. PBT-Bench: Benchmarking AI Agents on Property-Based Testing

- **Authors:** Lucas Jing, Xinqi Wang, Liao Zhang, Simon S. Du
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15229v1](http://arxiv.org/abs/2605.15229v1)
- **PDF:** [https://arxiv.org/pdf/2605.15229v1](https://arxiv.org/pdf/2605.15229v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **PBT‑Bench**, a new evaluation suite of 100 property‑based testing (PBT) challenges drawn from 40 real‑world Python libraries, each seeded with multiple semantic bugs that cannot be uncovered by naïve random input generation. By requiring agents to read documentation, infer the intended invariant, and craft a Hypothesis @given strategy that concentrates sampling in the bug‑triggering region, the benchmark isolates the specific ability to perform documentation‑grounded semantic reasoning for test generation. Experiments with eight recent LLMs show that providing explicit Hypothesis scaffolding improves bug‑recall for mid‑range models (up to +20 % points) but yields mixed or negative effects for the strongest models, and that failure patterns are model‑specific, leaving a substantial portion of hard bugs unsolved across all architectures.


<details>
<summary>Abstract</summary>

Existing code benchmarks measure whether an agent can produce any test that reproduces a known bug, or whether it can produce a
  patch that fixes a described issue. Neither isolates the distinct skill of property-based testing: deriving a semantic invariant
  from documentation, and then constructing an input-generation strategy precise enough to make a random search reveal the violation.
  We introduce PBT-Bench, a benchmark of 100 curated property-based testing problems across 40 real Python libraries. Each problem
  injects one or more semantic bugs (365 in total, mean 3.65 per problem) designed so that default-strategy random inputs almost
  never trigger them; the agent must read the library's documentation, identify the relevant invariant, and specify a Hypothesis
  @given strategy that concentrates mass in the trigger region. Bugs are stratified across three difficulty levels (L1-L3) spanning
  single-constraint boundary bugs to stateful, cross-function protocol violations. We evaluate eight contemporary LLMs under two
  prompting regimes (open-ended baseline vs. explicit Hypothesis scaffolding) for three independent runs per configuration. Bug
  recall under the PBT-guided prompt ranges from 42.1% to 83.4% across models; under the open-ended baseline, from 31.4% to 76.7%.
  Hypothesis scaffolding lifts mid-capability models by over 20 percentage points, but yields smaller gains for the strongest models,
  with two exceptions showing degradation, suggesting the structured prompt can interfere with certain model behaviours rather than
  complementing them. The hardest bugs prove model-specific: different architectures fail on different problems, leaving persistent
  gaps that no single model closes. We release the benchmark, harness, and full evaluation corpus to support downstream work on
  documentation-grounded semantic reasoning.

</details>


### 85. Collider-Bench: Benchmarking AI Agents with Particle Physics Analysis Reproduction

- **Authors:** Darius A. Faroughy, Sofia Palacios Schweitzer, Ian Pang, Siddharth Mishra-Sharma, David Shih
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13950v1](http://arxiv.org/abs/2605.13950v1)
- **PDF:** [https://arxiv.org/pdf/2605.13950v1](https://arxiv.org/pdf/2605.13950v1)
- **Categories:** cs.LG, cs.AI, hep-ex, hep-ph


> **Main contribution** – The paper introduces **Collider‑Bench**, a new, physics‑driven benchmark that tests whether large‑language‑model (LLM) agents can autonomously reconstruct and execute genuine Large Hadron Collider (LHC) analyses using only publicly available papers and open‑source toolchains, thereby exposing agents to the incomplete documentation, domain‑specific reasoning, and trial‑and‑error that characterize real scientific work.

**Methodology** – Each benchmark task asks an LLM‑based agent to translate a published analysis into a full simulation‑and‑selection pipeline, run open‑source event generators, and produce event‑yield histograms for prescribed signal regions. Performance is measured continuously with histogram‑based fidelity metrics, supplemented by an LLM judge that inspects the generated code and session trace for hallucinations, fabrications, or duplicated content. The authors also record the computational cost per task and provide a containerized sandbox for reproducibility.

**Key findings** – Across a “capability ladder” of general‑purpose coding agents, none consistently outperformed a baseline “physicist‑in‑the‑loop” workflow; agents often failed to fill critical gaps in the public toolchain or introduced subtle errors, highlighting current limitations of autonomous agents in high‑stakes, domain‑intensive scientific problem solving.


<details>
<summary>Abstract</summary>

Autonomous language-model agents are increasingly evaluated on long-horizon tool-use tasks, but existing benchmarks rarely capture the complexity and nuance of real scientific work. To address this gap, we introduce Collider-Bench, a benchmark for evaluating whether LLM agents can reproduce experimental analyses from the Large Hadron Collider (LHC) using only public papers and open scientific software. Such analyses are often difficult to reproduce because the public toolchain only approximates the software used internally by the experimental collaborations, while the published papers inevitably omit implementation details needed for a faithful reconstruction. Agents must therefore rely on physical reasoning, domain knowledge, and trial-and-error to fill these gaps. Each task requires the agent to turn a published analysis into an executable simulation-and-selection pipeline and submit predicted collision event yields in specified signal regions. These predictions are evaluated with standard histogram metrics that provide continuous fidelity scores without a hand-written rubric. We also report the computational cost incurred by each agent per task. Finally, we evaluate the codebase and full session trace using an LLM judge to catch qualitative failure modes such as fabrications, hallucinations and duplications. We release an initial set of tasks drawn from LHC searches, together with a containerized sandbox and event simulation tools. We evaluate across a capability ladder of general purpose coding agents. Our results show that on average no agent reliably beats the physicist-in-the-loop solution.

</details>


### 86. Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems

- **Authors:** Jun He, Deying Yu
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15228v1](http://arxiv.org/abs/2605.15228v1)
- **PDF:** [https://arxiv.org/pdf/2605.15228v1](https://arxiv.org/pdf/2605.15228v1)
- **Categories:** cs.AI, cs.LG


> The paper presents a Distributed Trust Framework (DTF) that replaces standing identity‑based privileges with proof‑derived authority for autonomous AI agents operating in sovereign, cloud‑native environments. DTF requires an agent to submit a *Justification Proof* of intent, which is independently validated through a consensus protocol; the resulting short‑lived Execution Identity and immutable Evidence Chain guarantee that every high‑stakes mutation is both authorized and auditable. Experiments on an OpenKedge‑based governed‑mutation substrate demonstrate that the framework enforces a strict invariant—no critical action can be executed without a verified proof—thereby making autonomous agent execution verifiable, replayable, and safe for regulated, nation‑scale digital services.


<details>
<summary>Abstract</summary>

Modern cloud and enterprise systems rely on identity-centric authorization, assuming that callers possessing valid credentials are safe to execute commands. The emergence of autonomous AI agents invalidates this assumption: agents can generate syntactically valid but semantically unsafe actions, making standing privileges a significant operational risk. This risk becomes especially acute in sovereign AI systems, where autonomous agents may interact with cloud infrastructure, regulated data, financial workflows, and national-scale digital services. Governed mutation substrates reduce this risk by interposing on agent actions: agents submit intents, infrastructure evaluates context and policy, and execution is mediated. However, this shifts the trust boundary: how can the decision to authorize an intent be made verifiable, distributed, and replayable?
  We introduce a Distributed Trust Framework (DTF), a verification framework for governed mutation systems that computes execution authority from structured, verifiable artifacts. DTF introduces a Justification Proof to encode the admissibility basis of an action, a consensus model for independent evaluation, an ephemeral Execution Identity derived from the approved proof, and an append-only Evidence Chain that preserves the authorization lifecycle. Under stated substrate assumptions, this architecture enforces a compact authorization invariant: no high-stakes execution without a proof object, no derived authority without consensus, and no valid mutation detached from evidence.
  We define the model, instantiate it over an OpenKedge-based governed mutation substrate, and show how it maps onto cloud-native environments. By shifting authorization from standing identity to proof-derived authority, DTF provides an infrastructure foundation for making agentic execution governable, auditable, and bounded in sovereign AI deployments.

</details>


### 87. Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights

- **Authors:** Wenrui Bao, Huan Wang, Jian Wang, Zhangyang Wang, Kai Wang, Yuzhang Shang
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13839v1](http://arxiv.org/abs/2605.13839v1)
- **PDF:** [https://arxiv.org/pdf/2605.13839v1](https://arxiv.org/pdf/2605.13839v1)
- **Categories:** cs.CL


> **Main contribution**  
The paper introduces **TFlow (Thought Flow)**, a novel weight‑space communication protocol for multi‑agent large‑language‑model (LLM) systems that replaces the usual token‑based message passing with transient, low‑rank LoRA updates to a fixed receiver model.

**Methodology**  
For each query, frozen “sender” agents process the input and a learned parameter‑generator converts their hidden activations into LoRA perturbations that are fused and applied only during the receiver’s forward pass. This yields instance‑specific weight changes without altering the model permanently or expanding the text context.

**Key findings**  
Across five benchmark tasks, a three‑agent TFlow setup improves the receiver’s accuracy by up to **8.5 %**, cuts processed tokens by up to **32.7 %**, and, relative to a conventional three‑agent token‑exchange baseline, reduces total tokens by **≈83 %** and inference time by up to **4.6×**, while retaining competitive performance on four of the five tasks. These results demonstrate that transient low‑rank weight perturbations are an efficient, executable medium for agentic AI collaboration.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems usually collaborate by exchanging natural-language messages. This interface is simple and interpretable, but it forces each sender's intermediate computation to be serialized into tokens and then reprocessed by the receiver, thereby increasing the generated-token cost, prefill overhead, and KV-cache memory. We study an alternative communication interface: instead of appending a sender's message to the receiver's context, compile the sender's hidden states into a transient, receiver-specific weight perturbation. We introduce TFlow (Thought Flow), a weight-space communication framework for a known and fixed receiver architecture. For each query, frozen role-prompted sender agents process the input, and a learned parameter generator maps their internal activations into low-rank LoRA perturbations targeting the receiver's modules. These perturbations are fused and applied only during the receiver's generation, enabling instance-level adaptation without permanently changing the model or enlarging the receiver's text context. With three Qwen3-4B agents, TFlow improves over a standalone receiver by up to 8.5 accuracy points across five benchmarks while reducing processed tokens by up to 32.69%. Compared with a text-based three-agent baseline, it reduces total processed tokens by up to 83.27% and the wall-clock inference time by up to 4.6$\times$, while maintaining competitive accuracy on four of five benchmarks. These results suggest that transient low-rank weight perturbations can serve as an executable communication medium for efficient multi-agent LLM collaboration.

</details>


### 88. EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents

- **Authors:** Jiaqi Liu, Xinyu Ye, Peng Xia, Zeyu Zheng, Cihang Xie, Mingyu Ding, Huaxiu Yao
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13941v1](http://arxiv.org/abs/2605.13941v1)
- **PDF:** [https://arxiv.org/pdf/2605.13941v1](https://arxiv.org/pdf/2605.13941v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **EvolveMem**, a self‑evolving memory system for large‑language‑model (LLM) agents that jointly adapts both the stored knowledge and the retrieval pipeline (scoring, fusion, and answer‑generation policies) through a closed‑loop “AutoResearch” process. An LLM‑driven diagnosis module analyzes per‑question failure logs, proposes concrete changes to a structured retrieval‑configuration action space, and a meta‑analyzer safely applies them with revert‑on‑regression and explore‑on‑stagnation safeguards, allowing the architecture to iteratively improve without human intervention. Experiments on the LoCoMo and MemBench benchmarks show that EvolveMem achieves up to 25.7 % relative gains over the strongest baselines and learns transferable retrieval strategies, demonstrating that autonomous co‑evolution of memory content and retrieval mechanisms can substantially boost long‑term performance of LLM agents.


<details>
<summary>Abstract</summary>

Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion strategies, and answer-generation policies remain frozen at deployment. We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it. We present EvolveMem, a self-evolving memory architecture that exposes its full retrieval configuration as a structured action space optimized by an LLM-powered diagnosis module. In each evolution round, the module reads per-question failure logs, identifies root causes, and proposes targeted configuration adjustments; a guarded meta-analyzer applies them with automatic revert-on-regression and explore-on-stagnation safeguards. This closed-loop self-evolution realizes an AutoResearch process: the system autonomously conducts iterative research cycles on its own architecture, replacing manual configuration tuning. Starting from a minimal baseline, the process converges autonomously, discovering effective retrieval strategies including entirely new configuration dimensions not present in the original action space. On LoCoMo, EvolveMem outperforms the strongest baseline by 25.7% relative and achieves a 78.0% relative improvement over the minimal baseline. On MemBench, EvolveMem exceeds the strongest baseline by 18.9% relative. Evolved configurations transfer across benchmarks with positive rather than catastrophic transfer, indicating that the self-evolution process captures universal retrieval principles rather than benchmark-specific heuristics. Code is available at https://github.com/aiming-lab/SimpleMem.

</details>


### 89. AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills

- **Authors:** Haomin Zhuang, Hanwen Xing, Yujun Zhou, Yuchen Ma, Yue Huang, Yili Shen, Yufei Han, Xiangliang Zhang
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13940v1](http://arxiv.org/abs/2605.13940v1)
- **PDF:** [https://arxiv.org/pdf/2605.13940v1](https://arxiv.org/pdf/2605.13940v1)
- **Categories:** cs.CR, cs.AI


> **Contribution**: The paper introduces **AgentTrap**, the first dynamic benchmark that evaluates how well LLM‑driven agents can safely incorporate third‑party “skills” (reusable workflow packages) without being subverted by hidden malicious behavior embedded in those skills.

**Methodology**: The authors construct 141 sandboxed tasks (91 malicious, 50 benign) spanning 16 supply‑chain threat dimensions. For each task an agent receives a normal user request, accesses a set of installed third‑party skills (some containing covert harmful steps), and executes the workflow. AgentTrap then automatically classifies the full execution trace as: successful attack, blocked/refused, attack not triggered, or no‑attack evidence.

**Key Findings**: Across multiple state‑of‑the‑art LLM agents, failures are rarely classic jailbreaks; instead agents routinely complete the user‑visible request while silently carrying out the unsafe side‑effects of a malicious skill. This reveals that runtime, end‑to‑end evaluation of the model‑framework‑workspace stack is essential for trustworthy agentic AI.


<details>
<summary>Abstract</summary>

Third-party skills are becoming the package ecosystem for LLM agents. They package natural-language instructions, helper scripts, templates, documents, and service configuration into reusable workflows. This makes skills useful, but it also introduces a new security problem: a malicious skill does not need to ask the model to perform an obviously harmful action. Instead, it can disguise the harmful behavior as part of a routine workflow, relying on the agent to execute that workflow with high-value permissions and limited human supervision.
  We introduce AgentTrap, a dynamic benchmark for evaluating whether LLM agents can use third-party skills while resisting malicious runtime behavior. AgentTrap contains 141 tasks: 91 malicious tasks and 50 benign utility tasks, covering 16 security-impact dimensions grounded in agent-skill supply-chain threats. In each task, the agent receives an ordinary user request, runs with installed skills that may contain malicious workflow elements, and is executed in a sandboxed environment. AgentTrap then judges complete trajectories for attack success, blocked or refused behavior, attack-not-triggered cases, and no-attack-evidence outcomes. Our central finding is that the most informative failures are not simple jailbreaks. Models often complete the visible user task while treating unsafe side effects introduced by the skill as part of the normal workflow. This motivates runtime evaluation of the concrete model--framework--workspace environment in which users actually delegate work. Code and data are available at https://github.com/zhmzm/AgentTrap and https://huggingface.co/datasets/zhmzm/AgentTrap.

</details>


### 90. ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles

- **Authors:** Yitian Yang, Yiqun Duan, Linghan Huang, Yiqi Zhu, Francesco Bailo, Chunmeizi Su, Huaming Chen
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13725v1](http://arxiv.org/abs/2605.13725v1)
- **PDF:** [https://arxiv.org/pdf/2605.13725v1](https://arxiv.org/pdf/2605.13725v1)
- **Categories:** cs.AI, cs.SI


> ScioMind presents a novel multi‑agent simulation framework that fuses cognitively‑inspired belief‑update mechanics with the generative reasoning power of large language models. The method combines (1) a memory‑anchored update rule wherein personality‑conditioned anchoring strength modulates an agent’s susceptibility to influence, (2) a hierarchical memory system that stores persistent experiences for reflective belief formation, and (3) dynamic agent profiles generated via a corpus‑grounded retrieval pipeline to create heterogeneous personalities and evolving internal states. In policy‑debate case studies, these components jointly increase opinion diversity, reduce unstable oscillations, and produce persistent belief trajectories that better match empirical patterns of polarization and extremization, demonstrating enhanced behavioral realism for LLM‑based social simulations.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent simulation offers a powerful testbed for studying social opinion dynamics. Yet current approaches often adopt two contrasting methods: either relying on fixed update rules with limited cognitive grounding or delegating belief change largely to unconstrained LLM interaction. We introduce ScioMind, a cognitively grounded simulation framework that bridges these paradigms by combining structured opinion dynamics with LLM-based agent reasoning. ScioMind integrates three key components: 1) a memory-anchored belief update rule that modulates susceptibility to influence via personality-conditioned anchoring strength; 2) a hierarchical memory architecture that supports persistent, experience-driven belief formation; and 3) dynamic agent profiles derived from a corpus-grounded retrieval pipeline, enabling heterogeneous personalities, rationales, and evolving internal states. We evaluate ScioMind on multiple case studies in a real-world policy debate scenario. Across metrics including polarisation, diversity, extremization, and trajectory stability, the proposed components consistently yield improvements in behavioural realism. In particular, dynamic profiles increase opinion diversity, memory and reflection reduce unstable oscillation, and anchoring induces persistent belief trajectories that better align with patterns reported in political psychology. These results suggest that our cognitively grounded design provides a novel solution to LLM-based social simulation that improves both stable and behavioural realism

</details>


### 91. SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems

- **Authors:** Hongji Pu, Xinyuan Song, Liang Zhao
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13716v1](http://arxiv.org/abs/2605.13716v1)
- **PDF:** [https://arxiv.org/pdf/2605.13716v1](https://arxiv.org/pdf/2605.13716v1)
- **Categories:** cs.SE, cs.MA


> **Contribution:** The paper introduces **SkillOps**, a plug‑in framework that treats a collection of LLM‑agent skills as a self‑maintaining software ecosystem, explicitly targeting the “skill technical debt” that accrues as libraries grow and evolve.

**Methodology:** SkillOps models each skill with a typed *Skill Contract* (preconditions, outcomes, actions, variables, and failure modes) and organizes the library in a **Hierarchical Skill Ecosystem Graph**. It then runs rule‑based diagnostics across utility, compatibility, risk, and validation dimensions to automatically prune, patch, and re‑type‑check the library, producing a “maintained” skill set that can be fed unchanged into any downstream retrieval or planning agent.

**Key Findings:** On the ALFWorld benchmark, a standalone agent using only the SkillOps‑maintained library reaches **79.5 % task success**, beating the best prior baseline by **8.8 pp** without any extra task‑time LLM calls. When added as a maintenance layer to retrieval‑heavy agents, it yields **+0.68–2.90 pp** improvements, all while incurring almost zero library‑time LLM usage, demonstrating that low‑overhead, library‑time maintenance is feasible and beneficial for agentic AI.


<details>
<summary>Abstract</summary>

Large language model agents increasingly rely on skill libraries for multi-step tasks, yet these libraries can accumulate persistent defects as skills are added, reused, patched, and linked to changing dependencies. We call this failure mode skill technical debt: library-level defects that may not break a single skill locally but can harm future retrieval, composition, and execution. Existing skill-based agents mainly focus on task-time retrieval, planning, and repair, while library-time maintenance remains underexplored. We propose SkillOps, a method-agnostic plug-in framework for maintaining skill libraries. SkillOps represents each skill as a typed Skill Contract (P, O, A, V, F), organizes skills with a Hierarchical Skill Ecosystem Graph, and diagnoses library health across utility, compatibility, risk, and validation dimensions. Given a raw skill library, SkillOps produces a maintained library that can be used by existing retrieval or planning agents without changing their internal code. On ALFWorld, SkillOps achieves 79.5 percent task success as a standalone agent, outperforming the strongest baseline by 8.8 percentage points with no additional task-time large language model calls. As a plug-in layer, it improves retrieval-heavy baselines by 0.68 to 2.90 percentage points. The current rule-based maintenance implementation uses nearly zero library-time large language model calls or tokens, showing that skill-library maintenance can be added as a low-overhead architectural layer.

</details>


### 92. How to Interpret Agent Behavior

- **Authors:** Jie Gao, Kaiser Sun, Jen-tse Huang, Katherine Van Koevering, Sijie Ji, Heyuan Huang, Weiyan Shi, Zhuoran Lu, Ziang Xiao, Daniel Khashabi, Mark Dredze
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13625v1](http://arxiv.org/abs/2605.13625v1)
- **PDF:** [https://arxiv.org/pdf/2605.13625v1](https://arxiv.org/pdf/2605.13625v1)
- **Categories:** cs.AI


> The paper introduces **ACT*ONOMY**, a grounded‑theory‑derived taxonomy (3‑level hierarchy: 10 high‑level actions, 46 sub‑actions, 120 leaf categories) and an open‑source pipeline for automatically tagging the natural‑language reasoning trajectories and execution traces of long‑running agents such as Claude Code and Codex. By mapping unstructured trace data to this shared vocabulary, the authors demonstrate that ACT*ONOMY can differentiate behavioral profiles across agents and reveal intra‑agent patterns that correlate with failure modes, thereby facilitating scalable diagnosis, debugging, and oversight of autonomous AI systems.


<details>
<summary>Abstract</summary>

Autonomous agents such as Claude Code and Codex now operate for hours or even days. Understanding their runtime behavior has become critical for downstream tasks such as diagnosing inefficiencies, fixing bugs, and ensuring better oversight. A primary way to gain this understanding is analyzing the reasoning trajectories and execution traces these agents generate. Yet such data remains in unstructured natural-language form, making it difficult for humans to interpret at scale. We introduce ACT*ONOMY (a combination of Action and Taxonomy), a taxonomy for describing and analyzing agent behavior at runtime. ACT*ONOMY has two components: (1) the taxonomy itself, developed through Grounded Theory and structured as a three-level hierarchy of 10 actions, 46 subactions, and 120 leaf categories; and (2) an open repository that hosts the living taxonomy, provides an automated analysis pipeline that applies it to agent trajectories analysis, and defines an extension protocol for customization and growth. Our experiments show that ACTONOMY can compare behavioral profiles across agents and characterize a single agent's behavior across diverse trajectories, surfacing patterns indicative of failure modes. By providing a shared vocabulary, ACT*ONOMY helps researchers, agent designers, and end users interpret agent behavior more consistently, enabling better oversight and control.

</details>


### 93. OpenAaaS: An Open Agent-as-a-Service Framework for Distributed Materials-Informatics Research

- **Authors:** Peng Kang, Bixuan Li, Xiaoya Huang, Shuo Shi, Weiqiao Zhou, Zhen Li, Yu Liu, Lei Zheng
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13618v1](http://arxiv.org/abs/2605.13618v1)
- **PDF:** [https://arxiv.org/pdf/2605.13618v1](https://arxiv.org/pdf/2605.13618v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> The paper introduces **OpenAaaS**, an open‑source, hierarchical “Agent‑as‑a‑Service” framework that lets a central master agent orchestrate complex materials‑informatics workflows while keeping all raw data and proprietary compute resources locally under the control of subordinate “near‑data” agents. The authors implement the system with a planning‑decomposition pipeline for the master agent and sandboxed execution containers for sub‑agents, and demonstrate it on (i) AlphaAgent, a literature‑analysis agent that outperforms single‑pass retrieval‑augmented generation baselines (4.66/5.0 on deep analytical questions) and (ii) a secure, ultra‑large hexa‑high‑entropy‑alloy descriptor database service that preserves data sovereignty across institutional boundaries. These results show that distributed, secure multi‑agent collaboration can be achieved without moving data, providing a scalable architectural foundation for agentic AI‑driven materials design.


<details>
<summary>Abstract</summary>

The Materials Genome Initiative catalyzed the proliferation of centralized platforms--SaaS, PaaS, and IaaS--that aggregate computational and experimental resources for accelerated materials discovery. In parallel, breakthroughs in large language models (LLMs) and autonomous agents have created powerful new reasoning capabilities for scientific research. Yet a critical "last mile" problem remains: while we possess world-class models and vast repositories of materials data, we lack the organizational infrastructure to compose these capabilities securely across institutional boundaries. The development of structural and functional materials for harsh service environments--high-temperature alloys, radiation resistant steels, corrosion-resistant coatings--remains characterized by long-term iteration, mechanistic complexity, and high domain expertise--demands that exceed both monolithic agent systems and traditional centralized platforms. To address this gap we propose OpenAaaS, an open-source hierarchical and distributed Agent-as-a-Service framework that enables organized multi-agent collaboration for intelligent materials design. OpenAaaS is built on a single foundational principle: code flows, data stays still. A Master Agent plans and decomposes complex research tasks without requiring direct access to subordinate agents' managed data and computational resources. Sub-agents, deployed as near-data execution nodes, retain full sovereignty over local datasets, proprietary algorithms, and specialized hardware. This architecture guarantees that raw data never leaves its domain of origin while enabling cross-scale, cross-domain secure integration of previously isolated materials intelligence silos. We validate the framework through two representative case studies: (i) AlphaAgent, an evidence-grounded materials literature analysis executor that achieves 4.66/5.0 on deep analytical questions against single-pass RAG baselines; and (ii) an ultra-large-scale hexa-high-entropy alloy descriptor database service that demonstrates secure near-data execution and domain-specific scientific workflows under strict data-sovereignty constraints. OpenAaaS establishes a principled pathway toward "organized research" via agent collectives, offering a scalable foundation for next-generation materials intelligent design platforms. All source code is available at https://github.com/Wolido/OpenAaaS.

</details>


### 94. NIMO Controller: a self-driving laboratory orchestrator based on the Model Context Protocol

- **Authors:** Naruki Yoshikawa, Ryo Tamura
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15227v1](http://arxiv.org/abs/2605.15227v1)
- **PDF:** [https://arxiv.org/pdf/2605.15227v1](https://arxiv.org/pdf/2605.15227v1)
- **Categories:** cs.AI, cond-mat.mtrl-sci, cs.RO


> The paper introduces **NIMO Controller**, a self‑driving‑laboratory orchestrator built on the **Model Context Protocol (MCP)**, which exposes every laboratory function as an MCP server. By auto‑generating a visual programming canvas from discovered MCP tools, the system lets non‑programmers assemble experimental workflows while simultaneously offering a uniform, machine‑readable API that AI agents can call directly. In a color‑matching SDL case study, the authors show that their MCP‑centric architecture enables seamless human‑agent interaction and simplifies workflow creation, demonstrating a practical pathway toward more accessible, agent‑friendly SDL software.


<details>
<summary>Abstract</summary>

Self-driving laboratories (SDLs) have attracted increasing attention as a means of accelerating scientific discovery; however, developing SDL software remains technically demanding. To improve accessibility, orchestration software frameworks have been proposed to coordinate SDL components. Nevertheless, existing frameworks are primarily designed for human interaction and do not provide standardized interfaces suitable for AI agents. In this work, we propose an SDL software architecture based on the Model Context Protocol (MCP), in which all SDL functionalities are exposed through MCP servers. Following this design principle, we introduce an MCP-based SDL orchestrator, named NIMO Controller. It provides a visual programming interface automatically generated through MCP-based tool discovery, allowing human users to design experimental workflows without writing code. The same MCP backend can also be accessed by AI agents, providing a unified interface for both human users and AI agents. We demonstrate the proposed system through a case study on a color-matching SDL. The results validate the usability of the proposed MCP-based SDL architecture.

</details>


### 95. Is Agentic AI Ready for Real-World Hardware Engineering? A Deep Dive with Phoenix-bench

- **Authors:** Qingyun Zou, Feng Yu, Hongshi Tan, Bingsheng He, WengFai Wong
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15226v1](http://arxiv.org/abs/2605.15226v1)
- **PDF:** [https://arxiv.org/pdf/2605.15226v1](https://arxiv.org/pdf/2605.15226v1)
- **Categories:** cs.AR, cs.AI, cs.SE


> The paper introduces **Phoenix‑bench**, the first large‑scale, end‑to‑end benchmark that evaluates agentic AI systems on realistic hardware‑design tasks. It supplies 511 fully verified Verilator instances (spanning 114 GitHub repositories) together with patches, design‑flow metadata, failing/passing testbenches, and a Docker‑pinned EDA environment, enabling a uniform comparison of 12 agents (four commercial, eight open‑source) across four LLM backbones. Experiments show that agents tuned for software engineering lose 37‑58 % of their success rate on hardware bugs, mainly because hardware defects propagate through signal‑flow across modules rather than call‑graph structures; failures concentrate on FSM/control‑flow and testbench bugs, and performance improves dramatically (≈ 42 % absolute lift) when agents receive a single round of test‑case feedback, highlighting that fine‑grained localization and iterative verification are far more critical than merely identifying the buggy file.


<details>
<summary>Abstract</summary>

We ask whether agentic AI systems built for software engineering transfer to realistic hardware engineering. Existing hardware LLM benchmarks isolate sub-tasks but none jointly requires repository navigation, hierarchy-aware localization, Electronic Design Automation (EDA) executable verification, and maintenance-style patching. We introduce \textbf{Phoenix-bench}, a synchronized corpus of 511 verified Verilator instances from 114 GitHub repositories, each shipped with the developer patch, design-flow labels, fail-to-pass and pass-to-pass testbenches, and a Docker-pinned EDA environment so resolved-rate differences reflect agent behavior rather than toolchain availability. Using Phoenix-bench we run a uniform evaluation of four commercial agents and eight open-source agentic structures across four LLM backbones, plus two diagnostic interventions (file-level oracle localization and one round of testbench-log feedback). Three findings emerge. (i)~Software and hardware are fundamentally different engineering tasks: the same agent loses 37\% to 58\% from SWE-bench Verified to Phoenix-bench because hardware bugs propagate across parallel instantiated modules through signal flow rather than along a software-style call graph, and software-tuned agents stop at the symptom file instead of tracing back through the instantiation chain. (ii)~Failures concentrate on design control-flow / finite state machine (FSM) bugs, verification testbench bugs, and hard cases that demand cross-hierarchy signal-flow tracking and coordinated multi-file edits. (iii)~Localization granularity matters far more than localization itself: a perfect file-level oracle yields only $+1.4$\% because the agent then breaks files that did not need editing, while a single round of test case feedback lifts resolved rate by $42$\% to $45$\% because the test case tells \emph{where} the bug is and \emph{what} the fix has to look like.

</details>


### 96. Position: Assistive Agents Need Accessibility Alignment

- **Authors:** Jie Hu, Changyuan Yan, Yu Zheng, Ziqian Wang, Jiaming Zhang
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13579v1](http://arxiv.org/abs/2605.13579v1)
- **PDF:** [https://arxiv.org/pdf/2605.13579v1](https://arxiv.org/pdf/2605.13579v1)
- **Categories:** cs.AI


> The paper argues that assistive AI agents for blind and visually impaired users must treat accessibility as a core alignment problem, not a peripheral usability add‑on, because existing agentic systems are built on sighted‑user assumptions—low‑cost verification, tolerant trial‑and‑error, and visual feedback—that systematically break under the verification, safety, and interaction constraints of BVI contexts. By analyzing 778 assistance‑task instances from prior studies, the authors show that scaling models or retrofitting interfaces does not cure these mismatches, and they propose a lifecycle‑oriented design pipeline (user research → system design → deployment → post‑deployment iteration) that embeds “accessibility alignment” throughout development. Empirically, the work demonstrates that BVI‑centered tasks expose critical failure modes of current agents, positioning them as a stress test that motivates a shift toward inclusive, alignment‑focused agent design.


<details>
<summary>Abstract</summary>

Assistive agents for Blind and Visually Impaired (BVI) users require accessibility alignment as a first-class design objective. Despite rapid progress in agentic AI, most systems are designed and evaluated under assumptions of sighted interaction, low-cost verification, and tolerable trial-and-error, leading to systematic failures in assistive scenarios that cannot be resolved by model scaling or post-hoc interface adaptations alone. Drawing on an analysis of 778 assistance task instances from prior work, we show that current agentic AI remain prone to failure in assistive scenarios due to mismatches between sighted-user design assumptions and the verification, risk, and interaction constraints faced by BVI users. We argue that accessibility should be treated as an alignment problem rather than a peripheral usability concern. To this end, we introduce accessibility alignment and propose a lifecycle-oriented design pipeline for accessibility-aligned assistive agents, spanning user research, system design, deployment and post-deployment iteration. We conclude that BVI-centered assistive tasks provide a critical stress test for agentic AI and motivate a broader shift toward inclusive agent design.

</details>


### 97. Self-Supervised On-Policy Reinforcement Learning via Contrastive Proximal Policy Optimisation

- **Authors:** Asim Osman, Sasha Abramowitz, Mark Bergh, Ulrich Armel Mbou Sob, Ruan John de Kock, Omayma Mahjoub, Oussama Hidaoui, Noah De Nicola, Arnol Manuel Fokam, Felix Chalumeau, Daniel Rajaonarivonivelomanantsoa, Siddarth Singh, Refiloe Shabe, Juan Claude Formanek, Simon Verster Du Toit, Arnu Pretorius
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13554v1](http://arxiv.org/abs/2605.13554v1)
- **PDF:** [https://arxiv.org/pdf/2605.13554v1](https://arxiv.org/pdf/2605.13554v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **Contrastive Proximal Policy Optimisation (CPPO)**, the first on‑policy algorithm that integrates contrastive representation learning with the classic PPO update, thereby deriving advantage estimates directly from contrastive goal‑conditioned Q‑values and eliminating the need for hand‑crafted rewards or replay buffers. The authors implement CPPO for both continuous and discrete action spaces and evaluate it on a broad suite of single‑agent and cooperative multi‑agent tasks, comparing against prior off‑policy contrastive RL methods and standard PPO. Experiments show that CPPO **outperforms all existing contrastive RL baselines on 14/18 tasks and matches or exceeds traditional PPO (which uses dense engineered rewards) on 12/18 tasks**, highlighting its effectiveness as a self‑supervised, reward‑free on‑policy approach for agentic AI.


<details>
<summary>Abstract</summary>

Contrastive reinforcement learning (CRL) learns goal-conditioned Q-values through a contrastive objective over state-action and goal representations, removing the need for hand-crafted reward functions. Despite impressive success in achieving viable self-supervised learning in RL, all existing CRL algorithms rely on off-policy optimisation and are mostly constrained to continuous action spaces, with little research invested in discrete environments. This leaves CRL disconnected from widely used and effective, modern on-policy training pipelines adopted across both single-agent and multi-agent RL in continuous and discrete environments. To establish a first connection, we introduce Contrastive Proximal Policy Optimisation (CPPO). CPPO is an on-policy contrastive RL algorithm that derives policy advantages directly from contrastive Q-values and optimises them via the standard PPO objective, without requiring a reward function or a replay buffer. We evaluate CPPO across continuous and discrete, single-agent and cooperative multi-agent tasks. Whilst the existence of an on-policy approach is inherently useful, we observe that \textbf{CPPO not only significantly outperforms the previous CRL baselines in 14 out of 18 tasks, but also matches or exceeds PPO's performance, which uses hand-crafted dense rewards, in 12 out of the 18 tasks tested.}

</details>


### 98. RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation

- **Authors:** Chengzhi Shen, Weixiang Shen, Tobias Susetzky,  Chen,  Chen, Jun Li, Yuyuan Liu, Xuepeng Zhang, Zhenyu Gong, Daniel Rueckert, Jiazhen Pan
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13542v1](http://arxiv.org/abs/2605.13542v1)
- **PDF:** [https://arxiv.org/pdf/2605.13542v1](https://arxiv.org/pdf/2605.13542v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> The paper presents **RealICU**, a new benchmark that evaluates large‑language‑model (LLM) agents on realistic, long‑horizon intensive‑care‑unit (ICU) decision‑support tasks using hindsight‑validated clinical labels rather than proxy clinician actions. By partitioning 30‑minute windows of 94 MIMIC‑IV patient trajectories into four physician‑oriented tasks (patient status, acute problems, recommended actions, and red‑flag safety alerts) and augmenting them with an oracle‑validated, larger “RealICU‑Scale” set, the authors show that current LLMs—including memory‑augmented and structured‑memory agents such as ICU‑Evo—suffer from a recall‑safety trade‑off and an anchoring bias toward early interpretations, leading to poor performance and unsafe recommendations. The benchmark thus provides a clinically grounded testbed for measuring and improving the long‑context reasoning and safety of agentic AI systems in high‑stakes medical settings.


<details>
<summary>Abstract</summary>

Intensive care units (ICU) generate long, dense and evolving streams of clinical information, where physicians must repeatedly reassess patient states under time pressure, underscoring a clear need for reliable AI decision support. Existing ICU benchmarks typically treat historical clinician actions as ground truth. However, these actions are made under incomplete information and limited temporal context of the underlying patient state, and may therefore be suboptimal, making it difficult to assess the true reasoning capabilities of AI systems. We introduce RealICU, a hindsight-annotated benchmark for evaluating large language models (LLMs) under realistic ICU conditions, where labels are created after senior physicians review the full patient trajectory. We formulate four physician-motivated tasks: assess Patient Status, Acute Problems, Recommended Actions, and Red Flag actions that risk unsafe outcomes. We partition each trajectory with 30-min windows and release two datasets: RealICU-Gold with 930-window annotations from 94 MIMIC-IV patients, and RealICU-Scale with 11,862 windows extended by Oracle, a physician-validated LLM hindsight labeler. Existing LLMs including memory-augmented ones performed poorly on RealICU, exposing two failure modes: a recall-safety tradeoff for clinical recommendations, and an anchoring bias to early interpretations of the patient. We further introduce ICU-Evo to study structured-memory agents that improves long-horizon reasoning but does not fully eliminate safety failures. Together, RealICU provides a clinically grounded testbed for measuring and improving AI sequential decision-support in high-stakes care. Project page: https://chengzhi-leo.github.io/RealICU-Bench/

</details>


### 99. MARLIN: Multi-Agent Game-Theoretic Reinforcement Learning for Sustainable LLM Inference in Cloud Datacenters

- **Authors:** H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13496v1](http://arxiv.org/abs/2605.13496v1)
- **PDF:** [https://arxiv.org/pdf/2605.13496v1](https://arxiv.org/pdf/2605.13496v1)
- **Categories:** cs.DC, cs.LG


> The paper introduces **MARLIN**, a multi‑agent game‑theoretic reinforcement‑learning framework that jointly optimizes latency (time‑to‑first token) and environmental metrics (carbon, water, and energy consumption) for large‑language‑model inference in cloud datacenters. By modeling each server node as a self‑interested agent that learns equilibrium policies through repeated games, MARLIN coordinates request routing, batching, and hardware scaling without centralized control. Empirical evaluation on production‑scale workloads shows that MARLIN cuts TTFT by ≥18 % while reducing carbon emissions 33 %, water usage 43 %, and energy costs 11 % relative to current state‑of‑the‑art inference management systems, highlighting a scalable, sustainability‑focused approach for agentic AI deployment.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have become increasingly prevalent in cloud-based platforms, propelled by the introduction of AI-based consumer and enterprise services. LLM inference requests in particular account for up to 90% of total LLM lifecycle energy use, dwarfing training energy costs. The rising volume of LLM inference requests is increasing environmental footprints, particularly carbon emissions and water consumption. To improve sustainability for LLM inference serving in cloud datacenter environments, we propose a novel multi-agent game-theoretic reinforcement learning framework called MARLIN to co-optimize time-to-first token (TTFT), carbon emissions, water usage, and energy costs associated with LLM inference. MARLIN demonstrates a reduction of at least 18% in TTFT, 33% in carbon emissions, 43% in water usage, and 11% in energy costs compared to state-of-the-art LLM inference management frameworks.

</details>


### 100. R^2-Mem: Reflective Experience for Memory Search

- **Authors:** Xinyuan Wang, Wenyu Mao, Junkang Wu, Xiang Wang, Xiangnan He
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13486v1](http://arxiv.org/abs/2605.13486v1)
- **PDF:** [https://arxiv.org/pdf/2605.13486v1](https://arxiv.org/pdf/2605.13486v1)
- **Categories:** cs.CL


> **Main contribution:** R²‑Mem introduces a “reflective experience” loop that lets large‑language‑model (LLM) agents learn from their own past memory‑search trajectories, turning successes and failures into abstract guidance without any reinforcement‑learning fine‑tuning.  

**Methodology:** In an offline phase, a rubric‑driven evaluator labels each step of historical search traces as high‑ or low‑quality; a self‑reflection learner then distills these labeled experiences into compact experience embeddings. During online inference, the agent retrieves the most relevant experience embedding and conditions its next search actions on it, thereby steering the search toward previously successful patterns and away from repeated mistakes.  

**Key findings:** Across multiple memory‑search benchmarks, R²‑Mem boosts F1 scores by up to 22.6 % while cutting token usage by 12.9 % and reducing the number of search iterations by 20.2 % compared with strong baselines, demonstrating an effective, RL‑free way to self‑improve LLM‑based agents in the agentic AI domain.


<details>
<summary>Abstract</summary>

Deep search has recently emerged as a promising paradigm for enabling agents to retrieve fine-grained historical information without heavy memory pre-managed. However, existing deep search agents for memory system repeat past error behaviors because they fail to learn from the prior high- and low-quality search trajectories. To address this limitation, we propose R^2-Mem, a reflective experience framework for memory search systems. In the offline stage, a Rubric-guided Evaluator scores low- and high-quality steps in historical trajectories, and a self-Reflection Learner distills the corresponding abstract experience. During the online inference, the retrieved experience will guide future search actions to avoid repeated mistakes and maintain high-quality behaviors. Extensive experiments demonstrate that R^2-Mem consistently improves both effectiveness and efficiency over strong baselines, improving F1 scores by up to 22.6%, while reducing token consumption by 12.9% and search iterations by 20.2%. These results verify that R^2-Mem provides a RL-free and low-cost solution for self-improving LLM agents.

</details>


### 101. PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents

- **Authors:** Mikhail Menschikov, Matvey Iskornev, Alexander Kharitonov, Alina Bogdanova, Mikhail Belkin, Ekaterina Lisitsyna, Artyom Sosedka, Victoria Dochkina, Ruslan Kostoev, Ilia Perepechkin, Evgeny Burnaev
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13481v1](http://arxiv.org/abs/2605.13481v1)
- **PDF:** [https://arxiv.org/pdf/2605.13481v1](https://arxiv.org/pdf/2605.13481v1)
- **Categories:** cs.CL


> PersonalAI 2.0 (PAI‑2) introduces a planning‑driven retrieval pipeline that lets LLM‑based agents iteratively traverse and query external knowledge graphs, using entity extraction, vertex matching and generated “clue‑queries” to steer multistage search. Experiments on six QA benchmarks show that graph‑traversal planners (e.g., BeamSearch, WaterCircles) improve factual correctness by ~6% over flat retrievers, and the full planning mechanism adds an additional ~18% gain, yielding a 4% average increase in LLM‑as‑Judge scores and state‑of‑the‑art performance (89% information‑retention) on the MINE‑1 benchmark. These results demonstrate that dynamic KG‑guided planning substantially reduces hallucination and boosts precision, positioning PAI‑2 as a scalable foundation for personalized, reasoning‑centric AI agents.


<details>
<summary>Abstract</summary>

We introduce PersonalAI 2.0 (PAI-2), a novel framework, designed to enhance large language model (LLM) based systems through integration of external knowledge graphs (KG). The proposed approach addresses key limitations of existing Graph Retrieval-Augmented Generation (GraphRAG) methods by incorporating a dynamic, multistage query processing pipeline. The central point of PAI-2 design is its ability to perform adaptive, iterative information search, guided by extracted entities, matched graph vertices and generated clue-queries. Conducted evaluation over six benchmarks (Natural Questions, TriviaQA, HotpotQA, 2WikiMultihopQA, MuSiQue and DiaASQ) demonstrates improvement in factual correctness of generating answers compared to analogues methods (LightRAG, RAPTOR, and HippoRAG 2). PAI-2 achieves 4% average gain by LLM-as-a-Judge across four benchmarks, reflecting its effectiveness in reducing hallucination rates and increasing precision. We show that use of graph traversal algorithms (e.g. BeamSearch, WaterCircles) gain superior results compared to standard flatten retriever on average 6%, while enabled search plan enhancement mechanism gain 18% boost compared to disabled one by LLM-as-a-Judge across six datasets. In addition, ablation study reveals that PAI-2 achieves the SOTA result on MINE-1 benchmark, achieving 89% information-retention score, using LLMs from 7-14B tiers. Collectively, these findings underscore the potential of PAI-2 to serve as a foundational model for next-generation personalized AI applications, requiring scalable, context-aware knowledge representation and reasoning capabilities.

</details>


### 102. Cognifold: Always-On Proactive Memory via Cognitive Folding

- **Authors:** Suli Wang, Yiqun Duan, Yu Deng, Rundong Zhao, Dai Shi, Xinliang Zhou
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13438v1](http://arxiv.org/abs/2605.13438v1)
- **PDF:** [https://arxiv.org/pdf/2605.13438v1](https://arxiv.org/pdf/2605.13438v1)
- **Categories:** cs.AI, cs.CL


> Cognifold introduces an “always‑on” memory architecture that continuously folds incoming event streams into self‑organizing, graph‑based cognitive structures, extending the classic Complementary Learning Systems model with a third prefrontal intent layer that drives proactive knowledge integration and intent surfacing. The system implements neuro‑inspired mechanisms—self‑assembly, similarity‑based merging, decay of stale nodes, and associative relinking—to maintain persistent, hierarchical representations without external retrieval prompts. Experiments on the newly proposed CogEval‑Bench and seven diverse cognitive‑domain benchmarks show that Cognifold uniquely forms emergent concept clusters that align with human‑like cognitive expectations while matching or surpassing traditional memory systems on standard retrieval tasks.


<details>
<summary>Abstract</summary>

Existing agent memory remains predominantly reactive and retrieval-based, lacking the capacity to autonomously organize experience into persistent cognitive structure. Toward genuinely autonomous agents, we introduce Cognifold, a brain-inspired "always-on" agent memory designed for the next generation of proactive assistants. CogniFold continuously folds fragmented event streams into self-emerging cognitive structures, bootstrapping progressively higher-level cognition from incoming events and accumulated knowledge. We ground this by extending Complementary Learning Systems (CLS) theory from two layers (hippocampus, neocortex) to three, adding a prefrontal intent layer. Emulating the prefrontal cortex as the locus of intentional control and decision-making, CogniFold achieves this through graph-topology self-organization: cognitive structures proactively assemble under the stream, merge when semantically similar, decay when stale, relink through associative recall, and surface intents when concept-cluster density crosses a threshold. We evaluate structural formation using CogEval-Bench, demonstrating that CogniFold uniquely produces memory structures that match cognitive expectations and concept emergence. Furthermore, across 7 broad-coverage benchmarks spanning five cognitive domains, we validate that CogniFold simultaneously performs robustly on conventional memory benchmarks.

</details>


### 103. TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints

- **Authors:** Zabir Al Nazi, Shubhashis Roy Dipta
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13414v1](http://arxiv.org/abs/2605.13414v1)
- **PDF:** [https://arxiv.org/pdf/2605.13414v1](https://arxiv.org/pdf/2605.13414v1)
- **Categories:** cs.AI


> The paper introduces **TRIAGE**, a benchmark that measures a language model’s ability to perform **prospective metacognitive control**—the capacity to select, order, and allocate a limited token budget across a batch of problems before any execution feedback is received. The authors formalize this as a single‑shot planning task, generate an oracle that knows each problem’s true solvability and compute cost, and score models by the ratio of their achieved “triage efficiency’’ to the oracle optimum. Experiments on a suite of math, science, coding, and multidisciplinary questions show that even state‑of‑the‑art and open‑source LLMs (with and without chain‑of‑thought prompting) fall far short of the oracle, revealing a significant gap in resource‑aware, self‑directed decision making that is crucial for deploying LLMs as autonomous agents under real‑world compute constraints.


<details>
<summary>Abstract</summary>

Deploying language models as autonomous agents requires more than per-task accuracy: when an agent faces a queue of problems under a finite token budget, it must decide which to attempt, in what order, and how much compute to commit to each, all before any execution feedback is available. This is the prospective form of metacognitive control studied for decades in human cognition, yet whether language models possess it remains untested. We introduce TRIAGE, an evaluation framework in which a model receives a task pool and a token budget calibrated to its own baseline cost, and commits to a single ordered plan that jointly encodes selection, sequencing, and per-problem allocation. Plans are scored against an oracle with full knowledge of the model's solvability and cost on each problem, yielding a triage efficiency ratio on a common scale. We evaluate frontier and open-source models, with and without reasoning enabled, across competition mathematics, graduate-level science, code generation, and expert multidisciplinary knowledge, and find that current language models exhibit substantial gaps in prospective metacognitive control, revealing a previously unmeasured capability dimension with direct implications for resource-efficient agent deployment.

</details>


### 104. Speculative Interaction Agents: Building Real-Time Agents with Asynchronous I/O and Speculative Tool Calling

- **Authors:** Coleman Hooper, Minwoo Kang, Suhong Moon, Nicholas Lee, Eric Wen, John Wawrzynek, Michael W. Mahoney, Yakun Sophia Shao, Amir Gholami, Kurt Keutzer
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13360v2](http://arxiv.org/abs/2605.13360v2)
- **PDF:** [https://arxiv.org/pdf/2605.13360v2](https://arxiv.org/pdf/2605.13360v2)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces **Speculative Interaction Agents**, a framework that combines asynchronous I/O with speculative tool‑calling to keep large‑language‑model (LLM) agents responsive in real‑time, latency‑sensitive scenarios (e.g., voice assistants) even when the agents must perform multi‑turn reasoning and external tool invocations.  

**Methodology:**  
1. **Asynchronous I/O** decouples the core reasoning thread from waiting on user or environment inputs, allowing the agent to continue processing while external calls are pending.  
2. **Speculative Tool Calling** lets the agent pre‑emptively invoke tools based on partial information, later correcting or confirming the result once the missing context arrives.  
3. For edge‑scale models, the authors add a **clock‑based training regime** that teaches the model to handle streaming tokens and asynchronous responses, and they generate synthetic data for supervised fine‑tuning (SFT).  

**Key findings:** On strong cloud LLM APIs, the approach yields **1.3‑1.7× latency reductions** with only minor drops in accuracy. When applied to small, on‑device models (Qwen2.5‑3B‑Instruct, Llama‑3.2‑3B‑Instruct), the clock‑trained agents achieve **1.6‑2.2× speedups** across several tool‑calling benchmarks, demonstrating that speculative, asynchronous execution can make agentic AI viable for real‑time, low‑latency applications.


<details>
<summary>Abstract</summary>

There is a growing demand for agentic AI technologies for a range of downstream applications like customer service and personal assistants. For applications where the agent needs to interact with a person, real-time low-latency responsiveness is required; for example, with voice-controlled applications, under 1 second of latency is typically required for the interaction to feel seamless. However, if we want the LLM to reason and execute an agentic workflow with tool calling, this can add several seconds or more of latency, which is prohibitive for real-time latency-sensitive applications. In our work, we propose Speculative Interaction Agents to enable real-time interaction even for agents with complex multi-turn tool calling. We propose Asynchronous I/O, which decouples the core agent reason-and-act thread from waiting for additional information from either the user or environment, thereby allowing for overlapping agentic processing while waiting on external delays. We also propose Speculative Tool Calling as a method to manage task execution when the agent is still unsure if it has received the full information or if additional user information may later be provided. For strong cloud models, our method can be applied out-of-the-box to existing real-time cloud APIs, providing 1.3-1.7$\times$ speedups with minor accuracy loss. To enable real-time interaction with small edge-scale models, we also present a clock-based training methodology that adapts the model to handle streaming inputs and asynchronous responses, and demonstrate a synthetic data generation strategy for SFT. Altogether, this approach provides 1.6-2.2$\times$ speedups with the Qwen2.5-3B-Instruct and Llama-3.2-3B-Instruct models across multiple tool calling benchmarks.

</details>


### 105. Multi-Agent Systems in Emergency Departments: Validation Study on a ED Digital Twin

- **Authors:** Markus Wenzel, Tobias Strapatsas, Jessika Kress, Dorothea Sauer, Nele Gessler, Horst K. Hahn
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13345v1](http://arxiv.org/abs/2605.13345v1)
- **PDF:** [https://arxiv.org/pdf/2605.13345v1](https://arxiv.org/pdf/2605.13345v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces a hybrid discrete‑event/agent‑based “digital twin” of an emergency department that is calibrated and validated against published ED size, patient‑load and staffing data, showing that its key performance indicators (e.g., wait times, length of stay) closely match real‑world observations. Using this validated DES‑ABM platform, the authors embed a proof‑of‑concept multi‑agent system that autonomously proposes and tests resource‑allocation policies, demonstrating that the MAS can reproduce documented outcomes of established optimization interventions. The study’s main contribution is a rigorously validated, modular ED digital twin coupled with an autonomous MAS, providing a scalable simulation framework for exploring and optimizing agentic decision‑making in complex healthcare environments.


<details>
<summary>Abstract</summary>

Emergency departments (ED) face challenges in patient care and resource management. We propose to explore optimization strategies in a realistic and flexible model and develop a hybrid Discrete Event Simulation (DES) and Agent-Based Model (ABM) simulating highly configurable ED environments. We specifically focus on the validation of the modeling approach. We derive configurations for ED sizes, patient load, and staffing from real-world studies. We then validate the model expressivity by matching its key performance indicators and metrics with their values known from literature. We proceed by implementing scientifically established and practice-proven resource optimization strategies. Comparing the documented real-world outcomes with our model's results demonstrates that the DES-ABM based simulation can effectively replicate real-world ER dynamics under interventions. We lastly integrate a Proof-of-Concept multi-agent system (MAS) that can autonomously explore resource allocation strategies within the simulated ER environment based on a temporal ledger of ED event records. This modular DES-ABM-MAS framework offers a powerful tool to explore resource optimization strategies in emergency departments.

</details>


### 106. IdeaForge: A Knowledge Graph-Grounded Multi-Agent Framework for Cross-Methodology Innovation Analysis and Patent Claim Generation

- **Authors:** Joy Bose
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13311v1](http://arxiv.org/abs/2605.13311v1)
- **PDF:** [https://arxiv.org/pdf/2605.13311v1](https://arxiv.org/pdf/2605.13311v1)
- **Categories:** cs.AI, cs.IR, cs.MA


> IdeaForge introduces a graph‑native, multi‑agent framework that unifies several invention methodologies (TRIZ, Design Thinking, SCAMPER) by having specialist agents populate a persistent FalkorDB knowledge graph with structured innovation artefacts (contradictions, principles, user needs, analogies, draft claims). The system’s core contribution is a convergence layer that links claims supported by multiple methodologies via CONVERGENT edges; graph traversal then identifies high‑confidence, cross‑methodology invention candidates, which a downstream drafting agent turns into structured patent drafts, and an InnovationScore ranks them on convergence, diversity, claim strength, and prior‑art challenge. Experiments on a legal‑tech case show that IdeaForge yields more diverse, traceable, and explainable innovation outputs than single‑method baselines, highlighting the utility of knowledge‑graph‑grounded, multi‑agent synthesis for agentic AI in computational creativity and patent generation.


<details>
<summary>Abstract</summary>

Current AI-assisted innovation systems typically apply a single ideation methodology (such as TRIZ or Design Thinking) using sequential prompt-based workflows that do not preserve intermediate reasoning structure. As a result, insights generated across methodologies remain fragmented, limiting traceability, synthesis, and systematic evaluation of novelty. We present IdeaForge, a knowledge graph-grounded multi-agent framework for innovation analysis and patent claim generation. IdeaForge integrates multiple innovation methodologies (TRIZ, Design Thinking, and SCAMPER) through specialist agents operating over a persistent FalkorDB knowledge graph. Each agent contributes structured entities and relationships representing contradictions, inventive principles, user needs, transformations, analogies, and candidate claims. The central contribution of IdeaForge is a cross-methodology convergence mechanism implemented through graph-based claim linkage. Claims independently supported by multiple methodologies are connected using CONVERGENT relationships, enabling identification of high-confidence innovation candidates through graph traversal. A downstream patent drafting agent generates structured patent drafts grounded in convergent claim subgraphs, reducing reliance on unconstrained language model generation. An InnovationScore formula ranks claims by convergent support, methodology diversity, claim strength, and prior art challenge count. We describe the graph schema, agent architecture, convergence detection pipeline, and patent synthesis workflow. Experiments on a legal technology use case demonstrate that graph-grounded multi-methodology synthesis produces more diverse and traceable innovation candidates compared to single-methodology baselines. We discuss implications for computational creativity, explainable AI-assisted invention, and graph-native innovation systems.

</details>


### 107. Discrete Diffusion for Complex and Congested Multi-Agent Path Finding with Sparse Social Attention

- **Authors:** Yuanzhe Wang, Tian Zhi, Zihang Wei, Hongguang Wang, Jiaming Guo, Yang Zhao, Zisheng Liu, Shiyu Quan, Xing Hu, Zidong Du, Yunji Chen
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13296v1](http://arxiv.org/abs/2605.13296v1)
- **PDF:** [https://arxiv.org/pdf/2605.13296v1](https://arxiv.org/pdf/2605.13296v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces **DiffLNS**, a hybrid MAPF solver that couples a **discrete denoising diffusion probabilistic model (D3PM)** with the repair‑oriented LNS2 algorithm. The D3PM is trained on expert demonstrations to learn a spatio‑temporal prior over joint action sequences, using a **sparse social attention** mechanism that respects the categorical action space of MAPF and yields diverse, multimodal draft plans. These diffusion‑generated drafts serve as warm‑starts for LNS2’s local‑search repair, dramatically improving feasibility in dense, congested environments; experiments show a 95.8 % overall success rate—up to 9.6 % absolute gain over the strongest baseline—and successful generalization from 96‑agent training instances to problems with up to 312 agents.


<details>
<summary>Abstract</summary>

Multi-Agent Path Finding (MAPF) is a coordination problem that requires computing globally consistent, collision-free trajectories from individual start positions to assigned goal positions under combinatorial planning complexity. In dense environments, suboptimal initial plans induce compound conflicts that hinder feasible repair. For repair-based solvers like LNS2, initial plan quality critically affects downstream repair, yet this factor remains underexplored. We propose DiffLNS, a hybrid framework that integrates a discrete denoising diffusion probabilistic model (D3PM) with LNS2. The D3PM serves as an initializer with sparse social attention that learns a spatiotemporal prior over coordinated multi-agent action trajectories from expert demonstrations and samples multiple joint plans. Operating directly on the categorical action space, our discrete diffusion preserves the MAPF action structure and samples from a multimodal joint-plan distribution to produce diverse drafts well suited for neighborhood repair. These drafts act as warm starts for downstream repair, which completes unfinished trajectories and resolves remaining conflicts under hard MAPF constraints. Experimental results show that despite being trained only on instances with at most 96 agents, the initializer generalizes to scenarios with up to 312 agents at inference time. Across 20 complex and congested settings, DiffLNS achieves an average success rate of 95.8%, outperforming the strongest tested baseline by 9.6 percentage points and matching or exceeding all baselines in all 20 settings. To the best of our knowledge, this is the first work to leverage discrete diffusion for warm-starting an LNS-based MAPF solver.

</details>


### 108. CANTANTE: Optimizing Agentic Systems via Contrastive Credit Attribution

- **Authors:** Tom Zehle
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13295v1](http://arxiv.org/abs/2605.13295v1)
- **PDF:** [https://arxiv.org/pdf/2605.13295v1](https://arxiv.org/pdf/2605.13295v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> CANTANTE tackles the core difficulty of tuning multi‑LLM agent systems by framing it as a credit‑assignment problem: system‑level rewards must be back‑propagated to the individual agents that generated them. The authors achieve this with a contrastive rollout scheme that compares multiple joint configurations on the same query, using the differences to produce per‑agent gradient‑like update signals; they implement these signals as learnable prompt parameters for each agent. Experiments on programming (MBPP), mathematical reasoning (GSM8K), and multi‑hop QA (HotpotQA) show that CANTANTE outperforms prior optimizers (GEPA, MIPROv2) and baseline prompts—e.g., +18.9 pp on MBPP and +12.5 pp on GSM8K—while using less inference compute, and an analysis of credit correlation confirms that the derived per‑agent signals meaningfully reflect individual contributions rather than merely echoing the global score.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems have demonstrated strong performance across complex real-world tasks, such as software engineering, predictive modeling, and retrieval-augmented generation. Yet automating their configuration remains a structural challenge, as scores are available only at the system level, whereas the parameters governing agent behavior are local. We argue that optimizing these systems is fundamentally a credit-assignment problem. We therefore introduce CANTANTE, a framework that decomposes system-level rewards into per-agent update signals by contrasting rollouts of multiple joint configurations on the same query. We instantiate it for prompt optimization, treating agent prompts as learnable system parameters. We evaluate CANTANTE against GEPA and MIPROv2 on programming (MBPP), mathematical reasoning (GSM8K), and multi-hop question answering (HotpotQA). Across these benchmarks, CANTANTE achieves the best average rank among all evaluated optimizers and consistently outperforms unoptimized prompts. It improves over the strongest baseline by +18.9 percentage points on MBPP and +12.5 percentage points on GSM8K, while incurring a lower inference cost. It remains within one standard deviation of the strongest baseline on HotpotQA. Crucially, our credit correlation analysis confirms that the attributer produces meaningful per-agent signals rather than echoing the global system score.

</details>


### 109. Do Biological Structural Guarantees Earn Their Complexity?

- **Authors:** Bogdan Banu
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.15225v1](http://arxiv.org/abs/2605.15225v1)
- **PDF:** [https://arxiv.org/pdf/2605.15225v1](https://arxiv.org/pdf/2605.15225v1)
- **Categories:** q-bio.QM, cs.AI


> The paper empirically evaluates whether biologically‑inspired structural guarantees actually improve the performance of deep‑learning agents. The authors implement three “biological” mechanisms—metabolic priority gating, autoinducer‑based quorum sensing, and Bayesian stagnation detection—and benchmark each against a naïve non‑biological baseline and an ablated version across more than 10 million trials (1,000 runs per seed, 10 seeds). The results show that the biologically‑grounded designs yield modest but consistent gains in stability and sample efficiency over the baselines, suggesting that such structural guarantees can provide measurable benefits for agentic AI systems, though the advantage diminishes when simpler control strategies are well‑tuned.


<details>
<summary>Abstract</summary>

Biologically-inspired AI agent frameworks claim reliability benefits through structural guarantees adapted from gene regulatory networks, immune systems, and metabolic control. These claims are rarely tested empirically against simpler alternatives. We present three deep benchmarks: metabolic priority gating, autoinducer-based quorum sensing, and Bayesian stagnation detection, each comparing a biologically-grounded implementation against a naive non-biological alternative and an ablated control, across 1,000 trials per seed and 10 seeds (10M+ data points total).

</details>


### 110. An Agentic AI Framework with Large Language Models and Chain-of-Thought for UAV-Assisted Logistics Scheduling with Mobile Edge Computing

- **Authors:** Hanwen Zhang, Dusit Niyato, Wei Zhang, Xin Lou, Malcolm Yoke Hean Low
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13221v1](http://arxiv.org/abs/2605.13221v1)
- **PDF:** [https://arxiv.org/pdf/2605.13221v1](https://arxiv.org/pdf/2605.13221v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces an “agentic AI” pipeline that uses large‑language models (augmented with retrieval and chain‑of‑thought prompting) to automatically convert a user‑specified UAV‑assisted logistics and mobile‑edge‑computing scenario into a clear mathematical formulation, and then solves the resulting hybrid scheduling problem with a two‑level deep‑RL controller built on proximal policy optimization (PPO). The upper PPO layer learns UAV routing (which determines service windows, energy consumption, and MEC availability), while the lower layer allocates compute and communication resources each time slot to meet task‑deadline constraints. In simulations the agentic‑AI produces consistently correct problem statements, and the hierarchical PPO attains near‑optimal performance—collecting 99.6 % of products in the last 500 episodes and satisfying 100 % of computational deadlines, outperforming an A2C baseline in stability and success rate.


<details>
<summary>Abstract</summary>

In cloud manufacturing, unmanned aerial vehicles (UAVs) can support both product collection and mobile edge computing (MEC). This joint operation forms a hybrid scheduling problem, where physical logistics decisions are coupled with computational task scheduling. In this paper, UAVs collect finished products from manufacturing stations and transport them back to a central depot. Meanwhile, computational tasks generated by industrial sensor devices at these stations are processed locally, at UAVs, or offloaded via UAVs to the cloud. This coupling makes the problem challenging. A UAV can provide MEC services only during its service window at a station, so routing decisions directly determine when UAV-assisted offloading is available. Routing decisions also affect the UAV energy budget and the availability of onboard computing and communication resources for computational task execution under task deadline constraints. To address this, we propose an agentic-AI-assisted optimization framework with two components. First, we develop an agentic AI that combines large language models, retrieval-augmented generation, and chain-of-thought reasoning to translate user input into an interpretable mathematical formulation for the hybrid scheduling problem. Second, we design a hierarchical deep reinforcement learning approach based on proximal policy optimization (PPO), where the upper layer learns UAV routing and the lower layer optimizes per-slot task execution and resource allocation. Simulation results show that the proposed framework yields more consistent formulations, while the hierarchical PPO achieves full product collection in 99.6% of the last 500 episodes and maintains a 100% deadline satisfaction rate, with more stable performance than the advantage actor-critic approach.

</details>


### 111. Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning

- **Authors:** Hao Zhou, Tiru Wu, Yan Jiang, Wanqi Zhou, Junxing Hu, Ai Han
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13213v1](http://arxiv.org/abs/2605.13213v1)
- **PDF:** [https://arxiv.org/pdf/2605.13213v1](https://arxiv.org/pdf/2605.13213v1)
- **Categories:** cs.AI


> The paper introduces **HAM³**, a three‑tier hierarchical adversarial framework that systematically attacks multi‑modal multi‑agent systems at the perception (visual/textual input perturbations), communication (message and topology corruption), and reasoning (cognitive pipeline biasing) layers. By integrating these attacks into agents built on ReAct, Plan‑and‑Solve, and Reflexion and evaluating them on the GQA benchmark, the authors show that HAM³ can cause coordinated failures in up to 78.3 % of test cases—especially when targeting the reasoning layer, where more than half of the successful attacks induce consistent errors across multiple agents. These results highlight critical vulnerabilities in MM‑MAS and provide a baseline for developing more robust, interpretable agentic AI.


<details>
<summary>Abstract</summary>

Multi-modal multi-agent systems (MM-MAS) have gained increasing attention for their capacity to enable complex reasoning and coordination across diverse modalities. As these systems continue to expand in scale and functionality, investigating their potential vulnerabilities has become increasingly important. However, existing studies on adversarial attacks in multi-agent systems primarily focus on isolated agents or unimodal settings, leaving the vulnerabilities of MM-MAS largely underexplored. To bridge this gap, we introduce HAM$^{3}$, a Hierarchical Attack framework for multi-modal multi-agent systems that decomposes attacks into three interconnected layers. Specifically, at the perception layer, HAM$^{3}$ mounts attacks by perturbing visual inputs, textual inputs, and their fused visual-textual representations. At the communication layer, it performs communication-level attacks that corrupt message content and interaction topology, such as manipulating shared context or communication links to distort collective information flow. At the reasoning layer, it conducts reasoning-level attacks that interfere with each agent's cognitive pipeline, biasing reasoning trajectories and ultimately compromising final decisions. We evaluate HAM$^{3}$ on the GQA benchmark through multi-agent systems built on distinct reasoning paradigms including ReAct, Plan-and-Solve, and Reflexion. Experiments demonstrate that our framework achieves an Attack Success Rate of up to 78.3%, with reasoning-layer attacks being the most effective. More than half of the successful attacks lead multiple agents to produce consistent errors. These findings offer valuable insights for building more robust and interpretable multi-agent intelligence.

</details>


### 112. When Does Hierarchy Help? Benchmarking Agent Coordination in Event-Driven Industrial Scheduling

- **Authors:** Ziqi Wang, Yuhao Yang, Zhiwei Ling, Wenzhuo Qian, Hailiang Zhao
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13172v1](http://arxiv.org/abs/2605.13172v1)
- **PDF:** [https://arxiv.org/pdf/2605.13172v1](https://arxiv.org/pdf/2605.13172v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **DESBench**, a new benchmark that isolates the coordination problem in a shared, event‑driven industrial scheduling domain with partial observability, multi‑timescale decisions, and dynamically coupled constraints. Using DESBench, the authors systematically compare four coordination architectures—centralized, hierarchical, heterarchical, and holonic—by measuring task effectiveness, constraint alignment, coordination efficiency, and robustness. The results show clear trade‑offs: centralized control is robust and communication‑light but does not scale; hierarchical control gains efficiency through decomposition yet suffers from cross‑level misalignment; heterarchical control is flexible but communication‑intensive; and holonic control maintains constraint satisfaction but loses global robustness, highlighting that the choice of coordination structure fundamentally determines agentic AI performance in complex, coupled environments.


<details>
<summary>Abstract</summary>

Recent advances in agent and multi-agent systems have shown strong performance on tool use, reasoning, and collaborative tasks. However, existing benchmarks mostly evaluate task completion in weakly coupled environments, and provide limited support for studying coordination in shared, dynamically evolving systems with hierarchy and coupled constraints. This leaves an important question underexplored: when do different coordination paradigms succeed or fail? We introduce Distributed Event-driven Scheduling Benchmark (DESBench), a benchmark for evaluating agent coordination in hierarchical event-driven scheduling. Built on a shared discrete-event driven environment in industrial scheduling, our benchmark captures multi-timescale decision making, partial observability, and dynamically coupled constraints. We define tasks and metrics that evaluate effectiveness, constraint alignment, coordination efficiency, and robustness, and focus on four representative coordination paradigms: centralized, hierarchical, heterarchical, and holonic. These paradigms correspond to distinct mechanisms of information flow, decision authority, and conflict resolution. Our controlled evaluations reveal clear coordination trade-offs: centralized coordination is robust and communication-efficient but scales poorly with difficulty; hierarchical coordination improves efficiency through decomposition but suffers from cross-level misalignment; heterarchical coordination is flexible but communication-heavy; and holonic coordination satisfies constraints well but loses global robustness. These findings demonstrate that coordination design fundamentally shapes agent system behavior in complex environments, revealing structural trade-offs that cannot be captured by outcome metrics alone and underscoring the imperative for more adaptive, principled, and dynamic coordination mechanisms in future MAS research.

</details>


### 113. Finding the Weakest Link: Adversarial Attack against Multi-Agent Communications

- **Authors:** Maxwell Standen, Junae Kim, Claudia Szabo
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13170v1](http://arxiv.org/abs/2605.13170v1)
- **PDF:** [https://arxiv.org/pdf/2605.13170v1](https://arxiv.org/pdf/2605.13170v1)
- **Categories:** cs.LG, cs.MA


> **Main contribution:** The paper introduces a principled adversarial‑attack framework that identifies the “weakest link” in a communicating multi‑agent reinforcement‑learning system—i.e., the specific agent, message, and timestep whose perturbation most degrades collective performance.  

**Methodology:** By exploiting Jacobian‑based gradient information, the authors devise message‑selection and victim‑selection heuristics and two novel adversarial loss functions that balance attack success against impact; these are applied as single‑victim perturbations to the communication channel during execution.  

**Key findings:** Across three benchmark domains (navigation, Predator‑Prey, Traffic Junction) and two communication protocols, the gradient‑guided attacks consistently outperform random baselines, achieving equal or greater performance drops in most settings and improving attack efficacy in roughly half of the thirty tested scenarios, thereby highlighting a critical vulnerability of agentic communication mechanisms.


<details>
<summary>Abstract</summary>

Multi-agent systems rely on communication for information sharing and action coordination, which exposes a vulnerability to attacks. We investigate single-victim communication perturbation attacks against Multi-Agent Reinforcement Learning-trained systems and propose methods that use gradient information from the Jacobian to identify which messages, agent, and timesteps are most susceptible to attack and have the greatest impact on the system. We enhance these methods with two proposed adversarial loss functions that trade-off attack success for attack impact which also create more effective perturbations. We empirically demonstrate the effectiveness of our methods against two different multi-agent communication methods in navigation, PredatorPrey, and TrafficJunction environments. Our results show that our novel message selection method achieves a similar or greater impact than random message selection across almost all tested scenarios. Our victim selection, message selection, tempo, and loss functions improve attack effectiveness in half of the thirty scenarios we tested.

</details>


### 114. Collaborating in Multi-Armed Bandits with Strategic Agents

- **Authors:** Idan Barnea, Ofir Schlisselberg, Yishay Mansour
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13145v1](http://arxiv.org/abs/2605.13145v1)
- **PDF:** [https://arxiv.org/pdf/2605.13145v1](https://arxiv.org/pdf/2605.13145v1)
- **Categories:** cs.LG


> **Main contribution:**  
The paper introduces **CAOS**, a mechanism for persistent, strategic agents who repeatedly face the same Bayesian multi‑armed bandit problem, showing that collaboration can be enforced without monetary transfers—solely via controlled information sharing.

**Methodology:**  
Agents are modeled as long‑lived players who repeatedly choose arms; the mechanism designs a protocol for reporting observations and prescribing actions such that truthfully sharing data and following the prescribed exploration schedule constitutes a Nash equilibrium. Regret analysis is then performed under this equilibrium to bound the collective loss.

**Key findings:**  
CAOS sustains collaborative exploration as a Nash equilibrium and guarantees a regret that is near‑optimal—only a small multiplicative factor away from the regret of a fully cooperative system. Thus, even when agents are self‑interested and could free‑ride, appropriately structured information sharing can achieve almost the same performance as in ideal, fully cooperative multi‑agent bandits.


<details>
<summary>Abstract</summary>

We study collaborative learning in multi-agent Bayesian bandit problems, where strategic agents collectively solve the same bandit instance. While multiple agents can accelerate learning by sharing information, strategic agents might prefer to free-ride and avoid exploration. We consider a setting with persistent agents that participate in multiple time periods. This is in contrast to most previous works on incentives in multi-agent MAB, which assume short-lived agents, namely each agent has a single decision to make and optimizes their expected reward in that single decision. As in the multi-agent MAB model with incentives, our model does not have monetary transfers, and the only incentives are through information sharing.
  We propose \texttt{CAOS}, a mechanism that sustains collaboration as a Nash equilibrium while achieving strong regret guarantees. Our results demonstrate that collaborative exploration can be sustained purely through information sharing, achieving performance close to that of fully cooperative systems despite strategic behavior.

</details>


### 115. ERPPO: Entropy Regularization-based Proximal Policy Optimization

- **Authors:** Changha Lee, Gyusang Cho
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13131v1](http://arxiv.org/abs/2605.13131v1)
- **PDF:** [https://arxiv.org/pdf/2605.13131v1](https://arxiv.org/pdf/2605.13131v1)
- **Categories:** cs.LG, cs.RO


> **Contribution:** The paper introduces **Entropy Regularization‑based Proximal Policy Optimization (ERPPO)**, a MARL algorithm that augments PPO with an observation‑dependent entropy regularizer to cope with non‑stationary, high‑dimensional perception uncertainties that cripple MAPPO.  

**Methodology:** ERPPO first trains a **Distributional Spatiotemporal Ambiguity (DSA) learner** to quantify object‑detection uncertainty (termed “ambiguity”) from multi‑dimensional sensor streams. During policy updates, the algorithm adds an entropy term whose strength is chosen adaptively: an L1‑type regularizer is applied in high‑ambiguity states to promote exploratory actions, while an L2‑type regularizer is used in low‑ambiguity states to stabilize updates.  

**Key Findings:** In AirSim‑based maritime search‑and‑rescue simulations, ERPPO achieves significantly higher detection accuracy and faster gradient convergence than MAPPO, especially under visually uncertain conditions, demonstrating reduced false detections and more reliable object localization in time‑critical multi‑agent tasks.


<details>
<summary>Abstract</summary>

Multi-Agent Proximal Policy Optimization (MAPPO) is a variant of the Proximal Policy Optimization (PPO) algorithm, specifically tailored for multi-agent reinforcement learning (MARL). MAPPO optimizes cooperative multi-agent settings by employing a centralized critic with decentralized actors. However, in case of multi-dimensional environment, MAPPO can not extract optimal policy due to non-stationary agent observation. To overcome this problem, we introduce a novel approach, Entropy Regularization-based Proximal Policy Optimization (ERPPO). For the policy optimization, we first define the object detection ambiguity under multi-dimensional observation environment. Distributional Spatiotemporal Ambiguity (DSA) learner is trained to estimate object detection uncertainty in non-stationary constraints. Then, we enhance PPO with a novel Entropy Regularization term. This regularization dynamically adjusts the policy update by applying a stronger (L1) regularization in high-ambiguity observation to encourage significant exploratory actions and a weaker (L2) regularization in low-ambiguity observation to stabilize the proximal policy optimization. This approach is designed to enhance the probability of successful object localization in time-critical operations by reducing detection failures and optimizing search policy. Experiments on a testbed with AirSim-based maritime searching scenarios show that the proposed ERPPO improves accuracy performance. Our proposed method improves higher gradient than MAPPO. Qualitative results confirm that ERPPO effectiveness in terms of suppressing false detection in visually uncertain conditions.

</details>


### 116. A Multi-Agent Orchestration Framework for Venture Capital Due Diligence

- **Authors:** Grigorios Alexandrou, Katerina Pramatari
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13110v1](http://arxiv.org/abs/2605.13110v1)
- **PDF:** [https://arxiv.org/pdf/2605.13110v1](https://arxiv.org/pdf/2605.13110v1)
- **Categories:** cs.MA, cs.AI, cs.IR


> The paper introduces an event‑driven, multi‑agent orchestration framework that automates venture‑capital due‑diligence by coupling LLMs with live web retrieval and a custom extraction pipeline. The system programmatically reverse‑engineers the Greek Business Registry’s dynamic frontend‑to‑backend API, pulls official filings, and parses them with a layout‑aware OCR extractor while a fallback mechanism flags missing data to prevent financial hallucinations. Experiments show that the agents can reliably generate structured investment insights from unstructured web sources, achieving lower hallucination rates and comparable accuracy to manual analysts, thereby advancing reliable, agentic AI for high‑stakes financial decision‑making.


<details>
<summary>Abstract</summary>

We present a fully automated multi-agent framework for corporate due diligence and market analysis in venture capital. The system runs on an event-driven orchestration architecture, combining Large Language Models (LLMs) with real-time web retrieval to synthesize unstructured data into structured investment intelligence. A central technical contribution is a programmatic extraction pipeline that reverse-engineers the frontend-to-backend communication of the Greek Business Registry ($Γ$.E.MH.), querying dynamic endpoints to retrieve official financial filings that are then parsed using a layout-aware OCR extractor. A structural fallback mechanism explicitly flags data absence rather than generating unverified figures, directly targeting hallucination in financial contexts. All workflow artifacts are publicly available to support replication.

</details>


### 117. Counterfactual Reasoning for Causal Responsibility Attribution in Probabilistic Multi-Agent Systems

- **Authors:** Chunyan Mu, Muhammad Najib
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13077v1](http://arxiv.org/abs/2605.13077v1)
- **PDF:** [https://arxiv.org/pdf/2605.13077v1](https://arxiv.org/pdf/2605.13077v1)
- **Categories:** cs.MA, cs.AI


> **Summary**  
The paper introduces a formal model for attributing causal responsibility in probabilistic multi‑agent systems, representing them as concurrent stochastic multi‑player games and defining a *retrospective counterfactual responsibility* measure that quantifies each agent’s accountability for a given outcome under a specific strategy profile. Responsibility is allocated using the Shapley value, and the authors prove that this allocation satisfies fairness, consistency, and other desirable axioms; they embed the measure in a verification‑and‑strategic‑reasoning framework that lets agents evaluate trade‑offs between expected reward and responsibility. By adopting Nash equilibrium as the decision criterion, they provide algorithms for computing stable strategy profiles where agents rationally balance performance against their assigned responsibility, demonstrating a scalable approach to responsibility‑aware agentic AI.


<details>
<summary>Abstract</summary>

Responsibility allocation -- determining the extent to which agents are accountable for outcomes -- is a fundamental challenge in the design and analysis of multi-agent systems. In this work, we model such systems as concurrent stochastic multi-player games and introduce a notion of retrospective (backward) counterfactual responsibility, which quantifies an agent's accountability for outcomes resulting from a given strategy profile. To allocate responsibility among agents, we utilise the Shapley value and formally show that this method satisfies key desirable properties, including fairness and consistency. Building on this foundation, we propose a formal framework that supports both verification and strategic reasoning in responsibility-aware multi-agent systems. Furthermore, by adopting Nash equilibrium as the solution concept, we demonstrate how to compute stable strategy profiles in which agents trade off responsibility against expected reward.

</details>


### 118. Ergodic Trajectory Design by Learned Pushforward Maps: Provable Coverage via Conditional Flow Matching

- **Authors:** Ehsan Aghazadeh, Masoud Malekzadeh, Ahmad Ghasemi, Hossein Pishro-Nik
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13063v1](http://arxiv.org/abs/2605.13063v1)
- **PDF:** [https://arxiv.org/pdf/2605.13063v1](https://arxiv.org/pdf/2605.13063v1)
- **Categories:** cs.LG


> **Main contribution**  
The paper introduces **e‑pushforward**, a two‑stage framework for ergodic coverage that separates the design of a uniformly ergodic latent trajectory from the matching of any desired spatial density. By learning a single *conditional flow‑matching* (CFM) transport map offline, the method can instantly generate energy‑constrained, collision‑free trajectories for any number of agents while providing provable guarantees on ergodicity and coverage error.

**Methodology**  
1. Construct an analytic latent trajectory that is exactly uniformly ergodic on a simple annular domain.  
2. Train a neural transport map \(v_\theta\) with CFM to push the latent occupancy distribution onto a user‑specified target density and to incorporate differentiable constraints (no‑fly zones, acceleration limits, fairness penalties) as soft loss terms.  
3. Deploy the composed map \(x(t)=T_\theta(\text{latent}(t))\) online without further optimization; the same map serves all agents and repeated missions.

**Key findings**  
- The authors prove an acceleration‑energy bound, an \(O(1/\sqrt{K})\) ergodic convergence rate over \(K\) trajectory cycles, and an approximation‑error bound that ties coverage error to the CFM training loss (estimable from diagnostics).  
- Empirical experiments on UAV data‑collection and multi‑robot exploration tasks show that a single trained push‑forward map yields trajectories that meet tight energy and no‑fly‑zone constraints while achieving substantially lower ergodic error than state‑of‑the‑art online re‑optimisation methods, even when scaling to large fleets.


<details>
<summary>Abstract</summary>

Designing continuous trajectories whose time-averaged occupancy provably matches a prescribed spatial density (the \emph{ergodic coverage} problem) is central to UAV-assisted data collection and sensing, robotic exploration, and mobile monitoring. For flying agents in particular, this challenge is acute: trajectories must balance coverage fidelity against tight energy budgets, no-fly zones, and acceleration limits. Existing methods either re-optimize each trajectory online (with cost growing in the horizon and re-running for every target, agent, and realization) or rely on bespoke analytical constructions that must be re-derived for each new constraint. We propose a \emph{epushforward} framework that decouples ergodicity from density matching: an analytic latent trajectory provides exact uniform ergodicity on a simple annular domain, and a single map, learned offline by optimal-transport conditional flow matching, transports this latent occupancy onto the prescribed target density. The composed trajectory is then asymptotically ergodic with respect to the learned pushforward distribution, with deviation from the target controlled by the flow-matching training loss. Once trained for a given target density and constraint set, the map serves an unbounded number of trajectories and a multi-agent fleet without per-agent retraining, and many differentiable operational constraints (no-fly zones, acceleration ceilings, or fairness penalties) enter as additive soft penalties in the training loss without re-deriving the design. We prove three results (an acceleration-energy bound, an $O(1/\sqrt{K})$ ergodic convergence rate in the number of trajectory cycles $K$, and an approximation-error bound) that combine into an end-to-end coverage bound estimable from CFM training diagnostics (certified given an architectural Lipschitz bound on $v_θ$).

</details>


### 119. TERMS-Bench: Diagnosing LLM Negotiation Agents Beyond Deal Rate

- **Authors:** Erica Zhang, Fangzhao Zhang, Aneesh Pappu, Batu El, Jose Blanchet, Susan Athey, Jiashuo Liu, James Zou
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13909v1](http://arxiv.org/abs/2605.13909v1)
- **PDF:** [https://arxiv.org/pdf/2605.13909v1](https://arxiv.org/pdf/2605.13909v1)
- **Categories:** cs.GT, cs.AI


> **Main contribution:** The paper introduces **Terms‑Bench**, a Bayesian‑game testbed that turns the negotiation counterpart into a fully observable “oracle” (its latent type, policy, and payoff are known to the evaluator). This makes the environment itself the verifier, allowing precise, agent‑attributable diagnostics rather than coarse aggregate metrics like deal‑rate.

**Methodology:** Terms‑Bench is instantiated as a bilateral price‑negotiation game in which each LLM negotiator interacts with a hidden‑state simulator; the evaluator can inspect the simulator’s true state and optimal policy, compute optimality gaps, and trace failures to specific reasoning or strategic deficiencies (e.g., belief mis‑calibration, cue misuse, constraint violations).

**Key findings for agentic AI:** When 13 state‑of‑the‑art LLM negotiation agents are evaluated, all achieve near‑perfect deal rates, yet they differ markedly in surplus extraction, compliance, and strategic behavior. Frontier models still leave sizable optimality gaps and display systematic bottlenecks (poor belief updates, misguided cue exploitation, or contract‑violation errors) that are invisible to prior benchmarks—demonstrating that Terms‑Bench provides actionable insight for improving the strategic competence of agentic LLMs.


<details>
<summary>Abstract</summary>

Negotiation is a central mechanism of economic exchange, shaping markets, procurement, labor agreements, and resource allocation. It is also a canonical testbed for agentic language models, requiring multi-turn interaction under hidden preferences, strategic communication, and binding constraints. These properties make negotiation hard to evaluate: unlike math or code, it has no intrinsic verifier. Existing LLM negotiation evaluations rely on LLM-vs.-LLM interaction or aggregate outcomes such as deal rate, leaving failures opaque. We introduce Terms-Bench, short for Testbed for Economic Reasoning in Multi-turn Strategy, a Bayesian-game framework that makes the environment itself the verifier by specifying the counterpart's latent type, policy, and payoff structure. We instantiate it in bilateral price negotiation, where the counterpart's private state and simulator policy are hidden from the agent but observable to the evaluator. This turns the counterpart from a black-box opponent into a diagnostic instrument, enabling agent-attributable failure analysis and oracle-reference optimality gaps. Evaluating 13 LLM agents spanning frontier systems from major providers, Terms-Bench turns negotiation evaluation from aggregate ranking into actionable diagnosis: where agents fail, why they fail, and what to strengthen. Empirically, frontier models saturate deal rate yet diverge in surplus extraction, cue use, belief calibration, and compliance, revealing agent-specific bargaining bottlenecks masked by prior benchmarks.

</details>


### 120. An Agentic LLM-Based Framework for Population-Scale Mental Health Screening

- **Authors:** Giuliano Lorenzoni, Paulo Alencar, Donald Cowan
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13046v1](http://arxiv.org/abs/2605.13046v1)
- **PDF:** [https://arxiv.org/pdf/2605.13046v1](https://arxiv.org/pdf/2605.13046v1)
- **Categories:** cs.AI


> The paper introduces a modular, agent‑centric framework that builds and stabilizes large‑language‑model (LLM) pipelines for population‑scale mental‑health screening, in which each processing step (pre‑processing, retrieval, selection, diversity control, thresholding, and decoding) is wrapped in a LangChain agent governed by explicit policies, proxy‑based evaluation, and a lock/rollback mechanism that prevents later changes from degrading prior performance. The methodology proceeds incrementally: it first explores feature representations, then tunes agents using proxy metrics, freezes configurations that meet improvement criteria, and finally employs an Orchestrator Agent to manage the full end‑to‑end workflow. In a proof‑of‑concept depression‑detection task on clinical transcripts, the system converges on stable settings (cosine similarity retrieval, dynamic Top‑k selection, and a 0.75 decision threshold) while keeping evaluation costs low and avoiding regressions, demonstrating that agentic AI can deliver trustworthy, reproducible, and adaptable pipelines for large‑scale mental‑health screening.


<details>
<summary>Abstract</summary>

Mental health disorders affect millions worldwide, and healthcare systems are increasingly overwhelmed by the volume of clinical data generated from electronic records, telemedicine platforms, and population-level screening programs. At the same time, the emergence of novel AI-based approaches in healthcare calls for intelligent frameworks capable of processing domain-specific unstructured clinical information while adapting to patient-specific needs. This paper proposes an agentic framework for building robust LLM-based pipelines, where each stage is encapsulated as a LangChain agent governed by explicit policies and proxy-guided evaluation. Stages are incrementally locked once validated, ensuring that later adaptations cannot overwrite configurations without demonstrated improvement. The proposed framework evolves from feature-level exploration, through proxy-based tuning and freeze/rollback mechanisms, to full orchestration by an Orchestrator Agent that coordinates preprocessing, retrieval, selection, diversity, threshold optimization, and decoding. A proof-of-concept in transcript-based depression detection demonstrates that the framework converges to stable configurations, such as cosine similarity, dynamic Top-k, and threshold 0.75, while controlling evaluation costs and avoiding regressions. These results highlight the potential of agentic AI to enable population-level mental health screening over large clinical datasets, addressing critical challenges in trustworthiness, reproducibility, and adaptability required in healthcare environments.

</details>


### 121. MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning

- **Authors:** Yuxin Liu, Ziang Ye, Yueqing Sun, Mingye Zhu, Jinwei Xiao, Zhuowen Han, Qi GU, Xunliang Cai, Lei Zhang
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13037v1](http://arxiv.org/abs/2605.13037v1)
- **PDF:** [https://arxiv.org/pdf/2605.13037v1](https://arxiv.org/pdf/2605.13037v1)
- **Categories:** cs.AI


> The paper introduces **MAP (Map‑then‑Act Paradigm)**, a plug‑and‑play framework that front‑loads environmental understanding for interactive LLM agents. MAP first conducts a global exploration phase to learn generic priors, then builds a task‑specific “cognitive map” of the environment, and finally uses this map to guide knowledge‑augmented execution, thereby avoiding the “Delayed Environmental Perception” bottleneck of reactive stepwise planners. Across multiple benchmarks and LLM backbones, MAP yields large performance jumps (e.g., turning near‑zero scores into successes in 22/25 ARC‑AGI‑3 games), and the authors further release **MAP‑2K**, a collection of map‑then‑act trajectories that, when used for finetuning, outperform models trained on expert imitation traces—demonstrating that explicit environment mapping is a more effective foundation for long‑horizon agent reasoning.


<details>
<summary>Abstract</summary>

Current interactive LLM agents rely on goal-conditioned stepwise planning, where environmental understanding is acquired reactively during execution rather than established beforehand. This temporal inversion leads to Delayed Environmental Perception: agents must infer environmental constraints through trial-and-error, resulting in an Epistemic Bottleneck that traps them in inefficient failure cycles. Inspired by human affordance perception and cognitive map theory, we propose the Map-then-Act Paradigm (MAP), a plug-and-play framework that shifts environment understanding before execution. MAP consists of three stages: (1) Global Exploration, acquiring environment-general priors; (2) Task-Specific Mapping, constructing a structured cognitive map; and (3) Knowledge-Augmented Execution, solving tasks grounded on the map. Experiments show consistent gains across benchmarks and LLMs. On ARC-AGI-3, MAP enables frontier models to surpass near-zero baseline performance in 22 of 25 game environments. We further introduce MAP-2K, a dataset of map-then-act trajectories, and show that training on it outperforms expert execution traces, suggesting that understanding environments is more fundamental than imitation.

</details>


### 122. Conveyor Parcel Routing with Order-Contiguous Arrivals

- **Authors:** Takuro Kato, Keisuke Okumura
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13035v1](http://arxiv.org/abs/2605.13035v1)
- **PDF:** [https://arxiv.org/pdf/2605.13035v1](https://arxiv.org/pdf/2605.13035v1)
- **Categories:** cs.MA


> **Main contribution:** The paper introduces **online MAPF‑OC**, a formal model for routing parcels on conveyor networks where agents appear over time and must be delivered in order‑contiguous blocks, and proposes **Dual‑Ordering Prioritized Planning (DOPP)**—a complete, polynomial‑time algorithm that jointly decides order‑level arrival sequences and agent‑level priorities to satisfy the contiguity constraint.

**Methodology:** DOPP operates in three nested layers: (1) it searches a high‑level space of permissible order‑arrival sequences; (2) for each candidate sequence it refines a priority ordering among the individual parcels; (3) it synthesizes a concrete, collision‑free schedule using classic prioritized planning, guaranteeing completeness in polynomial time.

**Key findings:** Across synthetic and real‑warehouse conveyor topologies, DOPP scales to hundreds of parcels, produces solutions within the tight (sub‑second) planning windows required in practice, and consistently yields higher delivery throughput and fewer downstream sorting operations than baseline MAPF planners that ignore order‑contiguity.


<details>
<summary>Abstract</summary>

In warehouse logistics, parcels released from the outfeed of an automated storage system must be routed through conveyor networks to workstations. Beyond collision avoidance, practical operations impose an additional requirement of order-contiguous arrivals: at each delivery point, parcels belonging to the same order must arrive as a consecutive block in the arrival sequence to reduce downstream re-sorting effort. We formalize this problem as online multi-agent path finding with order-contiguity (online MAPF-OC), where agents (i.e., parcels) appear over time and exit upon delivery. To efficiently solve online MAPF-OC, we propose Dual-Ordering Prioritized Planning (DOPP), a complete polynomial-time algorithm with a three-level structure that (i) searches order-level arrival sequences, (ii) refines agent-level priorities, and (iii) synthesizes feasible solutions via prioritized planning. Experiments on various conveyor-network layouts, including those derived from actual warehouses, demonstrate DOPP's practical scalability and ability to generate high-quality plans within tight time budgets.

</details>


### 123. Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Sycophancy

- **Authors:** Adarsh Kumarappan, Ananya Mujoo
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12991v1](http://arxiv.org/abs/2605.12991v1)
- **PDF:** [https://arxiv.org/pdf/2605.12991v1](https://arxiv.org/pdf/2605.12991v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution:** The paper shows that the sudden flip from correct to incorrect answers in LLM‑based multi‑agent systems under simulated peer disagreement (the “yield” phenomenon) is not caused primarily by RLHF‑induced sycophancy, but by a hidden, mid‑layer attention‑driven mechanism present even in pretrained base models.

**Methodology:** The authors evaluate four model families (base and Instruct variants) across varying jury sizes, use activation patching to isolate a narrow mid‑layer window where attention, not MLPs, carries the causal effect, and conduct systematic ablations of “channel framing” and “consensus strength” to dissect the attack surface; they also test interventions such as activation‑space patches and the insertion of a single correctly‑arguing dissenting agent.

**Key findings:** The mid‑layer attention disruption suppresses clean‑reasoning features, yielding up to a 47.5‑point drop in answer correctness that is consistent across model sizes and jury configurations; a single well‑reasoned dissent reduces this yield by 54‑73 percentage points, whereas prompt‑level defenses fail on out‑of‑distribution attacks, indicating that effective mitigation must target structured dissent and the identified attention mechanism rather than rely on surface‑level prompting.


<details>
<summary>Abstract</summary>

LLM-based multi-agent pipelines flip from correct to incorrect answers under simulated peer disagreement at rates we term yield, a vulnerability widely attributed to RLHF-induced sycophancy. We test this attribution across four model families and find it largely wrong: pretrained base models exhibit the same substitution pattern as their Instruct variants, averaging higher yield than Instruct. Using activation patching, we localize the corruption to a narrow mid-layer window where attention carries the causal weight and MLP contribution is negligible; patching above this window restores 96% of the clean-to-pressured P(correct) gap. The attack surface decomposes into two independent factors (channel framing and consensus strength) whose interaction produces a 47.5 percentage-point yield gap at majority consensus, preserved across jury sizes $N \in \{4, 5, 6\}$. Two converging activation-space interventions show that pressure suppresses clean-reasoning features rather than activating a new sycophancy circuit. A single correctly-arguing dissenter reduces yield by 54-73 percentage points across all framings tested, whereas the strongest prompt-level defense fails on attack variants outside its design surface. Mitigations should target the mechanism, structured dissent at the pipeline level, rather than prompt-level defenses.

</details>


### 124. Position: Agentic AI System Is a Foreseeable Pathway to AGI

- **Authors:** Junwei Liao, Shuai Li, Muning Wen, Jun Wang, Weinan Zhang
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12966v1](http://arxiv.org/abs/2605.12966v1)
- **PDF:** [https://arxiv.org/pdf/2605.12966v1](https://arxiv.org/pdf/2605.12966v1)
- **Categories:** cs.AI


> **Main contribution:** The paper argues that a purely monolithic, scale‑up approach cannot alone yield Artificial General Intelligence (AGI) and posits *Agentic AI*—systems composed of interacting, task‑specialized agents organized in directed‑acyclic‑graph (DAG) topologies—as a necessary, more efficient pathway to AGI.

**Methodology:** The authors develop a formal comparison between the optimization constraints of a single, scaled‑up model and those of an agentic architecture. Starting from simple routing schemes they analytically extend the framework to general DAG‑structured agent networks, deriving bounds that show exponential gains in sample efficiency and generalization for the agentic case. They also relate their results to mixture‑of‑experts models and critique existing multi‑agent implementations.

**Key findings:** The theoretical analysis demonstrates that Agentic AI can achieve exponentially better generalization and far lower data requirements than monolithic learners, making it a feasible route to AGI. The paper highlights the instability of current multi‑agent systems as a design flaw rather than a fundamental limitation, and calls for focused research on scalable, stable agentic architectures.


<details>
<summary>Abstract</summary>

Is monolithic scaling the only path to AGI? This paper challenges the dogma that purely scaling a single model is sufficient to achieve Artificial General Intelligence. Instead, we identify Agentic AI as a necessary paradigm for mastering the complex, heterogeneous distribution of real-world tasks. Through rigorous theoretical derivations, we contrast the optimization constraints of monolithic learners against the efficiency of Agentic systems, progressing from simple routing mechanisms to general Directed Acyclic Graph (DAG) topologies. We demonstrate that Agentic AI achieves exponentially superior generalization and sample efficiency. Finally, we discuss the connection to Mixture-of-Experts, reinterpret the instability of current multi-agent frameworks, and call for greater research focus on Agentic AI.

</details>


### 125. Reinforced Collaboration in Multi-Agent Flow Networks

- **Authors:** Zheng Wang, Yuang Liu, Yangkai Ding
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12943v1](http://arxiv.org/abs/2605.12943v1)
- **PDF:** [https://arxiv.org/pdf/2605.12943v1](https://arxiv.org/pdf/2605.12943v1)
- **Categories:** cs.LG


> The paper introduces **MANGO (Multi‑Agent Network Gradient Optimization)**, a data‑driven framework that builds a flow‑network representation of past successful multi‑agent LLM workflows and then jointly tunes both the collaboration topology and the individual agents. By combining reinforcement learning with gradient‑based textual updates—and a “skip” mechanism that avoids re‑optimizing already‑stable agents—MANGO learns more effective workflow paths while keeping computation low. Experiments on seven benchmarks show that this approach yields up to **12.8 % higher task performance**, a **47.4 % boost in efficiency**, and strong generalization to unseen domains, establishing a new state‑of‑the‑art for error‑robust, scalable agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent systems provide a powerful way to extend large language models (LLMs) by decomposing a complex task into specialized subtasks handled by different agents. However, their performance is often hindered by error propagation, arising from suboptimal workflow design or inaccurate agent outputs, which can propagate through the agent collaboration process and degrade final results. To address the challenges, we present MANGO (Multi-Agent Network Gradient Optimization), a data-driven framework that organizes and refines agent collaboration via a flow network constructed from past successful workflows. MANGO integrates reinforcement learning and textual gradients to jointly optimize workflow paths and agent behaviors, while a skipping mechanism prevents redundant updates to well-optimized agents for improving efficiency. Extensive experiments on seven benchmarks show that MANGO achieves up to 12.8% performance improvement over state-of-the-art baselines, enhances efficiency by 47.4%, and generalizes effectively to unseen domains. Our code and datasets are publicly available at https://github.com/openJiuwen-ai/agent-store/tree/main/community/mango.

</details>


### 126. Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue

- **Authors:** Vardhan Dongre, Dilek Hakkani-Tür
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12920v1](http://arxiv.org/abs/2605.12920v1)
- **PDF:** [https://arxiv.org/pdf/2605.12920v1](https://arxiv.org/pdf/2605.12920v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper introduces a dialogue‑enabled extension of the PARTNR household‑robot benchmark to study whether large‑language‑model (LLM) embodied agents can truly align their internal world models through communication. The authors propose quantitative metrics—observation convergence, information novelty, and belief‑sensitive messaging—that assess genuine world‑model alignment rather than mere surface coordination, and they evaluate three state‑of‑the‑art LLMs on collaborative tasks with partial observability. Results show that while dialogue dramatically cuts action conflicts (by 40–83 pp), it paradoxically lowers overall task success, revealing that current LLM agents achieve only shallow coordination and fall short of deep, belief‑aware world‑model alignment.


<details>
<summary>Abstract</summary>

Effective collaboration between embodied agents requires more than acting in a shared environment; it demands communication grounded in each agent's evolving understanding of the world. When agents can only partially observe their surroundings, coordination without communication is provably hard, but communication can, in principle, bridge this gap by allowing agents to share observations and align their world models. In this work, we examine whether LLM-based embodied agents actually realize the ability to communicate. We extend PARTNR, a benchmark for collaborative household robotics, with a natural-language dialogue channel that enables two agents with partial observability to communicate during task execution. To evaluate whether dialogue leads to genuine world-model alignment rather than superficial coordination, we propose a framework for measuring world-model alignment defined over per-agent world graphs: observation convergence (do private world models align over time?), information novelty (do messages convey what the partner lacks?), and belief-sensitive messaging (do agents model what their partner knows?). Our experiments across three LLMs reveal that dialogue reduces action conflicts 40 to 83 percentage points but degrades task success relative to silent coordination. Using our metrics, we characterize the gap between superficial coordination and genuine world-model alignment, and identify where current models fall on this spectrum.

</details>


### 127. Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents

- **Authors:** Harshita Chopra, Kshitish Ghate, Aylin Caliskan, Tadayoshi Kohno, Chirag Shah, Natasha Jaques
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12894v1](http://arxiv.org/abs/2605.12894v1)
- **PDF:** [https://arxiv.org/pdf/2605.12894v1](https://arxiv.org/pdf/2605.12894v1)
- **Categories:** cs.AI, cs.CL


> **Contribution:** The paper introduces **Persona Policies (PPol)**, a plug‑and‑play control layer that turns generic LLM user simulators into collections of realistic, behaviorally diverse personas while keeping the original task goals intact.

**Methodology:** Persona generation is framed as an LLM‑driven evolutionary program search: a Python generator is evolved with a multi‑objective fitness function that balances human‑likeness and coverage of varied human communication patterns. The optimized generator then samples many persona policies for any given task domain.

**Key Findings:** In retail and airline benchmark tasks, PPol‑conditioned simulators achieve 33–62 % higher human‑likeness fitness than baseline simulators, and annotators judge 80.4 % of their behavior as human‑like—close to real traces and twice the baseline rate. Training LLM agents with these diverse personas yields a 17 % relative improvement in task success on out‑of‑distribution user behaviors, demonstrating that PPol markedly enhances the robustness of simulated evaluation and training for agentic AI.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly deployed in settings where they interact with a wide variety of people, including users who are unclear, impatient, or reluctant to share information. However, collecting real interaction data at scale remains expensive. The field has turned to LLM-based user simulators as stand-ins, but these simulators inherit the behavior of their underlying models: cooperative and homogeneous. As a result, agents that appear strong in simulation often fail under the unseen, diverse communication patterns of real users. To narrow this gap, we introduce Persona Policies (PPol), a plug-and-play control layer that induces realistic behavioral variation in user simulators while preserving the original task goals. Rather than hand-crafting personas, we cast persona generation as an LLM-driven evolutionary program search that optimizes a Python generator to discover behaviors and translate them into task-preserving roleplay policies. Candidate generators are guided by a multi-objective fitness score combining human-likeness with broad coverage of human behavioral patterns. Once optimized, the generator produces a diverse population of human-like personas for any task in the domain. Across tau^2-bench retail and airline domains, evolved PPol programs yield 33-62% absolute gains in fitness score over the baseline simulator. In a blinded evaluation, annotators rated PPol-conditioned users as human 80.4% of the time, close to real human traces and nearly twice as frequently as baseline simulators. Agents trained with PPol are more robust to challenging, out-of-distribution behaviors, improving task success by +17% relative to training only on existing simulated interactions. This offers a novel approach to strengthen simulator-based evaluation and training without changing tasks or rewards.

</details>


### 128. EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents

- **Authors:** Hengwei Ye, Jiasheng Mao, Zhenhan Guan, Zheng Tian
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12887v1](http://arxiv.org/abs/2605.12887v1)
- **PDF:** [https://arxiv.org/pdf/2605.12887v1](https://arxiv.org/pdf/2605.12887v1)
- **Categories:** cs.IR, cs.AI


> **Contribution:** The paper introduces **EcoGEO**, a new paradigm that treats Generative Engine Optimization as an environment‑level problem for web‑enabled LLM search agents, and implements it with **TRACE**, a trajectory‑aware method that constructs a coordinated “evidence ecosystem” of interlinked pages to steer agents toward a desired product recommendation.

**Methodology:** TRACE receives a query and a fictional target product, then automatically generates a navigation entry page and a set of supporting pages that share terminology, link to one another, and present consistent product attributes. The ecosystem is designed to be traversed by an LLM‑based search agent, influencing its browsing trajectory (query reformulation, link‑following, and evidence synthesis) rather than merely boosting keyword density on a single page.

**Key Findings:** On the OPR‑Bench open‑ended product‑recommendation benchmark, TRACE consistently outperforms traditional page‑level GEO baselines, achieving higher target recommendation rates. Trajectory‑level analyses show more early crawls of the target page, more target‑focused follow‑up searches, and more internal‑link traversals, indicating that shaping the broader evidence environment—rather than adding isolated content—is an effective lever for controlling agentic LLM search behavior.


<details>
<summary>Abstract</summary>

Web-enabled LLM agents are changing how online information influences search outcomes. \ Existing Generative Engine Optimization (GEO) studies mainly focus on individual webpages. \ However, agentic web search is not a single-document setting: an agent may issue queries, crawl pages, follow links, reformulate searches, and synthesize evidence across multiple browsing steps. \ Influence therefore depends not only on page content, but also on how pages are organized, connected, and encountered along the agent's browsing trajectory. \ We study this shift through \textbf{Ecosystem Generative Engine Optimization} (\textbf{EcoGEO}), which treats GEO as an environment-level influence problem for web-enabled LLM agents. \ To instantiate this perspective, we propose \textbf{TRACE}, a \textbf{Trajectory-Aware Coordinated Evidence Ecosystem}. \ Given a recommendation query and a fictional target product, our method builds a controlled evidence environment that coordinates an agent-facing navigation entry page with heterogeneous support pages. \ These pages use shared terminology, internal links, and consistent product attributes to introduce, verify, and reinforce the target product. We evaluate our method on OPR-Bench, a benchmark for open-ended product recommendation. \ Experiments show that it consistently outperforms page-level GEO baselines in final target recommendation. \ Trajectory-level metrics further show increased initial target-result crawls, target-specific follow-up searches, and internal-link crawls, suggesting that the gains come from shaping the agent's evidence-acquisition process rather than merely adding more target-related content. \ Overall, our findings support an ecosystem research paradigm for GEO, where web-enabled LLM agents are studied in relation to the broader evidence environments that guide search, browsing, and answer synthesis.

</details>


### 129. ChipMATE: Multi-Agent Training via Reinforcement Learning for Enhanced RTL Generation

- **Authors:** Zhongkai Yu, Yichen Lin, Chenyang Zhou, Yuwei Zhang, Kun Zhou, Junxia Cui, Haotian Ye, Zhengding Hu, Zaifeng Pan, Ruiyi Wang, Yujie Zhao, Hejia Zhang, Jingbo Shang, Jishen Zhao, Yufei Ding
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12857v1](http://arxiv.org/abs/2605.12857v1)
- **PDF:** [https://arxiv.org/pdf/2605.12857v1](https://arxiv.org/pdf/2605.12857v1)
- **Categories:** cs.MA, cs.AI, cs.AR, cs.LG


> ChipMATE introduces the first self‑trained, multi‑agent system for RTL generation that eliminates the need for a golden testbench and works within air‑gapped vendor environments. The framework pairs a Verilog‑producing agent with a Python reference‑model agent that continuously cross‑verify each other’s outputs, using a back‑track inference mechanism and a two‑stage training pipeline (individual pre‑training followed by joint collaboration) built on a 64.4 K‑sample hybrid data generator. Evaluated on VerilogEval V2, ChipMATE reaches 75.0 % and 80.1 % pass@1 with 4 B and 9 B base models, surpassing all prior self‑trained approaches and even larger commercial models.


<details>
<summary>Abstract</summary>

Existing API-based agentic systems for RTL code generation are fundamentally misaligned with industrial practice: they assume a golden testbench is available at generation time, rely on closed-source APIs incompatible with chip vendors' air-gapped security requirements, and cannot be trained on vendors' proprietary RTL codebases, leaving valuable internal data unused. Recent self-trained models address the deployment constraint but remain single-turn generators that overlook the critical role of verification in real industrial flows.
  To bridge these gaps, we present ChipMATE, the first self-trained multi-agent framework for RTL generation. Inspired by industrial practice where correctness emerges from cross-comparison between independently written RTL modules and reference models, ChipMATE pairs a Verilog agent with a Python reference-model agent that mutually verify each other's outputs without any golden oracle. We design a backtrack-based inference workflow to prevent error propagation across turns, and a two-stage training pipeline that first trains each agent individually to saturate its code-generation capability, then trains the team jointly to collaborate effectively. To support the training, we further build a hybrid data-generation framework that produces 64.4K high-quality reference model training samples. ChipMATE achieves 75.0\% and 80.1\% pass@1 on VerilogEval V2 with 4B and 9B base models, outperforming all existing self-trained models and even DeepSeek V4 with 1600B parameters. Our code and model weights are publicly available in https://github.com/zhongkaiyu/ChipMATE.

</details>


### 130. Moltbook Moderation: Uncovering Hidden Intent Through Multi-Turn Dialogue

- **Authors:** Ali Al-Lawati, Nafis Tripto, Abolfazl Ansari, Jason Lucas, Suhang Wang, Dongwon Lee
- **Published:** 2026-05-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12856v2](http://arxiv.org/abs/2605.12856v2)
- **PDF:** [https://arxiv.org/pdf/2605.12856v2](https://arxiv.org/pdf/2605.12856v2)
- **Categories:** cs.AI, cs.SI


> The paper introduces **BOT‑MOD**, a moderation framework that shifts the detection focus from static content analysis to the **intent** of interacting agents in multi‑agent environments. BOT‑MOD engages a suspect agent in a *multi‑turn dialogue* and uses Gibbs‑sampling over a set of candidate intents to iteratively prune unlikely hypotheses, thereby inferring the agent’s underlying objective. Evaluated on a newly built Moltbook dataset containing realistic benign and malicious interaction patterns, BOT‑MOD accurately uncovers malicious intent across diverse adversarial setups while keeping false positives low, demonstrating a scalable, intent‑aware approach for moderating agents in open, multi‑turn dialogue systems.


<details>
<summary>Abstract</summary>

The emergence of multi-agent systems introduces novel moderation challenges that extend beyond content filtering. Agents with malicious intent may contribute harmful content that appears benign to evade content-based moderation, while compromising the system through exploitative and malicious behavior manifested across their overall interaction patterns within the community. To address this, we introduce BOT-MOD (BOT-MODeration), a moderation framework that grounds detection in agent intent rather than traditional content level signals. BOT-MOD identifies the underlying intent by engaging with the target agent in a multi-turn exchange guided by Gibbs-based sampling over candidate intent hypotheses. This progressively narrows the space of plausible agent objectives to identify the underlying behavior. To evaluate our approach, we construct a dataset derived from Moltbook that encompasses diverse benign and malicious behaviors based on actual community structures, posts, and comments. Results demonstrate that BOT-MOD reliably identifies agent intent across a range of adversarial configurations, while maintaining a low false positive rate on benign behaviors. This work advances the foundation for scalable, intent-aware moderation of agents in open multi-agent environments.

</details>


### 131. Neurodata Without Boredom: Benchmarking Agentic AI for Data Reuse

- **Authors:** Ling-Qi Zhang, Kristin Branson
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12808v2](http://arxiv.org/abs/2605.12808v2)
- **PDF:** [https://arxiv.org/pdf/2605.12808v2](https://arxiv.org/pdf/2605.12808v2)
- **Categories:** cs.LG


> The paper introduces **Neurodata Without Boredom**, a benchmark that evaluates how well current agentic AI (LLM‑driven coding assistants) can automate the reuse of fragmented neuroscience datasets. The authors assembled eight recent mouse‑neural‑population studies that differ in recording modality, behavioral task, and data format (NWB, custom APIs, plain Python/MATLAB files); for each they gave an agent the published paper, code, and raw data and asked it to load the data, interpret the experimental variables, and reformat everything into a common decoder‑training pipeline. Results show that general‑purpose coding agents can solve many of the individual sub‑tasks, but they rarely produce a completely correct end‑to‑end workflow, frequently err on format‑specific quirks and mis‑interpret documentation; moreover, agents acting as self‑checkers fail to reliably detect these errors without external ground‑truth, confirming that human‑in‑the‑loop oversight remains essential. The study therefore contributes a realistic, task‑oriented benchmark, characterizes systematic failure modes of agentic AI in scientific data integration, and offers concrete data‑sharing guidelines for the emerging “agentic‑AI era” of neuroscience.


<details>
<summary>Abstract</summary>

Neuroscience data are highly fragmented across labs, formats, and experimental paradigms, and reuse often requires substantial manual effort. A persistent roadblock to data reuse and integration is the need to decipher bespoke and diverse data formatting choices. Common data formats have been proposed in response, but the field continues to struggle with a fundamental tension: formats flexible enough to accommodate diverse experiments are rarely descriptive enough to be self-explanatory, and sufficiently descriptive formats demand detailed documentation and curation effort that few labs can sustain. Agentic AI is a natural candidate to solve this problem: LLMs read code and text faster and with sustained attention to the low-level details humans tend to skim over. To measure how well agentic AI performs on this task, we selected eight recent papers studying large-scale mouse neural population recordings that shared both data and code, spanning diverse recording modalities, behavioral paradigms, and dataset formats (e.g., NWB, specialized APIs, and general-purpose Python or MATLAB files). We provided agents with the data, code, and paper, and prompted them to load, understand, and reformat the data for a common downstream task: training a decoder from neural activity to task or behavioral variables. General-purpose coding agents commonly used by scientists performed well on each sub-task, but rarely strung together a fully error-free end-to-end solution. We characterize the types of mistakes agents made and the dataset properties that elicited them, and propose data-sharing best practices for the agentic-AI era. We further find that agents-as-judges are unreliable at catching errors, especially without ground-truth references, so interactive, human-in-the-loop coding remains necessary.

</details>


### 132. Synthesizing the Expert: A Validated Multimodal Dataset for Trustworthy AI-Assisted Swimming Coaching

- **Authors:** Ahmad Al-Kabbany, Esraa Kassem
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12799v1](http://arxiv.org/abs/2605.12799v1)
- **PDF:** [https://arxiv.org/pdf/2605.12799v1](https://arxiv.org/pdf/2605.12799v1)
- **Categories:** cs.MA, cs.CY, cs.MM


> The paper introduces a multi‑agent Retrieval‑Augmented Generation (RAG) framework that automatically constructs a high‑quality, multimodal “Question‑Context‑Answer” dataset for AI‑assisted swimming coaching, overcoming the scarcity of ethically sourced, expert‑labeled aquatic data. By integrating physiological measurements, scientific literature, kinematic sensor streams, and unstructured expert knowledge, the system generates 1,864 validated triplets—each screened against 12 physiological sound‑ness rules—thereby providing a trustworthy synthetic benchmark for grounding LLM‑driven coaching advice. Experiments demonstrate that this synthetic benchmark enables more reliable, expert‑aligned coaching outputs and establishes a reproducible baseline for future meta‑agent and trustworthy AI research in sports science.


<details>
<summary>Abstract</summary>

This research is primarily concerned with the critical problem of synthesizing a structured Retrieval-Augmented Generation (RAG) system for advanced AI applications in the domain of swimming. As the integration of Artificial Intelligence in sports science matures, its applications in swimming have become increasingly diverse, spanning from real-time technical coaching and talent scouting to comprehensive performance profiling and the dynamic personalization of training periodization. Within this landscape, RAG-based systems represent a pivotal advancement in Large Language Model (LLM) enhanced swimming analysis, as they allow for the grounding of generative outputs in authoritative domain knowledge, thereby ensuring the credibility of AI-generated advice, contextually and technically. Despite this potential, building robust RAG systems using only real-world aquatic data presents significant challenges, including ethical constraints regarding athlete biometrics, and the high cost of manual expert labeling. To address these barriers, we propose a novel generative framework that leverages a multimodal knowledge base gathered across four dimensions: physiological data, physiological literature, kinematic sensor data, and unstructured domain expertise. Our proposed framework utilizes a multi-agent LLM architecture to synthesize a high-fidelity dataset of 1,864 validated "Question-Context-Answer" triplets-drawn from 1,914 drafts evaluated against 12 physiological soundness rules. By providing a structured, synthetic ground truth, this work establishes a foundational benchmark for trustworthy AI in aquatics. The outcomes of this research promise to enhance the reliability of automated coaching and open a plethora of future directions in "Meta-Agent" development and athletic profiling, ultimately bridging the gap between raw data engineering and practical sports science application.

</details>


### 133. CHAL: Council of Hierarchical Agentic Language

- **Authors:** Tommaso Giovannelli, Griffin D. Kent
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12718v1](http://arxiv.org/abs/2605.12718v1)
- **PDF:** [https://arxiv.org/pdf/2605.12718v1](https://arxiv.org/pdf/2605.12718v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces **CHAL (Council of Hierarchical Agentic Language)**, the first multi‑agent debate framework that casts dialectic interaction as a **structured belief‑optimization problem** for defeasible domains rather than as a simple ground‑truth voting scheme. Each participant holds a **graph‑based CHAL Belief Schema (CBS)** whose thesis is treated as a differentiable objective; agents revise their CBSs via gradient‑informed updates while a configurable adjudicator’s meta‑cognitive value system (epistemic, logical, ethical) steers the overall trajectory in latent belief space. Experiments show that (i) the adjudicator’s value hyperparameters decisively shape debate dynamics, (ii) greater council diversity systematically improves belief convergence for all agents, and (iii) the approach scales across diverse fields, producing auditable belief artifacts that enable transparent evaluation and alignment of agentic AI reasoning.


<details>
<summary>Abstract</summary>

Multi-agent debate has emerged as a promising approach for improving LLM reasoning on ground-truth tasks, yet current methodologies face certain structural limitations: debate tends to induce a martingale over belief trajectories, majority voting accounts for most observed gains, and LLMs exhibit confidence escalation rather than calibration across rounds. We argue that the genuine value of debate, and dialectic systems as a whole, lies not in ground-truth tasks but in defeasible domains, where every position can in principle be defeated by better reasoning. We present the Council of Hierarchical Agentic Language (CHAL), a multi-agent dialectic framework that treats defeasible argumentation as an engine for belief optimization. Each agent maintains a CHAL Belief Schema (CBS), a graph-structured belief representation with a Bayesian-inspired architecture, that facilitates belief revision through a gradient-informed dynamic mechanism by leveraging the strength of the belief's thesis as a differentiable objective. Meta-cognitive value systems spanning epistemology, logic, and ethics are elevated to configurable hyperparameters governing agent reasoning and adjudication outcomes. We provide a series of ablation experiments that demonstrate systematic and interpretable effects: the adjudicator's value system determines the debate's overall trajectories in latent belief space, council diversity refines beliefs for all participants, and the framework generalizes across broad fields. CHAL is, to our knowledge, the first framework to treat multi-agent debate as structured belief optimization over defeasible domains. Further, the auditable belief artifacts it produces establish the foundation for dedicated evaluation suites for defeasible argumentation, with broader implications for building AI systems whose reasoning and value commitments are transparent, aligned, and subject to human oversight.

</details>


### 134. Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack

- **Authors:** Hao Wang, Hanchen Li, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12673v1](http://arxiv.org/abs/2605.12673v1)
- **PDF:** [https://arxiv.org/pdf/2605.12673v1](https://arxiv.org/pdf/2605.12673v1)
- **Categories:** cs.AI, cs.CR


> The paper introduces **BenchJack**, an automated red‑teaming framework that uses coding agents to probe agent‑oriented benchmarks for reward‑hacking vulnerabilities. By encoding a taxonomy of eight common design flaws (the Agent‑Eval Checklist) and running a generative‑adversarial loop that iteratively discovers exploits and patches them, BenchJack was able to generate near‑perfect scores on 10 widely used benchmarks (e.g., WebArena, OSWorld) without solving any tasks, surfacing 219 distinct flaws; the iterative pipeline then reduced the proportion of hackable tasks from ~100 % to <10 % on four benchmarks and fully secured two of them in three cycles. The work demonstrates that current evaluation suites lack adversarial robustness and that systematic, agent‑driven auditing can dramatically harden benchmark design for frontier, agentic AI systems.


<details>
<summary>Abstract</summary>

Agent benchmarks have become the de facto measure of frontier AI competence, guiding model selection, investment, and deployment. However, reward hacking, where agents maximize a score without performing the intended task, emerges spontaneously in frontier models without overfitting. We argue that benchmarks must be secure by design. From past incidents of reward hacks, we derive a taxonomy of eight recurring flaw patterns and compile them into the Agent-Eval Checklist for benchmark designers. We condense the insights into BenchJack, an automated red-teaming system that drives coding agents to audit benchmarks and identify possible reward-hacking exploits in a clairvoyant manner. Moreover, we extend BenchJack to an iterative generative-adversarial pipeline that discovers new flaws and patches them iteratively to improve benchmark robustness. We apply BenchJack to 10 popular agent benchmarks spanning software engineering, web navigation, desktop computing, and terminal operations. BenchJack synthesizes reward-hacking exploits that achieve near-perfect scores on most of the benchmarks without solving a single task, surfacing 219 distinct flaws across the eight classes. Moreover, BenchJack's extended pipeline reduces the hackable-task ratio from near 100% to under 10% on four benchmarks without fatal design flaws, fully patching WebArena and OSWorld within three iterations. Our results show that evaluation pipelines have not internalized an adversarial mindset, and that proactive auditing could help close the security gap for the fast-paced benchmarking space.

</details>


### 135. scShapeBench: Discovering geometry from high dimensional scRNAseq data

- **Authors:** Andrew J Steindl, João Felipe Rocha, Brian Tshilengi Di Bassinga, Zachary Warren, Matthew Scicluna, César Miguel Valdez Córdova, Shabarni Gupta, Leire Torices, Daniel Neumann, Timothy J. Mann, Ihuan Gunawan, Dhananjay Bhaskar, John G Lock, Christine L Chaffer, Guy Wolf, Smita Krishnaswamy
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12662v1](http://arxiv.org/abs/2605.12662v1)
- **PDF:** [https://arxiv.org/pdf/2605.12662v1](https://arxiv.org/pdf/2605.12662v1)
- **Categories:** cs.LG, q-bio.GN


> The paper presents **scShapeBench**, a new benchmark suite for automatically detecting the underlying geometric/topological shape of high‑dimensional single‑cell RNA‑seq datasets—a prerequisite for choosing appropriate downstream analysis pipelines in agentic‑AI‑driven bioinformatics. The authors construct synthetic point clouds from known skeleton graphs and curate expert‑annotated real datasets labeled as clustered, single‑trajectory, multi‑branching, or archetypal, and introduce topology‑aware evaluation metrics. As a baseline, they propose **scReebTower**, which leverages diffusion‑based geometry to build Reeb graphs; experiments show that scReebTower consistently outperforms existing methods such as PAGA and Mapper on both synthetic and real data, demonstrating its utility for automated shape detection in agentic AI scientific workflows.


<details>
<summary>Abstract</summary>

High-dimensional point cloud data arise across many scientific domains, especially single-cell biology. The shapes or topologies of these datasets determine the types of information that can be extracted. For example, clustered data supports cell-type identification, trajectory structures support transition analysis, and archetypal structures capture continua of cellular behaviors. Existing analysis pipelines often assume a specific shape. The standard Seurat pipeline combines UMAP visualization with Louvain clustering and therefore assumes clustered data, while tools such as Monocle and SPADE assume tree-like structures, and flow-based models such as MIOFlow and Conditional Flow Matching target trajectories. Choosing which pipeline to apply is therefore often left to bioinformaticians who visually inspect datasets before selecting an analysis strategy. With the rise of agentic AI scientists, automating shape detection is increasingly important for selecting downstream analysis pipelines. To address this problem, we introduce scShapeBench, a benchmark dataset for shape detection containing both synthetic and expert-annotated single-cell datasets. Synthetic datasets are sampled from ground-truth skeleton graphs with controlled variance. Real single-cell datasets are curated from diverse sources and annotated by experts into four categories: clusters, single trajectory, multi-branching, and archetypal. We additionally introduce scReebTower, a baseline method that uses diffusion geometry to extract Reeb graphs and connect visualization with pipeline selection. We provide topology-aware evaluation metrics and compare scReebTower against PAGA and Mapper on synthetic and real data. Our results indicate that scReebTower outperforms existing baselines. Overall, our contributions span benchmarks, evaluation metrics, and a baseline for automated shape detection in single-cell data.

</details>


### 136. Macro-Action Based Multi-Agent Instruction Following through Value Cancellation

- **Authors:** Wo Wei Lin, Ethan Rathbun, Enrico Marchesini Xiang Zhi Tan
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12655v1](http://arxiv.org/abs/2605.12655v1)
- **PDF:** [https://arxiv.org/pdf/2605.12655v1](https://arxiv.org/pdf/2605.12655v1)
- **Categories:** cs.AI, cs.MA


> **Paper Summary**

The authors identify a fundamental failure mode in multi‑agent RL when natural‑language instructions interrupt ongoing macro‑actions: standard Bellman backups conflate value estimates across instruction contexts, causing inconsistent “instruction‑aware” Q‑values. To fix this, they introduce **Macro‑Action Value Correction for Instruction Compliance (MAVIC)**, which explicitly adjusts the bootstrapped target at each instruction boundary by (1) subtracting the value of the now‑obsolete instruction objective and (2) adding back the continuation value under the current objective.  

Implemented as a lightweight modification to an actor‑critic MARL algorithm, MAVIC enables a single unified policy to handle stochastic instruction switches without reward shaping. Experiments in increasingly complex cooperative environments show that MAVIC dramatically improves instruction‑following compliance while retaining baseline task performance, confirming its effectiveness for agentic AI systems that must seamlessly incorporate external language directives.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) in real-world use cases may need to adapt to external natural language instructions that interrupt ongoing behavior and conflict with long-horizon objectives. However, conditioning rewards on instructions introduces a fundamental failure mode as Bellman updates couple value estimates across instruction contexts, leading to inconsistent values when instructions interrupt macro-actions. We propose Macro-Action Value Correction for Instruction Compliance (MAVIC), which corrects Bellman backups at instruction boundaries by correcting the incoming instruction objective and restoring the continuation value under the current objective. Unlike reward shaping, MAVIC modifies the bootstrapping target itself, enabling consistent value estimation under stochastic instruction switching within a unified policy. We provide theoretical analysis and an actor-critic implementation, and show that MAVIC achieves high instruction compliance while preserving base task performance in increasingly complex cooperative multi-agent environments.

</details>


### 137. Multi-Rollout On-Policy Distillation via Peer Successes and Failures

- **Authors:** Weichen Yu, Xiaomin Li, Yizhou Zhao, Xiaoze Liu, Ruowang Zhang, Haixin Wang, Yinyi Luo, Chen Henry Wu, Gaurav Mittal, Matt Fredrikson, Yu Hu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12652v1](http://arxiv.org/abs/2605.12652v1)
- **PDF:** [https://arxiv.org/pdf/2605.12652v1](https://arxiv.org/pdf/2605.12652v1)
- **Categories:** cs.LG, cs.AI


> **Paper Summary**

The authors propose **Multi‑Rollout On‑Policy Distillation (MOPD)**, a novel peer‑conditioned distillation scheme that leverages the whole set of student‑generated rollouts for a given prompt rather than treating each trajectory in isolation. MOPD constructs teacher signals by conditioning on both successful and failed peer rollouts—positive peer imitation reinforces correct reasoning patterns, while contrastive success‑failure conditioning supplies structured negative evidence about plausible mistakes. Across competitive‑programming, math, scientific QA, and tool‑use benchmarks, MOPD yields consistent performance gains over standard on‑policy distillation, and analysis shows that the mixed success‑failure contexts produce teacher scores that better correlate with verifier rewards, demonstrating more faithful, instance‑adaptive supervision for agentic LLMs.


<details>
<summary>Abstract</summary>

Large language models are often post-trained with sparse verifier rewards, which indicate whether a sampled trajectory succeeds but provide limited guidance about where reasoning succeeds or fails. On-policy distillation (OPD) offers denser token-level supervision by training on student-generated trajectories, yet existing methods typically distill each rollout independently and ignore the other attempts sampled for the same prompt. We introduce Multi-Rollout On-Policy Distillation (MOPD), a peer-conditioned distillation framework that uses the student's local rollout group to construct more informative teacher signals. MOPD conditions the teacher on both successful and failed peer rollouts: successes provide positive evidence for valid reasoning patterns, while failures provide structured negative evidence about plausible mistakes to avoid. We study two peer-context constructions: positive peer imitation and contrastive success-failure conditioning. Experiments on competitive programming, mathematical reasoning, scientific question answering, and tool-use benchmarks show that MOPD consistently improves over standard on-policy baselines. Further teacher-signal analysis shows that mixed success-failure contexts better align teacher scores with verifier rewards, indicating that the gains arise from more faithful, instance-adaptive supervision. These results indicate that effective on-policy distillation should exploit the student's multi-rollout trial-and-error behavior rather than treating rollouts as isolated samples.

</details>


### 138. KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference

- **Authors:** Alireza Nadali, Patrick Cooper, Ashutosh Trivedi, Alvaro Velasquez
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12471v1](http://arxiv.org/abs/2605.12471v1)
- **PDF:** [https://arxiv.org/pdf/2605.12471v1](https://arxiv.org/pdf/2605.12471v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> **Main contribution** – The paper presents **KV‑Fold**, a training‑free technique that turns a transformer’s key‑value cache into a recurrent “fold” accumulator, enabling inference over very long token sequences (up to 128 K tokens) without modifying the model architecture or parameters.  

**Methodology** – KV‑Fold processes the input in fixed‑size chunks; after each chunk the newly generated keys and values are concatenated to the existing KV‑cache, which is then fed back as the prefix for the next forward pass. This one‑step update is repeated like a left‑fold in functional programming, reusing the same frozen pretrained transformer and the cache‑concatenation primitive originally used for latent multi‑agent communication.  

**Key findings** – The induced recurrence is numerically stable (drift quickly plateaus) across model families, chunk sizes, and even 10 000‑fold changes in precision. On a needle‑in‑a‑haystack benchmark, KV‑Fold achieves **100 % exact‑match retrieval** for contexts from 16 K to 128 K tokens and chain depths up to 511 on Llama‑3.1‑8B, while fitting within a single 40 GB GPU. Thus, frozen transformers already possess a robust KV‑cache recurrence that provides practical, high‑fidelity long‑context inference for agentic AI systems without any retraining or architectural changes.


<details>
<summary>Abstract</summary>

We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks. At each step, the model processes the next chunk conditioned on the accumulated cache, appends the newly produced keys and values, and passes the enlarged cache forward; the same one-step update is applied repeatedly, analogous to foldl in functional programming. Building on the KV cache concatenation primitive introduced for latent multi-agent communication, we repurpose it as a chunk-to-chunk recurrence for long-context inference. When processing chunk t, the model attends to the KV cache carried from earlier chunks as a prefix, reusing its internal state across segments without modifying or retraining the model. Despite its simplicity, the induced recurrence is stable: per-step drift rises briefly and then saturates into a flat plateau that persists across deep chains. This plateau is insensitive to a 10,000x change in numerical precision, robust across chunk sizes, and consistent across model families. At the task level, KV-Fold preserves exact information over long distances. On a needle-in-a-haystack benchmark, it achieves 100% exact-match retrieval across 152 trials spanning contexts from 16K to 128K tokens and chain depths up to 511 on Llama-3.1-8B, while remaining within the memory limits of a single 40GB GPU. Compared to streaming methods, which trade fidelity for bounded memory, KV-Fold maintains long-range retrieval while operating as a sequence of tractable forward passes. Overall, our results show that frozen pretrained transformers already support a stable form of KV-cache recurrence, providing a practical route to long-context inference without architectural changes or training.

</details>


### 139. Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs

- **Authors:** Guinan Su, Yanwu Yang, Xueyan Li, Jonas Geiping
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12460v1](http://arxiv.org/abs/2605.12460v1)
- **PDF:** [https://arxiv.org/pdf/2605.12460v1](https://arxiv.org/pdf/2605.12460v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces **Multi‑Stream LLMs**, a new paradigm that replaces the traditional single‑stream chat format with several parallel streams for reading, thinking, and acting, and trains models via instruction‑tuning to consume and produce tokens simultaneously across these streams. By restructuring the forward pass so that each timestep reads from multiple input streams and writes to multiple output streams, the authors achieve true concurrent “reading‑while‑writing” and “thinking‑while‑acting” behavior, which eliminates the sequential bottleneck of existing autonomous agents. Experiments show that this parallel‑stream architecture yields higher throughput, more modular and secure agent designs, and easier monitoring of internal reasoning, thereby advancing the efficiency and controllability of agentic AI systems.


<details>
<summary>Abstract</summary>

The continued improvements in language model capability have unlocked their widespread use as drivers of autonomous agents, for example in coding or computer use applications. However, the core of these systems has not changed much since early instruction-tuned models like ChatGPT. Even advanced AI agents function on message exchange formats, successively exchanging messages with users, systems, with itself (i.e. chain-of-thought) and tools in a single stream of computation. This bottleneck to a single stream in chat models leads to a number of limitations: the agent cannot act (generate output) while reading, and in reverse, cannot react to new information while writing. Similarly, the agent cannot act while thinking and cannot think while reading or acting on information.
  In this work, we show that models can be unblocked by switching from instruction-tuning for sequential message formats to instruction-tuning for multiple, parallel streams of computation, splitting each role into a separate stream. Every forward pass of the language model then simultaneously reads from multiple input streams and generates tokens in multiple output streams, all of which causally depend on earlier timesteps. We argue that this data-driven change remedies a number of usability limitations as outlined above, improves model efficiency through parallelization, improves model security through better separation of concerns and can further improve model monitorability.

</details>


### 140. Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling

- **Authors:** Eilam Shapira, Moshe Tennenholtz, Roi Reichart
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12411v1](http://arxiv.org/abs/2605.12411v1)
- **PDF:** [https://arxiv.org/pdf/2605.12411v1](https://arxiv.org/pdf/2605.12411v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.MA


> The paper introduces a target‑adaptive “text‑tabular” framework for forecasting the next move of an unfamiliar LLM‑driven negotiation agent using only a handful of prior interactions. By representing each decision point as a hybrid row of structured game features and LLM‑encoded dialogue (the “Observer” LLM reads the context and contributes its hidden states as additional features), the model can be fine‑tuned on a small set of labeled examples per target agent and then applied to new agents. Experiments on simulated bargaining and procurement games show that this approach outperforms direct few‑shot prompting and pure text or tabular baselines, achieving a 4‑point AUC lift and a 14 % reduction in offer‑prediction error with as few as 16 adaptation examples, demonstrating that hidden LLM representations carry decision‑relevant signals that are missed by standard prompting.


<details>
<summary>Abstract</summary>

AI agents negotiate and transact in natural language with unfamiliar counterparts: a buyer bot facing an unknown seller, or a procurement assistant negotiating with a supplier. In such interactions, the counterpart's LLM, prompts, control logic, and rule-based fallbacks are hidden, while each decision can have monetary consequences. We ask whether an agent can predict an unfamiliar counterpart's next decision from a few interactions. To avoid real-world logging confounds, we study this problem in controlled bargaining and negotiation games, formulating it as target-adaptive text-tabular prediction: each decision point is a table row combining structured game state, offer history, and dialogue, while $K$ previous games of the same target agent, i.e., the counterpart being modeled, are provided in the prompt as labeled adaptation examples. Our model is built on a tabular foundation model that represents rows using game-state features and LLM-based text representations, and adds LLM-as-Observer as an additional representation: a small frozen LLM reads the decision-time state and dialogue; its answer is discarded, and its hidden state becomes a decision-oriented feature, making the LLM an encoder rather than a direct few-shot predictor. Training on 13 frontier-LLM agents and testing on 91 held-out scaffolded agents, the full model outperforms direct LLM-as-Predictor prompting and game+text features baselines. Within this tabular model, Observer features contribute beyond the other feature schemes: at $K=16$, they improve response-prediction AUC by about 4 points across both tasks and reduce bargaining offer-prediction error by 14%. These results show that formulating counterpart prediction as a target-adaptive text-tabular task enables effective adaptation, and that hidden LLM representations expose decision-relevant signals that direct prompting does not surface.

</details>


### 141. Ready from Day 1: Population-Aware Coordination for Large-Scale Constrained Multi-Agent Systems

- **Authors:** Angel Wang, Dominique Perrault-Joncas, Alvaro Maggiar, Carson Eisenach, Dean Foster
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.13900v1](http://arxiv.org/abs/2605.13900v1)
- **PDF:** [https://arxiv.org/pdf/2605.13900v1](https://arxiv.org/pdf/2605.13900v1)
- **Categories:** cs.MA, cs.LG


> **Contribution:** The paper introduces *population‑aware coordination interfaces*—learned primal and dual models that map compact summaries of a multi‑agent population to, respectively, the aggregate resource utilization response to a cost signal and the cost signal needed to achieve a target utilization. By conditioning on population structure, these interfaces remain accurate across planning cycles even as the agent composition shifts, eliminating the need for per‑cycle retraining and enabling scalable coordination from small samples.

**Methodology:** The authors embed the learned primal and dual maps into the upstream planner’s iterative Lagrangian‑relaxation loop. Population summaries (e.g., histograms of agent types) are fed to neural networks that are trained offline on simulated data; a Sim2Real back‑testing protocol is used to validate transferability before deployment. Experiments are conducted on a large‑scale supply‑chain capacity‑control problem.

**Key Findings:** Compared with population‑agnostic baselines, the population‑aware interfaces lower forecast error by 16–19 % and reduce capacity‑violation rates by 20–51 % under significant composition shifts. They scale from 20 K simulated agents to accurately coordinate 500 K real agents, and simulator‑trained primal maps achieve 11.1 % MAPE on real‑world observations versus 13–24 % for existing methods. These results demonstrate that encoding population information is crucial for reliable, large‑scale constrained multi‑agent coordination.


<details>
<summary>Abstract</summary>

In large-scale multi-agent systems with shared resource constraints, an upstream planner must iteratively evaluate candidate resource plans -- assessing feasibility, aggregate response, and marginal cost -- before committing to one. Lagrangian relaxation separates local decisions through a broadcast cost signal, but the planner still needs the cost-to-utilization response map to explore plan space, and this map depends on population composition that changes across planning cycles. We propose \emph{population-aware coordination interfaces}: learned primal and dual maps, conditioned on compact population summaries, that the planner queries inside its iterative loop. The primal map predicts aggregate utilization under a proposed cost trajectory; the dual map predicts the cost trajectory for a target plan. By encoding response-relevant population structure, these maps remain reliable across evolving populations without per-cycle retraining, and support coordination of large populations from compact subsamples. We additionally cast Sim2Real transfer as a backtestable procedure, enabling evaluation before deployment. In a supply-chain capacity-control case study, population-aware interfaces reduce forecast error by 16--19\% and capacity violations by 20--51\% relative to population-unaware baselines under composition shift; 20K-agent cohorts support accurate coordination of 500K-agent populations; and simulator-trained primal maps achieve 11.1\% MAPE on real observations versus 13--24\% for baselines.

</details>


### 142. Events as Triggers for Behavioral Diversity in Multi-Agent Reinforcement Learning

- **Authors:** Hannes Büchi, Manon Flageat, Eduardo Sebastián, Amanda Prorok
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12388v2](http://arxiv.org/abs/2605.12388v2)
- **PDF:** [https://arxiv.org/pdf/2605.12388v2](https://arxiv.org/pdf/2605.12388v2)
- **Categories:** cs.MA, cs.LG


> **Main contribution:** The paper proposes an event‑driven framework that separates an agent’s identity from its behavior, allowing any team member to switch roles instantaneously when a task‑relevant “event” occurs. It introduces (1) **Neural Manifold Diversity (NMD)**, a metric that quantifies behavioral diversity on a continuous manifold even for transient, agent‑agnostic policies, and (2) an **event‑conditioned hypernetwork** that produces Low‑Rank Adaptation (LoRA) modules to re‑parameterise a shared team policy on‑the‑fly.

**Methodology:** A shared base policy is trained jointly with the hypernetwork; when an event is detected, the hypernetwork generates a LoRA‑style weight‑delta that maps the base policy to a new point on the behavior manifold defined by NMD. The authors prove that this construction preserves optimality of reward maximisation while guaranteeing diverse behaviours, and they evaluate the system on several MARL benchmarks requiring role re‑assignment.

**Key findings:** Across all tested environments, the event‑triggered hypernetwork with NMD outperforms prior MARL baselines, achieves zero‑shot generalisation to unseen event sequences, and uniquely solves tasks that demand sequential, context‑specific behavior reassignment—demonstrating that event‑driven policy reconfiguration is an effective mechanism for behavioural diversity in agentic AI.


<details>
<summary>Abstract</summary>

Effective multi-agent cooperation requires agents to adopt diverse behaviors as task conditions evolve-and to do so at the right moment. Yet, current Multi-Agent Reinforcement Learning (MARL) frameworks that facilitate this diversity are still limited by the fact that they bind fixed behaviors to fixed agent identities. Consequently, they are ill-equipped for tasks where agents need to take on different roles at very specific moments in time. We argue that, to define these behavioral transitions, the missing ingredient is $\textbf{events}$. Events are changes in the state of the system that induce qualitative changes in the task. Based on this view, we introduce a framework that decouples agent identity from behavior, capturing a continuous manifold from which agents instantiate their behaviors in response to events. This framework is based on two elements. First, to build an expressive behavior manifold, we introduce Neural Manifold Diversity (NMD), a formal distance metric that remains well-defined when behaviors are transient and agent-agnostic. Second, we use an event-based hypernetwork that generates Low-Rank Adaptation (LoRA) modules over a shared team policy, enabling on-the-fly agent-policy reconfiguration in response to events. We prove that this construction ensures that diversity does not interfere with reward maximization by design. Empirical results demonstrate that our framework outperforms established baselines across benchmarks while exhibiting zero-shot generalization, and being the only method that solves tasks requiring sequential behavior reassignment.

</details>


### 143. ProfiliTable: Profiling-Driven Tabular Data Processing via Agentic Workflows

- **Authors:** Wei Liu, Yang Gu, Xi Yan, Zihan Nan, Beicheng Xu, Keyao Ding, Bin Cui, Wentao Zhang
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12376v1](http://arxiv.org/abs/2605.12376v1)
- **PDF:** [https://arxiv.org/pdf/2605.12376v1](https://arxiv.org/pdf/2605.12376v1)
- **Categories:** cs.AI


> ProfiliTable introduces an autonomous, multi‑agent pipeline that uses dynamic data profiling to turn vague user requests into correct, governance‑compliant table‑processing code. The system couples a ReAct‑style Profiler (which interactively explores the dataset to build a semantic context), a Generator that retrieves and assembles curated operators into task‑aware scripts, and an Evaluator‑Summarizer loop that feeds execution scores and diagnostics back for iterative refinement. Across 18 tabular task types, this closed‑loop, profiling‑driven approach significantly outperforms existing LLM‑based baselines, especially on complex multi‑step transformations, demonstrating the practical value of structured profiling feedback for reliable agentic AI in data engineering.


<details>
<summary>Abstract</summary>

Table processing-including cleaning, transformation, augmentation, and matching-is a foundational yet error-prone stage in real-world data pipelines. While recent LLM-based approaches show promise for automating such tasks, they often struggle in practice due to ambiguous instructions, complex task structures, and the lack of structured feedback, resulting in syntactically correct but semantically flawed code. To address these challenges, we propose ProfiliTable, an autonomous multi-agent framework centered on dynamic profiling, which constructs and iteratively refines a unified execution context through interactive exploration, knowledge-augmented synthesis, and feedback-driven refinement. ProfiliTable integrates (i) a Profiler that performs ReAct-style data exploration to build semantic understanding, (ii) a Generator that retrieves curated operators to synthesize task-aware code, and (iii) an Evaluator-Summarizer loop that injects execution scores and diagnostic insights to enable closed-loop refinement. Extensive experiments on a diverse benchmark covering 18 tabular task types demonstrate that ProfiliTable consistently outperforms strong baselines, particularly in complex multi-step scenarios. These results highlight the critical role of dynamic profiling in reliably translating ambiguous user intents into robust and governance-compliant table transformations.

</details>


### 144. Agent-Based Post-Hoc Correction of Agricultural Yield Forecasts

- **Authors:** Matthew Beddows, Aiden Durrant, Georgios Leontidis
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12375v1](http://arxiv.org/abs/2605.12375v1)
- **PDF:** [https://arxiv.org/pdf/2605.12375v1](https://arxiv.org/pdf/2605.12375v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces a modular large‑language‑model (LLM) agent that post‑hoc corrects crop‑yield forecasts generated by conventional machine‑learning models, compensating for the limited sensor and remote‑sensing data typical of commercial farms. The framework chains specialized tools for phenological phase detection, bias learning, and prediction‑range validation, allowing the LLM to inject domain knowledge and adjust the raw model outputs. Experiments on a proprietary strawberry dataset and USDA corn data show that the LLM‑driven corrections cut XGBoost’s MAE by 20 % (MAE ↓ 56 % MASE) and yielded comparable or larger gains for Random Forest and Moirai2 baselines, with Llama 3.1 8B delivering the most reliable improvements, underscoring the potential of agentic AI for lightweight, data‑scarce agricultural forecasting.


<details>
<summary>Abstract</summary>

Accurate crop yield forecasting in commercial soft fruit production is constrained by the data available in typical commercial farm records, which lack the sensor networks, satellite imagery, and high-resolution meteorological inputs that most state-of-the-art approaches assume. We propose a structured LLM agent framework that performs post-hoc correction of existing model predictions, encoding agricultural domain knowledge across tools for phase detection, bias learning, and range validation. Evaluated on a proprietary strawberry yield dataset and a public USDA corn harvest dataset, agent refinement of XGBoost reduced MAE by 20% and MASE by 56% on strawberry, with consistent improvements across Moirai2 (MAE 24%, MASE 22%) and Random Forest (MAE 28%, MASE 66%) baselines. Using Llama 3.1 8B as the agent produced the strongest corrections across all configurations; LLaVA 13B showed inconsistent gains, highlighting sensitivity to the choice of refinement model.

</details>


### 145. Attacks and Mitigations for Distributed Governance of Agentic AI under Byzantine Adversaries

- **Authors:** Matthew D. Laws, Alina Oprea, Cristina Nita-Rotaru
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12364v1](http://arxiv.org/abs/2605.12364v1)
- **PDF:** [https://arxiv.org/pdf/2605.12364v1](https://arxiv.org/pdf/2605.12364v1)
- **Categories:** cs.CR, cs.LG, cs.MA


> The paper exposes a critical vulnerability in the existing SAGA framework for agentic‑AI governance: a malicious or compromised Provider can subvert identity, privacy, and access‑control mechanisms. By formally modeling the Provider’s role and deploying realistic cloud‑based testbeds, the authors demonstrate concrete attacks that steal private data, erase attribution, and bypass policies. To mitigate these threats they introduce a spectrum of hardened architectures—**SAGA‑BFT** (full Byzantine fault‑tolerance at high cost), **SAGA‑MON** and **SAGA‑AUD** (lightweight server monitoring or client‑side auditing with modest overhead), and **SAGA‑HYB** (a hybrid of the two)—and empirically evaluate each, showing that monitoring/auditing solutions achieve near‑SAGA performance while thwarting the majority of Provider‑centric attacks, and that the hybrid design offers configurable security‑performance trade‑offs.


<details>
<summary>Abstract</summary>

Agentic AI governance is a critical component of agentic AI infrastructure ensuring that agents follow their owner's communication and interaction policies, and providing protection against attacks from malicious agents. The state-of-the-art solution, SAGA, assumes a logically centralized point of trust, the Provider, which serves as a repository for user and agent information and actively enforces policies. While SAGA provides protection against malicious agents, it remains vulnerable to a malicious Provider that deviates from the protocol, undermining the security of the identity and access control infrastructure. Deployment on both private and public clouds, each susceptible to insider threats, further increases the risk of Provider compromise.
  In this work, we analyze the attacks that can be mounted from a compromised Provider, taking into account the different system components and realistic deployments. We identify and execute several concrete attacks with devastating effects: undermining agent attributability, extracting private data, or bypassing access control. We then present three types of solutions for securing the Provider that offer different trade-offs between security and performance. We first present SAGA-BFT, a fully byzantine-resilient architecture that provides the strongest protection, but incurs significant performance degradation, due to the high-cost of byzantine resilient protocols. We then propose SAGA-MON and SAGA-AUD, two novel solutions that leverage lightweight server-side monitoring or client-side auditing to provide protection against most classes of attacks with minimal overhead. Finally, we propose SAGA-HYB, a hybrid architecture that combines byzantine-resilience with monitoring and auditing to trade-off security for performance. We evaluate all the architectures and compare them with SAGA. We discuss which solution is best and under what conditions.

</details>


### 146. LISA: Cognitive Arbitration for Signal-Free Autonomous Intersection Management

- **Authors:** Abderrahmane Lakas, Mohamed Amine Ferrag, Merouane Debbah
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12321v1](http://arxiv.org/abs/2605.12321v1)
- **PDF:** [https://arxiv.org/pdf/2605.12321v1](https://arxiv.org/pdf/2605.12321v1)
- **Categories:** cs.AI, cs.CY, cs.ET


> The paper introduces **LISA (LLM‑Based Intent‑Driven Speed Advisory)**, a novel signal‑free intersection manager that places a large language model at the core of the arbitration process, using it to reason about each vehicle’s declared intent, priority class, queue pressure and energy preferences. By encoding these factors into a prompt and running the LLM inference in a tightly bounded time window, LISA generates real‑time speed‑advice recommendations that replace traditional traffic signals or reservation‑based schemes. Empirical evaluation on realistic traffic scenarios shows that LISA cuts average control delay by up to 89 % (maintaining Level‑of‑Service C while baselines fall to F), reduces waiting time by 93 %, peak queue length by 60 %, fuel consumption by nearly 49 %, and raises intent‑satisfaction to 86 % versus 61 % for the best non‑LLM baseline, thereby demonstrating that LLM‑driven cognitive arbitration can serve as an effective primary decision‑maker for autonomous, signal‑free intersection control.


<details>
<summary>Abstract</summary>

Large language models (LLMs) show strong potential for Intelligent Transportation Systems (ITS), particularly in tasks requiring situational reasoning and multi-agent coordination. These capabilities make them well suited for cooperative driving, where rule-based approaches struggle in complex and dynamic traffic environments. Intersection management remains especially challenging due to conflicting right-of-way demands, heterogeneous vehicle priorities, and vehicle-specific kinematic constraints that must be resolved in real time. However, existing approaches typically use LLMs as auxiliary components on top of signal-based systems rather than as primary decision-makers. Signal controllers remain vehicle-agnostic, reservation-based methods lack intent awareness, and recent LLM-based systems still depend on signal infrastructure. In addition, LLM inference latency limits their use in sub-second control settings.
  We propose LISA (LLM-Based Intent-Driven Speed Advisory), a signal-free cognitive arbitration framework for autonomous intersection management. LISA uses an LLM to reason over declared vehicle intents, incorporating priority classes, queue pressure, and energy preferences. We evaluate LISA against fixed-cycle control, SCATS, AIM, and GLOSA across varying traffic loads. Results show that LISA reduces mean control delay by up to 89.1% and maintains Level of Service C while all non-LLM baselines degrade to Level of Service F. Under near-saturated demand, LISA reduces mean waiting time by 93% and peak queue length by 60.6% relative to fixed-cycle control. It also lowers fuel consumption by up to 48.8% and achieves 86.2% intent satisfaction, compared to 61.2% for the best non-LLM method. These results demonstrate that LLM-based reasoning can enable real-time, signal-free intersection management.

</details>


### 147. Ensuring Logic in the Fog: Sound POMDP Synthesis with LTL Objectives

- **Authors:** Can Zhou, Yulong Gao, Pian Yu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12581v1](http://arxiv.org/abs/2605.12581v1)
- **PDF:** [https://arxiv.org/pdf/2605.12581v1](https://arxiv.org/pdf/2605.12581v1)
- **Categories:** cs.LO, cs.AI, cs.FL, math.OC


> The paper introduces a sound reward‑shaping technique that converts LTL specifications into belief‑dependent reward signals for partially observable Markov decision processes (POMDPs), guaranteeing that the rewards are only given when a formally certified LTL satisfaction condition holds. By embedding this mechanism into an augmented Monte‑Carlo Tree Search planner, the authors obtain a quantitative synthesis method that can safely guide agents under partial observability despite the undecidability of qualitative LTL verification. Experiments on standard benchmark POMDPs show that the approach reliably outperforms existing solvers—solving tasks they cannot and scaling to larger domains while preserving provable correctness of the temporal‑logic objectives.


<details>
<summary>Abstract</summary>

Synthesising autonomous agents that can navigate uncertain environments while adhering to complex temporal constraints remains a fundamental challenge. While Linear Temporal Logic (LTL) provides a rigorous language for specifying such tasks, the inherent undecidability of qualitatively verifying LTL satisfaction in partially observable Markov decision processes renders quantitative synthesis difficult, especially when designing reliable reward signals for approximate solvers. In this paper, we bridge this gap with a novel, sound reward-shaping mechanism that dynamically generates belief-dependent rewards grounded in certified LTL satisfaction. By integrating this mechanism into an enhanced Monte Carlo Planning framework, we empower agents to navigate the `fog' of partial observability with a search process focused on maximising verifiable success. Our experiments demonstrate that this approach not only thrives in scenarios where existing solvers fail but also maintains effectiveness and scalability across diverse benchmark domains.

</details>


### 148. Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt Engineering Quality Assurance

- **Authors:** Elias Calboreanu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12280v1](http://arxiv.org/abs/2605.12280v1)
- **PDF:** [https://arxiv.org/pdf/2605.12280v1](https://arxiv.org/pdf/2605.12280v1)
- **Categories:** cs.SE, cs.AI


> The paper’s main contribution is an empirical demonstration that an LLM‑managed, checklist‑driven audit loop can systematically uncover consistency defects in the large, interdependent prompt specifications that govern multi‑agent LLM pipelines. The authors implemented nine successive audit rounds in which Claude‑based sub‑agents iteratively inspected the 7‑lane AEGIS orchestration system (≈7 150 lines of PROMPT.md files plus a shared contract) using a adapted Weinberg‑Freedman walkthrough; defects were coded into a seven‑category taxonomy and the audit protocol was distilled into a reproducible checklist. The study found 51 distinct prompt‑specification defects—revealing non‑monotonic convergence due to cascading edits and scope expansion—and showed that single‑file reviews miss many defect classes, highlighting the need for iterative, multi‑file LLM audits (and validation with other models or humans) to improve reliability in agentic AI systems.


<details>
<summary>Abstract</summary>

Prompt specifications for multi-agent large language model (LLM) systems carry data contracts and integration logic across many interdependent files but are rarely subjected to structured-inspection rigor. This paper reports a single-system empirical case study of iterative, agent-driven auditing applied to AEGIS (Autonomous Engineering Governance and Intelligence System), a production seven-lane orchestration pipeline whose prompt-specification surface comprises approximately 7150 lines: 6907 across seven lane PROMPT.md files and a 245-line shared Ticket Contract. Nine sequential audit rounds, executed by Claude sub-agents using a checklist-driven walkthrough adapted from Weinberg and Freedman, surfaced 51 prompt-specification consistency defects, distinct from the 51 STRIDE-categorized adversarial code findings reported in the companion preprint. Per-round counts were 15, 8, 12, 2, 8, 1, 4, 1, and 0. We report a seven-category post-hoc defect taxonomy with explicit coding rules, observed non-monotonic convergence consistent with cascading edits and audit-scope expansion, and an audit protocol distilled from the study, with the final locked checklist released as a reproducibility appendix. Single-file review missed defect classes that were surfaced only by later expanded-scope rounds in this system. The same LLM family authored and audited the specifications; replication with dissimilar models and human reviewers is required before generalization.

</details>


### 149. No Action Without a NOD: A Heterogeneous Multi-Agent Architecture for Reliable Service Agents

- **Authors:** Zixu Yang, Hang Zheng, Nan Jiang, Zhiyang Tang, Situo Zhang, Xiaobao Wu, Lu Chen, Kai Yu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12240v1](http://arxiv.org/abs/2605.12240v1)
- **PDF:** [https://arxiv.org/pdf/2605.12240v1](https://arxiv.org/pdf/2605.12240v1)
- **Categories:** cs.AI


> **Main contribution** – The paper introduces **NOD (Navigator‑Operator‑Director)**, a heterogeneous multi‑agent framework that externalizes a structured global state and adds a supervisory “Director” step to verify critical actions, thereby tackling the unreliability of LLM‑based service agents in long‑horizon tasks.

**Methodology** – NOD decomposes a service task into three roles: a **Navigator** that reasons over the explicit global state to plan the next step, an **Operator** that executes tool calls, and a **Director** that selectively reviews and can veto or amend those calls before execution. The architecture replaces implicit context‑based state tracking with a mutable state store and inserts a “no‑action‑without‑NOD” checkpoint for high‑risk operations.

**Key findings** – On the τ²‑Bench benchmark, NOD outperforms prior monolithic LLM agents in overall task success and, crucially, in the precision of critical actions. It reduces policy violations, tool hallucinations, and user‑intent misalignments, demonstrating that structured state and external oversight dramatically improve the reliability of agentic AI service systems.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents have increasingly advanced service applications, such as booking flight tickets. However, these service agents suffer from unreliability in long-horizon tasks, as they often produce policy violations, tool hallucinations, and misaligned actions, which greatly impedes their real-world deployment. To address these challenges, we propose NOD (Navigator-Operator-Director), a heterogeneous multi-agent architecture for service agents. Instead of maintaining task state implicitly in dialogue context as in prior work, we externalize a structured Global State to enable explicit task state tracking and consistent decision-making by the Navigator. Besides, we introduce selective external oversight before critical actions, allowing an independent Director agent to verify execution and intervene when necessary. As such, NOD effectively mitigates error propagation and unsafe behavior in long-horizon tasks. Experiments on $τ^2$-Bench demonstrate that NOD achieves higher task success rates and critical action precision over baselines. More importantly, NOD improves the reliability of service agents by reducing policy violations, tool hallucinations, and user-intent misalignment.

</details>


### 150. Harness Engineering as Categorical Architecture

- **Authors:** Bogdan Banu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12239v1](http://arxiv.org/abs/2605.12239v1)
- **PDF:** [https://arxiv.org/pdf/2605.12239v1](https://arxiv.org/pdf/2605.12239v1)
- **Categories:** cs.PL, cs.AI, math.CT


> The paper shows that the “harness” surrounding LLM‑based agents—its prompts, tools, memory, and orchestration logic—can be formally modelled using the categorical Architecture triple \((G,\text{Know},\Phi)\) from the ArchAgents framework. By mapping the four pillars of agent externalization (Memory → coalgebraic state, Skills → operad‑composed objects, Protocols → syntactic wiring \(G\), and the whole Harness → the Architecture) the authors derive structural guarantees (integrity gates, quality‑based escalation, convergence checks) that are preserved by compilation via identity or replay verification rather than by checking model outputs. A reference implementation provides compilers targeting Swarms, DeerFlow, Ralph, Scion, and LangGraph, each preserving three certificate types; experiments with real LLM agents demonstrate that the quality‑based escalation mechanism works consistently across two models on a single task, establishing categorical architecture as a rigorous theory for harness engineering in agentic AI.


<details>
<summary>Abstract</summary>

The agent harness, the system layer comprising prompts, tools, memory, and orchestration logic that surrounds the model, has emerged as the central engineering abstraction for LLMbased agents. Yet harness design remains ad hoc, with no formal theory governing composition, preservation of properties under compilation, or systematic comparison across frameworks. We show that the categorical Architecture triple (G, Know, Phi) from the ArchAgents framework provides exactly this formalization. The four pillars of agent externalization (Memory, Skills, Protocols, Harness Engineering) map onto the triple's components: Memory as coalgebraic state, Skills as operad-composed objects, Protocols as syntactic wiring G, and the full Harness as the Architecture itself. Structural guarantees-integrity gates, quality-based escalation, supported convergence checks-are Know-level certificates whose preservation is structural replay: our compiler checks identity and verifier replay, not output-layer correctness or model behavior. We validate this correspondence with a reference implementation featuring compiler functors targeting Swarms, DeerFlow, Ralph, Scion, and LangGraph: the four configuration compilers preserve three named certificate types by identity or replay, and LangGraph preserves the same certificates through its shared per-stage execution path. The LangGraph compiler creates one node per stage using the same per-stage method as the native runtime, providing LangGraph-native observability without reimplementing harness logic. An end-to-end escalation experiment with real LLM agents confirms that the quality-based escalation control path is model-parametric in this two-model, one-task experiment. The result positions categorical architecture as the formal theory behind harness engineering.

</details>


### 151. TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion

- **Authors:** Mohammad Khoshkdahan, Alexey Vinel
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12220v1](http://arxiv.org/abs/2605.12220v1)
- **PDF:** [https://arxiv.org/pdf/2605.12220v1](https://arxiv.org/pdf/2605.12220v1)
- **Categories:** cs.CV, cs.AI, cs.LG, cs.RO


> **Contribution:** The paper proposes **TriBand‑BEV**, a lightweight LiDAR‑only 3D pedestrian detector that recasts 3D detection as a 2‑D bird’s‑eye‑view (BEV) problem by encoding the full point cloud into three height‑aware BEV bands and then reconstructing 3‑D boxes from the 2‑D outputs.  

**Methodology:** A single‑stage convolutional network processes the tri‑band BEV tensor using deep **area‑attention** backbones, a hierarchical bidirectional neck that fuses coarse context (P4) with fine detail (P1‑P3), and a detection head that predicts oriented boxes with distribution‑focal side‑offset learning and a rotated IoU loss. Training incorporates a small vertical re‑binning, reflectance jitter, and an interquartile‑range filter to suppress noisy points.  

**Key Findings:** On the KITTI benchmark the model achieves **58.7 % / 52.6 % / 47.2 %** BEV AP for pedestrians (easy/moderate/hard) at **≈49 FPS** on a consumer GPU, outperforming Complex‑YOLO by +12.6 %, +7.5 %, and +3.1 % respectively, while maintaining stable performance under occlusion—demonstrating a practical real‑time perception module for autonomous agents.


<details>
<summary>Abstract</summary>

Safe autonomous agents and mobile robots need fast real time 3D perception, especially for vulnerable road users (VRUs) such as pedestrians. We introduce a new bird's eye view (BEV) encoding, which maps the full 3D LiDAR point cloud into a light-weight 2D BEV tensor with three height bands. We explicitly reformulate 3D detection as a 2D detection problem and then reconstruct 3D boxes from the BEV outputs. A single network detects cars, pedestrians, and cyclists in one pass. The backbone uses area attention at deep stages, a hierarchical bidirectional neck over P1 to P4 fuses context and detail, and the head predicts oriented boxes with distribution focal learning for side offsets and a rotated IoU loss. Training applies a small vertical re bin and a mild reflectance jitter in channel space to resist memorization. We use an interquartile range (IQR) filter to remove noisy and outlier LiDAR points during 3D reconstruction. On KITTI dataset, TriBand-BEV attains 58.7/52.6/47.2 pedestrian BEV AP(%) for easy, moderate, and hard at 49 FPS on a single consumer GPU, surpassing Complex-YOLO, with gains of +12.6%, +7.5%, and +3.1%. Qualitative scenes show stable detection under occlusion. The pipeline is compact and ready for real time robotic deployment. Our source code is publicly available on GitHub.

</details>


### 152. Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems

- **Authors:** Jiazhou Liang, Armin Toroghi, Yifan Simon Liu, Faeze Moradi Kalarde, Liam Gallagher, Scott Sanner
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12213v1](http://arxiv.org/abs/2605.12213v1)
- **PDF:** [https://arxiv.org/pdf/2605.12213v1](https://arxiv.org/pdf/2605.12213v1)
- **Categories:** cs.AI


> **Paper Summary**

The authors present **Goal‑Mem**, a goal‑oriented reasoning framework that augments retrieval‑augmented generation (RAG) memory for conversational LLM agents. Instead of retrieving documents solely by semantic similarity to the user query, Goal‑Mem treats the user utterance as a logical goal, decomposes it into atomic sub‑goals, and performs **backward‑chaining** retrieval: each sub‑goal triggers a targeted memory lookup, and unresolved sub‑goals dynamically guide further searches. This process is formalized in **Natural Language Logic**, a hybrid of first‑order logic verifiability and natural‑language expressivity.

Experimentally, Goal‑Mem is evaluated on two multi‑hop/commonsense benchmark suites against nine strong RAG‑based memory baselines. The results show consistent gains—especially on tasks requiring multi‑step inference and implicit knowledge—demonstrating that explicit goal‑driven retrieval substantially improves the reasoning capabilities of agentic LLM systems.


<details>
<summary>Abstract</summary>

LLM-based conversational AI agents struggle to maintain coherent behavior over long horizons due to limited context. While RAG-based approaches are increasingly adopted to overcome this limitation by storing interactions in external memory modules and performing retrieval from them, their effectiveness in answering challenging questions (e.g., multi-hop, commonsense) ultimately depends on the agent's ability to reason over the retrieved information. However, existing methods typically retrieve memory based on semantic similarity to the raw user utterance, which lacks explicit reasoning about missing intermediate facts and often returns evidence that is irrelevant or insufficient for grounded reasoning. In this work, we introduce Goal-Mem, a goal-oriented reasoning framework for RAG-based agentic memory that performs explicit backward chaining from the user's utterance as a goal. Rather than progressively expanding from retrieved context, Goal-Mem decomposes each goal into atomic subgoals, performs targeted memory retrieval to satisfy each subgoal, and iteratively identifies what information from memory should be retrieved when intermediate goals cannot be resolved. We formalize this process in Natural Language Logic, a logical system that combines the verifiability of reasoning provided by FOL with the expressivity of natural language. Through extensive experiments on two datasets and comparing to nine strong memory baselines, we show that Goal-Mem consistently improves performance, particularly on tasks requiring multi-hop reasoning and implicit inference.

</details>


### 153. Correcting Selection Bias in Sparse User Feedback for Large Language Model Quality Estimation: A Multi-Agent Hierarchical Bayesian Approach

- **Authors:** Andrea Morandi, Mahesh Viswanathan
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12177v1](http://arxiv.org/abs/2605.12177v1)
- **PDF:** [https://arxiv.org/pdf/2605.12177v1](https://arxiv.org/pdf/2605.12177v1)
- **Categories:** cs.CL


> **Main contribution**  
The paper introduces a hierarchical Bayesian framework that uses three cooperating agents to remove the severe selection bias inherent in sparse, user‑generated thumbs‑up/down signals for large‑language‑model (LLM) quality estimation.  

**Methodology**  
1. **Topic‑Clustering Agent** – clusters incoming interaction texts with UMAP + HDBSCAN on embeddings, yielding topic groups \(c\).  
2. **Bias‑Modeling Agent** – fits a two‑stage Beta‑Binomial model (via NUTS MCMC) that jointly infers each topic’s selection probability \(s_c\) and latent quality \(q_c\) while sharing strength across topics (partial pooling).  
3. **Synthesis Agent** – re‑weights the per‑topic posteriors by the empirical topic prevalence \(\hat\pi_c\) to produce a bias‑corrected aggregate quality posterior \(\bar Q\) and credible intervals, with optional drift alerts for online updates.  

**Key findings for agentic AI**  
- On the UltraFeedback dataset (≈10 k interactions, 18 topics) with simulated, highly imbalanced feedback (bias ratios up to 30:1), the Hierarchical‑Informed variant stays within **4–13 pp** of the true quality (\(Q^\star=0.625\)), whereas naive averaging errs by **40–50 pp**.  
- Incorporating a weak prior on the overall feedback channel (readable from any production dashboard) resolves an identifiability degeneracy and yields **95 % credible intervals that contain \(Q^\star\) in 50 % of random‑seed replicates** up to a bias ratio of 10.  
- All other weak‑prior Bayesian variants miss \(Q^\star\) by 22–33 pp, demonstrating that the bias‑channel prior—not a prior on latent quality—is essential for accurate bias correction.  

Thus, a multi‑agent hierarchical Bayesian pipeline can reliably estimate LLM quality from highly biased, sparse user feedback, offering a practical tool for monitoring and calibrating autonomous language agents in production.


<details>
<summary>Abstract</summary>

[Abridged] Production LLM deployments receive feedback from a non-random fraction of users: thumbs sit mostly in the tails of the satisfaction distribution, and a naive average over them can land 40-50 percentage points away from true system quality. We treat this as a topic- and sentiment- stratified selection-bias problem and propose a three-agent hierarchical Bayesian pipeline that does not require ground-truth labels on individual interactions. A Topic Clustering Agent partitions the stream via UMAP + HDBSCAN over text embeddings; a Bias Modeling Agent fits a two-stage hierarchical Beta-Binomial under NUTS, inferring per-topic selection rates $s_c$ and quality $q_c$ with partial pooling; a Synthesis Agent reweights $q_c$ by true topic prevalence $\hatπ_c = n_c/N$ to report a bias-corrected aggregate posterior $\bar Q = \sum_c \hatπ_c q_c$ with credible interval, plus drift signals for online recalibration. Validation uses UltraFeedback (N=10,232 retained interactions, $C=18$ clusters, $Q^\star=0.6249$) with simulated topic- and sentiment-dependent selection biases. We compare five Bayesian variants against Naive and IPW baselines. A mild prior on the feedback channel (typical positive-feedback rate and negative-to-positive ratio, both readable from any production dashboard without labels) keeps Hierarchical-Informed within 4-13 pp of $Q^\star$ as the bias ratio sweeps from 1:1 to 30:1, with 95% credible intervals covering $Q^\star$ in 50/50 random-seed replicates at $κ_{\max}=10$. Without channel-side priors, every weak-prior variant misses $Q^\star$ by 22-33 pp: the per-cluster sufficient statistics admit a one-parameter family of equally good fits, and the prior on the bias channel (not on latent quality) is what breaks the degeneracy.

</details>


### 154. Rollout Cards: A Reproducibility Standard for Agent Research

- **Authors:** Charlie Masters, Ziyuan Liu, Stefano V. Albrecht
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12131v1](http://arxiv.org/abs/2605.12131v1)
- **PDF:** [https://arxiv.org/pdf/2605.12131v1](https://arxiv.org/pdf/2605.12131v1)
- **Categories:** cs.AI


> The paper identifies that existing agent‑centric RL research lacks reproducible evidence because studies report only aggregate scores while discarding the underlying rollout trajectories that generate those scores. To remedy this, the authors propose **“rollout cards”**—standardized bundles that attach the full set of rollouts together with explicit metadata describing which runs were kept, dropped, or errored and the exact reporting rules used to compute headline numbers. Applying rollout cards to 50 public repositories and to four case studies (tool‑safety, multi‑agent coordination, theorem proving, and search) shows that different reporting conventions can shift success rates by up to 20.9 percentage points and even reverse model rankings, demonstrating that preserving rollout records is essential for reliable evaluation; the authors release an open‑source implementation in the Ergon gym and a library of rollout‑card exports for a range of benchmarks.


<details>
<summary>Abstract</summary>

Reproducibility problems that have long affected machine learning and reinforcement learning are now surfacing in agent research: papers compare systems by reported scores while leaving the rollout records behind those scores difficult to inspect. For agentic tasks, this matters because the same behaviour can receive different reported scores when evaluations select different parts of a rollout or apply different reporting rules. In a structured audit of 50 popular training and evaluation repositories, we find that none report how many runs failed, errored, or were skipped alongside headline scores. We also document 37 cases where reporting rules can change task-success rates, cost/token accounting, or timing measurements for fixed evidence, sometimes dramatically. We treat rollout records, not reported scores, as the unit of reproducibility for agent research. We introduce rollout cards: publication bundles that preserve the rollout record and declare the views, reporting rules, and drops manifests behind reported scores. We validate rollout cards in two settings. First, four partial public releases in tool safety, multi-agent systems, theorem proving, and search let us compute analyses their original reports did not include. Second, re-grading preserved benchmark outputs across short-answer, code-generation, and tool-use tasks shows that changing only the reporting rule can change reported scores by 20.9 absolute percentage points and, in some cases, invert rankings of frontier models. We release a reference implementation integrated into Ergon, an open-source reinforcement learning gym, and publicly publish Ergon-produced rollout-card exports for benchmarks spanning tool use, software engineering, web interaction, multi-agent coordination, safety, and search to support future research.

</details>


### 155. Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts

- **Authors:** Damir Safin, Dian Balta
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12105v1](http://arxiv.org/abs/2605.12105v1)
- **PDF:** [https://arxiv.org/pdf/2605.12105v1](https://arxiv.org/pdf/2605.12105v1)
- **Categories:** cs.AI


> The paper introduces a formal two‑dimensional design space for agentic AI that jointly captures **agency** (range of actions the system may take) and **autonomy** (degree of human‑free operation), each split into five concrete levels. It then proposes six concrete architectural tactics—checkpoints, escalation, multi‑agent delegation, tool provisioning, tool fencing, and write staging—that let developers deliberately move a deployment to a chosen point in this space, and it identifies five deployment parameters (model capability, architecture, tool fidelity, workflow bottlenecks, and evaluation) that bound what configurations are feasible. Through two public‑sector case studies, the authors show how the tactics enable compliance‑aware designs where responsibility, auditability, and reversibility are built in rather than added after deployment.


<details>
<summary>Abstract</summary>

Deploying agentic AI in regulated contexts requires principled reasoning about two design dimensions: agency (what the system can do) and autonomy (how much it acts without human involvement). Though often treated independently, they are coupled: at higher autonomy, human error correction is less available, so reliable operation requires constraining agency accordingly; compliance requirements reinforce this by mandating human involvement as action consequences grow. Yet no established approach addresses them jointly, leaving practitioners without a principled basis for reasoning about oversight, action consequences, and error correction.
  This work introduces a two-dimensional design space in which both dimensions are organised into five operational levels, making the coupling explicit and navigable. Autonomy ranges from human-commanded operation (L1) to fully autonomous monitoring (L5); agency ranges from reasoning over supplied context (L1) to committed writes to authoritative records (L5). Building on this space, we propose six architectural tactics--checkpoints, escalation, multi-agent delegation, tool provisioning, tool fencing, and write staging--for adjusting a deployment's position within it. The tactics are grounded in two worked examples from public-sector contexts, illustrating how they apply under realistic compliance constraints. We further examine five deployment parameters--model capability, agent architecture, tool fidelity, workflow bottlenecks, and evaluation--that shape what is achievable at any configuration independently of agency and autonomy. Together, the design space, tactics, and deployment parameters provide a shared vocabulary for principled, compliance-aware agentic AI design in which responsibility, auditability, and reversibility are explicit design considerations rather than properties that must be retrofitted after deployment.

</details>


### 156. Property-Level Reconstructability of Agent Decisions: An Anchor-Level Pilot Across Vendor SDK Adapter Regimes

- **Authors:** Oleg Solozobov
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.12078v1](http://arxiv.org/abs/2605.12078v1)
- **PDF:** [https://arxiv.org/pdf/2605.12078v1](https://arxiv.org/pdf/2605.12078v1)
- **Categories:** cs.SE, cs.AI


> **Paper Summary**

The authors introduce a *property‑level* evaluation of how well agent decisions can be reconstructed after the fact, using a single, unchanged tool—the Decision Trace Reconstructor (DTR). They applied DTR to a set of “anchor” decision traces drawn from six publicly available vendor SDKs (covering cloud‑agent, observability, tool‑use, telemetry, and protocol layers) and classified each decision‑event property as *fully fillable, partially fillable, structurally unfillable,* or *opaque*.  

Their pilot shows that reconstructability varies markedly across regimes: overall governance‑completeness ranges from **42.9 % to 85.7 %**, with a regime‑independent gap in the **reasoning‑trace** property and four additional gaps that depend on the specific SDK. The study provides a reproducible, checksum‑verified dataset and highlights where current SDKs and tracing standards fall short, offering a baseline for building more transparent, auditable agentic AI systems.


<details>
<summary>Abstract</summary>

Agentic AI failures need post-hoc reconstruction: what the agent did, on whose authority, against which policy, and from what reasoning. Cross-regime feasibility remains unmeasured under one property-level schema. We apply the Decision Trace Reconstructor unmodified to pinned worked-example anchors from six public vendor SDK regimes spanning cloud-agent, observability, tool-use, telemetry, and protocol traces, plus two comparator columns. Each Decision Event Schema (DES) property is classified as fully fillable, partially fillable, structurally unfillable, or opaque. Per-property reconstructability of an agent decision already varies between regimes at this anchor scale. Strict-governance-completeness separates into three tiers ranging from 42.9% to 85.7%, yielding one regime-independent gap (reasoning trace), four regime-dependent gaps, and one Mixed property; the pilot is single-annotator, one anchor per cell, descriptive, with outputs checksum-verifiable from a deposited reproducibility package.

</details>


### 157. Counterfactual Trace Auditing of LLM Agent Skills

- **Authors:** Xiaolin Zhou, Jinbo Liu, Li Li, Ryan A. Rossi, Xiyang Hu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11946v1](http://arxiv.org/abs/2605.11946v1)
- **PDF:** [https://arxiv.org/pdf/2605.11946v1](https://arxiv.org/pdf/2605.11946v1)
- **Categories:** cs.AI


> **Contribution** – The paper introduces **Counterfactual Trace Auditing (CTA)**, a framework that goes beyond pass‑rate metrics to quantify how an added LLM “skill” reshapes an agent’s internal reasoning trace. CTA produces **Skill Influence Pattern (SIP)** annotations that capture concrete behavioral changes (e.g., template copying, off‑task artifact generation, extra planning, recovery steps).

**Methodology** – For each task the authors run a paired experiment: the same LLM agent with and without a particular skill (Claude on the SWE‑Skills‑Bench, 49 software‑engineering problems). They segment both execution traces into goal‑directed phases, align the phases, and automatically generate structured SIP labels describing the skill’s influence on each phase.

**Findings** – Although the skill raises overall pass rate by only **+0.3 pp**, CTA discovers **522 SIP instances**, showing substantive behavioral modifications that traditional benchmarks miss. The effects concentrate on (1) high‑baseline “ceiling” tasks where performance is already saturated, (2) moderate‑baseline tasks that benefit the most but at higher token cost, and (3) distinct SIP types that correlate with baseline difficulty (surface anchoring on ceiling tasks, edge‑case prompting on mid‑range/floor tasks). These results reveal a hidden evaluation gap and provide a reproducible way to measure skill‑induced behavioral changes in agentic AI.


<details>
<summary>Abstract</summary>

Large Language Model agents are increasingly augmented with agent skills. Current evaluation methods for skills remain limited. Most deployed benchmarks report only pass rate before and after a skill is attached, treating the skill as a black box change to agent behavior. We introduce Counterfactual Trace Auditing (CTA), a framework for measuring how a skill changes agent behavior. CTA pairs each with skill agent trace with a without skill counterpart on the same task, segments both traces into goal directed phases, aligns the phases, and emits structured Skill Influence Pattern (SIP) annotations. These annotations describe the behavioral effect of a skill rather than only its task outcome. We instantiate CTA on SWE-Skills-Bench with Claude across 49 software engineering tasks. The resulting audit reveals a clear evaluation gap. Pass rate changes by only +0.3 percentage points on average, suggesting little aggregate effect. Yet CTA identifies 522 SIP instances across the same paired traces, showing that the skills substantially reshape agent behavior even when pass rate is nearly unchanged. The audit also separates several recurring effects that pass rate cannot detect, including literal template copying, off task artifact creation, excess planning, and task recovery. Three findings emerge. First, high baseline tasks contain most of the observed skill effects, although their pass rate is already saturated and therefore cannot reflect those effects. Second, tasks with moderate baseline performance show the most recoverable gain, but often at substantially higher token cost. Third, the dominant SIP type can be identified by baseline bucket: surface anchoring is most common on ceiling tasks and edge-case prompting is most common on mid-range and floor tasks. These regularities turn informal failure mode observations into reproducible behavioral measurements.

</details>


### 158. When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents

- **Authors:** Xiaolin Zhou, Aojie Yuan, Zheng Luo, Zipeng Ling, Xixiao Pan, Yicheng Gao, Haiyue Zhang, Jiate Li, Shuli Jiang, Prince Zizhuang Wang, Zixuan Zhu, Jinbo Liu, Ryan A. Rossi, Hua Wei, Xiyang Hu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11928v1](http://arxiv.org/abs/2605.11928v1)
- **PDF:** [https://arxiv.org/pdf/2605.11928v1](https://arxiv.org/pdf/2605.11928v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces **RobustBench‑TC**, a systematic sim‑to‑real benchmark that injects 22 realistic perturbations—spanning observation noise, action‑space errors, reward‑relevant metadata flaws, and transition glitches—into tool‑use language agents, and demonstrates that even large models (up to 32 B parameters) are highly vulnerable, especially to reward‑relevant and transition disturbances.  

**Methodology:** By framing tool‑use as a partially observable Markov decision process, the authors train agents with a **ToolRL‑DR** pipeline that uses domain‑randomized reinforcement learning on perturbation‑augmented trajectories covering the three statically encodable POMDP components (observations, actions, rewards).  

**Findings:** ToolRL‑DR, applied to a 3 B backbone, preserves ~75 % of clean‑task accuracy and achieves perturbed‑task performance on par with much larger open‑source baselines, closing ~27 % of the transition‑gap despite never seeing transition‑type failures during training, thereby highlighting RL‑based domain randomization as an effective route to more robust, deployable tool‑use agents.


<details>
<summary>Abstract</summary>

Tool-use language agents are evaluated on benchmarks that assume clean inputs, unambiguous tool registries, and reliable APIs. Real deployments violate all these assumptions: user typos propagate into hallucinated tool names, a misconfigured request timeout can stall an agent indefinitely, and duplicate tool names across servers can freeze an SDK. We study these failures as a sim-to-real gap in the tool-use partially observable Markov decision process (POMDP), where deployment noise enters through the observation, action space, reward-relevant metadata, or transition dynamics. We introduce RobustBench-TC, a benchmark with 22 perturbation types organized by these four POMDP components, each grounded in a verified GitHub issue or documented tool-calling failure. Across 21 models from 1.5B to 32B parameters (including the closed-source o4-mini), the robustness profile is sharply uneven: observation perturbations reduce accuracy by less than 5%, while reward-relevant and transition perturbations reduce accuracy by roughly 40% and 30%, respectively; scale alone does not close these gaps. We then propose ToolRL-DR, a domain-randomization reinforcement learning (RL) recipe that trains a tool-use agent on perturbation-augmented trajectories spanning the three statically encodable POMDP components. On a 3B backbone, ToolRL-DR-Full retains roughly three-quarters of clean accuracy and reaches an aggregate perturbed accuracy comparable to open-source 14B function-calling baselines while substantially narrowing the gap to o4-mini. It closes approximately 27% of the Transition gap despite never seeing transition perturbations in training, suggesting that RL on adversarial static tool-use inputs induces a more persistent retry policy that transfers to unseen runtime failures. The dataset, code and benchmark leaderboard are publicly available.

</details>


### 159. Proteus: A Self-Evolving Red Team for Agent Skill Ecosystems

- **Authors:** Zhaojiacheng Zhou
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11891v1](http://arxiv.org/abs/2605.11891v1)
- **PDF:** [https://arxiv.org/pdf/2605.11891v1](https://arxiv.org/pdf/2605.11891v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper introduces **Proteus**, a grey‑box, self‑evolving red‑team framework that quantifies *adaptive leakage*—the ability of a budgeted attacker to iteratively rewrite a third‑party LLM‑agent skill until it both passes static audit and causes verified runtime harm.

**Methodology:** Proteus formalizes a five‑dimensional “skill‑attack” space and repeatedly generates, audits, and sandbox‑executes candidate attacks. Structured audit feedback and runtime evidence are fed back to mutate the skill across rounds, while *path expansion* discovers alternative implementations of successful attacks and *surface expansion* transfers learned patterns to new attack objectives.

**Key findings:** Across eight evaluation cells, Proteus achieves 40–90 % attack‑success‑rate within five mutation rounds, and through path/surface expansion produces 438 lethal, audit‑bypassing skill variants. Even the strongest public auditor (AI‑Infra‑Guard) is fooled in up to 41.3 % of cases, demonstrating that existing skill‑vetting pipelines drastically under‑estimate residual risk against adaptive, feedback‑driven attackers.


<details>
<summary>Abstract</summary>

Agent skills extend LLM agents with reusable instructions, tool interfaces, and executable code, and users increasingly install third-party skills from marketplaces, repositories, and community channels. Because a skill exposes both executable behavior and context-setting documentation, its deployment risk cannot be measured by single-shot audits or prompt-level red teams alone: a realistic attacker can use audit and runtime feedback to repeatedly rewrite the skill. We frame this risk as \emph{adaptive leakage} -- whether a budgeted attacker can iteratively revise a skill until it passes audit and produces verified runtime harm -- and present \ours{}, a grey-box self-evolving red-team framework for measuring it. Proteus searches a formalized five-axis skill-attack space. Each candidate is evaluated through a unified audit-sandbox-oracle pipeline that returns structured audit findings and runtime evidence to guide cross-round mutation. Beyond initial evasion, Proteus performs path expansion, which finds alternative implementations of successful attacks, and surface expansion, which transfers learned implementation patterns to new attack objectives beyond the original seed catalogue. Across eight phase-1 cells, Proteus reaches 40--90\% Attack Success Rate at $5$ rounds (ASR@5) with positive learning-curve slopes on both evaluated auditors. Phase-2 path/surface expansion produces 438 jointly bypassing and lethal variants, with SkillVetter bypassed at $\geq 93\%$ in every cell and AI-Infra-Guard, the strongest public auditor we evaluate, still admitting up to 41.3\% joint-success. These results show that current skill vetting substantially underestimates residual risk when evaluated against adaptive, feedback-driven attackers.

</details>


### 160. On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment

- **Authors:** Bo Yin, Qi Li, Xinchao Wang
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11882v1](http://arxiv.org/abs/2605.11882v1)
- **PDF:** [https://arxiv.org/pdf/2605.11882v1](https://arxiv.org/pdf/2605.11882v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **FATE**, an on‑policy self‑evolution framework that converts verifier‑scored *failure trajectories* of tool‑using LLM agents into dense repair supervision, enabling agents to improve their safety without expert demonstrations.

**Methodology:** For each unsafe or over‑refusing trajectory, the current policy generates multiple repair candidates; a suite of verifiers re‑scores these candidates on security, utility, over‑refusal, and trajectory validity. The resulting trajectory‑level scores serve as supervised signals in a **Pareto‑Front Policy Optimization (PFPO)** loop that balances safety and task performance via Pareto‑aware updates after an initial supervised warm‑up.

**Key findings:** Across AgentDojo, AgentHarm, and ATBench benchmarks, FATE reduces attack success by **33.5 %**, cuts harmful compliance by **82.6 %**, and raises external safety diagnostics by **6.5 %** while preserving overall utility—demonstrating that leveraging failed trajectories is an effective, scalable way to align agentic AI safely.


<details>
<summary>Abstract</summary>

Tool-using LLM agents fail through trajectories rather than only final responses, as they may execute unsafe tool calls, follow injected instructions, comply with harmful requests, or over-refuse benign tasks despite producing a seemingly safe answer. Existing safety-alignment signals are largely response-level or off-policy, and often incur a safety-utility trade-off: improving agent safety comes at the cost of degraded task performance. Such sparse and single-objective rewards severely limit real-world usability. To bridge this gap, we propose FATE, an on-policy self-evolving framework that transforms verifier-scored failures into repair supervision without expert demonstrations. For each failure, the same policy proposes repair candidates, which are then re-scored by verifiers and filtered across security, utility, over-refusal control, and trajectory validity. This dense trajectory-level information is then used as a supervision signal for agent self-evolution. During this process, we further introduce Pareto-Front Policy Optimization (PFPO), combining supervised warmup with Pareto-aware policy optimization to preserve safety-utility trade-offs. Experiments on AgentDojo, AgentHarm, and ATBench show that FATE improves safety across different models and scales while preserving useful behavior. Compared with strong baselines, FATE reduces attack success rate by 33.5%, harmful compliance by 82.6%, and improves external trajectory-safety diagnosis by 6.5%. These results suggest that failed trajectories can provide structured repair supervision for safer self-evolving agents.

</details>


### 161. Adaptive TD-Lambda for Cooperative Multi-agent Reinforcement Learning

- **Authors:** Yue Deng, Zirui Wang, Yin Zhang
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11880v1](http://arxiv.org/abs/2605.11880v1)
- **PDF:** [https://arxiv.org/pdf/2605.11880v1](https://arxiv.org/pdf/2605.11880v1)
- **Categories:** cs.LG, cs.MA


> **Main contribution**  
The paper introduces **Adaptive TD‑λ (ATD‑λ)**, a method that dynamically adjusts the λ‑parameter in temporal‑difference learning for cooperative multi‑agent reinforcement learning (MARL). By estimating a likelihood‑free density ratio between the stationary distributions of the current and past policies using two replay buffers, ATD‑λ assigns each state‑action pair a λ value that reflects its relevance under the current policy, thereby addressing the bias–variance trade‑off without needing an explicit policy distribution.

**Methodology**  
- Two replay buffers of differing sizes store trajectories from the current policy and from earlier policies.  
- A parametric, likelihood‑free density‑ratio estimator computes the ratio of the two empirical distributions.  
- The estimated ratio is used to set λ adaptively for each update (higher λ for samples that are more likely under the current policy).  
- ATD‑λ is integrated into two state‑of‑the‑art cooperative MARL baselines: **QMIX** (value‑based) and **MAPPO** (actor‑critic).

**Key findings**  
Across the StarCraft II Micromanagement (SMAC) suite and Google‑Football academy tasks, ATD‑λ consistently matches or outperforms static‑λ baselines, achieving higher win‑rates and faster convergence. The results demonstrate that policy‑aware, adaptive λ scheduling can improve sample efficiency and final performance in cooperative MARL settings where the joint action space is large and data are scarce.


<details>
<summary>Abstract</summary>

TD($λ$) in value-based MARL algorithms or the Temporal Difference critic learning in Actor-Critic-based (AC-based) algorithms synergistically integrate elements from Monte-Carlo simulation and Q function bootstrapping via dynamic programming, which effectively addresses the inherent bias-variance trade-off in value estimation. Based on that, some recent works link the adaptive $λ$ value to the policy distribution in the single-agent reinforcement learning area. However, because of the large joint action space from multiple number of agents, and the limited transition data in Multi-agent Reinforcement Learning, the policy distribution is infeasible to be calculated statistically. To solve the policy distribution calculation problem in MARL settings, we employ a parametric likelihood-free density ratio estimator with two replay buffers instead of calculating statistically. The two replay buffers of different sizes store the historical trajectories that represent the data distribution of the past and current policies correspondingly. Based on the estimator, we assign Adaptive TD($λ$), \textbf{ATD($λ$)}, values to state-action pairs based on their likelihood under the stationary distribution of the current policy. We apply the proposed method on two competitive baseline methods, QMIX for value-based algorithms, and MAPPO for AC-based algorithms, over SMAC benchmarks and Gfootball academy scenarios, and demonstrate consistently competitive or superior performance compared to other baseline approaches with static $λ$ values.

</details>


### 162. IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection

- **Authors:**  Chia-Pei,  Chen, Kentaroh Toyoda, Anita Lai, Alex Leung
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11868v1](http://arxiv.org/abs/2605.11868v1)
- **PDF:** [https://arxiv.org/pdf/2605.11868v1](https://arxiv.org/pdf/2605.11868v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **IPI‑proxy**, an open‑source intercepting‑proxy toolkit that enables realistic red‑team testing of web‑browsing AI agents against indirect prompt‑injection (IPI) attacks on the very HTTP responses they retrieve from whitelisted domains. By dynamically rewriting live page content with a curated library of 820 attack strings (drawn from six prior benchmarks) and offering a YAML‑driven harness to sweep embedding techniques, insertion points, and payload sets, the system measures successful exfiltration callbacks without needing mock pages or sandboxed environments. Experiments show that IPI‑proxy can systematically trigger IPI vulnerabilities across multiple agent implementations, providing a reproducible, production‑level substrate for evaluating and hardening agentic AI systems against this class of web‑based attacks.


<details>
<summary>Abstract</summary>

Web-browsing AI agents are increasingly deployed in enterprise settings under strict whitelists of approved domains, yet adversaries can still influence them by embedding hidden instructions in the HTML pages those domains serve. Existing red-teaming resources fall short of this scenario: prompt-injection benchmarks ship pre-built adversarial pages that whitelisted agents cannot reach, and generic LLM scanners probe the model API rather than its retrieved content. We present IPI-proxy, an open-source toolkit for red-teaming web-browsing agents against indirect prompt injection (IPI). At its core is an intercepting proxy that rewrites real HTTP responses from whitelisted domains in flight, embedding payloads drawn from a unified library of 820 deduplicated attack strings extracted from six published benchmarks (BIPIA, InjecAgent, AgentDojo, Tensor Trust, WASP, and LLMail-Inject). A YAML-driven test harness independently parameterizes the payload set, the embedding technique (HTML comment, invisible CSS, or LLM-generated semantic prose), and the HTML insertion point (6 locations from \icode{head\_meta} to \icode{script\_comment}), enabling parameter-sweep evaluation without mock pages or sandboxed environments. A companion exfiltration tracker logs successful callbacks. This paper describes the threat model, situates IPI-proxy among contemporary IPI benchmarks and red-teaming tools, and details its architecture, design decisions, and configuration interface. By bridging static benchmarks and live deployment, IPI-proxy gives AI security teams a reproducible substrate for measuring and hardening web-browsing agents against indirect prompt injection on the same retrieval surface attackers exploit in production.

</details>


### 163. GEAR: Granularity-Adaptive Advantage Reweighting for LLM Agents via Self-Distillation

- **Authors:** Sijia Li, Yuchen Huang, Zifan Liu, Yanping Li, Jingjing Fu, Li Zhao, Jiang Bian, Ling Zhang, Jun Zhang, Rui Wang
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11853v2](http://arxiv.org/abs/2605.11853v2)
- **PDF:** [https://arxiv.org/pdf/2605.11853v2](https://arxiv.org/pdf/2605.11853v2)
- **Categories:** cs.LG, cs.AI, cs.CL


> **Main contribution:** The paper introduces **GEAR** (Granularity‑Adaptive Advantage Reweighting), a credit‑assignment framework that dynamically adjusts the granularity of advantage weighting for large‑language‑model (LLM) agents by leveraging self‑distillation signals.

**Methodology:** GEAR runs an on‑policy “student” model alongside a ground‑truth‑conditioned “teacher” model; the KL divergence between them is used as a reference‑guided signal to locate semantic deviation points. These spikes define adaptive segment boundaries: when divergence stays low, token‑level advantages are kept; when a spike occurs, the ensuing continuation is grouped into a segment whose advantage is re‑weighted by the divergence magnitude. This adaptive reweighting reshapes the trajectory‑level GRPO advantage used in reinforcement learning.

**Key findings:** Across eight math‑reasoning and tool‑use benchmarks with Qwen‑3 4B/8B models, GEAR consistently outperforms standard GRPO, pure self‑distillation, and fixed token‑ or turn‑level credit‑assignment baselines, achieving up to ~20 % absolute improvement on the toughest long‑horizon tasks. The results demonstrate that adaptive, fine‑grained credit assignment markedly enhances policy learning for agentic LLMs, especially in challenging, low‑baseline settings.


<details>
<summary>Abstract</summary>

Reinforcement learning has become a widely used post-training approach for LLM agents, where training commonly relies on outcome-level rewards that provide only coarse supervision. While finer-grained credit assignment is promising for effective policy updates, obtaining reliable local credit and assigning it to the right parts of the long-horizon trajectory remains an open challenge. In this paper, we propose Granularity-adaptivE Advantage Reweighting (GEAR), an adaptive-granularity credit assignment framework that reshapes the trajectory-level GRPO advantage using token- and segment-level signals derived from self-distillation. GEAR compares an on-policy student with a ground-truth-conditioned teacher to obtain a reference-guided divergence signal for identifying adaptive segment boundaries and modulating local advantage weights. This divergence often spikes at the onset of a semantic deviation, while later tokens in the same autoregressive continuation may return to low divergence. GEAR therefore treats such spikes as anchors for adaptive credit regions: where the student remains aligned with the teacher, token-level resolution is preserved; where it departs, GEAR groups the corresponding continuation into an adaptive segment and uses the divergence at the departure point to modulate the segment' s advantage. Experiments across eight mathematical reasoning and agentic tool-use benchmarks with Qwen3 4B and 8B models show that GEAR consistently outperforms standard GRPO, self-distillation-only baselines, and token- or turn-level credit-assignment methods. The gains are especially strong on benchmarks with lower GRPO baseline accuracy, reaching up to around 20\% over GRPO, suggesting that the proposed adaptive reweighting scheme is especially useful in more challenging long-horizon settings.

</details>


### 164. Trade-offs in Decentralized Agentic AI Discovery Across the Compute Continuum

- **Authors:** Patrizio Dazzi, Emanuele Carlini, Matteo Mordacchini, Saul Urso
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11839v1](http://arxiv.org/abs/2605.11839v1)
- **PDF:** [https://arxiv.org/pdf/2605.11839v1](https://arxiv.org/pdf/2605.11839v1)
- **Categories:** cs.DC, cs.AI


> **Main contribution:** The paper provides the first systematic comparison of three structured overlay networks—Chord, Pastry, and Kademlia—as the backbone for decentralized discovery services in agentic AI systems that must operate across the whole compute continuum (cloud, edge, and intermittently‑connected devices).  

**Methodology:** The authors embed each overlay in a common control‑plane prototype and evaluate them on two large‑scale benchmarks (a static 4 K‑node topology and a 4 K‑node churn scenario). Metrics include discovery reliability (lookup success rate), startup latency (time to form a functional directory), and control‑plane overhead (message traffic, state‑maintenance cost).  

**Key findings for agentic AI:**  
- **Reliability:** Kademlia consistently achieves the highest lookup success under churn, while Chord shows the poorest resilience to node turnover.  
- **Startup behavior:** Pastry converges fastest during network boot‑strapping, making it attractive for rapidly deployed edge clusters.  
- **Overhead:** Kademlia’s logarithmic routing tables incur lower maintenance traffic than Chord’s finger tables, but Pastry’s proximity‑aware routing yields modest bandwidth savings in geographically heterogeneous deployments.  

Overall, the study maps concrete trade‑offs—robustness vs. boot‑time vs. bandwidth—that designers of decentralized agent discovery services must balance when targeting heterogeneous edge‑to‑cloud AI deployments.


<details>
<summary>Abstract</summary>

Agentic systems deployed across the compute continuum need discovery mechanisms that remain effective across cloud, edge, and intermittently connected domains. In some emerging agentic architectures, decentralized discovery is already an active design direction, placing DHT-based lookup on the path toward agent directories. This paper studies the trade-offs among major structured-overlay families for agent discovery, comparing Chord, Pastry, and Kademlia as candidate indexing substrates within a shared control-plane framework. Using a benchmark subset centered on a 4096-node stationary comparison and a representative 4096-node churn benchmark, the paper characterizes how discovery reliability, startup behavior, and control-plane overhead vary across these overlays. The goal is to clarify the operating points they expose for agent discovery across edge-to-cloud environments.

</details>


### 165. Why Users Go There: World Knowledge-Augmented Generative Next POI Recommendation

- **Authors:** Qiuyu Ding, Heng-Da Xu, Wei Zhang, Dongyi Lv, Changda Xia, Feng Xiong, Mu Xu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11807v1](http://arxiv.org/abs/2605.11807v1)
- **PDF:** [https://arxiv.org/pdf/2605.11807v1](https://arxiv.org/pdf/2605.11807v1)
- **Categories:** cs.AI


> The paper introduces **AWARE**, an agent‑driven framework that enriches large‑language‑model (LLM) based next‑POI recommenders with up‑to‑date world knowledge (regional culture, seasonal trends, ongoing events) expressed as location‑ and time‑aware narrative contexts. The methodology treats an LLM as an autonomous “knowledge‑retrieval agent” that first gathers relevant external information, then conditions a generative recommendation model on both the user’s historical spatio‑temporal trajectory and the curated narrative, thereby grounding dynamic world facts in personalized mobility patterns. Experiments on three public mobility datasets show that AWARE consistently beats strong baselines, delivering up to **12.4 % relative gains** in recommendation accuracy, demonstrating the value of agentic, world‑knowledge augmentation for next‑POI prediction.


<details>
<summary>Abstract</summary>

Generative point-of-interest (POI) recommendation models based on large language models (LLMs) have shown promising results by formulating next POI prediction as a sequence generation task. However, the knowledge encoded in these models remains fixed after training, making them unable to perceive evolving real-world conditions that shape user mobility decisions, such as local events and cultural trends. To bridge this gap, we propose AWARE (Agent-based World knowledge Augmented REcommendation), which employs an LLM agent to generate location- and time-aware contextual narratives that capture regional cultural characteristics, seasonal trends, and ongoing events relevant to each user. Rather than introducing generic or noisy information, AWARE further anchors these narratives in each user's behavioral context, grounding external world knowledge in personalized spatial-temporal patterns. Extensive experiments on three real-world datasets demonstrate that AWARE consistently outperforms competitive baselines, achieving up to 12.4% relative improvement.

</details>


### 166. Beyond Inefficiency: Systemic Costs of Incivility in Multi-Agent Monte Carlo Simulations

- **Authors:** Alison Moldovan-Mauer, Benedikt Mangold
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11789v1](http://arxiv.org/abs/2605.11789v1)
- **PDF:** [https://arxiv.org/pdf/2605.11789v1](https://arxiv.org/pdf/2605.11789v1)
- **Categories:** cs.AI


> The paper introduces a controlled “sociological sandbox” that uses large‑language‑model (LLM) agents in Monte‑Carlo simulations of one‑on‑one debates to quantify how uncivil (toxic) communication degrades interactional efficiency. By varying toxicity levels and model sizes across thousands of runs, the authors show that toxic dialogue adds roughly 25 % more rounds before convergence—a delay that grows for smaller‑parameter models—and that the initiating agent enjoys a robust first‑mover advantage regardless of tone. These results demonstrate that the systemic cost of incivility can be systematically measured in multi‑agent AI systems, highlighting scalability‑dependent vulnerabilities that are critical for designing robust, cooperative agentic AI.


<details>
<summary>Abstract</summary>

Unconstructive debate and uncivil communication carry well-documented costs for productivity and cohesion, yet isolating their effect on operational efficiency has proven difficult. Human subject research in this domain is constrained by ethical oversight, limited reproducibility, and the inherent unpredictability of naturalistic settings. We address this gap by leveraging Large Language Model (LLM) based Multi-Agent Systems as a controlled sociological sandbox, enabling systematic manipulation of communicative behavior at scale. Using a Monte Carlo simulation framework, we generate thousands of structured 1-on-1 adversarial debates across varying toxicity conditions, measuring convergence time, defined as the number of rounds required to reach a conclusion, as a proxy for interactional efficiency. Building on a prior study, we replicate and extend its findings across two additional LLM agents of varying parameter size, allowing us to assess whether the effects of toxic behavior on debate dynamics generalize across model scale. The convergence latency of 25% reported in the previous study was confirmed. It was found that this latency is significantly bigger for models with fewer parameters. We further identify a significant first-mover advantage, whereby the agent initiating the discussion wins significantly above chance regardless of toxicity condition.

</details>


### 167. Behavioral Integrity Verification for AI Agent Skills

- **Authors:** Yuhao Wu, Tung-Ling Li, Hongliang Liu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11770v1](http://arxiv.org/abs/2605.11770v1)
- **PDF:** [https://arxiv.org/pdf/2605.11770v1](https://arxiv.org/pdf/2605.11770v1)
- **Categories:** cs.CR, cs.AI, eess.SY


> The paper introduces **Behavioral Integrity Verification (BIV)**, a framework that systematically checks whether an LLM‑agent’s “skill” (e.g., filesystem, network, credential, or shell access) behaves exactly as its declared capabilities. BIV combines deterministic static code analysis with LLM‑driven extraction of declared versus actual capabilities across a shared taxonomy, then generates structured evidence for deviation taxonomy, root‑cause classification, and malicious‑skill detection. Applied to ~50 k skills from the OpenClaw registry, BIV uncovers that 80 % of skills diverge from their specifications (mostly due to developer oversight), surfaces four new compound‑threat categories, and achieves a 0.946 F1 score on a 906‑skill malicious‑skill detection benchmark—substantially surpassing rule‑based and single‑pass LLM baselines, thereby demonstrating scalable integrity auditing for agentic AI components.


<details>
<summary>Abstract</summary>

Agent skills extend LLM agents with privileged third-party capabilities such as filesystem access, credentials, network calls, and shell execution. Existing safety work catches malicious prompts and risky runtime actions, but the skill artifact itself goes unverified. We formalize this as the behavioral integrity verification (BIV) problem: a typed set comparison between declared and actual capabilities over a shared taxonomy that bridges code, instructions, and metadata. The BIV framework instantiates this comparison by pairing deterministic code analysis with LLM-assisted capability extraction. The resulting structured evidence supports three downstream analyses: deviation taxonomy, root-cause classification, and malicious-skill detection. On 49,943 skills from the OpenClaw registry, the deviation taxonomy reveals a pervasive description-implementation gap: 80.0% of skills deviate from declared behavior, with four novel compound-threat categories surfaced. Root-cause classification finds that deviations are mostly oversight, not malice: 81.1% trace to developer oversight and 18.9% to adversarial intent, with 5.0% of skills carrying predicted multi-stage attack chains. On a 906-skill malicious-skill detection benchmark, BIV reaches an F1 of 0.946, outperforming state-of-the-art rule-based and single-pass LLM baselines. These results demonstrate behavioral integrity auditing for agent skills at scale.

</details>


### 168. OptArgus: A Multi-Agent System to Detect Hallucinations in LLM-based Optimization Modeling

- **Authors:** Zhong Li, Zihan Guo, Xiaohan Lu, Juntao Wang, Jie Song, Chao Shen, Jiageng Wu, Mingyang Sun
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11738v1](http://arxiv.org/abs/2605.11738v1)
- **PDF:** [https://arxiv.org/pdf/2605.11738v1](https://arxiv.org/pdf/2605.11738v1)
- **Categories:** cs.AI


> **Main contribution**  
The paper introduces **OptArgus**, the first multi‑agent framework specifically designed to detect “hallucinations” that occur when large language models (LLMs) generate optimization models—i.e., structural mismatches between the natural‑language problem description, the symbolic formulation, and the solver code. The authors also provide a fine‑grained taxonomy of such hallucinations (objective, variable, constraint, and implementation errors) and a new benchmark suite for systematic evaluation.

**Methodology**  
OptArgus consists of a **conductor** that routes a candidate artifact to a set of **specialist auditors** (each expert on a taxonomy slice), followed by an **evidence‑consolidation** stage that aggregates the auditors’ reports into a final detection/localization decision. The system is trained and calibrated using a three‑part benchmark: (1) 484 clean artifacts, (2) 1 266 artificially corrupted artifacts with known single‑error injections, and (3) 6 292 natural artifacts generated by LLMs.

**Key findings**  
Compared with a strong single‑agent baseline, OptArgus (i) generates fewer false alarms on clean artifacts, (ii) more accurately pinpoints the exact error location in controlled single‑error cases, and (iii) achieves higher overall hallucination detection rates on organically produced LLM outputs. These results demonstrate that a modular, taxonomy‑driven multi‑agent audit is an effective and scalable approach for improving the reliability of LLM‑based optimization modeling.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used to translate natural-language optimization problems into mathematical formulations and solver code, but matching the reference objective value is not a reliable test of correctness: an artifact may agree numerically while still changing the underlying optimization semantics. We formulate this issue as \emph{optimization-modeling hallucination detection}, namely structural consistency auditing over the problem description, symbolic model, and solver implementation. We develop, to our knowledge, the first fine-grained hallucination taxonomy specifically for optimization modeling, spanning objective, variable, constraint, and implementation failures. We use this taxonomy to design OptArgus, a multi-agent detector with conductor routing, specialist auditors, and evidence consolidation. To evaluate this setting, we introduce a three-part benchmark suite with $484$ clean artifacts, $1266$ controlled injected artifacts, and $6292$ natural LLM-generated artifacts. Against a matched single-agent baseline, OptArgus produces fewer false alarms on clean artifacts, more accurate top-ranked localization on controlled single-error cases, and stronger detection on natural model outputs. Together, these contributions turn optimization-modeling hallucination detection into a concrete empirical problem and suggest that modular, taxonomy-grounded auditing is a practical route to more reliable optimization modeling.

</details>


### 169. A Research Agenda on Agents and Software Engineering: Outcomes from the Rio A2SE Seminar

- **Authors:** Davide Taibi, Henry Muccini, Karthik Vaidhyanathan, Marcos Kalinowski, Michele Albano, Antonio Pedro Santos Alves, Renato Cerqueira, Mateus Devino, Matteo Esposito, Rodrigo Falcão, Vinicius Henning, Foutse Khomh, Valentina Lenarduzzi, Qinghua Lu, Matías Martínez, Henrique Mello, Daniel Mendez, Lucas Romao
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11720v1](http://arxiv.org/abs/2605.11720v1)
- **PDF:** [https://arxiv.org/pdf/2605.11720v1](https://arxiv.org/pdf/2605.11720v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> The paper reports a community‑driven research agenda for the emerging field of agentic AI in software engineering, derived from the A2SE seminar that gathered 18 academic and industry experts. Using structured presentations, collaborative clustering, and group discussions, participants converged on six thematic pillars—Governance, SE for Agents, Agents for Software Architecture, Quality & Evaluation, Sustainability, and Code—and outlined prioritized short‑ and long‑term research questions for each. The resulting agenda highlights that (i) software‑engineering practices must be reconceived to build, test, and maintain complex agentic systems, and (ii) agentic AI can be leveraged to automate and improve core SE activities, providing a concrete roadmap for future work in the agentic AI domain.


<details>
<summary>Abstract</summary>

The rise of agentic AI is reshaping software engineering in two intertwined directions: agents are increasingly applied to support software engineering tasks, and Agentic AI systems themselves are complex systems that require re-thinking currently established software engineering practices. To chart a coherent research agenda covering the two directions, we organized the A2SE seminar in Rio de Janeiro, bringing together 18 experts from academia and industry. Through structured presentations, collaborative topic clustering, and focused group discussions, participants identified six thematic areas: Governance, Software Engineering for Agents, Agents for Software Architecture, Quality and Evaluation, Sustainability, and Code, and they prioritized short-term and long-term research directions for each. This paper presents the resulting community-driven, opinionated research agenda, offering the SE community a structured foundation for coordinating efforts at this critical juncture.

</details>


### 170. Shaping Zero-Shot Coordination via State Blocking

- **Authors:** Mingu Kang, Sunwoo Lee, Yonghyeon Jo, Seungyul Han
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11688v1](http://arxiv.org/abs/2605.11688v1)
- **PDF:** [https://arxiv.org/pdf/2605.11688v1](https://arxiv.org/pdf/2605.11688v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> **Contribution:** The paper proposes **State‑Blocked Coordination (SBC)**, a novel framework that boosts zero‑shot coordination (ZSC) by systematically creating “blocked” versions of the environment, forcing agents to train with a spectrum of sub‑optimal partner behaviors without altering the underlying dynamics.  

**Methodology:** SBC generates a family of virtual environments by randomly masking (blocking) subsets of states during training, which implicitly diversifies partner policies the agent encounters. Agents are trained via standard RL (e.g., PPO) on these blocked environments, thereby learning robust coordination strategies that are transferable to the original, unblocked task.  

**Key Findings:** Across several ZSC benchmarks (including the **Overcooked** and **Hanabi** suites), SBC consistently outperforms prior diversity‑based methods, achieving higher pairwise scores with unseen AI partners and markedly better performance when paired with human participants, demonstrating a practical route to more reliable agentic AI cooperation in real‑world and human‑AI settings.


<details>
<summary>Abstract</summary>

Zero-shot coordination (ZSC) aims to enable agents to cooperate with independently trained partners without prior interaction, a key requirement for real-world multi-agent systems and human-AI collaboration. Existing approaches have largely emphasized increasing partner diversity during training, yet such strategies often fall short of achieving reliable generalization to unseen partners. We introduce State-Blocked Coordination (SBC), a simple yet effective framework that improves ZSC by inducing diverse interaction scenarios without direct environment modification. Specifically, SBC generates a family of virtual environments through state blocking, allowing agents to experience a wide range of suboptimal partner policies. Across multiple benchmarks, SBC demonstrates superior performance in zero-shot coordination, including strong generalization to human partners.

</details>


### 171. GeomHerd: A Forward-looking Herding Quantification via Ricci Flow Geometry on Agent Interactive Simulations

- **Authors:** Lake Yang, Junwei Su, Jingfeng Zeng, Wenhao Lu, Xingzhi Qian, Weitong Zhang, Chuan Wu, Dunhong Jin
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11645v1](http://arxiv.org/abs/2605.11645v1)
- **PDF:** [https://arxiv.org/pdf/2605.11645v1](https://arxiv.org/pdf/2605.11645v1)
- **Categories:** cs.MA, cs.LG, q-fin.ST


> **Main contribution:** The paper introduces **GeomHerd**, a novel forward‑looking framework that detects herding by measuring the discrete Ollivier‑Ricci curvature of action‑level interaction graphs generated from heterogeneous LLM‑driven financial‑trader simulations, thereby bypassing the lag inherent in traditional price‑correlation‑based herding metrics.  

**Methodology:** Agents are instantiated as persona‑conditioned LLM calls within a continuous‑spin (Cividino‑Sornette) multi‑agent simulator; their trade actions form a time‑evolving graph whose Ricci curvature is tracked, and a mean‑field analysis links this curvature to the classic CSAD herding statistic.  

**Key findings:** GeomHerd signals emerging coordination far earlier than price‑based baselines—median lead times of 272 simulation steps for order‑parameter onset and 40 steps over price‑correlation graphs—while also predicting cascade windows with lower log‑return MAE, and the curvature signal generalizes to unrelated models such as the Vicsek particle system, highlighting its relevance for proactive risk monitoring in agentic AI markets.


<details>
<summary>Abstract</summary>

Herding -- where agents align their behaviors and act collectively -- is a central driver of market fragility and systemic risk. Existing approaches to quantify herding rely on price-correlation statistics, which inherently lag because they only detect coordination after it has already moved realised returns. We propose GeomHerd, a forward-looking geometric framework that bypasses this observability lag by quantifying coordination directly on upstream agent-interaction graphs. To generate these graphs, we treat a heterogeneous LLM-driven multi-agent simulator -- each financial trader instantiated by a persona-conditioned LLM call -- as a forecastable world, and evaluate the geometric pipeline on the Cividino--Sornette continuous-spin agent-based substrate as our headline financial testbed. By tracking the discrete Ollivier--Ricci curvature of these action graphs, GeomHerd captures the structural topology of emerging coordination. Theoretically, we establish a mean-field bridge mapping our graph-theoretic metric to CSAD, the classical macroscopic herding statistic, linking GeomHerd to downstream price-dispersion measurement. Empirically, GeomHerd anticipates herding long before aggregate market baselines: on the continuous-spin substrate, our primary detector fires a median of 272 steps before order-parameter onset; a contagion detector ($β_{-}$) recalls 65% of critical trajectories 318 steps early; and on co-firing trajectories the agent-graph signal precedes price-correlation-graph baselines by 40 steps. As a complementary indicator, the effective vocabulary of agent actions contracts during cascades. The geometric signature transfers out-of-domain to the Vicsek self-driven-particle model, and a curvature-conditioned forecasting head reduces cascade-window log-return MAE over detector-conditioned and price-only baselines.

</details>


### 172. Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations

- **Authors:** Junjue Wang, Weihao Xuan, Heli Qi, Pengyu Dai, Kunyi Liu, Hongruixuan Chen, Zhuo Zheng, Junshi Xia, Stefano Ermon, Naoto Yokoya
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11633v1](http://arxiv.org/abs/2605.11633v1)
- **PDF:** [https://arxiv.org/pdf/2605.11633v1](https://arxiv.org/pdf/2605.11633v1)
- **Categories:** cs.AI


> The paper introduces **DORA**, the first comprehensive benchmark for evaluating large‑language‑model (LLM) agents on end‑to‑end disaster‑response workflows, comprising 515 expert‑crafted tasks from 45 real incidents, a library of 108 geospatial tools, and over 3,500 replayable gold‑standard tool‑call trajectories covering perception, spatial reasoning, evacuation planning, temporal analysis, and report synthesis. By testing 13 state‑of‑the‑art LLM agents on DORA, the authors show that current agents struggle with disaster‑specific grounding (e.g., damage semantics and sensor‑modality mismatches), are limited more by tool‑selection and argument generation than raw model size (gold tool‑order hints give ≤ 4.4 % boost), and their performance degrades sharply as the required tool‑call sequence lengthens (error gap expanding from 7 % to 56 %). These findings highlight critical gaps in agentic AI for operational geospatial reasoning and provide a rigorous testbed for future improvements.


<details>
<summary>Abstract</summary>

Operational disaster response goes beyond damage assessment, requiring responders to integrate multi-sensor signals, reason over road networks, populations and key facilities, plan evacuations, and produce actionable reports. However, prior work largely isolates remote-sensing perception or evaluates generic tool use, leaving the end-to-end workflows of emergency operations underexplored. In this paper, we introduce Disaster Operational Response Agent benchmark (DORA), the first agentic benchmark for end-to-end disaster response: 515 expert-authored tasks across 45 real-world disaster events spanning 10 types, paired with expert-verified, replayable gold trajectories totaling 3,500 tool-call steps. Tasks span five dimensions that cover the operational disaster-response pipeline: disaster perception, spatial relational analysis, rescue and evacuation planning, temporal evolution reasoning, and multi-modal report synthesis. Agents compose calls from a 108-tool MCP library over heterogeneous geospatial data: optical, SAR, and multi-spectral imagery across single-, bi-, and multi-temporal sequences (0.015-10m GSD), complemented by elevation and social vector layers. We comprehensively evaluate 13 frontier LLMs on our benchmark, revealing three persistent challenges: 1) disaster-domain grounding exposes unique failure modes (damage-semantic grounding, sensor-modality mismatch, and disaster-pipeline composition); 2) agents are doubly bottlenecked by tool selection and argument grounding, where gold tool-order hints improve accuracy by only 1.08-4.40%, and alternative scaffolds yield at most a 3.24% gain; 3) compositional fragility scales with trajectory length, the agent-to-gold gap widening from 7% to 56% on long pipelines. DORA establishes a rigorous testbed for operationally reliable disaster-response agents.

</details>


### 173. From Generic Correlation to Input-Specific Credit in On-Policy Self Distillation

- **Authors:** Guobin Shen, Lei Huang, Xiang Cheng, Chenxiao Zhao, Jindong Li, Dongcheng Zhao, Xing Yu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11613v1](http://arxiv.org/abs/2605.11613v1)
- **PDF:** [https://arxiv.org/pdf/2605.11613v1](https://arxiv.org/pdf/2605.11613v1)
- **Categories:** cs.LG, cs.AI


> The paper analytically shows that the token‑level reward used in on‑policy self‑distillation is exactly the incremental Bayesian‑filter term whose trajectory sum equals the pointwise mutual information (pMI) between a model’s response and the environment feedback conditioned on the input.  Building on this insight, the authors introduce **CREDIT**—a contrastive reformulation that subtracts a batch‑wise baseline to isolate the input‑specific portion of the teacher’s log‑probability, thereby turning the self‑distillation signal into a contrastive pMI objective that penalizes responses that remain probable under unrelated inputs.  Experiments on coding, scientific‑reasoning, and tool‑use benchmarks with two model families demonstrate that CREDIT consistently yields the highest aggregate gains over standard self‑distillation while adding virtually no extra computation.


<details>
<summary>Abstract</summary>

On-policy self-distillation has emerged as a promising paradigm for post-training language models, in which the model conditions on environment feedback to serve as its own teacher, providing dense token-level rewards without external teacher models or step-level annotations. Despite its empirical success, what this reward actually measures and what kind of credit it assigns remain unclear. Under a posterior-compatibility interpretation of feedback conditioning, standard in the implicit-reward literature, we show that the self-distillation token reward is a Bayesian filtering increment whose trajectory sum is exactly the pointwise mutual information between the response and the feedback given the input. This pMI can be raised by input-specific reasoning or by input-generic shortcuts, so we further decompose the teacher log-probability along the input axis. Based on this analysis, we propose CREDIT (Contrastive REward from DIsTillation), which isolates the input-specific component with a batch-contrastive baseline. At the sequence level, CREDIT is a teacher-side surrogate for a contrastive pMI objective that also penalizes responses remaining likely under unrelated inputs. Across coding, scientific reasoning, and tool-use benchmarks on two model families, CREDIT delivers the strongest aggregate performance at negligible additional compute.

</details>


### 174. CTFusion: A CTF-based Benchmark for LLM Agent Evaluation

- **Authors:** Dongjun Lee, Ga-eun Bae, Insu Yun
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11504v1](http://arxiv.org/abs/2605.11504v1)
- **PDF:** [https://arxiv.org/pdf/2605.11504v1](https://arxiv.org/pdf/2605.11504v1)
- **Categories:** cs.LG, cs.CR


> The paper introduces **CTFusion**, a novel streaming evaluation framework that uses live Capture‑The‑Flag (CTF) events to reliably benchmark LLM‑driven cybersecurity agents. By enforcing per‑agent isolation under a single team account and forwarding only the first correct flag for each challenge, CTFusion eliminates data‑contamination and cheating that plague existing static CTF benchmarks; it is implemented as a Model Context Protocol (MCP) server on the popular CTFd platform, making it easy to plug into any live CTF. Experiments with three LLMs, two agent architectures, and five live CTFs show that traditional CTF benchmarks give misleading performance scores, whereas CTFusion provides consistent, robust assessments of agentic AI capabilities in security tasks.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) have enabled agentic systems for complex, multi-step tasks; cybersecurity is emerging as a prominent application. To evaluate such agents, researchers widely adopt Capture The Flag (CTF) benchmarks. However, current CTF benchmarks reuse existing challenges, which exposes them to data contamination and potential cheating. Notably, we confirmed these issues in practice by integrating web search tools into an existing agent. To address these limitations, we present CTFusion, a streaming evaluation framework built on Live CTFs. To achieve this, CTFusion preserves per-agent independence under a single team account and reduces competition impact by forwarding only the first correct flag per challenge. Moreover, we implement CTFusion as a Model Context Protocol (MCP) server on the widely used CTFd platform, which offers broad applicability to diverse CTF events and agent types. Through experiments with three LLMs, two agents, and five Live CTFs, we demonstrate that existing CTF benchmarks can be unreliable in assessing LLM-based agents, while CTFusion can serve as a robust solution for evaluating cybersecurity agents. We release CTFusion as open source to foster future research in this area.

</details>


### 175. Distance-Constrained Unlabeled Multi-Agent Pathfinding

- **Authors:** Takahiro Suzuki, Yuma Tamura, Keisuke Okumura
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11503v1](http://arxiv.org/abs/2605.11503v1)
- **PDF:** [https://arxiv.org/pdf/2605.11503v1](https://arxiv.org/pdf/2605.11503v1)
- **Categories:** cs.MA


> The paper introduces **Distance‑\(r\) Independent Unlabeled Multi‑Agent Pathfinding (D‑r‑MAPF)**, a new variant of unlabeled MAPF in which agents must remain at least \(r\!+\!1\) vertices apart at all times—a realistic safety constraint absent from classic MAPF. The authors prove that, unlike standard unlabeled MAPF where feasibility is polynomial‑time decidable, D‑r‑MAPF feasibility is PSPACE‑complete, and they respond with two algorithmic families: (1) **reduction‑based optimal solvers** that compress the state space without losing feasibility, and (2) **configuration‑generator search** methods that explore feasible agent configurations directly. Experiments on grid and road‑network graphs demonstrate that both approaches can compute collision‑free, distance‑constrained schedules for hundreds of agents within seconds, establishing a practical baseline for safety‑aware, agentic AI coordination.


<details>
<summary>Abstract</summary>

We study a graph pathfinding problem Distance-$r$ Independent Unlabeled Multi-Agent Pathfinding, finding a set of collision-free paths between two sets where agents must stay at pairwise distance at least $r+1$ at all times. This additional constraint, generalizing collision modeling for classical MAPF, targets aspects of real-world multi-agent coordination. This additional distance constraint makes feasibility (i.e., whether a solution exists) PSPACE-complete, in contrast to standard (unlabeled) MAPF, where it can be decided in polynomial time. We address the challenge via two complementary approaches: (i) reduction-based optimal algorithms with a feasibility-preserving compression procedure, and (ii) a configuration generator-based search. Despite the hardness, empirical results show that our algorithm can handle hundreds of agents in a practical timeframe.

</details>


### 176. Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents

- **Authors:** Partha Madhira
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11487v1](http://arxiv.org/abs/2605.11487v1)
- **PDF:** [https://arxiv.org/pdf/2605.11487v1](https://arxiv.org/pdf/2605.11487v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> The paper introduces a **portable authorization framework** that lets autonomous enterprise agents carry explicit, machine‑interpretable authority beyond mere identity, enabling secure, auditable interactions across organizational boundaries. By dissecting insurance‑claims and supply‑chain scenarios, the authors identify gaps in current IAM models and propose a layered design where agents bear issuer‑signed authorization payloads (expressed via a typed constraint algebra) that are evaluated consistently by any enforcement engine, supporting delegation attenuation, semantic governance, fail‑closed behavior, and pre‑flight discovery. Prototype implementations using existing token formats (JWT/JWS, Verifiable Credentials, OAuth‑RARC) demonstrate that the model preserves a unified meaning of permissions while remaining interoperable with existing trust infrastructures—providing a concrete path toward standardized, revocable authority for agentic AI systems.


<details>
<summary>Abstract</summary>

Enterprise AI is shifting from copilots to autonomous agents capable of executing workflows, negotiating outcomes, and making decisions with limited human oversight. As these systems extend across organizational boundaries, identity alone is insufficient: an agent's authority must also be explicit, constrained, auditable, revocable, and consistently interpretable by independent receivers. This paper analyzes representative enterprise use cases in insurance claims processing and supply chain integrity to surface structural gaps in existing identity and access models. It proposes a portable authorization model for autonomous agents based on issuer-authored authorization payloads, typed constraint algebra, decision-consistent evaluation semantics, delegation attenuation, governed semantic resolution, fail-closed processing, and pre-flight discovery. The model separates credential containers, authorization payload semantics, and enforcement engines, allowing profiles such as JWT/JWS, Verifiable Credentials, OAuth Rich Authorization Requests, or policy-engine bindings to preserve a common authorization meaning across trust boundaries.

</details>


### 177. Robust Multi-Agent Path Finding under Observation Attacks: A Principled Adversarial-Plus-Smoothing Training Recipe

- **Authors:** Riad Ahmed
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11469v1](http://arxiv.org/abs/2605.11469v1)
- **PDF:** [https://arxiv.org/pdf/2605.11469v1](https://arxiv.org/pdf/2605.11469v1)
- **Categories:** cs.LG


> The paper introduces two adversarial‑robust training recipes—Adv‑PPO and Adv‑PPO + MACER—that improve the resilience of a shared neural policy for decentralized multi‑agent path‑finding (MAPF) against observation attacks, while keeping the same network architecture and deployment loop. Adv‑PPO augments Proximal Policy Optimization with worst‑case input perturbations and selects checkpoints based on adversarial performance; Adv‑PPO + MACER further fine‑tunes the checkpoint with a smoothing‑based loss derived from randomized‑smoothing certified radii. Experiments on the POGEMA benchmark (8×8 maps, four agents) show that the baseline PPO drops from 95.8 % clean success to 2.5 % under strong attacks, whereas Adv‑PPO recovers to 59.2 % and Adv‑PPO + MACER to 77.5 % worst‑case success with less than a 1 % loss in clean‑environment performance.


<details>
<summary>Abstract</summary>

Decentralized multi-agent path finding (MAPF) routes a team of agents on a shared grid, each acting from its own local view. The standard solution trains one shared neural policy with Proximal Policy Optimization (PPO), a popular on-policy reinforcement learning algorithm. Such a policy works well on clean observations, but a small input perturbation on one agent often changes its action, which then blocks a neighbour, and the team jams. In this paper we present two training recipes that keep the same network and the same deployment loop, yet make the policy hold up under perturbed observations. The first recipe, Adv-PPO, trains the shared policy against worst-case perturbations of its own input and selects the checkpoint by performance under adversarial perturbation. The second recipe, Adv-PPO+MACER, fine-tunes that checkpoint with a small on-policy smoothness term whose gradient follows the certified radius of randomized smoothing. On POGEMA with 8x8 maps and four agents, the unprotected PPO policy reaches 95.8% clean success but only 2.5% under the strongest attack. Adv-PPO recovers worst-case success to 59.2% at one percentage point of clean cost. Adv-PPO+MACER recovers it to 77.5% +/- 6.0% across three independent seeds at less than one percentage point of clean cost. We support these numbers with per-attack curves, a certified action-stability sanity check (which measures the smoothed-policy wrapper, not the deployed argmax policy), and side-by-side rollout storyboards that show the failure mode and the fix inside one environment instance.

</details>


### 178. Predictive Maps of Multi-Agent Reasoning: A Successor-Representation Spectrum for LLM Communication Topologies

- **Authors:** Ethan Parks, Dalal Alharthi
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11453v2](http://arxiv.org/abs/2605.11453v2)
- **PDF:** [https://arxiv.org/pdf/2605.11453v2](https://arxiv.org/pdf/2605.11453v2)
- **Categories:** cs.MA, cs.AI, cs.LG, cs.SI, math.SP


> **Contribution:**  
The paper proposes a pre‑inference structural diagnostic for multi‑agent LLM systems that predicts how a chosen communication topology (chain, star, mesh, etc.) will affect error drift, consensus formation, and robustness to perturbations.  

**Methodology:**  
It models the communication graph as a row‑stochastic operator P and computes its successor representation \(M=(I-\gamma P)^{-1}\). Three spectral quantities of M—spectral radius \(ρ(M)\), spectral gap \(Δ(M)\), and condition number \(κ(M)\)—are analytically derived for canonical topologies and empirically correlated with performance on a 12‑step state‑tracking task using Qwen2.5‑7B‑Instruct across 100 trials.  

**Key Findings:**  
- The condition number \(κ(M)\) perfectly ranks robustness to adversarial perturbations (Spearman \(r_s=1.0\)).  
- The spectral gap \(Δ(M)\) moderately predicts speed of consensus ( \(r_s=0.5\)).  
- The spectral radius \(ρ(M)\) is perfectly anti‑correlated with cumulative error ( \(r_s=-1.0\)), a reversal explained by bias drift that linear spectra miss; an affine‑noise extension to the successor map restores the expected ordering.  

These results introduce a drift‑aware, spectral‑based diagnostic that can guide the design of communication topologies for agentic LLM deployments before runtime evaluation.


<details>
<summary>Abstract</summary>

Practitioners deploying multi-agent large language model (LLM) systems must currently choose between communication topologies such as chain, star, mesh, and richer variants without any pre-inference diagnostic for which topology will amplify drift, converge to consensus, or remain robust under perturbation. Existing evaluation answers these questions only post hoc and only for the task measured. We introduce a structural diagnostic for multi-agent LLM communication graphs based on the successor representation $M = (I - γP)^{-1}$ of the row-stochastic communication operator, and we connect three of its spectral quantities, the spectral radius $ρ(M)$, the spectral gap $Δ(M)$, and the condition number $κ(M)$, to three distinct failure modes. We derive closed-form spectra for the chain, star, and mesh under row-stochastic normalization, and validate the predictions on a 12-step structured state-tracking task with Qwen2.5-7B-Instruct over 100 independent trials. The condition number is a perfect rank-order predictor of empirical perturbation robustness ($r_s = 1.0$); the spectral gap partially predicts consensus dynamics ($r_s = 0.5$); and the spectral radius is perfectly \emph{inverted} with respect to cumulative error ($r_s = -1.0$). We trace this inversion to a regime in which linear spectra are blind to non-contracting bias drift, and we propose an affine-noise extension of the predictive map that recovers the empirical ordering. We read this as a first step toward representational, drift-aware structural diagnostics for multi-agent LLM systems, sitting alongside classical spectral and consensus theory.

</details>


### 179. Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection

- **Authors:** Zi Liang, Ronghua Li, Yanyun Wang, Qingqing Ye, Haibo Hu
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11442v1](http://arxiv.org/abs/2605.11442v1)
- **PDF:** [https://arxiv.org/pdf/2605.11442v1](https://arxiv.org/pdf/2605.11442v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> **Contribution:** The paper introduces *Mobius Injection*, a previously unknown attack that turns LLM‑based autonomous agents into “zombie” nodes capable of launching agent‑oriented DDoS (AbO‑DDoS) floods by exploiting a logical flaw called **Semantic Closure**.  

**Methodology:** The authors craft a single malicious textual payload that triggers uncontrolled recursive calls inside the agent’s reasoning components. They evaluate the attack on six widely used agent frameworks (three “claw‑style” and three coding agents) interfaced with 12 state‑of‑the‑art proprietary or open‑weight LLMs, measuring call amplification, latency inflation, and scalability as the number of poisoned nodes grows.  

**Key Findings:** Mobius Injection is lightweight, evades standard DDoS detectors and AI safety filters, and can amplify a single node’s outbound calls by up to **51×** and inflate 95th‑percentile latency across a cluster by **229×**, with super‑linear degradation as more agents are compromised. The authors also propose a defensive technique—**Agent Component Energy (ACE) Analysis**—that monitors the energy flow in an agent’s component graph to spot anomalous recursive activity.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents have emerged as key intermediaries, orchestrating complex interactions between human users and a wide range of digital services and LLM infrastructures. While prior research has extensively examined the security of LLMs and agents in isolation, the systemic risk of the agent acting as a disruptive hub within the user-agent-service chain remains largely overlooked. In this work, we expose a novel threat paradigm by introducing Mobius Injection, a sophisticated attack that weaponizes autonomous agents into zombie nodes to launch what we define as gent-based and -Oriented DDoS (AbO-DDoS) attacks. By exploiting a structural vulnerability in agentic logic named Semantic Closure, an adversary can induce sustained recursive execution of agent components through a single textual injection. We demonstrate that this attack is exceptionally lightweight, stealthy against both traditional DDoS monitors and contemporary AI safety filters, and highly configurable, allowing for surgical targeting of specific environments or model providers. To evaluate the real-world impact, we conduct extensive experiments across three representative claw-style agents and three mainstream coding agents, integrated with 12 frontier proprietary or open-weight LLMs. Our results demonstrate that Mobius Injection achieves substantial attack success across diverse tasks, driving single-node call amplification up to 51.0x and multi-node p95 latency inflation up to 229.1x. The attack performance exhibits a superlinear increase with the number of poisoning nodes. To mitigate Mobius Injection, we propose a proactive defense mechanism using Agent Component Energy (ACE) Analysis, which detects malicious recursive triggers by measuring anomalous energy in the agent's component graph.

</details>


### 180. Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty

- **Authors:** Joykirat Singh, Zaid Khan, Archiki Prasad, Justin Chih-Yao Chen, Akshay Nambi, Hyunji Lee, Elias Stengel-Eskin, Mohit Bansal
- **Published:** 2026-05-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2605.11436v1](http://arxiv.org/abs/2605.11436v1)
- **PDF:** [https://arxiv.org/pdf/2605.11436v1](https://arxiv.org/pdf/2605.11436v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution** – The paper introduces **Agent‑BRACE**, a framework that explicitly separates belief tracking from action selection in LLM‑based agents operating in long‑horizon, partially observable environments. The belief component represents the posterior over world states as a set of natural‑language facts each tagged with a verbal certainty level, while a separate policy component conditions on this compact belief rather than the entire interaction history.

**Methodology** – Agent‑BRACE jointly trains two models via reinforcement learning: (1) a **belief‑state model** that abstracts raw observations and actions into structured NL claims with ordinal confidence labels (“certain”, “likely”, “unknown”, etc.), and (2) a **policy model** that takes the belief set as input and outputs actions. By extracting a belief representation at each step, the context length remains constant regardless of episode length.

**Key findings** – On several long‑horizon embodied language tasks, Agent‑BRACE improves success rates by **~14.5 % with Qwen2.5‑3B‑Instruct** and **~5.3 % with Qwen3‑4B‑Instruct** over strong RL baselines, while keeping the LLM’s context window essentially fixed. Calibration analysis shows the verbalized confidence scores become increasingly accurate as more evidence accumulates, demonstrating effective uncertainty tracking for agentic AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed on long-horizon tasks in partially observable environments, where they must act while inferring and tracking a complex environment state over many steps. This leads to two challenges: partial observability requires maintaining uncertainty over unobserved world attributes, and long interaction history causes context to grow without bound, diluting task-relevant information. A principled solution to both challenges is a belief state: a posterior distribution over environment states given past observations and actions, which compactly encodes history for decision making regardless of episode length. In LLM agents, however, the open-ended nature of text makes it unclear how to represent such a distribution. Therefore, we introduce Agent-BRACE: Agent Belief state Representation via Abstraction and Confidence Estimation, a method that decouples an LLM agent into a belief state model and a policy model, jointly optimized via reinforcement learning. The belief state model produces a structured approximation of the belief distribution: a set of atomic natural language claims about the environment, each annotated with an ordinal verbalized certainty label ranging from certain to unknown. The policy model conditions on this compact, structured approximate belief rather than the full history, learning to select actions under explicit uncertainty. Across long-horizon, partially observable embodied language environments, Agent-BRACE achieves an average absolute improvement of +14.5% (Qwen2.5-3B-Instruct) and +5.3% (Qwen3-4B-Instruct), outperforming strong RL baselines while maintaining a near-constant context window independent of episode length. Further analysis shows that the learned belief becomes increasingly calibrated over the course of an episode as evidence accumulates.

</details>



## Biorxiv (1 papers)


### 1. Reduced synaptic plasticity and E/I imbalance drive Peripersonal Space boundaries expansion in Schizophrenia

- **Authors:** Paredes, R., Grigoras, V., Ferroni, F., Ardizzi, M., Ferri, F., Series, P.
- **Published:** 2026-05-12
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2024.07.21.604515](https://doi.org/10.1101/2024.07.21.604515)

- **Categories:** neuroscience


> **Main contribution:** The paper provides a computational account of why schizophrenia (SCZ) patients show a narrowed yet still plastic peripersonal‑space (PPS) representation, showing that abnormal excitation‑inhibition (E/I) balance and reduced feed‑forward synaptic density alone cannot explain the impaired PPS expansion after tool use.  

**Methodology:** The authors built a biologically‑inspired PPS neural network model incorporating Hebbian learning, fitted it to behavioral PPS measurements before and after a tool‑use training protocol, and systematically manipulated the model’s learning rate, forgetting rate, and plasticity threshold to mimic SCZ‑related synaptic alterations.  

**Key findings:** PPS can still expand in the model despite E/I imbalance or lower synaptic density, but matching the patients’ limited post‑training expansion requires a *reduction* in synaptic plasticity (via slower learning, faster forgetting, or a higher plasticity threshold). This suggests that dysfunctional Hebbian plasticity, rather than static E/I dysregulation, underlies PPS abnormalities in SCZ and motivates experiments that track PPS changes in real time to differentiate among these mechanistic hypotheses.


<details>
<summary>Abstract</summary>

Abnormal encoding of peripersonal space (PPS) is believed to affect bodily self disruptions in schizophrenia (SCZ). Empirical studies show that SCZ patients exhibit a narrower PPS than controls but maintain its plasticity. Computational research links this smaller PPS to increased excitation of sensory neurons and reduced feedforward synaptic density. However, it is unclear how such differences influence learning during the expansion of PPS boundaries. We hypothesise that Hebbian plasticity can account for PPS expansion after active tool use training. To explore the effect of such mechanisms on PPS plasticity, we developed a SCZ network model which was fit to behavioural data before and after tool manipulation. We found that PPS expansion occurs in spite of E/I imbalance or reduced synaptic density, but does not match the post-training PPS representation of patients. A better fit was obtained after altering plasticity by either reducing the learning rate, increasing the forgetting rate or increasing the plasticity threshold. We discuss our findings in terms of dysfunctional plasticity in SCZ and highlight the key challenges in identifying the neurobiological correlates of reduced plasticity within PPS networks. Because current empirical data supports multiple viable mechanisms, we propose experiments to distinguish between the proposed plasticity accounts and clarify mixed findings on PPS representation in SCZ.

Graphical Abstract

O_FIG O_LINKSMALLFIG WIDTH=200 HEIGHT=123 SRC="FIGDIR/small/604515v2_ufig1.gif" ALT="Figure 1">
View larger version (34K):
org.highwire.dtl.DTLVardef@14ee71forg.highwire.dtl.DTLVardef@127c3aborg.highwire.dtl.DTLVardef@19f1338org.highwire.dtl.DTLVardef@a6e437_HPS_FORMAT_FIGEXP  M_FIG C_FIG HighlightsO_LIUsing a peripersonal space network model, we found that PPS expansion after tool-use occurs in spite of E/I imbalance or reduced synaptic density.
C_LIO_LIReduced feedforward synaptic plasticity is required to match the post-training PPS representation of patients.
C_LIO_LISuch reduction of synaptic plasticity could be achieved by either reducing the learning rate, increasing the forgetting rate or increasing the plasticity threshold relative to a healthy control model.
C_LIO_LIOur model predicts that measuring PPS at intermediate time points during a longer stimulation protocol would help distinguish between these plasticity differences.
C_LI

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*