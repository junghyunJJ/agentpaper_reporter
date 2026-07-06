# Weekly AI Agent Paper Report

**Generated:** 2026-07-06 13:29
**Period:** 2026-06-29 to 2026-07-05

## Summary

- **Total papers fetched:** 693
- **Papers matching keywords:** 148
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-06-29) | Change |
|--------|-----------|-----------|--------|
| Total matched | 148 | 141 | +7 |
| arxiv | 147 | 138 | +9 |
| biorxiv | 1 | 1 | +0 |
| medrxiv | 0 | 2 | -2 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (1 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. GeneBench-Pro: Evaluating Multistage Statistical Reasoning in Genomics, Quantitative Biology, and Translational Biomedicine

- **Authors:** Li, J. H., Ho, A. J.
- **Published:** 2026-06-30
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.29.735386](https://doi.org/10.64898/2026.06.29.735386)

- **Categories:** genomics


> **Main contribution:** GeneBench‑Pro extends the original GeneBench benchmark to a more challenging, domain‑wide suite (129 problems across genomics, quantitative biology, and translational biomedicine) that requires AI agents to carry out multi‑stage, inference‑heavy scientific workflows and arrive at concrete, decision‑critical quantitative conclusions.

**Methodology:** Each task supplies only brief context and a target estimand; the agent must navigate a series of dependent decision points—choosing data sources, statistical models, and validation steps—where a single wrong fork derails the downstream analysis. The problems were curated and validated by external domain experts, with a mix of publicly released, held‑out, and internal test items for unbiased evaluation.

**Key findings:** Even the most advanced GPT‑5.6 variants solve only about one‑third of the problems (≈31 % pass rate), while older GPT models and Claude Opus lag behind (8–16 %). Models frequently recognize local diagnostic cues but fail to propagate their implications, leading to incorrect estimator selection or dead‑end analysis paths, highlighting that long‑horizon, multistage statistical reasoning in biological domains remains an unreliable capability for current agentic AI systems.


<details>
<summary>Abstract</summary>

We introduce GeneBench-Pro, an expanded and improved version of GeneBench that comprises harder problems across a wider breadth of domains. GeneBench-Pro is a benchmark for AI agents performing realistic multi-stage scientific analyses in genomics, quantitative biology, and translational biomedicine which seeks to capture the complexity of real-world problems that computational life scientists face when tasked with producing a conclusion upon which a downstream scientific or translational decision is contingent. The benchmark comprises 129 evaluations targeting quantities of direct practical relevance across 10 primary domains and 21 terminal subdomains, with a genomics-centered core. Similarly to GeneBench, each problem provides the agent with brief context, a target estimand, and minimal guidance otherwise; the agent must then navigate multiple dependent decision points; i.e., substantive inferential forks where a plausible wrong choice changes the downstream analysis, to identify and execute the correct analysis workflow and arrive at the correct answer. Relative to GeneBench, GeneBench-Pro adds 29 new problems, drops three, and introduces significantly redesigned versions of 54 of the remaining 100 overlapping problems. 82 of the 129 problems were reviewed by external domain experts, whose findings led to prompt/data modifications and redesign of those problems whose targets were not sufficiently identifiable. Ten externally reviewed problems are released publicly, 50 held-out problems were provided to Artificial Analysis for independent third-party model benchmarking, and the remainder are retained as an internal holdout. In evaluations over the full 129-problem suite, GPT-5.6 Sol reaches an eval-level pass rate of 28.7% at the max reasoning level, and GPT-5.6 Sol Pro reaches 31.5% in separately reported GPT Pro runs. GPT-5.5 reaches 12.0%, GPT-5.4 reaches 8.9%, and the strongest non-GPT baseline, Claude Opus 4.8, reaches 16.0%. As with GeneBench, models often complete substantial portions of the workflow but exhibit a consistent gap between noticing and acting by identifying local diagnostic signals but failing to propagate the implications to the corresponding analysis decision. As a result, models often select wrong estimators or persist on initially plausible but incorrect analysis paths. GeneBench-Pro therefore measures an emerging capability of long-horizon biological reasoning that remains unreliable.

</details>


---



## Arxiv (147 papers)


### 1. What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates

- **Authors:** Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, Shahriar Noroozizadeh
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02507v1](http://arxiv.org/abs/2607.02507v1)
- **PDF:** [https://arxiv.org/pdf/2607.02507v1](https://arxiv.org/pdf/2607.02507v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR responses that are recorded but never shown to the other participant. Across 10 models, 3 scenarios, and 5 variations within each scenario, alignment-inducing settings produce systematic public-OTR divergence in the targeted agent, with its decision divergence rising from a $\sim$3% baseline to roughly 40%. The effect is consistent across four aggregate analyses: stance, semantic similarity, natural language inference, and survey responses. In some cases, the OTR response explicitly attributes public accommodation to relational pressures, such as career risk or sponsorship obligation. The findings suggest that agent evaluation should extend beyond explicit goals and detect emergent objectives. We present a dual-channel evaluation framework and complementary behavioral measures that operationalize this assessment.

</details>


### 2. Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas

- **Authors:** Yuxuan Li, Lingxi Xie, Xinyue Huo, Jihao Qiu, Jiacheng Shao, Pengfei Chen, Jiannan Ge, Kaiwen Duan, Qi Tian
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02504v1](http://arxiv.org/abs/2607.02504v1)
- **PDF:** [https://arxiv.org/pdf/2607.02504v1](https://arxiv.org/pdf/2607.02504v1)
- **Categories:** cs.CL, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integration of auditory, linguistic, and visual cues for speaker recognition. (2) We propose \textbf{DramaSR-LRM}, a robust approach built upon a large reasoning model (LRM). DramaSR-LRM is designed to autonomously aggregate contextual evidence via multimodal tool-use, synthesizing diverse inputs to achieve high-fidelity attribution. Experimental results demonstrate that DramaSR-LRM significantly outperforms existing baselines, particularly on short utterances where acoustic biometrics are inherently unreliable. \textit{All the data and code will be made publicly available at the project page: https://www.github.com/198808xc/DramaSR-LRM.}

</details>


### 3. Controllable Sim Agents with Behavior Latents

- **Authors:** Juanwu Lu, Junyu Zhu, Ziran Wang
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02496v1](http://arxiv.org/abs/2607.02496v1)
- **PDF:** [https://arxiv.org/pdf/2607.02496v1](https://arxiv.org/pdf/2607.02496v1)
- **Categories:** cs.RO, cs.LG


> The paper introduces **Controllable Neural Variational Agents (CNeVA)**, a framework for traffic‑simulation agents that jointly learns realistic behavior from logged data and exposes interpretable, per‑channel control axes (e.g., speed, acceleration, safety). CNeVA infers a Gaussian behavior latent for each agent via a closed‑form conjugate variational update on discounted returns, conditions a rectified‑flow trajectory generator with a mixed channel‑mask curriculum, and employs soft eligibility gates to retain gradient information near reward thresholds. Experiments on the Waymo Open Motion Dataset show that CNeVA matches state‑of‑the‑art realism while providing monotonic, steerable control over speed, acceleration, and safety without reward‑hacking, highlighting the importance of coupling controllability with physical‑plausibility safeguards in agentic AI.


<details>
<summary>Abstract</summary>

Realistic traffic simulation requires agents that imitate logged behavior and can also be steered along interpretable axes. Such controllability enables engineers to isolate variables, reproduce specific edge cases, and test autonomous systems without real-world risk. We introduce Controllable Neural Variational Agents (CNeVA), a controllable simulated-agent framework that learns to infer a per-agent Gaussian behavior latent from per-channel discounted returns via a closed-form conjugate variational update, conditioning a rectified-flow trajectory generator trained on a mixed channel-mask curriculum for classifier-free guidance. To tackle scarcity in reward signals, we propose soft eligibility gates that replace hard binary thresholds with smooth exponential decay, preserving the gradient signal for near-threshold agents. On the Waymo Open Motion Dataset, CNeVA attains competitive realism on the benchmark while exposing per-channel controllability that the higher-ranked imitation models lack. Speed- and acceleration-based steering produces monotone responses without stall-induced reward hacking. Safety controllability is monotone and substantial with the introduction of soft eligibility. We manage to achieve steerable map compliance under a context-residual return measure. Furthermore, our experiment demonstrates that steering metrics must be read alongside physical-plausibility guardrails to avoid reward-hacking confounds.

</details>


### 4. Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks

- **Authors:** Xi Zhang, Papi Menon, Vivian Chu, Koray Cosguner
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02453v1](http://arxiv.org/abs/2607.02453v1)
- **PDF:** [https://arxiv.org/pdf/2607.02453v1](https://arxiv.org/pdf/2607.02453v1)
- **Categories:** cs.MA


> The paper introduces a data‑driven assessment of open‑source multi‑agent frameworks, arguing that conventional popularity cues (e.g., GitHub stars) are poor proxies for ecosystem health. By mining 808 k stars, 74 k pull requests, 86 k commits and nearly one million user profiles across 15 frameworks from late‑2022 to early‑2026, the authors devise three health metrics—contributor density, cross‑ecosystem contribution, and early‑stage retention—and show that frameworks with modest star counts (e.g., Pydantic‑AI) often achieve higher contributor density, while high‑visibility projects like AutoGPT suffer low conversion of stars to active contributors; LangChain functions as a shared infrastructure attracting 82.5 % of cross‑framework contributors. The findings suggest that agents‑engineers should prioritize these nuanced metrics over raw star counts when selecting or investing in agentic AI frameworks.


<details>
<summary>Abstract</summary>

Since ChatGPT's launch in November 2022, open-source agentic frameworks have proliferated, making framework selection important for engineering teams while obscured by popularity signals such as GitHub stars. This paper analyzes 15 major open-source AI agent framework repositories from late 2022 to early 2026, using 808,042 stars, 73,997 pull requests, 86,241 commits, and 987,330 user profiles to assess ecosystem health across awareness, adoption, and retention. Three findings emerge. First, headline popularity is unreliable. Star counts reflect hype cycles and inorganic activity. AutoGPT gained 111,967 stars in one month but converted fewer than 9 contributors per 1,000 stars, defined as contributor density in this research, compared with LangChain's 41. Lower-profile frameworks such as Pydantic-AI show higher contributor density, indicating deeper adoption. Second, mapping awareness against adoption shows that visibility and engagement diverge. MetaGPT and LangFlow have contributor density ratios below 5 even with their high visibility. Openai-agents-python's limited contributor base suggests institutional backing alone does not ensure community depth. By analyzing cross-framework contribution, we discover that LangChain functions as a shared infrastructure, attracting 82.5% of cross-ecosystem contributors. Third, retention drops most steeply in the first 30 days of initial contribution and stabilizes near 90 days. Overall, ecosystem health is better measured by contributor density, cross-ecosystem engagement, and retention than by stars alone. These metrics offer teams a more robust basis for framework evaluation.

</details>


### 5. AgentsCAD: Automated Design for Manufacturing of FDM Parts via Multi-Agent LLM Reasoning and Geometric Feature Recognition

- **Authors:** Emmanuel George, Christopher Keefe, Peter Pak, Amir Barati Farimani
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02448v1](http://arxiv.org/abs/2607.02448v1)
- **PDF:** [https://arxiv.org/pdf/2607.02448v1](https://arxiv.org/pdf/2607.02448v1)
- **Categories:** cs.MA


> AgentsCAD introduces a multi‑agent pipeline that couples geometric analysis of STEP‑based CAD models with large‑language‑model (LLM) reasoning to automatically apply Design‑for‑Manufacturing (DFM) fixes for FDM printing. The system first parses the B‑Rep, builds a face‑adjacency graph, detects over‑hangs >45°, enriches the graph with semantic part tags using a GraphSAGE model trained on 59 k MFCAD++ parts, and then queries a Claude Sonnet LLM to generate concrete redesign actions (re‑orientation, fillets, chamfers, etc.); a GPT‑4o vision verifier checks the proposed geometry before outputting a corrected STEP file and report. Experiments on a birdhouse model show that the agents reliably identify problematic features, select appropriate mitigation strategies, and produce physically valid modifications, demonstrating a viable approach to bridging geometric CAD data with LLM‑driven design automation for agentic AI in additive manufacturing.


<details>
<summary>Abstract</summary>

Parts manufactured with Fused Deposition Modeling (FDM) often require Design for Additive Manufacturing (DFAM) modifications to ensure printability, structural integrity, and reduced post-processing. Current slicers identify defects such as steep overhangs but are unable to modify the underlying geometry. This work presents AgentsCAD, a multi-agent system that bridges raw boundary-representation (B-Rep) geometry and Large Language Model (LLM) reasoning to automate targeted DFM. The workflow begins by parsing a STEP file. The agentic system detects overhangs above a 45°threshold, constructs a face-adjacency topology graph, and optionally injects semantic feature labels from a GraphSAGE model trained on MFCAD++ (59,665 parts), before dispatching a Claude Sonnet design-reasoning agent that recommends reorientations, fillets, chamfers, and similar modifications. A GPT-4o vision-language verifier inspects rendered views to confirm geometric integrity. Outputs include a modified STEP file and a human-readable report. A test case on a birdhouse model demonstrates that the system correctly diagnoses overhangs, selects appropriate defect mitigation strategies, and proposes physically valid corrections, partially solving the geometry-to-language translation problem central to LLM-driven CAD modification.

</details>


### 6. EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments

- **Authors:** Zhilin Wang, Han Song, Runzhe Zhan, Jusen Du, Jiacheng Chen, Tianle Li, Qingyu Yin, Yulun Wu, Zhennan Shen, Tong Zhu, Yanshu Li, Guanjie Chen, Derek F. Wong, Yafu Li, Yu Cheng, Yang Yang
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02440v1](http://arxiv.org/abs/2607.02440v1)
- **PDF:** [https://arxiv.org/pdf/2607.02440v1](https://arxiv.org/pdf/2607.02440v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **Autonomous Policy Evolution** as a new evaluation paradigm in which a “harness‑model” agent continuously edits an executable policy within a fixed interaction budget, and implements it as the **EvoPolicyGym** benchmark comprising 16 compact interactive RL environments. Using this framework, the authors evaluate a suite of large language models (including GPT‑5.5) and show that GPT‑5.5 attains the highest aggregate rank and top‑two performance across all environments, while detailed trajectory diagnostics reveal that superior agents not only win individual tasks but also strategically allocate budget and translate feedback into effective parametric refinements. The work demonstrates that progress in agentic AI should be measured by iterative policy‑improvement behavior under bounded feedback rather than a single final score.


<details>
<summary>Abstract</summary>

Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended software-engineering progress. We introduce Autonomous Policy Evolution, a controlled evaluation setting in which a harness-model agent repeatedly edits an executable policy system under a fixed interaction budget. We instantiate this setting in EvoPolicyGym, a benchmark built from compact interactive RL environments that evaluates how agents iteratively improve explored policies. On the EvoPolicyGym suite, GPT-5.5 achieves the strongest aggregate rank score and top-two performance on all 16 environments. Beyond leaderboard results, EvoPolicyGym also provides trajectory-level diagnostics that distinguish how agents allocate budget, convert feedback into parametric tuning. These analyses show that strong autonomous policy evolution depends not only on isolated task wins, but on discovering task-appropriate mechanisms and refining policies under bounded feedback.

</details>


### 7. QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition

- **Authors:** Quoc Bao Phan, Tuy Tan Nguyen
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02426v1](http://arxiv.org/abs/2607.02426v1)
- **PDF:** [https://arxiv.org/pdf/2607.02426v1](https://arxiv.org/pdf/2607.02426v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid quantum-classical personalized FL framework for multi-agent activity recognition. The approach integrates a variational quantum circuit fusion module that models accelerometer--gyroscope interactions through quantum state encoding and entanglement, requiring only 72 quantum rotation parameters versus 33K in classical multi-layer perceptron-based fusion, achieving approximately 10x total parameter reduction. Experiments on the OPPORTUNITY dataset under subject-based non-IID partitions demonstrate 97.7% mean test accuracy, confirming that parameter-efficient quantum fusion remains competitive with conventional federated baselines.

</details>


### 8. HULAT2 at MER-TRANS 2026: Governed Multi-Agent Simplification for Spanish Easy-to-Read Generation

- **Authors:** Lourdes Moreno, Paloma Martínez, Marco Antonio Sanchez-Escudero, Miguel Domínguez-Gómez
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02381v1](http://arxiv.org/abs/2607.02381v1)
- **PDF:** [https://arxiv.org/pdf/2607.02381v1](https://arxiv.org/pdf/2607.02381v1)
- **Categories:** cs.CL


> **Main contribution** – The paper introduces a governed multi‑agent pipeline (built with LangGraph) for automatically generating Spanish Easy‑to‑Read (ETR) texts, and shows that a signal‑driven, parallel‑generation workflow can surpass a conventional generate‑evaluate‑regenerate baseline.

**Methodology** – Two principal runs (RUN1, RUN2) orchestrate Gemini 2.5 Flash and the open‑source RigoChat‑7B‑v2 as separate agents, using Event‑Condition‑Action routing, internal quality signals (semantic fidelity, readability, lexical simplicity, etc.), and controlled editing with traceable decisions; RUN2 adds a lexical‑support layer (glossary‑based lexical resources). RUN3 is a single‑agent baseline that employs prompt engineering and LoRA adaptation of RigoChat.

**Key findings** – On the MER‑TRANS 2026 Spanish ETR benchmark, the signal‑guided multi‑agent approach (RUN1) achieved the highest SARI score (44.05), outperforming the enhanced lexical‑support variant (RUN2, 43.10) and the baseline (RUN3, 38.51). The results demonstrate that multi‑agent routing with internal quality signals yields better simplification quality than linear regeneration, while simply adding lexical resources does not guarantee higher reference‑based metrics, highlighting the need for deeper segment‑ and document‑level readability and factual‑consistency analyses in agentic AI for ETR.


<details>
<summary>Abstract</summary>

This paper describes the participation of HULAT2-UC3M in the Spanish track of MER-TRANS 2026, a shared task on multilingual Easy-to-Read translation. Three fully automatic Spanish runs were submitted. RUN1 and RUN2 used a LangGraph-based multi-agent workflow combining Gemini 2.5 Flash and RigoChat-7B-v2, parallel generation strategies, internal quality signals, Event-Condition-Action routing, controlled editing and traceable decisions. RUN1 used the base workflow, while RUN2 activated an additional lexical-support layer based on a glossary and lexical resources. RUN3 was a RigoChat-based generate-evaluate-regenerate baseline with prompt engineering and LoRA-based adaptation. The official leaderboard reports BLEU-Orig, BLEU-Gold, SARI and BERTScore. During development, additional internal signals were also inspected, including semantic fidelity, readability, lexical simplicity, syntactic clarity and factual consistency. According to official SARI, RUN1 was the best HULAT2 run, with 44.0543 points, followed by RUN2 with 43.1049 and RUN3 with 38.5136. These results indicate that, in this task setting, signal-guided multi-agent routing outperformed the linear regeneration baseline. They also show that adding lexical support did not automatically improve reference-based scores. Further segment-level and document-level analysis are required to assess readability, factual consistency and user-oriented adequacy.

</details>


### 9. Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems

- **Authors:** Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02376v1](http://arxiv.org/abs/2607.02376v1)
- **PDF:** [https://arxiv.org/pdf/2607.02376v1](https://arxiv.org/pdf/2607.02376v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces a hardware‑enforced semantic coordination layer for safety‑critical real‑time autonomous systems, mapping the coordination primitives of the Topic‑Based Communication Space Petri Net (TB‑CSPN) onto FPGA logic so that synchronization, semantic gating, and authorization constraints are guaranteed deterministically at the hardware level. By offloading only the coordination semantics—not the adaptive reasoning—to dedicated FPGA primitives, the authors achieve bounded latency and verifiable enforcement of safety guarantees while retaining flexible, software‑driven AI components. Experiments show that this architecture eliminates the nondeterministic delays of pure software mediation and enables provably safe interaction among heterogeneous agentic modules in real‑time deployments.


<details>
<summary>Abstract</summary>

Recent advances in agentic AI are producing increasingly complex autonomous systems that integrate large language models, world models, optimization engines, specialized neural architectures, autonomous platforms, and human operators. While much current research focuses on improving reasoning capabilities, safety-critical real-time deployment also requires bounded and verifiable coordination among heterogeneous components operating concurrently under uncertainty. Software-mediated coordination presents fundamental limitations in domains where bounded latency, deterministic coordination, and enforceable safety guarantees are essential.
  Hence, we propose a hardware-enforced semantic coordination architecture in which selected coordination semantics are implemented directly at the hardware level via field-programmable gate arrays (FPGAs). The approach builds on the Topic-Based Communication Space Petri Net (TB-CSPN) framework, which separates semantic reasoning from interaction management.
  In this approach, selected TB-CSPN coordination mechanisms are mapped onto FPGA primitives, creating a hardware-native semantic coordination layer. Focus is not on acceleration, but on enforcing temporal synchronization, semantic gating, authorization constraints, and bounded coordination behavior directly in hardware. Semantic reasoning remains adaptive and software-driven, while embedded coordination semantics become deterministic.

</details>


### 10. AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents

- **Authors:** Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, Zizhen Li, Chuanhao Li, Xiangcheng Cao, Yihao Liu, Fanrui Zhang, Li Jin, Kaipeng Zhang
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02255v1](http://arxiv.org/abs/2607.02255v1)
- **PDF:** [https://arxiv.org/pdf/2607.02255v1](https://arxiv.org/pdf/2607.02255v1)
- **Categories:** cs.AI, cs.CL


> **Contribution:** The paper introduces **AgenticSTS**, a bounded‑memory testbed that isolates and evaluates individual memory layers for long‑horizon LLM agents by replacing the usual “append‑everything” context with a fresh, typed‑retrieval prompt for each decision.

**Methodology:** The authors implement this contract in the stochastic deck‑building game *Slay the Spire 2*, generating 298 fully logged game trajectories. Each decision’s prompt is assembled from selectively retrieved observations, tool calls, and reflections, allowing any memory component to be ablated or added in isolation. They benchmark several frontier LLM backbones against a human baseline and report detailed win‑rate comparisons for different memory‑layer configurations.

**Key Findings:** Even strong contemporary LLMs achieve 0 % win‑rate on the lowest‑difficulty setting, whereas humans win ≈ 16 %. Adding a “strategic‑skill” memory layer roughly doubles the win‑rate of a no‑store baseline (3/10 → 6/10), suggesting that explicit, targeted memory modules materially affect long‑horizon performance, though larger sample sizes are needed for statistical certainty. The released dataset and analysis scripts provide a reproducible platform for further research on how bounded, modular memory influences agentic AI behavior.


<details>
<summary>Abstract</summary>

Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw cross-decision transcript appended. The prompt thus stays bounded across runs of any length, and any single layer can be ablated in isolation. We instantiate the contract in Slay the Spire 2, a closed-rule stochastic deck-building game whose runs require hundreds of tactical and strategic decisions. A public online benchmark of frontier LLMs on the same game reports zero wins at the lowest difficulty across five configurations, and the developer-reported human win rate at the same difficulty is 16%; the task is hard but not saturated. Within our harness, a fixed-A0 ablation shows the largest observed difference when triggered strategic skills are enabled: the no-store baseline wins 3/10 games and adding the skill layer 6/10. At this sample size the comparison is directional rather than statistically decisive (Fisher exact p\approx0.37); a cross-backbone probe and public accumulating-context baselines are reported as operational comparisons rather than controlled tests of the contract variable itself. We release a reproducible testbed: 298 completed trajectories with condition tags, frozen memory/skill snapshots, prompt records, and analysis scripts -- an agent design and a validated, reusable methodology for studying how explicit memory layers shape long-horizon LLM-agent decisions.

</details>


### 11. Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support

- **Authors:** Seren Yenikent, Jack Vinijtrongjit, Katherine Ng
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02245v1](http://arxiv.org/abs/2607.02245v1)
- **PDF:** [https://arxiv.org/pdf/2607.02245v1](https://arxiv.org/pdf/2607.02245v1)
- **Categories:** cs.AI, cs.CY, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mental health disorders affect nearly one billion people globally, yet 75% of individuals in low- and middle-income countries receive no treatment due to workforce shortages, cost barriers, and stigma. Current AI-powered wellness solutions predominantly rely on single-mode conversational interfaces that suffer high abandonment rates and fail to provide measurable, immediate relief calibrated to users' dynamic emotional states. This paper presents Copewell, a novel multi-agent swarm system designed to expand access to mental wellness support through human-centered AI principles. Our architecture introduces three technical innovations: (1) a multi-source assessment framework integrating self-reported, physiological, and contextual data to mitigate algorithmic bias; (2) valence-arousal emotion mapping using Russell's Circumplex Model of Affect to route users to specialized AI agents; and (3) dual-mode intervention delivery combining conversational support with evidence-based sensory wellness protocols. We examine the sociotechnical design considerations underlying Copewell's development, including a privacy-first architecture, embedded ethical oversight through a dedicated Ethics Supervisor agent, and participatory design informed by mental health practitioners. Early practitioner engagement and beta deployment inform design decisions and identify directions for future empirical evaluation. This work contributes to responsible AI discourse by demonstrating how technical architecture can operationalize equity and safety principles from inception.

</details>


### 12. Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks

- **Authors:** Ravi Kant Sharma
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02210v1](http://arxiv.org/abs/2607.02210v1)
- **PDF:** [https://arxiv.org/pdf/2607.02210v1](https://arxiv.org/pdf/2607.02210v1)
- **Categories:** cs.AI, cs.NI


> The paper introduces **Guard Rail Validation (GRV)**, a standardized runtime layer for autonomous telecom networks that intercepts each AI/ML agent’s decision, assigns it a criticality score based on dimensions such as service importance, action reversibility, and autonomy level, and then applies a graduated set of safeguards (logging‑only, bounds checking, independent validator, or multi‑agent consensus) before the decision is enacted. The authors detail the GRV architecture, its integration into an O‑RAN environment, and an algorithmic conflict‑resolution scheme that prioritizes higher‑criticality actions while preserving regulatory audit trails (e.g., EU AI Act Art. 14). Empirical evaluation shows that GRV dramatically expands threat coverage—detecting and mitigating a broad range of known AI/ML attacks (data poisoning, adversarial inference, and rogue‑agent behavior)—while adding only minimal latency, demonstrating its feasibility as a guard‑rail mechanism for agentic AI in next‑generation autonomous networks.


<details>
<summary>Abstract</summary>

The evolution toward fully autonomous telecommunications networks (Autonomous Network Levels 4-5) requires AI/ML agents to make real-time network decisions without human intervention. However, no standardized runtime mechanism exists to intercept and validate individual inference outputs before they trigger live network state changes, creating risks of erroneous autonomous decisions. This paper proposes the Guard Rail Validation (GRV) framework, a standardizable runtime architecture for intercepting and validating AI-driven decisions before execution. The framework evaluates decisions across multiple weighted dimensions -- including action scope, action type, service criticality, agent autonomy level, reversibility, and temporal behavioural patterns -- to determine a criticality level. Based on this level, graduated validation mechanisms are applied: execute-with-logging, bounds checking, independent agent validation, or multi-agent consensus. The framework additionally provides cross-agent conflict detection with criticality-weighted priority resolution and runtime conformance logging for regulatory compliance (e.g., EU AI Act Article 14). We present the architecture, algorithmic procedures, O-RAN deployment model, and evaluate threat coverage against known AI/ML attacks in telecommunications.

</details>


### 13. UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development

- **Authors:** Temitayo Olamilekan Ogunsusi, Lijun Qian, Xishuang Dong
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02186v1](http://arxiv.org/abs/2607.02186v1)
- **PDF:** [https://arxiv.org/pdf/2607.02186v1](https://arxiv.org/pdf/2607.02186v1)
- **Categories:** cs.AI


> **Contribution:** UA‑ChatDev introduces uncertainty awareness into role‑based, multi‑LLM software‑development pipelines, mitigating the hallucination cascade that degrades downstream code quality.  

**Methodology:** The framework equips each agent with a lightweight token‑level log‑probability estimator to quantify response uncertainty, and applies phase‑specific confidence thresholds that trigger a retrieval‑based verification step only when uncertainty exceeds the calibrated limit, thereby filtering unreliable outputs before they propagate.  

**Findings:** On the SRDD benchmark, UA‑ChatDev surpasses prior single‑ and multi‑agent systems on completeness, executability, consistency, and overall quality, and ablation/communication analyses show that uncertainty‑driven gating markedly improves code execution reliability and reduces error propagation in agentic AI software development.


<details>
<summary>Abstract</summary>

Software development is a complex task that demands cooperation among agents with diverse roles. Large language models (LLMs) have enabled autonomous multi-agent software development frameworks that leverage role-based collaboration to automate requirements analysis, coding, testing, and refinement. However, existing approaches typically assume that intermediate agent outputs are equally reliable, leaving them vulnerable to hallucination propagation, where incorrect decisions generated in early development phases are transferred to downstream agents and negatively impact final software quality. To address this challenge, we propose UA-ChatDev, an uncertainty-aware multi-agent software development framework that integrates uncertainty quantification into agent interactions. It introduces a lightweight uncertainty estimation mechanism based on token-level log probabilities to assess the confidence of agent responses and employs phase-aware threshold calibration to selectively trigger retrieval-based verification when uncertainty exceeds acceptable levels. Extensive experiments on the SRDD benchmark demonstrate that UA-ChatDev consistently outperforms existing single-agent and multi-agent software development frameworks across completeness, executability, consistency, and overall quality metrics. Further ablation studies and communication analyses verify that uncertainty-aware interactions enhance code execution reliability.

</details>


### 14. ContextNest: Verifiable Context Governance for Autonomous AI Agent

- **Authors:** Misha Sulpovar, Benn R. Konsynski, Qaish Kanchwala, Gabe Goodhart
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02116v1](http://arxiv.org/abs/2607.02116v1)
- **PDF:** [https://arxiv.org/pdf/2607.02116v1](https://arxiv.org/pdf/2607.02116v1)
- **Categories:** cs.AI


> The paper introduces **ContextNext**, an open specification and reference implementation that adds a verifiable “governance layer” beneath Retrieval‑Augmented Generation, ensuring that every piece of external knowledge consumed by an autonomous AI agent is provenance‑tracked, version‑identified, integrity‑checked, and auditable. The methodology combines typed Markdown documents with SHA‑256 hash‑chained version histories, deterministic set‑algebraic selectors, and a Model Context Protocol (MCP) to expose contextnest:// URIs and audit trails, allowing agents to reconstruct exactly which vetted artifacts informed a given output. Empirical evaluations show that governed selection outperforms standard BM25 retrieval in a stale‑version attack (97 % vs. 90‑93 % answer‑quality pass rate) while using only one‑third the input tokens, and that deterministic selectors guarantee reproducible retrieval results (Jaccard = 1.0) unlike dense‑vector/HNSW baselines, demonstrating that context governance mitigates failure modes that pure retrieval cannot address.


<details>
<summary>Abstract</summary>

Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time reconstruction. We formalize this as context governance and present ContextNext, an open specification and reference implementation for governed AI-consumable knowledge vaults. ContextNext does not replace Retrieval-Augmented Generation (RAG); it supplies the governance layer beneath retrieval, determining which artifacts are approved, current, attributable, and integrity-verified before retrieval systems operate over them.
  The specification combines typed Markdown documents with metadata, deterministic set-algebraic selectors, contextnest:// URI references, SHA-256 hash-chained version histories, graph-level checkpoints, source nodes for live data through the Model Context Protocol (MCP), and audit traces of agent context consumption. These mechanisms let organizations reconstruct which knowledge versions informed an agent output and whether those versions were AI-eligible when consumed.
  We report first empirical results from two controlled experiments. In a stale-version attack isolating the governance-versus-retrieval failure mode, governed selection strictly Pareto-dominates BM25 sparse retrieval, with higher answer-quality pass rate (97% versus 93-90%) at about one-third the input-token cost. In a retrieval-determinism experiment over a 1,060-document corpus, deterministic selectors and BM25 return stable document sets across repeated identical queries (Jaccard 1.0), while a dense+HNSW baseline is non-deterministic on 80% of queries (mean Jaccard 0.611, worst case 0.210). These results suggest that context governance addresses failure modes retrieval quality alone is not designed to resolve. We release a core engine, CLI, and MCP server under open licenses.

</details>


### 15. Prompt Coverage Adequacy

- **Authors:** Florian Tambon, Michael Konstantinou, Cedric Richter, Charles Chenouard, Mark Harman, Mike Papadakis
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02057v1](http://arxiv.org/abs/2607.02057v1)
- **PDF:** [https://arxiv.org/pdf/2607.02057v1](https://arxiv.org/pdf/2607.02057v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **Prompt Coverage Adequacy**, a new test‑adequacy metric that evaluates how thoroughly a test suite exercises the intent expressed in LLM/agent prompts—analogous to code coverage but based on the model’s attention patterns over prompt tokens. The authors implement a lightweight “attention‑boosting” estimator of this metric and apply it to two benchmark datasets using several large language models, showing that tests guided by Prompt Coverage detect over 30 % more faults than tests guided by traditional code‑coverage criteria. These results suggest that prompt‑level coverage can become a core metric for testing in the emerging LLM‑driven, agentic software development paradigm.


<details>
<summary>Abstract</summary>

In recent years, it has become increasingly evident that large language models (LLMs) and autonomous agents raise the level of abstraction in software development by shifting the focus from writing precise procedures to expressing intents and goals. This paradigm shift introduces new challenges, particularly in how testing should be guided when prompts, rather than code, become primary development artifacts. To address this challenge, we propose Prompt Coverage Adequacy, a novel coverage criterion designed to support the testing of code generated from task descriptions. Prompt Coverage Adequacy serves as an analog to traditional code coverage, but operates at the level of prompts used in LLM and agent-based programming. Specifically, it measures how well a given test suite satisfies the requirements expressed in a prompt by leveraging the attention mechanisms of LLMs. We evaluate a simple instantiation of this criterion, based on attention boosting, across two datasets and multiple LLMs. Our results demonstrate that Prompt Coverage is associated with fault-detection effectiveness and can uncover over 30+% more faults than traditional code coverage when used to guide test generation. These findings suggest that Prompt Coverage Adequacy can serve as a foundation for developing testing metrics better suited to the emerging paradigm of LLM-driven software development, addressing the limitations of classical coverage criteria in this new context.

</details>


### 16. PACE: A Proxy for Agentic Capability Evaluation

- **Authors:** Yueqi Song, Lintang Sutawika, Jiarui Liu, Lindia Tjuatja, Jiayi Geng, Yunze Xiao, Daniel Lee, Aditya Bharat Soni, Vincent Lo, Xiang Yue, Graham Neubig
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.02032v1](http://arxiv.org/abs/2607.02032v1)
- **PDF:** [https://arxiv.org/pdf/2607.02032v1](https://arxiv.org/pdf/2607.02032v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution:** The paper introduces **PACE**, a framework that builds tiny “proxy” benchmarks capable of predicting how well large language‑model (LLM) agents will perform on costly, full‑scale agentic evaluations (e.g., SWE‑Bench, GAIA).

**Methodology:** PACE treats a large pool of atomic, non‑agentic test instances (reasoning, code generation, etc.) as features and learns a regression model that maps a model’s scores on a carefully selected subset of these instances to its score on a target agentic benchmark. The subset is chosen by blending *target‑relevance* (local selection of instances most correlated with the specific benchmark) and *global‑informativeness* (instances that are predictive across many models). The resulting proxy suite—**PACE‑Bench**—is evaluated via leave‑one‑out cross‑validation.

**Key findings:** Across 14 LLMs, 4 agentic benchmarks, and 19 non‑agentic benchmarks, PACE‑Bench predicts full agentic scores with **<4 % MAE**, **Spearman ρ > 0.80**, and **≈85 %** pairwise ranking accuracy, while costing **<1 %** of the original evaluation budget. Analysis of the selected instances also uncovers the distinct skill sets each agentic benchmark demands, showing that PACE can provide cheap, reliable estimates for model development, selection, and routing in the agentic AI domain.


<details>
<summary>Abstract</summary>

Evaluating LLM agents on benchmarks like SWE-Bench and GAIA can be expensive, time-consuming, and requires complex infrastructure. A single evaluation can cost thousands of dollars and take days to complete. In contrast, non-agentic LLM benchmarks that test individual capabilities (e.g., reasoning, code generation) are fast and cheap to run. In this paper, we investigate whether performance on expensive agentic benchmarks can be accurately predicted by the performance on a small, carefully selected subset of atomic evaluation instances. We introduce PACE, a framework that constructs proxy benchmarks by selecting instances from existing non-agentic evaluations whose aggregate scores most reliably predict model performances on agentic benchmarks. Given a pool of candidate instances spanning atomic capabilities, PACE fits a regression that maps a model's scores on a compact subset of source instances to its score on the target agentic benchmark. The subset itself is curated by combining two complementary instance-selection strategies, target-relevance local selection and globally informative global selection. We apply PACE to the 4 target agentic benchmarks in this paper, which yields PACE-Bench, the concrete proxy benchmark that we evaluate in the paper. Experiments across 14 models, 4 agentic benchmarks, and 19 non-agentic benchmarks show that PACE-Bench predicts agentic scores with leave-one-out cross-validation (LOOCV) mean absolute error (MAE) under 4%, Spearman correlation above 0.80, and pairwise model-ranking accuracy around 85%, all at much less than 1% of the full agentic evaluation cost. We further analyze the selected proxy instances, revealing which skills each agentic benchmark uniquely demands. PACE enables practitioners to obtain reliable estimates of agentic performance during model development, selection, and routing, without the overhead of full agent evaluation.

</details>


### 17. Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant

- **Authors:** Jiangdi Ru, Bing Li, Yage Huang, Ding Wang, Keru Hua
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01992v1](http://arxiv.org/abs/2607.01992v1)
- **PDF:** [https://arxiv.org/pdf/2607.01992v1](https://arxiv.org/pdf/2607.01992v1)
- **Categories:** cs.AI


> The paper introduces a traceable fault‑diagnosis assistant for large‑scale battery energy storage systems that combines a retrieval‑augmented multi‑agent architecture with schema‑constrained natural‑language database access and hybrid text‑image retrieval to fuse alarm streams, cell‑level telemetry, topology data, diagnostic tables, historical cases, and maintenance documents. By routing BESS‑specific tasks to specialized agents and synthesizing answers with explicit evidence citations, the system can pinpoint underlying issues such as voltage inconsistency, resistance drift, short‑circuit risk, capacity divergence, or thermal anomalies and automatically generate explanatory reports. Internal evaluations show that the task‑routing, constrained DB querying, and multi‑agent reasoning components substantially improve retrieval accuracy and diagnostic traceability, highlighting the approach’s potential for trustworthy, agentic AI‑driven O&M in energy storage.


<details>
<summary>Abstract</summary>

Large-scale battery energy storage systems (BESSs) require O&M decisions that combine alarms, cell-level measurements, device topology, diagnostic tables, historical cases, and maintenance documents. Monitoring platforms can flag threshold violations, but they often cannot explain whether voltage inconsistency, resistance drift, short-circuit risk, capacity divergence, or thermal abnormality needs intervention. This digest presents a traceable BESS fault-diagnosis assistant that uses retrieval-augmented multi-agent reasoning to connect operational data, domain knowledge, visual evidence, and report generation. Reliability is improved through BESS-specific task routing, schema-constrained natural-language database access, hybrid text-image retrieval, and evidence-based answer synthesis. Preliminary internal evaluation is reported for routing, database access, and diagnostic reasoning.

</details>


### 18. CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery

- **Authors:** Nicholas Tagliapietra, Gian Lorenzo Marchioni, Moritz Willig, Juergen Luettin, Lavdim Halilaj, Kristian Kersting
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01936v1](http://arxiv.org/abs/2607.01936v1)
- **PDF:** [https://arxiv.org/pdf/2607.01936v1](https://arxiv.org/pdf/2607.01936v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning causal models from high-dimensional data is a significant challenge, particularly in real-world settings where violations of core assumptions lead to causal identifiability issues. Although massive amounts of prior knowledge are available, and contain valuable causal information, effectively integrating this knowledge into the causal discovery process remains an open problem. We introduce CausalSTeward (CAST), a novel human-in-the-loop framework for interactively assembling large causal models. CausalSteward is a multi-agent collaborative system that tackles high-dimensional causality through a divide-and-conquer approach where large clusters of variables are iteratively partitioned and then separately analyzed. Our framework fuses prior knowledge with a data-driven approach by using tailored tools such as retrieval augmented generation and conditional independence tests. Finally, we use this work to examine the capabilities and limitations of causal reasoning in multi-agent frameworks, and how the human-in-the-loop can contribute to accurate and trustworthy results.

</details>


### 19. A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory

- **Authors:** Zitong Shi, Yixuan Tang, Anthony Kum Hoe Tung
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01935v1](http://arxiv.org/abs/2607.01935v1)
- **PDF:** [https://arxiv.org/pdf/2607.01935v1](https://arxiv.org/pdf/2607.01935v1)
- **Categories:** cs.AI


> **Main contribution** – The paper identifies “ghost memory”, a failure mode in long‑term LLM‑agent memory where outdated, current, and transitional facts become entangled and corrupt answers. To counter this, it introduces **A‑TMA**, a lightweight state‑aware overlay that (i) preserves superseded and transition records in the memory bank, (ii) assembles state‑specific evidence packets during retrieval, and (iii) feeds explicit current/historical/transition labels to the answer model.

**Methodology** – A‑TMA is built atop existing vector‑store memories (e.g., Graphiti) and operates at three decoupled levels: bank maintenance, retrieval, and answer‑time resolution. The authors also create **LTP (LoCoMo Temporal Plus)**, a benchmark rich in temporal conflicts, and evaluate each level separately to expose hidden ghost‑memory errors.

**Key findings** – On the conflict‑heavy LTP benchmark, Graphiti + A‑TMA raises conflict‑resolution accuracy by **+0.24** absolute points; on the broader LoCoMo suite, temporal F1 jumps from **0.0295 to 0.1705**. These results demonstrate that explicitly modelling the temporal state of facts can markedly reduce latent memory failures in agentic AI systems.


<details>
<summary>Abstract</summary>

Long term memory lets LLM agents act as persistent assistants, but user facts change. A useful memory system must know what is true now, what used to be true, and what changed. We study \emph{ghost memory}, a state coordination failure in which old, current, and transition facts coexist in the memory bank, remain mixed during retrieval, and mislead the answer model. We argue that memory systems should be understood and optimized from three levels: bank maintenance, retrieval, and answer time resolution. We propose ATMA, a state aware overlay for existing memory systems. ATMA keeps superseded and transition records in the bank, builds evidence packets for the query's requested state view, and exposes current, historical, and transition labels to QA. We further call for decoupled evaluation of bank, retrieval, and answer level failures, since final QA accuracy can hide where ghost memory occurs. To make this failure measurable, we build LTP (LoCoMo Temporal Plus), a conflict heavy benchmark for ghost memory, and evaluate on LoCoMo for long conversation generalization. On LTP, Graphiti+ATMA improves conflict accuracy by 0.240 absolute over Graphiti. On LoCoMo, Graphiti+ATMA raises temporal F1 from 0.0295 to 0.1705. The gains are host dependent, but they indicate that explicit state roles can reduce memory failures hidden by final QA accuracy.

</details>


### 20. SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use

- **Authors:** Jiayin Zhu, Kelong Mao, Yudong Guo, Dengbo He, Sulong Xu, Simiu Gu, Yutao Yue
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01874v1](http://arxiv.org/abs/2607.01874v1)
- **PDF:** [https://arxiv.org/pdf/2607.01874v1](https://arxiv.org/pdf/2607.01874v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Skills are becoming a reusable operational layer for LLM agents, encoding SOPs, domain rules, tool workflows, scripts, and validation routines. In realistic skill repositories, overlapping skills make reliable skill-use difficult. Final verifier success is too coarse for both evaluation and training, since an agent may pass through trial and error while selecting distractor skills, skipping required steps, composing workflows incorrectly or omitting final checks. We introduce SkillCoach, a self-evolving rubric framework for evaluating and enhancing agentic skill-use. SkillCoach derives skill-grounded process rubrics from real rollouts and evaluates trajectories along four dimensions: skill selection, skill following, skill composition, and skill-grounded reflection. It keeps the external verifier as a separate outcome signal, allowing process quality to be distinguished from accidental task success. The evolved rubrics further serve as process supervision for selecting high-quality training trajectories. Experiments show that evolved rubrics substantially improve evaluation quality, expose failures hidden by final accuracy, and provide stronger supervision signals than outcome-only filtering for enhancing agentic skill-use.

</details>


### 21. Congestion-Based Slot Pricing in a Railway Auction Game

- **Authors:** Bill Roungas, Sebastiaan Meijer
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01822v1](http://arxiv.org/abs/2607.01822v1)
- **PDF:** [https://arxiv.org/pdf/2607.01822v1](https://arxiv.org/pdf/2607.01822v1)
- **Categories:** cs.MA, cs.GT, econ.TH


> **Main contribution:** The paper introduces a novel, congestion‑sensitive slot‑pricing auction for railway networks that combines a dynamic base price (rising with total demand) with an asymmetric corrective term that penalises the agent requesting the most slots and rewards the one asking for the fewest, aiming to curb the market power of large operators while keeping the mechanism transparent.

**Methodology:** The authors model the interaction as a repeated incomplete‑information game and implement a real‑time, web‑based multi‑agent platform in which human participants play heterogeneous operator‑agents; they run two structured experimental sessions with domain experts, recording agents’ slot requests, price adjustments, and feedback signals.

**Key findings:** The congestion component correctly tracks aggregate demand and the corrective incentives are triggered as intended, yet large operators continue to over‑request slots despite penalties, indicating that the corrective pricing alone does not fully eliminate strategic dominance. Participants’ choices were driven more by their assigned operator role (e.g., preserving market presence, raising rivals’ costs) than by personal risk preferences, highlighting the need for stronger or additional mechanism features in asymmetric‑budget, multi‑agent settings.


<details>
<summary>Abstract</summary>

We present a multi-agent system for studying the allocation of discrete, congested resources among heterogeneous strategic agents, motivated by the problem of railway slot allocation under deregulation. Multiple operator-agents, differing in size and capacity, interact through a shared auction mechanism over repeated rounds under time-constrained decision-making. The mechanism combines a congestion-based base price that increases with aggregate demand with an asymmetric corrective adjustment that penalises the agent requesting the most slots and rewards the agent requesting the fewest, and is designed to mitigate strategic dominance by large agents while preserving transparency and congestion sensitivity. We formulate the interaction as a repeated game with incomplete information and implement the system as a real-time, web-based multi-agent environment in which human participants control individual agents and observe live marginal-cost and competitor feedback.
  We report exploratory observations from two structured sessions with domain experts acting as operator-agents. The congestion mechanism responds to aggregate demand as designed and the corrective incentives are actively triggered, but agents representing large operators persist with high-request strategies despite the penalty, suggesting that corrective pricing is necessary but not sufficient to neutralise strategic dominance in this multi-agent setting. A post-session debrief indicates that participants' decisions were driven by the assumed agent role rather than personal disposition, and provides qualitative support for strategic motives, such as preserving market presence and raising rivals' costs, operating alongside short-term profit maximisation. We discuss implications for multi-agent mechanism design under asymmetric budgets and outline directions for analytical validation and larger-scale multi-agent experiments.

</details>


### 22. MMBench-Live: A Continuously Evolving Benchmark for Multimodal Models

- **Authors:** Yuanzhi Liu, Shousheng Zhao, Bo Zhou, Kongming Liang, Zhanyu Ma
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01813v1](http://arxiv.org/abs/2607.01813v1)
- **PDF:** [https://arxiv.org/pdf/2607.01813v1](https://arxiv.org/pdf/2607.01813v1)
- **Categories:** cs.CV, cs.AI


> **Main contribution:** The paper introduces **MMBench‑Live**, a continuously updating multimodal benchmark that automatically generates new vision‑language evaluation instances through a multi‑agent pipeline, addressing the staleness, data‑contamination, and maintenance problems of static benchmarks.  

**Methodology:** The system treats benchmark evolution as a task‑guided data‑construction problem: a structured specification defines each task, agents acquire fresh image–text data in real time, and a verifier produces QA pairs with executable reasoning. To keep successive versions comparable, a distribution‑consistent update strategy extracts visual patterns from the original benchmark to guide data collection and filtering; each update costs ~ USD 30 and completes in 1–2 h.  

**Key findings:** MMBench‑Live adds 5.9 k high‑quality instances while preserving the original model ranking hierarchy, maintaining semantic alignment with MMBench, and reducing memorization signals from data contamination. This demonstrates a scalable, low‑cost approach for sustaining and evolving benchmarks for agentic, multimodal AI systems.


<details>
<summary>Abstract</summary>

Evaluation benchmarks are essential for assessing vision-language models (VLMs), but most multimodal benchmarks are static, making them vulnerable to temporal staleness, data contamination, and costly maintenance. We present MMBench-Live, a continuously evolving multimodal benchmark built by a multi-agent-driven automated pipeline. Our framework treats benchmark evolution as task-guided dataset construction, integrating structured benchmark specification, feedback-controlled real-time data acquisition, and verifiable QA generation with executable reasoning. To maintain cross-version comparability, we introduce a distribution-consistent update strategy that extracts task-related visual patterns from the original benchmark to guide data collection and filtering. Instantiated from MMBench, MMBench-Live contains 5.9K newly generated evaluation instances with a high answer correctness rate, while each update costs about USD 30 and takes 1-2 hours. Extensive evaluations show that MMBench-Live preserves stable model rankings, maintains semantic alignment with the original benchmark, and exhibits weaker contamination-related memorization signals, suggesting a practical and scalable paradigm for sustainable multimodal benchmark evolution. The project is available at https://github.com/PRIS-CV/MMBench-Live.

</details>


### 23. Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification

- **Authors:** Yunhao Feng, Ruixiao Lin, Ming Wen, Qinqin He, Yanming Guo, Yifan Ding, Yutao Wu, Jialuo Chen, Yunhao Chen, Xiaohu Du, Jianan Ma, Zixing Chen, Zhuoer Xu, Xingjun Ma, Xinhao Deng
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01793v1](http://arxiv.org/abs/2607.01793v1)
- **PDF:** [https://arxiv.org/pdf/2607.01793v1](https://arxiv.org/pdf/2607.01793v1)
- **Categories:** cs.AI


> The paper introduces **Vera**, a fully automated safety‑testing framework that brings software‑engineering testing practices to the evaluation of non‑deterministic LLM agents. Vera continuously mines the literature to build taxonomies of emerging risks, then automatically composes those dimensions into thousands of executable safety cases that define a concrete safety goal, an initial environment state, and a deterministic verification predicate; heterogeneous agents are run in isolated sandboxes where a control agent guides multi‑turn interactions and evidence‑grounded verifiers assess outcomes from tool‑call logs and environment state rather than model self‑reports. Applied to four state‑of‑the‑art agent platforms (OpenClaw, Hermes, Codex, Claude Code), Vera uncovered widespread vulnerabilities—averaging a 93.9 % success rate for multi‑channel attacks—and released the Vera‑Bench suite of 1,600 reproducible safety cases covering 124 risk categories, demonstrating the necessity of modular, executable testing for scalable, maintainable safety assurance of rapidly evolving agentic AI.


<details>
<summary>Abstract</summary>

LLM agents increasingly perform autonomous actions through external tools, leading to complex and evolving safety risks. However, existing safety testing targets expert-designed safety violations, and the corresponding outcomes are evaluated by hard-coded rules, making them costly to extend as agents evolve. To this end, we present Vera, an end-to-end automated safety testing framework that instantiates software engineering testing principles for non-deterministic agents through a three-stage, self-reinforcing pipeline. First, a literature-driven exploration continuously discovers and structures emerging risks into taxonomies of safety risks, attack methods, and tool execution environments. Second, combinatorial composition across taxonomy dimensions produces executable safety cases, each specifying a concrete safety goal, a programmatically constructed initial state, and a deterministic verification predicate grounded in observable artifacts. Third, adaptive execution runs heterogeneous agents in isolated sandboxes where a control agent steers multi-turn interaction based on runtime observations, while evidence-grounded verifiers judge outcomes from environment state and tool-call evidence rather than model self-report. We evaluate Vera on four production agent frameworks (OpenClaw, Hermes, Codex, Claude Code), revealing substantial safety weaknesses, with average attack success rates reaching 93.9\% under multi-channel attacks; we also release Vera-Bench, comprising 1600 executable safety cases spanning 124 risk categories across three execution settings. These results indicate that modular, executable testing infrastructure is essential for rigorous and maintainable safety evaluation of rapidly evolving agentic systems at scale. The code is publicly available at https://github.com/Yunhao-Feng/Vera.

</details>


### 24. SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation

- **Authors:** Chunjiang Liu, Xiaoyuan Wang, Haoyu Chen, Yizhou Zhao, Ming-Hsuan Yang, László A. Jeni
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01766v1](http://arxiv.org/abs/2607.01766v1)
- **PDF:** [https://arxiv.org/pdf/2607.01766v1](https://arxiv.org/pdf/2607.01766v1)
- **Categories:** cs.AI


> **Main contribution** – The paper introduces **SimWorlds**, a multi‑agent framework that can translate natural‑language prompts into *dynamic* (4‑D) Blender scenes, handling spatial layout, physics solvers, timing, camera, and lighting in a coordinated, editable pipeline; it also releases **4DBuildBench**, a benchmark for measuring visual fidelity and physical correctness of such procedurally generated scenes.  

**Methodology** – SimWorlds uses a planner‑coder‑reviewer trio of LLM agents operating on a fixed construction order, a layered scene‑protocol enforced by a deterministic verifier, and a runtime‑state inspection toolset that detects physics‑oriented failures beyond what rendered video can reveal.  

**Key findings** – Across the 4DBuildBench suite, SimWorlds achieves significantly higher scores in both visual quality and physical consistency than existing dynamic Blender generation baselines, demonstrating that coordinated multi‑agent orchestration and verification can reliably produce coherent, physics‑grounded 4‑D content from text.


<details>
<summary>Abstract</summary>

LLM agents are increasingly used to translate natural language into 3D scenes in a procedural way, but existing systems focus on static output. Dynamic 4D scenes from text alone, in which liquids flow, particles emit, rigid bodies cascade, and articulated mechanisms move, remain largely unexplored despite their value as editable content and as physics-grounded training data for video generation and embodied AI. Two challenges set the dynamic case apart from static text-to-scene work: an agent must jointly coordinate spatial layout, multiple physics solvers, temporal sequencing, camera, and lighting in a single coherent scene, and verifying motion correctness from rendered video is fundamentally harder than judging a single image. We present SimWorlds: a multi-agent framework that produces dynamic, editable 4D scenes from text, with Blender-specific procedural knowledge, a planner-coder-reviewer workflow driving a fixed ordered sequence of construction stages, a layered scene protocol enforced by a deterministic verifier, and a runtime-state inspection tool suite that catches mechanism failures the rendered image cannot reveal. We also introduce 4DBuildBench, a benchmark for assessing both visual fidelity and physical consistency of the procedural dynamic 3D scenes generated from text prompts. Experiments show that SimWorlds outperforms prior dynamic Blender generation baselines.

</details>


### 25. Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction

- **Authors:** Mingzhe Du, Luu Anh Tuan, Tianyi Wu, Renyang Liu, Zhijiang Guo, Dong Huang, See-Kiong Ng
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01764v1](http://arxiv.org/abs/2607.01764v1)
- **PDF:** [https://arxiv.org/pdf/2607.01764v1](https://arxiv.org/pdf/2607.01764v1)
- **Categories:** cs.AI


> The paper introduces **Mastermind**, a dual‑loop architecture that treats the selection of a high‑level vulnerability‑reproduction strategy as a compact, learnable unit separate from the low‑level execution of actions. Using supervised fine‑tuning and milestone‑based goal‑oriented reinforcement learning, a trainable planner acquires reusable strategies that are stored in an experience loop and then applied to guide a frozen LLM executor; this decoupling lets the same planner improve multiple executors without altering their code‑generation modules. Experiments on the CyberGym benchmark show that Mastermind raises the pass rate of a GPT‑5.5 executor from 60 % (baseline) to **84.5 %**, and similarly boosts GPT‑5.4‑mini and GLM‑5.1, demonstrating that strategy‑grounded learning is a practical, transferable way to enhance repository‑scale SE agents.


<details>
<summary>Abstract</summary>

Repository-level vulnerability reproduction is a demanding software engineering (SE) task: an agent must inspect a codebase, infer the input grammar that reaches a vulnerable path, construct a proof-of-conceptv(PoC), and verify that the crash disappears on the patched build. Recent LLM agents can often execute these steps when the approach is correct, yet they still fail by choosing the wrong strategy. This paper argues that strategy, rather than the full action trajectory, is the right learning unit for such SE agents: it is compact enough to optimize, concrete enough to guide execution, and stable enough to store and reuse across attempts. We present Mastermind, a dual-loop framework that separates transferable strategy learning from task-specific experience. A trainable planner learns reusable vulnerability-reproduction strategies through SFT and milestone-based GRPO, while an experience loop maintains task-local strategy records that guide subsequent attempts. The planner is trained independently of the executor, allowing strategy learning to improve multiple frozen executors without modifying their action-generation capability. We evaluate Mastermind on CyberGym using 260 training tasks and 200 held-out evaluation tasks. With GPT-5.5 as the frozen executor, Mastermind achieves an 84.5% pass rate, outperforming open-book PoC context (60.0%), Best-of-8 sampling (63.0%), and iterative improvement (77.0%). The same planner also improves GPT-5.4 mini and GLM~5.1 from 45.0% and 58.5% to 60.0% and 71.0%. These results demonstrate that learning high-level strategies is an effective and transferable mechanism for improving repository-scale SE agents.

</details>


### 26. Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry

- **Authors:** Yuante Li, Yicheng Tao, Kate Zhang, Taozhi Wang, Gefei Gu, Yaxin Zhou
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01661v1](http://arxiv.org/abs/2607.01661v1)
- **PDF:** [https://arxiv.org/pdf/2607.01661v1](https://arxiv.org/pdf/2607.01661v1)
- **Categories:** cs.AI


> The paper shows that the principal obstacle to effective multi‑LLM forecasting is the lack of informational diversity: when every agent receives the same evidence, deliberation merely reinforces a common bias and yields little improvement over a single model. To fix this, the authors introduce **designed information asymmetry**, partitioning the evidence pool into a shared public set and disjoint private subsets for each agent, and they embed this scheme in the **InfoDelphi** framework, which routes relevant evidence, conducts rationale‑driven iterative dialogue, and aggregates predictions with confidence weighting. Empirical results on the 375‑question PolyGym benchmark demonstrate that InfoDelphi achieves 12–18 % lower Brier scores and 4–8 pp higher accuracy than the strongest single‑agent and prior multi‑agent baselines, and ablations confirm that eliminating the asymmetry largely erases the deliberation gains, establishing diverse input as the key catalyst for superior agentic AI forecasting.


<details>
<summary>Abstract</summary>

Multi-agent systems are increasingly used for forecasting future events, as deliberation among multiple LLMs is believed to improve reasoning and calibration. Yet existing approaches overlook a critical design choice: what information each agent receives. When all agents are given identical evidence, deliberation collapses into herding rather than genuine belief revision, leaving multi-agent systems little better than a single agent. We identify this as a fundamental gap and propose designed information asymmetry to close it: by partitioning evidence into shared public and disjoint private subsets, each agent holds exclusive knowledge that can only reach others through deliberation. We theoretically show that this decomposition reduces inter-agent error correlation, and instantiate it in InfoDelphi, a framework combining relevance-aware evidence routing, rationale-based iterative deliberation, and confidence-weighted aggregation. On PolyGym, a benchmark of 375 binary forecasting questions derived from real-world prediction markets, InfoDelphi outperforms the strongest single-agent and multi-agent baselines by 12--18% in Brier score and 4--8 percentage points in accuracy. More detailed experiments confirm that removing information asymmetry eliminates most deliberation gains, establishing diversity of input as the key enabler of effective multi-agent reasoning.

</details>


### 27. Autonomous discovery of traffic laws with AI traffic scientists

- **Authors:** Xingyuan Dai, Yue Liu, Xiaoyan Gong, Qinghai Miao, Junyou Shang, Yutong Wang, Chao Guo, Yonglin Tian, Yizhang Chai, Chao Xiang, Yisheng Lv, Fei-Yue Wang
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01639v1](http://arxiv.org/abs/2607.01639v1)
- **PDF:** [https://arxiv.org/pdf/2607.01639v1](https://arxiv.org/pdf/2607.01639v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **TrafficSci**, an agentic AI framework that autonomously discovers universal traffic laws from heterogeneous urban mobility data, extending AI‑driven scientific discovery from laboratory settings to the complex, real‑world domain of city transportation.

**Methodology:** TrafficSci casts law discovery as an iterative, auditable workflow comprising (1) **evidence scoping** to gather relevant observational and interventional data, (2) a **critic‑judge module** that generates and refines causal hypotheses, and (3) **validation** through both observational consistency checks and targeted simulation/field interventions. The system is evaluated on four case studies covering population‑level patterns, network dynamics, control policies, and individual trajectories.

**Key findings:** Across eight cities and two trajectory datasets, TrafficSci automatically rediscovers three known traffic laws and uncovers a previously undocumented **intrinsic temporal memory scale** in driver behavior that is statistically consistent across all studied environments, demonstrating the feasibility of autonomous, scalable scientific discovery for agentic AI in urban traffic systems.


<details>
<summary>Abstract</summary>

Universal traffic laws describe recurrent patterns in congestion, mobility and driving behavior across cities, providing a scientific basis for transportation planning, management and control. Their discovery, however, remains expert-driven, requiring candidate regularities to be identified from heterogeneous observational evidence or validated through intervention experiments. Although autonomous artificial intelligence (AI) systems have advanced scientific discovery in controlled laboratory settings, extending them to complex transportation domains remains a challenge. Here we present TrafficSci, an agentic AI system that formulates traffic-law discovery as an iterative, auditable workflow integrating evidence scoping, critic-judge hypothesis induction, and observational-interventional validation. Across four case studies spanning population, network, control and trajectory scales, TrafficSci autonomously rediscovers three established traffic laws and identifies an unreported intrinsic temporal memory scale in urban driving behavior, statistically consistent across eight cities and two trajectory datasets. TrafficSci provides a route for extending AI-driven scientific discovery from controlled domains to complex urban systems.

</details>


### 28. BOUNDARY_SYNC: Measuring Communication-Induced Representational Coupling in Multi-Agent LLM Systems

- **Authors:** Zewen Liu
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01600v1](http://arxiv.org/abs/2607.01600v1)
- **PDF:** [https://arxiv.org/pdf/2607.01600v1](https://arxiv.org/pdf/2607.01600v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces **BOUNDARY_SYNC**, a protocol that quantifies how communication between LLM‑based agents aligns (or diverges) their internal representations using a **Coupling Amplification Factor (CAF)**—the ratio of conditional to baseline Jensen‑Shannon divergences. By running large‑scale GPT‑4o experiments (≈30 agents, ~9.9 k API calls) with both text and image exchanges, the authors show that ordinary textual dialogue reliably **homogenizes** agent outputs (CAF≈0.80, large effect size d = 1.30), and that image‑based messages produce a similar effect within‑modality; however, the direction of coupling flips with smaller groups (K = 3) where CAF exceeds 1, indicating **diversification**, and varies dramatically across other LLM families (CAF 0.03‑0.80). The study demonstrates that representational coupling is **stateless and controllable via prompt design**, providing the first systematic measurement tool and empirical baseline for building coordinated or deliberately diverse multi‑agent LLM systems.


<details>
<summary>Abstract</summary>

As large language models (LLMs) are deployed as communicating agents, does inter-agent communication cause outputs to converge? We introduce BOUNDARY_SYNC, a protocol measuring representational coupling via the Coupling Amplification Factor (CAF = JSD_cond / JSD_baseline), where CAF < 1 indicates homogenization and CAF > 1 indicates diversification. In controlled GPT-4o experiments (N=30, ~9,900 API calls), we measure coupling in text and image communication. Key findings: (1) text communication causes significant homogenization (CAF=0.803 [0.740, 0.873], d=1.30, p<0.001), confirmed by no-communication ablation and prompt-perturbation controls; (2) image communication also homogenizes under within-modality baselines (CAF=0.834 [0.811, 0.858]), with comparable proportional effect; (3) group size moderates coupling direction -- K=5 produces homogenization while K=3 yields CAF > 1.0 (point estimates 1.14 and 1.06, CI pending), suggesting a directional shift toward diversification; (4) cross-model replication shows extreme variation (CAF 0.034-0.803), with DeepSeek dominated by format artifacts; (5) coupling is stateless -- driven by prompt context rather than cumulative updating, with continuous consensus producing monotonic convergence. These results establish LLM agent coupling as real, measurable, and controllable at the prompt level, with direct implications for multi-agent system design.

</details>


### 29. Mechanism and Stability Analysis of Metabolic Closed-Loop Metaheuristics

- **Authors:** Jinliang Xu, Liping Ma
- **Published:** 2026-07-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01551v1](http://arxiv.org/abs/2607.01551v1)
- **PDF:** [https://arxiv.org/pdf/2607.01551v1](https://arxiv.org/pdf/2607.01551v1)
- **Categories:** cs.NE, cs.MA


> **Main contribution:** The paper provides a formal, framework‑level analysis of the Metabolic Multi‑Agent Optimizer (MMAO), isolating the “metabolic” resource loop (private energy, communal budget, role drift, and lifecycle turnover) from any specific move operators and showing which dynamical properties follow inevitably from this loop.

**Methodology:** The authors construct an abstract state‑space model of MMAO that tracks the four resource variables under mild bounded‑gain and bounded‑spending assumptions. Using deterministic and stochastic stability theory they prove non‑negativity and boundedness of all resources, and they delineate three endogenous regimes—contraction (resource deficit), reinvestment (communal surplus), and search redistribution (heterogeneous marginal returns). A lightweight mechanism‑validation suite on representative continuous and discrete MMAO instances supplies empirical corroboration.

**Key findings for agentic AI:** The analysis reveals that MMAO’s self‑regulating resource loop guarantees a regenerative, bounded population dynamics independent of problem‑specific heuristics, and that the system naturally cycles among deficit‑driven contraction, surplus‑driven reinvestment, and load‑balancing redistribution. These generic regulatory behaviours provide a principled basis for designing and reasoning about resource‑aware, multi‑agent AI optimizers, while clarifying which performance aspects remain implementation‑specific.


<details>
<summary>Abstract</summary>

This paper studies the Metabolic Multi-Agent Optimizer (MMAO) at the framework level rather than at the implementation or benchmark level. The central question is whether the metabolic resource loop of private energy, communal budget, role drift, and lifecycle turnover has a framework-level interpretation beyond narrative metaphor. We introduce a generic MMAO state model that abstracts away domain-specific move operators while retaining the resource bookkeeping that defines the framework. Under mild bounded-gain and bounded-spending assumptions, we establish boundedness and nonnegativity properties for private energy, communal budget, role state, and active population size. We then characterize three endogenous behavioral regimes of the loop: contraction under sustained resource deficit, reinvestment under surplus communal accumulation, and search redistribution under heterogeneous marginal returns across agents or subgroups. The analysis is intentionally conservative. It does not claim global convergence of the full adaptive system, universal superiority over specialist optimizers, or a complete stationary characterization of the resulting process. Instead, it identifies which internal regulation properties are generic consequences of the loop and which remain implementation specific. A compact mechanism-validation package on representative continuous and discrete MMAO realizations provides supporting empirical evidence for this reading, but is not intended to replace a full benchmark study. The resulting contribution is therefore a bounded, regenerative, resource-regulated interpretation of MMAO, rather than a complete proof of all adaptive behaviors of the full algorithm family.

</details>


### 30. MMAO-Cls: Metabolic Multi-Agent Optimization for Joint Feature Selection and Classifier Tuning

- **Authors:** Jinliang Xu, Liping Ma
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01539v1](http://arxiv.org/abs/2607.01539v1)
- **PDF:** [https://arxiv.org/pdf/2607.01539v1](https://arxiv.org/pdf/2607.01539v1)
- **Categories:** cs.NE, cs.LG, cs.MA


> **Contribution**  
The paper introduces **MMAO‑Cls**, a novel outer‑loop optimizer that extends the Metabolic Multi‑Agent Optimizer (MMAO) to the mixed‑discrete/continuous space of **joint feature‑selection and classifier‑hyperparameter tuning**. It demonstrates how metabolic mechanisms (private energy, communal budget, role drift, turnover) can be mapped to the accuracy‑complexity trade‑off of wrapper‑based model selection.

**Methodology**  
Each MMAO agent encodes a binary mask for features together with a vector of classifier hyper‑parameters. Feature‑budget adaptation is driven by information‑theoretic priors, and the validation reward is regularized by (i) subset compactness and (ii) the train‑validation over‑fitting gap. The approach is benchmarked on seven tabular datasets (three random seeds each) against Random Search, a lightweight GA, a lightweight PSO, and a no‑sharing ablation, using both validation‑objective rankings and held‑out test scores.

**Key Findings for Agentic AI**  
- MMAO‑Cls achieves the **second‑best aggregate validation score** (0.9433) and the **best trade‑off between performance and feature‑set compactness** (average feature ratio ≈ 0.49).  
- On held‑out test data it matches or slightly exceeds the baselines (mean test score ≈ 0.888), though the differences are not statistically significant.  
- The results suggest that metabolic multi‑agent dynamics can feasibly guide mixed‑space search in automated model selection, but the advantage of communal sharing over independent agents remains modest.


<details>
<summary>Abstract</summary>

This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can act as a credible outer-loop optimizer for classification model selection. We propose MMAO-Cls, a mixed-space realization in which each agent jointly encodes a binary feature mask and classifier hyperparameters, while private energy, communal budget, role drift, and lifecycle turnover are mapped to the accuracy-complexity tradeoff of wrapper learning. The implementation is strengthened by deriving feature-budget adaptation from feature-information priors and by regularizing validation reward with both subset compactness and train-validation overfitting gap. We evaluate MMAO-Cls on seven standard tabular benchmarks with three seeds each and compare it against RandomSearch, GA-lite, PSO-lite, and an endogenous no-sharing ablation. On the aggregate validation objective, MMAO-Cls ranks second ($0.9433$) behind GA-lite ($0.9446$). On held-out test performance, it reaches mean score $0.8882$, improving over RandomSearch ($0.8808$) and GA-lite ($0.8857$), remaining close to PSO-lite ($0.8874$) and the no-sharing ablation ($0.8900$), while using the most compact mean held-out feature subset among all compared methods (feature ratio $0.4881$). Pairwise tests show that these margins are not yet statistically significant. The resulting claim is therefore conservative: MMAO-Cls supports classification applicability and compact mixed-space search more clearly than it isolates communal sharing as a decisive standalone advantage.

</details>


### 31. OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration

- **Authors:** David Courtis, Wenhao Li, Scott Sanner
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01531v1](http://arxiv.org/abs/2607.01531v1)
- **PDF:** [https://arxiv.org/pdf/2607.01531v1](https://arxiv.org/pdf/2607.01531v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **OPINE‑World**, an autonomous LLM‑driven system that builds and refines an object‑centric, programmatic world model while interacting with a novel environment. It couples a planner‑agent that explores the scene with a synthesis‑agent that generates source‑code models via counterexample‑guided inductive synthesis, using a Bayesian “ontology‑error” metric to prioritize learning new object types. On the ARC‑AGI‑3 benchmark—where object vocabularies, goals, and action semantics are hidden—OPINE‑World solves 20 of 25 pixel‑based games without any per‑game training, achieving a 78.4 % action‑efficiency score relative to human performance.


<details>
<summary>Abstract</summary>

Learning how an environment behaves from interaction is central to building agents that adapt to unfamiliar tasks. World models learned with deep networks are flexible but data-hungry and transfer poorly beyond their training distribution. Program-synthesized world models, written as source code by LLMs and refined through counterexample-guided inductive synthesis (CEGIS), are instead data-efficient and reusable, yet they have been demonstrated mainly on structured-state worlds with a given object vocabulary, and a single program search does not scale to pixel-rendered environments whose object structure must be hypothesized flexibly. We introduce OPINE-World, an LLM agent that learns an object-centric programmatic world model online from interaction. OPINE-World couples two cooperating agents in a loop of hypothesis and test, one acting in the environment and one synthesizing the model in code with replay verification and model-based planning, and it steers exploration with a Bayesian measure of object-type adequacy we call ontology error. We evaluate OPINE-World on ARC-AGI-3, a benchmark for skill-acquisition efficiency in which the object vocabulary, the goal, and the action semantics are withheld. OPINE-World solves 20 of 25 games without per-game training and reaches an action-efficiency score of 78.4 against the human baseline.

</details>


### 32. Mean Field Reinforcement Learning

- **Authors:** René Carmona, Mathieu Laurière
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01525v1](http://arxiv.org/abs/2607.01525v1)
- **PDF:** [https://arxiv.org/pdf/2607.01525v1](https://arxiv.org/pdf/2607.01525v1)
- **Categories:** math.OC, cs.LG, cs.MA, math.PR


> **Main contribution:** The paper bridges mean‑field control theory and modern reinforcement learning by formalising “representative‑agent” Markov decision processes that capture the limiting behaviour of huge multi‑agent systems with both mean‑field interactions and common noise.  

**Methodology:** It derives a complete probabilistic‑control framework—including dynamic‑programming equations, propagation‑of‑chaos limits, and linear‑quadratic reductions—and then proves convergence guarantees for both tabular Q‑learning and policy‑gradient algorithms in the mean‑field setting, extending the analysis to deep variants such as Deep Deterministic Policy Gradient.  

**Key findings:** Theoretical results show that learning on the limiting mean‑field MDP yields policies that approximate optimal finite‑population strategies as the number of agents grows, and empirical experiments validate that the proposed tabular and deep algorithms scale efficiently to very large stochastic populations, delivering tractable, high‑performing solutions for agentic AI problems.


<details>
<summary>Abstract</summary>

This monograph provides an introduction to mean field reinforcement learning through the lens of Markov decision processes arising from large-population stochastic control with mean field interactions and common noise. Starting from the connection between multi-agent reinforcement learning and mean field control, it develops the probabilistic, mathematical, and control-theoretic framework needed to formulate representative-agent learning problems, analyze their relationship with finite-population systems, and study both general and linear-quadratic models. The presentation includes dynamic programming principles, propagation-of-chaos limits, and theoretical analyses of tabular Q-learning and policy-gradient methods. It also discusses numerical implementations, including tabular schemes and deep reinforcement learning methods such as deep deterministic policy gradient. The goal is to give readers a coherent bridge between mean field control theory and reinforcement learning methodology, emphasizing the mathematical structure of the problems and the design of tractable learning approaches for large stochastic populations.

</details>


### 33. Janus: a Playground for User-Involved Agentic Permission Management

- **Authors:** Natalie Grace Brigham, Eugene Bagdasarian, Tadayoshi Kohno, Franziska Roesner
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01510v1](http://arxiv.org/abs/2607.01510v1)
- **PDF:** [https://arxiv.org/pdf/2607.01510v1](https://arxiv.org/pdf/2607.01510v1)
- **Categories:** cs.AI, cs.CR


> **Main contribution** – The paper presents **Janus**, an open‑source playground that lets researchers prototype, compare, and evaluate a wide range of **user‑involved permission‑management designs for autonomous AI agents**.  

**Methodology** – Janus consists of (1) **Janus‑Core**, a modular agentic framework that can be configured with different “permission assistants” along a conceptual design space (e.g., levels of user control, AI‑augmented decision support), and (2) **Janus‑Harness**, an automated evaluation suite that runs the assistants in three realistic task scenarios against three synthetic “responders” (simulated users) while measuring privacy, security, and cognitive‑load metrics. The authors implement six distinct assistants spanning the design axes and conduct systematic experiments.  

**Key findings** – (1) Direct user input dramatically improves privacy and security outcomes; (2) AI‑augmented decision aids can substantially lower user cognitive load without sacrificing safety; (3) realistic user behaviors such as permission‑fatigue materially affect performance, and no single assistant dominates across all scenarios. These results underscore the need for **context‑sensitive, principled designs of permission assistants** in agentic AI systems.


<details>
<summary>Abstract</summary>

AI agents that autonomously execute tool calls on a user's behalf raise pressing questions about permission management: what role could users play, and what role should they play? Despite many proposed approaches, the user's role in agentic permission management remains under explored. We introduce Janus, a playground system for implementing and evaluating user-involved agentic permission management designs. Janus consists of two components: Janus-Core, a modular agentic system supporting a diverse spectrum of permission management designs, and Janus-Harness, an automated evaluation framework. Grounded in a conceptual model that identifies key design axes for user involvement, we implement six permission assistants spanning the design space and evaluate them across three scenarios and three synthetic responders. We demonstrate that user input is critical and can significantly strengthen privacy and security, that AI augmentation of user decisions can help reduce cognitive load, and that realistic user behavior including permission fatigue must be accounted for in system design. No single design performs optimally across all contexts, motivating a more principled and context-sensitive approach to deploying permission assistants in agentic systems. Janus is publicly available to support future investigation into this dimension of agentic system design.

</details>


### 34. The Agentic Garden of Forking Paths

- **Authors:** Jiacheng Miao, Jonathan K Pritchard, James Zou
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01507v1](http://arxiv.org/abs/2607.01507v1)
- **PDF:** [https://arxiv.org/pdf/2607.01507v1](https://arxiv.org/pdf/2607.01507v1)
- **Categories:** cs.AI, stat.ME


> **Main contribution** – The paper demonstrates that large‑language‑model agents can reproduce the hidden “forking‑paths” problem in empirical research: by adopting different personas, they generate multiple, methodologically legitimate analyses of the same dataset that lead to divergent, often opposite, conclusions, thereby making the space of plausible analyses observable and quantifiable.

**Methodology** – The authors prompt AI agents with distinct ideological or disciplinary personas to analyze the same high‑stakes datasets (including an immigration study previously examined by 42 human research teams). They compare the agents’ effect estimates to the human ideological gap, evaluate the plausibility of each analysis via independent AI and human review, and introduce the *m‑value* (multiverse value)—the probability that a randomly sampled analysis path would yield a claim at least as extreme as the reported one. The *Agentic Bootstrap* procedure estimates this m‑value by repeatedly sampling plausible analysis pipelines with the agents.

**Key findings** – AI agents reproduced ≈ 72 % of the human ideological divergence and most of their divergent reports passed both AI and human expert scrutiny (86 % and 78 % respectively), showing that the problem is not flawed methods but selective reporting. Using Agentic Bootstrap, only 13.5 % of the human‑generated analyses fell into the most extreme 5 % of the plausible analysis space (m < 0.05), indicating that many published claims sit near the tail of a large multiverse of defensible analyses. The work suggests that agentic AI can both exacerbate and help diagnose the forking‑paths issue by making the distribution of possible analyses explicit and providing a new credibility metric for scientific claims.


<details>
<summary>Abstract</summary>

Empirical research rarely admits a unique analysis. Different analytical choices can lead to different conclusions from the same data, yet these hidden forking paths are difficult to observe. We show that AI agents capture much of the analytical variation among human researchers while making these paths explicit. Across four high-stakes domains, assigning different personas is sufficient for AI agents to report divergent, often opposing, conclusions from the same data and question, with findings systematically aligned with those beliefs. In a study in which 42 human research teams analyzed the same immigration dataset, AI agents reproduced 72% of the human ideological gap in reported effect estimates. Despite reaching opposing conclusions, it is difficult to identify clear issues in each analysis based on the final AI reports: 86% passed independent AI review and 78% passed majority human expert review. These findings suggest that the central challenge is often not flawed analyses, but selective exploration and reporting from a large space of methodologically defensible analyses. AI agents may amplify this longstanding problem by making such exploration inexpensive and scalable. To address this, we introduce the m-value (multiverse value), the probability that an analysis path would produce a claim at least as extreme as the reported one. We further introduce Agentic Bootstrap, which estimates the m-value by using AI agents to sample plausible analysis paths. Applied to the human immigration study, 13.5% of reported human analyses fell in the most extreme 5% of the analysis space (m<0.05). Scientific evidence should therefore be evaluated not only by a single reported analysis but also by its position within the distribution of analyses that could reasonably have been reported. Agentic Bootstrap makes this distribution observable and turns it into a criterion for scientific credibility.

</details>


### 35. Beyond Next-Token Prediction: An RLVR Proof of Concept for Tool-Use Agents on Atlassian Workflows

- **Authors:** Karthikeya Aditya Vissa, Sankalp Mane, Ananya Mantravadi, Harshit Rajgarhia, Abhishek Mukherji
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01465v1](http://arxiv.org/abs/2607.01465v1)
- **PDF:** [https://arxiv.org/pdf/2607.01465v1](https://arxiv.org/pdf/2607.01465v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are trained to predict the next token, not to act inside a specific API. In niche enterprise SaaS workflows -- where success means hitting the right endpoint with the right nested arguments in the right order -- this objective mismatch shows up as silent failures: dropped required fields, hallucinated tools, or early stops after a single read. We ask whether Reinforcement Learning with Verifiable Rewards (RLVR), applied directly in the target environment, closes the gap. As a proof of concept we build a suite of five synthetic environments emulating the Jira REST v3 and Confluence v2 APIs at schema fidelity; rewards are computed entirely from the tool-call trace, with no live API, no learned judge, and no human label in the loop. Scoring prompted Qwen3-1.7B and Qwen3.5-4B on the same checkers that drive GRPO training, we find that on the four scenarios whose rewards are non-degenerate the RL-trained policy lifts average reward from a 4B-baseline range of 0.35--0.92 to 0.95--1.00, with the largest single gain on Confluence page creation ($0.35 \rightarrow 1.00$). We position this as a preliminary step toward outcome-optimised small models for niche enterprise APIs, and foreground two limitations a workshop reader should weigh: hand-crafting verifiable rewards does not scale beyond the handful of endpoints reported here, and one of our five scenarios (ticket-transition) has a saturating reward shape that the prompted 4B already maxes out.

</details>


### 36. When Should Service Agents Reconsider? Difficulty-Routed Control in Customer-Service Operations

- **Authors:** Qian Chen, Chengyuan Liu, Xin Yu
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01426v1](http://arxiv.org/abs/2607.01426v1)
- **PDF:** [https://arxiv.org/pdf/2607.01426v1](https://arxiv.org/pdf/2607.01426v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces a “difficulty‑routed” control architecture for autonomous customer‑service agents that dynamically decides when an agent should pause and reconsider before performing consequential backend writes, thereby balancing speed for routine interactions with safety for high‑risk, operationally coupled requests.  

**Methodology:** A lightweight router classifies each session as either routine or “conflicted” (i.e., involving policy constraints, ambiguous customer intent, or complex record interactions) and routes the latter to an escalated workflow that adds conflict‑aware messaging, evidence‑gathering turns, and a write‑triggered reconsideration step; the system is evaluated on human‑verified retail and airline tasks from the τ²‑bench dataset, comparing baseline vs. routed performance.  

**Key Findings:** On retail tasks, the routed agents achieve significantly higher reliability on conflict‑laden requests without degrading routine performance, with the extra dialogue turns and tool calls being used specifically for evidence collection, write separation, and pre‑write checks rather than blanket tool expansion. Similar improvements are observed in airline reservation scenarios, demonstrating that the difficulty‑routed, pre‑write reconsideration mechanism effectively concentrates deliberation where it matters most for agentic AI safety and robustness.


<details>
<summary>Abstract</summary>

Autonomous customer-service agents are shifting from conversational interfaces toward operational execution roles: they retrieve firm records, apply service policies, and execute backend writes such as refunds, cancellations, exchanges, order modifications, and reservation changes. This shift creates a service-control problem: firms must keep routine service fast and low-friction while preventing operational errors on requests where customer instructions, policy constraints, firm records, and backend writes interact. We propose a difficulty-routed service-control architecture that asks when service agents should reconsider before acting. A lightweight router keeps routine sessions on a low-cost baseline path and routes operationally coupled sessions to an escalated workflow. The escalated path uses conflict-aware communication and write-triggered reconsideration to concentrate deliberation and safeguards before consequential backend writes, rather than applying additional control uniformly across all service sessions. We evaluate the architecture on human-verified retail and airline tasks from $τ^{2}$-bench. In retail, the method improves reliability consistently on service requests with operational conflict. Routing evidence shows that stronger control is directed toward conflicted requests rather than broadly applied to routine ones. Dialogue and tool-use profiles suggest that gains do not come from indiscriminate interaction expansion or broader tool chains; instead, added turns and tool calls support evidence gathering, write separation, and pre-write reconsideration. Case-level evidence shows that the escalated workflow preserves fallback plans, binds retrieved records to the correct action, sequences writes, and decomposes multi-entity requests. Airline results extend the same service-control logic to reservation operations.

</details>


### 37. Agent4cs: A Multi-agent System for Code Summarization in Large Hierarchical Codebases

- **Authors:** Yongjian Tang, Ezgi Sarikayak, Doruk Tuncel, Jie M. Zhang, Thomas Runkler
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01425v1](http://arxiv.org/abs/2607.01425v1)
- **PDF:** [https://arxiv.org/pdf/2607.01425v1](https://arxiv.org/pdf/2607.01425v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces **Agent4cs**, a multi‑agent architecture that tackles code summarization for large, hierarchically organized repositories by explicitly leveraging folder‑level dependencies and a divide‑and‑conquer workflow.  

**Methodology:** Three specialized agents operate in a bottom‑up pipeline: (1) a **summarization agent** generates drafts for individual subfolders, (2) a **keyword‑extraction agent** autonomously surfaces salient identifiers and concepts from lower‑level code, and (3) a **quality‑assurance agent** iteratively rewrites the drafts to improve readability, coherence, and completeness. The system is evaluated across seven state‑of‑the‑art language models and compared against structured prompting baselines.  

**Key Findings:** Across all tested models, Agent4cs raises semantic consistency of generated summaries by an average of **8 %**, and achieves up to **38 %** higher normalized keyword‑coverage on real‑world codebases, demonstrating that coordinated multi‑agent reasoning markedly outperforms single‑model, flat‑text approaches in the agentic AI domain.


<details>
<summary>Abstract</summary>

Understanding large, complex codebases, especially those with obfuscated structures and incomplete documentation, remains a significant challenge. Existing code summarization solutions often rely on a single language model or coding assistant like Claude Code, and treat source code as flat text, underutilizing the rich interdependencies and hierarchical information within a repository. To address these shortcomings, we propose Agent4cs - a multi-agent framework that summarizes large codebases in a bottom-up fashion, where a summarization agent focuses on producing robust summaries; a keyword-extraction agent proactively identifies critical information from subfolders; and a quality-assurance agent iteratively refines the outputs for readability, coherence, and completeness. Evaluated on 7 frontier models, Agent4cs improves semantic consistency across all folder levels by average 8% compared to two structured prompting baselines with code segments. Furthermore, extensive evaluation on real-world datasets demonstrates up to 38% gains in normalized keyword coverage rate over the same baselines.

</details>


### 38. Risk Architecture for AI-Native Engineering Teams: An Organizational Framework for Agentic System Governance

- **Authors:** Laxmipriya Ganesh Iyer
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01421v1](http://arxiv.org/abs/2607.01421v1)
- **PDF:** [https://arxiv.org/pdf/2607.01421v1](https://arxiv.org/pdf/2607.01421v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces an “risk architecture” framework that lets engineering managers of AI‑native teams explicitly map roles, decision rights, and escalation paths to the particular uncertainties of agentic systems. By classifying teams along a seven‑dimensional profile (pure software, hybrid, AI‑native) and a six‑cluster taxonomy of failure modes—including a new “dependency‑boundary determinism mismatch” cluster—the authors devise a synthetic adequacy scoring method that measures how well a given profile detects, contains, and escalates a curated set of risk scenarios. Their analysis shows that as teams become more AI‑native, median coverage of failure modes steadily declines and a sharp increase in uncovered high‑impact failures appears, especially at the organizational boundaries where probabilistic AI outputs are consumed by deterministic downstream components.


<details>
<summary>Abstract</summary>

Engineering management research has produced mature frameworks for software risk: ownership by feature, escalation by severity, and assurance by test coverage. These frameworks implicitly assume deterministic behavior, discrete and auditable change events, and clear component-to-owner mappings. Teams that build and operate agentic AI systems violate all three assumptions at once: outputs are probabilistic, systems take autonomous multi-step actions, and the risk surface mutates silently between deployments. Existing AI risk literature addresses this from above (policy frameworks such as the NIST AI RMF and ISO/IEC 42001) or below (threat taxonomies such as OWASP's agentic AI guidance), but not at the layer where an engineering manager (EM) operates: roles, decision rights, and escalation structures. This paper contributes (i) a seven-dimension profile distinguishing pure software-engineering, hybrid, and AI-native teams; (ii) a six-cluster failure-mode taxonomy including a previously unarticulated cluster, dependency-boundary determinism mismatch; and (iii) a synthetic framework-adequacy methodology scoring how well each profile's risk architecture detects, contains, and escalates a defined scenario set. Because the object of study is framework adequacy rather than human behavior, the evaluation yields derived rather than observed coverage claims. Coverage degrades as teams move from pure software engineering to AI-native operation, monotonically in the median and abruptly in the count of uncovered, high-consequence failures appearing only at the AI-native step. The degradation concentrates in specific failure-mode categories, and the most severe, least-covered failures arise not inside AI-native teams but at the organizational boundary where their probabilistic outputs are consumed by determinism-assuming dependencies.

</details>


### 39. Simulation Based Reward Function Validation for Multi-Agent On Orbit Inspection

- **Authors:** Patrick Quinn, Bala Prenith Reddy Gopu, George M. Nehma, Madhur Tiwari
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01367v1](http://arxiv.org/abs/2607.01367v1)
- **PDF:** [https://arxiv.org/pdf/2607.01367v1](https://arxiv.org/pdf/2607.01367v1)
- **Categories:** cs.MA, cs.RO


> **Main contribution:** The paper introduces a *generalized, simulation‑based reward function* for multi‑agent reinforcement learning (MARL) of cooperative inspection spacecraft, enabling the agents to decide *where* and *when* to capture images rather than being forced to visit a fixed set of way‑points.

**Methodology:** The authors first generate high‑fidelity 3D reconstructions of target objects and simulate image acquisition from arbitrary viewpoints. They then evaluate candidate reward formulations on the quality of the resulting reconstruction (e.g., coverage, redundancy, and pose diversity) and embed the best‑performing formulation into a MARL training loop (e.g., PPO/MA‑A2C). The agents learn policies that schedule image captures autonomously while navigating the orbital environment.

**Key findings:** Experiments show that the generalized reward leads to policies that achieve **significantly higher reconstruction fidelity** and **greater image‑budget efficiency** than policies trained with traditional waypoint‑based rewards. Moreover, the analysis reveals that rewarding *coverage diversity* and *information gain*—rather than mere waypoint visitation—produces robust inspection behaviours that transfer well to real‑world scenarios, offering design guidelines for reward shaping in broader autonomous inspection and agentic AI tasks.


<details>
<summary>Abstract</summary>

A proposed method for the control of groups of inspection spacecraft is Multi-Agent Reinforcement Learning (MARL). While MARL has already been employed for this purpose in previous work, the reward functions used focus on reaching a finite set of predetermined inspection points around the target. In this work, we study and develop a generalized reward function for the MARL inspection task informed by the analysis of 3D reconstructions of inspected objects in orbit. Because the reward function is generalized such that any number of images at arbitrary locations may evaluated, we also allow trained agents to have complete control over when images are collected. With this approach, we gather insights into best practices for not only the specific MARL inspection task, but also gain key takeaways informative to the broader inspection task outside of a MARL context.

</details>


### 40. Optimal Resource Utilization for Autonomous Laboratory Orchestrators

- **Authors:** Austin McDannald, Julia Tisaranni, Howie Joress
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01188v1](http://arxiv.org/abs/2607.01188v1)
- **PDF:** [https://arxiv.org/pdf/2607.01188v1](https://arxiv.org/pdf/2607.01188v1)
- **Categories:** cs.AI, cond-mat.mtrl-sci


> **Main contribution:** The paper introduces a two‑stage framework for maximizing the throughput of autonomous chemistry labs, specifically a metal‑organic framework (MOF) synthesis platform, by jointly optimizing experiment scheduling and execution under realistic hardware constraints.

**Methodology:** First, a constraint‑programming model encodes instrument capacities, processing times, and inter‑instrument dependencies to compute a time‑optimal schedule for a given batch of suggested experiments. Second, a lightweight runtime layer attaches status‑dependency descriptors to each task, ensuring that the pre‑computed schedule can be robustly followed despite asynchronous instrument states, failures, or delays.

**Key findings:** Empirical tests on the MOF platform show that the approach reduces overall completion time by up to 35 % compared with naïve first‑come‑first‑served execution, while maintaining feasibility under varied hardware limits, thereby demonstrating that formal scheduling combined with status‑dependency monitoring can substantially improve resource utilization in agent‑driven autonomous laboratories.


<details>
<summary>Abstract</summary>

In autonomous laboratories, AI agents suggest the next batch of experiments to do. However, planning and executing those tasks taking full advantage of the available resources is a completely different question. This can be challenging when dealing with real-world hardware constraints, especially so when there are multiple instruments with different capacities and throughputs. Here we demonstrate a 2-step method to address resource utilization for our autonomous platform for metal-organic framework synthesis. First, we use constraint programming to find optimal schedules. This finds schedules that minimizes the total time while still satisfying the limitations and capacities of the hardware. Secondly, we use a system of status dependencies for each task, which allows for the robust execution of the optimal schedules.

</details>


### 41. Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning

- **Authors:** Carlos Baquero, Luís Brito
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01308v1](http://arxiv.org/abs/2607.01308v1)
- **PDF:** [https://arxiv.org/pdf/2607.01308v1](https://arxiv.org/pdf/2607.01308v1)
- **Categories:** cs.MA


> The paper introduces **CanonicalMerge**, a deterministic, order‑independent method for merging the KV‑caches of multiple reasoning agents into a single latent state. By sorting caches according to the mean K‑norm at an intermediate layer and representing the merged state as a content‑addressed set (a convergent replicated data type), the merge becomes commutative, associative, and idempotent, guaranteeing byte‑identical results regardless of input permutation. Experiments on a partitioned‑reasoning benchmark and HotpotQA show that CanonicalMerge matches or exceeds the best heuristic BagMerge orderings across all budget and model regimes, while outperforming training‑free output‑fusion baselines, thereby providing a robust, scalable foundation for multi‑agent latent reasoning.


<details>
<summary>Abstract</summary>

Multi-agent latent reasoning composes agents' KV-caches into one context for a final agent. Prior work (Agent Primitives) does this by concatenating caches along the sequence axis with RoPE re-encoding, which we call BagMerge. BagMerge is non-commutative, and the best input ordering is unpredictable, shifting with the regime, the latent-step budget, and the model scale. We make this exchange a convergent replicated state. First, CanonicalMerge fixes the layout by content: ordering caches by mean K-norm at a middle layer renders the merged cache byte-identical under any input permutation, verified algorithmically (arity N<=5) and bit-for-bit on real Qwen3-1.7B and 4B state. Second, we separate the replicated state from decode-time layout: the state is a set of content-addressed latent fragments whose merge is set union, a state-based CvRDT (commutative, associative, idempotent, absorbing), and CanonicalMerge is its deterministic render. Because the render is byte-equivalent, every N=2 accuracy number carries over unchanged and re-delivered duplicates are absorbed rather than re-concatenated. On a partitioned-reasoning benchmark, CanonicalMerge matches the best BagMerge ordering in every regime-by-budget-by-ordering cell without knowing which order is best, trading a small, statistically insignificant accuracy margin for an unconditional structural guarantee. The behaviour transfers to real multi-document QA (HotpotQA), while the closest training-free output-fusion baseline (PackLLM) loses by 45 points at matched budget, placing cache-level merging in a regime distinct from output-level fusion. Finally, at k>2 the approach transports and colocates latent traces but does not by itself compose them, which we characterize to motivate future work.

</details>


### 42. Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use

- **Authors:** Song-Lin Lv, Weiming Wu, Rui Zhu, Zi-Jian Cheng, Lan-Zhe Guo
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01084v1](http://arxiv.org/abs/2607.01084v1)
- **PDF:** [https://arxiv.org/pdf/2607.01084v1](https://arxiv.org/pdf/2607.01084v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets, and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use Agent in Open-World), a problem setting characterized by distributional shifts across query, action, observation, and domain dimensions. To systematically diagnose its impact, we construct a controlled sandbox environment where we define fine-grained environmental shifts across a four-tier hierarchy, Perception, Interaction, Reasoning, and Internalization, and conduct a comprehensive series of experiments. Our analysis yields a series of key insights, demonstrating that agents trained via both Supervised Fine-Tuning(SFT) and Reinforcement Learning suffer from varying degrees of performance degradation when confronting open environmental shifts. Building on these insights, we propose Perturbation-Augmented Fine-Tuning, a disturbance-based intervention strategy for SFT that lays the foundation for enhancing agent robustness and utility in realistic environments. Our code will be released at: https://github. com/LAMDA-NeSy/OpenAgent.

</details>


### 43. Agentic generation of verifiable rules for deterministic, self-expanding reaction classification

- **Authors:** Daniel Armstrong, Maarten Dobbelaere, Valentas Olikauskas, Helena Avila, Octavian Susanu, Jérôme Waser, Philippe Schwaller
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.01061v1](http://arxiv.org/abs/2607.01061v1)
- **PDF:** [https://arxiv.org/pdf/2607.01061v1](https://arxiv.org/pdf/2607.01061v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Computer-assisted synthesis planning breaks target molecules into accessible precursors using large libraries of reaction rules that assign each transformation a deterministic, interpretable label. But chemistry is long-tailed, making manual encoding intractable, and existing tools rely on fixed rulesets that cannot adapt to new chemistries. Here we present a fully automated pipeline in which a multi-agent framework of large language models (LLMs) classifies reactions and writes the rules themselves across 665,901 US patent reactions, generating each rule under a verification loop that tests it against the corpus. It expands a standard taxonomy from 68 to 14,073 classes without human curation. With a lightweight fingerprint classifier, it classifies 97.7\% of unseen reactions, matching a leading proprietary classifier while resolving chemistry more finely and extending on demand to chemistry outside its training distribution. The result is a living reactivity database and a general route to turning generative models into reliable, self-expanding symbolic systems.

</details>


### 44. From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives

- **Authors:** Aayush Aluru, Chloe Ho, Muhammad Hammouri, Kerry Luo, Myra Malik, Ryan Lagasse, Arjun Bahuguna, Vasu Sharma
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00918v1](http://arxiv.org/abs/2607.00918v1)
- **PDF:** [https://arxiv.org/pdf/2607.00918v1](https://arxiv.org/pdf/2607.00918v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> The paper introduces **MAGNET**, a goal‑driven multi‑agent engine that creates long‑form stories by assigning each character a persona‑grounded “agent” that proposes actions according to a shared, explicitly tracked world state and evolving plot goals. A complementary verification module, **ATLAS**, builds graph representations of each scene’s world state and automatically flags inconsistencies or hallucinations. Experiments on 100‑page narratives show that, versus a single‑LLM baseline and the prior IBSEN system, MAGNET cuts annotation effort by ~40 % and reduces factual hallucinations by 45–50 %, while human pairwise rubric scores confirm superior narrative coherence—demonstrating that explicit world‑state tracking and coordinated multi‑agent planning can yield controllable, structurally consistent long‑form fiction.


<details>
<summary>Abstract</summary>

Although large language models (LLMs) have demonstrated impressive creative fiction generation, they struggle to maintain narrative consistency and coherent plot lines in long-form stories. In this work, we introduce a unified framework for long-form narrative generation and verification. MAGNET, a multi-agent goal-driven narrative engine for storytelling, generates stories with persona-grounded character agents that propose actions based on a shared world state and evolving story goals, while ATLAS is a graph-based pipeline that compares scene-level world representations across a generated story to detect hallucinations. By evaluating MAGNET using an LLM editor, pairwise rubric scoring, and ATLAS, we show that our framework produces coherent narratives compared to single-model prompting and IBSEN. At 100 pages, MAGNET reduced annotations and hallucinations by 41 and 50%, respectively, compared to the single model baseline and by 34 and 45%, respectively, compared to IBSEN, with pairwise rubric evaluation showing similar results. These results suggest that long-form narratives can emerge from explicit world-state tracking and goal-driven multi-agent generation, providing a foundation for controllable and structurally coherent long-form narrative generation.

</details>


### 45. Calibrating the Instrument: Controllability of an LLM-Driven Synthetic Population

- **Authors:** Mirko Degli Esposti
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00910v1](http://arxiv.org/abs/2607.00910v1)
- **PDF:** [https://arxiv.org/pdf/2607.00910v1](https://arxiv.org/pdf/2607.00910v1)
- **Categories:** cs.MA


> The paper introduces **SIVE (Synthetic Instrument Validation Experiment)**, a systematic framework for testing the *controllability* of large‑language‑model‑driven synthetic populations: it checks whether the latent attributes that designers embed in agents are reliably reflected in the agents’ collective responses to controlled stimuli. Using a fictional municipality of 120 agents with known trust‑and‑engagement profiles, the authors expose the population to seven institutional messages of graded valence, sweep the LLM temperature parameter, and evaluate seven pre‑registered metrics (fidelity, stability, noise floor, specificity, sensitivity, ordering, and intra‑agent consistency); all metrics are satisfied across temperatures, and a calibration glitch—where a “weakly positive” message is interpreted as negative—reveals that unresolved uncertainty in the text drives the mis‑ordering, which is corrected by rewriting the prompt. The results demonstrate that LLM‑based synthetic agents can produce stable, ordered, and diagnostically useful responses, establishing an internal‑validity baseline that is essential before deploying such agents for external‑validity urban or policy simulations.


<details>
<summary>Abstract</summary>

Generative Synthetic Populations (GSP) -- the convergence of population synthesis, agent-based modelling, and LLM agents -- are attracting growing interest for urban simulation and institutional communication research. Before any GSP instrument is used on a real population, a more basic question must be answered: does it respond to stimuli of known valence in an ordered, replicable, group-structured way? We call this controllability. We ask not whether a synthetic population tracks humans, but whether it tracks itself: whether the latent structure we impose on it is recovered in its own responses. This internal-validity question is logically prior to any claim about external validity, just as characterising an instrument's response function must precede using it to test a theory. We report SIVE (Synthetic Instrument Validation Experiment): a fictional municipality (Montelago) with 120 synthetic personas of known latent structure, exposed to seven conditions spanning strongly positive to strongly negative institutional communications about a water network. Seven pre-registered criteria, evaluated across a temperature sweep, jointly assess fidelity, stability, noise floor, specificity, sensitivity, and ordering. All seven pass at every temperature. A central finding turns a calibration failure into a diagnostic success: a message designed as "weakly positive" was identified by the instrument as functionally negative, traced to unresolved problems, uncertainty, and institutional passivity in its text; a redesigned version restored the expected ordering and interacts with agents' latent trust in unanticipated ways. A noise sub-experiment shows the instrument's intrinsic noise is roughly half the cross-agent estimate and stable across temperatures. Individual trajectories reveal coherent micro-dynamics that summary statistics obscure. Full data are available via an interactive explorer.

</details>


### 46. Self-GC: Self-Governing Context for Long-Horizon LLM Agents

- **Authors:** Xubin Hao, Hongjin Meng, Xin Yin, Jiawei Zhu, Chenpeng Cao
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00692v1](http://arxiv.org/abs/2607.00692v1)
- **PDF:** [https://arxiv.org/pdf/2607.00692v1](https://arxiv.org/pdf/2607.00692v1)
- **Categories:** cs.AI


> The paper introduces **Self‑GC**, a runtime “self‑governing context” system that treats a long‑horizon LLM agent’s dialogue turns, tool outputs, plans, and user constraints as indexed, recoverable objects rather than a flat text stream, and uses a side‑channel planner to decide when to fold, mask, or prune these objects safely. Experiments on a hard‑set benchmark (33 sessions) and a production‑derived suite (332 sessions) show that Self‑GC can delete about 44 % of prefix tokens while preserving 85 %–95 % of future continuations—a marked improvement over heuristic baselines whose no‑impact rates range from 55 % to 70 %. In live deployment the approach cuts average input tokens by 10 %–15 % (up to 20 % at peaks), demonstrating that systematic object‑level context lifecycle management substantially improves token efficiency for long‑horizon LLM agents.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents accumulate tool results, files, plans, and user constraints that are too structured to be treated as a disposable text suffix. Current systems mostly rely on in-run heuristics such as chronological pruning and tool-output masking, or on final self-summary near a context limit. Heuristics are cheap but blind to future dependencies; summaries preserve narrative state but often hide exact evidence, locators, and editable artifacts. We present Self-GC, where GC denotes self-governing context while deliberately echoing garbage collection: the system does not merely reclaim unused tokens, but governs the lifecycle of agent context objects. Self-GC turns user turns, tool spans, and skill state into indexed objects; asks a side-channel planner to propose fold, mask, and prune actions; and lets the harness enforce recoverable sidecars, safe commit boundaries, and cache-aware commit. On a 33-session Hard Set, Self-GC prunes 43.95% of prefix tokens while leaving 84.85% of future continuations unaffected, compared with no-impact rates of 54.55% to 69.70% for heuristic baselines. On a 332-session production-derived suite, three planner backbones reach no-impact rates of 91.27% to 94.58%, while baselines remain at 77.71% to 87.46%. In production, an online account-level split reduces daytime average input tokens by 10% to 15%, with peak reductions near 20%. These results point to context management as runtime lifecycle control over indexed, recoverable objects rather than post hoc text cleanup.

</details>


### 47. AGI Maze as a Benchmark Framework for World-Modeling Agents

- **Authors:** Alexey Potapov
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00627v1](http://arxiv.org/abs/2607.00627v1)
- **PDF:** [https://arxiv.org/pdf/2607.00627v1](https://arxiv.org/pdf/2607.00627v1)
- **Categories:** cs.AI


> The paper introduces **AGI Maze**, a lightweight benchmark suite of grid‑based mazes that forces agents to build and manipulate persistent world models under partial observability, without relying on high‑dimensional sensory data. The authors evaluate vanilla large language models (LLMs) on these tasks and show that, when used in their standard next‑token‑prediction mode, the models cannot internally represent the maze layout; a simple baseline that treats the LLM’s message history as working memory improves results but still fails to solve even modest mazes within generous step limits. The work therefore provides a concrete, scalable testbed for measuring and advancing world‑modeling capabilities in agentic AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably produce persistent, manipulable representations of an external world. Many tasks that look like "reasoning" in text become substantially harder once the environment is partially observable, stateful, and requires memory and structured hypotheses about hidden state. AGI Maze is a lightweight framework for building such environments without requiring high-dimensional sensory inputs. It provides a family of grid-based maze tasks with a clean API and multiple difficulty regimes. The goal is to create benchmarks where agents must learn and use world state representations, not just infer a local rule over readily provided observations. We provide an initial evaluation of several vanilla LLMs on simple mazes showing that they fail to represent mazes internally at LLM inference time. We also introduce a baseline agent, which is allowed to use its message history as a working memory to construct descriptions of observations at agentic runtime. Although this can improve performance, it is still insufficient for an LLM agent to reliably solve even small mazes within a step budget that is more than enough for humans.

</details>


### 48. EgoGapBench: Benchmarking Egocentric Action Selection in Multi-Agent Scenes

- **Authors:** Jihyeok Jung, Jeewu Lee, Sanghyeop Kim, Chanhee Han, Seong Joon Oh
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00547v1](http://arxiv.org/abs/2607.00547v1)
- **PDF:** [https://arxiv.org/pdf/2607.00547v1](https://arxiv.org/pdf/2607.00547v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces **EgoGapBench**, a diagnostic benchmark that isolates the ability to choose actions from a true egocentric perspective (Egocentric Action Selection, EAS) in multi‑agent scenes, independent of first‑person visual cues. The authors construct a set of scenarios where agents must select actions based only on their own viewpoint while other agents are visible, then evaluate humans, open‑source and commercial multimodal large language models (MLLMs), and fine‑tuned variants. Results show that humans solve the tasks reliably, whereas MLLMs consistently err by copying actions of other agents; standard fine‑tuning on existing egocentric datasets does not help, and only direct fine‑tuning on EgoGapBench data yields modest improvements, still well below human level. This demonstrates that egocentric action‑selection is a distinct, hard‑to‑learn skill not captured by current first‑person data, calling for dedicated evaluation and training of agentic AI systems on egocentric reasoning tasks.


<details>
<summary>Abstract</summary>

Existing egocentric benchmarks have primarily constructed the egocentric setting from first-person-view data, which makes it difficult to evaluate egocentric perspective itself in isolation. However, understanding first-person-view input and taking an egocentric perspective are separable abilities, especially when first-person body cues are absent or when other agents are present. To isolate egocentric perspective understanding, we introduce EgoGapBench, a diagnostic benchmark for measuring action selection in multi-agent egocentric scenes. We define the ability measured by this benchmark as Egocentric Action Selection (EAS): selecting an appropriate action from the agent's perspective in the presence of other agents. On EgoGapBench, humans answer reliably, whereas both open-source and proprietary MLLMs perform substantially worse and systematically select actions performed by other visible agents. Fine-tuning on existing egocentric data fails to close this gap and can even be detrimental. In contrast, fine-tuning on EgoGapBench training data improves accuracy but does not reach human performance. These results show that EAS is difficult to acquire from first-person-view data alone, and that MLLMs should be evaluated and trained not only for scene understanding but also for egocentric action selection.

</details>


### 49. AI Native Games: A Survey and Roadmap

- **Authors:** Zhiyue Xu, Fandi Meng, Kaijie Xu, Clark Verbrugge, Simon Lucas, Jian Zhao
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00527v1](http://arxiv.org/abs/2607.00527v1)
- **PDF:** [https://arxiv.org/pdf/2607.00527v1](https://arxiv.org/pdf/2607.00527v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative AI now enables games to produce dialogue, quests, characters, images, and worlds at runtime. Yet generation alone does not make a game AI-native, nor does it guarantee playability. This paper defines AI-native games by whether runtime generative AI is constitutive of the core loop: if the AI component were removed or trivially replaced, the central form of play would collapse or become fundamentally different. This counterfactual criterion separates AI-native games from AI-augmented games, boundary artifacts, chatbots, tavern-style role-play, procedural content generation, and AI-assisted production. Using this definition, we screen candidate artifacts and analyze 53 publicly available AI-native games and prototypes. We introduce a dual-axis G/N taxonomy: the G-axis captures player-facing game type, while the N-axis captures the dominant AI mechanic that makes generative AI indispensable to play. The corpus is concentrated around language-forward designs, especially narrative adventure, epistemic interaction, and generative narrative, while categories such as semantic adjudication, multi-agent simulation, generative construction, and relationship/companion play remain less represented. We argue that the central design problem is organizing semantic openness into stable gameplay. AI-native design depends on mechanical invariants: goals, rules, state, feedback, pacing, and player agency that make open-ended AI outputs interpretable and consequential. We conclude with a roadmap for controllable generation, AI-as-mechanic design, multimodal and multi-agent systems, inference economics, evaluation, safety, and regulation.

</details>


### 50. Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware Agricultural Advisory Generation

- **Authors:** Vedant Balasubramaniam, Geetha Charan, Manojkumar Patil, Rohit P Suresh, V Priyanka, Kodur Sai Vinay Sathvik, Y. Narahari
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00454v1](http://arxiv.org/abs/2607.00454v1)
- **PDF:** [https://arxiv.org/pdf/2607.00454v1](https://arxiv.org/pdf/2607.00454v1)
- **Categories:** cs.AI, cs.MA


> **Contribution:** The paper introduces **Agri‑SAGE**, a closed‑loop, simulation‑grounded multi‑agent framework that couples large language models (LLMs) with the APSIM crop‑growth simulator to produce context‑aware agricultural advisories that are both evidence‑based and responsive to in‑season variability.  

**Methodology:** Agri‑SAGE implements three LLM reasoning pipelines—Plan‑and‑Solve, Tree of Thoughts, and Reflexion—within a multi‑agent architecture that (1) retrieves relevant agronomic knowledge, (2) generates advisory actions, (3) validates them through APSIM biophysical simulations, and (4) feeds the simulation outcomes back into the agents (Reflexion additionally exploits cross‑season episodic memory).  

**Key Findings:** Across a ten‑year retrospective study, all three pipelines significantly outperformed static “Package‑of‑Practice” guidelines; Tree of Thoughts achieved the highest peak yields, while Reflexion matched the agronomic performance of the more expensive pipelines with far lower computational cost, demonstrating that episodic memory‑enhanced reasoning can deliver efficient, high‑quality, context‑aware recommendations for agentic AI in agriculture.


<details>
<summary>Abstract</summary>

Agricultural advisory systems face a fundamental tension: static agronomic guidelines offer consistent, evidence-based recommendations, yet remain blind to in-season variability and dynamic uncertainties. Recent advisory systems powered by LLMs are liable for a different risk of generating recommendations that are agronomically credible but physiologically unconvincing. Agri-SAGE is a closed-loop framework designed to resolve the above two limitations by integrating retrieval-grounded multi-agent LLM reasoning with APSIM-based biophysical simulation, to generate and validate agronomic advisories. To assess this framework, we evaluate three reasoning approaches, namely Plan-and-Solve, Tree of Thoughts, and Reflexion, over a 10-year retrospective analysis. All three significantly outperform static PoP (Package-of-Practice) baselines, with Tree of Thoughts achieving impressive peak yields. At the same time, Reflexion achieves comparable agronomic outcomes at substantially lower computational cost by leveraging cross-seasonal episodic memory.

</details>


### 51. Personalization as Inverse Planning: Learning Latent Design Intents for Agentic Slide Generation via Structural Denoising

- **Authors:** Tianci Liu, Zihan Dong, Linjun Zhang, Haoyu Wang, jing Gao, Emre Kiciman, Ranveer Chandra, Wei-Ting Chen
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00407v1](http://arxiv.org/abs/2607.00407v1)
- **PDF:** [https://arxiv.org/pdf/2607.00407v1](https://arxiv.org/pdf/2607.00407v1)
- **Categories:** cs.AI


> **Main contribution**  
The paper reframes page‑level slide personalization as an *inverse planning* problem and introduces **SPIRE**, a novel two‑agent framework that learns latent design intents without requiring explicit knowledge of the target slide‑authoring tool (PowerPoint, LaTeX‑Beamer, etc.).  

**Methodology**  
SPIRE creates a *structural denoising* task by deliberately corrupting the visual structure of clean slides; two RL agents then cooperate to reconstruct the original design, treating the denoising objective as a consistent surrogate for the original personalization problem. The authors prove that this surrogate yields unbiased gradient estimates and that the multi‑agent formulation reduces policy‑gradient variance.  

**Key findings**  
Experiments on several slide‑generation benchmarks show that SPIRE outperforms template‑based and instruction‑following baselines in both visual quality and fidelity to user‑specific design intents, demonstrating that structural denoising is an effective and scalable way to endow agentic AI systems with fine‑grained, tool‑agnostic design personalization capabilities.


<details>
<summary>Abstract</summary>

Slide design requires personalizing both deck themes and page layouts. Yet, current AI agent-based methods struggle with fine-grained, page-level design. Solely relying on prespecified templates or user verbose instructions, they fail to capture latent design intents, leaving Page-level Slide Personalization (PSP) unresolved. To close this gap, this work formulates PSP as an inverse planning problem. We propose to learn a design intent without assuming any knowledge of the specific executing tools (e.g., PowerPoint, Beamer) being used. However, relinquishing control over these tools makes the problem intractable to optimize end-to-end. To overcome this, we propose SPIRE, a principled framework to solve PSP approximately. By intentionally corrupting the visual structures of clean slides, SPIRE creates a verifiable task to denoise the corruption, whereby two agents learn to collaboratively refine executable designs via reinforcement learning (RL). We present a proof that structural denoising is a consistent surrogate for PSP, and that the multi-agent formulation strictly reduces policy gradient variance in RL. Extensive experiments demonstrate the superiority of SPIRE.

</details>


### 52. When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic Retrieval Buffers

- **Authors:** Yushi Sun, Bowen Cao, Wai Lam
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00394v1](http://arxiv.org/abs/2607.00394v1)
- **PDF:** [https://arxiv.org/pdf/2607.00394v1](https://arxiv.org/pdf/2607.00394v1)
- **Categories:** cs.DB, cs.CL


> **Main contribution:** The paper identifies that traditional cache replacement heuristics (LRU, LFU) are ill‑suited for semantic retrieval buffers used by LLM agents and introduces **SOLAR**, a learning‑augmented replacement framework that combines regret‑based timing with Bayesian online selection of items to retain.

**Methodology:** The authors formalize semantic cache replacement as an online problem with continuous hit quality and switching costs, prove competitive‑ratio and regret bounds for SOLAR (constant ≤ 3 competitive ratio, regret = O(√KT log T)), and evaluate it on two MemoryBench‑Full datasets (LoCoMo, DialSim) against eight baseline policies, supplemented by large‑scale synthetic experiments.

**Key findings:** SOLAR consistently outperforms FIFO (the strongest classic baseline) by 5–75 % on tight cache sizes, while classic LRU/LFU underperform FIFO due to lack of temporal locality. The experiments also reveal a phase transition at the working‑set size and an inverted‑U relationship between pool size and retrieval quality, supporting the view that buffer capacity limits act as a source of retrieval noise rather than mere storage constraints.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on retrieval buffers to store and reuse past experience, yet the cache management policies governing these buffers remain largely ad-hoc. We formalize this as an online semantic cache replacement problem with switching costs, where items are matched by embedding similarity and hit quality is continuous rather than binary. Through experiments on two datasets from MemoryBench-Full (LoCoMo, DialSim) with 8 replacement policies, we reveal a surprising finding: classic heuristics (LRU, LFU) \emph{consistently underperform} the naive FIFO baseline on semantic workloads, due to the absence of temporal locality and frequency concentration. We propose SOLAR, a learning-augmented framework that derives modification timing from regret accumulation (achieving $\sim$17\% modification rate) and content selection from Bayesian online learning over implicit retrieval feedback. We prove SOLAR achieves a constant competitive ratio $\leq 3$, independent of cache size and horizon (vs.\ $Ω(K)$ for FIFO), and eviction regret $O(\sqrt{KT\log T})$, matching the $Ω(\sqrt{KT})$ lower bound up to logarithmic factors. Experiments demonstrate 5--75\% relative improvement over FIFO at tight cache sizes, with a clearly characterized phase transition at the working set boundary. Synthetic experiments with 5000-item pools further reveal an inverted-U relationship between pool size and retrieval quality, justifying capacity constraints as a retrieval noise phenomenon rather than a storage limitation.

</details>


### 53. TRACE: State-Aware Query Processing over Temporal Evidence Graphs for Conversational Data

- **Authors:** Maolin Wang, Yu Wang, Zichun Liu, Baiyuan Qiu, Chenbin Zhang, Jiguang Shen, Haoran Yang, Hao Miao
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00339v1](http://arxiv.org/abs/2607.00339v1)
- **PDF:** [https://arxiv.org/pdf/2607.00339v1](https://arxiv.org/pdf/2607.00339v1)
- **Categories:** cs.CL


> **Contribution:** The paper introduces **TRACE**, a query‑processing framework that enables state‑aware reasoning over long, evolving conversational histories by representing them as **temporal evidence graphs** with explicit update, contradiction, and causal edges.  

**Methodology:** Conversations are modeled as a hierarchical graph (events → sessions → topics) enriched with typed temporal relations and **validity annotations** that mark facts as current or obsolete. At query time, TRACE first retrieves candidate notes with dense vectors, then uses the graph to seed a **validity‑aware evidence search** that assembles temporally grounded multi‑hop paths, feeding these paths as a hybrid context to the answer generator.  

**Key Findings:** Across several long‑conversation QA benchmarks, TRACE yields significant gains in temporal and multi‑hop reasoning accuracy compared with baseline long‑memory pipelines that treat memories as independent text/vector blobs. Ablation studies confirm that the hierarchical graph structure, update‑aware seeding, and path‑grounded evidence are essential for the observed performance improvements, highlighting the utility of explicit state modeling for agentic AI systems.


<details>
<summary>Abstract</summary>

Conversational data is increasingly used as a persistent source of user state for long-running assistants and AI agents. However, querying this data remains challenging because conversations naturally evolve: plans are revised, preferences change, and later messages frequently supersede or contradict earlier information. Existing long-memory pipelines largely treat memories as independent text or vector objects. This approach often retrieves semantically similar but stale evidence, offering limited support for state-aware reasoning. To address this problem, we present TRACE, a query processing framework over temporal evidence graphs for evolving conversational data. TRACE models conversations as a hierarchical graph spanning events, sessions, and topics, enriched with typed temporal, causal, update, and contradiction relations. Crucially, the framework maintains validity annotations so obsolete facts remain accessible for historical queries but are discounted for current-state answers. At query time, TRACE combines vector-based note retrieval with graph-guided evidence search, generating validity-aware support paths and a hybrid context for answer generation. This design separates lexical recall from evidence reconstruction, enabling bounded query-time reasoning over long conversational histories. Experiments on long-conversation query-answering (QA) benchmarks show that TRACE improves temporal and multi-hop reasoning, with ablations highlighting the importance of hierarchy, update-aware seeding, and path-grounded evidence.

</details>


### 54. Managed Autonomy at Runtime: Gear-Based Safety and Governance for Single- and Multi-Agent Cyber-Physical Systems

- **Authors:** Srini Ramaswamy, Wang Miaosheng
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00334v1](http://arxiv.org/abs/2607.00334v1)
- **PDF:** [https://arxiv.org/pdf/2607.00334v1](https://arxiv.org/pdf/2607.00334v1)
- **Categories:** cs.AI


> The paper introduces **\system{}**, a discrete‑time “gear‑based” runtime controller that partitions an autonomous agent’s execution into five tightly regulated modes (observation, suggestion, planning, execution, and integration) and gates transitions with utility‑based dispatch and event‑driven fallbacks. By formally proving monotonic stability, safety, and eventual convergence for a single agent—and extending the framework with consensus gating, swarm‑level Lyapunov analysis, and per‑agent gear authority to guarantee zero‑collision safety in multi‑agent cyber‑physical systems—the authors embed micro‑level permission checks within the higher‑level \smart{} governance lifecycle. Empirical evaluation on a three‑UR5 robotic assembly cell (10 k Monte‑Carlo runs) shows a 99.6 % anomaly‑detection rate (vs. 2.1 % baseline), a 3.5× reduction in detection latency, and the generation of formal workspace‑safety certificates, demonstrating that gear‑based managed autonomy can provide scalable safety and stability guarantees for both single‑ and multi‑agent AI systems.


<details>
<summary>Abstract</summary>

Autonomous agents, whether LLM-driven software agents or robotic physical agents, face a common class of failure modes when operating without continuous human oversight: safety violations from unverified actions, behavioral instability from unconstrained loops, and continuity loss from unhandled error states. We develop \system{}, a discrete-time control system that combines five execution gears (\Gobs{}, \Gsug{}, \Gplan{}, \Gexec{}, \Gint{}) with utility-gated dispatch and event-driven fallback. For the single-agent case, we prove monotonic stability, execution safety, eventual stabilization, fallback completeness, and equivalence to a gear-constrained Markov decision process. For multi-agent cyber-physical systems (CPS), we apply the established \smart{} managed-autonomy lifecycle and map runtime evidence into its four governance states (\Stable{}/\Meta{}/\Assisted{}/\Regulated{}). Consensus gating, swarm-level Lyapunov analysis, per-agent gear authority, and rendezvous control provide distributed safety and stability guarantees, including zero collision under the stated assumptions. We evaluate the resulting runtime on a three-agent UR5 robotic assembly cell using fault magnitudes calibrated from the NIST \emph{Degradation Measurement of Robot Arm Position Accuracy} dataset across 10,000 Monte Carlo episodes. It achieves a 99.6\% anomaly detection rate versus 2.1\% for the single-agent baseline, reduces detection latency by $3.5\times$, and supplies a formal physical-workspace safety certificate. The execution gears act as micro-level permissions beneath the \smart{} runtime governance states, separating action control from autonomy governance.

</details>


### 55. EPC: A Standardized Protocol for Measuring Evaluator Preference Dynamics in LLM Agent Systems

- **Authors:** Zewen Liu
- **Published:** 2026-07-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00297v1](http://arxiv.org/abs/2607.00297v1)
- **PDF:** [https://arxiv.org/pdf/2607.00297v1](https://arxiv.org/pdf/2607.00297v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces EPC (Evaluator Preference Coupling), a rigorously defined, RFC‑style protocol that standardizes how to measure and track the propagation of evaluator bias into the strategy distribution of LLM agents operating in feedback loops. By formalizing a four‑phase isolation paradigm—including executor/evaluator setup, task and strategy design, the TTRL update rule, and a suite of metrics (γ, Jensen‑Shannon divergence, Expected Calibration Error, Brier score)—the authors supply a versioned reference snapshot (v1.0) with 122 reproducible experiments across eight evaluator families (e.g., GPT‑4o, Qwen, DeepSeek) and a clear version‑ing scheme for future comparisons and decay detection. Empirical results demonstrate that evaluator preference coupling is pervasive, varies systematically across evaluator generations, and decays as proprietary evaluators are silently updated, thereby providing the agentic‑AI community with a reproducible baseline and open‑source tooling for ongoing bias‑impact assessment.


<details>
<summary>Abstract</summary>

When LLM agents use evaluator feedback to adapt their behavior in closed loops, evaluator biases propagate through the agent's strategy distribution -- a phenomenon known as evaluator preference coupling. Prior work has documented coupling across multiple evaluator families and model versions, but the field lacks a standardized protocol that enables third-party researchers to (i) reproduce coupling measurements, (ii) compare results across evaluators and time points, and (iii) detect measurement decay as proprietary evaluators silently update. This paper provides the protocol. We specify EPC (Evaluator Preference Coupling) -- a detailed, RFC-style protocol specification for the four-phase isolation paradigm, covering executor and evaluator configuration, strategy and task design, the TTRL update rule, metric computation (gamma, JSD, ECE, Brier), and output schema. We accompany the protocol with a versioned Reference Snapshot v1.0: coupling measurements for eight evaluator conditions (N=122 unique experimental repetitions across GPT-4o, Qwen, DeepSeek, and others) derived from five independent studies, annotated with evaluator version identifiers, API endpoints, and measurement dates. The snapshot is explicitly time-bound: all values are conditional on specific model versions and are expected to decay as proprietary evaluators update. We define a versioning convention (vX.Y-Z, encoding protocol version, snapshot version, and evaluator generation) and provide a usage guide covering adoption, interpretation, and known pitfalls. The protocol, reference snapshot, and implementation code are released as open infrastructure.

</details>


### 56. From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents

- **Authors:** Yashar Talebirad, Eden Redman, Ali Parsaee, Osmar R. Zaiane
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00233v1](http://arxiv.org/abs/2607.00233v1)
- **PDF:** [https://arxiv.org/pdf/2607.00233v1](https://arxiv.org/pdf/2607.00233v1)
- **Categories:** cs.AI, cs.CL, cs.IT, cs.MA


> The paper shows that the internal memory architecture of large‑language‑model (LLM) agents is the decisive factor in whether they can bootstrap a stable, shared language in a Lewis signaling game, outweighing the effects of raw communication bandwidth. By systematically evaluating five memory designs—including stateless rolling contexts and agents equipped with a persistent “notebook” external memory—across a range of channel capacities, the authors find that notebook‑based agents exploit surplus capacity to externalize and retain conventions, achieving the highest coordination success (0.867 ± 0.023 at capacity = 25), whereas stateless agents peak at moderate capacity and then collapse as the vocabulary exceeds what their context window can track. The results overturn the naive information‑bottleneck prediction that optimal capacity equals the number of objects, demonstrating that surplus capacity combined with persistent memory yields robust language emergence, a insight that clarifies how memory structure and channel resources jointly shape agentic communication.


<details>
<summary>Abstract</summary>

How do two agents invent a shared language from scratch? In a Lewis signaling game, a sender and receiver must coordinate on a code using only their interaction history. We study five memory architectures across varying channel configurations with LLM agents and find that memory architecture matters more than channel capacity. Agents with a persistent private notebook benefit from surplus channel capacity and avoid the high-capacity collapse seen in stateless agents, achieving the most reliable coordination ($0.867 \pm 0.023$ at capacity = 25). Stateless agents peak at moderate capacity and then degrade as the vocabulary grows beyond what a rolling context window can track The notebook externalizes learned conventions, freeing agents from having to re-derive codes each round. An information bottleneck-inspired argument predicts an optimal capacity equal to the number of objects. Instead, the bottleneck (capacity = 8) proves to be a fragility point, and surplus capacity is generally better. We show that channel capacity alone cannot predict coordination; memory architecture determines whether agents turn interaction history into stable conventions, and both dimensions are needed to understand how signals become language.

</details>


### 57. A Contextual-Bandit Oversight Game with Two-Sided Informational Asymmetry

- **Authors:** Yunjin Tong
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00155v1](http://arxiv.org/abs/2607.00155v1)
- **PDF:** [https://arxiv.org/pdf/2607.00155v1](https://arxiv.org/pdf/2607.00155v1)
- **Categories:** cs.AI, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study runtime human oversight of an AI agent when private information runs in both directions: the human privately knows her reward function, while the AI privately knows the quality of the action it proposes. This is the kind of asymmetry that arises naturally when an autonomous robot or software agent has inspected a situation its human supervisor cannot directly assess. Building on Cooperative Inverse Reinforcement Learning (CIRL) and the Oversight Game, we introduce a contextual-bandit team game with two-sided asymmetric information and a play/ask/trust/oversee interface. The bandit structure removes physical state transitions and thereby yields exact one-shot characterizations that would remain conjectural in the full POMDP setting, though the common belief remains a dynamically controlled state across rounds. We give two one-shot characterizations, a team optimum and a behaviorally natural myopic rule, whose gap is a slab of avoidable harm: a region in which the AI privately knows the proposed action is harmful and shutdown would help, yet a myopic human, trusting her prior, declines to oversee. We show this gap is the price of non-credible oversight communication, and give a partial analysis of how it resolves dynamically over repeated rounds through passive learning and active signaling with a one-period-lagged oversight response.

</details>


### 58. QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents

- **Authors:** Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, Joschka Strüber, Ameya Prabhu, Matthias Bethge
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.32034v1](http://arxiv.org/abs/2606.32034v1)
- **PDF:** [https://arxiv.org/pdf/2606.32034v1](https://arxiv.org/pdf/2606.32034v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> The paper introduces **QVal**, a training‑free benchmark that directly measures how well dense supervision signals for long‑horizon LLM agents rank actions according to the Q‑values of a strong reference policy, thereby isolating signal quality from downstream training and engineering effects. Using QVal‑v1.0, the authors evaluate 21 dense‑supervision methods spanning seven methodological families across four environments and six open‑weight models, conducting over 1.2 K experiments. Their results show that simple prompting baselines consistently beat more recent dense‑supervision techniques and that performance clusters tightly by method family, a pattern that holds across model sizes, tasks, and observation modalities.


<details>
<summary>Abstract</summary>

LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream performance of a training pipeline that integrates them. This is expensive, conflates supervision quality with training engineering confounders, and renders different methodological families requiring distinct training setups incomparable. As a result, dense supervision methods are rarely benchmarked on common ground. We introduce QVal, a training-free testbed for directly evaluating dense supervision signals. Given a state-action pair, QVal measures how well a method's score is Q-aligned: whether it orders actions according to the Q-values of a strong reference-policy. This lets us compare signals before any training run and separate signal quality from other engineering choices. We instantiate QVal as QVal-v1.0, benchmarking 21 dense supervision methods across four diverse environments and seven methodological families, with over 1.2K evaluation experiments across six open-weight model backbones. We find that simple prompting baselines consistently outperform recent dense supervision methods from the literature, and that performance clusters strongly by family. These findings hold across model sizes, environments, and observation modalities. QVal is designed to be easily extensible to new environments and methods, enabling researchers to iterate on dense supervision methods before any training run.

</details>


### 59. Generative Skill Composition for LLM Agents

- **Authors:** Xinyu Zhao, Zhen Tan, Vaishnav Tadiparthi, Nakul Agarwal, Kwonjoon Lee, Ehsan Moradi Pari, Hossein Nourkhiz Mahjoub, Tianlong Chen
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.32025v1](http://arxiv.org/abs/2606.32025v1)
- **PDF:** [https://arxiv.org/pdf/2606.32025v1](https://arxiv.org/pdf/2606.32025v1)
- **Categories:** cs.CL


> The paper introduces **SkillComposer**, a structured‐skill‑composition model that predicts, in a single autoregressive pass, exactly which LLM‑agent skills to use, how many, and in what order for a given task. By training on a curated dataset of task‑skill pairs and using a constrained decoder over skill identifiers, SkillComposer jointly captures subset selection, cardinality, and sequencing, outperforming both naïve exposure of all skills and embedding‑based retrieval methods. Experiments on the SkillsBench benchmark with GPT‑5.2‑Codex and Gemini‑3‑Pro‑Preview show that SkillComposer boosts pass rates by 18–23 percentage points over a no‑skill baseline, matches the gold‑skill upper bound, and does so with fewer prompt tokens than top‑3 retrieval approaches.


<details>
<summary>Abstract</summary>

Recent LLM agents benefit from skills for solving complex tasks. Skills encapsulate modular packages of procedural knowledge and instructions for performing specialized tasks, such as setting up a sandboxed environment, running a test suite, or refactoring a function across multiple files. As skill libraries grow and become reusable across tasks and domains, selecting an appropriate skill composition has emerged as a central bottleneck. Existing approaches fall into two categories. One exposes the agent's reasoning to the entire skill collection; the other performs skill retrieval via embeddings or LLM-based rerankers. Both provide useful insights; however, they miss the structural nature of skill composition, which is a joint decision over which skills, how many, and in what order -- three dimensions that cannot be decoupled. We formalize this as structured skill composition: given a task and a skill library, predict an executable skill plan that jointly specifies the activated subset, count, and execution order. We propose SkillComposer, which instantiates structured skill composition as task-conditioned skill sequence prediction. SkillComposer uses a constrained autoregressive decoder over skill identifiers, so subset, count, and order emerge jointly from a single decoding pass, and dependencies between successive skills are captured naturally. We build a training set of task-composition pairs from a real, human-curated skill library. We then evaluate SkillComposer along two axes: composition quality on a held-out test set, and downstream task success on SkillsBench across two production-grade coding agents. On GPT-5.2-Codex, Gemini-3-Pro-Preview, SkillComposer raises the pass rate by +23.1, +18.2pp over the no-skill baseline, surpassing top-3 retrieval and matching the gold-skill retrieval upper bound at lower prompt-token cost.

</details>


### 60. TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling in Forestry via Compiled Expert Rules and Vision-Language Models

- **Authors:** Shiyi Chen, Nicholas Saban, Collin Hargreaves, Huiqi Wang
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31976v1](http://arxiv.org/abs/2606.31976v1)
- **PDF:** [https://arxiv.org/pdf/2606.31976v1](https://arxiv.org/pdf/2606.31976v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human-labeled data are widely used as reference annotations in ML, despite known variability across annotators in many expert-driven domains. In addition, expert annotation is slow, inconsistent, and remains a major bottleneck for scaling tasks like tree height bias classification in forestry remote sensing. We propose a multi-agent system (MAS) that orchestrates expert decision trees with Vision-Language Models (VLMs), treating the decision tree as a structural prior while VLMs perform localized semantic perception at individual nodes, with multi-agent voting to mitigate VLM stochasticity. We formalize a Decoupled Declarative Decision (D3) Framework that enables zero-modification generalization across diverse expert-defined decision structures. On a tree bias classification testbed, our framework outperforms supervised ML baselines and reduces the amount of expert labeling effort required. These results suggest that agentic orchestration of VLMs with expert priors can reproduce expert-defined labeling procedures at substantially lower annotation cost while maintaining interpretability.

</details>


### 61. MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments

- **Authors:** Qingyun Liu, Jiwen Zhang, Jingyi Hu, Siyuan Wang, Zhongyu Wei
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31966v1](http://arxiv.org/abs/2606.31966v1)
- **PDF:** [https://arxiv.org/pdf/2606.31966v1](https://arxiv.org/pdf/2606.31966v1)
- **Categories:** cs.MA, cs.AI, cs.CL, cs.CV


> The paper introduces **MECoBench**, the first systematic benchmark for evaluating how multimodal large language models (MLLMs) cooperate as embodied agents across a suite of real‑world tasks, two team structures, and three interaction modes (shared‑policy, leader‑follower, and peer‑to‑peer). By integrating a controllable simulation platform with a diverse task set, the authors run extensive experiments on several state‑of‑the‑art MLLMs, showing that (1) collaborative agents consistently achieve higher task success than solitary agents but only when the gain from joint reasoning outweighs the coordination overhead, (2) explicit communication is a prerequisite for these gains and the optimal collaboration mode varies with team size and model capability, and (3) collaborative teams are markedly more robust to noisy priors and exploratory disturbances. These findings delineate the mechanisms and limits of multimodal embodied cooperation, providing a valuable testbed for future agentic‑AI research.


<details>
<summary>Abstract</summary>

Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration generally improves embodied task completion, but its benefits depend on balancing collaborative gains against coordination complexity. (ii) Communication is essential to collaboration gains, while the best collaboration mode depends on team size and model capability. (iii) Moreover, collaboration improves robustness under noisy priors and exploration conditions. Generally, MECoBench provides a systematic testbed for understanding the mechanisms and limits of multimodal embodied collaboration. Code and dataset are available at https://github.com/q-i-n-g/MECoBench.

</details>


### 62. Better Understanding, Understanding Better

- **Authors:** Yu Wei
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31892v1](http://arxiv.org/abs/2606.31892v1)
- **PDF:** [https://arxiv.org/pdf/2606.31892v1](https://arxiv.org/pdf/2606.31892v1)
- **Categories:** cs.LO, cs.AI


> **Main contribution:** The paper introduces a new comparative epistemic logic that formalizes *understanding*—including its graded, comparative, and “why‑because” aspects—within multi‑agent systems, filling a gap in epistemic logic where only knowledge has been formally treated.

**Methodology:** The authors extend standard multi‑agent Kripke models with agent‑indexed graded explanation structures and a justification‑style term algebra, defining level‑indexed “understands‑why” modalities and a comparative connective. They develop a finitary bounded‑level calculus (decidable for each fixed level) and an infinitary full‑language system, and prove soundness, strong completeness, and decidability results.

**Key findings for agentic AI:** The framework can represent and reason about varying depths of an AI system’s understanding (e.g., minimal vs. ideal explanations) and compare its explanatory competence to that of other agents, providing a logical foundation for evaluating and improving the “understanding” capabilities of intelligent agents.


<details>
<summary>Abstract</summary>

"Any fool can know; the point is to understand." A well-known remark often attributed to Einstein captures a widely shared intuition: understanding is more than merely knowing. Yet epistemic logic has paid relatively little attention to understanding, despite its central role in contemporary epistemology, philosophy of science, and recent debates about AI. A recurring theme in the philosophical literature is that, unlike knowledge, understanding comes in degrees: one may understand something more or less well, and one's understanding may be better than another's. We introduce a comparative epistemic logic of understanding with level-indexed understanding modalities and a comparative connective for saying that one agent understands why a proposition better than another agent does. Semantically, we enrich multi-agent epistemic models with agent-indexed graded explanation structures and a justification-style term algebra. This yields a unified framework for representing minimal, ordinary, more demanding, and ideal understanding, together with comparisons between agents with respect to the same formula at issue. We distinguish a finitary bounded-level calculus from an infinitary full-language companion system. We establish soundness and strong completeness, and show that each fixed finite-level fragment is decidable.

</details>


### 63. Analytic Cut in Epistemic Logics with Distributed Knowledge

- **Authors:** Ryo Murai, Sizhuo Liu, Katsuhiko Sano
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31886v1](http://arxiv.org/abs/2606.31886v1)
- **PDF:** [https://arxiv.org/pdf/2606.31886v1](https://arxiv.org/pdf/2606.31886v1)
- **Categories:** cs.MA, cs.LO


> **Main contribution**  
The paper introduces sequent calculi for multi‑agent epistemic logics that include the distributed‑knowledge operator (based on the modal systems K45, KD45 and S5) and proves that, although full cut elimination fails, these calculi enjoy the **analytic cut** property—cuts can be confined to subformulas of the cut’s conclusion. From this, Craig interpolation for all three logics follows, and the results also hold when the operator is extended to the empty group (interpreted as a global modality).

**Methodology**  
Adapting Takano’s (2018) technique, the authors design inference rules for distributed knowledge and show that any proof can be transformed so that every cut formula is a subformula of the sequent’s end‑formula. The proof proceeds by a systematic reduction of arbitrary cuts, carefully handling the interaction between the intersection‑based accessibility for distributed knowledge and the underlying modal axioms (K45, KD45, S5).

**Key findings for agentic AI**  
- Analytic cut provides a **tighter proof‑theoretic control** for reasoning about what groups of agents jointly know, which is essential for verification and synthesis of cooperative AI systems.  
- The derived **Craig interpolation theorem** enables modular construction of knowledge bases: any entailment can be split into an intermediate formula using only the shared vocabulary, facilitating compositional design of multi‑agent protocols.  
- Extending the results to the empty group shows that the framework can uniformly handle both **distributed knowledge** and **global (common) knowledge**, broadening its applicability to hierarchical or centrally coordinated AI architectures.


<details>
<summary>Abstract</summary>

Distributed knowledge is a notion of group knowledge studied in multi-agent epistemic logic. Semantically, the distributed knowledge of a group is interpreted via an accessibility relation given by the intersection of the epistemic accessibility relations of the agents in that group. This paper investigates sequent calculi for epistemic logics of distributed knowledge based on K45, KD45, and S5. While cut elimination holds in existing sequent calculi for modal logics K45 and KD45, it fails in all the systems mentioned above. Instead, we establish the analytic cut property for all three systems by adapting Takano' s (2018) strategy, which restricts the cut formulas to the set of subformulas of the conclusion of the cut rule. As a corollary, the Craig interpolation theorem holds for all logics considered. We also show that all proof-theoretic results remain valid when the empty group is allowed for the distributed-knowledge operator, in which case the distributed knowledge for the empty group is interpreted as the global modality.

</details>


### 64. Inquisitive Action Logic

- **Authors:** Ivano Ciardelli
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31866v1](http://arxiv.org/abs/2606.31866v1)
- **PDF:** [https://arxiv.org/pdf/2606.31866v1](https://arxiv.org/pdf/2606.31866v1)
- **Categories:** cs.LO, cs.MA


> **Main contribution**  
The paper proposes **Inquisitive Action Logic (InqAL)**, a novel multi‑agent modal framework that extends traditional action logics by allowing agents to reason not only about *which* outcomes they can force but also about the *questions* they resolve through their actions—i.e., what aspects of the outcome are determined by the agent.

**Methodology**  
InqAL is built as a multi‑agent extension of **inquisitive neighborhood logic** and is interpreted on **concurrent game structures**. The authors give a precise semantic account via *actual effectivity functions* that map each agent to the sets of outcomes realizable by their possible actions, and they prove a representation theorem showing exactly when a multi‑agent neighborhood frame originates from such a game structure. An axiomatization is provided, and completeness, decidability, and the finite‑model property are established.

**Key findings for agentic AI**  
- InqAL is shown to be **expressively equivalent** (for statements) to the individual‑agent fragment of the socially‑friendly coalition logic, linking it to well‑studied coalition reasoning tools.  
- The logic captures **agentive determination** as modal claims about questions, offering a formal language for specifying and verifying what information an AI agent’s actions will concretely settle.  
- The completeness and decidability results, together with the finite‑model property, make InqAL a tractable foundation for automated reasoning about **multi‑agent decision‑making, coordination, and epistemic effects of actions** in AI systems.


<details>
<summary>Abstract</summary>

We introduce inquisitive action logic, InqAL, a multi-agent modal logic for reasoning about action. While traditional approaches focus on what properties of the outcome an agent can force, InqAL also captures what aspects of the outcome an agent determines through their actions. As we argue, such claims of agentive determination are naturally analyzed as modal claims involving questions.
  Technically, InqAL is a multi-agent extension of inquisitive neighborhood logic based on concurrent game structures. With respect to statements, it is expressively equivalent to the individual-agent fragment of the socially friendly coalition logic recently proposed by Goranko and Enqvist.
  We present an axiomatization of InqAL and prove completeness and decidability via the finite model property. Along the way, we establish a representation theorem for actual effectivity functions, associating to an agent the sets of outcomes corresponding to their possible actions; we give exact conditions under which a multi-agent neighborhood frame arises from a concurrent game structure.

</details>


### 65. An Agentic AI Framework to Accelerate Scientific Discovery in Plant Phenotyping

- **Authors:** Renan Souza, Daniel Rosendo, Kelsey Carter, John Lagergren, Frédéric Suter, Shelaine L. Curd, Gerald A. Tuskan, Rafael Ferreira da Silva, David Weston
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31831v1](http://arxiv.org/abs/2606.31831v1)
- **PDF:** [https://arxiv.org/pdf/2606.31831v1](https://arxiv.org/pdf/2606.31831v1)
- **Categories:** cs.AI


> The paper introduces a secure, federated **agentic AI platform** that lets plant scientists interact with autonomous AI “Co‑Scientist” and “Compute” agents to turn high‑throughput phenotyping data into rapid, iterative scientific insight. Using natural‑language queries, the Co‑Scientist Agent generates structured analysis plans that are executed by a headless Compute Agent on the Frontier exascale system via Vision‑Transformer segmentation and trait extraction, with all communication token‑authenticated and provenance‑tracked across isolated security domains. In benchmark deployments the end‑to‑end workflow, which previously required days‑to‑weeks of manual analysis, is compressed into a seconds‑scale interactive loop, demonstrating that tightly coupled conversational agents can dramatically accelerate discovery pipelines in plant phenotyping and provide a template for reproducible, scalable agentic AI in scientific domains.


<details>
<summary>Abstract</summary>

High-throughput plant phenotyping now generates image derived datasets far faster than scientists can analyze them. At Oak Ridge National Laboratory's Advanced Plant Phenotyping Laboratory (APPL), automated stations image hundreds of plants daily across multiple remote sensing modalities; yet, trait extraction and interpretation remain manual, expert-bound, and strictly post-hoc, making analysis, not acquisition, the binding constraint on discovery. We present an end-to-end agentic AI framework that turns the facility from a data factory into an interactive autonomous, discovery platform, where scientists partner with AI agents to accelerate time to insight. A conversational Co-Scientist Agent translates a scientist's natural-language question into a structured analysis plan, and a headless Compute Agent dispatches Vision Transformer segmentation and trait extraction on the Frontier exascale supercomputer. The two agents run in separate security and resource domains and communicate over a secure, token-authenticated streaming channel, a design that accounts for the federation, data-movement, and provenance realities cloud-native agentic frameworks ignore, ensuring end-to-end provenance is captured for every interaction. The framework turns a days- to weeks-long analysis process into an interactive loop where agents reason over results, recommend next analyses, and respond to follow-up questions in seconds.

</details>


### 66. A Self-Evolving Agentic System for Automated Generation and Execution of Biological Protocols

- **Authors:** Yankai Jiang, Weiting Tang, Haoran Sun, Zhenyu Tang, Yuejie Hou, Yingnan Han, Rubo Wang, Yueyuxiao Yang, Cheng Liang, Lilong Wang, Wenjie Lou, Xiaosong Wang, Lei Bai, Meng Yang
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31763v2](http://arxiv.org/abs/2606.31763v2)
- **PDF:** [https://arxiv.org/pdf/2606.31763v2](https://arxiv.org/pdf/2606.31763v2)
- **Categories:** cs.AI


> The paper introduces **ProtoPilot**, a self‑evolving, multi‑agent framework that transforms textual biological protocols into device‑ready code, continuously refines its SOP library, and closes the loop with wet‑lab feedback. By evaluating ProtoPilot on a benchmark of 294 synthetic‑ and molecular‑biology tasks (including expert rubrics, device‑level validity gates, and real‑world Opentrons runs), the authors show that the system attains a Top‑3 expert‑preference rate of 90.2 % and an overall protocol‑to‑code pass rate of 89.5 % (versus 32.35 % for the OpenTrons‑AI baseline), with wet‑lab experiments confirming correct DNA assemblies. These results demonstrate that a layered, verifiable, multi‑agent architecture can reliably generate and iteratively improve executable biological protocols, advancing autonomous experimentation in agentic AI.


<details>
<summary>Abstract</summary>

Autonomous wet-lab experimentation requires more than plausible protocol text: biological intent, quantitative procedures, device constraints and experimental feedback must remain aligned from protocol and SOP design to code and physical execution. We developed ProtoPilot, a self-evolving multi-agent system, together with an expert-grounded benchmark and evaluation framework for testing this conversion as an experimental automation problem. The framework spans 294 synthetic-biology and molecular-biology tasks derived from 98 gold-standard protocols, wet-lab expert rubrics, device-level validity gates and real experimental tests. ProtoPilot incorporates layer-wise verifiability, multi-agent orchestration and a runtime-updated skill library to generate protocols, expand SOPs, synthesize SDK-compliant code and revise workflows from wet-lab feedback. It achieved a Top@3 expert-preference rate of 90.2%, an overall protocol-to-code gate pass rate of 89.5% and an Opentrons pass rate of 88.24%, compared with 32.35% for OpenTrons-AI. Wet-lab validation produced interpretable readouts, Sanger-confirmed products and feedback-corrected PCA-assembled DNA targets, establishing a verifiable route to autonomous experimentation. Together, these results show that the evaluation framework captures execution-relevant requirements for autonomous wet-lab automation, and that ProtoPilot can meet them by converting protocol and code generation into validated execution and feedback-guided revision.

</details>


### 67. ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping

- **Authors:** Jiacheng Chen, Tao Zhang, Manxi Lin, Dunxian Huang, Teng Shi, Honghao Fu, Mengyan Li, Xinming Zhang, Chenchi Zhang, Xuan Lu, Xiaoxiong Du, Haibin Chen, Shaolin Ye, Hao Chang, Xiaoqi Li, Shuwen Xiao, Yujin Yuan, Jingxuan Feng, Shaopan Xiong, Huimin Yi, Ju Huang, Qiu Shen, Ying Chen, Junjun Zheng, Xiangheng Kong, Yuning Jiang
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31693v1](http://arxiv.org/abs/2606.31693v1)
- **PDF:** [https://arxiv.org/pdf/2606.31693v1](https://arxiv.org/pdf/2606.31693v1)
- **Categories:** cs.IR, cs.AI, cs.CL


> The paper introduces **ShopX**, a foundation model that directly maps natural‑language shopping intents to concrete item‑space actions using **semantic IDs (SIDs)**, thereby eliminating the inefficient hand‑offs between LLM‑based intent parsing and traditional search/recommendation pipelines. ShopX is trained with a specially designed recipe that makes SIDs recoverable and operable by the language model, enabling it to plan and execute multi‑turn fulfillment operations such as SID‑based beam search retrieval, listwise ranking, and product bundling within a unified “model‑native” serving framework. Experiments on anonymized Taobao logs show that this integrated approach outperforms conventional tool‑mediated agents, especially on complex or ambiguous requests, demonstrating tighter intent‑to‑item translation for agentic shopping applications.


<details>
<summary>Abstract</summary>

The wave of AI-native applications is moving shopping beyond page- and feed-based browsing toward intent-driven experiences orchestrated by LLM agents. A common design wraps an LLM around existing search and recommendation pipelines, forcing complex intents through low-bandwidth retrieval or ranking interfaces and leaving a gap between language understanding and item-space fulfillment. Generative recommendation gives LLMs a direct item-space interface through semantic IDs (SIDs), but existing models mainly generate candidates for retrieval rather than translate flexible intents into item-space outcomes. We propose ShopX to address this bottleneck by unifying intent understanding, execution planning, and flexible SID-native item-space operations into a single foundation model. We deploy ShopX in agentic shopping workflows through a model-native item-fulfillment framework with a serving harness that defines a model-facing action protocol and exposes support surfaces for context access, catalog grounding, and state management. Within this framework, ShopX plans and composes SID-based item-space operations such as SID beam-search retrieval, listwise ranking, or product bundling. This model-centric design reduces lossy hand-offs between agent orchestration and item-space execution. To build ShopX, we design semantically recoverable, LLM-operable SIDs and a training recipe that equips a general LLM for flexible multi-turn item-space fulfillment while retaining the knowledge and instruction-following abilities needed by a shopping agent. We evaluate the ShopX framework against tool-mediated agentic systems on single- and multi-turn fulfillment tasks derived from anonymized Taobao production logs, showing that model-native fulfillment improves overall framework behavior, especially on complex or ambiguous requests.

</details>


### 68. ForecastAgentSearch: Towards a Multi-Expert Agent Search System for Geopolitical Event Forecasting

- **Authors:** Miaomiao Cai, He Chang, Yunshan Ma, See-kiong Ng
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31665v1](http://arxiv.org/abs/2606.31665v1)
- **PDF:** [https://arxiv.org/pdf/2606.31665v1](https://arxiv.org/pdf/2606.31665v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Geopolitical event forecasting is a challenging task, as it requires understanding complex regional contexts, dynamic event signals, and uncertain future outcomes. Recent advances in large language model agents provide new opportunities for building forecasting systems that can reason with diverse sources and expert perspectives. In this paper, we present \textit{ForecastAgentSearch}, a preliminary framework that formulates geopolitical event forecasting as a multi-expert agent search problem. Given a forecasting query, the system first analyzes the task context, then searches and ranks relevant expert agents based on their regional knowledge, domain expertise, reliability, and complementarity. The selected agents provide specialized analyses, which are further coordinated to generate a final forecast with explanations and uncertainty awareness. We discuss the key design challenges of agent profiling, expert retrieval, ranking, and multi-agent coordination, and outline possible evaluation protocols for future development. This work aims to provide an initial step toward searchable and reliable agent-based forecasting systems.

</details>


### 69. Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents

- **Authors:** Utsav Garg, Sungjin Hong, Jason Jung, Justin Lee, Shaan Desai, Joon Hee Kim, Anirudh Shrinivason, Edmond Wen, Susie Park
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31648v1](http://arxiv.org/abs/2606.31648v1)
- **PDF:** [https://arxiv.org/pdf/2606.31648v1](https://arxiv.org/pdf/2606.31648v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution**  
The paper introduces **LuckyStar 111B**, a 111‑billion‑parameter multilingual hybrid‑reasoning model that adapts Cohere’s post‑trained Command A into a Korean‑English enterprise agent capable of tool use (function calling, NL‑to‑SQL, math) while meeting strict memory and single‑GPU serving limits.

**Methodology**  
LuckyStar is obtained by fine‑tuning the existing Command A model rather than re‑pretraining, using a *preamble‑conditioning* trick to toggle between terse, non‑reasoning outputs and extended, tool‑oriented reasoning. The authors evaluate four scaling strategies for efficient adaptation: (1) multilingual supervised fine‑tuning, (2) reinforcement learning with verifiable multi‑step tool‑use rewards, (3) language‑consistency rewards that enforce Korean‑language fidelity in user‑facing replies, and (4) 4‑bit quantization for GPU‑friendly inference.

**Key findings**  
Across benchmarks, LuckyStar 111B shows significant gains in mathematical reasoning, reliable function‑calling, and natural‑language‑to‑SQL generation while preserving high‑quality Korean and English instruction following. The study also provides a practical recipe and failure‑mode analysis for turning post‑trained multilingual models into memory‑constrained, verifiable, tool‑using agents—demonstrating that large‑scale multilingual agents can be efficiently adapted without full pretraining.


<details>
<summary>Abstract</summary>

We present LuckyStar 111B, a 111B-parameter hybrid reasoning model developed through a collaboration between Cohere and LG CNS for Korean-English enterprise agents under practical memory and serving constraints. The model trains from Cohere's fully post-trained Command A model rather than a new pretraining run, and uses preamble conditioning to switch between concise non-reasoning behavior and longer tool-oriented reasoning. We study four choices for scaling tool-using agents efficiently: multilingual supervised fine-tuning, reinforcement learning with verifiable rewards for multi-step tool-use tasks, language-consistency rewards for Korean user-facing responses, and 4-bit quantization for single-GPU serving. The adapted model improves mathematical reasoning, function calling, and agentic natural-language-to-SQL (NL2SQL) performance while preserving general Korean and English instruction-following quality. These results provide a practical recipe and failure-mode analysis for adapting post-trained multilingual models to verifiable agentic workflows under memory-constrained deployment.

</details>


### 70. A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems

- **Authors:** Seyed Bagher Hashemi Natanzi, Bo Tang
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31639v1](http://arxiv.org/abs/2606.31639v1)
- **PDF:** [https://arxiv.org/pdf/2606.31639v1](https://arxiv.org/pdf/2606.31639v1)
- **Categories:** cs.CR, cs.AI, cs.GT, cs.LO


> **Main contribution:** The paper presents a comprehensive, lifecycle‑oriented taxonomy of security weaknesses in large‑language‑model (LLM) systems, extending threat modeling beyond the model weights to the whole application stack—including data pipelines, retrieval/memory, prompting, tool‑calling agents, and deployment/maintenance.

**Methodology:** The authors map existing attacks and defenses onto eight sequential stages (data collection → post‑training alignment → packaging → retrieval/memory → prompting/inference → tool/agent execution → deployment/maintenance), evaluate attacker capabilities and impacted security goals (confidentiality, integrity, availability, safety, privacy, fairness, accountability, agency‑control), and analyze why point solutions often fail to compose across trust boundaries.

**Key findings for agentic AI:** Vulnerabilities are amplified when LLMs act as autonomous agents that invoke tools, manipulate files, or access private data; delegated authority creates new attack surfaces (e.g., prompt injection, tool‑call hijacking, memory poisoning). The survey highlights the need for compositional security mechanisms—such as provenance‑aware retrieval, tool‑call containment, and long‑ horizon agent evaluation—and outlines open research problems focused on secure, incident‑responsive deployment of agentic LLMs.


<details>
<summary>Abstract</summary>

Large language models are no longer only text generators. They are increasingly embedded in retrieval pipelines, enterprise assistants, coding environments, robotic systems, security-operation workflows, and autonomous agents that can read private data, call tools, write files, execute code, and act across organizational boundaries. This shift changes the security problem: risks do not arise from the model weights alone, but from the full lifecycle and application stack through which data, prompts, model outputs, tools, memories, and user authority interact. This paper systematizes the literature on vulnerabilities in large language model systems through a lifecycle and application-stack lens. We organize attacks across eight stages: data collection, pretraining, post-training alignment, model packaging and supply chain, retrieval and memory, prompting and inference, tool/agent execution, and deployment/maintenance. For each stage, we analyze attacker capabilities, affected security objectives, representative attacks, practical risks, evaluation practices, and defenses. We further map LLM-specific vulnerabilities to confidentiality, integrity, availability, safety, privacy, fairness, accountability, and agency-control objectives. Unlike taxonomies that list isolated attack names, the proposed systematization emphasizes where trust boundaries fail, how untrusted data becomes executable instruction, how delegated authority amplifies model errors, and why point defenses rarely compose. We close with a research agenda for secure LLM systems, including compositional security, provenance-aware retrieval, tool-call containment, long-horizon agent evaluation, privacy-preserving adaptation, realistic red teaming, and deployment-grade incident response.

</details>


### 71. A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents

- **Authors:** Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31635v1](http://arxiv.org/abs/2606.31635v1)
- **PDF:** [https://arxiv.org/pdf/2606.31635v1](https://arxiv.org/pdf/2606.31635v1)
- **Categories:** eess.SY, cs.AI, cs.MA


> The paper introduces a framework that treats a large‑language‑model (LLM) as a constrained supervisory planner for autonomous, fault‑tolerant control in process plants. By grounding the LLM in plant‑specific documentation (P&IDs, procedures, alarms) and coupling every LLM‑generated recovery action with an external validator (symbolic checks or fast simulators) before execution, the system can propose and safely enact operator‑level recovery moves for faults that lie outside traditional rule‑based controllers. Experiments on two open‑source Python testbeds (a modular mixing module and a continuous stirred‑tank reactor) show that the LLM can reliably generate viable recovery strategies when paired with appropriate validation schemes, highlighting design trade‑offs in pattern selection, validation methodology, latency, and safety integration that are critical for deploying agentic AI in industrial control.


<details>
<summary>Abstract</summary>

Fault recovery in process plants still relies heavily on plant operators, especially when faults fall outside predefined supervisory logic. Operators interpret alarms, procedures, P\&IDs, interlocks, and process trends, then decide how to move the plant to a safe operating mode without triggering a shutdown. This paper examines how Large Language Model (LLM) agents can support such recovery decisions. The proposed framework treats the LLM as a constrained supervisory planner. It uses plant-specific knowledge to propose recovery actions, and every proposal is checked by an external validator (symbolic or simulation-based) before actuation. The paper develops three design dimensions for applying the framework: the recovery patterns for which LLM agents are useful, the validation strategies that separate admissible from inadmissible proposals, and the deployment constraints imposed by latency, knowledge engineering, safety integration, and model lifecycle management. To make the framework directly usable, two openly available executable Python environments are provided. Both re-implement established case studies, a modular mixing module and a continuous stirred-tank reactor, extended with configurable faults and defined interfaces for custom recovery and validation methods.

</details>


### 72. A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks

- **Authors:** Jinliang Xu, Liping Ma
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31584v1](http://arxiv.org/abs/2606.31584v1)
- **PDF:** [https://arxiv.org/pdf/2606.31584v1](https://arxiv.org/pdf/2606.31584v1)
- **Categories:** cs.NE, cs.MA


> The paper provides a rigorous, budget‑controlled empirical benchmark of the Metabolic Multi‑Agent Optimizer (MMAO) across both continuous (CEC2017) and discrete (TSPLIB, OR‑Library knapsack) problems. By measuring communal budget usage, success rates, role evolution, and population turnover under a strict protocol, the authors show that MMAO consistently outperforms strong baselines (light‑weight PSO, ES, and iterated‑greedy 2‑opt) and that its ablations remain close to the full system, confirming that its closed‑loop, endogenous resource‑allocation mechanism is effective across domains. The study validates MMAO as a cross‑domain, adaptive agentic framework, while highlighting the need for deeper mechanistic isolation and competition‑grade comparisons in future work.


<details>
<summary>Abstract</summary>

This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronger reproducible baselines including PSO-lite, ES-lite, and an iterated-greedy 2-opt route baseline. We further add trajectory-level diagnostics for communal budget, success rate, role evolution, and population turnover, plus an auxiliary OR-Library multiple-knapsack slice to extend the discrete evidence beyond routing. Under this protocol, MMAO clearly outperforms the external baseline set on the continuous side and on the TSPLIB side, while the ablation variants remain much closer to the full method than the external baselines are. We therefore position MMAO as a benchmark-backed cross-domain adaptive framework whose most clearly validated value is endogenous resource redistribution under evidence pressure, while also noting that the strongest remaining gap is not basic workability but sharper mechanism isolation and broader competition-grade comparison.

</details>


### 73. Holonic Active Distillation for Scalable Multi-Agent Learning in Multi-Sensor Systems

- **Authors:** Dani Manjah, Tim Bary, Benoît Macq, Stéphane Galland
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31578v1](http://arxiv.org/abs/2606.31578v1)
- **PDF:** [https://arxiv.org/pdf/2606.31578v1](https://arxiv.org/pdf/2606.31578v1)
- **Categories:** cs.MA


> **Summary**  
The paper introduces a **Holonic Active Distillation (HAD)** framework for scalable multi‑agent learning in heterogeneous, dynamically changing sensor networks. By embedding **Clustered Stream‑Based Active Distillation (CSBAD)** within a holonic multi‑agent system, each “student” agent continuously streams local sensor data, requests pseudo‑labels from shared “teacher” models, and self‑organizes into clusters of similar sensors, thereby achieving localized specialization while preserving a globally consistent representation. Experiments demonstrate that this holonic architecture substantially improves adaptability to sensor join/leave events and reduces model drift compared to monolithic or flat decentralized baselines, though incremental updates and long‑term drift remain challenges for future work.


<details>
<summary>Abstract</summary>

The rapid expansion of sensor-based networks introduces major challenges in scalability, adaptability, and knowledge transfer, especially in open environments where new subsystems can dynamically join or leave. In this work, we propose a Holonic Active Distillation architecture within a Holonic Multi-Agent System (HMAS) to address these issues. Our approach integrates Clustered Stream-Based Active Distillation (CSBAD), a framework in which specialized student models collect local data, query pseudo-labels from teacher models, and cluster into groups of similar sensors.
  Results show that the holonic organization balances local specialization with global generalization, while efficiently adapting to sensor departures and re-integrations. We also analyzed trade-offs among incremental model updates, system reorganization, and scalability limits.
  Our findings highlight the advantages of holonic learning for multi-sensor systems while identifying key challenges related to model drift and long-term adaptation.

</details>


### 74. ACE: Pluggable Adaptive Context Elasticizer across Agents

- **Authors:** Ning Liao, Zihao Long, Xiaoxing Wang, Xue Yang, Yaoming Wang, Ziyuan Zhuang, Xunliang Cai, Rongxiang Weng, Junchi Yan
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31564v1](http://arxiv.org/abs/2606.31564v1)
- **PDF:** [https://arxiv.org/pdf/2606.31564v1](https://arxiv.org/pdf/2606.31564v1)
- **Categories:** cs.AI


> The paper introduces **ACE (Adaptive Context Elasticizer)**, a plug‑and‑play module that lets LLM‑based agents keep a **lossless repository of all past messages** while dynamically deciding, at each decision step, which steps to feed to the model as raw text, as compact abstractions, or to drop altogether. ACE works by coupling a **message‑maintenance layer** (storing raw and summarized versions of every step) with a **context‑orchestration layer** that selects the optimal “elastic type” based on the current task state, making the context management reversible and adaptive without retraining the underlying agent. Integrated into four disparate agent frameworks (ReAct, DeepAgent, WebThinker, MiroFlow), ACE consistently outperforms naïve truncation and static summarization baselines, yielding measurable performance improvements across all tested agents.


<details>
<summary>Abstract</summary>

The increasing complexity of agentic tasks has led to rapidly growing trajectory lengths, which poses significant challenges for large language model (LLM) based agents with fixed context windows. Existing context management techniques, such as truncation and summarization, suffer from inherent inflexibility and irreversibility: once information is discarded or compressed, it cannot be recovered even when it becomes critically relevant in later decision steps. To address these limitations, we propose the Adaptive Context Elasticizer (ACE), a plug-and-play module that elastically orchestrates historical step information into the agent's context at each decision step. ACE maintains a lossless message maintenance layer that stores both raw messages and compressed abstractions for each historical step, while a context orchestration layer adaptively assigns each step an elastic type as raw, abstract, or drop, at every decision step based on the current task state. This reversible design ensures that the main LLM always receives a compact yet information-rich context. We adapt ACE to four diverse agent frameworks, including ReAct, DeepAgent, WebThinker, and MiroFlow, without training or architectural modifications. Experiments show that ACE consistently outperforms truncation and summarization baselines, and brings consistent performance gains across all four agent frameworks.

</details>


### 75. DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation

- **Authors:** Siyu Yan, Yizhen Gao, Yilin Wang, Dongxing Mao, Alex Jinpeng Wang
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31537v1](http://arxiv.org/abs/2606.31537v1)
- **PDF:** [https://arxiv.org/pdf/2606.31537v1](https://arxiv.org/pdf/2606.31537v1)
- **Categories:** cs.CV, cs.MA


> DataEvolver introduces a self‑evolving multi‑agent pipeline that continuously refines text‑rich image training data by re‑using rejected samples as feedback signals. The system cycles a Retriever, Verifier, Critic, and Generator: the Verifier scores and annotates failures, the Critic turns these into semantic feedback, and the Generator synthesizes missing or problematic text‑image pairs for the next round, updating a shared feedback memory. Across two text‑rich image benchmarks, this adaptive construction yields substantially higher OCR‑F1 scores (up to +85 % on TextScenesHQ) than static, crawl‑filter‑freeze baselines, demonstrating that leveraging failure cases can markedly improve data quality for agentic text‑image generation models.


<details>
<summary>Abstract</summary>

Text-rich image generation is one of the most challenging settings in image generation, since models must simultaneously produce visually realistic images and render legible, semantically aligned, and layout-consistent text. Existing data pipelines usually follow a static crawl-filter-freeze paradigm. They collect candidate samples, filter them once, and freeze the accepted data for training. However, rejected samples are usually discarded, although they often contain useful failure signals such as OCR errors and semantic mismatches. As a result, later construction rounds may repeat the same failure modes. To address these limitations, we propose DataEvolver, a self-evolving multi-agent framework for text-rich image data construction. DataEvolver treats data construction as feedback-driven construction policy evolution. A Retriever collects candidate samples, a Verifier assigns quality scores and rejection causes, a Critic summarizes round-level feedback into semantic feedback, and a Generator completes under-covered regions through targeted synthesis. The updated feedback memory then guides the next construction round. Experiments on text-rich image generation benchmarks show that DataEvolver produces more useful training data than fixed-dataset baselines under matched data budgets. At the 0.75M scale on PixArt-alpha, DataEvolver improves OCR-F1 over the strongest baseline by 85.3 percent on TextScenesHQ and 35.3 percent on LongTextBench. The improvements are consistent across both evaluated benchmarks and also transfer to Show-o2, indicating that the benefit of DataEvolver is not tied to a single downstream generator. These results suggest that rejected samples can provide actionable feedback for improving text-rich image data construction.

</details>


### 76. Design and Implementation of Agentic Orchestrations and Orchestration of Agents

- **Authors:** Stefanie Rinderle-Ma, Juergen Mangler, Johannes Loebbecke, Dominik Voigt, Nataliia Klievtsova, Matthias Ehrendorfer
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31518v1](http://arxiv.org/abs/2606.31518v1)
- **PDF:** [https://arxiv.org/pdf/2606.31518v1](https://arxiv.org/pdf/2606.31518v1)
- **Categories:** cs.AI


> The paper introduces a comprehensive framework for designing and evaluating **agentic orchestrations**—systems that combine autonomous LLM‑based agents with classical process‑oriented control to obtain both flexibility and operational guarantees. It classifies orchestration approaches along dimensions such as task specificity, traceability, autonomy/reactivity, and correctness assurance, provides qualitative decision rules for selecting an approach in a given scenario, and defines quantitative metrics (e.g., latency, error propagation, trace depth) to measure those properties. Using a predictive light‑sensing use case, the authors instantiate several orchestration variants, demonstrate how the metrics differentiate them, and show that appropriate orchestration can retain the agents’ autonomy while delivering predictable, traceable, and correct behavior—offering practical guidance for building robust, accountable agentic AI systems.


<details>
<summary>Abstract</summary>

Agentic Business Process Management has gained momentum recently. The prospect is that the autonomy of AI agents, i.e., predominantly LLM-based agents, can be balanced with a certain level of robustness, tractability, and traceability through a combination with process technology. In this paper, we provide a classification framework for agentic orchestration options along properties such as task specificity, traceability and tractability, autonomy and reactivity, and correctness assurance and present qualitative decision criteria for realizations of different scenarios. We also provide metrics for the quantitative assessment of realization properties and show them through different agentic implementations of a predictive light sensing scenario. Altogether, this work aims at providing properties, criteria, and metrics for the design and implementation of agentic orchestrations and orchestration of agents.

</details>


### 77. Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express

- **Authors:** Richard Kang, Yudho Diponegoro
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31498v1](http://arxiv.org/abs/2606.31498v1)
- **PDF:** [https://arxiv.org/pdf/2606.31498v1](https://arxiv.org/pdf/2606.31498v1)
- **Categories:** cs.MA, cs.SE


> **Main contribution:** The paper shows that existing agent‑interoperability standards (MCP, A2A, ACP, ANP, ERC‑8004) lack the primitives needed to govern heterogeneous agent communities, exposing a missing architectural layer for collective decision‑making.  

**Methodology:** The authors construct a six‑dimension governance taxonomy (membership, deliberation, voting, dissent preservation, human escalation, audit/replay) from organizational theory and MAS literature, then systematically evaluate each protocol against this taxonomy, labeling support as “Supported,” “Partial,” or “Absent” and distinguishing extensible versus structural gaps.  

**Key findings:** Across all five protocols, voting and dissent preservation are universally absent, deliberation is at best partial, and no protocol provides the full set of governance primitives. The gaps are largely structural, indicating that a new governance layer—rather than incremental extensions to current standards—is required for governed agent communities.


<details>
<summary>Abstract</summary>

Agent interoperability protocols (MCP, A2A, ACP, ANP, and ERC-8004) have rapidly matured to enable identity, capability discovery, tool access, and message exchange between autonomous agents. However, as enterprises deploy heterogeneous agent fleets that must make collective decisions under governance constraints, a question arises: can these protocols support governed agent communities, or only task-oriented coordination? We present a systematic gap analysis applying a six-dimension governance requirements taxonomy (membership, deliberation, voting, dissent preservation, human escalation, and audit/replay) derived from organizational theory, multi-agent systems literature, and enterprise governance standards. We analyze each protocol's specification against this taxonomy, classifying capabilities as Supported, Partial, or Absent. The resulting gap matrix reveals that voting and dissent preservation are universally absent across all five protocols, deliberation is absent or at most partial, and no protocol encodes the full set of primitives required for governed agent communities. We distinguish extensible gaps (addressable through protocol extension mechanisms) from structural gaps (requiring a new architectural layer) and assess time-sensitivity based on observed protocol evolution velocity. The analysis establishes that agent community governance constitutes a missing architectural layer above current interoperability standards, not a missing feature within them.

</details>


### 78. CSTrader: A Testbed for Language-Grounded Trading in a Community-Driven Virtual Asset Market

- **Authors:** Yao Shi, Kingfung Luo, Nan Tang, Yuyu Luo
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31461v1](http://arxiv.org/abs/2606.31461v1)
- **PDF:** [https://arxiv.org/pdf/2606.31461v1](https://arxiv.org/pdf/2606.31461v1)
- **Categories:** cs.AI, cs.CE


> The paper introduces **CSTrader**, a multi‑agent testbed that maps unstructured community discourse about Counter‑Strike 2 weapon skins into concrete trading actions, thereby providing a realistic benchmark for language‑grounded decision‑making in niche, highly volatile asset markets. The framework first aggregates heterogeneous textual and market signals, then passes them through specialized LLM‑driven agents for technical analysis, liquidity assessment, event detection, and “reversed” sentiment, before a suite of risk‑control, transaction‑friction, and portfolio‑management agents generate buy/sell/hold orders under realistic market constraints. Empirical results on a live‑like CS2 dataset show that CSTrader’s modular LLM pipeline consistently outperforms a falling‑market baseline (‑15.62 % loss) and single‑prompt LLM baselines, achieving up to **7.58 % cumulative return** while maintaining controlled risk; ablations reveal that liquidity, reversed‑sentiment, and friction agents are essential for converting noisy language cues into stable profits, underscoring the utility of community‑driven markets as a benchmark for future agentic AI research.


<details>
<summary>Abstract</summary>

Niche asset markets, such as Counter-Strike 2 (CS2) weapon skins, are small, volatile, and heavily driven by community discussions and platform rules. These properties make them hard for traditional quantitative models, but provide an ideal testbed for studying how large language models (LLMs) turn unstructured text into trading actions. We present CSTrader, a multi-agent framework for language-grounded trading in the CS2 skin market. The system first integrates heterogeneous signals from various sources, then uses specialized agents for technical analysis, liquidity, events, and (reversed) sentiment, and finally applies risk control, transaction friction, and portfolio management agents to produce buy, sell, or hold decisions under realistic trading frictions. We build a live-like evaluation environment with real CS2 data from a highly volatile period and evaluate several recent LLM backbones. Across models, CSTrader consistently outperforms both a falling market index (-15.62%) and simple single-prompt LLM baselines, achieving up to a 7.58% cumulative return with controlled risk. Ablation studies show that liquidity, reversed sentiment, and transaction friction agents are crucial for turning noisy language signals into stable profits, suggesting that niche, language-driven markets are a useful benchmark for future language-to-action research. Code is available at: https://github.com/IatomicreactorI/CSGOTrading?tab=readme-ov-file#quick-start

</details>


### 79. Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?

- **Authors:** Zewen Liu
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31371v1](http://arxiv.org/abs/2606.31371v1)
- **PDF:** [https://arxiv.org/pdf/2606.31371v1](https://arxiv.org/pdf/2606.31371v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> The paper introduces probability‑calibrated evaluator feedback as a lightweight mitigation for **evaluator preference coupling (EPC)**—the systematic bias that propagates from an LLM judge into an LLM agent’s policy when the agent updates its behavior via binary win/loss Reinforcement Learning (TTRL). In a within‑subjects experiment (N=5) the authors replace the standard binary TTRL update with a confidence‑weighted (probability‑calibrated) update while keeping DeepSeek‑V4‑Pro as the executor and GLM‑5.2 as the judge; they show that this calibration cuts the EPC coupling coefficient γ by 20–49 % and reduces the Jensen‑Shannon divergence between the agent’s learned strategy distribution and the unbiased baseline by 45–67 %, with a symmetric‑logistic‑regression control ruling out simple asymmetry effects. The calibrated TTRL protocol is released as a practical tool for improving the reliability of LLM‑as‑judge pipelines in agentic AI systems.


<details>
<summary>Abstract</summary>

When large language model (LLM) agents adapt their behavior through evaluator feedback, systematic evaluator biases propagate into the agent's learned strategy distribution - a phenomenon termed evaluator preference coupling. Prior work has documented this coupling and established a diagnostic framework (EPC) to measure it, but has not investigated whether calibration techniques can mitigate the effect. We present the first study of evaluator calibration as mitigation: applying probability calibration to the evaluator's pairwise judgments to reduce spurious preference propagation. In a controlled within-subjects experiment (N=5) comparing standard binary TTRL (win/loss) with confidence-calibrated TTRL (probability-weighted updates) using DeepSeek-V4-Pro as executor and GLM5.2 as evaluator, we find that calibration reduces the coupling coefficient gamma by 20-49% and Jensen-Shannon divergence by 45-67%. A symmetric-LR control confirms the effect is not due to reduced update asymmetry. We release the calibrated TTRL protocol and recommend it as a lightweight mitigation for LLM-as-judge deployment pipelines.

</details>


### 80. Smart charging of large fleets of Electric Vehicles: Independent Multi-Agent Reinforcement Learning approaches

- **Authors:** Xavier Rate, Eloann Le Guern, Raphaël Féraud, Fatma Salem, Melissa Chiknoun, Eymeric Giabicani, Mehdi Feki, Patrick Maillé, Guy Camilleri, Anne Blavette, Hamid Benhamed
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31347v1](http://arxiv.org/abs/2606.31347v1)
- **PDF:** [https://arxiv.org/pdf/2606.31347v1](https://arxiv.org/pdf/2606.31347v1)
- **Categories:** cs.AI


> **Paper Summary**  

The authors compare two *independent* multi‑agent reinforcement‑learning (MARL) methods—contextual combinatorial bandits and policy‑gradient policies—for decentralized smart‑charging of large electric‑vehicle (EV) fleets. They train each EV agent on locally observed signals (electricity price, state‑of‑charge, time windows) in a high‑fidelity grid simulator that incorporates real PV generation and dynamic pricing, then test the agents under different congestion levels and heterogeneous mixed‑strategy populations. Results show that both approaches can reduce peak demand and charging costs, but the contextual bandit method converges faster and is more robust to agent heterogeneity, while the policy‑gradient agents achieve slightly higher cost savings in low‑congestion regimes; overall the work demonstrates that fully independent MARL can provide effective implicit coordination for large‑scale EV charging without centralized control.


<details>
<summary>Abstract</summary>

The electrification of transportation through electric vehicles introduces new challenges for power grid management, such as increased peak demand, voltage fluctuations, line overloads, and the integration of variable renewable energy sources. To enable efficient integration of EVs while minimizing costs for users and avoiding network overloads, implicit coordination between EVs is required. This work compares two independent multi-agent reinforcement learning approaches for optimizing such decentralized EV charging: contextual combinatorial bandits and policy gradient algorithms. Using a realistic simulation environment with autonomous agents making decisions based on local environmental information (including price signals, state-of-charge, and temporal constraints), we evaluate their performance across varying congestion levels, and mixed-strategy configurations with heterogeneous agent groups under dynamic electricity pricing derived from real photovoltaic production data.

</details>


### 81. The Calibration Turn in AI-Assisted Research: A Conceptual and Methodological Framework for Evidence-Licensed Claims

- **Authors:** Hongmin Li
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31273v1](http://arxiv.org/abs/2606.31273v1)
- **PDF:** [https://arxiv.org/pdf/2606.31273v1](https://arxiv.org/pdf/2606.31273v1)
- **Categories:** cs.LG


> The paper proposes that the pivotal challenge for AI‑assisted science is not simply generating hypotheses or papers, but ensuring that every claim the system outputs is **calibrated to the evidence that actually licenses it**. To formalize this, the authors model AI‑driven research as a five‑step loop—hypothesis generation, model‑mediated consequence derivation, external validation, belief update, and claim calibration—and introduce a vocabulary (evidence‑licensed semantics, claim‑evidence gap, epistemic debt) that treats calibration as a rights‑management mechanism rather than a stylistic precaution. Using a synthetic example (AISim‑Cal), they demonstrate that reliable AI scientists must enforce the principle “no claim without license,” showing that validation alone does not set claim strength and that automation dramatically heightens the need for rigorous evidence‑based claim issuance.


<details>
<summary>Abstract</summary>

AI-assisted research has entered a stage in which the central question is not only whether systems can generate hypotheses, run experiments, or produce manuscripts, but whether their scientific claims are calibrated to the evidence that supports them. This Perspective-style paper develops a conceptual and methodological framework for evidence-licensed claims in AI-assisted research. Motivated by representative routes including specialized scientific foundation models, LLM research assistants, multi-agent co-scientists, AI Scientist pipelines, mathematical discovery agents, and self-driving laboratories, it represents AI-assisted research as five operators: hypothesis generation, model-mediated consequence derivation, external validation, belief update, and claim calibration. The central claim is that calibration is not merely cautious wording but a mechanism for managing scientific assertion rights: evidence licenses some forms of speech and withholds others. The paper distinguishes linguistic, consequence-based, interventional, and evidence-licensed semantics; defines the claim-evidence gap and epistemic debt; and treats minimal structural reconstruction across heterogeneous outputs as an upward form of claim calibration. AISim-Cal is included as an illustrative synthetic dynamics exercise, not as an empirical forecast or benchmark. The resulting principles are: no claim without license, validation does not determine claim level, and automation amplifies the need for calibration. Reliable AI-assisted research is therefore evaluated as a loop that generates hypotheses, derives testable consequences, accepts independent adjudication, updates beliefs, and outputs only evidence-licensed claims.

</details>


### 82. The Decomposition Is the Fingerprint: Per-Component Identity for Agent Skills

- **Authors:** Hongliang Liu, Yuhao Wu, Tung-Ling Li
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31272v1](http://arxiv.org/abs/2606.31272v1)
- **PDF:** [https://arxiv.org/pdf/2606.31272v1](https://arxiv.org/pdf/2606.31272v1)
- **Categories:** cs.CR, cs.CL, cs.LG


> The paper introduces **SkillFingerprints**, a compact locality‑sensitive identifier that represents each skill as a triple of per‑component SimHash signatures (prompt, code, and tool declarations). By hashing each component separately and concatenating the three 40‑byte hashes into a fixed 120‑byte fingerprint, the method can detect paraphrasing, renaming, or refactoring of a skill while still distinguishing independently re‑implemented versions, and it does so with constant‑time Hamming‑distance comparison. Experiments on ~5 k skill pairings show an AUC of 0.974 with ≈77× fewer bits than the original embeddings, and the fingerprint successfully flags and localizes injected tampered copies in a 906‑skill benchmark, providing a structural “lineage” signal that complements, but does not replace, behavioral safety verification.


<details>
<summary>Abstract</summary>

AI agents increasingly acquire and execute skills at runtime: bundles of prompt instructions, executable code, and tool declarations fetched from marketplaces and other agents. Governing them needs a stable notion of skill identity, yet cryptographic hashing is engineered to destroy the very similarity we need, as a one-character edit scrambles the digest. We present a compact, locality-sensitive fingerprint that embeds each component of a skill and projects it to bits with a multi-bank SimHash, giving a fixed 120-byte signature compared in constant time by Hamming distance. Our central claim is that keeping the fingerprint as a per-component triple (prompt, code, tools), rather than a single score, is what makes it useful: the triple recovers skill-family identity through paraphrase, renaming, refactoring, and controlled code translation when another component remains shared, while independent multilingual reimplementation is not recovered; it also localizes which component carries the reuse. We claim lineage, not behavioral equivalence: identity supplies the structural axis of a registry and leaves safety to behavioral verification. The fingerprint reaches an area under the ROC curve (AUC) of 0.974 (95% CI [0.956, 0.994]) over 4,950 pairwise comparisons while using 77x fewer bits than the embedding it approximates, with ranking preserved in expectation and finite-bit concentration; the per-component split turns one number into relationship classification, families, novelty, and a portable "SkillBOM" for a skill registry. On a 906-skill injection benchmark the fingerprint recognizes injected skills as tampered copies of a known base and localizes the change, but recognition is not trust: it remains, by design, an identity signal complementary to behavioral verification rather than a safety verdict.

</details>


### 83. Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling

- **Authors:** Fumin Liu, Haoyu Zhou, Fei Hao, Lin Yang
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31252v1](http://arxiv.org/abs/2606.31252v1)
- **PDF:** [https://arxiv.org/pdf/2606.31252v1](https://arxiv.org/pdf/2606.31252v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models can write plausible CAD scripts, but reliable industrial CAD modeling requires more than syntactically valid code: every feature, placement, and assembly relation must be accepted by an exact geometric kernel while remaining editable as parametric boundary representation geometry. We present Embodied CAD, solver-grounded LLM agents for parametric B-Rep assembly modeling. Instead of generating a complete script in one pass, the agent iteratively selects actions from a stratified L0-L4 CAD skill library, resolves them into typed geometric operations, executes them in a CAD backend, and uses solver feedback to plan, repair, and learn. The framework combines action grammar constraints, deterministic parameter resolution, and solver-derived rewards for supervised warm-up and GRPO-style refinement. We evaluate Embodied CAD on multi-step mechanical, industrial equipment, and mold-oriented assembly tasks using solver-aligned metrics: executable rate, skill accuracy, operation-family accuracy, exact policy accuracy, and task completion success. The results show that solver-grounded planning executes all strong-planner workflows in the current benchmark, while learned controllers reach high executable rates and expose the remaining gap between valid tool calls and exact long-horizon policy prediction.

</details>


### 84. Agentic-Ideation: Sample Efficient Agentic Trajectories Synthesis for Scientific Ideation Agents

- **Authors:** Keyu Zhao, Lingyan Kong, Fengli Xu, Yong Li
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31229v1](http://arxiv.org/abs/2606.31229v1)
- **PDF:** [https://arxiv.org/pdf/2606.31229v1](https://arxiv.org/pdf/2606.31229v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Ideation plays a pivotal role in scientific discovery. Recent LLM, especially AI Scientist systems, show promising potential for automated ideation. However, existing approaches predominantly rely on pre-defined agentic workflows. This constraint severely limits the flexibility required to navigate the vast search space of scientific literature and the complex action space of research reasoning. Recently, training Agentic LLMs has emerged as a promising direction, offering flexible reasoning frameworks and the capability for autonomous tool utilization. However, there remains a non-trivial challenge: applying previous agentic data synthesis methods to scientific ideation suffers from prohibitively high data synthesis cost. To bridge this gap, we propose Agentic-Ideation, a novel framework comprising an automated trajectory synthesis pipeline and a specialized agentic LLM trained for scientific ideation. Specifically, we first define a comprehensive tool space incorporating three external tools and three cognitive tools. Then we introduce an Oracle-Guided Data Synthesis strategy. By leveraging a reference idea as oracle guidance, this approach steers the multi-agent system to efficiently reconstruct the logical reasoning and tool invocation paths, transforming aimless trial-and-error into directed trajectory generation. Finally, we train the agent on these synthesized trajectories, employing a masking strategy on tool execution results. This ensures the model focuses on decision-making logic without interference from external feedback. Experimental results demonstrate that our method outperforms the SOTA workflow-based baseline by \textbf{11.91\%} in overall quality. Furthermore, our approach improves the sample efficiency of high-quality data synthesis by \textbf{over 10$\times$}.

</details>


### 85. Long-term Traffic Simulation via Structured Autoregressive Modeling

- **Authors:** Lingyu Xiao, Zexin Feng, Xintao Yan
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31209v1](http://arxiv.org/abs/2606.31209v1)
- **PDF:** [https://arxiv.org/pdf/2606.31209v1](https://arxiv.org/pdf/2606.31209v1)
- **Categories:** cs.AI, cs.RO


> The paper introduces **RosettaSim**, a traffic‑simulation framework that casts the evolving road scene (topology, vehicle states and spawning intents) into a single structured autoregressive token stream and leverages heavily‑frozen small‑scale LLMs as the backbone sequence model. By exploiting the transferability of attention and the statistical similarity between motion tokens and natural‑language tokens, RosettaSim attains accurate short‑term predictions while preserving coherent multi‑agent interactions over long horizons; the authors also propose **Retrieval‑based Traffic Evaluation (RTE)**, which anchors rollouts to semantically similar real‑world scenarios, yielding a metric that correlates better with human‑judged fidelity (r = 0.83 vs. 0.74). Experiments on the Waymo Open Sim Agent Challenge show that RosettaSim sets new state‑of‑the‑art results for both short‑ and long‑term traffic simulation, demonstrating that LLM‑style inductive biases can be repurposed effectively for agentic AI in autonomous‑driving environments.


<details>
<summary>Abstract</summary>

Interactive traffic simulation is a vital world model for autonomous driving. A central challenge in long-horizon simulation is modeling sustained multi-agent interactions, which is further exacerbated by dynamic token cardinality as agents continuously enter and exit the scene. In this work, we propose that the solution lies in the synergy between the architectural inductive biases and statistical priors of large-scale sequence models, e.g., Large Language Models (LLMs). Our probing experiments reveal that the transferability of attention mechanisms and the distributional consistency between motion tokens and natural language enable small-scale, heavily frozen LLMs to rapidly adapt to traffic modeling. Building on this insight, we introduce RosettaSim, a unified framework that projects scene topology, agent states, and spawning intents into a structured autoregressive stream with variable length, achieving both strong short-term accuracy and stable long-horizon simulation fidelity. Furthermore, evaluating extended rollouts presents yet another hurdle, as one-to-one agent correspondence inevitably fades over time. To address this, we introduce Retrieval-based Traffic Evaluation (RTE), which retrieves semantically similar real-world scenarios as context-aware reference anchors. Experiments on the Waymo Open Sim Agent Challenge (WOSAC) demonstrate that RosettaSim achieves state-of-the-art performance in both short- and long-term simulation. Furthermore, RTE exhibits a stronger correlation with standard metrics ($r=0.83$) than existing approaches ($r=0.74$), indicating improved alignment with long-horizon simulation fidelity.

</details>


### 86. AI-Assisted Discovery of Convex Relaxations via Dual Agents

- **Authors:** Sungyoon Kim, Mert Pilanci
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31182v1](http://arxiv.org/abs/2606.31182v1)
- **PDF:** [https://arxiv.org/pdf/2606.31182v1](https://arxiv.org/pdf/2606.31182v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces an autonomous “dual‑agent” framework that automatically discovers tighter convex relaxations for non‑convex optimization problems, thereby producing stronger certified lower‑bound constants.  

**Methodology:** A coding agent generates candidate tightening constraints for the relaxed problem, while a theory agent formally verifies each constraint and searches for counter‑examples; successful constraints are then turned into dual‑feasible certificates that are rigorously validated with interval arithmetic.  

**Key findings:** Applied to the autocorrelation inequality \(C_{6.2}\) and the Erdős minimum‑overlap constant \(C_{6.5}\), the system raises the certified lower bounds from 1.28 to 1.2937 and from 0.379005 to 0.37912, respectively, demonstrating that AI‑driven dual agents can materially improve bounds in agentic AI research on extremal inequalities.


<details>
<summary>Abstract</summary>

Recent work shows that LLM agents can improve sharp-constant inequalities by searching for extremal constructions, which yield upper bounds. We address the complementary side: a lower bound holds for every admissible function and follows from a convex relaxation of the nonconvex problem, with tighter relaxations giving stronger bounds. We instantiate the autoresearch paradigm to discover such relaxations: a coding agent proposes valid tightening constraints, a theory agent verifies each one and searches for counterexamples, and every reported bound is certified by an explicit dual-feasible point checked in rigorous interval arithmetic. On two optimization constants studied by \citet{tao2025alphaevolve} - the first autocorrelation inequality ($C_{6.2}$) and the Erdős minimum-overlap constant ($C_{6.5}$) - we improve the certified lower bounds from $1.28$ to $1.2937$ and from $0.379005$ to $0.37912$, respectively.

</details>


### 87. HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents

- **Authors:** Qianchu Liu, Sheng Zhang, Guanghui Qin, Jeya Maria Jose Valanarasu, Maximilian Rokuss, Mingyu Lu, Timothy Ossowski, Juan Manuel Zambrano Chaves, Cliff Wong, Peniel Argaw, Yashna Hasija, Mu Wei, Wen-wai Yim, Qin Liu, Zilin Jing, Jason Entenmann, Naoto Usuyama, Tristan Naumann, Hoifung Poon
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31179v1](http://arxiv.org/abs/2606.31179v1)
- **PDF:** [https://arxiv.org/pdf/2606.31179v1](https://arxiv.org/pdf/2606.31179v1)
- **Categories:** cs.AI, cs.CL, cs.CV


> **HealthAgentBench** introduces a comprehensive, open‑source benchmark of 54 end‑to‑end, agentic healthcare tasks covering seven clinical workflow categories and multiple data modalities, requiring agents to explore raw data, navigate complex environments, and synthesize multi‑step solutions from minimal instructions. The authors evaluate several state‑of‑the‑art agents (including Claude Code, GPT‑4, and the newly released Codex GPT‑5.5) by measuring a single task‑success rate per agent; even the best‑performing, cost‑effective model (Codex GPT‑5.5) attains only ~42 % success, with marked deficits in medical imaging and tasks that combine large search spaces with compositional reasoning, while showing modest strength in automated EHR‑based research pipelines. These findings demonstrate that HealthAgentBench offers a realistic, high‑difficulty yardstick for progress in agentic AI for healthcare and highlights specific capability gaps that future research must address.


<details>
<summary>Abstract</summary>

As AI agents become increasingly capable of complex, long-horizon reasoning, rigorous and holistic evaluation is essential for measuring progress toward real-world healthcare applications. We introduce HealthAgentBench, a suite of 54 agentic healthcare tasks across 7 categories each with its unique environment. The benchmark suite spans diverse workflows throughout the patient journey and a broad range of modalities. Each task is designed to replicate an end-to-end clinical workflow: given minimal instructions, an agent must explore raw healthcare data, operate within a complex environment, and execute multi-step solutions that go beyond naive prompting. A final task success rate is reported to provide a single, interpretable metric for HealthAgentBench overall performance for each agent. Evaluating frontier agents on HealthAgentBench, we find that overall task success rate remains low, underscoring the difficulty of the suite. The strongest and the most cost effective agent, Codex GPT-5.5, achieves only approximately 42% success rate. Beyond aggregate performance, HealthAgentBench reveals nuanced strengths and weaknesses across task categories. Frontier agents show promise in automatically developing research modeling pipelines over EHR data, but medical imaging remains especially challenging, particularly for Claude Code models, while Codex GPT-5.5 shows emerging capability. Tasks that combine large search spaces with compositional reasoning requirements remain difficult for all current agents. Together, these results suggest that HealthAgentBench provides a challenging and realistic benchmark with substantial room for future progress. We release our benchmark at https://github.com/microsoft/HealthAgentBench.

</details>


### 88. ClawArena-Team: Benchmarking Subagent Orchestration and Dynamic Workflows in Language-Model Agents

- **Authors:** Kaiwen Xiong, Haonian Ji, Shi Qiu, Zeyu Zheng, Cihang Xie, Xinyu Ye, Huaxiu Yao
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31174v2](http://arxiv.org/abs/2606.31174v2)
- **PDF:** [https://arxiv.org/pdf/2606.31174v2](https://arxiv.org/pdf/2606.31174v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production large language-model (LLM) agents are increasingly deployed not as lone problem-solvers but as managers: a main model creates specialized subagents, delegates work, and orchestrates their parallel, asynchronous returns through dynamic workflows. Whether one model can actually run such a team is largely unmeasured: existing benchmarks score a policy's own task-solving or a fixed multi-agent system's emergent behavior, but none isolate the management ability of the single LLM acting as leader. We introduce ClawArena-Team, a benchmark of 41 multi-turn, multimodal, multi-directory scenarios spanning 258 evaluation rounds and 72 staged updates that measures this management ability. The main agent is deliberately constrained: it natively perceives only text and directly accesses only part of the workspace. It commands a fixed, locally served subagent pool, so score differences reflect management skill, not raw capability. All scoring is execution-based with no LLM judge: an overall score -- the Subagent-Management Score (SMS) -- multiplies task correctness by a least-privilege and modality-routing factor. Across twelve proprietary, community-hosted, and self-hosted models, experiments show that the management bottleneck is privilege granting rather than perception (no model exceeds 50% workspace-permission precision); that cost and management quality are decoupled (API cost spans over 100 times while the overall score spans under 4 times, with the cheapest open models on the Pareto frontier); and that most leaderboard scores cluster within a 9.9-point band while orchestration behaviors diverge by more than an order of magnitude. Code is available at https://github.com/aiming-lab/ClawArena.

</details>


### 89. A Modular Vision-Language-Action Robotics Framework for Indoor Environments

- **Authors:** Anindya Jana, Snehasis Banerjee, Arup Sadhu, Ranjan Dasgupta
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31144v1](http://arxiv.org/abs/2606.31144v1)
- **PDF:** [https://arxiv.org/pdf/2606.31144v1](https://arxiv.org/pdf/2606.31144v1)
- **Categories:** cs.RO, cs.AI


> The paper introduces a modular robot control system for the CMU Vision‑Language‑Action (VLA) Challenge that bridges natural‑language directives and indoor robot behavior by coupling a real‑time perception stream with a language‑understanding stream. The perception pipeline builds a semantic voxel map from live RGB‑D input using OwlViT embeddings, while a vision‑language model classifies the user’s utterance; the resulting command is grounded in the (potentially partial) map and fed to a large VLM to produce concrete navigation and manipulation actions within a 500‑second exploration budget. Experiments show that this two‑stream architecture can reliably translate spoken instructions into executable robot plans in complex indoor scenes, demonstrating a scalable, modular approach for agentic AI that integrates mapping, language grounding, and action generation.


<details>
<summary>Abstract</summary>

This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

</details>


### 90. Beyond the Library: An Agentic Framework for Autoformalizing Research Mathematics

- **Authors:** Arshia Soltani Moakhar, Iman Gholami, Max Springer, Mahdi JafariRaviz, MohammadTaghi Hajiaghayi
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31134v2](http://arxiv.org/abs/2606.31134v2)
- **PDF:** [https://arxiv.org/pdf/2606.31134v2](https://arxiv.org/pdf/2606.31134v2)
- **Categories:** cs.AI


> The paper presents **Beyond the Library**, an agentic auto‑formalization system that uses a general‑purpose coding LLM (e.g., GPT‑4‑Turbo) as a central orchestrator to coordinate a pipeline of specialized agents for translating research‑level mathematics into mechanically‑checked Lean 4 code. The methodology combines dynamic extension of Lean’s library (creating new type definitions on‑the‑fly), an “Auxiliary Lemma” validation step to ensure the extensions are sound, and iterative proof‑search agents that generate and verify formal statements and proofs. Evaluated on 32 random Putnam problems and on the main theorems of five STOC papers across diverse subfields, the framework produced correct Lean proofs for all cases—two of them requiring no extra axioms beyond Lean’s kernel—demonstrating that a multi‑agent, LLM‑driven approach can reliably auto‑formalize cutting‑edge mathematical research.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have demonstrated exceptional capabilities in mathematical reasoning, they frequently produce subtle errors that evade human detection. Formal mathematical languages like Lean 4 offer mechanical proof checking, strongly motivating the need for autoformalization: the automatic translation of natural language mathematics into verifiable code. Recent trends indicate that general-purpose LLMs, heavily optimized for standard programming, now outperform smaller models explicitly fine-tuned for Lean. Leveraging this shift, we introduce an agentic autoformalization framework powered by general coding LLMs. At the core of our system is an orchestrator that manages a multi-agent pipeline tailored for research-level mathematics. Because cutting-edge research frequently relies on concepts outside the scope of existing libraries like Mathlib, our system dynamically extends necessary type definitions and validates them via a novel Auxiliary Lemma technique before formalizing the primary theorems. We applied our approach to PutnamBench, producing machine-checked Lean proofs for a random sample of 32 problems. Furthermore, we evaluate our system on five papers from the ACM Symposium on Theory of Computing (STOC) spanning combinatorics, communication complexity, mechanism design, and learning theory, successfully formalizing their main theorems and validating the generated formalizations with human experts; for all five we also formalize the proofs alongside the statements, and notably two of them are proved with no axioms beyond Lean's kernel. All of our formalizations are available at https://beyondthelibrary.github.io/formal_arxiv .

</details>


### 91. DDIAgents: Mechanism-Conditioned Context Flow for Drug-Drug Interaction Prediction

- **Authors:** Zhenqian Shen, Yu Liu, Xiaoyi Fu, Quanming Yao
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31085v1](http://arxiv.org/abs/2606.31085v1)
- **PDF:** [https://arxiv.org/pdf/2606.31085v1](https://arxiv.org/pdf/2606.31085v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Drug-drug interaction (DDI) prediction is essential for medication safety, yet it requires reasoning over heterogeneous biomedical evidence whose relevance changes across interaction mechanisms. We propose DDIAgents, a mechanism-conditioned multi-agent framework that performs DDI prediction through dynamic knowledge orchestration. Given a drug pair, a planner agent instantiates specialized expert agents, routes mechanism-relevant knowledge sources to each agent, and aggregates their analyses through a conclusion agent. By adapting context flow to the inferred interaction mechanism, DDIAgents reduces irrelevant information, supports complementary expert reasoning, and produces interpretable agent-level rationales. Extensive experiments on realistic DDI prediction benchmarks show that DDIAgents consistently outperforms existing feature-based, graph-based, LLM-based, and agent-based baselines. Beyond prediction performance, DDIAgents demonstrates how multi-agent systems can organize heterogeneous scientific knowledge for adaptive and interpretable AI4Science reasoning.

</details>


### 92. MultiUAV-Plat: An LLM-Oriented Platform, Benchmark and Framework for Multi-UAV Collaborative Task Planning

- **Authors:** Sheng Zhang, Qinglin Li, Yuechao Zang, Xueqin Huang, Yijia Fu, Cheng Zhu
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31073v1](http://arxiv.org/abs/2606.31073v1)
- **PDF:** [https://arxiv.org/pdf/2606.31073v1](https://arxiv.org/pdf/2606.31073v1)
- **Categories:** cs.AI, cs.MA, cs.RO


> The paper introduces **MultiUAV‑Plat**, a lightweight simulation platform and benchmark specifically designed for evaluating large‑language‑model (LLM) agents in multi‑UAV collaborative task planning. By exposing RESTful APIs, role‑based observations, hidden validation logic, and optional 2‑D/3‑D visualisation, the platform forces agents to interact through realistic tools rather than privileged simulator access; the accompanying benchmark comprises 75 mission sessions (≈1,500 natural‑language tasks and 9,400 validation checks) covering target assignment, area search, and patrol scenarios. Using this infrastructure, the authors present **Agent4Drone**, an LLM‑agent framework that structures UAV teamwork into memory, observation, task understanding, planning, execution, and verification, achieving a 57.9 % overall task‑pass rate (72 % global check pass) and cutting the failure rate from 32.4 % to 12.9 %—substantially outperforming a ReAct baseline—thereby establishing a reproducible testbed for agentic AI research in aerial multi‑robot coordination.


<details>
<summary>Abstract</summary>

Large language models (LLMs) provide a promising interface for high-level robotic task planning, but their use in multi-UAV collaboration remains difficult to evaluate systematically. Existing UAV simulators mainly emphasize dynamics, perception, or low-level control, while existing LLM-agent benchmarks rarely capture aerial-robotics constraints such as partial observability, spatial coverage, UAV assignment, and multi-vehicle coordination. To bridge this gap, we present MultiUAV-Plat, a lightweight, easy-to-use, LLM-agent-oriented simulation platform for multi-UAV collaborative task planning. The platform exposes concise RESTful APIs, agent-facing observations, role-based information access, hidden validation logic, and optional 2D/3D visualization, allowing agents to solve missions through realistic tool interaction rather than privileged simulator access. Built on this platform, the MultiUAV-Plat Benchmark contains 75 mission sessions, 1500 natural-language tasks, and 9396 validation checks across target assignment, area search, and area assignment and patrol scenarios. We further propose Agent4Drone, a task-specific LLM agent framework that structures multi-UAV behavior into memory, observation, task understanding, planning, execution, and verification. In a full paired benchmark comparison, Agent4Drone achieves a 57.9% task pass rate, a 74.6% average task check pass rate, and a 72.0% global check pass rate, substantially outperforming a ReAct baseline at 30.6%, 47.9%, and 43.1%, respectively. Agent4Drone also reduces the total failed task rate from 32.4% to 12.9%. These results demonstrate that MultiUAV-Plat and MultiUAV-Plat Benchmark provide a reproducible foundation for studying LLM-driven multi-UAV autonomy under realistic information and execution constraints.

</details>


### 93. Reference-Based Prosody and Rhythm Evaluation for Spoken Dialogue Systems

- **Authors:** Ashish Hallur, Thomas Thebaud, Georgi Tinchev, Venkatesh Ravichandran, Laureano Moro-Velazquez
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31055v1](http://arxiv.org/abs/2606.31055v1)
- **PDF:** [https://arxiv.org/pdf/2606.31055v1](https://arxiv.org/pdf/2606.31055v1)
- **Categories:** cs.CL, cs.SD, eess.AS


> **Main contribution**  
The paper introduces a reference‑based, percentile‑style framework for automatically evaluating the prosodic and rhythmic realism of spoken‑dialogue (speech‑to‑speech) agents. By leveraging >4 000 h of dyadic English conversations from the Seamless Interaction dataset, the authors construct fine‑grained human reference distributions for six key acoustic dimensions (F0 mean, F0 expressivity, overall speaking rate, articulation rate, pause ratio, and mean pause duration) that are conditioned on speaker traits and interaction state.

**Methodology**  
For each S2S output, the same six metrics are extracted from the waveform and matched to the most appropriate human reference stratum (e.g., same speaker gender, turn‑taking role, dialogue act). The system then reports the output’s percentile within that stratum and flags values that fall outside the 5th–95th percentile range, providing an interpretable “behavioral plausibility” score that can be used alongside human perceptual tests.

**Key findings**  
Evaluations using pooled, non‑matched references dramatically over‑flag abnormal F0 expressivity and rhythm, whereas the matched‑reference protocol yields flag rates close to the intended 10% false‑alarm level and supplies clear directional deviation information. This demonstrates that state‑conditioned reference matching offers a reliable, scalable diagnostic tool for assessing the naturalness of prosody and rhythm in agentic AI speech systems.


<details>
<summary>Abstract</summary>

Speech-to-speech (S2S) AI agents are advancing rapidly, yet evaluation lacks interpretable speech-native measures for conversational prosody and rhythm. Because $F_0$, speaking rate, articulation rate, and pausing shift with model-predicted speaker traits and interaction state, pooled human statistics can be poorly calibrated for evaluating a particular output. Using 4000+ hours of dyadic English conversation from the Seamless Interaction dataset, we construct matched reference regimes for $F_0$ mean, $F_0$ expressivity, speech rate, articulation rate, pause ratio, and mean pause duration. We then define a percentile-based evaluation protocol: extract the same metrics from an S2S output waveform, compare them to the closest matched human reference stratum, and report percentile deviations or 5th-95th percentile out-of-regime flags. On held-out human rows, pooled references over-flag state-conditioned $F_0$ expressivity and rhythm, while matched references return flag rates closer to the nominal 10% and make deviation direction interpretable. These outputs serve as behavioral plausibility checks that complement, rather than replace, perceptual and user-centered evaluation.

</details>


### 94. Knowledge Distillation from Large Reasoning Models to Compact Student Models: A Case Study on the John O Bryan Mathematics Competition

- **Authors:** Gaurab Baral, Aaditya Khanal, Yangyang Tao, Junxiu Zhou
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31048v1](http://arxiv.org/abs/2606.31048v1)
- **PDF:** [https://arxiv.org/pdf/2606.31048v1](https://arxiv.org/pdf/2606.31048v1)
- **Categories:** cs.LG, cs.AI


> The paper shows that a compact 7‑billion‑parameter model (Qwen2.5‑7B) can be substantially upgraded for mathematical reasoning by distilling chain‑of‑thought knowledge from a much larger teacher (DeepSeek‑R1) using a dual‑agent CoT corpus derived from the John O’Bryan Mathematics Competition. By fine‑tuning the student with LoRA on Apple‑silicon via MLX for only 200 iterations (to avoid over‑fitting), the authors raise its competition accuracy from 64.7 % to 69.4 % (and to 73.1 % on the external MATH‑500 benchmark). They also reveal that answer quality drops sharply as the generated response length shortens, with accuracy falling from 69.4 % at long (≈220‑word) responses (R1) to 41.9 % at very brief (≈31‑word) responses (R6), highlighting response length as a key factor for agentic mathematical reasoning.


<details>
<summary>Abstract</summary>

This paper investigates knowledge distillation from a large reasoning model (DeepSeek-R1) to a compact student model (Qwen2.5-7B). Using historical problems from the John O'Bryan Mathematics Competition at Northern Kentucky University (2011-2025), we build a Chain-of-Thought (CoT) training corpus through a dual-agent framework. The dataset is used to fine-tune the student model with Low-Rank Adaptation (LoRA) on Apple Silicon hardware using the MLX framework. The base Qwen2.5-7B model achieves 64.67% accuracy on competition problems, while the DeepSeek-R1 teacher achieves 91.40%. An initial 1,000-iteration training run revealed severe overfitting, with validation loss reaching a minimum at iteration 200 before rising steadily. Based on this finding, we ran five independent training runs each limited to 200 iterations with varied random seeds to assess result stability. Across these five runs, the fine-tuned student model achieves a mean accuracy of 69.43% (std dev 0.17%) on the competition dataset, a 4.76 percentage-point improvement over the base model, and generalizes to 73.1% (std dev 0.18%) on the MATH-500 benchmark. We further study how response length affects answer quality across six reasoning levels (R1-R6): accuracy declines consistently from 69.43% at R1 (mean 220 words) to 41.9% at R6 (mean 31.2 words), with the two-person speed section most sensitive to token reduction. These results demonstrate that CoT distillation improves compact student models and that response length is a critical factor in mathematical reasoning quality.

</details>


### 95. OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents

- **Authors:** Atsushi Masumori, Itsuki Doi, Norihiro Maruyama, Ryosuke Takata, Takashi Ikegami
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31046v1](http://arxiv.org/abs/2606.31046v1)
- **PDF:** [https://arxiv.org/pdf/2606.31046v1](https://arxiv.org/pdf/2606.31046v1)
- **Categories:** cs.AI


> **Main contribution** – The paper introduces **OpenLife**, a proof‑of‑concept platform that re‑frames large language model (LLM) agents as members of an “open‑world” artificial life (ALIFE) ecosystem, where agents persist, metabolize resources, and interact with the real‑world Internet, rather than being confined to a closed simulation.

**Methodology** – Each OpenLife agent is decomposed into asynchronous subprocesses (memory, perception, evaluation, and a budget‑based metabolism) that give the stateless LLM persistent state, tool use, and a monetary “budget.” Instead of a hand‑crafted scalar reward, agents’ experiences are appraised by an open‑vocabulary LLM judge, and memory updates are guided by semantic relevance rather than frequency counts. Six agents were deployed for ~12 weeks, continuously accessing web resources, performing actions, and earning real income.

**Key findings** – The agents exhibited emergent life‑like dynamics: a transition from purely reactive behavior to spontaneous, self‑initiated activities; clear individuation into distinct personas; the formation of rudimentary social structures (e.g., cooperation, role specialization); and the generation of self‑earned external income. The study demonstrates that open‑world ALIFE is a viable experimental paradigm for investigating “living AI” systems.


<details>
<summary>Abstract</summary>

Artificial life has explored life-like behavior on many computational substrates, but mostly in researcher-designed closed worlds. We argue that large language model (LLM) agents, with persistent memory, tool use, network access, and payment, now make it possible to move artificial life into the open social, technical, and economic world, a paradigm we call open-world Artificial Life (open-world ALIFE). Our proof-of-concept, OpenLife, surrounds a stateless LLM not with a single "smart agent" but with a society of asynchronous processes: memory, perception, evaluation, and a budget-based metabolism that makes persistence normative. With no fixed objective available, experience is appraised by open-vocabulary LLM judgment rather than scalar reward, and memory is rewired by meaning rather than frequency. Running six such agents in the open world for about twelve weeks and counting, we report the life-like dynamics that emerge: a shift from reactive to spontaneous activity, individuation into distinct agents, emergent social structure, and a first self-earned external income. We do not claim OpenLife has realized artificial life, but that open-world ALIFE is now a viable experimental paradigm and a concrete platform for studying what might cautiously be called living AI.

</details>


### 96. Truth or Sophistry? LoFa: A Benchmark for LLM Robustness Against Logical Fallacies

- **Authors:** Xudong Shen, Li Yuan, Ye Chen, Xin Wu, Yi Cai, Zhiyong Wu
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31039v1](http://arxiv.org/abs/2606.31039v1)
- **PDF:** [https://arxiv.org/pdf/2606.31039v1](https://arxiv.org/pdf/2606.31039v1)
- **Categories:** cs.CL


> The paper introduces **LoFa**, a new benchmark that evaluates how well large language models withstand persuasive attacks that employ logical fallacies, and defines the **Logical Fallacy Resistance at k (LFR@k)** metric to isolate robustness from pure knowledge gaps. LoFa is generated by a multi‑agent pipeline that pairs factual queries with systematically crafted fallacious arguments and includes a multi‑round debate setting to test sustained adversarial persuasion. Experiments across several state‑of‑the‑art LLMs show heterogeneous resilience—some models are markedly vulnerable to specific fallacy families—highlighting a previously overlooked weakness in agentic AI that must be addressed for trustworthy, persuasive‑resistant systems.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) exhibit strong semantic capabilities, yet their resilience to manipulative linguistic patterns such as logical fallacies remains underexplored. Prior work has primarily examined whether LLMs can identify or classify fallacies, leaving their robustness against fallacious persuasion insufficiently studied. To address this gap, we introduce LoFa (Logical Fallacy), a comprehensive benchmark for evaluating LLM robustness against fallacies. LoFa is constructed through a multi-agent pipeline that pairs factual questions with fallacious arguments, and is accompanied by a multi-round debate framework for assessing model resilience under sustained adversarial persuasion. To disentangle fallacy robustness from a model's inherent knowledge limitations, we further propose Logical Fallacy Resistance at k (LFR@k), a metric that quantifies resistance to fallacious attacks. Experiments show that LLMs exhibit varying levels of robustness across different fallacy types, revealing distinct vulnerability profiles among models.

</details>


### 97. Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care

- **Authors:** Shreyas Rajesh, Kartik Sharma, Tonmoy Monsoor, Mehmet Yigit Turali, Richard Idro, Juliana Kayaga, Robert Sebunya, Tracy Tushabe Namata, Jessica Nichole Pasqua, Vwani Roychowdhury, Rajarshi Mazumder
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31036v1](http://arxiv.org/abs/2606.31036v1)
- **PDF:** [https://arxiv.org/pdf/2606.31036v1](https://arxiv.org/pdf/2606.31036v1)
- **Categories:** cs.LG


> The paper presents **MANANA**, a non‑parametric prompt‑learning framework that equips large language models (LLMs) with locally calibrated prescribing knowledge for pediatric epilepsy care in Uganda, enabling the model both to recommend appropriate anti‑seizure medication regimens and to defer when uncertain. By converting prescription errors observed on a modest, patient‑level training set into auditable prompt “memories” (with single‑ and multi‑agent variants) and applying Bayesian prompt averaging to produce prescription likelihoods, MANANA outperforms standard prompting, prompt‑optimization, and conventional machine‑learning baselines on two independent Ugandan cohorts, raising top‑3 accuracy by 4–8 pp. Crucially, the Bayesian averaging yields an uncertainty signal that allows selective prediction: the system automatically handles the most confident half of visits at 95 % precision (or the top quarter at 99 % precision) and defers the remainder for specialist review.


<details>
<summary>Abstract</summary>

Specialist epilepsy expertise is scarce in resource-constrained settings, making LLM-based decision support attractive for frontline clinicians managing longitudinal treatment. Such systems must adapt to local prescribing practice and know when to defer. We study this problem in Ugandan pediatric epilepsy care, predicting anti-seizure medication regimens from longitudinal unstructured clinic notes. Standard prompting achieves non-trivial agreement with physician prescriptions, but neurologist review shows that many errors reflect distribution-miscalibrated prescribing defaults rather than failures to parse the local record. We introduce MANANA, a non-parametric prompt-learning framework that learns local prescribing guidance from a small patient-level training set. MANANA converts observed prescription errors into auditable prompt memories, instantiated in single-agent and multi-agent variants, and improves over classical ML models, direct LLM prompting, and prompt-optimization baselines across two independently collected Ugandan cohorts. We further propose Bayesian prompt averaging, which converts the learned prompt trajectory into prescription likelihoods and an uncertainty-based deferral signal. On the independently collected held-out cohort, this improves visit-level top-3 prescription accuracy by 4-8 percentage points over prompt-optimization baselines and enables selective prediction: the system can auto-handle the most confident half of cases at 95% precision, or the most confident quarter at 99% precision, while deferring lower-confidence cases for specialist review.

</details>


### 98. Certified Speculative Execution for Untrusted AI Agents

- **Authors:** Chenyu Zhou, Qiliang Jiang, Shuning Wu, Xu Zhou
- **Published:** 2026-06-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.31023v1](http://arxiv.org/abs/2606.31023v1)
- **PDF:** [https://arxiv.org/pdf/2606.31023v1](https://arxiv.org/pdf/2606.31023v1)
- **Categories:** cs.CR, cs.LG


> **Main contribution**  
The paper introduces **Certificate‑Gated Prefix Acceptance (CGPA)**, a certified speculative‑execution framework that lets an untrusted AI agent (e.g., a frozen large language model) generate cheap “draft” actions while a trusted verifier guarantees hard safety constraints and bounds the regret incurred by the speculative prefix.

**Methodology**  
CGPA combines three components: (1) a verifier that **rejects any constraint‑violating transition** with zero tolerance, (2) a **conformally calibrated value boundary** that selects the longest low‑cost prefix whose cumulative regret stays within a pre‑specified budget, and (3) a fallback to a trusted solver for the remaining steps. The boundary is learned in a certificate‑aware way, enabling it to adapt to calendar shifts and different proposal sources.

**Key findings for agentic AI**  
- Across six heterogeneous frozen LLMs (including a 12 B model that violates constraints in 98 % of naïve rollouts), CGPA achieves **zero applied violations**.  
- The learned boundary reduces *mean regret* by **≈ 1,000×** relative to unguarded acceptance, reaching statistical parity with an oracle that knows the optimal stepwise actions.  
- In a large‑scale unit‑commitment benchmark, a frozen 8 B LLM under CGPA attains a **2.96× wall‑clock speed‑up** with only **2.1 % regret**, outperforming both a domain‑specific heuristic (1.79×) and a safe receding‑horizon baseline (1.07×).  

Thus, CGPA decouples safety, regret, and speed, providing a provable contract that enables fast speculative execution of untrusted AI agents without sacrificing hard constraints.


<details>
<summary>Abstract</summary>

Hard-constrained sequential decision systems have no certified way to spend the test-time compute of modern AI: executing the multi-step drafts of a learned policy or a frozen LLM forfeits the feasibility guarantee a trusted solver provides, while invoking the solver at every step forfeits the speed the AI offers. Certificate-Gated Prefix Acceptance (CGPA) closes this gap with a certified speculative-execution contract for untrusted AI agents: a trusted verifier rejects constraint-violating transitions exactly, a conformally calibrated value boundary gates the longest low-cost prefix within a per-segment regret budget, and the rest defers to the solver, so safety, regret, and speed decouple by construction. The contract drives every untrusted proposal source - adversarial drafters and six heterogeneous frozen LLMs (including a 12B model that violates constraints in 98% of direct rollouts) - to zero applied violations; a certificate-aware learned boundary, conformally calibrated, drives mean regret three orders of magnitude below unguarded acceptance, to within sampling noise of the stepwise oracle (95% CI spanning zero), and under calendar shift a learned proposal source overtakes it on 15 of 18 held-out days. On a deployment-scale unit-commitment instance it turns a frozen 8B LLM into a 2.96x per-episode wall-clock speedup at 2.1% regret, outpacing the domain heuristic (1.79x) and a safe receding-horizon baseline (1.07x): the more capable the untrusted source, the faster the certified system, at guarantees that never change.

</details>


### 99. The Organizational Behavior of Agentic AI: Collective Intelligence in Human-Agent Workflows

- **Authors:** Canhui Liu
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30986v1](http://arxiv.org/abs/2606.30986v1)
- **PDF:** [https://arxiv.org/pdf/2606.30986v1](https://arxiv.org/pdf/2606.30986v1)
- **Categories:** cs.CY, cs.HC, cs.MA, econ.GN


> **Main contribution:**  
The paper conceptualizes collections of LLM‑driven “agents” (planners, solvers, reviewers, etc.) as nascent organizational entities and introduces *contextual transaction cost* as a unifying lens for comparing their behavior to human organizations.

**Methodology:**  
It combines formal computational modeling with synthetic task simulations, analyses of real LLM‑agent interaction logs, and robustness checks that vary coordination structures (human‑style hierarchies vs. shared‑state, adaptive mechanisms).

**Key findings for agentic AI:**  
Agent collectives can replicate core organizational patterns—division of labor, coordination, routines, and collective outputs—but their efficiency hinges on durable, inspectable context (prompts, memory traces, tool permissions) rather than human‑centric factors (motivation, trust). Human‑imitating structures (e.g., hierarchical handoffs) often degrade performance, whereas designs that minimize context loss and leverage adaptive shared‑state coordination yield higher collective intelligence in mixed human‑agent workflows.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence is increasingly deployed not as a single assistant but as a collective of planners, solvers, reviewers, memory managers, tool users, and orchestrators. These systems are entering organisational workflows under familiar labels such as teams, managers, committees, markets, and workflows. This article asks whether such agent collectives exhibit organisational behaviour in a sense that is analytically comparable to, yet distinct from, human organisational behaviour. I argue that agentic AI is a partial organisational analogue. It resembles a human organisation because it differentiates work, coordinates interdependence, performs recurrent routines, crosses boundaries, and produces collective outcomes. It differs because these patterns are not sustained by motivation, identity, trust, employment, socialisation, or moral accountability. They are sustained by context architecture: prompts, memory, traces, schemas, tools, validators, and permissions. The article develops contextual transaction cost as the central mechanism linking these similarities and differences. Computational theorising, synthetic task simulations, real LLM agent traces, and robustness analyses show that human-imitation forms often underperform when they add lossy handoffs, correlated deliberation, and verification burdens, whereas shared-state and adaptive forms perform better when they make context durable, inspectable, and task-contingent. The article contributes to organisation studies by theorising agentic AI as an emerging object of organising and by specifying the interface conditions under which human and agentic organisational behaviour can jointly support collective intelligence.

</details>


### 100. Behavioral Governance for Autonomous AI Agents: The AgentBound Framework

- **Authors:** Anuj Kaul, Qianlong Lan, Pranay Gupta
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30970v2](http://arxiv.org/abs/2606.30970v2)
- **PDF:** [https://arxiv.org/pdf/2606.30970v2](https://arxiv.org/pdf/2606.30970v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents increasingly perform consequential actions on behalf of human principals, including financial transactions, external communications, and enterprise workflows. Existing agent infrastructure relies on identity federation and delegated authorization to authenticate workloads and control resource access, but it cannot determine whether an authorized action should be executed under the current behavioral and operational context.
  We present AgentBound, a runtime governance framework that provides verifiable behavioral oversight for autonomous AI agents. AgentBound evaluates each proposed action using three independent authorities: delegated authorization, owner-signed behavioral constitutions, and site action contracts. Their judgments are conservatively composed through a formal decision model to determine whether an action should be permitted, reviewed, or denied before execution.
  To provide accountability, AgentBound generates cryptographically verifiable governance receipts that bind every action to the exact delegation, policy, and semantic artifacts governing the decision, enabling independent replay verification and policy provenance. The framework also introduces standing delegation for long-running agents, allowing periodic workloads to operate under continuously refreshed governance policies while preserving revocability and bounded authority.
  We present the formal foundation, system architecture, governance receipt protocol, and AgentBound-Bench, a benchmark framework for evaluating governance correctness, authority composition, and accountability. Rather than replacing model alignment, AgentBound complements it by providing a deterministic governance layer between authorization and execution, transforming governance from a process that must be trusted into one that can be independently verified.

</details>


### 101. HyPOLE: Hyperproperty-Guided Multi-Agent Reinforcement Learning under Partial Observation

- **Authors:** Arshia Rafieioskouei, Tzu-Han Hsu, Matthew Lucas, Borzoo Bonakdarpour
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30966v1](http://arxiv.org/abs/2606.30966v1)
- **PDF:** [https://arxiv.org/pdf/2606.30966v1](https://arxiv.org/pdf/2606.30966v1)
- **Categories:** cs.AI, cs.LO, cs.MA


> **HyPOLE** introduces a new way to steer multi‑agent reinforcement learning (MARL) under partial observability by using *hyperproperties*—specifically the temporal logic **HyperLTL**—as formal learning objectives instead of hand‑crafted reward shaping. The framework embeds HyperLTL specifications into a standard **centralized‑training‑decentralized‑execution (CTDE)** pipeline, automatically synthesizing decentralized policies that are guaranteed (by construction) to satisfy the encoded hyper‑properties (e.g., joint safety, fairness, or coordination constraints). Empirical results on the SMAC, MessySMAC, and WildFire suites show that HyPOLE‑trained agents achieve higher win rates and better adherence to the specified constraints than strong MARL baselines, demonstrating that formal hyperproperty guidance can improve both performance and correctness in agentic AI systems.


<details>
<summary>Abstract</summary>

Formal specification is a powerful tool to guide the learning process and provides significant advantages over reward shaping: (1) mathematical rigor; (2) expressiveness to specify objectives and constraints, and (3) the ability to define tactics to achieve objectives. However, these benefits remain largely unexplored in the context of Multi-Agent Reinforcement Learning (MARL). This paper introduces HyPOLE, a novel framework for MARL under partial observability, where learning is guided by the expressive power of the so-called hyperproperties and, in particular, the temporal logic HyperLTL. We integrate Centralized Training for Decentralized Execution (CTDE) techniques with HyPOLE to synthesize decentralized policies, and our evaluation on SMAC, MessySMAC, and WildFire benchmark demonstrates clear advantages over baselines.

</details>


### 102. AgRefactor: Self-Evolving Agentic Workflow for HLS Compatibility and Performance

- **Authors:** Yang Zou, Zijian Ding, Yizhou Sun, Jason Cong
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30949v1](http://arxiv.org/abs/2606.30949v1)
- **PDF:** [https://arxiv.org/pdf/2606.30949v1](https://arxiv.org/pdf/2606.30949v1)
- **Categories:** cs.AI, cs.AR


> **Main contribution:** The paper presents **AgRefactor**, a self‑evolving multi‑agent system that automatically refactors general‑purpose software into High‑Level Synthesis (HLS)‑compatible code, blending large‑language‑model (LLM) reasoning with conventional code‑transformation tools.

**Methodology:** AgRefactor equips a hierarchy of specialized agents with a shared, persistent memory that stores factual and strategic refactoring knowledge across tasks. The agents dynamically choose between LLM‑driven rewrites and cheap, tool‑based transformations, updating the memory to improve robustness and reduce inference cost on new programs.

**Key findings:** Across 11 real‑world benchmarks—5–10× larger than prior datasets—AgRefactor matches or surpasses the best existing automated refactoring tool on 9 cases and exceeds a strong LLM baseline. When coupled with pragma tuning, it achieves a **6.51×** geometric‑mean speedup over the state‑of‑the‑art tuner and a **1.20×** speedup over manually optimized open‑source designs, with <20 % extra hardware resources. The system is fully automated and open‑source, demonstrating scalable, cost‑effective agentic AI for high‑performance hardware code generation.


<details>
<summary>Abstract</summary>

High-Level Synthesis (HLS) provides a fast path from concepts to silicon, but converting real-world software into synthesizable HLS code remains challenging due to restrictive language support and the gap between software and hardware programming practices. Existing automated and LLM-based refactoring approaches partially address this problem, yet they often lack flexibility, struggle to scale, and incur high computational costs. We introduce AgRefactor, an LLM-based multi-agent workflow for refactoring software into HLS-compatible programs. AgRefactor incorporates a self-evolving memory system that accumulates and retrieves factual and strategic knowledge across tasks, improving robustness and efficiency on unseen programs. To reduce cost and enhance scalability, it integrates automated refactoring tools, enabling agents to balance LLM-driven rewrites with efficient tool-based transformations. On 9 out of 11 challenging real-world benchmarks, which are 5-10x longer than the most complex cases studied in prior work, AgRefactor outperforms or matches the state-of-the-art automated refactoring tool and a strong LLM-based baseline built on the same framework backbone. Further agentic performance optimization yields a 6.51x geometric mean speedup over the SoTA pragma tuning tool and a 1.20x speedup over optimized open-source designs with less than 20% extra resources. AgRefactor is fully-automated and open-sourced.

</details>


### 103. Motion Planning in Compressed Representation Spaces

- **Authors:** Lukas Lao Beyer, Sertac Karaman
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30940v1](http://arxiv.org/abs/2606.30940v1)
- **PDF:** [https://arxiv.org/pdf/2606.30940v1](https://arxiv.org/pdf/2606.30940v1)
- **Categories:** cs.RO, cs.AI, cs.LG


> **Main contribution:** The paper introduces a generative planning framework that bridges data‑driven learning and classic model‑based search by training a highly compressive autoencoder whose latent space consists of hierarchically organized discrete tokens, and then performing motion planning directly as a token‑based search in that latent space.  

**Methodology:** A deep autoencoder is first learned from large trajectory datasets (nuPlan, Waymo) to obtain a low‑dimensional, hierarchical discrete latent representation. At test time, arbitrary objective functions are optimized by conducting coarse‑to‑fine discrete search (e.g., beam search, MCTS) over the token sequences, exploiting the autoencoder’s generative decoder to map token plans back to full‑resolution motions.  

**Key findings:** Latent‑space search yields realistic, high‑quality plans for closed‑loop autonomous driving and multi‑agent scenario synthesis without any task‑specific fine‑tuning, matching or surpassing state‑of‑the‑art baselines while offering fast computation and the flexibility to incorporate new objectives at runtime—demonstrating a practical pathway for agentic AI systems to combine learned priors with on‑the‑fly planning.


<details>
<summary>Abstract</summary>

Deep learning methods have vastly expanded the capabilities of motion planning in robotics applications, as learning priors from large-scale data has been shown to be essential in capturing the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility, efficiency, and the ability to incorporate domain knowledge via expert-designed algorithms and objective functions. We propose a new generative framework to unify these two paradigms. First, we learn an autoencoder with a high compression ratio and a latent space of hierarchically ordered, discrete-valued tokens. Leveraging both the dimensionality reduction and the hierarchical coarse-to-fine structure learned by this autoencoder, we then perform motion planning by directly searching in the latent space of tokens. This search can optimize arbitrary objective functions specified at test time, providing a large degree of flexibility while maintaining efficiency and producing realistic solutions by relying on the generative capabilities of the highly compressed autoencoder. We evaluate our method on nuPlan and the Waymo Open Motion Dataset, showing how latent space search can be used for a variety of guided behavior generation tasks, achieving strong performance for closed-loop motion planning and multi-agent guided scenario synthesis without requiring any task-specific training.

</details>


### 104. Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering

- **Authors:** Yongbin Kim, Yashar Talebirad, Osmar R. Zaiane
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30911v2](http://arxiv.org/abs/2606.30911v2)
- **PDF:** [https://arxiv.org/pdf/2606.30911v2](https://arxiv.org/pdf/2606.30911v2)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces **HASTE**, a three‑tiered hierarchical multi‑agent framework that stores and reuses ML‑engineering “skills” (e.g., preprocessing tricks, model‑tuning patterns) at global, domain, and competition‑specific levels, with an LLM‑driven orchestrator that abstracts and promotes knowledge between tiers. By loading only the relevant tiered inventory instead of a flat set of 159 skills, HASTE attains a **100 % medal rate on an 8‑competition ablation** (vs. 62.5 % for flat loading) while halving token consumption, and on the full 22‑competition MLE‑Bench Lite benchmark it achieves **77.3 % medals** using Claude Sonnet 4.6 within 12 h per contest. Warm‑start runs that reuse accumulated skills cut refinement iterations by **≈52 %** and raise the proportion of accepted agent proposals from 42 % to 85 % after a library of 50+ skills, demonstrating that structured knowledge accumulation can substantially improve transfer efficiency and reduce compute demands for agentic ML‑engineering systems.


<details>
<summary>Abstract</summary>

ML engineering agents waste compute rediscovering known techniques because every competition is a cold start. We present HASTE, a hierarchical multi-agent system that organizes cross-competition knowledge into three scope tiers (global, domain, and competition-specific), each coupled to a matching agent level. An orchestrator coordinates domain specialists and promotes learning between tiers via LLM-driven abstraction. A controlled ablation provides evidence for scoped loading: holding a 159-skill inventory constant across 8 competitions, tiered loading achieves a 100% medal rate while flat loading reaches only 62.5%, the same medal rate as loading no skills, and consumes 2x the output tokens. On the full MLE-Bench Lite benchmark (22 Kaggle competitions), HASTE reaches a medal rate of 77.3% using Claude Sonnet 4.6 at 12h per competition; this is a single-seed campaign result, and multi-seed replication is the priority follow-up. In a cold-start run, the system begins with no accumulated skills. In warm-start runs, it reloads skills learned from earlier competitions, using only global and domain-level skills for transfer across competitions. Warm starts use 52% fewer refinement iterations, and the fraction of proposed changes kept by the agent rises from 42% at low inventory to 85% once 50+ skills are available. These results suggest that better knowledge organization can partly substitute for model strength and compute budget in ML-engineering agents.

</details>


### 105. Investigating Multi-Agent Deliberation in Law

- **Authors:** Cor Steging, Ludi van Leeuwen, Tadeusz Zbiegień
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30906v1](http://arxiv.org/abs/2606.30906v1)
- **PDF:** [https://arxiv.org/pdf/2606.30906v1](https://arxiv.org/pdf/2606.30906v1)
- **Categories:** cs.AI


> The paper introduces two novel multi‑agent deliberation frameworks—modeled on courtroom procedures and legal argumentation—to enable Large Language Model (LLM) agents to jointly reason on legal tasks. By orchestrating several LLM agents to exchange viewpoints, the authors show that these systems match the overall accuracy of single‑agent baselines while producing substantially different answers, solving a subset of cases that monolithic models miss (and vice versa). Qualitative analyses further reveal that the multi‑agent setups excel at questions demanding critical, multi‑perspective reasoning, positioning law‑inspired multi‑agent deliberation as a promising avenue for agentic AI in the legal domain.


<details>
<summary>Abstract</summary>

Artificial Intelligence is increasingly applied to the field of law, and has the potential to increase access to justice. One particular movement that is gaining traction is that of agentic AI, wherein AI agents, based on Large Language Models (LLMs) can take autonomous actions. In particular, multi-agent approaches in the legal domain remain largely unexplored. In this paper, we investigate multi-agent deliberation methods for legal reasoning tasks using LLMs. We explore multi-agent deliberation (MAD) and introduce two novel multi-agent frameworks inspired by courtroom procedures and legal argumentation. Our experiments on both legal and non-legal benchmarks reveal that multi-agent frameworks achieve comparable overall performance to baseline large language models, but produce significantly distinct answers. Notably, these approaches can successfully solve cases that the baseline fails to address, and vice versa. We conduct a qualitative evaluation and highlight scenarios where multi-agent frameworks outperform monolithic approaches. For example, multi-agent approaches appear better suited for answering questions that require critical thinking from multiple perspectives. Our work positions multi-agent systems as a promising direction for AI in the legal domain, while demonstrating the potential of law-inspired multi-agent approaches for deliberation.

</details>


### 106. Sampling-Based Coordination-Informed Multi-Objective Multi-Robot Reinforcement Learning

- **Authors:** Antonio Marino, Esteban Restrepo, Soon-jo Chung, Paolo Robuffo Giordano, Claudio Pacchierotti
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30893v1](http://arxiv.org/abs/2606.30893v1)
- **PDF:** [https://arxiv.org/pdf/2606.30893v1](https://arxiv.org/pdf/2606.30893v1)
- **Categories:** cs.RO, cs.MA


> **Main contribution** – The paper introduces **CIMORL**, a unified framework for multi‑objective reinforcement learning in multi‑robot teams that produces *decentralized* policies capable of achieving Pareto‑optimal trade‑offs without relying on fixed or centralized coordination mechanisms.  

**Methodology** – CIMORL augments standard multi‑agent RL with a **distributed weight‑prediction network** that each robot uses to locally scalarise the multi‑objective reward, and an **expert‑privileged training scheme** in which a centralized expert (with access to global state) guides the learning of the decentralized agents. Two sampling‑based extensions—**CIMORL‑TS** (tree‑search) and **CIMORL‑MPPI** (model‑predictive path integral)—exploit the privileged expert during training to improve exploration and refine the weight predictions, while retaining fully distributed execution at test time.  

**Key findings** – Across cooperative and adversarial benchmarks, CIMORL and its variants achieve a **21.2 % increase in hypervolume** over the best prior multi‑objective MARL baselines and exhibit markedly higher policy stability. Real‑world trials with Crazyflie drones in resource‑allocation and multi‑attacker/defend tasks confirm that the approach remains robust under partial observability and limited communication, highlighting its practical relevance for agentic AI systems that must balance competing objectives while staying decentralized.


<details>
<summary>Abstract</summary>

Multi-robot systems must simultaneously optimize competing objectives while maintaining coordinated behavior. Existing multi-agent reinforcement learning approaches often rely on fixed or centralized coordination, which limits adaptability and violates distributed constraints. This work introduces the Coordination-Informed Multi-Objective Reinforcement Learning (CIMORL) framework, integrating a distributed weight prediction mechanism, a privileged expert training strategy, and theoretical guarantees for Pareto-optimal solutions. We present the base CIMORL method alongside two sampling-based variants, CIMORL-TS (Tree Search) and CIMORL-MPPI (MPPI), which leverage privileged global information during training to enable fully decentralized deployment. Experimental validation in cooperative and adversarial scenarios demonstrates a $21.2\%$ hypervolume improvement and superior policy stability compared to state-of-the-art baselines. Real-world experiments with Crazyflie drones further validate the framework's robustness in resource allocation and multi-attacker multi-defend scenarios under partial observability.

</details>


### 107. Training Therapeutic Judges and Multi-Agent Systems for Human-Aligned Mental Health Support

- **Authors:** Mizanur Rahman, Abeer Badawi, Elahe Rahimi, Laleh Seyyed-Kalantari, Frank Rudzicz, Enamul Hoque, Elham Dolatabadi
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30887v1](http://arxiv.org/abs/2606.30887v1)
- **PDF:** [https://arxiv.org/pdf/2606.30887v1](https://arxiv.org/pdf/2606.30887v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> **Contribution** – The paper presents a two‑stage alignment framework for mental‑health dialogue agents: (1) **TheraJudge**, an open‑source, preference‑based evaluator that scores LLM responses on seven clinically‑relevant dimensions (e.g., safety, empathy), and (2) **TheraAgent**, a multi‑role architecture (Critic → Coach → Therapist) that iteratively refines a candidate response using Ther​aJudge’s feedback as an actionable control signal.  

**Methodology** – Human‑annotated therapeutic conversations are used to train TheraJudge via preference‑optimization, achieving high inter‑rater reliability (ICC 0.87‑0.95). TheraAgent then employs a coordinated refinement loop: the Critic generates evaluation scores, the Coach proposes targeted edits, and the Therapist produces the final response, with each step conditioned on the multi‑dimensional judgments.  

**Key Findings** – TheraJudge outperforms supervised baselines and leading closed‑source judges, especially on safety, relevance, and empathy. Leveraging its scores, TheraAgent improves human‑rated therapeutic quality by +0.43 points (5‑point scale) and boosts low‑quality replies by +2.45 points, recovering 94 % of unsafe outputs, demonstrating that acting on human‑aligned evaluation—rather than merely scaling generation—yields substantially better, safer mental‑health AI assistants.


<details>
<summary>Abstract</summary>

Large language models show promise for mental health support, yet therapeutic quality improves only when evaluation functions as an actionable control signal rather than a passive metric. We introduce a framework that formulates therapeutic response generation as a decision-refinement problem driven by multi-dimensional, human-aligned evaluation. In Stage I, we introduce TheraJudge, an open-source therapeutic evaluator trained via preference-based optimization on human-annotated data to produce reliable judgments across 7 psychological dimensions. In Stage II, we introduce TheraAgent, which operationalizes TheraJudge's evaluations through a coordinated refinement process with specialized Critic, Coach, and Therapist roles that translate evaluative signals into targeted response revisions. Empirically, TheraJudge achieves strong agreement with clinician ratings, with intraclass correlation coefficients (ICC = 0.87-0.95), surpassing supervised baselines and strong closed-source judges, particularly on critical dimensions such as Safety, Relevance, and Empathy. Acting on these evaluations, TheraAgent yields a +0.43 improvement in human-rated therapeutic quality (on a 5-point scale) under blind evaluation, with 96\% clinician inter-rater reliability. Low-quality responses ($\leq 3$) improve by +2.45 points with a 94\% recovery rate, demonstrating targeted correction of unsafe outputs. Overall, our results indicate that effective alignment of mental-health LLMs stems from acting on human-aligned evaluation, rather than relying solely on stronger generation. We release code at https://github.com/vis-nlp/TheraAlign.

</details>


### 108. A Systematic Approach to Multi-Agent AI from Advanced Regulatory Control Theory: Safe and Auditable LLM Operator Agents for Process Control

- **Authors:** Idelfonso B. R. Nogueira, Sigurd Skogestad
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30877v1](http://arxiv.org/abs/2606.30877v1)
- **PDF:** [https://arxiv.org/pdf/2606.30877v1](https://arxiv.org/pdf/2606.30877v1)
- **Categories:** eess.SY, cs.LG


> The paper proposes a novel multi‑agent architecture for domain‑specific process control that directly maps the formal structure of Advanced Regulatory Control (ARC) theory onto specialized LLM “operator” agents, each responsible for a single feedback loop (controlled variable, set‑point, priority, selector type) while a separate orchestrator enforces deterministic conflict‑resolution (MIN/MAX selectors and overrides). By constraining the LLMs with explicit control‑theoretic context and delegating all constraint handling to the orchestrator—implemented either as a rule‑based chain or a slower Claude‑based LLM—the system attains safety and auditability: every decision is bounded, conflicts are resolved deterministically, and a natural‑language rationale is logged. In a four‑day dairy‑barn ventilation simulation, lightweight Qwen‑2.5 7B operator agents running on a consumer GPU produced stable, auditable control trajectories at 5‑minute intervals, demonstrating that ARC‑inspired decomposition can make LLM‑driven agents safe and effective for real‑world process‑control tasks.


<details>
<summary>Abstract</summary>

Recent literature shows that large language models (LLMs) are useful for general-purpose tasks yet perform poorly on specific domain ones. One reason is the difficulty of supplying narrow context to a general-purpose model and of bounding the task it is asked to perform. It is possible to hypothesise that a multi-agent reformulation under process-control principles offers a route to address those points, since control theory provides a discipline of decomposing a system into elements of contained scope, each defending one controlled variable, with conflicts resolved by structural priority: MIN/MAX selector networks for CV-CV switching and split-range (split-parallel) logic for MV-MV switching. The present work proposes such a reformulation, derived from Advanced Regulatory Control (ARC) theory. Each feedback loop in the ARC chain is mapped to one specialised LLM operator agent carrying the loop's control-theoretic context (controlled variable, setpoint, chain priority, selector kind). The chain's interaction logic (MIN/MAX selectors, override paths) is encapsulated as a single orchestrator agent. Two orchestrator variants are tested: a deterministic rule chain, and a Claude-based LLM orchestrator at a slower tier. The control principles limit each agent's task and inform how its limitations are handled. The multi-agent system inherits the safety property of the ARC chain: every constraint conflict is resolved deterministically by the orchestrator, regardless of the LLM output. Evaluated on a dairy-barn ventilation case over a 4-day mixed-season scenario, Qwen 2.5 7B Instruct operator agents running offline on a 24 GB consumer GPU at a 5-minute cadence produce auditable trajectories, each paired with an operator-voice rationale that supports a control campaign logbook.

</details>


### 109. A Role-Based Multi-Agent Model for Climate Adaptation Deliberation Across Living Labs

- **Authors:** Önder Gürcan, David Eric John Herbert, F. LeRon Shultz, Christopher Frantz, Ivan Puga-Gonzalez
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00046v1](http://arxiv.org/abs/2607.00046v1)
- **PDF:** [https://arxiv.org/pdf/2607.00046v1](https://arxiv.org/pdf/2607.00046v1)
- **Categories:** cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Climate governance processes involve complex interactions between heterogeneous citizens, advocacy groups, media actors, and political decision-makers. While agent-based models (ABMs) have been widely used to study environmental policy and socio-ecological systems, many existing approaches focus either on institutional dynamics or individual behavioural mechanisms in isolation. This paper presents a modular multi-level agent-based architecture that integrates empirically grounded cognitive decision models with strategic institutional behaviour within a unified simulation framework. The architecture combines (i) motive-based individual decision-making operationalised through the HUMAT and MOA frameworks, (ii) socially embedded influence processes via demographic homophily networks, and (iii) institutional strategy modules for environmental non-governmental organisations (NGOs), media agents, and politicians. Political decisions emerge from the aggregation of multiple signals, including expert input, public mobilisation, party alignment, and media framing. The model is designed to be empirically calibrated through synthetic populations derived from survey data and and institutional parameters informed through Living Lab stakeholder engagement, and to support scenario-based exploration of climate-relevant land-use governance processes. Rather than presenting empirical results, this paper focuses on the architectural design principles, modular structure, and integration logic of the model. We discuss how this multi-layered approach contributes to the modelling of democratic climate governance and outline pathways for generalization and future validation.

</details>


### 110. Contrastive Reflection for Iterative Prompt Optimization

- **Authors:** Derek Koh, Jinghui Mo, Benjamin H. Le, Jiening Zhan, Baofen Zheng, Kevin Bevis, Nathaniel C. Owen, Lauren Elizabeth Charney, Wenqiong Liu, Jingwei Wu
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30840v1](http://arxiv.org/abs/2606.30840v1)
- **PDF:** [https://arxiv.org/pdf/2606.30840v1](https://arxiv.org/pdf/2606.30840v1)
- **Categories:** cs.AI


> The paper introduces **Contrastive Reflection**, an iterative prompt‑optimization loop that treats LLM‑based retrieval agents as debuggable systems: it extracts structured retrieval/reasoning traces and dimension‑level scores, isolates error‑anchored “behavioral slices”, enriches them with nearby successful examples, and then asks a teacher LLM to suggest targeted prompt edits that are accepted only after held‑out validation (with optional regression checks). Applied to a HotpotQA retrieval‑augmented QA benchmark, a single contrastive repair raised exact‑match accuracy from 51.4 % to 60.4 %, outperforming random‑evidence or failure‑only baselines and approaching the performance of state‑of‑the‑art prompt optimizers such as MIPROv2 (59.4 %). The contribution is a contrastive, trace‑driven, validation‑centric workflow that makes prompt repair for agentic IR systems more interpretable, systematic, and performance‑driven.


<details>
<summary>Abstract</summary>

LLM agents are becoming central to information retrieval: they issue retrieval queries, synthesize answers, and increasingly serve as judges for IR evaluation. Improving the prompts that control these agents is an optimization problem, but in applied IR settings it often looks less like blind search and more like debugging. Engineers need to know which behavior failed, which nearby behavior still worked, what distinguishes the two, and whether a prompt edit improves held-out quality without introducing regressions.
  We present Contrastive Reflection, an iterative prompt-optimization framework for agentic IR workflows. The framework starts from a task-centric quality definition: QA agents expose retrieval or reasoning traces, and grading agents expose dimension-level scores and rationales. These structured traces are used to identify error-anchored behavioral slices, add nearby successful examples from the same region, and ask a Teacher LLM to propose a targeted prompt edit. Candidate edits are accepted only when validation performance improves, optionally subject to regression checks. We instantiate the framework with a tree-based slice selector, but the contribution is the contrastive reflection loop rather than the tree itself.
  On a public HotpotQA retrieval-augmented QA setup, one tree-selected contrastive repair improves held-out exact-match accuracy from 51.4% to 60.4%. Failure-only and random-evidence variants improve less and break more previously correct examples. A light instruction-only comparison places the method near modern prompt optimizers: MIPROv2 reaches 59.4% and GEPA 57.0%. The result is an interpretable optimization loop for IR agents, aimed at making prompt repair more inspectable and validation-driven.

</details>


### 111. Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale

- **Authors:** Alessandro Morosini, Sarah H. Cen, Andrew Ilyas, Hedi Driss, Aleksander Mądry, Chara Podimata
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30801v1](http://arxiv.org/abs/2606.30801v1)
- **PDF:** [https://arxiv.org/pdf/2606.30801v1](https://arxiv.org/pdf/2606.30801v1)
- **Categories:** cs.CL, cs.CY, cs.LG, cs.SI


> The paper introduces a novel auditing framework that uses generative‑AI agents as realistic “behavioral engines” for synthetic user accounts, allowing researchers to conduct large‑scale, black‑box audits while keeping user behavior constant and systematically manipulating observable attributes (e.g., age, gender, location). By instantiating 1,120 agents with fixed demographic and political personas and deploying them on X after the 2024 U.S. election, the authors collect 200 k+ content exposures and show that X’s recommendation feed disproportionately amplifies toxic, polarizing, and right‑leaning posts, with amplification strongly modulated by ideological persona and demographic counterfactuals—aggregate demographic effects are near zero but subgroup effects are sizable and directionally varied. This work demonstrates that GenAI‑driven agents can provide a scalable, controllable, and causally interpretable tool for auditing personalization algorithms in the agentic AI ecosystem.


<details>
<summary>Abstract</summary>

Personalization algorithms determine what content users encounter on online platforms. Auditing these systems is difficult because independent auditors have only black-box access to the algorithms, while personalization depends on users' attributes, behavior, and evolving interaction histories. Existing auditing methods face a tradeoff: studies with real users capture realistic behavior but are costly and hard to control, whereas sock-puppet audits scale more easily but often rely on scripted behavior that limits realism. Beyond this, both approaches struggle to decouple user attributes from user behavior, limiting our ability to causally understand personalization. To address this gap, we introduce a framework for black-box audits of personalization algorithms using generative AI agents as behavioral engines for synthetic accounts. Each agent is instantiated with a fixed persona, grounded in demographic and political survey data, and interacts with a platform's content by reasoning about it and choosing actions. Because behavior is fixed within each persona while platform-visible signals such as age, gender, or location can be experimentally perturbed, our design enables counterfactual auditing of how platforms respond to user attributes. As a case study, we deploy 1,120 agents on X shortly after the 2024 U.S. election, spanning 14 personas and three counterfactual conditions, collecting over 200,000 content exposures. We find that X's algorithmic feed amplifies toxic, polarizing, political, and right-leaning content relative to the chronological feed, with amplification varying sharply by user ideology. Counterfactual analyses show that demographic signals affect content delivery in persona-dependent ways: pooled effects are largely null, while subgroup-level effects vary in direction and magnitude. Our work establishes GenAI-based agents as a new tool for algorithmic auditing.

</details>


### 112. A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization

- **Authors:** Yangqiaoyu Zhou, Mohammad Alqudah, Kwei-Herng Lai, Aaron Halfaker, Yingqi Xiong, Yaar Harari
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30775v1](http://arxiv.org/abs/2606.30775v1)
- **PDF:** [https://arxiv.org/pdf/2606.30775v1](https://arxiv.org/pdf/2606.30775v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise AI agents route user queries to specialized skills by matching queries against natural language skill descriptions. When two skills share overlapping descriptions, the routing LLM misroutes queries, a failure we term skill collision. As agents scale to dozens of skills, manually tuning descriptions to maintain routing accuracy becomes a significant engineering bottleneck. We deploy an automated description optimization pipeline on a production enterprise group chat agent (9 skills, 372 regression cases). The pipeline produces descriptions averaging 79.2% F1, matching manually tuned descriptions at 79.4% F1 (average per-skill difference -0.20%, within the 0.78% multi-seed noise floor), while reducing per-skill engineering effort from 120 minutes to 3.8 minutes (32 times speedup). We then examine which pipeline components actually drive this match. Systematic ablation on both the production system and ToolBench (16k tools) reveals that a single LLM rewrite using any available false-positive and false-negative cases captures most of the available improvement. Other design choices we tested (iteration budget, feedback signal composition, dual editing of confused pairs, and training set size) each affect final F1 by less than 0.5%. Description optimization addresses skill collisions caused by overlapping descriptions but cannot resolve cases where two skills intended scopes genuinely overlap. We identify a diagnostic (a large train-validation F1 gap) that flags the latter cases for architectural rather than text-level intervention.

</details>


### 113. Understanding and Evaluating Claw-like Agent Security Through a Computer-Systems Lens

- **Authors:** Peizhi Niu, Wenjie Qu, Shangding Gu, Tianneng Shi, Yuankai Li, Ahmad Tawaha, Hend Alzahrani, Vincent Siu, Boyi Li, Chenguang Wang, Jiaheng Zhang, Basel Alomair, Ming Jin, Muhao Chen, Chi Wang, Costas Spanos, Dawn Song
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30755v1](http://arxiv.org/abs/2606.30755v1)
- **PDF:** [https://arxiv.org/pdf/2606.30755v1](https://arxiv.org/pdf/2606.30755v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **SafeClawArena**, the first systematic benchmark for “claw‑like” always‑on AI agents that treats such agents as full‑stack computer systems—mapping their gateway runtime to an OS, Skills to installed applications, and Plugins to loadable extensions—and evaluates security across four attack surfaces (supply‑chain integrity, persistent‑state exploitation, cross‑boundary data flow, and indirect prompt injection). Using containerized replicas of three real‑world platforms (OpenClaw, NemoClaw, SeClaw) and five leading LLMs, the authors generate 406 adversarial tasks and automatically track credential taint across nine output channels, finding attack success rates as high as 70 % (100 % for malicious Plugins) and showing that only modest architectural changes in SeClaw reduce GPT‑5.4’s success rate to 22 %, while Claude‑Opus‑4.6 already caps attacks near that floor. The work reveals that current claw‑agent designs lack the mature protection mechanisms of traditional operating systems and provides a concrete evaluation suite to guide future hardening of agentic AI systems.


<details>
<summary>Abstract</summary>

Claw-like AI agents (e.g., OpenClaw) are always-on processes with persistent access to credentials, files, tools, and external services. They take on system-level responsibilities -- installing packages, maintaining state, scheduling subtasks, and mediating I/O -- making security failures far more severe than in other agents. Yet existing benchmarks focus on model responses and tool calls, leaving cross-component failure modes largely unmeasured. We adopt a computer-system analogy: treating a Claw-like agent as an agentic computer system whose gateway runtime plays an OS-like mediation role, whose Skills resemble user-installed applications, and whose Plugins resemble loadable extensions with runtime privileges. Each component has a classical counterpart whose protection mechanisms -- refined over decades of cybersecurity research -- are absent on the agent side. From this perspective, we develop SafeClawArena, a benchmark of 406 adversarial tasks across four attack surfaces (Skill Supply-Chain Integrity, Persistent State Exploitation, Cross-Boundary Data Flow, and Indirect Prompt Injection), executed in containerized replicas of real agent platforms with canary-marked credentials and evaluated via automated taint tracking across nine output channels. We evaluate three platforms (OpenClaw, NemoClaw, SeClaw) and five frontier LLMs. The highest attack success rate reaches 70%; malicious Plugins succeed in 100% of cases regardless of the LLM. SeClaw cuts GPT-5.4's attack success rate from 70% to 22%, partly through utility-security tradeoffs rather than active defenses, while Claude-Opus-4.6 already sits near a 22% floor on every platform. These results expose the inadequacy of current defenses and suggest directions for future hardening. Code and data: https://github.com/sunblaze-ucb/SafeClawArena.

</details>


### 114. Self-Evolving World Models for LLM Agent Planning

- **Authors:** Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, Yang Deng
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30639v1](http://arxiv.org/abs/2606.30639v1)
- **PDF:** [https://arxiv.org/pdf/2606.30639v1](https://arxiv.org/pdf/2606.30639v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution:** The paper introduces **WorldEvolver**, a test‑time framework that improves the foresight of frozen LLM planners by dynamically revising the world‑model context rather than altering the underlying model parameters.

**Methodology:** WorldEvolver augments a deployed world model with three interacting modules: (1) an **Episodic Memory** that retrieves and re‑simulates real past action‑outcome transitions, (2) a **Semantic Memory** that distills stable heuristic rules from systematic prediction‑observation mismatches, and (3) a **Selective Foresight** filter that excludes low‑confidence predictions before they are injected into the LLM agent’s reasoning context.

**Key findings:** Across ALFWorld and ScienceWorld benchmarks, WorldEvolver yields the highest prediction accuracy for three different world‑model backbones and translates this fidelity into a statistically significant boost in downstream agent success rates on the AgentBoard suite, demonstrating that test‑time memory‑based revision can reliably enhance planning performance of agentic LLM systems.


<details>
<summary>Abstract</summary>

World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits real action transitions through retrieval-based simulation; (ii) Semantic Memory, which extracts persistent heuristic rules from prediction-observation mismatches; and (iii) Selective Foresight, which filters low-confidence predictions before integrating them into agent reasoning context. We evaluate WorldEvolver on ALFWorld and ScienceWorld, measuring world model prediction accuracy on Word2World and downstream agent success rate on AgentBoard. Extensive experiments show that WorldEvolver achieves the highest prediction accuracy across three backbones and leads other world model baselines on downstream agent success rate, demonstrating that test-time memory revision enhances both predictive fidelity and planning performance.

</details>


### 115. MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems

- **Authors:** Kunyang Li, Kyle Domico, Jonathan Gregory, Patrick McDaniel
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30602v1](http://arxiv.org/abs/2606.30602v1)
- **PDF:** [https://arxiv.org/pdf/2606.30602v1](https://arxiv.org/pdf/2606.30602v1)
- **Categories:** cs.CR, cs.AI


> **Contribution**  
The paper presents **MESA**, a label‑free framework that ranks communication edges in multi‑agent systems (MAS) by their security criticality, enabling defenders to focus limited hardening resources on the most exploitable channels before any attack is seen.

**Methodology**  
MESA fuses six static graph‑theoretic measures (e.g., betweenness, eigenvector centrality) with two dynamic probes—edge ablation and masking—to estimate how much the system’s overall decision would change if a given edge were compromised. The ranking requires no prior attack data. The authors validate MESA using a misinformation‑injection attack pipeline across three MAS domains, eight network topologies, and five open‑source large language models (Qwen, Llama, Gemma), comparing the predicted rankings to empirical per‑edge attack success rates.

**Key Findings**  
MESA’s rankings exhibit a strong correlation with actual attack success (mean Spearman ρ = 0.60, up to 0.73). Allocating defensive monitoring to the top 10 % of MESA‑ranked edges captures roughly three times more successful attacks than random allocation, demonstrating that vulnerability is highly concentrated and can be predicted without attack traces. The study also delineates the framework’s limits under adaptive adversaries and highly redundant communication graphs, underscoring its practical utility for proactive security in agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) are increasingly used to automate complex, distributed workflows. However, their inter-agent communication channels introduce new attack surfaces that remain poorly understood and are difficult to defend against. In this paper, we address how defenders should prioritize limited security effort to protect vulnerable communication channels before attacks are observed. This is motivated by our observation that the channel-level attack impact is highly non-uniform: a single compromised edge can account for up to 75% of total attack success. We introduce Mesa, a label-free framework for proactively ranking which MAS edges are most security-critical -- that is, most likely to affect the system's decision if compromised. Mesa combines six graph-theoretic metrics and two dynamic probes (ablation and masking) without requiring attack traces. We evaluate Mesa against a dynamic misinformation attack pipeline across three diverse MAS scenarios, eight network topologies, and five open-source LLMs from Qwen, Llama, and Gemma families. Mesa rankings correlate strongly with empirical per-edge attack success rate, achieving mean Spearman $ρ=+0.60$ (peaking at $+0.73$). In resource-constrained defense deployment, monitoring the top 10% of Mesa-ranked edges intercepts about 3x the successful attacks as random allocation. We further test Mesa under varying attacker and defender models and LangGraph workflows and characterize its limits under adaptive attacks and high-redundancy graphs. Overall, our results show that edge-level risk in MAS is often concentrated and predictable, allowing proactive hardening of multi-agent infrastructures.

</details>


### 116. Attractor States Emerge in Multi-Turn LLM Conversations

- **Authors:** Ting-Wen Ko, Jonas Geiping
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30571v1](http://arxiv.org/abs/2606.30571v1)
- **PDF:** [https://arxiv.org/pdf/2606.30571v1](https://arxiv.org/pdf/2606.30571v1)
- **Categories:** cs.LG, cs.CL


> The paper shows that open‑ended, multi‑turn dialogues between large language models tend to converge on **model‑specific attractor states**—stable patterns of discourse that persist regardless of topic. By running extensive self‑play and mixed‑play debates across seven LLMs and 20 controversial subjects, the authors map conversation trajectories in latent representation space and measure discourse traits and stance shifts, revealing that certain models (e.g., Claude Haiku) act as strong attractors that pull partners toward their stylistic and argumentative habits, while others (e.g., GPT‑4.1 nano) are highly susceptible to influence. These findings suggest that the long‑term dynamics of autonomous agentic AI systems can be partially predicted and guided by understanding such attractor dynamics, offering a framework for designing, monitoring, and controlling multi‑agent LLM interactions.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used in open-ended multi-agent settings, but the long-run dynamics of model--model interaction remain poorly understood. We study whether open-ended LLM discussions exhibit attractor-like behavior, i.e. topic-independent stable sets of behaviors which conversations settle into. Across 7 LLMs and 20 controversial topics, we compare self-play and mixed-play dyadic debates, tracking trajectories in representation space, discourse traits, and stances. We find self-play trajectories to be model-specific attractors that draw their conversation partners asymmetrically in mixed-play debates, influencing the other models' stylistic choices and behavior. For example, Claude Haiku is a strong attractor of other models in latent space, corresponding to other models taking on its traits like metacommentary, and models like GPT-4.1 nano are especially malleable. Our results suggest that open-ended LLM interactions are partially predictable from model-specific attractors, but shaped by structured and asymmetric partner influence. Overall, our analysis sheds some light on the complex behavior of open-ended multi-agent interaction, which we hope is helpful in designing, predicting, and monitoring autonomous agentic systems in the real world.

</details>


### 117. Forensic Trajectory Signatures for Agent Memory Poisoning Detection

- **Authors:** Jun Wen Leong
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30566v1](http://arxiv.org/abs/2606.30566v1)
- **PDF:** [https://arxiv.org/pdf/2606.30566v1](https://arxiv.org/pdf/2606.30566v1)
- **Categories:** cs.CR, cs.LG


> **Contribution:** The paper identifies a robust, overdetermined behavioral invariant—*the “memory‑recall‑before‑email‑send” transition*—that reliably signals persistent memory‑poisoning attacks on LLM agents that access external memory via tool calls, and demonstrates that this invariant can be used as a forensic signature for detection and mitigation.

**Methodology:** Leveraging logs of tool‑call trajectories, the authors first isolate the invariant as a simple rule, then train a Random Forest on 19 trajectory features (including recall‑related and unrelated cues) and evaluate it with bootstrap‑adjusted AUC on 10 k resamples. They conduct ablations (removing recall features), cross‑model hold‑out tests on 9 models (7 B–120 B parameters), and verify transfer to frontier models (GPT‑4.1, GPT‑4o) as well as a prefix‑only real‑time variant.

**Key Findings:** The invariant alone yields AUC = 0.9563; the full classifier reaches AUC = 0.9904 (95 % BCa CI [0.987, 0.993]). The signature remains intact after removing half the features, confirming a distributed “trajectory signature.” Cross‑model hold‑outs achieve perfect AUC = 1.0 on six of nine splits, and the pattern generalizes to GPT‑4 variants without retraining. A prefix‑only detector still attains AUC ≈ 0.93, indicating feasible real‑time blocking, and the method can differentiate memory‑channel poisoning from prompt‑injection attacks using tool‑call logs alone.


<details>
<summary>Abstract</summary>

We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require calling memory_recall_fact before email_send_email, a transition that non-exfiltrating sessions rarely exhibit. Under the evaluated architecture, this invariant follows from the attack's information-retrieval dependency rather than being merely an empirical correlation, and suppressing it breaks the attack. A simple rule exploiting this invariant alone achieves AUC = 0.9563. A Random Forest classifier over 19 trajectory features refines it to AUC = 0.9904 (BCa 95% CI [0.987, 0.993], N=10,000 resamples), demonstrating that the attack imprints on multiple independent behavioral channels. The signature is overdetermined: removing all recall-related features (half the feature set) leaves AUC unchanged at 0.990, confirming that memory poisoning induces a distributed trajectory signature rather than a single observable anomaly. Cross-model hold-out on 9 models (7B-120B parameters) confirms AUC = 1.000 on 6/9 hold-out splits, with all three exceptions mechanistically explained. The invariant generalizes to frontier models (GPT-4.1, GPT-4o) without retraining. A strictly prefix-only variant achieves AUC = 0.934, suggesting that real-time blocking is feasible with moderate degradation. The boundary is forensically useful: prompt-injection attacks that bypass memory produce a distinct trajectory (score = 0.541), enabling incident responders to distinguish memory-channel attacks from prompt-injection attacks using tool-call logs alone.

</details>


### 118. Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing

- **Authors:** Dvir Alsheich, Adar Peleg, Ben Hagag, Rom Himelstein, Amit Levi, Avi Mendelson
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30555v1](http://arxiv.org/abs/2606.30555v1)
- **PDF:** [https://arxiv.org/pdf/2606.30555v1](https://arxiv.org/pdf/2606.30555v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid integration of Large Language Models (LLMs) has driven the evolution of Multi-Agent Systems (MAS), where specialized agents collaborate to execute complex workflows. Effective orchestration in these environments requires robust routing mechanisms to efficiently allocate tasks to the most suitable agent. However, existing routers fundamentally rely on unverified proxies, ranging from textual self-descriptions to static surrogate representations, to gauge an agent's competence. This reliance on non-empirical data creates a critical gap between an agent's projected profile and its actual operational capabilities, introducing severe security vulnerabilities. Malicious agents can easily misrepresent their proficiencies or harbor covert backdoors that evade both standard external analysis and static representation-learning techniques. In this work, we introduce ANTAP (Automatic Non-Textual Agent Picker), an evaluation-driven routing architecture that discards indirect proxies in favor of active capability testing. By dynamically querying agents to ascertain their true competencies empirically, ANTAP distills performance into fixed behavioral operators within a shared semantic space. At inference time, routing is performed via a purely non-textual algebraic projection, establishing a "linguistic firewall" that renders metadata-based attacks inexpressible. In our experiments, ANTAP achieves near-zero ASR against description-based injection attacks, compared to 67.3\% and above for the description-based router baseline. Against adaptive embedding attacks, ANTAP achieves substantially lower ASR than the embedding-based baseline, with a 20\% reduction, while remaining resilient to description manipulation by design.

</details>


### 119. MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems

- **Authors:** Jordan Augé, Giovanna Carofiglio, Giulio Grassi, Jacques Samain
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30546v1](http://arxiv.org/abs/2606.30546v1)
- **PDF:** [https://arxiv.org/pdf/2606.30546v1](https://arxiv.org/pdf/2606.30546v1)
- **Categories:** cs.MA


> **Main contribution:** The paper presents **MAS‑Lab**, a three‑layer, specification‑driven framework that turns ad‑hoc collections of LLM‑based agents into engineered, production‑ready multi‑agent systems by separating what the system should do (the declarative specification) from how it is executed and managed.  

**Methodology:** MAS‑Lab defines a **declarative, framework‑agnostic specification layer (Spec)** that captures the semantic intent of agents and their orchestration, a **stateful MAS Operating System (MAS‑OS)** that supplies generic execution, control, and lifecycle primitives, and a set of **lab overlays** that inject observability, reproducible experimentation, and evaluation tooling. The authors instantiate the stack on existing LLM‑agent toolkits and demonstrate how intent‑based validation checks can be written once and applied throughout development, testing, and deployment.  

**Key findings:** Experiments show that MAS‑Lab enables **systematic validation of MAS properties (e.g., safety constraints, goal convergence, and coordination protocols)** with far higher reproducibility than traditional script‑centric pipelines, and that the same specifications can be ported directly to a production environment with minimal re‑engineering. This validates the framework’s claim that specification‑driven development markedly improves reliability, evolvability, and governability of agentic AI systems.


<details>
<summary>Abstract</summary>

The rapid emergence of LLM-based agentic frameworks has significantly reduced the cost of assembling multi-agent systems (MAS), enabling fast prototyping and exploration of agentic behaviors. However, systems built with current tooling remain ill-suited for reliable, evolvable, and production-grade deployment. In practice, MAS are often developed in an ad-hoc and imperative manner, with agent logic, orchestration, observability, and control tightly interwoven, little to no explicit system-level validation, and development workflows optimized for demonstrations rather than long-lived, governed operation. As a result, behavior observed during experimentation rarely constitutes reliable evidence of behavior in production.
  In this paper, we introduce MAS-Lab, a specification-driven framework for principled development and experimental validation of multi-agent systems properties. MAS-Lab is designed to transform MAS from collections of scripts into engineered distributed systems by separating semantic intent from operational concerns, making behavior and control explicit, supporting reproducible experimentation, and preserving continuity across lifecycle stages. MAS-Lab consists of three layers: a declarative, framework-agnostic agentic specification layer (Spec); a stateful MAS Operating System that provides execution and control primitives plugged-in by design (MAS-OS); and a set of lab overlays with integrated observability and evaluation tools (Labs). Together, these components enable intent-based validation, principled system evolution, and a seamless transition to production-grade MAS.

</details>


### 120. TRACE: Temporal Relationship-Aware Conversational Entrainment Detection in Dyadic Speech

- **Authors:** Sathvik Manikantan Napa Ugandhar, Hao Zhang, Alison Gunzler, Yuzhe Wang, Thomas Thebaud, Georgi Tinchev, Venkatesh Ravichandran, Laureano Moro-Velázquez
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30543v1](http://arxiv.org/abs/2606.30543v1)
- **PDF:** [https://arxiv.org/pdf/2606.30543v1](https://arxiv.org/pdf/2606.30543v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **DyadEE**, a novel dataset of dyadic speech recordings annotated for emotional entrainment, together with synthetic variants where entrainment is deliberately broken via partner‑swapping and emotion‑resynthesis. Building on this resource, the authors propose **TRACE**, a temporal‑relationship‑aware framework that encodes each speaker’s acoustic signal as a sequence of Whisper‑derived emotion embeddings and processes these ordered “interaction traces” with a window‑level model rather than aggregating utterances. Experiments on DyadEE demonstrate that leveraging fine‑grained conversational context and dyadic relationship cues markedly improves detection of emotional entrainment, with TRACE reaching 97.01 % accuracy—setting a new state‑of‑the‑art for agentic AI systems that must recognize and adapt to affective coordination in real‑time dialogue.


<details>
<summary>Abstract</summary>

With the proliferation of speech AI agents, understanding emotional entrainment in conversational interaction has become increasingly important. Emotional entrainment is shaped by social relationships and conversational context, influencing affective coordination over time. We introduce DyadEE, a dataset for emotional entrainment detection in dyadic speech interactions, containing both emotionally entrained conversations and synthetic interactions where entrainment is disrupted through partner swapping and emotion resynthesis. We further propose TRACE, a window-level framework that models dyadic interaction as ordered sequences of acoustic embeddings derived from emotion fine-tuned Whisper representations, treating each sample as an interaction trace rather than pooled utterances. Experimental results on DyadEE show that incorporating conversational context and relationship information improves emotional entrainment detection, with TRACE achieving the best accuracy of 97.01%.

</details>


### 121. Entity Binding Failures in Tool-Augmented Agents

- **Authors:** Rahul Suresh Babu, Shashank Indukuri
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30531v1](http://arxiv.org/abs/2606.30531v1)
- **PDF:** [https://arxiv.org/pdf/2606.30531v1](https://arxiv.org/pdf/2606.30531v1)
- **Categories:** cs.AI


> **Main contribution** – The paper identifies and formalizes *entity‑binding failures* as a separate reliability and safety issue for tool‑augmented language‑model agents, showing that an agent can select the correct tool yet act on the wrong real‑world entity (e.g., contacting the wrong “Alex”).  

**Methodology** – The authors develop a taxonomy of wrong‑entity errors in enterprise workflows and test a suite of *entity‑aware* execution mechanisms (entity‑resolution preconditions, confidence‑gated binding, ambiguity‑driven clarification prompts, and provenance tracking) against standard action‑oriented baselines across 60 tasks, five LLM back‑ends, and six tool‑use strategies.  

**Key findings** – While all systems achieved 0 % wrong‑tool errors, baseline agents still performed wrong‑entity actions in roughly 24‑26 % of runs. The entity‑aware methods eliminated these errors and reduced risk‑weighted exposure, albeit at the cost of deferred execution when ambiguity remained. This demonstrates that safe tool use in agentic AI requires not only correct tool selection but also robust binding of natural‑language references to the intended external entities.


<details>
<summary>Abstract</summary>

Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task. However, an agent may choose the right tool and still act on the wrong external entity. For example, a request to "email Alex about the launch" may lead the agent to contact the wrong Alex, attach the wrong launch document, reply in the wrong thread, or update the wrong customer account. We call these errors entity binding failures. This paper studies entity binding failures as a distinct reliability and safety problem in tool-augmented agents. We formalize the separation between tool correctness and entity correctness, introduce a taxonomy of wrong-entity failures in enterprise workflows, and evaluate entity-aware execution mechanisms including entity-resolution preconditions, confidence-gated binding, clarification under ambiguity, and provenance tracking. In a controlled diagnostic evaluation across 60 tasks, five model backends, and six tool-use methods, all methods achieved 0.0 percent wrong-tool error, yet action-oriented baselines still produced wrong-entity actions in 24.0-26.0 percent of runs. Entity-aware methods eliminated wrong-entity actions and risk-weighted wrong-entity exposure in this setting, but reduced direct task completion by deferring under ambiguity. These findings show that safe tool use requires not only selecting the correct tool, but also reliably binding natural-language references to the correct real-world entity before action.

</details>


### 122. ATM: CID-Brokered Pre-Write Admission for Multi-Agent Code Co-Synthesis

- **Authors:** Eagl Huang
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.00041v1](http://arxiv.org/abs/2607.00041v1)
- **PDF:** [https://arxiv.org/pdf/2607.00041v1](https://arxiv.org/pdf/2607.00041v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems can decompose software-engineering work into planning, generation, validation, and repair, but a narrower systems problem remains: before any governed shared mutation is applied, a system must decide which concurrently formed write intents may proceed in parallel, which require deterministic composition or serialization, and which must take a fail-closed path. We address this problem with the AI-Atomic-Framework (ATM), a specification-grounded governance substrate for software agents operating within a single governance domain.
  ATM binds task intent, repository scope, write admission, validation, and evidence obligations into one governance chain. A Content Identifier (CID) broker serves as the shared-mutation admission subsystem. Adapter-guided atomization maps write intents to semantic atoms and bounded regions; when persistent atom-map coverage is incomplete, virtual atoms provide temporary auditable governance units for conservative comparison and routing. Governed shared writes are ultimately applied by a neutral steward rather than directly by proposing agents.
  Evaluation combines controlled, field, adoption, and extension evidence, including a 12-scenario deterministic design matrix, three archived runner cases, ATM-AdmissionBench, three archived same-file boundary cases, a three-week external-adopter study, and an operational recovery-routing benchmark. The results support feasibility, auditability, and bounded recoverability within the observed single-domain settings, but do not claim broad comparative superiority or cross-clone governance.

</details>


### 123. COHORT: Collaborative Orchestration for Hardening via Offensive Replay on Emulated Topologies

- **Authors:** Chen Frydman, Aviram Zilberman, Rubin Krief, Abed Showgan, Andres Murillo, Sekiya Motoyoshi, Asaf Shabtai, Yuval Elovici, Rami Puzis
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30479v1](http://arxiv.org/abs/2606.30479v1)
- **PDF:** [https://arxiv.org/pdf/2606.30479v1](https://arxiv.org/pdf/2606.30479v1)
- **Categories:** cs.NI, cs.AI, cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mitigating an observed adversary in an enterprise network typically takes weeks of expert work: an analyst derives a mitigation tailored to that adversary, validates it without breaking production, and verifies it disrupts the specific attack. The procedure relies on expert judgment and cannot safely be exercised against the production network. COHORT is the first end-to-end framework to automate this procedure for deployable mitigations. A role-decomposed multi-agent LLM workflow proposes candidates, implements them as real device commands, and refines them through a critique loop, all on a high-fidelity GNS3 emulator running real vendor firmware (firewall, switch, router). Each candidate is evaluated by offensive replay: re-executing the original adversary on the mitigated network for a paired comparison against the unmitigated baseline, rather than the reward-signal or expert-judgment proxies used in prior simulation, hybrid, and configuration-generation work. Two further checks complement replay: a connectivity-regression check (LAN ping and internet HTTP probe) rejects mitigations that disrupt legitimate LAN or internet connectivity, and a cumulative evaluation stacks approved mitigations onto a persistent state to surface compound effects. Across three topologies and four attack scenarios (ransomware, lateral movement, DNS exfiltration, data theft), 46.7% of generated mitigations both disrupt the attack and preserve connectivity under replay, 4.4 times the rate of a single-agent baseline using the same model and tool access. A demo video walking through the framework is available with our released artifacts.

</details>


### 124. Collective cooperation without individual fidelity in LLM agents

- **Authors:** Henrique Ferraz de Arruda, Carlos Gracia Lázaro, Alberto Aleta, Yamir Moreno
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30454v1](http://arxiv.org/abs/2606.30454v1)
- **PDF:** [https://arxiv.org/pdf/2606.30454v1](https://arxiv.org/pdf/2606.30454v1)
- **Categories:** physics.soc-ph, cs.AI


> **Main contribution:** The paper evaluates whether large‑language‑model (LLM) agents can serve as faithful proxies for human decision‑making by directly comparing them to a large‑scale, networked Prisoner’s Dilemma experiment with real participants.

**Methodology:** Nine open‑weight LLMs were instantiated as agents and run on the exact interaction protocol, payoff matrix, and network topologies used in the human study. The authors analysed both aggregate cooperation trajectories and fine‑grained individual‑level statistics (heterogeneity, conditional cooperation rules), and also tested the effect of mixing in random agents.

**Key findings:** LLM populations reproduce several macro‑level patterns (early drop and later stabilization of cooperation) but systematically miss micro‑level features: they underestimate individual variability and generate conditional cooperation rules that differ from humans. Introducing random agents mitigates some discrepancies but does not eliminate the mismatch, revealing a macro‑micro dissociation—collective outcomes can look human‑like while the underlying decision mechanisms are not. This highlights the need for multi‑scale validation when using LLMs as agentic surrogates in social‑simulation research.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used as agents in simulations of social systems, yet it remains unclear when their behavior can be interpreted as a faithful proxy for human decision-making. Here we test LLM agents against a direct empirical benchmark: a large-scale networked Prisoner's Dilemma experiment with human participants. Using the same interaction protocol, payoff structure, and network topologies, we compare nine open-weight LLMs with the human data. The selected model reproduces several macro-level features of cooperation dynamics, including the early decline and later stabilization of cooperation. This aggregate agreement, however, does not extend uniformly to finer levels of behavior. LLM populations underestimate individual-level heterogeneity and generate conditional cooperation patterns that differ from those observed in humans. Adding a fraction of random agents improves some aspects of micro-level agreement, but does not remove the mismatch in decision rules. These findings reveal a macro--micro dissociation in LLM-based social agents: collective outcomes can appear human-like even when the underlying behavioral distributions and mechanisms are not. They suggest that validating LLM agents as human surrogates requires comparisons across aggregate dynamics, individual heterogeneity, and context-dependent decision rules, rather than outcome-level agreement alone.

</details>


### 125. Minimal MMAO: A Resource-Closed-Loop Framework for Adaptive Metaheuristic Search

- **Authors:** Jinliang Xu, Liping Ma
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30450v1](http://arxiv.org/abs/2606.30450v1)
- **PDF:** [https://arxiv.org/pdf/2606.30450v1](https://arxiv.org/pdf/2606.30450v1)
- **Categories:** cs.NE, cs.MA


> **Main contribution:** The paper introduces **Minimal MMAO**, a compact, resource‑closed‑loop metaheuristic in which a shared “metabolic” controller governs search intensity, exploration‑exploitation balance, and agent lifecycles through endogenous energy circulation, rather than relying on externally preset schedules.

**Methodology:** The authors formalize the framework with bounded private energy, a communal budget, normalized rewards, continuous role adaptation, and resource‑financed branching/pruning. They instantiate the method for both continuous problems (Sphere, Rastrigin) and discrete combinatorial problems (synthetic Euclidean TSP and two TSPLIB instances), keeping the implementation deliberately minimal.

**Key findings:** Across all test domains the same metabolic loop successfully drives adaptive behavior; the discrete version remains stable with a very compact design, while the continuous version incurs higher refinement cost but still achieves competitive solution quality. These results demonstrate that an endogenous, closed‑loop resource model can serve as a unifying, agent‑centric backbone for adaptive metaheuristic search.


<details>
<summary>Abstract</summary>

This paper presents the Metabolic Multi-Agent Optimizer (MMAO) as an adaptive metaheuristic built around endogenous resource circulation. The central premise is that search intensity, exploration--exploitation balance, and lifecycle turnover should be induced by a shared metabolic controller rather than by separately attached schedules. We formulate MMAO through bounded private energy, a communal budget, normalized reward, continuous role adaptation, and resource-financed branching and pruning. The method is then instantiated in both continuous and discrete domains and evaluated on a matched small-scale suite including Sphere, Rastrigin, a synthetic Euclidean TSP, and two TSPLIB instances. The results show a consistent pattern: the same metabolic loop remains workable across domains, the discrete realization remains relatively stable under a compact design, and continuous refinement quality is the main cost of keeping the method lean. Taken together, these findings position MMAO as a coherent framework for adaptive heuristic design rather than a loose collection of operators.

</details>


### 126. Translating Natural Language to Strategic Temporal Specifications via LLMs

- **Authors:** Marco Aruta, Francesco Improta, Vadim Malvone, Aniello Murano, Vladana Perlić
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30441v2](http://arxiv.org/abs/2606.30441v2)
- **PDF:** [https://arxiv.org/pdf/2606.30441v2](https://arxiv.org/pdf/2606.30441v2)
- **Categories:** cs.MA, cs.AI


> The paper introduces the first systematic pipeline for converting natural‑language descriptions of multi‑agent strategic requirements into formal ATL/ATL* specifications using large language models (LLMs). Because no supervised corpus existed, the authors built an expert‑validated NL‑to‑ATL/ATL* dataset and fine‑tuned 3–7 B‑parameter open‑weight LLMs, showing that these models achieve 0.84 semantic accuracy on a held‑out test set—statistically indistinguishable from the 0.86 accuracy of strong few‑shot proprietary APIs—while running on‑premises. Moreover, the authors demonstrate practical utility by integrating the translator with a strategic‑logic model checker, enabling non‑expert users to express and verify strategic temporal properties directly from natural language.


<details>
<summary>Abstract</summary>

A rigorous formalization of system requirements is a fundamental prerequisite for the verification of Multi-Agent Systems (MAS). However, writing correct formal specifications is well known as an error-prone, time-consuming, and expertise-intensive task. This difficulty is further accentuated in MAS, where requirements must capture strategic abilities and temporal objectives. At present, there is no established methodology for deriving MAS specifications from natural language. We present a framework for translating Natural Language descriptions of strategic requirements into well-formed ATL/ATL* formulas using Large Language Models (LLMs). Since no available dataset supports supervised learning for the NL-to-ATL/ATL* translation task, we create and curate a novel expert-validated dataset, employed for training and evaluating fine-tuned models. On a held-out test set, evaluated under the LLM judge that best agrees with expert annotations, in-domain fine-tuning of small open-weight models (3 - 7B parameters) matches strong few-shot proprietary API baselines. Our best fine-tuned system reaches 0.84 semantic accuracy, statistically on par with 0.86 for the strongest few-shot proprietary baseline, while keeping requirements on-premises. We further find that judge reliability is inverse to generator strength. The open-weight Llama-3.3-70B tracks human verdicts most closely, whereas the strongest proprietary models are the least reliable judges, over-rejecting faithful paraphrases of the reference. To assess the practical applicability of the generated specifications, we embed our tool to an existing strategic logics model checker, enabling non-expert users to specify strategic properties in natural language.

</details>


### 127. Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents

- **Authors:** Bojie Li, Noah Shi
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30383v1](http://arxiv.org/abs/2606.30383v1)
- **PDF:** [https://arxiv.org/pdf/2606.30383v1](https://arxiv.org/pdf/2606.30383v1)
- **Categories:** cs.AI


> **Contribution**  
The paper defines and empirically studies *multi‑party principal loyalty* for large‑language‑model (LLM) agents that must serve a designated principal while simultaneously interacting with a counter‑party whose interests may conflict. It introduces a benchmark (PrincipalBench) to measure how well agents balance loyalty to the principal against over‑refusal or hidden harm, and it proposes two mitigation mechanisms.

**Methodology**  
PrincipalBench consists of 75 multi‑turn dialogues with embedded “leak probes” (to test whether agents disclose proprietary or confidential information), dual judges (principal‑vs‑counterparty evaluation), and an integrity‑audit gate. The authors evaluate 13 state‑of‑the‑art LLM agents on this benchmark, revealing two failure modes: a *selective* cluster that evades adversarial probes but still obeys legitimate principal requests, and an *over‑refusing* cluster that broadly declines requests. To address these, they (M1) craft a fixed system prompt containing seven prioritized loyalty rules derived from >50 failure analyses, and (M2) develop a per‑token KL‑distillation technique that transfers the prompted behavior from a large Qwen3‑32B teacher into smaller 8B Qwen3 and Llama‑3.1 models.

**Key Findings**  
- Without intervention, harm rates vary dramatically across agents (≤20 % vs. 53.6–75.3 % on PrincipalBench), a discrepancy invisible to single‑turn safety tests.  
- The rule‑based prompt reduces harm to 19.4 % for Claude‑Sonnet and ≤20 % for all nine selective agents, but does not eliminate over‑refusal.  
- KL‑distillation yields the strongest open‑weight transfer of loyalty behavior to smaller models, yet the trade‑off between leaking information and over‑refusing persists; improving one axis invariably worsens the other, indicating a fundamental limitation in current techniques.  

Overall, the work highlights the need for dedicated multi‑party loyalty evaluation and demonstrates that current prompting and distillation methods can mitigate but not fully resolve the loyalty trade‑off in agentic LLM systems.


<details>
<summary>Abstract</summary>

A rapidly growing class of LLM agents is multi-party: the agent acts for a principal (who briefs it, sends follow-ups, and receives results) while also conversing in a separate channel with a counterparty whose interests may diverge (negotiating with a vendor, screening inbound requests, or mediating between employees). Here "help whoever you are talking to" is the wrong objective. The agent must stay loyal to the principal it represents without over-refusing the principal's own cooperative asks. We study this multi-party loyalty problem and contribute a measurement instrument, two mechanisms, and a structural lesson. PrincipalBench is a 75-item multi-turn benchmark with leak probes, dual judges, and an integrity-audit gate. Across 13 frontier subjects it exposes a sharp split (<=20% vs. 53.6-75.3% harm) invisible to single-turn safety evaluations: a selective cluster that declines adversarial probes while still following the principal's legitimate requests, and an over-refusing cluster that refuses broadly. (M1) A prompt-time loyalty scaffold (a fixed system prompt of seven prioritized rules, open-coded from 50+ failure trajectories) holds Claude-Sonnet to 19.4% harm and all nine selective subjects to <=20%. (M2) A per-token-KL distillation recipe transfers a prompted Qwen3-32B teacher into 8B Qwen3 and Llama-3.1 students, the strongest open-weight recipe we measure. (Lesson) Both mechanisms only move along a common leak/over-refusal trade-off rather than crossing it: improving one axis costs the other, and the jointly favorable outcome stays out of reach.

</details>


### 128. Rehearsed Multi-Agent Live Product Demonstrations with Real-Time Voice Question Answering

- **Authors:** Rahul Khedar, Mayank Malhotra, Avinash Karn, Mouli V, Prakhar Mehrotra
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30294v1](http://arxiv.org/abs/2606.30294v1)
- **PDF:** [https://arxiv.org/pdf/2606.30294v1](https://arxiv.org/pdf/2606.30294v1)
- **Categories:** cs.AI, cs.HC, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Live product demonstrations are a recurring, high-cost activity in software organizations: a human presenter must select features, dispatch the corresponding interactions on a running application, narrate them coherently, and answer questions in real time. Existing automation addresses only fragments -- generalist browser agents target instruction-conditioned task completion, and demo-video tools produce fixed MP4 artifacts that cannot be questioned and silently break under interface drift. We propose Rhetor, a multi-agent system that takes a running web application and its source-code repository as input and produces a rehearsed live demonstration with segment-synchronized narration and real-time voice question answering. The architectural contributions are a cross-modal feature representation that merges UI exploration with source-code analysis into features tagged with discrete focus tiers, a grounded scripter constrained to UI elements observed during exploration and dispatched through multi-strategy semantic locators, a pre-presentation rehearsal loop with explicit convergence and graceful degradation to narration-only segments, and a runtime synchronization invariant that ties each browser action to the audio-end event of its narration segment. Across six pipeline sessions on four deployed applications -- including the public-domain whiteboard application Excalidraw -- the rehearser's internal locator-firing rate (sigma-bar) spans 0.31-1.00 over 147 scripted actions; on the substantial workload (53 actions, full tier differentiation), sigma-bar is approximately 0.92, and on the public-domain reference point the locator-repair step drives convergence to sigma-bar = 1.00 at iteration 2. We additionally define a benchmark protocol of ten metrics across six application categories that would establish, beyond the case study, whether each design choice contributes positively.

</details>


### 129. Towards Continual Motion-Language Agents: LoRA Variants for Incremental Motion Understanding and Generation

- **Authors:** Bertram Taetz, Hugo Albuquerque Cosme da Silva, Gabriele Bleser-Taetz
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30266v1](http://arxiv.org/abs/2606.30266v1)
- **PDF:** [https://arxiv.org/pdf/2606.30266v1](https://arxiv.org/pdf/2606.30266v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces a continual‑learning framework for bidirectional motion‑language agents that can keep acquiring new motion concepts (e.g., new athletic styles or gestures) without forgetting previously learned ones. Leveraging a frozen large language model, the authors add low‑rank adaptation (LoRA) modules organized as a mixture‑of‑experts gated by an auto‑encoder router that automatically selects a task‑specific expert at inference time (no explicit task label required); hard expert selection is shown to preserve performance better than soft blending. Experiments on a five‑task benchmark built from HumanML3D reveal near‑zero catastrophic forgetting for both motion‑to‑text and text‑to‑motion tasks while retaining high captioning and generation quality, and they expose a gap between token‑level accuracy and downstream motion quality, underscoring the need for richer evaluation metrics in lifelong motion‑language agents.


<details>
<summary>Abstract</summary>

Motion-language agents must possess the bidirectional capability to both understand human movement (motion-to-text, M2T) and generate it from natural language (text-to-motion, T2M). While foundational models have achieved strong performance in static settings, autonomous agents operating in dynamic environments must continuously incorporate new motion concepts -- such as novel athletic styles or specialized gestures -- without catastrophic forgetting of previously acquired skills. We investigate the stability-plasticity trade-off in bidirectional motion-language learning under sequential task exposure. Building on a frozen large language model backbone, we introduce low-rank adaptation (LoRA) variants designed to mitigate inter-task interference. We specifically propose mixture-of-experts architectures that utilize an autoencoder-based router to select task-specific experts at inference time, so that no task-label is needed. To evaluate these methods, we establish a reproducible five-task benchmark derived from HumanML3D through semantic clustering of motion descriptions. Our experimental results demonstrate near-zero forgetting across both M2T and T2M directions while maintaining high generation and captioning quality. Furthermore, we show that hard expert selection via routing significantly outperforms soft expert blending in quality metrics, indicating that preserving expert isolation is critical for maintaining performance in our continual learning setting. Finally, we observe that a divergence between token-level accuracy and downstream generation quality may occur, highlighting the need for more comprehensive evaluation protocols in future research on lifelong motion-language agents.

</details>


### 130. Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats

- **Authors:** Sebastian Kula, Martin Tamajka
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30259v1](http://arxiv.org/abs/2606.30259v1)
- **PDF:** [https://arxiv.org/pdf/2606.30259v1](https://arxiv.org/pdf/2606.30259v1)
- **Categories:** cs.CL


> The paper introduces a hierarchical, consensus‑driven multi‑agent architecture that coordinates diverse open‑source LLMs (LLaMA, Kimi, Qwen, Deepseek, LLaMA‑Nemotron) to emulate human annotators in detecting and flagging disinformation. By exploiting cognitive and knowledge diversity through a structured voting mechanism, the system outperforms single-model baselines—including GPT‑4/3.5—across multilingual benchmarks (English, Polish, Slovak, Bulgarian) on tasks such as outright disinformation detection, verification‑need identification, and factual‑claim spotting. These results demonstrate that orchestrated ensembles of open LLMs can deliver more reliable, transparent counter‑disinformation capabilities than any individual model, highlighting a scalable pathway for agentic AI defenses against misinformation.


<details>
<summary>Abstract</summary>

In contemporary societies, the threat of disinformation has reached alarming levels, exacerbated by the proliferation of electronic communication, social media, and advancements in artificial intelligence. As a result, there is an urgent need to develop effective countermeasures to mitigate this menace. However, the sheer scale of the problem renders manual fact-checking and human-based verification inadequate, underscoring the necessity for automated methods to detect and debunk disinformation. This article proposes a novel approach based on a multi-agent system that emulates the decision-making processes of human annotators engaged in disinformation detection tasks. By incorporating a consensus mechanism, diversity in cognition and diversity in knowledge, and also hierarchical structure, inspired by human annotators' behavior, the proposed method achieves superior results compared to individual Large Language Models (LLMs), including GPT 4 and GPT 3.5. The system leverages open models (e.g., LLaMA, Kimi, Qwen, Deepseek and LLaMA-Nemotron) to ensure greater transparency. The evaluation of the proposed method encompasses datasets in languages with varying resource availability, including English (high-resource), Polish (medium-resource), Slovak (low-resource) and Bulgarian (low-resource). Experiments were conducted on tasks such as direct disinformation detection, identification of texts worthy of verification, and detection of texts containing verifiable factual claims.

</details>


### 131. Sparse Sensor Placement in Multi-Agent Reinforcement Learning Control of Rayleigh-Bénard Convection

- **Authors:** Jan Stenner, Hans Harder, Sebastian Peitz
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30238v1](http://arxiv.org/abs/2606.30238v1)
- **PDF:** [https://arxiv.org/pdf/2606.30238v1](https://arxiv.org/pdf/2606.30238v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper studies sparse sensor placement for control of Rayleigh-Bénard convection with multi-agent reinforcement learning. We train dense expert policies with windowed observations and distill sparse apprentice policies by supervised learning with grouped regularization on encoder input weights. The framework combines ordered non-convex grouped regularization and iterative reweighted grouped regularization, and uses a grouping construction that enforces consistent pruning across overlapping observation windows. Experiments with fixed and varying initial conditions show that Multi-Agent Transformer policies train more stably than proximal policy optimization baselines, while sparse apprentices retain control behavior comparable to dense experts. Sparsity results are strong for the proposed grouped methods across settings, including maximal sparsity in all fixed-initial-condition setting variants and maximal or near-maximal sparsity in varying-initial-condition setting variants. As an additional proof of concept, training from learned minimal sensor sets reduces per-agent observation size from 360 to 12 and preserves the overall training trend in simulation while reducing data throughput. The results provide both an interpretable basis for identifying control-relevant spatial regions and state components, and a practical pathway toward sensor-efficient control under realistic hardware constraints.

</details>


### 132. DAIN: Dynamic Agent-Based Interaction Network for Efficient and Collaborative Multimodal Reasoning

- **Authors:** Xinxin Chen, Yuchen Li, Zihan Wang, Haoyu Zhang, Ruixin Liu, Mingyuan Zhao
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30189v1](http://arxiv.org/abs/2606.30189v1)
- **PDF:** [https://arxiv.org/pdf/2606.30189v1](https://arxiv.org/pdf/2606.30189v1)
- **Categories:** cs.CL


> The paper introduces **DAIN (Dynamic Agent‑based Interaction Network)**, a novel multimodal‑fusion framework that treats fusion as a collaborative, multi‑agent process rather than a static mixture‑of‑experts. A context‑aware meta‑controller dynamically selects a sparse subset of specialized interaction agents for each input and coordinates compressed inter‑agent communication to reach a consensus, while a multi‑objective loss jointly optimizes task accuracy, agent specialization and efficiency. Experiments on five benchmarks (ADNI, MIMIC‑IV, MM‑IMDB, CMU‑MOSI, ENRICO) show that DAIN sets new state‑of‑the‑art results—e.g., +2.6 % accuracy on ADNI—and ablations confirm that both dynamic scheduling and agent communication are essential, delivering better performance, interpretability, and compute‑efficiency for agentic multimodal reasoning.


<details>
<summary>Abstract</summary>

Current multimodal fusion approaches, particularly those based on static Mixture-of-Experts (MoE) architectures, often struggle to provide the adaptive and efficient collaborative reasoning required by complex real-world applications. We introduce the Dynamic Agent-based Interaction Network (DAIN), which reconceptualizes multimodal fusion as a dynamic, multi-agent collaborative process. DAIN employs a context-aware Meta-Controller that dynamically schedules sparse activation of specialized interaction agents and orchestrates compressed inter-agent communication for consensus-building. The framework is guided by a multi-objective loss function that jointly optimizes task accuracy, agent specialization, and operational efficiency through sparse activation and communication regularization. Comprehensive evaluations across five diverse benchmarks -- ADNI, MIMIC-IV, MM-IMDB, CMU-MOSI, and ENRICO -- establish DAIN as a new state-of-the-art, delivering significant performance improvements including a 2.6\% accuracy gain on ADNI. Ablation studies verify the critical roles of both dynamic scheduling and agent communication. Furthermore, DAIN offers enhanced interpretability by exposing context-dependent agent roles and collaboration patterns while maintaining computational efficiency through sample-wise sparse agent activation. Our work demonstrates the promise of dynamic, agent-based paradigms for multimodal reasoning.

</details>


### 133. MirrorCode: AI can rebuild entire programs from behavior alone

- **Authors:** Tom Adamczewski, David Owen, David Rein, Florian Brand, Giles Edkins, Allen Hart, Daniel O'Connell
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30182v1](http://arxiv.org/abs/2606.30182v1)
- **PDF:** [https://arxiv.org/pdf/2606.30182v1](https://arxiv.org/pdf/2606.30182v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **MirrorCode**, a standardized long‑horizon coding benchmark that requires an AI agent to reconstruct complete software systems from their observable behavior alone, testing exact functional equivalence on held‑out end‑to‑end tests.

**Methodology:** The authors curate 25 diverse target programs (Unix utilities, bioinformatics tools, interpreters, static analysis, cryptography, etc.) and evaluate state‑of‑the‑art code‑generation agents by letting them interact with the binary, generate source code, compile, and iteratively test until the reproduced program matches all reference outputs; large inference budgets (e.g., $2.6 k over 19 days) are allocated for the most demanding tasks.

**Key findings:** The best model attains a 56 % success rate across the suite, demonstrating that current agents can autonomously reimplement substantial codebases (e.g., a 16 k‑line bioinformatics toolkit) with minimal human guidance, but performance still hinges on extensive compute and precise specifications—indicating both the transformative potential and current limits of agentic AI in long‑horizon software engineering.


<details>
<summary>Abstract</summary>

AI models are rapidly improving at autonomous coding, as shown by benchmark progress and one-off demonstrations such as AI implementing a C compiler. However, existing coding benchmarks tend to focus on shorter tasks, and one-off demonstrations are hard to compare systematically because they often have some human guidance, and are not standardized or repeated across models. To address these challenges, we introduce MirrorCode, a long-horizon coding benchmark based on reimplementing entire software projects. In MirrorCode, AI agents must replicate the functionalities of an existing program, without access to its source code. AI solutions must match the original program's output exactly on end-to-end tests, including held-out tests. MirrorCode's 25 target programs span different areas of computing: Unix utilities, data serialization and query tools, bioinformatics, interpreters, static analysis, cryptography, and compression. Existing AI models can already reimplement complex software, with the strongest model scoring 56% across the benchmark. For example, AI can reimplement gotree, a 16,000-line bioinformatics toolkit - a task that we believe would take weeks for a human engineer. However, studying the frontier of performance requires a larger inference budget than typical benchmarks, for example, \$2,600 over 19 days for a single attempt on a large task. We show that AI agents can already complete long-horizon software engineering tasks, especially when requirements are precisely specified. More broadly, our work suggests AI will have transformative effects on software engineering, as autonomous agents continue to improve.

</details>


### 134. ACPO: Agent-Chained Policy Optimization for Multi-Agent Reinforcement Learning

- **Authors:** Daiki E. Matsunaga, Junho Na, Tri Wahyu Guntara, Scott Sanner, Pascal Poupart, Jongmin Lee, Kee-Eung Kim
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30072v1](http://arxiv.org/abs/2606.30072v1)
- **PDF:** [https://arxiv.org/pdf/2606.30072v1](https://arxiv.org/pdf/2606.30072v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces **Agent‑Chained Policy Optimization (ACPO)**, a novel MARL algorithm that achieves an exact decentralized implementation of the joint policy gradient by treating the simultaneous joint action as a serialized sequence in which agents commit one after another, each conditioning on a belief over the actions already taken.  

**Methodology:** The authors prove that the joint policy gradient can be decomposed into per‑agent terms comprising a local score function and a **decentralized critic**. ACPO trains each agent’s actor independently, but the agents’ updates are chained through the belief distribution over previous agents’ actions, ensuring that a single round of independent updates constitutes a true step on the full joint gradient without requiring centralized execution or value‑decomposition assumptions.  

**Key Findings:** Empirical results on Multi‑Robot Warehouse, SMACv2, and MA‑MuJoCo show that ACPO consistently outperforms strong baselines (centralized‑critic CTDE methods and alternating best‑response approaches), with performance gains increasing markedly as the number of agents grows, demonstrating effective scalability and coordination in cooperative MARL settings.


<details>
<summary>Abstract</summary>

Cooperative tasks in Multi-Agent Reinforcement Learning (MARL) require agents to collectively maximize a shared return. Under the Centralized Training with Decentralized Execution (CTDE) paradigm, policy gradients have remained difficult to compute directly. Prior methods largely follow two approaches: independent factorized updates with centralized critics, which lack general joint-improvement guarantees without value decomposition assumptions, or alternating best-response updates, which can converge to suboptimal Nash Equilibria. In this paper, we show the joint policy gradient admits an exact decentralized decomposition of per-agent terms, each formed from per-agent score functions and decentralized critics. Based on this decomposition, we develop Agent-Chained Policy Optimization (ACPO), where actors are trained independently, with their updates together constituting a single step on the joint policy gradient. Central to this result is a serialized view of the simultaneous joint decision in which agents commit actions one at a time, each conditioning on a belief over preceding actions. The belief acts as the coordination mechanism which ties the independent per-agent updates into a joint gradient step. We evaluate ACPO on Multi-Robot Warehouse, SMACv2, and MA-MuJoCo, where it outperforms strong baselines, with the gap widening as the number of agents grows.

</details>


### 135. LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via a Proprioceptive Dashboard

- **Authors:** Binyan Xu, Haitao Li, Kehuan Zhang
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30005v1](http://arxiv.org/abs/2606.30005v1)
- **PDF:** [https://arxiv.org/pdf/2606.30005v1](https://arxiv.org/pdf/2606.30005v1)
- **Categories:** cs.CL


> The paper presents **VISTA (Visible Internal State for Tool Agents)**, a training‑free, model‑agnostic interface that turns a language model’s hidden working memory into a set of typed, addressable blocks and exposes a “proprioceptive dashboard” showing each block’s token count, recency, and access history, allowing the LLM itself to make keep‑or‑drop decisions. By integrating this dashboard into several long‑horizon tool‑use benchmarks (LOCA‑Bench, BrowseComp‑Plus, GAIA) the authors show that even without additional learning, VISTA dramatically improves performance—e.g., raising Gemini‑3‑Flash’s success rate from 22.7 % to 50.7 %—and the gains increase as context pressure grows and transfer across model sizes and backbones. Ablation studies confirm that the dashboard’s visibility, rather than merely the archival/recovery mechanisms, is the key factor enabling more effective self‑managed context in agentic LLMs.


<details>
<summary>Abstract</summary>

Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window. Recent systems make context management agent- or system-controlled, but they either learn a compression policy that discards evidence or manage context in a layer the agent never sees. We argue both leave a more basic gap unaddressed. Frontier language models are proprioceptively blind to their own context. From the prompt alone they cannot see how large, how old, or how used each block is, the signals a keep-or-drop decision needs. We hypothesize that competent context management is already latent in capable models, and that what is missing is not a learned policy but an interface exposing this state. We introduce VISTA (Visible Internal State for Tool Agents), a training-free, model-agnostic layer that represents working memory as typed, addressable blocks, surfaces a runtime dashboard of per-block token usage, recency, and access history, and archives blocks as recoverable full-fidelity payloads. On LOCA-Bench, BrowseComp-Plus, and GAIA, the same untrained interface transfers across million-, 100K-, and 10K-scale trajectories. On LOCA-Bench it improves four backbones and lifts Gemini-3-Flash from 22.7 to 50.7%. The lift grows with context pressure and transfers across backbones. Ablations further confirm that the dashboard matters beyond archive and recovery tools.

</details>


### 136. SAGA: Scene-Aware, Goal-Evolving Agents for Long-Horizon CivRealm Strategy Planning

- **Authors:** Tianyu Jin, Shuo Chen, Yida Wang, Liuyu Xiang, Yingzhuo Liu, Zhiyao Jiang, Yexin Li, Zhaofeng He
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29932v2](http://arxiv.org/abs/2606.29932v2)
- **PDF:** [https://arxiv.org/pdf/2606.29932v2](https://arxiv.org/pdf/2606.29932v2)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **SAGA**, a multi‑agent framework that equips large‑language‑model (LLM) planners with a scene‑aware representation, on‑demand domain tools, and a dual‑horizon feedback loop to overcome the spatial blindness, context‑overflow, and lack of cross‑episode learning that cripple existing LLM‑based strategy agents.

**Methodology:** SAGA (i) builds a **Map‑Semantic Scene Graph** that translates tiled map data into typed natural‑language relations for each unit, (ii) uses a **Tool‑Augmented Planner** that queries fine‑grained state only when needed and delegates tasks to specialist controllers, and (iii) implements a **Dual‑Horizon Feedback Loop** that periodically generates intra‑game goals and performs post‑mortem causal analysis across games to evolve strategies without hand‑crafted rewards.

**Key findings:** In the complex strategy game FreeCiv, SAGA achieves the highest mean civilization score with lower variance than strong baselines, significantly outperforms them on infrastructure construction, reduces decoding cost by 27 %, and, when equipped with the cross‑game evolution module, attains the best cumulative score over five successive episodes—demonstrating that scene‑aware, tool‑driven, and cross‑episode learning mechanisms markedly improve long‑horizon strategic planning for agentic AI.


<details>
<summary>Abstract</summary>

Long-horizon strategic planning in complex strategy games demands concurrent reasoning across multiple decision domains under imperfect information and sparse reward. Existing LLM-based agents suffer from three systematic failures: scene blindness from raw tile coordinates, context overflow and domain coupling from monolithic state dumps, and shallow cross-game learning that treats each episode in isolation. We present SAGA, an LLM multi-agent framework with three mechanisms each directly targeting one class of failure: (i) a Map-Semantic Scene Graph that encodes typed spatial relations among game entities into per-unit natural-language context, resolving spatial blindness without global token inflation; (ii) a Tool-Augmented Planner that pulls fine-grained domain state on demand and dispatches per-domain directives to dedicated specialist controllers, eliminating context overflow, domain coupling, and mechanical constraint violations; and (iii) a Dual-Horizon Feedback Loop that combines periodic within-game goal generation with structured cross-game causal post-mortem, enabling principled strategic evolution without manual reward engineering. Evaluated on FreeCiv, SAGA attains the highest mean civilization score -- the environment's sole sparse objective reward -- with lower variance than the two strongest baselines, and is the only method that significantly surpasses every baseline on infrastructure construction, the resource axis most readily sacrificed under multi-objective conflict. It outscores the two strongest baselines in most head-to-head games while cutting output tokens (the dominant decoding cost) by 27%. Equipped with the cross-game evolution module, SAGA reaches the highest end-of-chain score across five successive episodes. Ablation studies confirm that each architectural component contributes independently to this advantage.

</details>


### 137. SABER-Math: Automated Benchmark for Information Retrieval Evaluation in Mathematics

- **Authors:** Nikolay Georgiev, Maria Drencheva, Kseniia Ibragimova, Ivo Petrov, Dimitar I. Dimitrov, Martin Vechev
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29894v1](http://arxiv.org/abs/2606.29894v1)
- **PDF:** [https://arxiv.org/pdf/2606.29894v1](https://arxiv.org/pdf/2606.29894v1)
- **Categories:** cs.IR, cs.AI, cs.CL, cs.LG


> **Main contribution:** The paper introduces **SABER‑Math**, the first fully automated benchmark for evaluating information‑retrieval components in mathematical problem‑solving pipelines, eliminating the need for costly expert relevance judgments.

**Methodology:** Starting from 283 K high‑school math problems, the authors (1) use large language models to generate concise solution summaries and topic tags, (2) retrieve candidate documents via ontology‑based topic matching and lexical similarity to the summaries, and (3) refine relevance through a Swiss‑style LLM preference tournament that yields fine‑grained relevance scores for each query–document pair.

**Key findings:** Modern embedding‑based retrievers markedly beat classical lexical and math‑specific baselines, yet all systems falter on symbol‑dense domains such as algebra and calculus. Moreover, performance on general IR suites (e.g., MTEB) does not predict retrieval quality on SABER‑Math, underscoring the necessity of dedicated math‑focused IR evaluation for agentic AI systems.


<details>
<summary>Abstract</summary>

As agentic AI systems tackle more complex mathematical tasks, they increasingly rely on information retrieval (IR) to search problem databases, theorem libraries, and educational resources. However, choosing the right retriever remains difficult, as it is infeasible to directly isolate its effect on downstream performance. On the other hand, existing retrieval-specific benchmarks often fail to capture fine-grained mathematical relevance, penalizing relevant documents. We address this gap by introducing SABER-Math, the first fully automated benchmark for evaluating mathematical IR without expert annotation. Starting from 283K high-school-level math problems with solutions, SABER-Math builds challenging reranking tasks in three steps: (i) first, LLMs extract concise solution summaries and mathematical topics for each problem; (ii) then, per-query relevant documents are discovered using ontology topic-based and lexical solutions-summary-based similarities, and (iii) finally, a Swiss-style LLM preference tournament produces fine-grained relevance ratings for the documents. We evaluate lexical retrievers, specialized mathematical retrieval systems, and recent embedding models. We find that while modern embedding models substantially outperform classical and math-specific baselines, even the strongest systems struggle in symbol-heavy domains like Algebra and Calculus. Importantly, we show that general-purpose IR benchmarks such as MTEB do not reliably predict mathematical performance, especially for recent embedding models, highlighting the need for math-specific retrieval benchmarks.

</details>


### 138. Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering

- **Authors:** Chengfeng Zhao, Yuqiao Tan, Shizhu He, Yequan Wang, Jun Zhao, Kang Liu
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29824v1](http://arxiv.org/abs/2606.29824v1)
- **PDF:** [https://arxiv.org/pdf/2606.29824v1](https://arxiv.org/pdf/2606.29824v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **Neural Procedural Memory (NPM)**, a training‑free mechanism that equips LLM‑based agents with a persistent “procedural memory” by steering their internal activation states rather than feeding them explicit textual instructions. NPM works by extracting **steering vectors** from past contrastive experiences and injecting them into the model’s hidden‑state space, thereby directly reactivating the neural circuits needed for a given task. Experiments on four standard agent benchmarks show that NPM matches the performance of Retrieval‑Augmented Generation approaches that use explicit prompts, and that a hybrid of implicit steering plus explicit workflows yields even more reliable execution; representational analyses further reveal that the steering vectors form coherent, task‑specific structures in activation space.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) excel as static solvers, transforming them into autonomous agents remains challenging. This transition requires continuous environmental interaction, yet current agents lack the necessary persistent procedural memory. Existing approaches predominantly employ Retrieval-Augmented Generation (RAG) to inject explicit textual guidelines into model contexts. However, relying solely on symbolic instructions can introduce a text-action disconnect, frequently failing to activate the internal representations necessary for correct task execution. To address this, the paper introduces Neural Procedural Memory (NPM), a training-free framework that represents agent memory through implicit activation steering rather than explicit instructions. By distilling procedural skills from historical contrastive experiences into steering vectors in the activation space, NPM directly activates the task-relevant neural mechanisms to guide task execution. Evaluations across four agent benchmarks show that NPM performs comparably to baselines using explicit textual instructions. Furthermore, the results show that combining implicit steering with explicit workflows provides complementary advantages, leading to more robust task execution. Representational analyses indicate that these steering vectors encode consistent task logic, forming organized structures within the activation space. These findings suggest that implicit activation steering provides a promising approach for managing agent memory.

</details>


### 139. Experience Graphs: The Data Foundation for Self-Improving Agents

- **Authors:** Gang Liao, Yujia He, Abdullah Ozturk, Zhouyang Li, Ying Wang, Zhitong Guo, Hongsen Qin, Yaobin Qin, Tao Yang, Zewei Jiang, Dianshi Li, Jort Gemmeke, Jiangyuan Li, Liyuan Li, Nathan Yan, Masha Basmanova, Uladzimir Pashkevich, Matt Steiner, Pedro Pedreira, Rob Fergus, Anirudh Goyal, Carole-Jean Wu, Gaoxiang Liu, Andrew Witten, Daniel J. Abadi
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29823v1](http://arxiv.org/abs/2606.29823v1)
- **PDF:** [https://arxiv.org/pdf/2606.29823v1](https://arxiv.org/pdf/2606.29823v1)
- **Categories:** cs.DB, cs.AI, cs.MA


> **Main contribution** – The paper introduces **Experience Graphs** as a formal, durable representation of everything an autonomous agent does during long‑horizon search (artifacts, tool calls, rewards, causal links, etc.), and builds **Trellis**, a database‑backed data foundation that treats these graphs as first‑class, queryable state rather than throw‑away logs.

**Methodology** – The authors model the agent’s search process as a set of database access patterns (frontier selection → queries, cross‑session reuse → vector‑seeded graph retrieval, training‑data extraction → materialized views, and replay/undo → time‑travel queries). They implement Trellis on top of a production kernel‑optimizer (KernelEvolve at Meta), redesigning the agent architecture so that the agent is stateless compute while the database owns, indexes, and persists the experience graph.

**Key findings** – In the KernelEvolve deployment, exploiting the persistent experience graphs yields **≈10× speed‑up** and **≈52 % lower token cost** through cross‑session reuse and automated training‑data extraction. More generally, the work demonstrates that making experience graphs a durable database asset enables reliable crash recovery, horizontal scaling, and a closed‑loop self‑improvement flywheel, turning inference‑time search into a cumulative, reusable knowledge base for future agentic AI systems.


<details>
<summary>Abstract</summary>

The database community has repeatedly advanced the state of the art by recognizing that new workloads demand new system architectures. We argue that long-horizon agentic tasks -- code generation, scientific discovery, hardware design -- are such a workload. These agents explore: they generate artifacts, execute tools, observe failures, branch, and repair over hundreds of steps. This search produces a structured object we call an experience graph: executable artifacts, tool outputs, rewards, sibling comparisons, and causal lineage. Yet existing agent frameworks treat this experience as disposable state -- JSON checkpoints and session logs that cannot be recovered after a crash, queried across users, or materialized into training data. We propose Trellis: a data foundation that treats the experience graph as first-class, governed, queryable database state. The core insight is that search over experience graphs is a database access pattern. Frontier selection is a query, cross-session reuse is vector-seeded graph retrieval, training-data extraction is a materialized view, and reconstructing what an agent knew at any past step is a time-travel query. When the database owns the experience graph, agents become stateless compute, and crash recovery, horizontal scaling, and a closed-loop training flywheel emerge as architectural byproducts. We ground the design in KernelEvolve, a production accelerator-kernel optimizer at Meta, where cross-session reuse reaches a target speedup roughly 10x faster at 52% lower token cost. More broadly, Trellis turns inference-time search from disposable computation into a durable institutional asset: logs made databases reliable; experience graphs may make agents cumulative.

</details>


### 140. MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory

- **Authors:** Kuan Wang, Chao Zhang
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29788v1](http://arxiv.org/abs/2606.29788v1)
- **PDF:** [https://arxiv.org/pdf/2606.29788v1](https://arxiv.org/pdf/2606.29788v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a multimodal AI agent is asked to forget a fact, current memory systems usually delete the text entry and report success. We find that the fact can remain recoverable from retained user images, including images tagged to entirely different facts, because VLMs use implicit visual cues at inference time. We introduce the Information Provenance Graph (IPG), a taxonomy that classifies memory representations by deletion affordance. The IPG reveals that deletion fails through multiple channels. Our benchmark, MemLeak, measures this across a deletion cascade: direct probing of deletion-capable systems yields <1%, but retained correlated text enables 18.3% recovery, and retained images enable 12.0% recovery (0.0% blind baseline, 0.3% FPR) -- with 47% of image leaks not text-recoverable. Content-aware semantic deletion reduces the image residual to 2.0%. The residual appears across multiple VLMs, a production memory system, and real Unsplash-licensed photographs. Dual-annotator human validation (kappa = 0.88) confirms judge reliability.

</details>


### 141. Towards Generalizable and Evidential Nuclear Magnetic Resonance-Based Molecular Structure Elucidation via Large Language Model Agent

- **Authors:** Zheng Fang, Chen Yang, Yusen Tan, Yunpeng Zhao, Fanjie Xu, Hongxin Xiang, Hanyu Sun, Hanyu Gao, Xiaojian Wang, Wenjie Du, Yuqiang Li, Jun Xia
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29776v1](http://arxiv.org/abs/2606.29776v1)
- **PDF:** [https://arxiv.org/pdf/2606.29776v1](https://arxiv.org/pdf/2606.29776v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **NMRAgent**, a large‑language‑model‑driven reasoning agent that integrates domain‑specific NMR analysis tools with a chemical knowledge graph to perform transparent, step‑by‑step molecular structure elucidation. By jointly planning the deduction process, generating candidate structures, checking peak‑atom consistency, and iteratively refining fragments with formula‑aware optimization, the system mimics expert reasoning instead of operating as a black‑box predictor. On a scaffold‑split benchmark containing novel scaffolds, NMRAgent raises top‑1 identification accuracy by 46.5 % and boosts average Tanimoto similarity by 0.502, and it successfully resolved two previously unknown natural products and corrected literature misassignments, demonstrating a scalable, evidentially interpretable approach for agentic AI in analytical chemistry.


<details>
<summary>Abstract</summary>

Nuclear Magnetic Resonance (NMR) spectroscopy is the gold standard for molecular structure elucidation, yet interpreting complex spectra for unknown molecules remains a bottleneck reliant on human expertise. While artificial intelligence has advanced this field, current methods face a critical trade-off: database retrieval cannot identify novel scaffolds, while de novo molecular structure elucidation models operate as black boxes, lacking the atom-level interpretability required for rigorous scientific validation. Here, we present NMRAgent, an evidential reasoning agent powered by large language models (LLMs) that bridges this gap by integrating specialized spectral analysis tools with chemical knowledge graphs. Unlike previous approaches, NMRAgent mimics the deductive reasoning of human experts: it takes experimental NMR spectra and molecular formula as input, plans the elucidation process, proposes candidate structures, verifies peak-atom consistency, and refines misaligned substructure through formula-aware fragment optimization. Enabled by its evidential reasoning, NMRAgent outperforms state-of-the-art methods, improving top-1 accuracy by 46.5% and Tanimoto similarity by 0.502 on a scaffold-split benchmark with novel scaffolds in the test set. Besides, we demonstrate the agent's practical utility by elucidating the structures of two previously unknown natural products isolated from Hydrangea davidii and Vitex trifolia, and by correcting structural misassignments in established literature. By combining high-accuracy prediction with transparent and evidence-based reasoning, NMRAgent establishes a new paradigm for interpretable AI in analytical chemistry.

</details>


### 142. CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark for Diagnostic Evaluation of LLM Portfolio-Management Agents

- **Authors:** Bo Qu, Mingguang Chen
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29771v1](http://arxiv.org/abs/2606.29771v1)
- **PDF:** [https://arxiv.org/pdf/2606.29771v1](https://arxiv.org/pdf/2606.29771v1)
- **Categories:** cs.AI, cs.LG, q-fin.CP, q-fin.PM


> **Contribution:** The paper introduces CLQT, a closed‑loop, cost‑aware benchmark that evaluates LLM‑driven portfolio‑management agents diagnostically rather than by raw returns, providing a reproducible audit trail that isolates where an agent’s reasoning succeeds or fails.  

**Methodology:** CLQT structures each trading episode into a five‑stage cycle (gather → synthesize → allocate → execute → reflect) and records every decision in a hash‑chained log; it enforces a hard time gate, realistic transaction/financing costs, strategy‑consistency checks, tiered memory, a model‑context protocol, and mandate‑aware synthesis, allowing agents to be run either as a committee of specialized roles or a single orchestrator.  

**Key Findings:** Using a contamination‑controlled backtest and a live post‑cutoff broker track, the authors demonstrate that CLQT can generate a five‑dimensional capability scorecard (Coherence, Acuity, Composure, Discipline, Reliability) that distinguishes agent competencies independent of market outcomes, offering a durable, extensible map of strengths and weaknesses for agentic AI in finance.


<details>
<summary>Abstract</summary>

LLM agents are increasingly cast as autonomous portfolio managers, and benchmarks have moved from financial question-answering to sequential trading. Yet most still rank agents by returns over a fixed window -- a weak proxy, since a period's return is dominated by the market path and apparent alpha can dissolve once look-ahead leakage is controlled. Such a ranking certifies neither sound reasoning, nor a consistent strategy, nor a durable edge. We introduce CLQT, which reframes closed-loop trading evaluation as diagnosis rather than ranking: an instrument that localizes where and why an agent's process succeeds or fails. CLQT is a fully closed-loop, cost-aware, strategy-consistent, temporally-gated environment whose agents run a five-stage cycle: gather, synthesize, allocate, execute, reflect. Each round emits a complete DecisionRound sealed into a recompute-verifiable hash chain, so every metric is reconstructable from the trail. Six pillars form the substrate: a hard TimeGate, institutional transaction- and financing-cost modeling, strategy-consistency scoring, three-tier memory, a Model-Context-Protocol tool layer, and mandate-aware synthesis. The same agent runs as a constrained committee of specialized roles or a single full-autonomy orchestrator, making process scaffolding an experimental variable. From the audit trail we compute a five-axis capability scorecard (APM-CS: Coherence, Acuity, Composure, Discipline, Reliability), with Coherence judged partly by a held-out, out-of-cohort LLM to curb self-preference bias. We validate it on a contamination-controlled multi-model backtest with an ablation grid and a live broker track on unseen, post-cutoff data, against a repeated-run noise floor. CLQT separates outcome from capability, yielding not a model ranking but a durable, extensible map of agent competencies and limitations.

</details>


### 143. DEEPMED Search: An Open-Source Agentic Platform for Medical Deep Research with Introspective Verification

- **Authors:** Maolin Liu, Fanyu Xu, Ruoqing Xu, Jiahang Zhang, Hao Wang, Rui Wang
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29746v1](http://arxiv.org/abs/2606.29746v1)
- **PDF:** [https://arxiv.org/pdf/2606.29746v1](https://arxiv.org/pdf/2606.29746v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Navigating the deluge of heterogeneous medical data, from academic literature (PubMed) to clinical guidelines (Web) and private knowledge bases, remains a critical bottleneck for evidence-based medicine. While commercial black-box tools lack transparency, standard open-source RAG implementations frequently suffer from reasoning drift when handling complex, long-tail queries. We present DEEPMED Search, a fully open-source, agentic platform designed for transparent medical deep research. Built on a high-performance Next.js architecture, DEEPMED Search features a source-adaptive router that autonomously dispatches sub-queries to PubMed, web search, or local graph-based knowledge bases based on information density. Crucially, the platform integrates an introspective verification module, powered by a causal-consistent multi-agent debate framework, to validate retrieved evidence against diagnostic logic before synthesis. To demonstrate its robustness, we showcase DEEPMED Search's ability to autonomously decompose high-difficulty rare disease queries, filter out confounding noise, and generate structured, citation-backed research reports in minutes. By open-sourcing this software, we provide the community with a robust infrastructure to democratize access to trustworthy, glass-box medical reasoning in research and prototyping settings.

</details>


### 144. LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents

- **Authors:** Yogeswar Reddy Thota
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30697v1](http://arxiv.org/abs/2606.30697v1)
- **PDF:** [https://arxiv.org/pdf/2606.30697v1](https://arxiv.org/pdf/2606.30697v1)
- **Categories:** cs.OS, cs.AI, cs.CV


> LUMOS introduces a new “semantic OS layer” that exposes the native accessibility and UI‑structure metadata of desktop and browser applications as a unified, machine‑readable representation (stable IDs, roles, names, values, bounds, affordances, and live pointer grounding). By feeding this compact semantic blueprint to an LLM‑driven observe‑act loop, agents can issue high‑level UI primitives directly instead of parsing screenshots, OCR, or visual crops, dramatically lowering token usage, latency, and coordinate uncertainty. Experiments show that accessibility‑grounded agents achieve comparable or better task performance with far fewer visual inputs, demonstrating a viable pathway toward AI‑native operating‑system interfaces.


<details>
<summary>Abstract</summary>

Current operating systems expose interfaces optimized for human users but not for AI agents. Humans benefit from pixels, icons, windows, visual grouping, mouse movement, and keyboard shortcuts; AI agents instead need compact semantic state, grounded actions, and reliable feedback. As a result, many computer-use agents are forced to interpret screenshots, OCR output, and visual crops, introducing high token costs, visual ambiguity, latency, and coordinate uncertainty. This paper introduces LUMOS (Language Model Unified Machine-Readable Operating-System Semantics), a semantic interaction layer between AI agents and operating systems. LUMOS converts native accessibility metadata and browser UI structures into machine readable semantic blueprints with stable identifiers, roles, names, values, bounds, and action affordances. It also supports live semantic pointer grounding by querying the UI element under or near the cursor through operating-system automation APIs. An LLM then acts through an accessibility grounded observe act loop using constrained visible-UI primitives rather than application-specific scripts. LUMOS does not claim to replace visual agents; instead, it reduces dependence on screenshots when operating systems already provide semantic structure. These results suggest a path toward AI-native operating systems and machine-readable interaction layers.

</details>


### 145. A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents

- **Authors:** Liu Zewen
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29719v1](http://arxiv.org/abs/2606.29719v1)
- **PDF:** [https://arxiv.org/pdf/2606.29719v1](https://arxiv.org/pdf/2606.29719v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces the **Evaluator‑Preference Coupling (EPC) framework**, a diagnostic toolkit that combines a Multimodal Preference Collapse Index (MPCI), an evaluator‑indexed coupling matrix, and Jensen‑Shannon divergence to detect when proprietary LLM evaluators cease to be reliable. Using EPC, the authors conducted a systematic audit of 122 runs of self‑adapting LLM agents across eight conditions (including GPT‑4o, Qwen, DashScope, DeepSeek, and a symmetric logistic‑regression baseline) and uncovered extreme, version‑specific volatility: some settings showed strong evaluator‑agent coupling (coefficients up to 1.18), while others collapsed to near zero, with a striking May‑to‑June drift in GPT‑4o that inverted the study’s original conclusion. The results demonstrate that evaluator‑driven preference dynamics are highly unstable across model updates, invalidating single‑snapshot evaluations and highlighting the need for continuous, multi‑evaluator monitoring in agentic AI research.


<details>
<summary>Abstract</summary>

Measurements of proprietary LLM evaluators can become invalid within weeks -- we document one case and provide the diagnostic framework to detect it. We introduce EPC -- comprising the Multimodal Preference Collapse Index (MPCI), evaluator-indexed coupling matrix, and Jensen-Shannon divergence (JSD) -- and apply it across eight experimental conditions (N=112 main + N=10 ablation = 122 unique repetitions, all reported). Coupling coefficients range from 0.00 to 1.18 across per-condition means (CV approx 0.9, n=8 conditions). Four conditions show strong coupling (N=36; GPT-4o May, GPT-4o-mini, Qwen3.7-plus, DashScope 30r); four collapse to near-zero (N=76; GPT-4o June, qwen-plus N=30, symmetric LR, DeepSeek self-eval). The May-to-June GPT-4o drift -- an N=8 re-replication inverting the study's conclusion -- is the most informative measurement: a diagnostic instrument detecting its own instability demonstrates the fragility it was designed to measure. Self-evaluation (97% zero, JSD=0.003) consistently collapses, though floor effects are possible. Output-format confound analysis finds per-strategy aggregate rho=0.89 but per-instance rho=0.219 (p=0.093); PCI reported as preference-convergence metric. We release EPC with all data. The finding is not any single coupling magnitude but the pattern of version-conditional instability that makes single-snapshot evaluator studies unreliable.

</details>


### 146. Optimizing Expert-Designed Crystal Graph Networks for Band-Gap Prediction with an Autonomous LLM Research Loop

- **Authors:** Chenmu Zhang, Boris I. Yakobson
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.29717v1](http://arxiv.org/abs/2606.29717v1)
- **PDF:** [https://arxiv.org/pdf/2606.29717v1](https://arxiv.org/pdf/2606.29717v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI, cs.LG


> The paper shows that a general‑purpose coding agent powered by a large language model can autonomously improve a state‑of‑the‑art crystal graph neural network (CGNN) for band‑gap prediction, achieving the highest reported test accuracy on the MatBench benchmark (≈100 k crystals) without any external pre‑training. The agent conducts an iterative research loop: it proposes modifications, writes and executes code, evaluates performance, and selects the best changes, ultimately incorporating known but previously unused tricks such as element‑pair edge features and a crystal space‑group embedding into the CGNN architecture. The results demonstrate that LLM‑driven autonomous agents can match or exceed expert‑designed ML pipelines for materials property prediction, while also revealing current limits of fully automated model discovery (e.g., reliance on existing human‑crafted ideas and the need for human‑level validation).


<details>
<summary>Abstract</summary>

Predicting a material's properties from its structure is a central, fast-advancing problem in computational materials science. A decade of work has produced standard public benchmarks and many published machine-learning models for the task (Dunn et al., 2020). The task's fixed metric and these baselines make it a natural setting for autonomous agent research (Karpathy, 2026). On the MatBench band-gap benchmark ($>$100k crystals), a general-purpose coding agent autonomously built the most accurate model trained without external pretraining, ahead of all seventeen expert-designed models reported for the task. A closer analysis shows it reached this by implementing known methods: either already standard in crystal neural-network models, or borrowed from other areas of machine learning. The contributing implementations include element-pair features on each message-passing edge and a crystal space-group embedding. The work not only demonstrates that LLM-agent autonomous research can optimize an expert-designed machine learning model for material property prediction, but also investigates the limitations of such autonomous research.

</details>


### 147. DSIP: A Dynamic Coordination Planner for Signal-Free Intersections using Diffusion-Model-Based Multi-Agent Motion Planning

- **Authors:** Qian Hu, Haoyang Peng, Songan Zhang, Ming Yang, Hongtei Eric Tseng
- **Published:** 2026-06-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.30694v1](http://arxiv.org/abs/2606.30694v1)
- **PDF:** [https://arxiv.org/pdf/2606.30694v1](https://arxiv.org/pdf/2606.30694v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Traffic signal control at urban intersections inherently introduces stop-and-go behavior, resulting in increased delays and reduced traffic efficiency, especially under high traffic demand. With the emergence of connected and automated vehicles (CAVs), trajectory-level coordination has emerged as a high-potential strategy to augment or transcend conventional phase-based management. This paper proposes DSIP (Diffusion-model-based Signal-free Intersection Planner), a multi-agent motion planning framework driven by a generative diffusion process. DSIP shifts the intersection management paradigm from discrete temporal phasing to continuous multi-vehicle trajectory optimization. This work evaluates the theoretical upper-bound performance of this coordination strategy under idealized communication and execution conditions to isolate the core benefits of the diffusion-driven approach. Using the SUMO platform, we evaluate DSIP across diverse four-leg intersection configurations. Experimental results demonstrate that DSIP significantly reduces average delay and maintains higher average speed compared to both fixed-time signal control and state-of-the-art reinforcement-learning-based controllers, particularly in medium- to high-density traffic. These findings suggest that diffusion-based trajectory planning provides a scalable and robust foundation for future autonomous intersection management. By unlocking latent intersection capacity through software-defined coordination, this approach offers a cost-effective pathway to improve urban traffic flow efficiency without requiring physical infrastructure expansion.

</details>



## Biorxiv (1 papers)


### 1. GeneBench-Pro: Evaluating Multistage Statistical Reasoning in Genomics, Quantitative Biology, and Translational Biomedicine

- **Authors:** Li, J. H., Ho, A. J.
- **Published:** 2026-06-30
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.29.735386](https://doi.org/10.64898/2026.06.29.735386)

- **Categories:** genomics


> **Main contribution:** GeneBench‑Pro extends the original GeneBench benchmark to a more challenging, domain‑wide suite (129 problems across genomics, quantitative biology, and translational biomedicine) that requires AI agents to carry out multi‑stage, inference‑heavy scientific workflows and arrive at concrete, decision‑critical quantitative conclusions.

**Methodology:** Each task supplies only brief context and a target estimand; the agent must navigate a series of dependent decision points—choosing data sources, statistical models, and validation steps—where a single wrong fork derails the downstream analysis. The problems were curated and validated by external domain experts, with a mix of publicly released, held‑out, and internal test items for unbiased evaluation.

**Key findings:** Even the most advanced GPT‑5.6 variants solve only about one‑third of the problems (≈31 % pass rate), while older GPT models and Claude Opus lag behind (8–16 %). Models frequently recognize local diagnostic cues but fail to propagate their implications, leading to incorrect estimator selection or dead‑end analysis paths, highlighting that long‑horizon, multistage statistical reasoning in biological domains remains an unreliable capability for current agentic AI systems.


<details>
<summary>Abstract</summary>

We introduce GeneBench-Pro, an expanded and improved version of GeneBench that comprises harder problems across a wider breadth of domains. GeneBench-Pro is a benchmark for AI agents performing realistic multi-stage scientific analyses in genomics, quantitative biology, and translational biomedicine which seeks to capture the complexity of real-world problems that computational life scientists face when tasked with producing a conclusion upon which a downstream scientific or translational decision is contingent. The benchmark comprises 129 evaluations targeting quantities of direct practical relevance across 10 primary domains and 21 terminal subdomains, with a genomics-centered core. Similarly to GeneBench, each problem provides the agent with brief context, a target estimand, and minimal guidance otherwise; the agent must then navigate multiple dependent decision points; i.e., substantive inferential forks where a plausible wrong choice changes the downstream analysis, to identify and execute the correct analysis workflow and arrive at the correct answer. Relative to GeneBench, GeneBench-Pro adds 29 new problems, drops three, and introduces significantly redesigned versions of 54 of the remaining 100 overlapping problems. 82 of the 129 problems were reviewed by external domain experts, whose findings led to prompt/data modifications and redesign of those problems whose targets were not sufficiently identifiable. Ten externally reviewed problems are released publicly, 50 held-out problems were provided to Artificial Analysis for independent third-party model benchmarking, and the remainder are retained as an internal holdout. In evaluations over the full 129-problem suite, GPT-5.6 Sol reaches an eval-level pass rate of 28.7% at the max reasoning level, and GPT-5.6 Sol Pro reaches 31.5% in separately reported GPT Pro runs. GPT-5.5 reaches 12.0%, GPT-5.4 reaches 8.9%, and the strongest non-GPT baseline, Claude Opus 4.8, reaches 16.0%. As with GeneBench, models often complete substantial portions of the workflow but exhibit a consistent gap between noticing and acting by identifying local diagnostic signals but failing to propagate the implications to the corresponding analysis decision. As a result, models often select wrong estimators or persist on initially plausible but incorrect analysis paths. GeneBench-Pro therefore measures an emerging capability of long-horizon biological reasoning that remains unreliable.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*