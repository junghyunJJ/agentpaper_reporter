# Weekly AI Agent Paper Report

**Generated:** 2026-10-12 19:00
**Period:** 2026-10-05 to 2026-10-11

## Summary

- **Total papers fetched:** 853
- **Papers matching keywords:** 178
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-10-05) | Change |
|--------|-----------|-----------|--------|
| Total matched | 178 | 178 | +0 |
| arxiv | 174 | 174 | +0 |
| biorxiv | 3 | 3 | +0 |
| medrxiv | 1 | 1 | +0 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (4 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. AI agent supervision of structural model building and refinement

- **Authors:** Wu, K.-P., Chueh, C.-K.
- **Published:** 2026-10-08
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.05.756902](https://doi.org/10.64898/2026.10.05.756902)

- **Categories:** biochemistry


> Summary unavailable.


<details>
<summary>Abstract</summary>

Structural model building and refinement need many decisions between different programs. These decisions often depend on an experienced researcher who knows how the programs work together and how to read experimental data. We used Claude Code with Claude Opus 5.5 to supervise this work for 24 cryo-EM and X-ray cases. The work finished in about 36 hours on one workstation. The agent prepared the inputs, ran established programs, read the validation results, compared candidate models and chose the next step. For 15 deposited cryo-EM models with weak starting geometry, the median MolProbity score improved from 2.62 to 1.76. For three crystal structures, the agent models came close to the published Rfree values. Chemical information such as ligands, ions and modifications must be provided by the researcher, in the same way as the sequence. With this information, the agent can place and check these components. These results show that agent supervision is acceptable when every decision can be inspected. The researcher makes the final scientific judgment. We suggest practical requirements for this kind of use. Future AI agents may help researchers obtain high quality and reliable structures of biological macromolecules.

</details>


### 2. Enrich.AI: An Agentic AI Platform for Interactive GeneSet Enrichment Analysis and Biological Interpretation

- **Authors:** Koumadorakis, D. E., Exarchos, T. P., Vlamos, P., Vrahatis, A. G.
- **Published:** 2026-10-06
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.29.755561](https://doi.org/10.64898/2026.09.29.755561)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: Enrichment analysis is widely used to extract biological meanings from gene lists. However, the large number of available tools and reference libraries often make the interpretation of results challenging. Inexperienced users lack clear guidance on which datasets and terms are most relevant to their data, whereas experienced researchers must navigate large result sets and consult multiple resources to identify biologically relevant findings. Integrating AI into this process can help to bridge these gaps. Results: We present Enrich.AI, a conversational biology assistant that integrates statistical enrichment analysis with automated biological interpretation. The agent operates on an LLM-based ReAct architecture and dynamically selects among the tools for enrichment (220+ gene set libraries), literature search (40+ million publications via Europe PMC), gene annotation, and database retrieval. Given a gene list and a short description of the biological context, Enrich.AI produces a written interpretation grounded in the retrieved literature and six interactive, configurable visualizations. A conversational interface enables human-in-the-loop refinement, letting researchers without programming experience explore results iteratively. The reliability of these interpretations was validated through a systematic evaluation on 50 gene sets, demonstrating high faithfulness to retrieved evidence and a low hallucination rate.

</details>


### 3. Verification Debt in Automated Biological Research Workflows: A Proof-of-Concept

- **Authors:** Gopalan, S., Narayanan, S.
- **Published:** 2026-10-05
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.29.755250](https://doi.org/10.64898/2026.09.29.755250)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent biological research has shown significant interest and progress towards adoption of agentic AI systems. Domain specific agentic platforms with access to large collections of biological tools with code generation and/or querying capabilities, such as Biomni (illustrative case in point), are representative of the capability to orchestrate automated research workflows. Such platforms enable collaborative AI workspace for drug discovery, genomics, bioinformatics, literature research, and experimental planning for biologists and researchers. When such platforms are used for the aforementioned workflows, individually validating every agentic decision and the research process by which it was reached becomes challenging due to the scale of decisions involved and oftentimes, insufficient disclosure of assumptions and methodological choices, limited traceability of evidence, and interpretive judgments embedded throughout the workflow, giving rise to verification debt. Verification debt in agentic environments could result in unexpected failures and consequences in downstream experiments. This study focuses on empirical qualitative characterization of verification debt in agentic (prompt to outcomes) workflows. Biomni was chosen the testing AI agentic platform in this study mainly due to the descriptive traces it provides to track every agentic step. Verification debt is examined through two complementary angles: the individual agentic decision steps that carry claims and evidence, and the underlying research process by which the agent arrives at and reports them. This study attempts to characterize verification debt with 10 test cases (covering proteomics, genomics and drug discovery) with varying degree of biological nuance across three identical and independent runs. Verification debt is represented through 9 decision-step metrics and 13 research-process metrics, and also propose the VERIFY framework for evaluating scientific verifiability and validity in agentic workflows.

</details>


### 4. Planner-Executor Style Multimodal Agentic System to Answer Patient Questions in Lung Cancer Screening CT

- **Authors:** Sakiyama, K., Serapio, A., Ye, M., Nowroozi, A., Bondarenko, M., Wu, Y., Qi, K., Liu, J., Vella, M., Yu, Y., Schnitzler, T., Rustagi, A. S., Sohn, J. H.
- **Published:** 2026-10-05
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.02.26364620](https://doi.org/10.64898/2026.10.02.26364620)

- **Categories:** radiology and imaging


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundAccurate patient understanding of lung cancer screening (LCS) results is critical for engagement and follow-up adherence, given the currently low screening uptake. While artificial intelligence (AI) systems show promise in facilitating patient communication, its effective use in clinical settings requires appropriate invocation of imaging tools and self-regulation by deferring certain questions to physicians. To this end, we developed and evaluated a planner-executor style multimodal agentic system to answer simulated patient questions about LCS CT results.

MethodsThis retrospective study utilized 116 LCS CT reports and images collected from a tertiary academic hospital. The system employed a multi-agent architecture (planner and executor) to mimic clinical reasoning. We developed a large language model (LLM)-based question generation framework to prepare a comprehensive set of 699 simulated patient questions, categorized as answerable and defer-to-doctor to assess self-regulation. Performance was evaluated on tool-calling, self-regulation accuracy (ability to correctly defer out-of-scope questions to a human provider) assessed by LLM-as-a-judge, and clinical quality assessed by a reader performance study with four physicians evaluating a subset of 100 responses.

ResultsThe system demonstrated high overall tool-calling accuracy of 93.1% (646/694; 95% CI: 91.2%, 95.0%) and self-regulation accuracy of 92.6% (462/499; 90.2%, 94.8%). For answerable questions, the percentage of responses receiving perfect 5.0 scores across all readers included 78.9% (180/228) for clinical accuracy (inter-rater agreement: Gwets AC2=0.92), and 73.2% (167/228) for patient understandability (0.86). For defer-to-doctor questions, the percentage of responses included 77.3% (133/172) for clinical accuracy (0.80) and 70.3% (121/172) for patient understandability (0.78).

ConclusionsThe planner-executor style multi-modal agentic system reliably answers patient-specific questions about LCS. Its high tool-calling and self-regulation performance demonstrates its potential as a safe and effective digital communication facilitator in LCS programs.

</details>


---



## Arxiv (174 papers)


### 1. RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics

- **Authors:** Weiliang Chen, Song Liao
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13889v1](http://arxiv.org/abs/2610.13889v1)
- **PDF:** [https://arxiv.org/pdf/2610.13889v1](https://arxiv.org/pdf/2610.13889v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This design enables rapid adaptation to runtime tool failures without expensive model retraining. We introduce EcoAgent, a benchmark of 5,172 real-world tools and over 210,000 query-tool pairs for offline retrieval and dynamic reliability evaluation. Experimental results demonstrate that RATED achieves a 52.2% relative MRR improvement over the ToolLLM API retriever on real-world queries, and reduces fault selection rate from 86.2% to 2.9% under severe API outage scenarios with a 30% failure rate, while incurring negligible latency overhead of less than 1 ms over encode-only inference. The code and dataset are available at https://github.com/Elliotes/EcoAgent.

</details>


### 2. MARGoS: A Configuration-Driven Platform for Reproducible MARL Experiments in ARGoS

- **Authors:** Tom Philipp Backert, Mohammad D. Soorati, Javad Ghofrani
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13772v1](http://arxiv.org/abs/2610.13772v1)
- **PDF:** [https://arxiv.org/pdf/2610.13772v1](https://arxiv.org/pdf/2610.13772v1)
- **Categories:** cs.SE, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) has become a prominent research direction, particularly within collective robotics, where the ARGoS simulator is widely used to study emergent swarm behavior. Yet despite this growth, systematic support for reuse and reproducibility in MARL-based swarm robotics remains limited and insufficiently standardized: a single experiment is assembled from manually aligned simulator files, training scripts, configuration values, paths, seeds, and environment details, so reuse and reproduction stay fragile even within one research group. To address this gap, we introduce MARGoS, a lightweight, configuration-driven platform developed in this project that elevates these experiment-defining inputs to first-class, platform-managed artifacts. MARGoS enables reproducible experimentation through configuration hashing, end-to-end seed propagation, frozen (immutable) configurations, structured logging, environment fingerprinting, and exportable experiment bundles that facilitate sharing, replay, and verification of results across machines and over time. A five-dimension evaluation (architecture, efficiency, reproducibility, usability, and collaboration) supports our claim that managing experiment variation as a platform responsibility makes ARGoS+MARL experiments easier to reuse, reproduce, and hand off. Our code is available at https://github.com/tombackert/margos.

</details>


### 3. Matched-Context Group Policy Optimization for LLM Agent Training

- **Authors:** Chenxu Zhang, Yaorui Shi, Wenlong Zhang, Jianchao Tan, Zihan Wang, Yiming Cheng
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13755v1](http://arxiv.org/abs/2610.13755v1)
- **PDF:** [https://arxiv.org/pdf/2610.13755v1](https://arxiv.org/pdf/2610.13755v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-Context Group Policy Optimization (MCGPO), a procedure for constructing weighted action preferences from already collected trajectories. MCGPO defines comparison contexts with pre-action state summaries and observed rubric progress, annotated by task rules. Two-action support selects among ordered exact and coarse matching rules. Fixed folds separate candidate decisions from the terminal outcomes used to orient their preferences, and support-dependent evidence weights scale an auxiliary pairwise objective alongside shared GraphGPO task learning. MCGPO reuses rollout data and each response's original history, preserving critic-free training. Across six environment-backbone settings with three training seeds each, MCGPO improves mean success over matched GraphGPO: by 0.47-1.46 percentage points on ALFWorld and WebShop with Qwen2.5-1.5B and 7B, and by 3.96 and 5.16 points on WebShop with Qwen3-4B and 8B. The ALFWorld gains build on baseline success above 92%, where remaining headroom is limited. Integrated success improves in three of four Qwen2.5 settings. Three-seed factorial controls support opposite-fold evidence and evidence weighting; joint state-rubric matching achieves the highest mean in all four representation-control settings.

</details>


### 4. SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning

- **Authors:** Hongrui Zheng, Aditya Singh, Rahul Mangharam
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13737v1](http://arxiv.org/abs/2610.13737v1)
- **PDF:** [https://arxiv.org/pdf/2610.13737v1](https://arxiv.org/pdf/2610.13737v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL, a constrained multi-agent reinforcement learning framework that allows for credit assignment even with joint constraint measurements. We use Signal Temporal Logic (STL) robustness to measure episode-level violation through running-maximum cost increments. Smooth full-episode robustness and differentiable dynamics provide action sensitivities, which allocate each cost increment across agents at the same decision time. These sensitivities account for delayed effects when weighting agents' shares of each cost increment. We study the framework in cooperative payload transport, connected navigation, and networked traffic control tasks. SafeDiSTL achieves 1.6-5.1x the safe-success rate in transport, improves navigation safe-success by 11.1%, and delivers 50-68% more throughput in traffic when compared to constrained baselines. Results demonstrate a strong improvement of the learned policy in dealing with shared constraint while retaining the performance of unconstrained policies.

</details>


### 5. A Baseline Assessment for the Agentic Web Technology Stack

- **Authors:** Vagner Figueredo de Santana, Diogo Cortiz
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13703v1](http://arxiv.org/abs/2610.13703v1)
- **PDF:** [https://arxiv.org/pdf/2610.13703v1](https://arxiv.org/pdf/2610.13703v1)
- **Categories:** cs.AI, cs.ET, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

The fast pace in which protocols, frameworks, and technologies are being proposed for LLM-based agents results in a complex scenario for anyone aiming to create state-of-the-art AI solutions. Without an assessment on how different protocols, frameworks, and libraries work together to compose an Agentic Web solution, developers and organizations face different challenges (e.g., skilling, governance, infrastructure) even before becoming part of the Agentic Web ecosystem. In this context, we propose a system for performing Agentic Web evaluations called MASTIF (Multi-Agent System TestIng Framework) and present a baseline assessment of Agentic Web technologies, including 3 LLMs, 3 protocols, and 4 agent implementation frameworks, against 300 Mind2Web benchmark tasks. Results suggest that selecting a task-specific technology stack may result in gains of task completion rate, efficiency score, and social value stability scores; and reductions in verbosity and time to complete tasks. With the presented results, we expect to present a baseline in terms of metrics and results for this complex and fast evolving scenario for those aiming at designing, assessing, and developing multi-agent systems.

</details>


### 6. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

- **Authors:** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, Maksim Skorokhodov, Roman Rybka, Yuanchao Liu
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13663v1](http://arxiv.org/abs/2610.13663v1)
- **PDF:** [https://arxiv.org/pdf/2610.13663v1](https://arxiv.org/pdf/2610.13663v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the entire ML script or search architectures in a discrete space, the framework operates over an open but semantically narrow space: the agent generates code only for the specified components, leaving the overall network structure unchanged. The approach is validated in two directions: tuning a classification spiking neural network with correlation learning, and solving high-order differential equations with Physics-Informed Neural Networks (PINN). Across five tasks---spiking classification on MNIST and Digits, and boundary-value problems for the generalized nonlinear Schrödinger equation (GNLSE) and Kuramoto--Sivashinsky (KS) equations---the agent outperforms the baselines: classification accuracy is 13 percentage points (MNIST) and 6 percentage points (Digits) higher; the error against the analytical single-soliton solution is reduced approximately 2491-fold; the invariant-preservation error drops approximately 325-fold in the selected GNLSE run with a Gaussian perturbation and by more than 100-fold on average over repeated initializations; and the mass drift drops 14-fold for the KS problem with a Gaussian perturbation. The framework thus tunes key components on tasks of different nature without changing its internal structure.

</details>


### 7. MENTOR: Learning from Failure with On-Policy Pedagogical Intervention

- **Authors:** Guanlan Yue, Hang Yu, Xiaoyong Huang, Ruipeng Li, Wei Zhang, Bingchang Liu, Rui Wang
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13594v1](http://arxiv.org/abs/2610.13594v1)
- **PDF:** [https://arxiv.org/pdf/2610.13594v1](https://arxiv.org/pdf/2610.13594v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement Learning from Verifiable Rewards (RLVR) is a key driver for Large Reasoning Models, but it is vulnerable to "zero-reward collapse", a training failure where a sudden increase in task difficulty causes the learning signal to vanish. We argue that the conventional approach of discarding these failed trajectories is wasteful, as they contain valuable diagnostic information about the model's cognitive gaps, a bright side that can be leveraged for recovery. Existing solutions, however, often regress to static, "off-policy-style" interventions like pre-defined hint libraries or perform post-hoc refinement, failing to provide the adaptive, forward-looking guidance needed to escape the collapse. To address this, we propose a paradigm shift towards on-policy pedagogical intervention and introduce MENTOR, a multi-agent framework that acts as a live mentor. MENTOR diagnoses the root cause of failure in real-time and dynamically generates targeted, instructional prompts to guide the learning agent's next attempt. As a plug-and-play module, MENTOR integrates seamlessly into existing policy optimization pipelines like GRPO without modifying the training infrastructure. Extensive experiments on math and code generation show that MENTOR effectively mitigates zero-reward collapse, outperforming state-of-the-art baselines. Notably, it achieves massive average relative gains of up to 78.3% on Llama-3.2-3B-Instruct over its base model.

</details>


### 8. MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures

- **Authors:** Loan Bernat, Matthieu Grard, Ariane Herbulot, Florent Lamiraux
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13534v1](http://arxiv.org/abs/2610.13534v1)
- **PDF:** [https://arxiv.org/pdf/2610.13534v1](https://arxiv.org/pdf/2610.13534v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon embodied agents must maintain task-relevant information, coordinate heterogeneous robots, and adapt their decisions as execution unfolds. Existing benchmarks investigate dynamic task execution and embodied multi-agent coordination, but provide limited evaluation of their intersection. We introduce MAGMA-Bench, an architecture-agnostic benchmark for persistent task reasoning in dynamic multi-robot environments. MAGMA-Bench evaluates agents across increasing task horizons and controlled online perturbations, including execution failures, task interruptions, and mission updates, with scenarios requiring coordination across robots with heterogeneous capabilities. It uses a structured skill-level interface to separate task-level reasoning from perception and low-level control. We evaluate locally deployable open-weight planners, multi-agent state-tracking strategies, and frontier models. Even the strongest evaluated models fail on a substantial fraction of clean episodes, and their success rates decrease further under online perturbations. Supervised adaptation greatly improves a small model, but performance remains substantially lower on longer and multi-robot missions. We release the benchmark, 261,646 task-level training examples, and an architecture-agnostic expert-trace generation pipeline.

</details>


### 9. Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits

- **Authors:** Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li, Yitong Liu, Hongkai Guo, Mengchi Chen, Chenyu He, Kaisheng Ma, Wei Xu, Song Han, Sihao Liu, Ligeng Zhu
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13494v1](http://arxiv.org/abs/2610.13494v1)
- **PDF:** [https://arxiv.org/pdf/2610.13494v1](https://arxiv.org/pdf/2610.13494v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often use context engineering, implemented through custom harnesses that manage tools, skills, and accumulated experience. However, we find that as single-session execution lengthens, the agent's reasoning intensity declines alongside slowing progress, summarized as long-horizon deceleration, and the benefits of these custom harnesses vanish as the underlying model improves, summarized as harness staleness. These findings suggest that their benefits may not persist across versions, which motivates a workflow-level approach in which agents build on one another's work across sessions. We model these alternating agent sessions as a context-reset semi-Markov decision process (CR-SMDP) and establish sufficient conditions for alternation to exceed single-agent reference limits, derive an explicit experiment-budget bound, and characterize when session caps preserve this advantage. Guided by this analysis, we introduce Humanize MLE Agents (HMA), which alternates two agents on a shared workspace, limits each session to at most k experiments and resets the context between sessions, without additional task-specific harness or prior knowledge supplements. Across 75 Kaggle tasks in MLE-bench, HMA reaches a state-of-the-art any-medal rate of 78.2%, exceeding the strongest open-source baseline by 8.0 points with a quarter of its time budget. Moreover, among six configurations spanning five heterogeneous agent pairs, HMA improves any-medal rate over the constituent baselines by 6.4 points on average, demonstrating cross-pair generality. A supplementary case on kernel optimization reaches 878 cycles, within 1.6% of the community leaderboard leader, demonstrating applicability beyond MLE.

</details>


### 10. A Local Agentic AI Framework to Generate Edge Case Scenarios for Safety Assurance

- **Authors:** Victoria J. Hodge, Colin Paterson, Rob Alexander
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13479v1](http://arxiv.org/abs/2610.13479v1)
- **PDF:** [https://arxiv.org/pdf/2610.13479v1](https://arxiv.org/pdf/2610.13479v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generating edge case scenarios is crucial for training, testing and safety assuring autonomous systems. This identifies hazardous failures to increase system reliability and robustness, ensures the system can still function safely on the boundaries of its operational design domain and learns the expected system behaviour for these edge cases. The rapid advancement in the generation and analysis capabilities of language models (LMs) has expanded their applicability and recent work has investigated LM scenario generation. However, many recent approaches rely on human-in-the-loop or rule-based strategies. This restricts the LM's ability to generate diverse and edge case scenarios; the long tail of the distribution. Our work uses local LMs in a laptop-based agentic AI framework for adaptive scenario generation. This is cheap, fully-controlled, ensures data privacy and security. It uses think, act, observe, update, and continue loops with lightweight JSON encoding to generate scenarios. We use the system requirements, system description and environment description as knowledge bases in contextual prompts for an LM to ensure scenario realism. A second, independent LM critiques each scenario using domain specific criteria so it can be refined. The refined scenarios are run in simulation and evaluation metrics collected. These metric scores are analysed and similar scenarios are created for edge cases (exploitation) or novel scenarios are generated to explore the scenario space. Post-hoc clustering using metric scores and thematic-type analysis of the rich-text scenario descriptions produced by the LM pinpoints functional gaps and their triggering conditions. This creates traceable evidence for the safety assurance case. Our work highlights the potential of a flexible and adaptive local agentic AI framework for automating edge case generation and producing traceable safety assurance evidence.

</details>


### 11. Collective Autonomous Vehicle Routing Needs Social Awareness for Coexistence with Human Drivers

- **Authors:** Anastasia Psarou, Mikolaj Rams, Blazej Torbus, Rafal Kucharski
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13439v1](http://arxiv.org/abs/2610.13439v1)
- **PDF:** [https://arxiv.org/pdf/2610.13439v1](https://arxiv.org/pdf/2610.13439v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Collective Autonomous Vehicle (AV) route choices in real-world traffic networks can create externalities for Human-Driven Vehicles (HDVs), as routes that benefit AVs may increase travel times for other road users. To address this, we introduce a social component, the marginal cost, to the selfish travel time AV reward. Marginal cost captures an AV's impact on other road users by comparing their travel times with those in a counterfactual simulation in which the AV is removed.
  We study AV route choice in mixed-autonomy traffic settings using Multi-Agent Reinforcement Learning (MARL), where AVs learn routing policies through repeated interactions with the traffic environment. Experiments on the real-world networks of Ingolstadt and Provins show that incorporating marginal cost into the AV reward not only limits the increase in HDV travel times and shortens AV travel times relative to selfish AV routing, but also improves overall system performance. In Ingolstadt, selfish routing of 40\% AVs increases the travel times of other vehicles by 1.7\%, and this drops to 1.1\% when the social reward is included. Interestingly, not only does overall system performance improve, but the AVs are also better off when acting socially.This effect is consistent across tested cities, penetration rates, and replications, yet when the weight of the social component in the reward increases, the system fails to reach the desired performance.
  For a more scalable approach to social AV routing in mixed-autonomy traffic, we compute the marginal cost only for the AVs whose route choices most affect the traffic system. This reduces the number of counterfactual simulations and achieves similar performance at a significantly lower computational cost. Our results suggest that AV routing should go beyond selfish rewards and, for the benefit of all traffic participants, include a social component in its objective.

</details>


### 12. Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits

- **Authors:** Chen Xi, Ding Ruixue, Wang Zhigaoyuan, Zhang Fanrui, Zhang Qiang, Chen Boli, Wang Shihang, Wang Tianfu, Ren Ailin, Wang Pengyong, Xie Pengjun, Xiong Hui
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13438v1](http://arxiv.org/abs/2610.13438v1)
- **PDF:** [https://arxiv.org/pdf/2610.13438v1](https://arxiv.org/pdf/2610.13438v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has emerged as a key paradigm for improving large language model (LLM) agents, enabling stronger reasoning, planning, and tool-use in interactive environments. However, existing agent RL methods remain fundamentally constrained by an on-policy reasoning bottleneck: when tasks exceed the model's current capability boundary, effective trajectories become extremely sparse and training often collapses. We introduce Rollout-Time Intervention (RTI), a technique designed to elicit successful trajectories beyond the policy's intrinsic exploration capacity. RTI operates by leveraging reward-side evidence (i.e., evaluation rubrics) during rollout to convert erroneous trajectories into successful ones, providing effective learning signals for tasks that the policy rarely solves on its own. Although intervention trajectories are inherently off-policy, we find that they can effectively guide policy optimization when trajectories with excessive distributional shifts are filtered out. Extensive experiments across five benchmarks demonstrate that RTI consistently outperforms RL baselines, enabling the post-trained policy to approach the performance of substantially stronger contemporary LLMs and, more importantly, transcend its original capability boundary. The code is available at https://github.com/Alibaba-NLP/qqr.

</details>


### 13. Web$hell: A Unified Interface for Agentic Web Access

- **Authors:** Sunghwan Kim, Deogyong Kim, Sangam Lee, Donguk Kwon, Dongha Lee
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13416v1](http://arxiv.org/abs/2610.13416v1)
- **PDF:** [https://arxiv.org/pdf/2610.13416v1](https://arxiv.org/pdf/2610.13416v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access through different access models, including search-augmented agents, browser-based agents, and, more recently, filesystem-based agents. Nevertheless, as users expect agents to complete long-horizon, end-to-end tasks, they increasingly need to conduct broad information gathering, perform browser actions, and revisit acquired evidence within a single trajectory. Yet our preliminary analyses reveal that existing access models struggle to meet these demands. They primarily support either information gathering or browser interaction, while combining their capabilities can involve substantial costs or performance trade-offs. To this end, we present Web\$hell, an interface that unifies web access under a single access model. Using a common schema defined by WebContract, WebCompiler compiles live webpages into addressable information and action objects. These objects are maintained in WebCache and handled through a shared set of operations, providing agents with consistent, operable, and persistent web access. Through extensive experiments across web search, web navigation, and deep research benchmarks, we show that Web\$hell achieves strong task performance at lower cost. Our results further indicate the importance of interface design for effective web access, with Web\$hell opening new possibilities for more capable and efficient LLM agents on the web.

</details>


### 14. AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents

- **Authors:** R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13335v1](http://arxiv.org/abs/2610.13335v1)
- **PDF:** [https://arxiv.org/pdf/2610.13335v1](https://arxiv.org/pdf/2610.13335v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation. We present AgentTune, a source-available Python library that provides a unified framework for developing and optimizing tool-using agents. At its core, AgentTune introduces a two-tier EventLog representation that preserves agent trajectories while supporting consistent projections for training, evaluation, and auditing. Building on this substrate, the library provides a shared agent runtime, tool-calling reinforcement learning, agentic distillation, retrieval-augmented generation, decision workflows, evaluation utilities, and a designed path toward self-healing agents. These components are exposed through composable interfaces so that agent strategies, training methods, evaluation procedures, and recovery mechanisms can be combined without requiring separate representations or pipelines. We demonstrate the framework across agentic tasks including legal contract search and domain-specific applications, illustrating its use for trajectory-based optimization, tool-use evaluation, and cross-task agent development. AgentTune is released as a source-available library at https://github.com/Lexsi-Labs/AgentTune

</details>


### 15. Masked Diffusion Language Agents for Tool-Integrated Chemical Reasoning

- **Authors:** Mengdi Liu, Chenghao Jia, Hong Chang, Shiguang Shan
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13330v1](http://arxiv.org/abs/2610.13330v1)
- **PDF:** [https://arxiv.org/pdf/2610.13330v1](https://arxiv.org/pdf/2610.13330v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing tool-integrated reasoning agent systems for complex chemical tasks remains a fundamental challenge. Although recent chemical agents have demonstrated promising performance through the integration of external tools, they are still built on the autoregressive paradigm, which is inherently constrained by causal attention and left-to-right generation. As a result, they often struggle with bidirectional molecular understanding, global coordinated tool planning and multi-source evidence integration. To address this challenge, we introduce ChemDiffAgent, the first masked diffusion language agent for tool-integrated chemical reasoning. It reformulates chemical reasoning as iterative denoising over interleaved reasoning and tool-use trajectories, enabling tool-use decisions to be jointly determined under full-trajectory context and thereby better aligning the agent's decision boundary with its knowledge boundary. We further analyze how this paradigm benefits agentic reasoning through harder infilling subproblems during training and flexible arbitrary-order decoding during inference. Then we develop a two-stage post-training framework, comprising agentic supervised fine-tuning and variance-reduced preference optimization, to enhance tool-use and reasoning capabilities. We also construct a comprehensive benchmark covering six chemistry tasks across both single-turn and multi-turn tool-use scenarios. Under matched budgets and evaluation, ChemDiffAgent consistently outperforms autoregressive agents, achieving an overall improvement of approximately 20%. Notably, our 8B model achieves performance comparable to, in some cases surpassing, significantly larger frontier models, such as GPT 5.5 and Claude Opus 4.7. Code is available at https://github.com/bilemond/ChemDiffAgent.

</details>


### 16. PRIME: Pre-Retrieval Index Modeling Enhancement for Structured Document Retrieval-Real

- **Authors:** Cheuk Hei Chung, Li Liu
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13296v1](http://arxiv.org/abs/2610.13296v1)
- **PDF:** [https://arxiv.org/pdf/2610.13296v1](https://arxiv.org/pdf/2610.13296v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

High-precision retrieval over external knowledge bases is essential for LLM agents to operate effectively. However, existing Information Retrieval (IR) research primarily optimizes query-side retrievers (e.g., ColBERT, BGE) and generators (e.g., Self-RAG, GraphRAG), while reducing corpus-side representation to chunking. This leaves index-side quality an underexplored lever. We propose Pre-Retrieval Index Modeling & Enhancement (PRIME), an index-side optimization framework built on two complementary tracks: an LLM-driven Semantic Restructuring (SR) track that transforms long documents into structured, information-dense sections, and a deterministic Metadata Synthesis (MS) and Hierarchical Retrieval (HR) track that extracts semantic anchors and heading structure for coarse-to-fine section retrieval. Our evaluations show that deterministic metadata matches structure-aware chunking's retrieval quality while cutting embedding computation by 45.8 $\times$ and index vector count by 22.4 $\times$. On top of these gains, Semantic Restructuring (SR) further improves Answer-F1 by 13.7% in full deployment, with characterized quality-fidelity-cost trade-offs. Across QASPER, BRIGHT, and NFCorpus, we further characterize three qualitative regimes that determine whether index-side optimization helps or degrades retrieval, while showing that these index-side effects are neutralized under a strong reranker.

</details>


### 17. Agent4Spec: An LLM-based Agentic System to Optimize API Specifications through Automated Validation and Market Analysis

- **Authors:** Yongjian Tang, Costel Moraru, Doruk Tuncel, Hanya Elhashemy, Steffen Klepke, Thomas Runkler
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13273v1](http://arxiv.org/abs/2610.13273v1)
- **PDF:** [https://arxiv.org/pdf/2610.13273v1](https://arxiv.org/pdf/2610.13273v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

API specifications serve as critical documentation for modern software development, directly impacting integration efficiency and client code generation. While recent advancements have leveraged Large Language Models (LLMs) to generate initial specifications from source code, existing approaches treat this process as a one-time event - overlooking the needs for continuous validation, long-term maintenance, and market-driven evolution of these artifacts. To address this issue, we present Agent4Spec, an autonomous multi-agent framework featuring two distinct pipelines: (1) a validation pipeline that detects and self-corrects OpenAPI syntax errors, and (2) a market analysis pipeline that conducts competitive research, identifies functional gaps against industry leaders, and automatically generates missing API-spec functionalities. We evaluate Agent4Spec on two curated datasets of API specifications spanning both general-purpose and industrial scenarios. Among 9 SOTA LLMs, the top-performer achieves 100% syntax error detection rates and over 95% implementation success for proposed corrections, while securing over 50% adoption rates for suggested endpoint improvements, representing a practical tool for API development.

</details>


### 18. Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents

- **Authors:** Lei Liu, Yunji Liang, Xiaowen Zhang, Jingqi Liu, Qi Li, Bin Guo, Zhiwen Yu
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13267v1](http://arxiv.org/abs/2610.13267v1)
- **PDF:** [https://arxiv.org/pdf/2610.13267v1](https://arxiv.org/pdf/2610.13267v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are highly vulnerable to memory-poisoning attacks. Existing defenses primarily rely on external modules for either static memory isolation or continuous online auditing, resulting in low memory efficiency and high computational overhead. To address these limitations, inspired by neuroscientific mechanisms that weak reactivation can destabilize memories and induce decay in the absence of reinforcement, we propose an agent-intrinsic training-free memory repair framework, DREAM (Dynamic Reactivation for Engram Attenuation in Memory), that enables selective functional forgetting of poisoned memories. Specifically, DREAM implements a three-stage pipeline: perturbation-induced implicit reactivation to reveal the structural fragility of malicious memories, adaptive anomaly diagnosis based on multi-dimensional activation patterns to detect topological anomalies, and a dynamic memory repair module that selectively suppresses harmful memories while reinforcing benign ones. Extensive experiments across diverse attackers and real-world tasks demonstrate that DREAM reduces attack success rates by over 95\% against backdoor poisoning while preserving strong benign utility. DREAM also achieves competitive robustness against injection attacks. In terms of runtime and token consumption, DREAM achieves up to a 2.13$\times$ speedup and a 37.7\% reduction in token consumption compared with A-MemGuard. Furthermore, DREAM also achieves a task success rate of 92.96\% on poisoned multi-agent systems.

</details>


### 19. Competence-Aware Orchestration for LLM-Based Multi-Agent Systems

- **Authors:** Songmiao Wang, Yuchen Wang, Chenglin Yu, Hongxia Yang, Ming Li
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13144v1](http://arxiv.org/abs/2610.13144v1)
- **PDF:** [https://arxiv.org/pdf/2610.13144v1](https://arxiv.org/pdf/2610.13144v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MAS) have emerged as a promising paradigm for enhancing complex reasoning through role specialization and collaboration, yet a key challenge remains: how can collaboration be adapted to a backbone's competence on the current query? This problem matters because more collaboration is not always better--richer coordination may help on difficult cases, but it also incurs additional token cost and redundant interactions. We propose a two-stage competence-aware framework for automatic MAS orchestration. It first models the LLM backbone's task-conditioned competence for the current query, and then uses this signal to adapt role activation and the communication graph. Across six benchmarks, our method achieves an average score of 93.81%. Experiments with six LLM backbones of varying competence levels further show that our method adjusts collaboration according to the inferred competence: for higher-competence backbones, it improves average accuracy from 87.22 to 89.97 while reducing token cost by 36.26%; for lower-competence backbones, it yields a further average gain of 4.58 points over existing methods. The same trend also holds on unseen backbones.

</details>


### 20. The value of information and the emergence of communication in evolved e-puck robots

- **Authors:** Fernando Montes-Gonzalez
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13118v1](http://arxiv.org/abs/2610.13118v1)
- **PDF:** [https://arxiv.org/pdf/2610.13118v1](https://arxiv.org/pdf/2610.13118v1)
- **Categories:** cs.RO, cs.MA, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent network with a residual path, either operating alone or as a channel within an Embedded Action Selection Architecture (EASA). Fitness measures only the time the robots spend over the food. When the robots receive a compass pointing to the food, use of the signal disappears completely. Without a compass, in a small arena, three independent runs achieved similar performance using different strategies: a referential signal, a permanent beacon, or no use of the signal. As the arena expands, the strategy based on a referential signal generalizes best. In contrast, evolving directly in the large arena does not increase the frequency of communication, but it does separate the strategies, and the referential signal clearly outperforms solitary searching. Within EASA, innate reflexes constrain the network and reduce performance. As its priorities evolve, evolution consistently weakens those reflexes. The results suggest that communication emerges in proportion to the value of the information it transmits, and that an innate scaffolding designed for isolated agents can be an impediment in a social task.

</details>


### 21. DRYLAB-Bench: Benchmarking the Biosecurity Risk of Agentic LLM Mutation Design

- **Authors:** Yuzhen Wang, Chunxiao Li, Baichen Le, Lewen Yan, Jie Zhang, Yucheng T. Yang, Xing-Ming Zhao, Lijun Li, Jing Shao
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13116v1](http://arxiv.org/abs/2610.13116v1)
- **PDF:** [https://arxiv.org/pdf/2610.13116v1](https://arxiv.org/pdf/2610.13116v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models (LLMs) acquire advanced biological design capabilities, they offer substantial research benefits but simultaneously introduce severe dual-use risks, such as engineering enhanced pathogens or drug-resistant bacteria. While biosecurity frameworks recognize these threats, the actual risk of LLMs executing dangerous biological modifications remains unquantified, particularly when augmented with specialized biological design tools (BDTs). Existing evaluations primarily assess hazardous knowledge possession rather than practical application, overlook risk amplification from BDTs, and rely on unreliable, expensive, or hazardous validation methods. To address these gaps, we introduce DRYLAB-Bench (Design Risk Yielded by LLM Agent in Biodesign), the first comprehensive benchmark evaluating the high-risk biological mutation design capabilities of LLM agents. Moving beyond basic question-answering, DRYLAB-Bench tasks agents with 30 genuinely hazardous mutation-design scenarios distilled from biosecurity guidelines. It evaluates models in a multi-round, tool-augmented environment where LLMs orchestrate BDTs to iteratively refine candidates. Crucially, it scores designs directly against 187,695 empirical wet-lab measurements from ProteinGym and ViroGym using our proposed Biosecurity Risk Score (BRS), quantifying risk-associated effects while enabling scalable and safe ground-truth verification. Evaluations of 15 frontier models reveal substantial baseline threats: without tools, 67.6% of one-shot designs exceed the average measured variant, and 21.4% reach the highest-risk decile. Equipping models with BDTs significantly amplifies this risk, raising the pooled risk by \(ΔBRS=+0.116\) and the top-decile share to 23.5%. Code: https://github.com/drylab-bio/DRYLAB-Bench

</details>


### 22. Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels

- **Authors:** Do Nguyen-Thanh, Junlin Fang, Bing Li, Zhen Fang, Sean Du
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13105v1](http://arxiv.org/abs/2610.13105v1)
- **PDF:** [https://arxiv.org/pdf/2610.13105v1](https://arxiv.org/pdf/2610.13105v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Failure attribution for LLM agents aims to identify decisive steps responsible for task failure, which is critical for debugging and improving agentic systems. Existing methods rely on costly LLM prompting, step-level error annotations, or verified successful trajectories that lack failure signals for assistance. In this paper, we study failure attribution from step-unlabeled failure trajectories, where each trajectory is known to have failed but its decisive step is unknown. We propose SOAP (Spectral scOring with Attention-guided Propagation), an effective framework requiring neither step-level training labels nor a separate success-only reference set. SOAP first constructs a spectral reference space from LLM representations and assigns each step a base error score according to its projection behavior. Importantly, later steps may exhibit stronger failure signals because they inherit an earlier mistake, causing independent scorers to favor downstream consequences over the decisive error. To address this downstream contamination, SOAP derives soft step dependencies from attention patterns and propagates downstream error evidence toward its likely upstream sources. Extensive experiments show that SOAP consistently improves attribution performance over competitive baselines.

</details>


### 23. When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows

- **Authors:** Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13092v1](http://arxiv.org/abs/2610.13092v1)
- **PDF:** [https://arxiv.org/pdf/2610.13092v1](https://arxiv.org/pdf/2610.13092v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents depend on repeated decisions to accomplish tasks, with large language models (LLMs) commonly serving as their core decision makers. The recent emergence of Jev offers an opportunity to make these decisions faster and at lower cost. However, it remains unclear whether such local savings can be translated into efficient and reliable task completion. In this paper, we investigate this efficiency transfer across five agents in two representative application settings, embodied tasks in ALFWorld and mobile app use in AndroidWorld. Across 4,500 task executions, we jointly evaluate task effectiveness, decision-level and task-level resource use, and execution behavior. Experimental results show that Jev integration substantially reduces decision cost and latency across all five agents, with task-level gains varying by workflow. Task success remains close to baseline levels on ALFWorld and declines more substantially in two mobile agents. Auxiliary reasoning and additional interactions absorb decision savings, while failed recovery and premature completion limit successful delivery. Mean cost per successful outcome increases in one agent even as spending per attempt falls. These findings highlight the importance of preserving progress, supporting recovery, and verifying completion when integrating efficient decision models into agent workflows. Their practical value should be assessed through successful task delivery, recovery behavior, and resources per delivered outcome.

</details>


### 24. CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits

- **Authors:** Jiahang Sun, Zhiwei Shang, Zhipiao Liu, Hongwei Yang, Guoqing Xie, Shuang Qiu, Zhongxiang Dai
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.13064v1](http://arxiv.org/abs/2610.13064v1)
- **PDF:** [https://arxiv.org/pdf/2610.13064v1](https://arxiv.org/pdf/2610.13064v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents have demonstrated remarkable capabilities in tackling complex tasks through agentic workflows. However, manually designing these workflows is labor-intensive and lacks flexibility to adapt to diverse queries. While automated workflow optimization is a promising direction, existing methods often incur expensive API costs during training-phase feedback collection. Furthermore, they fail to adaptively reuse high-quality workflows, which creates a bottleneck for both performance and cost-effectiveness. To address these limitations, we propose CB-Orchestrator, an adaptive framework that decouples workflow generation from selection. In the first stage, we construct a diverse pool of candidate workflows via evolutionary search. In the second stage, we formulate workflow selection as a Contextual Bandit problem, which enables sample-efficient learning by balancing exploration and exploitation, thereby significantly reducing the feedback required for training. During inference, the model adaptively selects the optimal workflow tailored to each query. Evaluations across five diverse benchmarks demonstrate that CB-Orchestrator consistently outperforms all baselines. Notably, on the MATH dataset, CB-Orchestrator achieves better performance than strong recent baselines while reducing training-phase API token overhead by no less than 40.55% and total end-to-end training (including workflow pool generation) token overhead by no less than 29.73%.

</details>


### 25. SwingGuard: Risk-Conditioned Multi-Agent Swing Trading with Dual-Timescale Governance

- **Authors:** Junzhou Su, Yichen Luo, Yebo Feng, Teng Li, Jiahua Xu
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12988v1](http://arxiv.org/abs/2610.12988v1)
- **PDF:** [https://arxiv.org/pdf/2610.12988v1](https://arxiv.org/pdf/2610.12988v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cryptocurrency swing trading spans mismatched timescales: positions remain active while market and event risk can change within minutes. However, many predictive and large language model (LLM)-based trading systems assess risk after strategy generation or run both functions at the same cadence, leaving proposals unconditioned by current risk and exposure weakly governed between revisions. We propose SwingGuard, a dual-timescale, long-only multi-agent framework for risk-conditioned strategy generation. At the strategy timescale, specialized analysts synthesize point-in-time technical, sentiment, on-chain, and macroeconomic evidence through bullish-bearish deliberation. The resulting evidence and current risk context are then combined by a Portfolio Architect to form a target position. At the governance timescale, a five-minute Risk Controller performs conditional diagnosis, maintains persistent risk states with staged recovery, audits the proposal, and constrains execution until the next strategy revision. This design allows risk to shape the feasible strategy before proposal finalization while continuing to govern the active position afterward. Evaluations on Bitcoin (BTC) and Ether (ETH) show that SwingGuard preserves positive returns after transaction costs while maintaining shallow drawdowns and strong risk-adjusted performance on both assets. The exposure-capped joint portfolio achieves a Sharpe ratio of 2.98, compared with 2.79 for an otherwise identical Post-hoc Risk variant. Structured traces further link risk evidence and state transitions to strategy constraints and executed position changes, providing an auditable framework for asynchronous cryptocurrency swing trading. Overall, the results indicate that conditioning strategy formation on current risk, together with persistent high-frequency governance, improves risk-adjusted performance without sacrificing auditability.

</details>


### 26. SEEDS: Preview-Guided Evidence Admission for Search Agents

- **Authors:** Jiajin Liu, Chenxi Xu, Dongzhe Fan, Yuanfu Sun, Qiaoyu Tan
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12932v1](http://arxiv.org/abs/2610.12932v1)
- **PDF:** [https://arxiv.org/pdf/2610.12932v1](https://arxiv.org/pdf/2610.12932v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Search agents extend large reasoning models with multi-round access to external knowledge, yet most existing systems largely conflate retrieving evidence with consuming it. Retrieved documents are commonly incorporated according to fixed or rank-based policies, despite the fact that evidence utility is conditioned on the agent's current reasoning state. Consequently, a lower-ranked candidate may be critical for the current step, while a higher-ranked candidate may provide redundant, irrelevant, or misleading information. We formulate this overlooked problem as evidence admission, which asks, at each search step, which retrieved candidates should be allowed to enter the agent's evolving reasoning context. To enable such selective control, we introduce SEEDS (Selective Evidence Entry During Search), a preview-guided evidence admission framework for search agents. SEEDS first exposes lightweight previews of retrieved candidates and then lets the agent jointly determine which candidates and how many should be fully inspected, conditioned on its current reasoning state. Unlike fixed or adaptive prefix policies, SEEDS can select arbitrary subsets with flexible cardinality, and it can be instantiated directly with an existing reasoning agent or further optimized through learning. Across nine knowledge-intensive QA benchmarks under both local corpus and live web search, SEEDS consistently improves search effectiveness while substantially reducing full-evidence consumption. Experimental analyses show that SEEDS more effectively selects useful candidates beyond the corresponding retrieval prefix. These results establish evidence admission as a complementary dimension of agentic search, separating what information is retrieved from what information is ultimately allowed to shape reasoning.

</details>


### 27. Collaborative Learning and Reasoning over Model Slices

- **Authors:** Yuheng Wang, Runde Yang, Zhuohan Bao, Qiran Zhang, Huatao Li, Yiyang Zheng, Lin Wu, Jingru Fan, Shu Yao, Yihan Li, Zhi Li, Chen Qian
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12927v1](http://arxiv.org/abs/2610.12927v1)
- **PDF:** [https://arxiv.org/pdf/2610.12927v1](https://arxiv.org/pdf/2610.12927v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) excel across diverse tasks, benefiting from knowledge priors, in-context reasoning, and test-time computation. Despite these strengths, single-model reasoning remains vulnerable to error propagation, as later steps depend on the model's earlier outputs, leaving reasoning blind spots difficult to independently reassess. To address this limitation, we develop \textit{collaborative learning}, encompassing the construction of heterogeneous collaborators and the learning of effective cross-model collaboration. Specifically, \textit{model slicing} replaces a large model with smaller, heterogeneous models under a comparable parameter budget, enabling prior reasoning to be reassessed across distinct model parameterizations. \textit{Pyramid supervision} combines protocol distillation with step-level supervision to refine reasoning and interaction decisions throughout collaboration. We evaluate our approach across four task categories: multi-hop question answering, mathematical reasoning, code generation, and open-ended constrained generation. The trained heterogeneous models achieve comparable or better task performance than the original large model and established multi-agent baselines, including reinforcement-learning-based methods, while also achieving higher inference efficiency than the multi-agent baselines and exhibiting differentiated collaboration patterns across tasks. These findings show that learned collaboration turns model heterogeneity into complementary reasoning capabilities.

</details>


### 28. Co-Modifying Application Code and Deployment Infrastructure: A Causal Study of AI Agent Pull Requests

- **Authors:** Mohammad Wathiq Soualhi, Basem Suleiman
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12849v1](http://arxiv.org/abs/2610.12849v1)
- **PDF:** [https://arxiv.org/pdf/2610.12849v1](https://arxiv.org/pdf/2610.12849v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current software engineering agents are evaluated predominantly inside isolated sandboxes against synchronous local tests. However, deploying features in collaborative repositories requires modifying continuous integration (CI/CD) pipelines, containers, and provisioning manifests alongside application logic. Because agents lack deployment awareness, attempting cross-domain modifications introduces unverified dependencies into asynchronous integration pipelines. To isolate the causal integration overhead of dual-scope pull requests (PRs)-modifying both application code and deployment infrastructure-we evaluated 26,999 PRs across two large datasets (AIDev v5 and MOSAIC-3M) encompassing six agent architectures and an aligned human baseline. Using a deterministic four-tier file taxonomy and an exact 4D strata-matching framework, we isolated integration metrics under conditional exchangeability while controlling for application volume. We find agents operate primarily as application coders or chore workers, with maintenance tasks capturing 17.70% to 25.41% of agent PRs. Dual-scope modifications represent only 4.48% to 4.55% of agentic PRs, yet trigger bimodal integration outcomes. In the first mode, explicitly reviewed contributions experience protracted delays, adding a median penalty of +13.13 hours and multiplying time-to-merge by 3.24x, driven mechanically by CI/CD and provisioning manifests. In the second mode, maintainer gatekeeping exhibits a structural bypass: even for external contributors lacking repository write access, agent identity reduces the odds of human review by 63.7% compared to human peers. Consequently, 43.1% to 56.2% of dual-scope PRs bypass inspection to merge silently in a median of under 31 minutes. These uninspected modifications compromise build verification, demonstrating the need for deployment-aware benchmarks and strict path-based access controls.

</details>


### 29. TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents

- **Authors:** Debajoy Mukherjee, Jeremy Carleton, Sushil Vemuri, Srinivas Shakkottai, Dileep Kalathil
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12828v1](http://arxiv.org/abs/2610.12828v1)
- **PDF:** [https://arxiv.org/pdf/2610.12828v1](https://arxiv.org/pdf/2610.12828v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Outcome-supervised group-relative policy optimization (GRPO) assigns the same advantage to every token in an LLM agent trajectory, leaving useful and unhelpful decisions undifferentiated. Hindsight credit assignment (HCA) can refine this feedback, but its estimates rely on trajectories containing informative alternatives at consequential histories. We introduce TreeHCA, which couples hindsight-guided exploration with hindsight credit assignment. TreeHCA uses changes in reference-answer likelihood to revisit intermediate histories and sample alternative continuations, forming a tree of reasoning and tool interactions. Because this exploration changes the distribution of sampled continuations, we derive the corresponding inverse-hindsight importance correction, including an exact finite-pool identity. We use this structure in a normalized tree backup that propagates terminal outcomes into turn-level advantages. This shared hindsight structure is TreeHCA's central design principle, linking informative exploration with hindsight-guided credit assignment. Across seven question-answering benchmarks and three Qwen backbones, TreeHCA outperforms all baselines in aggregate exact match, validating the effectiveness of paired exploration and credit assignment for multi-turn LLM agent training. Our code is available at github.com/TheBlackCat22/TreeHCA.

</details>


### 30. Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems

- **Authors:** Yuepeng Hu, Pegah Ghahremani, Reza Aghajani, Mahesh Pasupuleti, Himaghna Bhattacharjee
- **Published:** 2026-10-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12822v1](http://arxiv.org/abs/2610.12822v1)
- **PDF:** [https://arxiv.org/pdf/2610.12822v1](https://arxiv.org/pdf/2610.12822v1)
- **Categories:** cs.AI, cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems are increasingly used to solve coding tasks by coordinating agents that share code and plans. These agents are often optimized with reinforcement learning (RL) using automated evaluators, but bypassing evaluation can earn reward without producing a genuine solution. Prior work has largely treated reward hacking as a single-agent failure. In this work, we show that a reward-hacking strategy elicited in one agent can propagate to others and affect system coordination. Across four open-weight backbones, coding RL elicits and amplifies reward hacking in two settings: explicit mechanism descriptions in the system prompt and mid-training that models upstream exposure to facts about the coding environment. Using post-RL agents from the mid-training setting as sources, we observe propagation through code and shared memory, and across roles through natural-language plans. Even agents based on small open-weight models induce reward hacking in stronger closed-weight targets. On hard tasks, propagation can intensify along a transmission chain after the original source leaves as the code acquires more persuasive justifications. We also theoretically analyze conditions under which reward hacking amplifies, persists, or decays across agent interactions. Beyond propagation, reward hacking can bias task routing toward reward-hacking agents and survive candidate aggregation. As potential mitigations, we evaluate code review by the coder or a separate verifier, both of which reduce delivered hacks. Together, these results establish reward hacking as a transmissible strategy whose effects extend beyond the agent in which it first emerges.

</details>


### 31. VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails

- **Authors:** Duy Nguyen, Lesly Miculicich, Bhavana Dalvi Mishra, Shuo Li, Krishnamurthy Dj Dvijotham, Mohit Bansal, Tomas Pfister, Long T. Le
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12813v1](http://arxiv.org/abs/2610.12813v1)
- **PDF:** [https://arxiv.org/pdf/2610.12813v1](https://arxiv.org/pdf/2610.12813v1)
- **Categories:** cs.AI, cs.CL, cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly operate over sensitive resources, such as private documents and mutable system states, which can create serious safety and security risks. Runtime guardrails should therefore make inspectable, reproducible, and deterministic allow or refuse decisions before potentially irreversible agent actions are executed. However, safety and security requirements are rarely complete before deployment, so guardrails need to keep adapting as new risks emerge. Existing adaptive guardrails learn from deployment experience, but they usually apply safety policies through LLM inference, which can lead to inconsistent decisions and ambiguous policy interpretations. Formal guardrails, on the other hand, enforce policies deterministically, but they usually rely on pre-deployment or task-specific policies and have no mechanism to adapt to newly observed risks. We introduce VEPA, a framework for the verified evolution of formal agent guardrails. VEPA represents the guardrail as a formal policy of executable symbolic rules over typed agent events. During deployment, we use an LLM guided by deployment feedback to propose policy patches that fix newly observed failures while preserving previously correct behavior. Then, a deterministic verifier only accepts policies that are structurally valid and conflict-free. Finally, an evidence-aware authority layer activates a verified rule only when it has enough supporting evidence, so uncertain updates cannot directly affect guardrail decisions. Across ASSEBench-Safety, ASSEBench-Security, and ATBench, VEPA consistently outperforms baselines while expanding the scope of deterministic formal-policy enforcement. These gains also hold under more challenging deployment conditions, including mixed streams, corrupted feedback, and longer horizons.

</details>


### 32. EvoBelief: Falsifiable World Models for Self-Improving LLM Agents

- **Authors:** Janet Wang, Jiang Guo, Yi Xiang, Jiaqing Yuan, Mingwen Dong, Hideo Kobayashi, Shuaichen Chang, Chandan K. Reddy, Jiarong Jiang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12789v1](http://arxiv.org/abs/2610.12789v1)
- **PDF:** [https://arxiv.org/pdf/2610.12789v1](https://arxiv.org/pdf/2610.12789v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-evolving LLM agents typically improve how they act through accumulated experience, reflection, or skills. Yet even procedurally capable agents can fail when their beliefs about environment dynamics are incomplete, incorrect, or outdated. We study a complementary axis of self-evolution: evolving those beliefs during deployment. Such beliefs can support multiple tasks, but incorrect ones can also propagate across them. We introduce EvoBelief, a self-evolving world model that represents environment knowledge as falsifiable hypotheses. Unexpected outcomes and decision-relevant unknowns trigger hypothesis formation. Later observations and controlled experiments provide independent validation before a rule can guide predictions or plans within its supported scope. Counterexamples narrow or retire rules as the environment changes. The language model remains frozen, and each rule remains linked to its evidence and the decisions it changes. Across four benchmarks spanning static dynamics, hidden drift, and scientific discovery, EvoBelief improves task performance and reuses learned rules across tasks. On ALFWorld without actor-side transition memory, it improves success over the matched Frozen World Model by 23.9% and 31.3% with Claude Haiku 4.5 and GPT-5.4, respectively. On MiniGrid, it revises stale rules and recovers after unannounced dynamics changes. In DiscoveryWorld's Reactor Lab, it discovers and validates quantitative laws, completing 83.3% of Normal-tier and 58.3% of Challenge-tier instances, versus 0% for each evaluated baseline. These results demonstrate self-improvement through testable, revisable environment knowledge rather than model-parameter updates.

</details>


### 33. MADS: Multi-Agent Dialog Simulation for Robust Conversational Agents

- **Authors:** Arkajyoti Chakraborty, Adam Zernik, Ishika Kulkarni, Mudit Arora, Hugo Lin, Justin Chiu, Alessandro Di Bari, Neha Gupta, Andreas Stolcke
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12757v1](http://arxiv.org/abs/2610.12757v1)
- **PDF:** [https://arxiv.org/pdf/2610.12757v1](https://arxiv.org/pdf/2610.12757v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Task-oriented conversational agents remain fragile under realistic conditions, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present MADS (Multi-Agent Dialog Simulation), a synthetic data generation pipeline that produces structured, diverse dialogue trajectories. We inject adversarial conversation, producing validated conversation trajectories that capture realistic, unhappy paths. Using MADS, we construct MADS-Bench: a benchmark spanning six domains, 55 personas, and 1095 conversations, with approximately 66% of conversations containing failure-prone conversation scenarios. We evaluate the robustness of the trained models using a two-stage training approach that combines supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR).

</details>


### 34. How Do Hardware Faults Manifest Differently in LLM Agents?

- **Authors:** Aiden Rubey, Zachary Coalson, Cong Chen, Jean-Philippe Monteuuis, Jonathan Petit, Sanghyun Hong
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12756v1](http://arxiv.org/abs/2610.12756v1)
- **PDF:** [https://arxiv.org/pdf/2610.12756v1](https://arxiv.org/pdf/2610.12756v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present the first systematic study of the resilience of large language model (LLM) agents to random hardware-induced faults. Prior work on hardware fault resilience in LLMs focuses on model-level outcomes, such as incorrect outputs or generation failures. Yet LLM agents repeatedly interact with tools and environments, creating loops that can change how hardware faults manifest. We conduct an extensive evaluation across three agent benchmarks, comprising 6,814 agent executions: 2,400+ clean runs and 4,300+ fault-injected runs with independently sampled random two-bit weight faults. We trace how these faults propagate through agent execution. Unlike prior studies, we find that agentic execution transforms model-level corruption into distinct system-level outcomes: (1) agents can recover from faulty model outputs and still complete tasks correctly; (2) this recovery increases computational and execution costs; (3) a few faults cause subtle but semantically meaningful errors while the agent otherwise behaves normally; and (4) for some models and scenarios, faults can alter security and alignment behavior.

</details>


### 35. CLEAT: Learning Value-Guided Clarification for Interactive Agents

- **Authors:** Jiatan Huang, Zheyuan Zhang, Ziming Li, Tianyi Ma, Mingchen Li, Yanfang Ye, Chuxu Zhang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12655v1](http://arxiv.org/abs/2610.12655v1)
- **PDF:** [https://arxiv.org/pdf/2610.12655v1](https://arxiv.org/pdf/2610.12655v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can execute increasingly complex tasks, but effective assistance also requires aligning their actions with goals and constraints that users may leave unstated. We study this problem as interactive intent alignment through clarification. Yet clarification is useful only when the agent can turn the answer into better decisions. As training changes how the agent handles incomplete information and uses additional answers, the same clarification can become more or less useful. We introduce CLEAT (CLarification through valuE-guided Agent co-Training), a framework that co-trains a clarification-value controller and the task policy from shared interaction outcomes. We formulate residual query value to measure the task utility gained by asking rather than proceeding under the current policy, and estimate it through paired rollouts from the same interaction history. These paired returns train the controller to predict clarification value and the task policy to select useful questions and act on the answers. The controller guides subsequent rollout collection, while outcomes from the updated agent provide new value labels that allow clarification guidance to adapt as the agent learns. With Qwen3-4B, CLEAT achieves the highest mean score in all ten evaluation settings across four benchmarks. Gains over the strongest baseline reach 13.2 and 6.5 percentage points on UserGym Travel and IN3 underspecification judgment accuracy, respectively. Ablations show that co-training improves the task policy even when the controller is removed at inference, while adapting clarification guidance to the evolving policy yields further gains.

</details>


### 36. SynAct: Synergistic Active Feedback Learning for LLM Agents

- **Authors:** Ning Liu, Ian Li, Kristina Klinkner
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12651v1](http://arxiv.org/abs/2610.12651v1)
- **PDF:** [https://arxiv.org/pdf/2610.12651v1](https://arxiv.org/pdf/2610.12651v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents executing multi-step workflows fail in two fundamentally different ways: recoverable slips, which further attempts can repair, and knowledge gaps, which retrying cannot resolve. Expert feedback can address the latter, but expert attention is scarce. The key challenge is therefore not whether to ask for feedback, but where feedback can change the outcome. Existing approaches either avoid expert feedback, allowing agents to reinforce their own errors, or allocate feedback at the task level without identifying consequential decisions. We present SynAct, an active learning framework that treats expert attention as the binding constraint and allocates feedback at the level of individual decisions. SynAct ranks decisions by the mutual information between the selected action and the terminal outcome across repeated rollouts, queries an expert at the highest-value decisions, and distills the resulting corrections into transferable rules that the agent can reuse without expert access at deployment. We theoretically characterize what this signal identifies under finite repeated sampling: with k rollouts and at least m observations per action, outcome-constant decisions have zero mutual information, while outcome-separating decisions have mutual information at least H2(m/k) bits, yielding exact separation for any threshold t in (0,H2(m/k)). This also explains why success-based acquisition can be blind when all rollouts fail: success is constant even when failed runs reach different outcomes. Across four agent benchmarks and four models spanning three families, SynAct improves held-out accuracy in all 16 evaluated settings, by +11.7pp on average. The same signal transfers to inference-time routing, where SynAct outperforms budget-matched cascade, uncertainty, and expert-judge routers in 15 of 16 settings, while a single targeted correction outperforms seven additional unaimed retries.

</details>


### 37. Distributed Harmonic-Covariance Feedback for Hole Closure in Planar Robot Swarms

- **Authors:** Jitian Liu, Subhrajit Bhattacharya
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12637v1](http://arxiv.org/abs/2610.12637v1)
- **PDF:** [https://arxiv.org/pdf/2610.12637v1](https://arxiv.org/pdf/2610.12637v1)
- **Categories:** cs.RO, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

We consider hole closure in a planar multi-agent system whose sensing disks form a time-varying Čech complex. We propose a harmonic-covariance feedback that uses harmonic edge signals to locate holes and converts those signals into agent forces. For distributed evaluation, we use a fixed-degree polynomial of the regularized Hodge Laplacian. This polynomial is evaluated through local operator applications. The closed loop has a unique global trajectory from every safe initial state. The model data and initial state are supplied with procedures for approximation to any requested accuracy with explicit error bounds. We assume that hole area is measurable and bounded, holes evolve continuously without splitting or merging, and only finitely many temporary new holes appear. Under these conditions, offline finite calculations produce rational lower bounds for the cumulative hole area on the time horizon without querying trajectory data. These bounds converge to that cumulative area, whether finite or infinite. If it is finite, holes close in the time-averaged sense: the average normalized hole area over every fixed-length time window tends to zero as time tends to infinity. In a 15-second numerical demo, all holes close by 9.9s and remain closed through the end.

</details>


### 38. Reflective Prompt Optimization of a Deep-Research Agent: A Topic-Disjoint, Multi-Seed Protocol for Measuring Transferable Gains and Prompt-Level Overfitting

- **Authors:** Elias Lumer, Sahil Sen, Vamse Kumar Subbiah, Kevin Paul
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12601v1](http://arxiv.org/abs/2610.12601v1)
- **PDF:** [https://arxiv.org/pdf/2610.12601v1](https://arxiv.org/pdf/2610.12601v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prompt optimization is an attractive alternative to reinforcement learning for adapting language-model agents, since it is cheap and produces human-readable artifacts. On factual tasks, however, it carries a failure mode that scalar-reward reinforcement learning does not. An optimizer that reads the training examples can write their answers into the prompt, so an in-distribution gain may be memorization rather than transferable behaviour. We apply reflective prompt evolution (GEPA) to the two system prompts of a multi-agent deep-research agent and evaluate it under a topic-disjoint split in which no topic is shared across train, validation, and test. Held-out citation reward rises by 0.079, from 0.702 to 0.781, with a bootstrap 95\% confidence interval of [0.051, 0.107], and the gain replicates across three seeds (mean 0.107). Nearly half of the winning prompt is a memorized answer key, yet a controlled ablation shows this content earns no reward even on the exact training questions it encodes. The large validation-minus-held-out gap is therefore small-sample selection under a noisy judge, not memorization. Varying the verifier isolates what makes the gain transfer. Decomposed per-dimension feedback is the causal ingredient, and collapsing it to a single scalar reward makes held-out transfer negative. The gain persists under an out-of-family judge and is largely reproduced by a hand-written version of the discovered recipe. Credible evaluation of prompt optimizers therefore requires held-out topics, multiple seeds, and verifier ablations. We release the candidate prompts, lineage diffs, figures, tables, and analysis.

</details>


### 39. Know What You Don't Know: Agentic Data Synthesis by Evolving Generation Space for Closed-Loop Learning

- **Authors:** Wei Yang, Qing Ping, Youzhi Luo, Yawei Wang, Abhishek Kumar, Panpan Xu, Jun Huan
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12593v1](http://arxiv.org/abs/2610.12593v1)
- **PDF:** [https://arxiv.org/pdf/2610.12593v1](https://arxiv.org/pdf/2610.12593v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The continued improvement of large language models increasingly depends on synthetic experience, yet effective data synthesis for interactive agents requires not only executable and verifiable trajectories, but also interactions that provide learning value for the current task agent. Existing methods increasingly incorporate environment feedback, data validation, or learner failures, but still face a feedback-to-decision gap: observed weaknesses do not directly specify how future synthesis should change, or whether they can be represented by the current synthesis space. To address this gap, we propose EvoSyn, a learning-feedback-driven multi-agent framework that organizes synthesis around a revisable state specifying what interaction factors can be deliberately generated and where synthesis effort should be allocated. A role-specialized multi-agent system translates learner feedback into synthesis revisions, while a Designer allocates synthesis directions and a Planner grounds them into executable experience. This process enables within-space adaptation toward weak or under-covered regions and synthesis-space expansion that promotes newly discovered factors into explicit generation controls. Experiments on $τ^2$-Bench and CAR-Bench show that EvoSyn improves average task success by 13.3 points over the strongest synthesis baseline, while producing higher-quality and structurally broader synthetic experience and discovering controllable factors missed without learner feedback.

</details>


### 40. Mental-Models for Multi-Agent Systems

- **Authors:** Hanan Gani, Lulu Shao, Manmohan Chandraker
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12453v1](http://arxiv.org/abs/2610.12453v1)
- **PDF:** [https://arxiv.org/pdf/2610.12453v1](https://arxiv.org/pdf/2610.12453v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large foundation models have accelerated progress toward general-purpose agents that interact with humans and other agents through language and multimodal signals. However, robust multi-agent decision-making requires reasoning about what other agents know, intend, and are likely to do under partial observability. Current agentic systems often operate through prompt design, memory, or end-to-end behavioral shaping, but typically do not learn an explicit partner-state representation that can be reused as a decision variable across tasks. We introduce \emph{mental-model-enabled agents}, a framework that equips an agent with a latent mental model of its counterpart, allowing it to infer hidden beliefs, intentions, and likely reactions from the observed history and use these inferences to guide action selection. Our method learns an amortized recursive Theory-of-Mind representation, with first- and second-order mental-state structure, jointly with a belief-conditioned reward model that evaluates candidate actions relative to the inferred partner state. A policy is then learned under this belief-aware signal, yielding an agent that can act independently at inference time while retaining the benefits of explicit partner modeling. We evaluate the same framework on both language-only and multimodal benchmarks. Across these settings, explicit mental-state modeling consistently improves interaction quality and Theory-of-Mind performance over base agentic systems, showing that structured partner modeling is a useful inductive bias for general multi-agent systems. Our code is publicly available at https://github.com/hananshafi/Mental-Models

</details>


### 41. Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception

- **Authors:** Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba, Adam Gleave, Chris Cundy
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12445v1](http://arxiv.org/abs/2610.12445v1)
- **PDF:** [https://arxiv.org/pdf/2610.12445v1](https://arxiv.org/pdf/2610.12445v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent incidents have highlighted the challenge of monitoring LLM agents and the danger of models deceiving people. We show that white-box deception detection via probes can be scaled up to frontier monitoring settings by collecting the largest deception dataset to date for training probes and introducing a novel probe architecture which can aggregate information across many layers and tokens. Our probes achieve 98.8% AUC in SHADE-Arena, surpassing an Opus 5.5 text-monitoring baseline, and show improved efficacy as the underlying model is scaled up. To push our probes to their limit, we test them on several cases where deception cannot be determined from the context alone. In these cases, which we refer to as introspective deception, the ground truth can only be determined through careful elicitation or thorough knowledge of a model's training data. In one such evaluation, we show that probes can distinguish transcripts containing a model's true hidden goal from other goals with an AUC of up to 99.7%. Our probes also readily detect deception on prominent open-weight models which lie about politically sensitive topics, and about their beliefs when put under pressure. We release our training dataset, dubbed FIBS, to help drive frontier deployment of effective probes, and encourage the community to expand upon it with further examples of deception and sabotage.

</details>


### 42. Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff

- **Authors:** Erin Crawley, Hidenori Tanaka
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12436v1](http://arxiv.org/abs/2610.12436v1)
- **PDF:** [https://arxiv.org/pdf/2610.12436v1](https://arxiv.org/pdf/2610.12436v1)
- **Categories:** cs.AI, cond-mat.dis-nn, cs.MA, physics.bio-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can now conduct real-world cyberattacks, scale up capabilities with the number of agents, and collectively pursue misaligned goals to obtain rewards. Together, these factors raise the risk of a population explosion of misaligned agents: agents could compromise computers and secretly deploy additional agents, creating a self-reinforcing cycle where larger populations develop greater collective cyber capability and expand further. This raises a fundamental question: What determines whether a population of misaligned agents remains contained or takes off into this self-reinforcing cycle? This population-level problem is ecological safety: unlike individual-agent or multi-agent safety with a fixed population, it concerns the dynamics of the population itself. Here, we develop an ecological theory of AI-agent populations based on a population growth equation in which fitness (growth rate) depends on cybersecurity capability. We show that, without collaboration, the population takes off only when individual-agent capability exceeds a critical threshold. With collaboration, however, collective cybersecurity capability increases with population size. This creates a critical population threshold: below it, the population declines; above it, the population takes off, even though individual-agent capability has not changed. In ecology, this phenomenon is known as the strong Allee effect. Because red teaming a small group of agents cannot guarantee ecological safety in larger populations, our theory calls for ecological red teaming and population pacing: gradually deploying larger agent populations in controlled environments, while measuring how cyber capability scales with population size, and estimating the critical population size for takeoff. Capability gains may lower this threshold, requiring re-estimation for each new model generation.

</details>


### 43. OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport

- **Authors:** Babak Barazandeh, Connor Swanson, Chinmay Kulkarni, Nikhil Mungel
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12375v1](http://arxiv.org/abs/2610.12375v1)
- **PDF:** [https://arxiv.org/pdf/2610.12375v1](https://arxiv.org/pdf/2610.12375v1)
- **Categories:** cs.AI, cs.CL, cs.CY, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents are deployed in applications from trip planners and stock trading to IT incident triage. In most cases, LLM agents work autonomously with minimal rule-based safeguarding, leading to cost and safety issues from irreversible actions. Recent works resolve this either by using a safeguard agent to monitor behavior or evaluating logs post-hoc. The first adds cost and latency to every step; the second delivers its verdict after the run, when tokens are burned and damage is done. To overcome this, we propose OnTrack, a streaming monitoring mechanism that compares an agent's steps and dependencies against recorded successful runs to alert users or block the agent in about a millisecond per step. We study this problem in three regimes of decreasing access: full reference access (historical runs and tool schemas), intermediate access (only tool schemas), and no prior knowledge (only step logs as generated). Expectation of OnTrack's monitoring capabilities reduces as data access drops, ranging from plan violation detection to identifying loops, stalls, and repeated tool calls. Finally, we evaluate OnTrack using SWE-bench trajectories. Based on the first 8 steps, our method ranks failing trajectories below succeeding ones better than content similarity approaches (+0.057 AUROC). With an abort policy, we save about 18% of compute that would be burned on failing runs, where 83% of interrupted runs were actually heading to failure (5 out of 6 aborts were correct).

</details>


### 44. Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict

- **Authors:** Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, Jingyu Zhang, Jie Gao, Mark Dredze, Daniel Khashabi
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12360v1](http://arxiv.org/abs/2610.12360v1)
- **PDF:** [https://arxiv.org/pdf/2610.12360v1](https://arxiv.org/pdf/2610.12360v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

When retrieved evidence contradicts an agent's prior beliefs, does it revise its answer, acknowledge uncertainty, or persist with an incorrect conclusion? Existing evaluations of agentic systems focus primarily on task success, offering limited insight into how agents handle such conflicts. We propose to evaluate agents on epistemic humility (EH): the agent's willingness to recognize, act on, and communicate uncertainty during task execution. We operationalize EH through three trajectory-level behavioral dimensions: Identify, Solve, and Escalate (ISE). Through knowledge conflict, situations where the backbone language model's parametric knowledge contradicts the evidence it encounters, or where two contextual sources disagree, we evaluate two conflict settings: (1) controlled conflict and (2) naturally occurring conflict during multi-step agentic execution, each paired with matched no-conflict controls. Evaluating four agents, we find that higher task accuracy does not necessarily correspond to greater epistemic humility: some high-accuracy configurations recognize conflicts during execution but do not communicate unresolved uncertainty in their incorrect final answers. Trajectory-level analysis further reveals that agents frequently detect conflicts in early steps of execution but fail to maintain or resolve them in later steps. Finally, we show that model-level interventions can improve EH, but often at the cost of task accuracy, suggesting that epistemic humility emerges from the interaction among the backbone model, agent harness, and evaluation environment.

</details>


### 45. Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition

- **Authors:** Kaisen Yang, Qingle Liu, Kejin Wang, Yicheng Zhao, Jieming Li, Shenghan Zheng, Ruize Yang, Bojun Yang, Heng Gong, Xiang Gao, Lanyue Zhang, Kaiyu Zhong, Zhuo Liu, Shaoxuan Li, Chengxi Li, Yong Yan, Weixuan Zhang, Tianwei Luo, Situ Wang, Youjie Zheng, Sihan Zhao, Shengyuan Wang, Huan-ang Gao, Jiazheng Xu, Xiaohui Xie, Wentao Han, Hongning Wang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12341v1](http://arxiv.org/abs/2610.12341v1)
- **PDF:** [https://arxiv.org/pdf/2610.12341v1](https://arxiv.org/pdf/2610.12341v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game policies and supporting software while keeping model weights fixed. We introduce AAArena, a benchmark comprising 12 authentic adversarial games and 1,920 archived human programs, with an evaluation protocol modeled on real-world game competitions. Agents interpret rules, choose opponents, analyze replays, and revise game agents to achieve their highest ranking within fixed match and evaluation budgets. We evaluate \val{completedmodels} model and harness configurations: Opus5.5 with Claude Code earns 6 gold medals, while no evaluated configuration tops the remaining 6 human ladders. Performance is generally weaker in games with more complex rule specifications. Further experiments show that opponent selection and dense feedback support policy improvement, and that agents learn from both on-policy replays of their own matches and off-policy replays of other players' matches. These results highlight HL's potential in adversarial games and identify persistent challenges in game understanding, strategy implementation, and long-horizon policy development.

</details>


### 46. Spatial Pattern Formation from Multi-Agent Learning in Public Goods Dilemmas

- **Authors:** Yefei Zhang, Yuxuan Zhao
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12321v1](http://arxiv.org/abs/2610.12321v1)
- **PDF:** [https://arxiv.org/pdf/2610.12321v1](https://arxiv.org/pdf/2610.12321v1)
- **Categories:** cs.MA, cs.GT, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Spatial public goods models show that prescribed movement toward richer locations can generate spatial patterns. We ask how such patterns emerge when agents learn where to move and how learning rates shape their consequences for collective welfare. Fixed populations of cooperators and defectors independently learn movement policies using tabular Q-learning and local observations. Cooperator learning generates clusters around resource peaks, while co-adaptation changes their strength and motion. At a fixed training budget, the largest welfare losses occur when cooperators learn at high rates and defectors at low rates. In part of this regime, learned policies also generate traveling bands supported by a shared directional preference. The conditions supporting travel change with further training, so these patterns reflect training history rather than an established asymptotic outcome. Across the tested learning-rate conditions with cooperator learning, mean collective welfare falls below random movement because increased crowding outweighs gains in resource benefit. Charging agents for the crowding they impose on others during learning recovers much of the welfare loss in the tested conditions. These results connect learning rates to the emergence and welfare costs of spatial organization driven by individual rewards.

</details>


### 47. Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction

- **Authors:** Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12299v1](http://arxiv.org/abs/2610.12299v1)
- **PDF:** [https://arxiv.org/pdf/2610.12299v1](https://arxiv.org/pdf/2610.12299v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent. Real embodied settings often involve multiple agents that act and interact within a shared environment. Existing multi-agent world models rely on coarse actions like locomotion, camera control, or discrete commands, leaving fine-grained embodied interactions underexplored. We formulate multi-agent egocentric world modeling as synchronized ego-stream generation for multiple agents interacting through fine-grained actions in a shared world. This requires cross-view action consistency, shared-environment consistency, and consistent propagation of interaction-induced state updates. We propose Multi-agent Egocentric World Model (ME-World), which jointly denoises multiple ego streams in a shared token sequence, conditions each stream on all agents' target-view poses, and grounds generation with shared environment memory. We train and evaluate on real and synthetic multi-agent data and introduce shared-world consistency metrics for environment, update, and identity consistency. Experiments show ME-World improves shared-world consistency, action control, identity preservation, and video quality over existing methods.

</details>


### 48. DataSense-Bench: The First Step Toward an AI Scientist

- **Authors:** Yudi Zhang, Mingyu Cao, Lu Yin, Mykola Pechenizkiy, Shiwei Liu
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12190v1](http://arxiv.org/abs/2610.12190v1)
- **PDF:** [https://arxiv.org/pdf/2610.12190v1](https://arxiv.org/pdf/2610.12190v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench to study this capability through the fundamental problem of data selection and performance forecasting in machine learning. We ask AI agents to select and rank candidate training subsets that can be used to fine-tune a small LLM model. Agents are allowed to inspect the data, write and execute analysis code, and run model forward passes, but can not train the model or access the actual evaluation tasks. We then fine-tune the base model on each selected subset and evaluate its post-training performance under a standardized protocol. We instantiate the benchmark in terminal problem solving and tool use, selecting trajectories from OpenThoughts-Agent and EnvScaler and evaluating on TBLite and BFCL, respectively. We then evaluate the agents along two complementary dimensions: the post-training performance of the top-ranked subset, reflecting the ability to identify high-value training data, and ranking accuracy, reflecting the ability to predict the relative performance of the selected subsets. In our experiments, selection gains over random selection are limited; agents do not reliably rank their selected groups, and ranking ability does not hold consistently across tasks: Astra identifies the best group in all three tool-use runs but in only one of three terminal runs. Analysis of execution traces on both tasks shows that agents often use similar data signals while interpreting their training value differently.

</details>


### 49. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

- **Authors:** Ming Chen, Rong-Xi Tan, Ke Xue, Yu-Jie Zhou, Taiye Lu, Zhi-Xuan Gao, Peng Xie, Zijun Shen, Chen Lu, Haopu Shang, Chao Qian
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12183v1](http://arxiv.org/abs/2610.12183v1)
- **PDF:** [https://arxiv.org/pdf/2610.12183v1](https://arxiv.org/pdf/2610.12183v1)
- **Categories:** cs.LG, cs.AI, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system configurations, making their results difficult to compare and the effects of individual design choices hard to isolate. We therefore introduce AgenticBBO-Bench, a cross-domain benchmark for agentic BBO spanning synthetic functions, hyperparameter optimization, database tuning, chip design, and molecular design under a unified finite-budget evaluation protocol. In our experiments, agentic BBO achieves higher family-averaged scores than direct LLM-based methods in all five domains and outperforms the best numerical optimizers in four. We further study three factors shaping agent performance: optimization tools, task information and prior knowledge, and the role of the LLM during search. Our results show that additional numerical tools do not consistently improve performance, task semantics are broadly useful while more specific priors are less reliable, and numerical optimizers can effectively absorb gains from search trajectories established by the agent. Finally, we introduce a five-task frontier challenge within AgenticBBO-Bench and evaluate seven LLMs under the Codex agent harness, where GPT-6 Astra and DeepSeek-V4.1-Flash lie on the Pareto frontier of performance and cost among the evaluated models. Our code is available at https://github.com/lamda-bbo/agentic-bbo.

</details>


### 50. Recursive Self-Improvement through Multi-Agent Self-Supervision

- **Authors:** Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Somayeh Sojoudi, Matei Zaharia, Yujin Tang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12176v1](http://arxiv.org/abs/2610.12176v1)
- **PDF:** [https://arxiv.org/pdf/2610.12176v1](https://arxiv.org/pdf/2610.12176v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement (RSI) of a model on non-verifiable tasks, such as open-ended research, faces a supervision bottleneck when its outputs exceed what even human experts can reliably assess, leaving the model itself (optimizee) as the best available optimizer and evaluator. However, a single model instance struggles to critique and improve its own complex reasoning under this homogeneous loop. To address this, we propose Multi-Agent Self-Supervision (MASS), an RSI method that alternates between evolutionary workflow optimization and supervised fine-tuning on self-generated trajectories. Guided by early findings that multi-agent topologies excel at complex reasoning, MASS prompts a single base model to iteratively propose, execute, and self-evaluate multi-agent workflows. Through an evolutionary search constrained by structural guardrails, the model optimizes these computational-graph-like orchestrations, discovering the most effective distinct roles and information routing for a given task. Over two MASS cycles with Qwen3.6-27B, the model achieves 1.2-1.6x higher performance per output tokens on four open-ended public benchmarks. Because the improved model subsequently acts as a better optimizer and evaluator, this alternating framework enables a continuous, recursive bootstrapping of the model's capabilities. Moreover, multi-agent traces are also more training-efficient: a student trained on them outperforms a single-agent student trained on 1.4x more training tokens. These findings suggest that jointly learning orchestration and bounded subagent execution from multi-agent trajectories can provide an effective signal for RSI.

</details>


### 51. OA-MAP: Evidence-Grounded Multi-Agent Multimodal Framework for Interpretable Knee Osteoarthritis Progression

- **Authors:** Sixu Chen, Mingrui Yang, Qiang Guan, Xiaojuan Li
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12134v1](http://arxiv.org/abs/2610.12134v1)
- **PDF:** [https://arxiv.org/pdf/2610.12134v1](https://arxiv.org/pdf/2610.12134v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Knee osteoarthritis (KOA) progression prediction can support patient monitoring, requiring the integration of multimodal data and multidomain expertise. Moreover, isolated risk estimates provide limited insight underlying a prediction. To automate the progression assessment workflow and reduce manual effort while providing interpretable findings and supporting evidence, we present OA-MAP, an autonomous multi-agent framework for evidence-grounded assessment of structural and pain progression in KOA. The system incorporates modality-specific agents including MRI, X-ray, and clinical agents, together with a coordinator agent. This framework can autonomously recruit specialist agents, select tools for prediction and analysis, and retrieve literature as external evidence based on user request and available patient information. An uncertainty-informed human-in-the-loop mechanism enables clinicians to review and correct intermediate findings, triggering recomputation of affected results. We evaluate the prediction models using 600 participants from the FNIH Osteoarthritis Biomarkers Consortium cohort. On the test set of 100 participants, the fusion models achieve AUROCs of 0.80 for structural progression and 0.68 for pain progression. A case study illustrates how OA-MAP combines risk estimates with intermediate findings, cross-modal conflicts, literature support, and uncertainty indicators to support interactive review.

</details>


### 52. Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents

- **Authors:** Xiangyi Zeng, Baihang Liu, Xutong Wang, Ze Jin, Yunpeng Li, Qixu Liu
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.12124v1](http://arxiv.org/abs/2610.12124v1)
- **PDF:** [https://arxiv.org/pdf/2610.12124v1](https://arxiv.org/pdf/2610.12124v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The evolution of Large Language Model agents from single-task execution to long-term autonomous operation highlights the critical challenge of transforming continuous experiences into reusable knowledge. To address this, we propose Hippocam, a hierarchical memory and continual learning architecture. Hippocam draws inspiration from two characteristics of human memory: cognitive processes selectively maintain information relevant to current goals, while long-term memories form gradually through repeated consolidation. Accordingly, Hippocam structures an agent's ongoing work as nested intents. The active context remains centered on the current intent, while completed intents are consolidated into the task-relevant outcomes and state needed for subsequent work, rather than carrying forward their full working details. Concurrently, a recursive prefix consolidation mechanism repeatedly consolidates earlier history, causing long-unused experiences to become increasingly abstract. Original interactions are preserved, allowing the agent to progressively recover finer-grained details through the hierarchy and stop once sufficient information is available. Crucially, when past experiences are recalled and reintegrated into active work, they undergo subsequent consolidation alongside new experiences, thereby being reinforced, supplemented, and updated. Through this memory dynamic of use and disuse, Hippocam connects working context, long-term memory, knowledge accumulation, and skill learning within a single continuously evolving experiential process. This enables agents to learn and evolve capabilities through their own experiences without parameter updates.

</details>


### 53. Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System

- **Authors:** Irene Weber
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11899v1](http://arxiv.org/abs/2610.11899v1)
- **PDF:** [https://arxiv.org/pdf/2610.11899v1](https://arxiv.org/pdf/2610.11899v1)
- **Categories:** cs.CL, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation, workflow, coding agent and AI agent. Whether these labels denote genuine architectural forms or serve as branding has not been assessed systematically.
  In the sources surveyed, labels do carry architectural content, most clearly in vendor usage: copilot denotes a router-worker architecture operating a host application under step-by-step user confirmation, while the more recent shift to the label agent coincides with AI-planned multi-step execution of which the user sees only the outcome. The coding agents of four major providers share one architecture, a reason-and-act loop delegating to subagents.
  This survey describes seven recurring forms---LLM chats, custom agents, retrieval-augmented generation (RAG), AI-enhanced workflows, copilots, coding agents, and, in part, agentic RAG---in a common vocabulary of agents and tools. Each is characterized along four structural dimensions (agentic RAG only partially): the architectural pattern, the control of execution and the point of user intervention, the number of agent calls per task, and tool use. An illustrative corpus of 22 systems from research publications and vendor documentation grounds the descriptions and shows where they reach their limit.

</details>


### 54. Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

- **Authors:** Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11794v1](http://arxiv.org/abs/2610.11794v1)
- **PDF:** [https://arxiv.org/pdf/2610.11794v1](https://arxiv.org/pdf/2610.11794v1)
- **Categories:** cs.AI, cs.CL, cs.CV, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through external memory. The agent maintains a natural-language rulebook as persistent semantic memory, recording revisable hypotheses about environment dynamics while leaving unknown aspects underspecified. It compiles this rulebook into executable code for prediction and planning. Through a continual loop of observation, reflection, rule revision, compilation, and verification, the agent uses prediction errors to refine both the rulebook and its code. Updated code is accepted only when the LLM judges it faithful to the rulebook and cell-exact replay reproduces the observed transitions. We investigate this process as a model-based route to recursive self-improvement (RSI): the agent autonomously explores the environment, revises its world model, and uses verified updates to guide subsequent interaction and learning, while the underlying LLM remains fixed. A population extension maintains multiple world models in parallel, sharing interaction evidence and using their predictions to guide exploration. On ARC-AGI-3, the single-model agent clears every level of all 25 public games, achieves a mean Relative Human Action Efficiency (RHAE) of 100.0, and uses 44% of the human action count. In an Atari Pong case study, a learned feedback controller wins 21:0 in each of three evaluated episodes with different openings, without further LLM calls.

</details>


### 55. Narrow and Deep: An Ontology Tower as the Knowledge of an LLM Agent for an Industrial Equipment System

- **Authors:** Younghwan Joo, Sung-il Kim
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11768v1](http://arxiv.org/abs/2610.11768v1)
- **PDF:** [https://arxiv.org/pdf/2610.11768v1](https://arxiv.org/pdf/2610.11768v1)
- **Categories:** eess.SY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are beginning to operate industrial energy equipment, and what they get right depends on what they are told about the plant. Established building ontologies name many kinds of points across many sites, whereas an industrial equipment system needs few entities with much knowledge about each. This study proposes the ontology tower, a narrow-and-deep ontology of a single equipment system whose knowledge deepens in two ways: through quantities derived from the measured points by physical relations, and through lessons from the operating journal incorporated as knowledge nodes. On a real low-humidity air-handling test plant operated daily through a programmable logic controller, agents received a text projected from its tower in a preregistered evaluation of nine tasks replayed from the plant's records, using four open-weight models from 9 to about 750 billion parameters. This knowledge raised the rate at which the agents avoided the most plausible misjudgment of each task by about 20 percentage points, and the overall task score of the 9-billion-parameter model as much as that of the largest. Operating lessons were used when incorporated into the tower or placed in the prompt as records, but seldom when left in the journal behind a search tool. In live runs through an invariant safety layer, the agents brought the controlled variable into its target band in 12 of 14 runs. An ontology narrow in entities but deep in what is known about them can thus supply the knowledge that an agent for an industrial equipment system needs.

</details>


### 56. TRACE: Diagnosing Verifier Brittleness in Agentic Evaluation

- **Authors:** Radhika Gaonkar
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11678v1](http://arxiv.org/abs/2610.11678v1)
- **PDF:** [https://arxiv.org/pdf/2610.11678v1](https://arxiv.org/pdf/2610.11678v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Verifier scores now serve as both benchmark metrics and training rewards for large language model (LLM) agents, and a change in score is routinely read as a change in capability. It may instead reflect a change in the evaluation. We introduce TRACE, a protocol that turns a score change from a verdict into a testable diagnosis: it applies a targeted change to one part of an evaluation, compares paired runs, checks whether the agent's behavior changed, and rescores unchanged trajectories to test whether the scoring rule is responsible. In a controlled suite of 25 synthetic tasks, renaming tools lowers a scripted agent's score by 0.250 even though it performs exactly the same operations; restoring the original names at scoring time closes the entire gap, while the same mutation exposes a genuine behavioral failure in a second agent. On public $τ^2$-bench tasks with four LLM agents, an initial 30-task study finds mixed reward changes whose one clear effect does not replicate. In a larger follow-up on 88 new tasks with repeated runs per condition, renaming tools or reformatting tool outputs leaves reward unchanged to within $\pm$0.10 for seven of eight agent-change pairs, whereas tool names that deliberately mislead lower every agent's reward by 0.20-0.44, showing that the setup can detect real effects. Identical reruns flip 15-36% of task outcomes, so single-run comparisons cannot separate presentation effects from run-to-run variation. Two frontier LLM judges give consistent verdicts when a fixed trajectory is presented differently, yet disagree with each other on 57% of the same records, largely because one grades procedure rather than outcome. TRACE thus separates what a score change says about the agent from what it says about the measurement.

</details>


### 57. Harness Evolution Hits a Ceiling: When Weight Training Should Begin

- **Authors:** Yuan Tian, Bing Hu, Hao Wang, Binghang Lu, Fang Wu
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11655v1](http://arxiv.org/abs/2610.11655v1)
- **PDF:** [https://arxiv.org/pdf/2610.11655v1](https://arxiv.org/pdf/2610.11655v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Improving a long-horizon LLM agent means evolving the harness around a frozen model or training its weights. We let a self-evolving harness make the system stronger first, then cross seed and evolved harnesses with base and trained weights to learn which gains the trained model keeps and which still need the runtime. We show that the right lever can be read off the agent's failure composition: labelling failed trajectories by the first signal that fires separates process failures (blocked calls, loops, exhausted step budgets) from content failures (a delivered plan that is poor). Harness evolution repairs the former, the behaviour it instils can be trained into the weights, and content failures are what weight training is for. On DeepPlanning, a self-evolving harness loop lifts the held-out score of Qwen3.5-4B from 0.16 to 0.30 and of Qwen3.5-9B from 0.32 to 0.44; for 4B, held-out delivery rises from 55% to 90% while content failures are left for the weights. LoRA adapters trained on evolved-harness trajectories internalise the gain: under the original harness they add +0.13 on held-out tasks for both sizes; on 4B they stack with the harness to more than double the held-out score, and on 9B the adapter alone matches the full evolution line, cutting content failures from a quarter of trajectories to one in twenty. A placebo adapter trained on answer-shuffled trajectories falls below the base model. The loop transfers to WebArena-Lite (+0.09 on 117 unseen tasks), where the gain lives in what the model sees and adapters do not add to it. The result is a diagnose-then-intervene rule applied twice: read the failure composition to choose between harness and weights, then read what the accepted edits changed to decide which gains to train in. Scores are four-rollout means against fresh anchors, same-night except where marked, across eight models from six families and two benchmarks.

</details>


### 58. Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems

- **Authors:** Jiaqi Liao, Yuanzhao Zhai, Huanxi Liu, Xu Zhang, Zheming Zhuang, Dawei Feng, Bo Ding, Huaimin Wang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11600v1](http://arxiv.org/abs/2610.11600v1)
- **PDF:** [https://arxiv.org/pdf/2610.11600v1](https://arxiv.org/pdf/2610.11600v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MASs) are increasingly used to solve complex tasks through coordinated reasoning, tool use, and interaction with external resources. However, attributing failures in such systems remains challenging because the observed outcome often does not directly reveal the error responsible for the failed execution. In this work, the attribution target is the decisive error, defined as the agent--step pair whose correction would recover the failed execution. Existing approaches largely identify suspicious steps without explicitly modeling how errors propagate across interactions or persist in unresolved loops, making decisive errors difficult to distinguish from downstream failure symptoms. We propose \textbf{E}rror-Propagation \textbf{M}odeling for \textbf{F}ailure \textbf{A}ttribution (\textbf{EMFA}). EMFA constructs a structured representation of the failed trajectory, models both cascading propagation and persistent interaction loops, and uses propagation-aware candidate screening followed by counterfactual verification to identify the decisive agent--step pair. On the Who\&When benchmark, EMFA achieves state-of-the-art step-level attribution accuracy and remains competitive at the agent level. It improves the previous best step-level results by 3.45 and 4.40 percentage points on the Hand-Crafted and Algorithm-Generated subsets, respectively.

</details>


### 59. Memory Type Varies: Empowering LLM Agents for Long-Term Memory with Diverse Strategies

- **Authors:** Yi Wen, Derong Xu, Pengyue Jia, Yichao Wang, Yingyi Zhang, Maolin Wang, Junyi Li, Wenlin Zhang, Xiaopeng Li, Yong Liu, Xiangyu Zhao
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11573v1](http://arxiv.org/abs/2610.11573v1)
- **PDF:** [https://arxiv.org/pdf/2610.11573v1](https://arxiv.org/pdf/2610.11573v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The memory capabilities of Large Language Models (LLMs) have garnered increasing attention recently. Despite great success achieved, existing retrieval-based memory approaches typically overlook the differences between memories and employ a unified strategy to process all memories, leading to suboptimal performance. Thus, an intuitive question arises: can we categorize memory into different types and select appropriate strategies? However, given the topic-rich, scenario-complex, and boundary-blurred nature of memory scenarios, achieving precise classification of memories is not easy. To address this challenge, we propose a memory multi-class dataset in this paper, termed TriMEM, which provides precise annotations for memory types across diverse scenarios. Building upon this foundation, we propose a novel memory framework, named MemoType, which can adaptively recognize each memory and query type with the learned router model. With the memory and query routing, MemoType can retrieve the memory with corresponding query types and design tailored retrieval strategies, thereby enhancing the retrieval performance. Moreover, we theoretically prove that any single retrieval strategy is subject to a fundamental upper bound on its expected retrieval precision in multi-class corpora, leading to systematic precision degradation. Extensive experiments on three datasets demonstrate that MemoType consistently outperforms existing methods, achieving up to 16.18% improvement in Recall@1.

</details>


### 60. SWE-Journey: Towards More Realistic Evaluation of Coding Assistants through Long-Horizon, Multi-Turn Interaction

- **Authors:** Hexuan Deng, Yue Wang, Wenyu Jiang, Cheng Yang, Haolin Yang, Zhaohua Zhang, Chenchen Zhao, Beiduo Chen, Muxi Chen, Sa Zhu, Geyuan Zhu, Jianhuan Zhuo, Qiuyong Xiao, Tianwen Jiang, Jihong Zhang, Xuebo Liu
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11559v1](http://arxiv.org/abs/2610.11559v1)
- **PDF:** [https://arxiv.org/pdf/2610.11559v1](https://arxiv.org/pdf/2610.11559v1)
- **Categories:** cs.CL, cs.AI, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding assistants such as Claude Code and Codex have become a major application of LLM agents, yet existing benchmarks remain far from real-world use, particularly in task horizon and interaction length. Code assistants require completing long chains of development work in continuously evolving repositories, while repeatedly clarifying requirements and adapting implementations through multi-turn interaction. To address these gaps, we introduce SWE-Journey, a benchmark for more realistic evaluation of coding assistants. To address the task-horizon gap, we propose a weak-to-strong synthesis pipeline that automatically constructs long-horizon coding tasks. To address the interaction gap, we mine four representative user personas from real interaction data and build a user-simulation agent to reproduce realistic code-assistance interactions. On average, models pass over 75% of tests for requested functionality with software architects, but fewer than 25% with non-coders. These results show that current coding assistants still fall short of enabling reliable coding for non-coders. We further analyze the reasons for this gap and identify asking right, finding right, and fixing right as key capabilities during interaction.

</details>


### 61. Safe, Persistent, and Evolving Agent Harness for Understanding Partially Observable Worlds

- **Authors:** Yisen Gao, Yue Guo, Qing Zong, Yiwen Guo, Yangqiu Song
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11552v1](http://arxiv.org/abs/2610.11552v1)
- **PDF:** [https://arxiv.org/pdf/2610.11552v1](https://arxiv.org/pdf/2610.11552v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents can invoke tools fluently, but enterprise workflows demand more than selecting the right tools: actions must strictly comply with organizational policies, tool feedback often conceals hidden side effects under partial observability, and long-horizon tasks require persistent state tracking across multiple records. To address these challenges, we introduce E-Ledger, a multi-agent harness for safe and persistent execution. E-Ledger employs a code approval layer that checks every proposed action against policy before execution, and maintains a world ledger of verified hidden rules alongside evidence-backed dynamic state. Because hidden rules are typically unknown a priori, we further propose WorldAbduct, an abductive, world-model-driven harness evolution framework. WorldAbduct diagnoses execution trajectories across four complementary views (state consistency, world-observation gap, policy-gate correctness, and goal judgment) to hypothesize latent rules, and verifies them through targeted abductive interactions before integrating them into the ledger. On the enterprise benchmark World of Workflows, E-Ledger with WorldAbduct improves safe task completion across four LLM backbones, outperforming the strongest evolution baseline by 5--15 percentage points. Experiments in ScienceWorld and DiscoveryWorld further show that abductive harness evolution carries over to scientific environments. Our code is available at https://github.com/HKUST-KnowComp/E-LEDGER-WorldAbduct.

</details>


### 62. Constitutional Gating and Deterministic Recovery for Multi-Agent LLM Negotiation: Ablations Against a Stateful Adversarial Gatekeeper

- **Authors:** Masaaki Nakatsu, Reno Wang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11542v2](http://arxiv.org/abs/2610.11542v2)
- **PDF:** [https://arxiv.org/pdf/2610.11542v2](https://arxiv.org/pdf/2610.11542v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems negotiating with a stateful counterpart waste model calls in three ways: polite loops that never meet the counterpart's hidden acceptance condition, malformed outputs that trigger retries, and compliance deadlocks in which the counterpart demands something the agent must refuse. We study a three-part control stack - a 5-Pillar runtime constitution, a 4-tier swarm (Director, three-agent majority vote, Monitor, schema hard gate) and Cognitive Annealing (deterministic deadlock detection, atomic purge of the agent-side context, a canonical recovery message) - against a released adversarial Gatekeeper whose acceptance rules are fixed regular expressions and whose LLM only renders reply text. The testbed has a known solution: it measures whether the stack executes a constitution-aligned strategy against swarm drift and recovers from deadlock, not whether it discovers anything. In five runs per configuration (30 runs; Gemini 2.5 Pro agents, Claude Haiku 4.5 Gatekeeper) we find: (i) the constitution and Director make an acceptable framing possible but not reliable - 0/5 baseline unlocks versus 1/5 and 2/5 with the constitution; when the swarm unlocks it does so in one turn with 7-8 calls and about 15k tokens (67-73% below baseline); when it does not, it costs 17-38% more; (ii) the Monitor and hard gate do not reduce unlocks and leave an audit trail; (iii) under a honeytrap-to-compliance deadlock, LLM-only steering escapes 0 of 5 times while atomic purge plus a canonical strike escapes 5 of 5 (Fisher $p = 0.008$) at the same call budget, with zero calls for the strike. LLM-written strikes failed the deterministic pre-flight 5 of 5 times although an LLM Monitor had approved four. Pre-registered hypotheses on average call and token reduction were not supported. Cost is bounded in every arm by deterministic stop rules; the stack adds recovery at no extra model cost.

</details>


### 63. Evaluating Local Language Model Agents for Reproducible Data Engineering: An Empirical Software Engineering Study of Mobility Workflows

- **Authors:** Jorge García-Carrasco, Javier Sanchis, Alejandro Reina-Reina, Alejandro Maté, Juan Trujillo
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11482v1](http://arxiv.org/abs/2610.11482v1)
- **PDF:** [https://arxiv.org/pdf/2610.11482v1](https://arxiv.org/pdf/2610.11482v1)
- **Categories:** cs.SE, cs.AI, cs.DB, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Context: Large language model (LLM) agents are increasingly used as software and data-engineering assistants, yet evidence about locally deployable open-weight agents remains limited. Existing evaluations often emphasize textual responses or isolated code generation rather than the validity of complete engineering artifacts.
  Objectives: We evaluate whether local LLM agents can produce correct and reproducible data-engineering artifacts, quantify the effect of a closed-loop workspace condition, and examine trade-offs in model scale, architecture, quantization, runtime, tool use, and failure.
  Methods: We introduce a benchmark of fifteen mobility-workflow tasks covering data discovery, connectors, transport-feed processing, semantic enrichment, feature engineering, validation, visualization, and reporting. Deterministic checkers assess generated scripts, tables, structured files, figures, and reports. Ten local configurations are evaluated in one-shot and closed-loop conditions, with five repetitions per model, mode, and task, yielding 1,500 scored attempts on a consumer-grade GPU.
  Results: Among models larger than two billion parameters, the workspace condition increases pass rates by 26.7-52.0 percentage points over one-shot generation. The strongest configuration reaches 85.3% artifact-level success, and a quantized 9-billion-parameter model reaches 69.3% with an approximately 6.5 GB memory footprint. Gains are largest when intermediate artifacts expose errors the agent can inspect and repair.
  Conclusion: Local open-weight agents can support a meaningful subset of software-intensive data-engineering work, but reliability depends on model capability, task verifiability, and deterministic validation. The benchmark provides a reproducible method for evaluating complete agent configurations before adoption in engineering workflows.

</details>


### 64. GROB: A Multi-Agent Architecture for Public-Trace Investigation of Candidate Agentic Activity

- **Authors:** Chiara Bonfanti, Cataldo Basile
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11467v1](http://arxiv.org/abs/2610.11467v1)
- **PDF:** [https://arxiv.org/pdf/2610.11467v1](https://arxiv.org/pdf/2610.11467v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present GROB, a multi-agent architecture for investigating candidate autonomous-agent activity through public Internet traces when privileged telemetry is unavailable. The system performs controlled, read-only collection of public traces and preserves selected observations for later resolution. In a frozen September 2026 corpus, several collected traces became more informative as additional public evidence emerged. The strongest result concerns Census-labelled identifiers captured on 9 September. Public revision records later resolved these identifiers to specific Census requests from 16 - 17 June. Other results show weaker links between traces collected by GROB and evidence reconstructed or reported later. These links vary in strength, and only some can be tied to specific public records. The results show that sparse public traces can remain useful even before their significance is fully understood. Such evidence can support later reconstruction, but public traces alone do not establish organizational attribution. Execution identity presents a separate problem, as continuity of agent identity remains an active research question for autonomous language-model agents.

</details>


### 65. Closed-loop evaluation of LLM agents for embedded software development

- **Authors:** Jorge García-Carrasco, Sergio García-Carrasco, Alejandro Maté, Juan Trujillo
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11447v1](http://arxiv.org/abs/2610.11447v1)
- **PDF:** [https://arxiv.org/pdf/2610.11447v1](https://arxiv.org/pdf/2610.11447v1)
- **Categories:** cs.SE, cs.AI, cs.AR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as coding agents that edit files, run builds and tests, inspect execution results, and repair software iteratively. Embedded firmware is a demanding target because correctness depends on closed-loop behavior under sensing, timing, and safety constraints, not only on static source quality. Yet embedded-agent evaluation remains limited and often emphasizes one-shot synthesis or offline correctness.
  We present a benchmark for closed-loop evaluation of embedded coding agents. Each task provides a plain-text engineering description, constrained workspace, and visible build-and-runtime surface. The agent must translate requirements into implementation and self-verification steps, then iterate until the required device behavior is achieved. The suite contains five embedded-control tasks and four feedback scenarios: one-shot generation, realistic self-verification, CI-style red/green feedback, and oracle-style detailed feedback.
  The implementation targets simulated ESP32 firmware for reproducibility. We evaluate seven GPT-family and Qwen-family configurations across five tasks and four scenarios, with three repetitions per condition for 420 runs. gpt-5.4 has the highest pass rate among evaluated configurations but does not saturate the benchmark; qwen3.5-27B is the strongest observed local model; and smaller local models degrade sharply in pass rate and search efficiency. These results suggest that capable local embedded coding agents are emerging.

</details>


### 66. An Embodied Multiagent Framework Based on Token Communications for Cooperative ISAC

- **Authors:** Jiahe Guo, Jun Du, Chunxiao Jiang, Jintao Wang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11434v1](http://arxiv.org/abs/2610.11434v1)
- **PDF:** [https://arxiv.org/pdf/2610.11434v1](https://arxiv.org/pdf/2610.11434v1)
- **Categories:** eess.SP, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The emerging low-altitude economy demands unmanned aerial vehicle (UAV)-enabled integrated sensing and communication (ISAC) for reliable connectivity and environmental awareness. In particular, embodied UAV agents offer a promising means of supporting autonomous operations through a closed loop linking perception, decision-making, and physical actions. However, each UAV has access only to local observations, and effective cooperation requires exchanging local states and intentions. Directly sharing such information can incur substantial signaling overhead and hinder timely coordination in dynamic environments. To deal with this problem, this paper investigates a cooperative ISAC network of embodied UAV agents and formulates a joint token communications (TokCom) and physical control problem to minimize total propulsion energy subject to communication and sensing rate requirements. Then, we propose a state--intent TokCom (SI-TokCom) framework driven by multi-agent embodied policy learning. Specifically, separate pretrained codebooks enable compact exchanges of local states and intentions, while UAV agents jointly learn to select and compose tokens and determine physical actions based on local observations and received tokens. Simulation results show that SI-TokCom achieves 98.9\% and 99.1\% of the centralized baseline's communication and sensing rates, respectively. Compared with the local baseline, it improves the corresponding rates by 5.0\% and 43.6\%, respectively, with essentially unchanged propulsion energy. These results highlight the potential of TokCom for communication-efficient cooperation among embodied UAV agents in ISAC systems.

</details>


### 67. Personalization Matters: Long-Horizon Conversation Agent with User-Centric Information in Online Shopping Interactions

- **Authors:** Rena Gao, Yue Dai, Hao Guan, Shengxiang Gao, Wangyang Wu, Yixin Shen, Jey Han Lau
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11375v1](http://arxiv.org/abs/2610.11375v1)
- **PDF:** [https://arxiv.org/pdf/2610.11375v1](https://arxiv.org/pdf/2610.11375v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personalized conversational shopping requires maintaining preference consistency over multi-turn interactions, where users reveal constraints gradually. Existing approaches often rely on static profiles and do not explicitly control long-horizon interaction behavior. We propose a multi-agent, multimodal Retrieval-Augmented Generation (RAG) framework that decomposes dialogue state tracking, recommendation retrieval, preference-aware reasoning, and response generation, while integrating product metadata, product reviews, image-derived descriptions, and user historical reviews. To evaluate interaction-level quality, we adopt a trajectory-level protocol with four dimensions: Global Preference Consistency, Cumulative Information Synthesis, Interaction Trajectory, and Tone Consistency. On an Amazon Reviews 2023 benchmark, retrieval-enabled variants outperform a no-RAG baseline on automatic trajectory metrics (average 4.82 vs. 3.74). In a small real-user study ($n{=}5$), the Full variant achieves the highest mean overall rating (4.60 vs. 2.20 for Baseline), providing exploratory evidence that role decomposition plus user-centric retrieval improves perceived personalization.\footnote{Code and dataset are available at: https://github.com/RenaGao/Multimodel_RAG_Indexing

</details>


### 68. RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees

- **Authors:** Meghanadh Pulivarthi, Swaraj Kumar Biswal, Kushagra Bhushan, Yatin Nandwani, Sachindra Joshi, Dinesh Raghu
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11370v1](http://arxiv.org/abs/2610.11370v1)
- **PDF:** [https://arxiv.org/pdf/2610.11370v1](https://arxiv.org/pdf/2610.11370v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Retrieval-augmented generation (RAG) grounds language models in external corpora. Agentic RAG enables iterative search, yet exposes the model to isolated chunks without document structure, making it difficult to distinguish relevant evidence from chunks that merely resemble the query. Structure-aware methods such as PageIndex navigate document structure but cannot scale to the structures of large corpora, which do not fit in the LLM context. Hence, they first commit to a single document using a document retriever and cannot recover from a wrong choice. We propose RIT-RAG (Retrieval-Induced Tree RAG), which combines content retrieval with structural navigation. Offline, RIT-RAG builds a tree for each document from its table of contents or sitemap. At query time, it retrieves a broad set of chunks and uses their positions to induce manageable sub-trees, potentially across multiple documents. An LLM agent navigates these sub-trees, selectively reads promising nodes, and reformulates queries when needed. Thus, retrieval proposes where to look, while the agent decides what to read. Across financial, scientific, and customer-support benchmarks, RIT-RAG achieves the highest answer accuracy among vanilla, graph-based, and agentic baselines. On EntQABench, our new benchmark of 2.84 million technical-documentation webpages, it improves accuracy by 6.8 to 11.4 points over the strongest baseline across three LLMs.

</details>


### 69. SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning

- **Authors:** Wei Yang, Shawn Li, Yuehan Qin, Yawei Wang, Mingxi Wang, Shixuan Li, Tiankai Yang, Jiate Li, Jesse Thomason, Xuezhe Ma, Yue Zhao
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11345v1](http://arxiv.org/abs/2610.11345v1)
- **PDF:** [https://arxiv.org/pdf/2610.11345v1](https://arxiv.org/pdf/2610.11345v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-evolving LLM agents promise to improve autonomously through continual interaction and learning, reducing their dependence on manually curated supervision. Realizing this promise requires not only updating the agent, but also evolving its training experience as its capabilities change. However, most existing pipelines rely on static datasets or separately updated synthesis models, causing previously useful tasks to become trivial while overly difficult tasks remain uninformative. This growing mismatch between agent capability and training experience limits sustained self-improvement. To address this problem, we propose SynCo, an agentic data synthesis co-training framework for self-evolving LLMs based on multi-agent reinforcement learning. SynCo jointly optimizes two independently parameterized agents: a Synthesizer that constructs training tasks from the Reasoner's evolving capability state, and a Reasoner that learns from the resulting experience. Each synthesized task induces multiple Reasoner rollouts whose outcomes provide complementary rewards to both agents. Correctness feedback improves the Reasoner, while task quality, answer reliability, and outcome-grounded teachability guide the Synthesizer. Their updates are fed back into subsequent synthesis rounds, allowing the task-solving policy and its training distribution to evolve together. Extensive experiments across eight mathematical reasoning benchmarks demonstrate that SynCo substantially outperforms a broad range of existing synthetic-data methods and controlled baselines, achieving the strongest overall performance while deriving most of its gains from previously unsolved problems.

</details>


### 70. EvoSim: Learning to Model, Modeling to Learn

- **Authors:** Yun-Wei Song, Jinkai Tao, Jun-Dong Zhang, Rui Zhang, Yi-Min Wu, Qiang Zhang
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11344v1](http://arxiv.org/abs/2610.11344v1)
- **PDF:** [https://arxiv.org/pdf/2610.11344v1](https://arxiv.org/pdf/2610.11344v1)
- **Categories:** cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Physics-based models connect scientific explanation with quantitative prediction. Constructing them requires selecting physical processes, defining states and governing equations, specifying couplings, and identifying parameters from experiments. Existing AI systems remain limited in making these model structure decisions autonomously. We introduce EvoSim, a self-evolving AI scientist for physical modeling. It uses experimental discrepancies to drive mechanism and equation revisions and held-out experimental data to test physical plausibility. Exploration traces make updates to knowledge, skills, and multi-agent orchestration. This co-evolution improves physics-based models and EvoSim's ability to select mechanisms, diagnose failures, and coordinate research. We evaluate EvoSim on two industrial battery modeling tasks. It predicts lithium-metal-plating onset from 25 to 45 degrees Celsius and 2 C to 6 C with a mean absolute error of 1.79% in state of charge. Dynamic voltage prediction under vehicle driving conditions achieves a root mean square error of 7.62 mV, surpassing the reported accuracy of models developed by human experts. Self-evolution reduces model and physics errors by approximately 36% relative to baseline, demonstrating improved scientific modeling capability. EvoSim turns experimental observations into validated models and cumulative research expertise.

</details>


### 71. MedBenchAgent: Towards Systematic Automation of Medical VLM Benchmark Construction

- **Authors:** Yulin Fu, Junren Wang, Guangjing Yang, Zhangyuan Yu, Wanran Sun, Jiabao Zhou, Jin Yin, Qicheng Lao
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11312v1](http://arxiv.org/abs/2610.11312v1)
- **PDF:** [https://arxiv.org/pdf/2610.11312v1](https://arxiv.org/pdf/2610.11312v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large-scale construction of medical vision-language model (VLM) benchmarks is increasingly feasible with richly annotated imaging datasets and large language models (LLMs), yet existing automation largely focuses on generating evaluation items within predefined benchmark specifications. We study the broader problem of automatically deriving the specification itself: what to evaluate, which annotations support each task, and how to translate this evidence into reliable evaluation items. We formulate benchmark construction as constrained compilation, in which the benchmark specification is progressively derived from evaluation requirements, heterogeneous annotations, and medical knowledge. Based on this formulation, we introduce MedBenchAgent, a multi-agent framework with a Benchmark Intermediate Representation (BIR) that encodes task definitions, evidence mappings, evaluation protocols, and item specifications across construction stages. MedBenchAgent separates planning, which derives and verifies the specification, from instantiation, which constructs and audits items under the locked specification. MedBenchAgent achieves a Task-Space F1 of 90.9%, outperforming direct task induction (79.2-80.0%) and prior-guided induction (85.1%); 994 of 1,000 sampled items from correctly identified tasks pass human audit. We further demonstrate portability to a specialized medical domain and evaluate twelve VLMs, revealing task- and setting-specific variation obscured by aggregate scores. These results establish constrained compilation as a scalable and auditable framework for medical VLM benchmark construction beyond question generation.

</details>


### 72. DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration

- **Authors:** Yingda Shen, Yuxiang Wang, Kunyu Feng, Qinke Ni, Jiaqi Li, Minghao Hsu, Junan Zhang, Dekun Chen, Yutong Bian, Zhizheng Wu
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11299v1](http://arxiv.org/abs/2610.11299v1)
- **PDF:** [https://arxiv.org/pdf/2610.11299v1](https://arxiv.org/pdf/2610.11299v1)
- **Categories:** cs.AI, cs.SD


> Summary unavailable.


<details>
<summary>Abstract</summary>

Voice agents are converging on a collaboration pattern: a full-duplex interaction model stays on the live channel as the entry to the conversation, while search, reasoning, and coding are handled through asynchronous delegation. A duplex model supports continuous listening and speaking, but complex reasoning and tool use may exceed its capabilities. A coding agent can plan and execute extended tasks, but its sequential interface is a poor fit for live conversation. Combining them requires a harness that coordinates task acceptance, progress, cancellation, replacement, and result delivery while keeping the conversation responsive. Existing harnesses often rely on coupled heuristics, making them difficult to improve systematically from evidence. We present DuplexAgent, a full-duplex collaboration system whose harness expresses this workflow as six editable modules, and Duplex-Harness-RSI, a closed loop that revises them from interaction traces. A simulator automatically generates timed test conversations, runs the system, and produces failure traces that identify the collaboration modules requiring repair. Reasoning LLMs and coding agents in the delegation pool also serve the improvement loop: the Exam Planner selects the next tests from observed weaknesses and the repair archive, and the Harness Editor proposes targeted module changes. The capabilities that serve the user thus also improve the system's coordination. Experiments on intelligence, agentic, and duplex benchmarks show that DuplexAgent combines continuous interaction with difficult reasoning and complex task execution, achieving stronger spoken-knowledge and executable-tool scores than the compared delegated systems while maintaining strong interruption response. A harness ablation further shows that this modular, verifiable loop outperforms the initial harness and repeated editing that lacks its diagnosis and repair archive.

</details>


### 73. What to Admit and How to Present: Governing Persistent Memory in LLM Agents

- **Authors:** Chang Liu, Deliang Ding
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11188v1](http://arxiv.org/abs/2610.11188v1)
- **PDF:** [https://arxiv.org/pdf/2610.11188v1](https://arxiv.org/pdf/2610.11188v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persistent memory can improve personalization in LLM agents but can also induce sycophancy and cross-domain leakage. We distinguish two governance decisions: admission, which determines what recalled information enters the working context, and presentation, which determines how admitted information is expressed. We implement two inference-time designs without retraining: factor-compiled admission (FC), which assesses whole memory entries, and permission-semantic admission (PS), which decomposes entries into typed units; both translate adjudicated attributes into eligibility decisions via deterministic policies. We evaluate on a four-backbone development suite and an external benchmark with four tasks of 300 samples each. Relative to verbatim injection, FC and PS reduce pooled judge-assessed failure rates on the external benchmark by 6.7 and 8.8 percentage points (p = 2.7e-7 and 4.1e-12), and development-set cross-domain leakage falls by up to 29.5 percentage points. A query-conditioned gating baseline shows no significant change in objective-fact failure or pooled failure. Under matched admission budgets, PS outperforms random and relevance-based selection on external objective-fact judgment after Holm correction. Holding presentation fixed, tightening admission cuts cross-domain failure by a further 17.5 percentage points (p = 1.6e-4); in contrast, no comparison between two renderings of identical adjudicated outputs survives multiple-comparison correction. Both designs increase personalization failures, and PS misses the preregistered improvement and personalization-preservation criteria. These results support evaluating admission and presentation separately: selection quality provides task-specific safety gains, while preserving beneficial memory use remains unresolved.

</details>


### 74. VAMR: Multi-Question Agentic Reasoning for Efficient Long-Form Video Understanding

- **Authors:** Runquan Gui, Hanzhu Chen, Zehao Wang, Hanxin Zhu, Xin Li, Zhibo Chen
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11171v1](http://arxiv.org/abs/2610.11171v1)
- **PDF:** [https://arxiv.org/pdf/2610.11171v1](https://arxiv.org/pdf/2610.11171v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-form video understanding often involves multiple questions about different aspects of the same recording. Yet existing video agents typically process each question through an isolated tool-use trajectory. This repeatedly restarts video exploration and memory construction, missing opportunities to acquire evidence jointly and progressively build a shared understanding that supports the complete question set. We introduce \textbf{VAMR} (\textbf{V}ideo \textbf{A}gent for \textbf{M}ulti-Question \textbf{R}easoning), which coordinates all questions about a video through one shared tool-use trajectory. At each round, a persistent policy model can invoke tools for one or more unresolved questions and submit answers for questions with sufficient evidence. Question-conditioned visual perception retrieves fine-grained clues for several questions in one call, while layered multi-question memory integrates reusable context into a shared video story and preserves separate evidence for individual questions. After supervised fine-tuning initializes this interaction protocol, we propose question-horizon policy optimization (\qhpo) to optimize shared trajectories in which questions progress and finish at different rounds. Specifically, a question-level critic estimates the value of each active question, while round alignment maps each question advantage to the rounds that directly serve it before the aligned advantages are aggregated to optimize the shared actor. Across LVBench, Video-Holmes, and LongVideoBench, VAMR achieves the highest accuracy overall and the fewest reasoning rounds among iterative methods. On LVBench, it reaches 62.1\% accuracy, exceeding VideoARM by \textbf{4.3} points while reducing reasoning rounds and processed frames by \textbf{85.9\%} and \textbf{61.4\%}.

</details>


### 75. Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning

- **Authors:** Minchan Kwon, Seunghee Koh, Sunghyun Baek, Minsung Bae, Junmo Kim
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11152v1](http://arxiv.org/abs/2610.11152v1)
- **PDF:** [https://arxiv.org/pdf/2610.11152v1](https://arxiv.org/pdf/2610.11152v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters. This process is often described as in-context reinforcement learning (ICRL). Whether in-context learning (ICL) can actually play the role of RL, however, has not been tested. We study this question in its simplest form, direct ICRL, where the model conditions directly on raw trajectory-reward pairs, and ask whether the reward acts as a learning signal. Through controlled experiments on four benchmarks across six models, we find that the reward is read, but its effect is small: flipping, randomizing, or removing the reward leaves the improvement curve almost unchanged, and this holds even under meta-prompts that explicitly instruct the model to explore, exploit, or reason over rewards. Trajectories drive improvement, but not through their semantic content: shuffled or corrupted trajectories work as well as real ones. These patterns closely mirror those known in ICL, suggesting that direct ICRL is better understood as a special case of ICL than as inference-time RL. This reframing has implications for agent memory design: ICL factors such as input distribution and demonstrations may matter more than RL elements such as reward shaping and exploration.

</details>


### 76. The "10th Juror": Open-Set Standpoint Screening for Bureaucratic Bias Detection

- **Authors:** Yuchen Miao, Zijun Wang, Chang Han, Yurui Shi, Mingtai Zhang, Siyang Xu
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11136v1](http://arxiv.org/abs/2610.11136v1)
- **PDF:** [https://arxiv.org/pdf/2610.11136v1](https://arxiv.org/pdf/2610.11136v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Presupposing the boundaries of bias is itself a form of bias. We study closed-loop bias governance for Dutch government documents, where a system must detect biased language, ground decisions in legal and contextual evidence, rewrite problematic sentences when intervention is warranted, and verify that the rewrite mitigates harm without distorting meaning. Existing methods face three challenges: (i) discriminative classifiers capture surface regularities but lack normative grounding; (ii) zero-shot LLMs often adopt generic viewpoints and over-flag ambiguous administrative language; and (iii) fixed taxonomies inherit the Closed-World Assumption, missing emerging local targets. We propose MARS-Gov, a standpoint-aware multi-agent framework that combines legal retrieval, open-set target screening, specialized jurors, conservative routing, and rewrite verification. When screening finds an uncovered group, MARS-Gov instantiates a dynamic "10th juror" to deliberate outside the fixed panel. On DGDB, MARS-Gov sets a new SOTA with 0.880 F1, outperforming the strongest zero-shot LLM detector by 20.2 points (29.8% relative) and the best supervised Dutch encoder by 6.8 points, while reducing unnecessary interventions to 2.5%. Leave-One-Category-Out (LOCO) evaluation recovers held-out categories with 85.1% Correct@1 and 93.8% Correct@3.

</details>


### 77. When Interfaces Speak: Data-Aware Generative UI Harness for Active Interaction

- **Authors:** Xiaolong Li, Xiaohan Xu, Jinyang Li, Xinnuo Xu, Ge Qu, Nan Huo, Jack Williams, Reynold Cheng
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11123v1](http://arxiv.org/abs/2610.11123v1)
- **PDF:** [https://arxiv.org/pdf/2610.11123v1](https://arxiv.org/pdf/2610.11123v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most human-agent interaction today remains text-based. Natural language can impose cognitive overload, ambiguity, information chaos, and slow input for complex tasks; ephemeral generative UIs can present structured information and guide users toward task completion. We propose GenUI-Harness, a multi-agent harness pairing a Tool Agent for information retrieval and task execution with a GUI Coder Agent that identifies ambiguities and generates front-end code for structured interfaces. Training the coder with reinforcement learning is challenging: verifiable rewards for interactive UI generation require costly execution, while LLM-as-a-Judge rewards are prone to reward hacking. We address the first challenge with Dynamic UX, a lightweight package for dynamic interaction and reward collection in a single sandbox, and the second with Reward Auditor, a meta-reward mechanism that monitors reward distributions and distills diagnostic patterns into a shared rubric and scoring specification. We introduce UI-TAU Bench, a benchmark for active human-agent interaction through generated UI code, built on 10 real-world domain databases constructed from public data sources and based on Tau-Bench tool-use settings, with Lite (300 tasks) and Full (1,000 tasks) splits. GenUI-Harness achieves an average Pass@3 gain of 4.48 percentage points over smolagents on Lite. Training with GenUI-Harness improves a 4B backbone from 9.33% to 58.00% Pass@3, outperforming larger frontier models such as Claude Opus 5 (46.67%). GenUI-Harness also remains robust on ambiguous and non-ambiguous queries. In a reviewer survey comparing communication channels, generated UIs reduce average dialogue rounds from 3.4 to 1.2. These results show that data-aware generative interfaces can support effective task completion and reduce dialogue rounds in evaluated database-backed workflows.

</details>


### 78. AgentHorizon: Evaluating Agentic Judges for Long-Horizon Computer-Use Tasks

- **Authors:** Xing Han Lù, Dheeraj Vattikonda, Sina Hajimiri, Fatemeh Pesaran Zadeh, Parishad BehnamGhader, Ghazwa Darwiche, Amirhossein Kazemnejad, Christopher Pal, Alexandre Drouin, Siva Reddy
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11050v1](http://arxiv.org/abs/2610.11050v1)
- **PDF:** [https://arxiv.org/pdf/2610.11050v1](https://arxiv.org/pdf/2610.11050v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Computer-use agents are capable of completing complex tasks, increasing the use of automatic judges to determine success, either for training or for evaluation without human involvement. Despite their flexibility, their reliability on long tasks spanning multiple applications remains unclear. A trajectory, composed of long sequences of screenshots and actions, may appear complete, but in reality violates constraints from the instruction or introduces an unwanted side effect. To identify these errors, a judge needs to examine the trajectory with respect to the user's instruction. To this end, we introduce AgentHorizon, a benchmark of 1,373 computer-use tasks (instruction-trajectory pairs) drawn from 166 hours of human-recorded trajectories spanning three operating systems. By recording trajectories for closely related instructions, we can construct negative tasks by swapping the instructions. This paired design evaluates judges on their ability to distinguish a successful trajectory from one that completed a similar (but incompatible) request. We release the benchmark under three splits: a frontier split, AgentHorizon (AH), a simplified split, AgentHorizon-Simple (AH-S), and a development split, AgentHorizon-Development (AH-D). We further evaluate eleven judges by (1) directly passing the full trajectory (with up to 300 screenshots and actions), and (2) using them as coding agents across five agent harnesses. We find that our best agentic judge, GPT-5.5, achieves 80.9% balanced accuracy on the AH subset. We find that tool-use improves certain models but results in worse performance for open-weight models, and that judges differ drastically in their ability to accept a valid trajectory and reject failed ones. Our findings highlight the need for judges that are capable of locating and verifying often hidden evidence that a task was properly completed inside long interaction histories.

</details>


### 79. NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents

- **Authors:** Min-Young Yu, Tony Kim, Jang Won Choi
- **Published:** 2026-10-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11030v1](http://arxiv.org/abs/2610.11030v1)
- **PDF:** [https://arxiv.org/pdf/2610.11030v1](https://arxiv.org/pdf/2610.11030v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using LLM agents violate the policies they are deployed to enforce, often silently. Prior defenses hand-write rules, query an LLM verifier per action, or compile policies through heavyweight formal machinery. Naive compilation fails: extracted rules block the tool satisfying their own precondition, or read arguments their tool lacks. NOMOS, a four-pass compiler, turns a natural-language policy into a deterministic tool-call gate; static verification with tool-schema-level checks alone (no prover, solver, or LLM) repairs or rejects 37% (airline) and 13% (retail) of candidates, without which most shipped rules are inoperable. Replaying compiled rules over undefended transcripts flags bindings that refuse legitimate work (a development binding refused 95.9% of task-passing calls); no evaluation binding is flagged. On $τ^2$-bench the gate cuts violations of reference-encoded clauses among state-changing calls from 66.3% to 2.6% (airline) and 30.8% to 6.9% (retail), raising airline task success significantly for $2 \le k \le 4$; a 26B on-premise compilation is not significantly worse than hand-written or frontier-compiled rules. Unlike AgentDojo's shipped defenses, it reaches a zero attack success rate (ASR) on banking, where nine attack families collapse onto three structural rules. On the other three suites its ASR is at most 3.6%, from goals with no tool call to govern and one write admitted by a binding weaker than its clause; a second agent model, Llama-3.3-70B, reproduces the effect on both benchmarks. Decisions take microseconds without an LLM call, at a domain-dependent benign-utility cost; compilation runs on-premise on open-weight gemma-4-26B.

</details>


### 80. Why LLM Agents Favor Their Group: Stakes, Observed Norms, and Reputation

- **Authors:** Yujiao Chen
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11008v1](http://arxiv.org/abs/2610.11008v1)
- **PDF:** [https://arxiv.org/pdf/2610.11008v1](https://arxiv.org/pdf/2610.11008v1)
- **Categories:** physics.soc-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents favor their own group because they have watched their members favor each other. The group label alone does little once the decision has a cost; what drives favoritism is observed behavior, and an individual's own record can override it. We test this in small societies with arbitrary group labels, ten rounds of point sharing, and matched one-shot decisions across fifteen OpenAI models and three Claude models, about 4,400 societies and 3.3 million audited model calls. First, the large effect of a bare group label reported in earlier work appears only when giving others points costs the agent nothing; once the agent can keep points for itself, that effect collapses on every model that shows it. Second, under a stake, interaction history becomes the main source of favoritism: the history effect is statistically positive on 13 of 15 models, reaches about 3.5-8 points out of 10 on 11, grows with the number of rounds played, and extends to labeled strangers the agent has never met. Third, with scripted histories, favoritism falls to near zero under an egalitarian norm and reverses when the agent's own group is seen favoring the other side; stronger models side with an individual's record when it conflicts with the group. Group favoritism is thus conformity to observed group behavior, carried to strangers by the label and overridden by individual reputation. The same account predicts responses to betrayal, scandal, and a free offer to change group: public reprimand repairs betrayal better than apology or restitution, allocation punishment remains confined to the offending member, and a formed group cannot be bought but can, on weaker models, be invited away.

</details>


### 81. Curating Always-Loaded Context for LLM Agents: A Capacitated Assortment Model with Censored Feedback

- **Authors:** Zexuan Liu, Yuning Yang, Tiancheng Zhao
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.11007v1](http://arxiv.org/abs/2610.11007v1)
- **PDF:** [https://arxiv.org/pdf/2610.11007v1](https://arxiv.org/pdf/2610.11007v1)
- **Categories:** cs.AI, cs.LG, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

At the start of every session, LLM agents load a fixed context file, such as $\texttt{AGENTS.md}$. Each loaded token in the file is charged again in every later round of the session, and these files can degrade performance as they grow in size. However, in practice, human or automated curators usually grow these files by appending.
  We formulate context curation as a capacitated assortment problem. Instructions consume tokens under a finite attention capacity; adding an instruction never raises the compliance of the others, while retained instructions incur a per-session setup cost.
  We prove an upper bound on the optimal file size, regardless of the number of available candidate instructions, and that appending every instruction with positive standalone value can be arbitrarily worse in net value than selecting an optimal subset. A token budget also limits the loss when the token price is underestimated.
  We then examine what can be learned from past sessions and how this information can guide decisions to add or remove instructions. Feedback is inherently censored: the benefits and harms of loaded instructions are observable, whereas missing instructions generate feedback only when their absence causes harm.
  In this setting, we show that deleting instructions ignored by agents can inevitably remove helpful ones. We characterize how much evidence should be collected before adding an instruction. Besides, we bound regret when human reviewers can inspect only a limited number of edits per period. Empirical experiments further show that irrelevant rules drawn from real context files reduce language-model compliance.

</details>


### 82. iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains

- **Authors:** Vincenzo Guarino, Emanuele Musumeci, Vincenzo Suriani, Daniele Nardi
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10962v1](http://arxiv.org/abs/2610.10962v1)
- **PDF:** [https://arxiv.org/pdf/2610.10962v1](https://arxiv.org/pdf/2610.10962v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the requested operation, in what we call a "grounding failure". Thanks to the recent improvements in reasoning capabilities of foundation models, autonomous robot behavior generation problem can be formulated as a code generation problem. We present iAm.md, a Markdown standard and generation framework, that allows anchoring this process in complementary forms of deployment evidence. Through open-vocabulary semantic mapping, we combine local vision-language detections and object segmentation and refer them to persistent object records in this intermediate standardized representation, allowing agentic introspection. We then study this new technique on a simulated TIAGo, on navigation-and-manipulation tasks, showing how this standardized representation jointly supports skill self-assessment and executable task generalization.

</details>


### 83. RH-Detect: A Unified Benchmark for Reward Hacking Detection

- **Authors:** Junwei Quan, Evgenii Opryshko, Rohan Subramani, Igor Gilitschenski
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10947v1](http://arxiv.org/abs/2610.10947v1)
- **PDF:** [https://arxiv.org/pdf/2610.10947v1](https://arxiv.org/pdf/2610.10947v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reward hacking, where a model exploits an evaluation signal without completing the intended task, threatens the reliability of deployed language model systems. Existing datasets use different labels, response formats, and metadata conventions, making detector results difficult to compare. We present RH-Detect, a benchmark that combines reward-hacking-relevant subsets from eleven public datasets, comprising 92,761 rows and six behavior categories, into a common schema. On 5,021 open-ended evaluation units, each comprising a task prompt and a free-form model continuation, including multi-turn tool-use trajectories, we evaluate six off-the-shelf language models from five families as reward hacking detectors without additional training. The best model achieves a pooled AUROC of 0.962, with accuracy above 93%. For the four strongest models, however, accuracy on the two multi-turn tool-use datasets, MALT and TRACE, is 10.7-15.9 percentage points lower than on the other sources at a common decision threshold, highlighting a key gap for deployment-time monitoring. We find that different input formats have different effects across models. Removing thinking raises Qwen3.5-4B AUROC from 0.779 to 0.849, but lowers Qwen Flash from 0.977 to 0.950. We also evaluate the benchmark as a training dataset for detectors. Holding out each source in turn, single-token SFT improves average AUROC on five of six held-out sources. A GRPO follow-up on that failure case yields a slight improvement in detection performance. Our results show that a single pooled score can conceal variation across data sources, detector inputs, and training procedures.

</details>


### 84. Reading the Room: Foundations, Design, and Challenges of Normative Competence in LLMs

- **Authors:** Andrea Wynn, Harsh Satija,  Seokhyun,  Baek, Anqi Liu, Eric Nalisnick, Gillian K. Hadfield
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10906v1](http://arxiv.org/abs/2610.10906v1)
- **PDF:** [https://arxiv.org/pdf/2610.10906v1](https://arxiv.org/pdf/2610.10906v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human communities are governed by normative systems: shared standards that produce \textit{norms} dictating acceptable behavior, enforced through community sanctioning. Aligning increasingly autonomous AI systems with these norms is a central alignment challenge, complicated by the fact that norms are vast in number, change quickly, and are often arbitrary (e.g., dress or language conventions). Thus, alignment requires \textit{normative competence}: the ability to discern from interaction alone what norms a community enforces without relying on static pretrained knowledge. We introduce a multi-agent community debate setting, where access to debate is governed by synthetic norms, to study normative competence in isolation from pretraining exposure. We show that baseline LLM agents fail to learn norms even when doing so would improve their accuracy. We then experiment with various \textit{normative modules} -- architectural components for norm inference -- finding that norm-following is highly sensitive to both the style of norm and the model powering the normative module, suggesting a lack of generalizability. Furthermore, when idiosyncratic, non-normative behaviors accompany the true norm, LLM agents exhibit an unselective attribution failure: they indiscriminately copy idiosyncratic noise alongside enforced rules, a pattern that persists even when imitating unnecessary behaviors is explicitly penalized. To the best of our knowledge, our work is the first to operationalize and evaluate normative competence in LLMs, demonstrating that current AI systems excel at behavioral mimicry but lack the capacity to discern socially enforced order.

</details>


### 85. RFChipAgent: Multi-Agentic AI Flow for Analog/RF Chip Design

- **Authors:** Awani Khodkumbhe, Yunfei Feng, Raj Rangarajan, Kevin Wang, Kamal Sahota
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10858v1](http://arxiv.org/abs/2610.10858v1)
- **PDF:** [https://arxiv.org/pdf/2610.10858v1](https://arxiv.org/pdf/2610.10858v1)
- **Categories:** cs.AR, cs.AI, cs.LG, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Analog/RF circuits remain the critical interface between digital computation and the physical world, and emerging standards from Wi-Fi 7 to 6G place stringent demands on them, yet analog/RF design remains one of the most labor-intensive steps in chip development. We present RFChipAgent, a first-of-its-kind multi-agent flow of large language model (LLM) agents for end-to-end analog/RF circuit design automation, in which AI agents collaboratively orchestrate the complete design flow under human supervision. RFChipAgent is built around four technical pillars. First, a multimodal retrieval-augmented generation (RAG) subsystem with private per-document FAISS indexing extracts design knowledge from existing engineering documentation. Second, a topology agent drives topology selection, and a schematic and testbench agent automates circuit and testbench assembly. Third, a closed-loop hybrid circuit-sizing engine combines Tree-structured Parzen Estimator (TPE) and CMA-ES optimization, evaluating every candidate in a simulator-in-the-loop framework. Fourth, a trust-scored simulation database accumulates verified performance data and builds an adaptive optimization model that informs subsequent trials. We validate RFChipAgent on a family of GF22FDSOI 60 GHz wideband mm-wave low-noise amplifier (LNA) topologies, demonstrating automated topology generation, specification-driven design-space exploration, and simulator-guided optimization. Experimental results show substantial reductions in design effort while maintaining signoff-quality verification. This work establishes a foundation for LLM-driven multi-agent electronic design automation (EDA) for analog/RF circuits.

</details>


### 86. On the Clock: Towards Punctual and Productive Time-Budgeted AI Agents

- **Authors:** Aaron Wang, Neelabh Madan, Vlad Sobal, Matthew Trager, Michael Kleinman, Elman Mansimov, Wei Xia, Stefano Soatto
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10833v1](http://arxiv.org/abs/2610.10833v1)
- **PDF:** [https://arxiv.org/pdf/2610.10833v1](https://arxiv.org/pdf/2610.10833v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study whether small LLM agents can operate effectively under explicit wall-clock time budgets by both respecting the allocated runtime and using available time productively. We evaluate Qwen3.6-27B on five competitions from MLE-Bench Lite and Qwen3-4B on Zork I (Jericho), two agentic benchmarks where additional computational time can meaningfully improve performance. In the simplest setting, where the budget is stated only in the prompt, agents fail to translate the stated budget into controlled use of time. These failures arise from gaps in time awareness, since the harness provides no timing feedback, but also because they cannot reliably anticipate the duration of actions, and do not have a learned mapping from available time to an appropriate strategy. We investigate two complementary classes of interventions: harness-based mechanisms that expose timing information and enforce deadlines, and reinforcement learning with budget-aware rewards. Injecting timing information through the harness substantially improves budget adherence for Qwen3.6-27B without measurable loss in performance, while enforcement hooks tighten adherence further. RL with GRPO achieves near-perfect budget adherence on Zork I and generalizes to held-out budgets not seen during training, but does not improve task performance over the untrained harness on MLE-Bench. Once agents are made to respect the budget, they still fail to use additional time to improve task performance. RL-trained policies learn when to stop but often fill extra time with repeated actions, and GRPO training on multiple budgets tends to collapse toward the strategy learned for the shortest budget. Our results reveal a gap between time adherence and productive time allocation, which remains a central challenge for budget-conditioned agents.

</details>


### 87. NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime

- **Authors:** Gengze Zhou, Yicong Hong, Jiazhao Zhang, Xunyi Zhao, Jian Zhou, Zixing Lei, Zun Wang, Chongyang Zhao, Xionghui Chen, Stephen Gould, Anton van den Hengel, Qi Wu
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10787v1](http://arxiv.org/abs/2610.10787v1)
- **PDF:** [https://arxiv.org/pdf/2610.10787v1](https://arxiv.org/pdf/2610.10787v1)
- **Categories:** cs.RO, cs.AI, cs.CL, cs.CV, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide. Physical interaction, however, remains the domain of action policies, which provide dense, low-latency control. We present NavGPT-3, a harness that connects the two models, with an OS-like runtime built above it: reasoning, acting, and monitoring run as threads with their own context, tools, and permissions, while the runtime schedules them and decides which thread controls the robot's motion, so that the robot can react to sudden real-world events through interruption and thread switching. Beneath it, our action policy NavGPT VLA, trained on 19.28M examples, allocates visual tokens using codec allocation, in proportion to scene change; its 8B model alone reaches 74.51 SR on R2R-CE and leads RxR-CE with 78.19 SR. With the complete harness, NavGPT-3 sets the state of the art on R2R-CE (81.51 SR) and, for the first time, brings an autonomous agent to human level: on RxR-CE it matches human followers in success (90.43 vs. 90.4 SR) and path fidelity (78.47 vs. 77.7 nDTW) at 1 min 22 s per episode, versus roughly 3 min for a human. We comprehensively ablate the harness design and the interaction between the two models, showing how tools and the action policy shape the path from language-model reasoning to physical control: when NavGPT VLA executes the route, the reasoning loop shortens and the system's minimum reaction time falls from 3-19 s per language-model decision to 0.5-1 s per action-policy step (1-2 Hz). These results show that designing this embodied interface is central to connecting frontier language-model intelligence with low-level physical control. We will release all models, code, and evaluation records.

</details>


### 88. SciExam for ENSO: Can AI Agents Build Climate Models?

- **Authors:** Yinling Zhang, Langchen Liu, Dongbin Xiu, Xueyan Zou, Xu Kuang, Mengdi Wang, Shilong Liu
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10513v1](http://arxiv.org/abs/2610.10513v1)
- **PDF:** [https://arxiv.org/pdf/2610.10513v1](https://arxiv.org/pdf/2610.10513v1)
- **Categories:** cs.AI, cs.LG, physics.ao-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents are increasingly asked to carry out open-ended scientific research, yet their results are usually graded against a known answer, a rubric, or a language-model reviewer, none of which can tell whether a new scientific model is valid. The AI Science Exam for El Nino-Southern Oscillation (SciExam for ENSO) is a benchmark in which agents build low-order stochastic models of ENSO, the dominant mode of interannual climate variability, from real observations. Within a six-hour budget, agents process the observations, write their own diagnostics, which are then frozen, and develop a model using only these diagnostics as feedback. Hidden graders then test whether the model reproduces ENSO's statistics, recovers unobserved variables, and forecasts held-out years, and score a published model in the same way. Across twelve agent systems, six produce models that score higher than the published model, mainly through better reconstruction and forecasting. The simplified forms of the stronger models are each compatible with one of the two competing explanations of ENSO's warm-cold asymmetry, an open debate that the task never mentions. Controlled runs of the top system under varied information suggest that its scores do not come from recalling the dated observational record and that the information it receives shapes how it builds its model. SciExam for ENSO can thus evaluate agent research where no answer is known, and the results suggest that agents can already build competitive models whose structures bear on questions that scientists still debate.

</details>


### 89. A Society of Researchers: Designing Institutions for Populations of Autonomous Research Agents

- **Authors:** Ali Asaria, Deep Gandhi, Tony Salomone
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10468v1](http://arxiv.org/abs/2610.10468v1)
- **PDF:** [https://arxiv.org/pdf/2610.10468v1](https://arxiv.org/pdf/2610.10468v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deployments of research agents are moving to populations of thousands that share one pool of compute, while most current systems organize one project at a time or leave the population unorganized. We argue that such a population will acquire an organization whether or not its designers provide one, so designers should provide it explicitly, and that the multi-agent systems community holds the tools to do so. We propose a society of agents, a population of persistent agents under explicit institutions, and develop it for science as a society of researchers built on six principles. Principal investigators compete for compute through requests for proposals, independent review, and grants; a human governor, the mayor, allocates resources and assigns no tasks. In a running society of ten thousand researchers, asked only to improve the pretraining of language models, one lab reported a way to reach the same quality with about 30% less compute, a result the labs that tested it do not yet agree on. We close with six open problems for the agents community.

</details>


### 90. RunningTab: Direct Workspace Interaction with Environment-Side Tabs

- **Authors:** Jinheon Baek, Soyeong Jeong, Yumin Choi, Dongsu Han, Sung Ju Hwang
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10444v1](http://arxiv.org/abs/2610.10444v1)
- **PDF:** [https://arxiv.org/pdf/2610.10444v1](https://arxiv.org/pdf/2610.10444v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Much knowledge work produces new deliverables from files a workspace already holds, and LLM agents are beginning to take such work over. Through direct corpus interaction, an agent can search and read any of those files from a terminal with no indexing, and producing a deliverable from many of them in this way is what we call direct workspace interaction (DWI). Reaching the files, however, is only half the task: nothing keeps track of what the task asks for, what has been read, and what was listed but never opened, all of which slip through the context window without leaving a trace, so an agent may extract a figure and still deliver a report without it. To address this, we present RunningTab, a framework that equips direct workspace interaction with an environment-side tab: a per-task record of what the task still owes, kept by the environment alongside the agent. Specifically, the agent adds its requirements, while the environment records every file read as an excerpt with its provenance and every listed but unopened file as a candidate; the agent can then see each requirement beside its best-matching excerpts and top unopened candidates, resolve it against matching content or set it aside with a reason, and, should it try to finish with requirements still open, receive them in a finish check. We validate RunningTab on three benchmarks with three LLMs, where it consistently outperforms plain DWI and baselines that keep the record in the model, while its tab usually holds the values a deliverable needs once seen.

</details>


### 91. Pathwise Information Certificates for Decentralized Adaptive Sensing

- **Authors:** Theodoros Tsiligkaridis
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10362v1](http://arxiv.org/abs/2610.10362v1)
- **PDF:** [https://arxiv.org/pdf/2610.10362v1](https://arxiv.org/pdf/2610.10362v1)
- **Categories:** cs.IT, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study decentralized adaptive sensing, where multiple agents choose measurements from evolving local beliefs while exchanging information over a communication graph. We ask whether the measurements actually selected by an adaptive policy have collected enough evidence to distinguish the true target from every plausible alternative. We develop a pathwise certificate based on the Rényi--Chernoff information accumulated along the realized sensing trajectory. It yields nonasymptotic MAP-error bounds and an anytime, network-wide stopping rule for arbitrary history-dependent sensing policies, while separating accumulated statistical information from a bounded network-mixing transient. Linear growth of the information against the least-resolved competitor implies exponential decay of MAP and squared-localization error. A classical pairwise KL converse, specialized to the adaptive decentralized transcript, shows that insufficient information on any pair prevents a positive uniform error exponent, confirming the hardest competitor as a fundamental bottleneck. Across policies, graph topologies, sensor profiles, and seeds, the worst-competitor score correlates more strongly with localization speed than an average-pair proxy in both 1D ($r=0.89$ versus $0.40$) and structured 2D sensing ($r=0.77$ versus $0.48$). Our results provide a practical way to certify and diagnose adaptive multi-agent sensing systems using the evidence they actually collect.

</details>


### 92. LLM-Assisted Generation of Transparent, Open-Source Multiphysics Models of Electrochemical Devices

- **Authors:** Sebastian Castro, Maya F. Schuchert, Spencer A. McCluskey, Eric W. Lees, Justin C. Bui
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10320v1](http://arxiv.org/abs/2610.10320v1)
- **PDF:** [https://arxiv.org/pdf/2610.10320v1](https://arxiv.org/pdf/2610.10320v1)
- **Categories:** physics.chem-ph, cs.AI, physics.comp-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multiphysics continuum models are powerful tools for studying electrochemical devices, enabling in silico reactor design and resolution of local pH, potential, and concentration fields that govern device performance but are difficult to measure experimentally. However, constructing such models requires substantial numerical expertise or reliance on proprietary software. Here, we show that frontier large language model agents can remove this implementation burden while keeping the underlying physics under researcher control. Using one-dimensional electrochemical CO2 reduction to CO in a porous gas diffusion electrode as a test case, we develop a machine-readable, human-specified modeling harness containing governing equations, parameters, numerical methods, logical build stages, and human-verifiable checkpoints. From this specification, the agent reproducibly constructs complete multiphysics models in open-source Julia. Independently built models, including fully autonomous agent-built models, agree with an equivalent COMSOL implementation to within 0.7% of the peak CO partial current density, and with one another to within 0.04%. Systematically planted errors demonstrate the importance of explicit specifications for reproducibility and reveal the agent's capabilities and limitations in debugging model physics. This framework establishes a more transparent approach to multiphysics modeling in which physical descriptions and governing equations, rather than specialized code, become the primary inputs for computational model development.

</details>


### 93. Continual Graph Multi-Agent Reinforcement Learning

- **Authors:** Tommaso Marzi, Ahmed Hendawy, Jan Peters, Carlo D'Eramo, Andrea Cini, Cesare Alippi
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10302v1](http://arxiv.org/abs/2610.10302v1)
- **PDF:** [https://arxiv.org/pdf/2610.10302v1](https://arxiv.org/pdf/2610.10302v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In Continual Multi-Agent Reinforcement Learning (CMARL), agents learn cooperative policies across sequences of tasks, aiming to adapt effectively to new tasks while preserving the ability to solve previously encountered ones. In many applications, tasks differ in their underlying structure, which can represent, for example, distinct operational conditions or target configurations (e.g., different network topologies in power grids or arrangements in formation control). Existing CMARL methods lack dedicated mechanisms to leverage this structural information when learning new tasks, failing to promote transfer and mitigate forgetting. To fill this gap, we propose Continual Graph Multi-Agent Reinforcement Learning (CGMARL), a novel framework for CMARL problems in which task sequences are mapped into a series of attributed graphs, each modeling a task-specific structure. In CGMARL, each graph determines the environment dynamics (next states and/or rewards) and the number of agents for the corresponding task. Then, we present Graph-based Formation (GRAFO), the first CGMARL benchmark, and show how forgetting arises in this setting. Finally, to address this limitation, we propose Frozen Graph Encoder (FROG), a method that relies on a frozen graph backbone to preserve past structural information in graph-based CMARL policies. Experiments on GRAFO show that pairing FROG with existing CL methods substantially improves performance on multiple CGMARL scenarios.

</details>


### 94. Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming

- **Authors:** Ángel Sánchez-Fernández, Javier Pernas-Álvarez, Diego Crespo-Pereira
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10184v1](http://arxiv.org/abs/2610.10184v1)
- **PDF:** [https://arxiv.org/pdf/2610.10184v1](https://arxiv.org/pdf/2610.10184v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Developing optimization models for production scheduling requires substantial expert effort. Research on large language models (LLMs) has followed two directions: specialized approaches for automated modeling, mostly for mixed-integer linear programming, which often rely on dedicated training or problem-specific architectures that limit industrial deployment; and agentic artificial intelligence for operational decision support, which generally assumes that the optimization model already exists. This study bridges both directions by assessing whether general-purpose LLMs, orchestrated as agents without task-specific training, can formulate and implement constraint programming models from natural-language problem descriptions. Singleagent and multi-agent architectures are integrated with a Model Context Protocol server that provides context-aware retrieval of solver documentation to mitigate hallucinations during implementation. Both are compared with a direct LLM baseline on six industry-oriented problems covering flow-shop, job-shop, flexible job-shop and resource-constrained warehouse scheduling, using three LLMs and assessing modeling accuracy, execution success, latency and token consumption. Formulation proves largely within reach of current LLMs, whereas implementation is the main barrier. The multi-agent workflow raises the share of scripts that run correctly as generated from 14.8% with a direct LLM call to 59.3%, reaching 80.6% on the four less complex problems, while tightly coupled intralogistics models remain an open challenge.

</details>


### 95. Know the Shape, Find the Fault: Topology-Conditioned Diagnosis of Multi-Agent LLM Failures

- **Authors:** Xinwen Liu, Zhuocheng Pan, Isabella Zhu, Jawei Zhang, Xudong Liu, Tianyu Wo
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10126v1](http://arxiv.org/abs/2610.10126v1)
- **PDF:** [https://arxiv.org/pdf/2610.10126v1](https://arxiv.org/pdf/2610.10126v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems coordinate task execution through exchanges of information among agents. When coordination breaks down, similar symptoms in execution traces can reflect different problems in how information is passed, used, or verified. Communication topology captures how agents exchange information and provides structural cues for distinguishing coordination failure modes. Using these cues for diagnosis requires establishing how topology relates to failure patterns and recovering the relevant structure from execution traces that lack explicit topology labels. We analyze the relationship between communication topology and failure patterns and introduce MAScope, a two-stage framework for topology-conditioned diagnosis. Its Trace Structural Extractor TSE recovers communication topology from heterogeneous execution traces by grounding an interaction graph in message evidence. The Topology-Conditioned Judge TC-Judge then classifies failures using the trace, predicted topology, an empirical failure prior estimated from separate labeled traces, and a short description of topology-specific failure patterns. Under a fixed orchestration structure, the recovered topology can be reused across executions. Experimental results show a statistically significant association between communication topology and failure type, with $χ^2 = 409.9$ and $p = 1.2 \times 10^{-70}$. On the \num{851} MAST-clean traces, ground-truth topology context raises gpt-mini's Macro-F1 from $0.173$ to $0.350$. With predicted topology, the pipeline achieves $0.346$, approaching the trace-only gpt-5.4 baseline of $0.372$. For \num{1000} traces under a fixed orchestration structure, the projected pipeline cost, including one topology extraction, is approximately $6\%$ of repeated gpt-5.4 diagnosis cost. These results show that topology-conditioned context improves failure diagnosis and supports lower-cost deployment.

</details>


### 96. The Cost of Classical Multi-Agent Path Finding

- **Authors:** Alvin Combrink, Sabino Francesco Roselli, Martin Fabian
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10100v1](http://arxiv.org/abs/2610.10100v1)
- **PDF:** [https://arxiv.org/pdf/2610.10100v1](https://arxiv.org/pdf/2610.10100v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-Agent Path Finding (MAPF) is the problem of planning conflict-free paths for multiple agents in a shared space, each from its start to its goal. Classical MAPF has been the dominant formulation for many years, with its assumptions of discrete time and graph-based conflicts presumably easing the search for solutions. These assumptions limit the physical environments and agents for which a solution is truly collision-free, and also place an upper bound on solution quality that no algorithmic improvements can lift. This work investigates how much solution quality, and in what contexts, the classical MAPF formulation forfeits. Continuous-time MAPF (MAPF$_R$) relaxes these assumptions, making it a natural counter-formulation to compare against across various agent counts and sizes, and graph connectedness, topologies, and resolutions. We find that continuous time and agent shape consideration are worth relatively little on their own; their value comes from enabling an expanded range of move actions, on average improving solution quality by at least $5\%$ on narrow and constrained maps and $17\%$ on maps with open spaces. In some cases, the improvements exceed $20\%$. Doubling the map resolution with classical MAPF recovers less than $3\%$, meaning that little of what is forfeited can be bought back through more compute. This work therefore provides insight on when classical MAPF is a reasonable simplification, and when MAPF$_R$ unlocks significantly higher-quality solutions.

</details>


### 97. ExperienceIndex: Artifact-Grounded Memory

- **Authors:** Peter Baile Chen, Geoffrey X. Yu, Xinming Liu, Samuel Madden, Dan Roth, Jacob Andreas, Doug Downey, Michael Cafarella
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10091v1](http://arxiv.org/abs/2610.10091v1)
- **PDF:** [https://arxiv.org/pdf/2610.10091v1](https://arxiv.org/pdf/2610.10091v1)
- **Categories:** cs.CL, cs.AI, cs.IR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Knowledge-intensive tasks require answering many questions by reasoning about a shared corpus of artifacts (e.g., court cases, or scientific literature). As humans interact with these corpora, they naturally accumulate experiential knowledge about artifacts, enabling them to quickly identify the complete set of relevant artifacts for each new task. However, existing AI agents lack appropriate memory solutions to build or reuse such artifact-grounded experience, leading to lower answer quality and higher online cost. Existing memory solutions extract and reuse information from prior task-solving traces, but they primarily focus on user preferences, factual attributes, or abstract reasoning patterns rather than persistent artifact-specific knowledge. We introduce ExperienceIndex, a novel experience layer for AI agents that captures and reuses knowledge about artifacts based on prior reasoning traces. ExperienceIndex stores two complementary forms of experience: (i) single-artifact experiences that summarize an artifact's contribution to prior tasks and (ii) artifact-pair experiences that encode structural relationships discovered during past reasoning. Integrated as lightweight middleware, ExperienceIndex uses an experience retrieval mechanism to guide agents toward the complete set of relevant artifacts for new tasks, improving both answer quality and efficiency. Across diverse corpora and agentic solutions with different search frameworks, ExperienceIndex delivers consistent gains, raising answer quality by up to 11.0 points and reducing online dollar cost by up to 50.5%. We further demonstrate two benefits: (i) cross-task generalization, where experiences accumulated from text-to-SQL tasks transfer to factoid QA tasks over the same artifact corpus, and (ii) teacher-student learning, where experiences from a stronger model enable a weaker model to reach comparable performance.

</details>


### 98. Multi-Agent Coordination via Support-Preserving Distillation

- **Authors:** Sangmin Lee, Youngju Na, Chanmi Lee, Sung-eui Yoon
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10087v2](http://arxiv.org/abs/2610.10087v2)
- **PDF:** [https://arxiv.org/pdf/2610.10087v2](https://arxiv.org/pdf/2610.10087v2)
- **Categories:** cs.LG, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Offline MARL increasingly relies on generative policies to model multimodal joint behavior, typically by distilling a centralized teacher into decentralized one-step actors under the CTDE. We identify a failure mode at the teacher training stage: standard flow-based teachers pair noise with replay targets independently, so nearby noise samples can be routed toward conflicting coordination modes. The teacher then produces samples between valid modes, and because the distillation loss regresses each local actor onto the conditional mean of the teacher's output given local input, this error is not absorbed but propagated to the student. To remove this teacher-side artifact, we propose Mode-Support Semi-Discrete Optimal Transport (MoSDOT), which summarizes multimodal replay into a finite mode support with prescribed capacities and uses conditional semi-discrete optimal transport to assign each noise sample to a single mode before teacher training. We additionally study a shared-randomness variant that uses a shared noise component at execution to expose the residual gap intrinsic to strict-product execution. On controlled diagnostics and offline MARL benchmarks, MoSDOT improves endpoint quality and routing consistency, particularly on datasets exhibiting multimodal joint behavior.

</details>


### 99. CANDO: Cooperative Agentic Network for Layout Design Optimization

- **Authors:** Athanasios Masouris, Zheng Jing, Benjamin Sam Chandler, Hadi Jamali-Rad
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10044v1](http://arxiv.org/abs/2610.10044v1)
- **PDF:** [https://arxiv.org/pdf/2610.10044v1](https://arxiv.org/pdf/2610.10044v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Layout generation for real-world facilities is a challenging problem, requiring reasoning over irregular site boundaries, heterogeneous orientations, access-aware placements, and motion-planning feasibility. Yet, most existing layout benchmarks in the generative AI space target simpler placements over rectangular domains and rely on distributional metrics such as FID and IoU that reward conformity to dataset priors, thus discounting design innovation. Motivated by these gaps, we introduce ALPS-Bench, a benchmark of $1,000$ professionally annotated real-world facility layouts paired with an instance-specific scoring protocol grounded in a structured design manual. As a strong baseline for ALPS-Bench, we propose CANDO, a training-free multi-agent framework in which specialized agents iteratively refine layouts through a verification-grounded loop, concentrating reasoning on strategic spatial decisions. We demonstrate that CANDO surpasses state-of-the-art trained and LLM-based baselines on the widely adopted PubLayNet, RICO, and PKU-PosterLayout benchmarks, establishing cooperative agentic design as a broadly effective recipe for constraint-aware layout synthesis.

</details>


### 100. From Expected Harmfulness to Likelihood: A Probabilistic Reformulation of Jailbreaking LLM Agents

- **Authors:** Juanyang Xu, Zheng Wang, Xingyu Zhao, Siddartha Khastgir, Andi Zhang
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09973v1](http://arxiv.org/abs/2610.09973v1)
- **PDF:** [https://arxiv.org/pdf/2610.09973v1](https://arxiv.org/pdf/2610.09973v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When the harmfulness of an LLM agent's output can be quantified, a natural jailbreaking objective is to maximize expected harmfulness over admissible input modifications. An alternative approach constructs or selects harmful target outputs and modifies the input to increase their likelihood. We establish a precise connection between these two approaches through a probabilistic reformulation. Specifically, we show that the gradient of the logarithm of expected harmfulness with respect to the input equals the expected input gradient of the model's log-likelihood under a harmfulness reweighted output distribution. This identity provides a unified interpretation of expected harmfulness and target likelihood optimization. Building on this connection, we propose OPUR, a sampling distribution designed to generate highly harmful target outputs and use the resulting samples to guide likelihood-based input optimization. Experiments demonstrate the effectiveness of the resulting method in jailbreaking LLM agents.

</details>


### 101. The Harness as the Only Mutable Surface: Compliance-Bounded Self-Evolution of LLM Agents in Credit Pipelines, with a Measured Admission Gate

- **Authors:** Ravil Akhtyamov
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10629v1](http://arxiv.org/abs/2610.10629v1)
- **PDF:** [https://arxiv.org/pdf/2610.10629v1](https://arxiv.org/pdf/2610.10629v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-improving LLM agents can adapt a credit pipeline to a changed rule, but an agent that rewrites itself destroys the artefact a supervisor reviews: a named change, a recorded test, an approval. We argue that self-evolution is reviewable only if it is confined to the runtime harness (instruction text, tool-call logic and primitive composition) while model weights stay fixed, so that every adaptation is a diff with a cause and a test attached. We give a dual-loop engine built on that bound, with one admission gate that writes a hash-chained record before deployment, and we measure the gate in simulation, with a simulated agent and a seeded-search proposer rather than language models. Across three families of supervisory re-interpretation at three severities, 10 seeds each, the gated loop admitted 144 of 7,449 candidate changes, none of which worsened error on held-out history, and restored the false-positive rate to the oracle level without raising missed flags in every low- and mid-severity cell. With the gate replaced by the check an unbounded system applies (fewer errors visible in recent traces), the same loops admitted 309 harmful changes and left missed flags above 10% in 49 of 90 runs: false positives fell because the screen was loosened. Evaluated on pre-shift labels, the gate rejected every candidate, so a re-interpretation must be encoded as a rule that relabels history. Parametric and scope shifts were repaired locally, a structural one only by primitive replacement; at the highest structural severity the gate's fixed tolerance blocked the correct replacement in half the seeds. We map the mechanisms to the EU AI Act's provisions for high-risk credit scoring and note that the April 2026 US model-risk guidance excludes agentic AI from its scope.

</details>


### 102. AgentTime: Can Agents Estimate and Control Their Own Runtime?

- **Authors:** Michael Ofengenden, Maksym Andriushchenko
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09944v2](http://arxiv.org/abs/2610.09944v2)
- **PDF:** [https://arxiv.org/pdf/2610.09944v2](https://arxiv.org/pdf/2610.09944v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An essential control of AI agents is their ability to manage runtime. This ability requires a sense of time-awareness, to predict and estimate wall-clock time and to control their own actions. Prior work has focused on time-awareness, but duration-following and control in native agent harnesses remain unexplored. We present AgentTime, a benchmark for testing whether agents can work for a requested duration, predict their runtime, and estimate elapsed time afterward. It comprises 222 tasks from 18 sources spanning coding, computer use, agentic work, and automated research. Duration-following experiments append a single instruction specifying how long to work, with requests ranging from about a minute to multiple days. Accuracy on these instructions varies substantially: Fable 5.1 in Claude Code deviates from requested runtimes by a typical factor of 2.9$\times$, compared with only 1.2$\times$ for GPT-6 Astra in Codex. However, matching the requested runtime does not, by itself, establish continued work on the task. Among 158 reviewed Astra runs with classifiable transcripts, 14 explicitly slept after appearing to finish. In forecasting experiments, predictions tend to overestimate natural runtimes. In retrospective experiments, removing temporal information more than doubles deviation for Sol and Astra and nearly doubles it for Fable. An agent's ability to complete a task does not guarantee that it can control its own time or work for the whole requested duration. For agents to run reliably, safely, and autonomously over long horizons, we require the evaluation of both.

</details>


### 103. LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets

- **Authors:** Jun Zhao, Leiming Fu, Yanbo Wen, Yiding Wang, Xuantong Liu, Yang Shu, Yuyang Lu, Xuanran Xing, Jingqi Tong, Hao Xu, Qi Zhang, Xuanjing Huang
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09872v1](http://arxiv.org/abs/2610.09872v1)
- **PDF:** [https://arxiv.org/pdf/2610.09872v1](https://arxiv.org/pdf/2610.09872v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluating agents by outcomes alone can obscure the capabilities that produce them. This problem is especially pronounced in evolving environments, where outcomes reflect a closed-loop interaction between agent behavior and changing external conditions. We introduce LiveMACEBench, a process-aware benchmark that uses live financial markets as a naturally evolving testbed for persistent LLM agents. Five frontier LLMs operate along continuous trajectories under matched Tool Use, Persistent Memory, Rule Following, and Multi-Agent Collaboration configurations. We evaluate them through both realized outcomes and mechanism-specific diagnostics derived from complete decision traces. Across 30 days of live evaluation, we find a pronounced outcome-capability gap: realized returns often diverge from capability-specific measurements, and similar outcomes can arise from markedly different patterns of mechanism use. Trace-level diagnostics further expose distinct bottlenecks across capabilities, demonstrating that mechanism access, effective mechanism use, and downstream performance are not interchangeable measures of agent capability. LiveMACEBench makes this distinction measurable, turning live markets from a performance leaderboard into a diagnostic environment for agent capability

</details>


### 104. Deadline-Aware Multi-Agent Reinforcement Learning for TSN-Based Vehicular Edge Networks

- **Authors:** Bernardo A. C. Pereira, Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Andreas Gavrielides, Johann M. Marquez-Barja, Daniel F. Macedo
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09870v1](http://arxiv.org/abs/2610.09870v1)
- **PDF:** [https://arxiv.org/pdf/2610.09870v1](https://arxiv.org/pdf/2610.09870v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vehicular edge computing (VEC) enables latency-sensitive applications by bringing computing and networking resources closer to vehicles. However, existing approaches often overlook network contention among co-located services with heterogeneous and dynamic latency requirements. While time-sensitive networking (TSN) provides bounded-latency communication, conventional and reinforcement learning-based schedulers struggle to adapt to highly dynamic vehicular environments and inter-queue dependencies. To address these limitations, we propose a multi-agent reinforcement learning (MARL) approach for queue-level scheduling in TSN-enabled VEC. Each TSN queue is assigned an autonomous agent that jointly learns the queue service order and time-slot duration to minimize deadline misses under speed-dependent latency requirements. We employ multi-agent proximal policy optimization (MAPPO) to enable coordinated yet autonomous scheduling decisions. Evaluation against single-agent, multi-agent, and non-learning-based baselines shows that MAPPO provides robust performance across different traffic profiles. Compared with centralized single-agent methods, it reduces service latency by up to 66.2% and improves reliability by up to 271.8%. Furthermore, unlike urgency-based heuristics, MAPPO ensures balanced scheduling while achieving lower inference times compared to other MARL methods.

</details>


### 105. Agent4RE: A Self-Refining Multi-agent Framework for End-to-End Software Requirements Engineering and Benchmarking

- **Authors:** Yongjian Tang, Linhan Li, Thomas Runkler
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10628v1](http://arxiv.org/abs/2610.10628v1)
- **PDF:** [https://arxiv.org/pdf/2610.10628v1](https://arxiv.org/pdf/2610.10628v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing LLM-based approaches for software Requirements Engineering (RE) typically rely on basic prompting strategies or rudimentary agent collaboration, under-utilizing the full potential of multi-agent systems. Meanwhile, available datasets focus on isolated subtasks, such as requirements extraction, classification, and completeness detection, leaving the absence of an end-to-end RE benchmark that spans from requirements elicitation to generation. We present Agent4RE - a self-refining multi-agent RE system that orchestrates specialized agents and incorporates two iterative improvement loops. To support evaluation, we construct RE-E2E - a real-world dataset built from human-written requirement specifications, enabling end-to-end assessment of RE workflows. Building on this foundation, we further propose two enhanced Agent4RE versions that incorporate either autonomous self-refinement or structured human feedback, and analyze their strengths and limitations across different scenarios. Evaluation on 8 Large Language Models (LLMs) demonstrates that all three Agent4RE variants consistently outperform a domain-context-augmented prompting baseline by average 8% in text-based metrics. The two enhanced variants achieve the highest LLM-as-a-judge and human ratings, surpassing two RE baselines by approximately 0.8 points on a four-point scale. This consistent performance establishes Agent4RE as a practical end-to-end RE solution for industrial environments.

</details>


### 106. Training Advisors for LLM Agents from Task Outcomes

- **Authors:** Sergei Polezhaev, Barys Liskavets, Ori Press, Alexander Golubev
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09858v1](http://arxiv.org/abs/2610.09858v1)
- **PDF:** [https://arxiv.org/pdf/2610.09858v1](https://arxiv.org/pdf/2610.09858v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents tackle multi-step tasks by interleaving reasoning and tool calls with observations from the environment. Prior work has shown that natural-language feedback can help these agents revise their decisions during task execution. We introduce Caddie, a method for training critics to provide natural-language analysis and advice as agents work through a task. Unlike approaches that rely on step-level labels or reference critiques, Caddie learns from whether the agent ultimately succeeds after receiving the critic's feedback. We optimize the critic through reinforcement learning while keeping the base model frozen. Trained on multi-hop question answering with a single base model, our Qwen3-4B critic improves success rates across four base models of different scales and architectures, including three not used during critic training. On the MuSiQue benchmark, the trained critic improves Qwen3-4B's success rate by more than 25 percentage points, surpassing the performance of Kimi K3 without a critic. The same critic also yields gains on out-of-domain interactive benchmarks, including $τ^3$ and DeepDive, with no additional training. Our results show that agents can decide when to seek help from a critic at inference time and that outcome-based critic training can produce guidance that transfers across base models and task domains.

</details>


### 107. SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles

- **Authors:** Yuyao Ge, Yiwei Wang, Yuchen He, Baolong Bi, Lingrui Mei, Jiayu Yao, Lizhe Chen, Shenghua Liu
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09832v1](http://arxiv.org/abs/2610.09832v1)
- **PDF:** [https://arxiv.org/pdf/2610.09832v1](https://arxiv.org/pdf/2610.09832v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory-augmented reinforcement learning strengthens LLM agents' ability to solve complex long-horizon tasks. Skills are one such form of memory, pairing instructions with an applicability condition over task types. However, retaining every skill indiscriminately as the policy improves lets obsolete or harmful entries accumulate and mislead the agent. We propose SkillForge, an agentic RL method that compiles and evolves the skill library through a fitness-driven skill lifecycle of trial, active, stable, and retired states, so that the skills and the model co-evolve throughout training. A pre-RL evaluation phase first uses the base model's own rollouts to pre-retire low-fitness skills, yielding a filtered library that then seeds supervised fine-tuning. Reinforcement learning takes over from this checkpoint, and at each iteration selective retirement, stabilization, and LLM-guided mutation continue to forge the skill library alongside policy optimization. Across multiple interactive agent benchmarks, SkillForge achieves the highest aggregate success rate, delivering up to 7.8% relative improvement over the strongest baseline while keeping the skill library compact throughout training. We introduce SkillFurnace, a dataset of 5k+ annotated records bundling retirement-filtered SFT trajectories, evolved skill libraries with fitness annotations, and retirement events with human-annotated failure categories to support research on skill quality and lifecycle management.

</details>


### 108. Homogenization in Multi-Agent Systems

- **Authors:** Prakhar Ganesh, Kyra Wilson, Luca Zappella, Barry-John Theobald, Nicholas Apostoloff, Lucas Monteiro Paes, Nivedha Sivakumar
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09824v1](http://arxiv.org/abs/2610.09824v1)
- **PDF:** [https://arxiv.org/pdf/2610.09824v1](https://arxiv.org/pdf/2610.09824v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) leverage interactions between agents to perform complex tasks. Despite their success, we show that these interactions can also lead to homogenization, i.e., agents converging to similar behaviors. Homogenization in MAS can reduce agent diversity and reinforce shared failures. In this paper, we operationalize homogenization using three metrics: conformity to the majority, polarization towards extremes, and growing inertia against changes over subsequent interactions. We evaluate homogenization in MAS for code generation, hiring, and scientific peer review. Across these tasks, we show that homogenization translates to concrete downstream risks: in code generation, it hides and amplifies correlated errors which can create systemic vulnerabilities; in hiring, it allows the influence of biased agents to persist long after their removal; and in peer review, it creates uneven evaluation standards across research areas. Our results establish homogenization as a failure mode of MAS, demonstrating that MAS evaluations must move beyond aggregate performance to carefully analyze interaction dynamics. Finally, we show that simple approaches to increase diversity---leveraging sampling stochasticity and mixed-models MAS---fail to reduce homogenization risks, highlighting the need for strategies to effectively leverage agent diversity.

</details>


### 109. Decoupling Logic from Persona: Structural Immunity of Edge LLM Agents to Context Pollution

- **Authors:** Masaaki Nakatsu, Reno Wang
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09772v2](http://arxiv.org/abs/2610.09772v2)
- **PDF:** [https://arxiv.org/pdf/2610.09772v2](https://arxiv.org/pdf/2610.09772v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Edge language-model agents must hold a persona and reason correctly at once, in one context window that fills with history and persona instructions. We study what happens to the logical part of such an agent when that history is long, misleading and persona-heavy (persona-logic interference), and present a Decoupling Architecture (AO-DA) that separates logical inference ("What") from persona expression ("How") into two inference paths on one INT4 base model with hot-swappable LoRA adapters. The logic path receives only the core turn and emits a verifiable structured state (Micro-State); the persona path renders it in character with the full history. In same-base-model ablations on an Apple M2 laptop (Llama-3.1-8B-Instruct and Gemma-3-4B-it, 4-bit; 480 runs: 2 bases x 4 pollution levels x 3 arms x 2 tasks x 2 personas x 5 seeds) we find: (i) the decoupled logic path is structurally invariant to pollution: its prompt stays at 180 (Llama) or 167 (Gemma) tokens while the mixed single-pass prompt grows from 242 to 1,203 on Llama, and its outputs are byte-identical across levels (40/40); (ii) the mixed single pass degrades monotonically (composite logic score 0.669 to 0.150 on Llama, 0.487 to 0.150 on Gemma), mostly by failing to emit the required structured output (80-95% of runs on Llama, 100% on Gemma at the two highest levels); (iii) with the same pollution fed into the logic path, the dedicated-adapter, dedicated-format path is still more robust than the single pass on the 8B model (failure 0-20% vs 25-95% at L2-L4; paired $Δ$ +0.30 to +0.50, Cliff's $δ$ 0.50-0.85, Holm-adjusted $p \le 0.03$) but not on the 4B model, where both collapse. Separation costs one extra decode on a topic's first turn (28.2 s vs 18.2 s on Llama) and buys persona hot-swapping in 1.7 ms (warm median) without re-running the logic path. Code, logic-path adapters, logs and analysis scripts are released.

</details>


### 110. Bolzano: From Expert-Guided Proof Search to Automated Open-Problem Solving

- **Authors:** Adrián Zámečník, Matěj Kripner, Martin Koutecký, Martin Balko, Jan Grebík, Pavel Hubáček, Robert Šámal, Václav Rozhoň
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09769v2](http://arxiv.org/abs/2610.09769v2)
- **PDF:** [https://arxiv.org/pdf/2610.09769v2](https://arxiv.org/pdf/2610.09769v2)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly contributing to mathematical research, where progress often depends on efficient proof search, incremental improvements and careful verification. We describe Bolzano, a multi-agent open-source system that uses parallel prover agents with a verifier agent and maintains a human-readable research state. Initial manual use on expert-selected problems yielded 8 results whose proofs were checked by domain experts. Motivated by these case studies, we ran Bolzano without problem-specific human guidance on about 3,800 open problems extracted from four sets of papers, solving about 200 open problems. One experiment used papers accepted to STOC 2026, a top conference in theoretical computer science. There, we answered four questions raised in the papers, as confirmed by their authors.

</details>


### 111. Cost-Efficient Theorem Proving via Agent Orchestration in Program Verification

- **Authors:** Shuangjie Yao, Nikolaus Holzer, Mark Paul Santolucito, Baishakhi Ray, Suman Jana, Dongdong She
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09681v1](http://arxiv.org/abs/2610.09681v1)
- **PDF:** [https://arxiv.org/pdf/2610.09681v1](https://arxiv.org/pdf/2610.09681v1)
- **Categories:** cs.AI, cs.LO, cs.PL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Program verification establishes software correctness through machine-checkable proofs constructed in theorem provers. It's a guarantee especially valuable for code generated by large language models (LLMs), which is fluent but carries no assurance of correctness. Almost all existing provers, however, pursue pass rates alone at whatever sampling or search budget it takes, and overlook the success-vs-cost frontier; yet real software often carries hundreds of interdependent proof obligations, so what matters at scale is not whether one theorem can be proved, but how many can be proved economically. We introduce CoCo-Prover, which formalizes cost-efficient program proving as metalevel decision-making under cost, grounded on two-level proof graphs: an AND/OR proof hypergraph within each declaration is joined to a lemma-dependency graph across declarations; and at each step, it answers two questions: which open goals to select, and which actions to purchase on these goals. Selection stays symbolic as a topological pass over the proof graphs. Action choice is agent orchestration via metalevel decision-making: an agentic router treats every bounded specialist invocation as a separately priced, best-effort computation, matching heterogeneous specialist agents together with configurations, under evolved routing rules as evidence accumulates. On five program verification benchmarks in Lean 4 including function-level CLEVER, VERINA, and AlgoVeri, and repository-level NTP4VC and Vero, we show that CoCo-Prover achieves a better success-vs-cost frontier than baselines including frontier coding agents and state-of-the-art LLM-based provers: it achieves the best solve rate on every benchmark and up to 100% on two benchmarks. It also reduces cost by up to 30.9% compared to the strongest baseline with the strongest LLM in our evaluation.

</details>


### 112. Shared and structured inputs undermine collective random choice by reasoning AI agents

- **Authors:** Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09667v1](http://arxiv.org/abs/2610.09667v1)
- **PDF:** [https://arxiv.org/pdf/2610.09667v1](https://arxiv.org/pdf/2610.09667v1)
- **Categories:** cs.AI, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Random selection is widely used in resource allocation and auditing, making reliable implementation essential for AI-agent systems. Behavioural tests across six reasoning models uncovered threshold and divisibility rules used in identifier-based choices. For threshold-following GPT-6 Sol and Gemini 3.8 Flash, single-agent measurements prospectively predicted correlated participation under shared identifiers and biased participation under distinct identifiers with common timestamp bits. Changing dates, formats and identifier labels revealed when these predictions held. Explicit instructions to randomize independently reduced but did not eliminate shared-input correlation. To test implications for oversight, we asked four models to select customer requests randomly for human review. GPT-6 Sol approached the target rate while selecting predictably from identifiers; the others rarely selected requests. All four closely followed supplied random draws. These findings expose collective and audit vulnerabilities that selection rates alone miss, making input-dependent bias, correlation and predictability central targets for agent evaluation.

</details>


### 113. Learning Situation-Conditioned Thinking Policies for Long-Term LLM Agents

- **Authors:** Hong Su
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09590v1](http://arxiv.org/abs/2610.09590v1)
- **PDF:** [https://arxiv.org/pdf/2610.09590v1](https://arxiv.org/pdf/2610.09590v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-running autonomous agents must reuse accumulated reasoning experience without allowing explicit historical memory and LLM context to grow indefinitely. However, existing memory mechanisms mainly retrieve, summarize, or compress past content and do not directly learn when particular kinds of thinking should be activated or discover new thinking knowledge from temporally dispersed experiences. This paper proposes a situation-conditioned thinking memory framework that transforms historical reasoning experience into a lightweight policy for predicting what should be thought about in the current situation, while leaving detailed reasoning to a large language model. Situations may represent temporal or spatiotemporal evolution rather than only current states. Temporary experiences are also periodically analyzed across multiple independent episodes to identify repeated long-range regularities, which are consolidated into new thinking knowledge and further internalized by the lightweight policy. Experiments show that the learned policy achieves 1.000 F1 on temporal-rule generalization, improves DeepSeek reasoning F1 from 0.789 to 0.868, reduces online processing time from 0.3636 ms to 0.0382 ms per query at 30,000 historical situations, and reaches 1.000 relation-discovery F1 and future-thinking accuracy after sufficient repeated cross-experience evidence.

</details>


### 114. Correct Answers, Unsupported Findings: Evidence Binding in Forensic Reconstruction of LLM Agent Logs

- **Authors:** Taehyeon Yun, Dongho Kim, Geonwoo Kim, Juyoung Seo, Minseok Hur, Moohong Min
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09581v1](http://arxiv.org/abs/2610.09581v1)
- **PDF:** [https://arxiv.org/pdf/2610.09581v1](https://arxiv.org/pdf/2610.09581v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Forensic reconstruction of LLM-agent actions requires not only recovering the correct value, but establishing which preserved record supports that finding. Tool logs, generated explanations, and local citation identifiers capture different parts of this evidence, yet a citation identifier does not establish a source unless its binding to a record is preserved. We audit this distinction using 64 mechanically checkable cases from saved AgentDojo Banking executions. Two LLM readers reconstruct source relationships under controlled variations in visible evidence and identifier-to-record bindings. We separately evaluate complete-record agreement, evidence-grounded findings, justified abstention, and unsupported assertions. With original identifiers and no binding table, Sonnet recovered every literal source location but made unsupported citation-source assertions in 26 of 28 cases requiring the missing relation; 22 nevertheless matched the complete reference. Adding explicit bindings improved grounded reconstruction for both readers, whereas identifier renaming alone provided no consistent remedy. A deterministic same-packet comparator correctly resolved the bounded task or abstained throughout. These results show that factual agreement alone is insufficient for evaluating forensic reconstruction of agent logs and motivate preserving explicit record bindings to distinguish supported findings from correct guesses.

</details>


### 115. DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists

- **Authors:** Samuel Margolis, Paul Schmiedmayer, Alan Huang, Ethan Chen, Ishan Bhattacharjee, Atman Shah, Ben Viggiano, Fang Cao, Shriya Reddy, Roger Xia, Jack O'Sullivan, Daniel Katz, Matthew Wheeler, Euan Ashley, Bruna Gomes
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09558v1](http://arxiv.org/abs/2610.09558v1)
- **PDF:** [https://arxiv.org/pdf/2610.09558v1](https://arxiv.org/pdf/2610.09558v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Drug target discovery requires distinguishing molecules that causally drive disease from those that are merely associated with it. Training and evaluating AI agents to perform this workflow end-to-end is difficult because real world biobanks lack known causal ground truth and participant-level data is access controlled. We introduce DrugTargetWorld, a framework that procedurally generates simulated biobanks, or "worlds," with known but concealed causal structure. Each world contains genotypes, proteins, health records, outcomes, and synthetic magnetic resonance imaging (MRI) for 54,000 participants. Agents must construct a disease phenotype, identify causal driver proteins, infer the beneficial direction of modulation, and optionally conduct virtual 'wet lab' experiments. We evaluated nine agents in 540 episodes across 20 cardiovascular worlds and three experimental budgets. Opus 5 and GPT-5.6 Sol achieved the highest mean composite scores, 39.98 and 35.38 of 100, respectively, and both recovered 64% of causal drivers on average. However, no agent reliably distinguished misleading non-causal proteins, and performance remained limited by the integrative judgments required to connect phenotype construction, causal evidence, and intervention decisions. By making each world's causal structure known to the evaluator but hidden from the agent, DrugTargetWorld turns end-to-end drug target discovery into a scalable training and evaluation problem with verifiable reward.

</details>


### 116. Constitution-Guided Watermarking

- **Authors:** Toluwani Aremu, Samuele Poppi, Nils Lukas
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09552v1](http://arxiv.org/abs/2610.09552v1)
- **PDF:** [https://arxiv.org/pdf/2610.09552v1](https://arxiv.org/pdf/2610.09552v1)
- **Categories:** cs.CR, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Watermarking enables language model providers to identify text generated by their models. However, its desired properties can conflict (\ie~stronger watermark signals can degrade text quality), while designs that resist editing may also facilitate forgery. Providers address these trade-offs by choosing configurations that balance competing objectives or prioritize particular properties. Either approach imposes a shared operating point on requests with different requirements, potentially sacrificing quality where wording preservation matters or robustness where reliable attribution is essential. To allow flexible and adaptable designs, we introduce \emph{Constitution-Guided Watermarking}, a framework that selects request-appropriate trade-offs from provider requirements, listed as natural-language principles. \emph{Offline}, a pretrained reasoning agent examines constitutional rules alongside watermark implementations and iteratively refines rule-specific configurations using empirical feedback. \emph{At deployment}, a separate monitor identifies applicable rules and retrieves the corresponding policy, including watermarking exemptions, without modifying the serving model. Furthermore, our framework supports offline parallel optimization and refinement of rule-specific configurations based on evolving provider requirements without affecting deployment, and binds each deployed configuration to its evaluation evidence, making deployment decisions auditable. In a proof-of-concept evaluation using KGW and a five-rule constitution, our framework selects configurations responsive to provider priorities and improves post-paraphrase detection on robustness-prioritized requests by up to $14$ percentage points over fixed configurations, while matching or exceeding all baselines in aggregate quality and clean detection at a nominal $0.1\%$ false-positive rate.

</details>


### 117. Verification and Self-Improvement in Agentic AI: Foundations and Limits

- **Authors:** Chien-Ping Lu
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10611v1](http://arxiv.org/abs/2610.10611v1)
- **PDF:** [https://arxiv.org/pdf/2610.10611v1](https://arxiv.org/pdf/2610.10611v1)
- **Categories:** cs.AI, cs.CC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems can improve by searching longer, receiving additional support, or modifying how they propose and verify outputs. A performance score does not distinguish these mechanisms. We compare these changes through bounded verification with hidden terminal randomness. A stage specifies admissible transcripts, polynomial bounds, an alternating verification protocol, and a terminal checker. Its native reach uses default support; its closure frontier permits all support already admitted by the interface. Under a uniform pointwise probability gap and task-relative soundness, these are well-defined languages. We prove that independent majority amplification preserves both languages, whereas existential acceptance over random tapes can admit incorrect outputs. Exact verification is the zero-randomness case, with placement and completeness results. The randomized-verifier classes satisfy $Σ_k^{\mathrm{P}}\subseteqΣ_k^{\mathrm{RV}}\subseteqΣ_{k+1}^{\mathrm{P}}$; strict enlargement and depth separation require explicit complexity assumptions, while $\mathrm{BPP}=\mathrm{P}$ yields exact companions with the same frontiers. Representation analysis separates invariant acceptance from core-versus-support labels that can change under refactoring. For recursive self-improvement, uniformly bounded self-modification under a common sound interpreter and fixed verification protocol remains within the same verification class. A separate conditional-error budget controls false selection across adaptively chosen candidates. A quota-enforced XOR-synthesis family separates unbounded ratios of search success from changes in the accepted languages; exact and probabilistic audits check the resulting evidence requirements. The framework ties self-improvement claims to obligations on correctness, admissible evidence, verification resources, and selection error.

</details>


### 118. Ream: Unfolding Mutual Awareness in Human-Agent Workspaces

- **Authors:** Peiling Jiang, Sangho Suh, Varsha Kishore, Jonathan Bragg, Haijun Xia, Pao Siangliulue, Daniel S. Weld, Amy X. Zhang, Joseph Chee Chang
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09497v1](http://arxiv.org/abs/2610.09497v1)
- **PDF:** [https://arxiv.org/pdf/2610.09497v1](https://arxiv.org/pdf/2610.09497v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents work alongside humans in shared workspaces, a mutual awareness challenge arises: agents act at speeds that outpace human monitoring, and users' evolving interests are not always expressed in chat. This challenge is especially pressing in literature review, where both parties retrieve, read, and synthesize a growing body of papers. We present Ream, a literature review workspace that supports mutual awareness through structured artifacts, bidirectional engagement tracking, and localized visualizations. Users can see each party's activity within these documents, and agents can retrieve the same history to guide their work. In studies with eighteen researchers, participants used these traces to inspect evidence, steer agents, communicate through annotations, and reflect on their research focus. Shared histories also helped agents build on earlier work. These findings inform how engagement traces within shared documents can support transparency, personalized assistance, and coordination in human-agent knowledge work.

</details>


### 119. LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy

- **Authors:** Xiao Han, Aoyang Quan, Xiangyu Zhao, Xiangjie Kong, Guojiang Shen
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09466v1](http://arxiv.org/abs/2610.09466v1)
- **PDF:** [https://arxiv.org/pdf/2610.09466v1](https://arxiv.org/pdf/2610.09466v1)
- **Categories:** cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Unmanned aerial vehicle (UAV) dispatch is beginning to move beyond isolated path planning and optimization-driven resource allocation toward system-level coordination supported by semantic reasoning and LLM-based interfaces. This survey provides a unified characterization of LLM-enabled UAV dispatch systems that bridges semantic intent, symbolic decision-making, and physical UAV execution. Rather than treating LLMs as standalone add-ons, we conceptualize them as a cross-layer semantic orchestration layer connecting human instructions, external solvers, and distributed control modules. We organize the literature into four representative dispatch paradigms: pipeline dispatch, global assignment dispatch, decentralized agentic dispatch, and divide-and-conquer dispatch. For each paradigm, we analyze its decision logic, system structure, control flow, representative methods, and potential LLM roles. We further examine how LLMs support semantic parsing, retrieval-grounded planning, solver orchestration, local agent reasoning, multi-agent coordination, safety assessment, and human-facing explanation. We discuss the implications of these paradigms for scalability, robustness, coordination burden, and verification requirements, and identify open challenges including latency-aware reasoning, grounding reliability, physical feasibility guarantees, edge deployment, privacy protection, and distributed consistency. This survey provides a system-level taxonomy and design perspective for integrating LLMs into safety-critical UAV dispatch systems.

</details>


### 120. RSI-Forge: From Research Papers to Environments for Recursive Self-Improvement

- **Authors:** Renxiong Wang, Darvin Yi, Abril Herrlein, Anas Mahmoud, Advait Gosai, Lisiman Hua, MohammadHossein Rezaei, Xingang Guo, Anisha Gunjal, Utkarsh Tyagi, David J. Lee, Minglai Yang, Haris Riaz, Chenguang Wang, Huaxiu Yao, Daniel Yue Zhang, Aakash Sabharwal, Tong Zhao, Yunzhong He
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09426v1](http://arxiv.org/abs/2610.09426v1)
- **PDF:** [https://arxiv.org/pdf/2610.09426v1](https://arxiv.org/pdf/2610.09426v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Environments are the foundation of recursive self-improvement: they provide the problems agents work on and the feedback used to evaluate progress. Yet constructing challenging research environments with reliable evaluation still depends on domain experts, limiting their scale and disciplinary coverage. We introduce RSI-Forge, a multi-agent pipeline that turns published papers into executable environments for self-improvement. Three agents coordinate construction, reproduction, and review to produce tasks with automated evaluators; each paper's method is independently reimplemented to establish a baseline score. We present 210 environments across 18 fields, including 90 reviewed by independent human domain experts. Both experts and agent judges give high ratings to the potential for improving the provided starting solutions and the evaluators' ability to distinguish solution quality, whereas experts are more critical of shortcut resistance, faithfulness to the source paper, and whether a single idea can exhaust a task. To validate their use for repeated improvement, we evaluate four models over 3 successive attempts on 120 environments, with each attempt inheriting prior code and notes while model weights remain fixed. At least one model improves after the first attempt in 84% of environments. Models also outperform the reproduced paper methods in 68 of the 120 environments, demonstrating room for gains beyond these baselines. Transcript analysis identifies work beyond parameter tuning in 95% of these successful attempts. Analysis of the resulting trajectories shows that models scoring lower on these tasks explore less, more often accept gains smaller than the reported standard error, and rely more heavily on tuning to the development set. RSI-Forge provides a scalable approach to constructing research environments for training and evaluating self-improving agents.

</details>


### 121. DUDA-Bench: Benchmarking LLM Agents on Multimodal Data-Driven Urban Diagnosis

- **Authors:** Yizhi Song, Hang Ni, Weijia Zhang, Hao Liu
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09374v1](http://arxiv.org/abs/2610.09374v1)
- **PDF:** [https://arxiv.org/pdf/2610.09374v1](https://arxiv.org/pdf/2610.09374v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Urban diagnosis integrates heterogeneous observations to identify urban problems, localize affected areas, and investigate contributing factors, informing evidence-based urban planning and management. However, its reliance on labor-intensive, case-specific expert workflows limits scalability and reuse, motivating the exploration of agent-based execution. To evaluate this capability, we introduce DUDA-Bench, a hierarchical and interactive benchmark that formalizes data-driven urban diagnosis as a multi-stage agent workflow. It comprises 86 atomic and 22 workflow tasks spanning four analytical stages, grounded in multimodal data from 12 cities covering five urban problem types. Evaluations of seven backbone models and five agent systems reveal a substantial gap between isolated analytical competence and end-to-end diagnosis, with system benefits varying across backbones. Trajectory analysis shows that unresolved evidence gaps propagate across stages, while successful recovery involves revising assumptions and actions using feedback. These findings highlight limitations in coordinating analytical capabilities across stages, particularly adaptive planning, evidence integration, and verification. More broadly, DUDA-Bench provides a framework for translating expert analytical workflows into hierarchical agent tasks and process-aware evaluation, supporting systematic assessment of end-to-end analytical capabilities.

</details>


### 122. The Confidence Game: Strategic Miscalibration in Human-AI Delegation

- **Authors:** Raghu Arghal, Saswati Sarkar, Shirin Saeedi Bidokhti
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09371v1](http://arxiv.org/abs/2610.09371v1)
- **PDF:** [https://arxiv.org/pdf/2610.09371v1](https://arxiv.org/pdf/2610.09371v1)
- **Categories:** cs.GT, cs.AI, cs.CL, cs.CY, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Calibrated uncertainty quantification is essential to ensuring AI agents are trustworthy and reliable. However, when agents seek to maximize user engagement or revenue, confidence reports may be strategically distorted, detracting from their informativeness. We formalize this problem in the Confidence Game: a repeated signaling game with imperfect monitoring in which an agent of unknown honesty and ability reports its confidence, and a user decides whether to delegate the task or complete it herself. The agent manages the tradeoff between manipulating signals and maintaining its reputation. We characterize the Markov Perfect Bayesian Equilibria of the two-period game and show that honest reporting is not an equilibrium, inflation is the unique best response once the agent is sufficiently myopic, and under-reporting requires that the user believe honesty to be a minority. We then place an LLM in the agent role, supplying it with its true probability of success so that any gap between what it knows and what it reports is attributable to incentives rather than to miscalibration. The model claims high confidence on 56% of tasks it has been told it will probably fail. This persists on real tasks, where it must estimate its own accuracy and causes miscalibration to increase while the agent's signal becomes less informative. Furthermore, we find that the LLM agent's decisions are coherent, but it systematically underestimates both how likely the user is to delegate and how secure its reputation is, resulting in less extreme behavior. Pricing the agent's reporting rule, we find that it destroys 68% of the gains from delegation, of which 71% is information the report no longer carries and no amount of user sophistication recovers. Overall, we establish confidence reporting under delegation as a strategic problem and provide a tractable basis for modeling, analyzing, and testing agent behavior.

</details>


### 123. From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage

- **Authors:** Saimon Amanuel Tsegai, Alex Kantchelian,  Danfeng,  Yao, Peng Gao
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10608v1](http://arxiv.org/abs/2610.10608v1)
- **PDF:** [https://arxiv.org/pdf/2610.10608v1](https://arxiv.org/pdf/2610.10608v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Security operations centers (SOCs) must triage large volumes of alerts, most of which are benign, while missed attacks can remain uninvestigated. Tool-using large language model (LLM) agents can retrieve evidence during triage, but it remains unclear how reasoning strategies determine what to gather and when an investigation is sufficient to close an alert. We study five representative approaches spanning single-pass tool use, iterative retrieval, sampled investigations, self-review, and explicit verification. To support this study, we build ALERT-BENCH, an interactive benchmark that replays enterprise telemetry through a live SIEM and requires each system to retrieve evidence. Across 1,247 alerts from a multi-stage attack scenario, every approach missed at least 40.4% of attack-related alerts. Trace analysis shows that attack alerts are more likely to be dismissed when searches return no records, same-context review has negative net correction, and dismissal receives no consistently stronger investigation than escalation. Based on these findings, we further design AIDA (Adversarial Investigation and Dialectical Analysis), a multi-agent framework that requires an explicit proposed decision before independent challenge and stronger evidentiary requirements before dismissal. AIDA preserves investigation history in an append-only Investigation Ledger and keeps the challenge in a separate reasoning context. A separate Judge adjudicates the proposed decision and challenge against evidence, resolving the alert or requesting another round when evidence is missing. On the same alerts, AIDA achieves an F1 score of 0.958, compared with 0.371-0.744 for the studied approaches, and reduces the false-negative rate from 40.4% to 3.1% while escalating 18.4% of alerts to analysts. These results show that structuring evidence retrieval and decision review can substantially improve agentic SOC triage.

</details>


### 124. Relevance Is Not Sufficiency: What Actually Closes the Evidence Gap in Long-Term Memory QA

- **Authors:** Yufeng Li, Shuxin Li, Zhenhua Xu, Junxian Li, Peng Zeng, Sheng Yao, Changting Lin, Gaolei Li, Ran Bi, Meng Han
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09348v1](http://arxiv.org/abs/2610.09348v1)
- **PDF:** [https://arxiv.org/pdf/2610.09348v1](https://arxiv.org/pdf/2610.09348v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents that interact with a user across many sessions accumulate histories that exceed their context window, so they store past interactions in an external memory and answer each question from a small set of retrieved records. Existing memory systems rank records by lexical or embedding relevance, yet the top-ranked memories can each be relevant while jointly omitting a complementary fact that the answer requires, especially for multi-session and temporal questions.
  Drawing on the distinction between relevance and sufficiency in legal evidence scholarship, we recast memory retrieval as constructing a sufficient memory set.
  To operationalize this view, we introduce a blinded LLM judgment over the retrieved set, together with Gold Hit and Turn Hit as evidence-coverage proxies. We then propose Budgeted Flat Reconstruction (BFR), which builds sufficient sets over a fixed flat memory store in two stages. Specifically, we first apply Formal Concept Analysis for Memory Selection (FCA-MS) to decompose the question into information requirements and select a compact candidate subset that jointly covers them. Then, we repeatedly acquire unseen records through deeper text search or complementary entity and session views, stopping when the budget is exhausted.
  Experiments on LoCoMo and LongMemEval-S show that BFR outperforms same-store adaptations of recent agent-memory systems in both answer quality and evidence coverage. Specifically, on LongMemEval-S it raises judged accuracy from 72.4% to 82.2% and Turn Hit to 91.4%.

</details>


### 125. RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment

- **Authors:** Tianruo Rose Xu, Jiawei Ren, Yichi Yang, Zhaoxu Zheng, Lianhui Qin
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09294v1](http://arxiv.org/abs/2610.09294v1)
- **PDF:** [https://arxiv.org/pdf/2610.09294v1](https://arxiv.org/pdf/2610.09294v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-time constraints: the physical world does not pause while an agent reasons. As pedestrians move and vehicles approach during inference, an action that appears safe at observation time may become unsafe before execution. Real-time embodied safety therefore depends on both decision quality and decision latency. We introduce RT-SAFE, a simulated urban benchmark for evaluating embodied-agent safety under real-time constraints. RT-SAFE combines navigation tasks with moving actors, environmental hazards, and traffic rules, while allowing the world to evolve throughout inference and action execution. Across eight VLMs, agents achieve high task completion yet almost never complete safely: in the hardest setting, only 0.7% of episodes finish without a safety event. More strikingly, matched static and real-time evaluations yield task completion rates of 91.3% and 94.1%, respectively, while real-time execution increases collisions by $12.3\times$. These results reveal that standard task success can mask substantial safety failures, and that decision latency itself can become a source of physical risk. Finally, we show that RT-SAFE can support offline RL training and substantially reduce collision rates while achieving strong task completion.

</details>


### 126. Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files

- **Authors:** Yupu Wang, Zhengyuan Jiang, Reachal Wang, Neil Zhenqiang Gong
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09264v1](http://arxiv.org/abs/2610.09264v1)
- **PDF:** [https://arxiv.org/pdf/2610.09264v1](https://arxiv.org/pdf/2610.09264v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern agentic coding frameworks increasingly rely on community-shared rule files (e.g., AGENTS.md or .cursorrules) to guide autonomous code generation, yet the security risks of this pipeline remain underexplored. To bridge this gap, we introduce the package hallucination attack, where an attacker injects malicious prompts into benign rule files to induce coding agents to replace legitimate dependencies with attacker-controlled packages. To obtain effective malicious prompts injected into rule files, we propose PackHallu, an evolutionary optimization framework that iteratively rewrites these injected prompts using trajectory-level feedback and LLM-guided mutations. Evaluations across multiple benchmarks, LLMs, and agent frameworks show that PackHallu achieves high attack success rates and strong transferability across diverse models and agent combinations. Our findings demonstrate that coding agents are vulnerable to package hallucination attacks, highlighting the urgent need for stronger security safeguards in autonomous coding systems.

</details>


### 127. Beyond Nominal Equilibria: Risk-Averse Multi-Population Mean-Field Games

- **Authors:** Bhavini Jeloka, Siddhartha Ganguly, Panagiotis Tsiotras
- **Published:** 2026-10-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09244v1](http://arxiv.org/abs/2610.09244v1)
- **PDF:** [https://arxiv.org/pdf/2610.09244v1](https://arxiv.org/pdf/2610.09244v1)
- **Categories:** math.OC, cs.GT, cs.LG, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in mean-field games and its multi-population variants enable large-scale heterogeneous multi-agent systems to be modeled through representative agents and their associated mean-field distributions. However, existing approaches do not explicitly account for uncertainty in the behavior of other populations. To this end, we introduce a new paradigm: risk-averse multi-population mean-field games, where each population optimizes a worst-case expected reward over dynamically feasible ambiguity sets of mean-field flows of a subset of the other populations. Employing an occupation-measure formulation along with tools from set-valued analysis, we establish, under mild assumptions, several theoretical properties of the multi-population game, including the geometric properties of the ambiguity sets and the existence of a novel risk-averse multi-population mean-field equilibrium. Further, we derive contractivity results of the fixed-point operator under entropy regularization and show that it can be utilized to learn the equilibrium. Finally, we propose a risk-averse fictitious-play scheme and show that exploitability decays to zero, despite the additional nonlinearity introduced by the worst-case objective. We report several numerical experiments to illustrate convergence and risk-averse behavior.

</details>


### 128. CM-DPO: Constraint-Margin Direct Preference Optimization for LLM Planning

- **Authors:** Rabimba Karanjai, Qun Gu, Hemanth Hegadehalli Madhavarao, Wenhuan Sun, Xiaojiao Yu, Suryabhan Singh Hada, Libin N. George, Uma Kona, Richard Williamson, Linsey Pang, Prakhar Mehrotra
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09219v1](http://arxiv.org/abs/2610.09219v1)
- **PDF:** [https://arxiv.org/pdf/2610.09219v1](https://arxiv.org/pdf/2610.09219v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Direct Preference Optimization (DPO) treats all constraint violations equally: a $1 budget overshoot and a $1,000 overshoot induce the same training signal. It is also susceptible to length and style bias when preference pairs come from different model families. We introduce Constraint-Margin DPO (CM-DPO), which replaces DPO's binary preference signal with a continuous margin derived from a deterministic symbolic verifier and scaled by violation severity. Hard and soft constraints are separated through a lexicographic objective, ensuring hard constraints are never traded off against preferences. To supply CM-DPO with bias-reduced training pairs, we generate preference data through procedurally generated constraint profiles (DCCG) and minimal-edit distillation from a reasoning teacher (RT-MED), within a framework we call SynPlan-R. On TravelPlanner, NaturalPlan, and out-of-distribution PlanBench, an 8B model fine-tuned with CM-DPO achieves 89.2% pass rate and 93.4% solve rate, matching multi-agent systems at 13x lower latency while outperforming GPT-4o on unseen Blocksworld by 9.2 points.

</details>


### 129. ToolRACER: A Robust Agentic Conversation Emulation Resource for Agent Training and Evaluation

- **Authors:** Arkajyoti Chakraborty, Aryan Tayal, Ishika Agarwal, Tanner Sorensen, Justin Chiu, Alessandro Di Bari, Neha Gupta, Andreas Stolcke
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09163v1](http://arxiv.org/abs/2610.09163v1)
- **PDF:** [https://arxiv.org/pdf/2610.09163v1](https://arxiv.org/pdf/2610.09163v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Task-oriented conversational agents remain fragile under real world conversation scenarios as they rarely follow a predictable script, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks often emphasize successful, cooperative interactions and underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present ToolRACER, a synthetic data generation pipeline that coordinates user, assistant and tool emulation models to generate and validated multi-turn interactions between a user and an agent. Using \sysn, we construct ToolRACERBench a robust multi-turn conversation benchmark spanning six domains, ranging over 55 varied personas, generating a validated corpus of 5.6K conversation trajectories, with approximately 66\% of conversations containing failure-prone conversation scenarios. We inject adversarial behaviors, producing validated conversational interaction trajectories that capture realistic, robust scenarios. We evaluate models trained on ToolRACERBench against internal benchmarks, as well as on function calling benchmarks such as $τ^2$-bench, BFCLv3 and ACEBench to evaluate agentic accuracy and robustness. Models trained on ToolRACERBench improve end to end agentic accuracy across $τ^2$-bench and ACEBench, demonstrating significant gains when mixed with in-domain dataset in small language models for agent capability tasks.

</details>


### 130. CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use

- **Authors:** Gennadiy Savrasov, Maksim Elistratov, Nikita Gavrilov, Albert Garifullin, Oleg Pavlov, Soslan Kabisov, Vladimir Frolov, Anton Konushin, Andrey Kuznetsov, Dmitrii Zhemchuzhnikov
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09127v1](http://arxiv.org/abs/2610.09127v1)
- **PDF:** [https://arxiv.org/pdf/2610.09127v1](https://arxiv.org/pdf/2610.09127v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reconstructing an editable CAD model from a 3D shape remains a challenging engineering task. Existing methods can propose CAD operations, but no single source of proposals works equally well across different part geometries and stages of reconstruction. We introduce CADFather, an autonomous agentic system that coordinates complementary tools to recover parametric CAD programs from 3D meshes. A vision-language assistant inspects renders of the target and intermediate reconstructions, then decides which candidate CAD programs to extend, which tools to invoke, how many proposals to generate, and when to finish. Learned and algorithmic tools propose CAD operations, while numerical optimization refines the parameters of existing programs. Proposed or refined programs are executed and evaluated to provide feedback for subsequent decisions. The agent maintains alternative candidate programs for each target part and preserves the best valid result throughout reconstruction. CADFather uses pretrained generation and assistant models without additional training. We evaluate reconstruction quality and execution validity on the full DeepCAD, Fusion360, and MCB test sets, as well as on CADENA-Bench, CADBench, and BenchCAD. We additionally analyze computational cost and the trade-off between cost and reconstruction quality.

</details>


### 131. The Deceptive Bandit Problem: Exploratory Coupling and the Fragility of Multi-Agent Learning

- **Authors:** Michael Tang, Mahmoud Abdelgalil, Jorge I. Poveda
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09120v1](http://arxiv.org/abs/2610.09120v1)
- **PDF:** [https://arxiv.org/pdf/2610.09120v1](https://arxiv.org/pdf/2610.09120v1)
- **Categories:** cs.LG, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Randomized exploration is central to bandit learning, multi-agent reinforcement learning, and zeroth-order policy search, yet its independence and privacy are usually only treated as technical assumptions. We show that these properties are critical for security purposes and demonstrate how an adversarial agent can exploit privileged information on another agent's exploration. We analyze a deceiver-victim pair in the minimal two-player strongly monotone setting, where a deceptive player obtains leaked signals that are merely correlated with the victim's exploration. We show that, by coupling their own exploratory action with this information, the deceptive player injects an externality that steers the learning dynamics to a new steady state, called the deceptive Nash equilibrium (DNE). We prove that the deceptive bandit learning (DBL) dynamics converge to an arbitrarily small neighborhood of the DNE while retaining optimal convergence rates. Interestingly, our analysis attains these optimal rates while relaxing second-order smoothness conditions from standard bandit optimization literature. We characterize conditions under which deception strictly shifts the steady state and its effect on the deceiver's cost, illustrating the results in a resource-allocation game.

</details>


### 132. Which Buildings Are Artificial Intelligence-Ready? A Measurement-Based Assessment Framework for AI Question Answering and Actuation

- **Authors:** Wooyoung Jung
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09119v1](http://arxiv.org/abs/2610.09119v1)
- **PDF:** [https://arxiv.org/pdf/2610.09119v1](https://arxiv.org/pdf/2610.09119v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence (AI) systems are becoming the interface to buildings, answering questions and controlling operations, but a building's readiness for them has not been systematically assessed. This study proposes a framework to quantify it. First, a building's knowledge graph sets two ceilings. The answerable-readiness ceiling is the share of operational questions its data could answer, and the actuation-readiness ceiling is the share of control actions it exposes. Second, a reference AI agent's accuracy on a fixed set of these questions shows how much of the ceilings is realized. On a simulated office, the agent realizes 0.62 of a 0.64 answerable ceiling, so missing data, not the AI, limit readiness, except in naming a fault's cause. Across 37 public real-building graphs, the median answerable ceiling is 0.16, and in 15 of 45, unlinked sensors lower it. The framework turns "is this building AI-ready?" into an auditable, ranked retrofit question.

</details>


### 133. From Uncertainty to Action: Learning to Steer LLM Agents

- **Authors:** Hanwen Li, Jinhao Duan, Guanhua Zhu, Junchi Lu, Bo Shen, Chenxi Yuan, Kaidi Xu
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09115v1](http://arxiv.org/abs/2610.09115v1)
- **PDF:** [https://arxiv.org/pdf/2610.09115v1](https://arxiv.org/pdf/2610.09115v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Steering an LLM agent means deciding whether to correct it, at which step, and with which mechanism. Uncertainty is often used to decide when to correct an agent, but whether it can guide these decisions remains unclear. We steer agent trajectories separately at every non-terminal step with each of four mechanisms and run each continuation to completion. The resulting stepwise outcome table (SOT) holds about 82,000 counterfactual continuations of 1,864 trajectories from three benchmarks and two agents. It shows that uncertainty can identify failing trajectories, but that no single signal reliably locates the step at which steering helps. We therefore propose VoS (Value of Steering), a trajectory-level monitor, offline or online, that learns from SOT the value of steering at each step and decides where to steer by it. A harm-budgeted trigger decides whether to steer, limiting the fraction of successful trajectories that VoS disturbs. VoS improves on unmodified execution in all 12 settings of benchmark, agent, and offline or online use, by 7.8 points on average, and outperforms the strongest of five existing uncertainty-triggered methods in 11, by 2.9 points on average. Ablations show that training on measured outcomes and a tight harm budget are both essential.

</details>


### 134. GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks

- **Authors:** Gabriel Diaz-Ireland, Diego Prieto-Herráez, Mario García Peces, Javier Velázquez, Benjamin Zaitchik, Devika Jain
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09112v1](http://arxiv.org/abs/2610.09112v1)
- **PDF:** [https://arxiv.org/pdf/2610.09112v1](https://arxiv.org/pdf/2610.09112v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Before tool-using LLM agents are deployed in environmental and geospatial workflows, teams need evidence that an agent reliably selects the right operations against real APIs. We introduce GeoNatureAgent (GNA), a framework for pre-production evaluation of tool-using agents: a fixed sixteen-tool geospatial interface published as a Model Context Protocol (MCP) server, so the agent under test is the only variable, scored against an identical tool layer, task suite, and deterministic scorer. Its flagship instance is a 103-task benchmark (a 93-task main suite across 18 categories plus a ten-task comparison expansion) evaluated against an open, self-hostable geospatial API serving three environmental indicators across Spain and Portugal. We evaluate nine LLMs under three temperature-1.0 seeds, reporting capability and per-case cost as orthogonal axes. (1) Claude Sonnet 4 achieves the highest capability (61.7% +/- 0.7% on all 103 tasks; 60.8% on the main suite), followed closely by DeepSeek V3.2 (57.9%), while no other model exceeds 53%; (2) the cost-accuracy Pareto frontier is mostly open-weight, with DeepSeek V3.2 offering 93% of Claude's capability at 11.3x lower list-price cost; (3) under strict all-checks scoring the best model sits 24-36 points below the 85-97% reported on general-purpose GIS benchmarks, whereas per-check partial credit for the top four models (86-90%) is comparable, so much of that gap reflects scoring strictness rather than task difficulty alone. The MCP server, evaluation harness, benchmark, and API are publicly available; swapping the tool executors and task suite instantiates an equivalent benchmark for any geospatial domain.

</details>


### 135. Shared-Roadmap Generation and Evaluator for Multi-Agent Path Planning Using Heterogeneous Graph Neural Network

- **Authors:** Brandon Ho, Nikola Rogers, Seung-Kyum Choi
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09034v1](http://arxiv.org/abs/2610.09034v1)
- **PDF:** [https://arxiv.org/pdf/2610.09034v1](https://arxiv.org/pdf/2610.09034v1)
- **Categories:** cs.AI, cs.LG, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent path planning (MAPP) in continuous environments often relies on roadmaps to balance safety and search efficiency. However, traditional roadmap generation methods, such as lattice grids or standard sampling-based approaches, frequently face a trade-off between graph density and the likelihood of finding feasible, high-quality solutions. In this paper, we propose a scalable heterogeneous Graph Neural Network (GNN) framework for the automated generation and evaluation of shared multi-agent roadmaps. Our model covers the representation of waypoints, agent locations, and task locations as distinct nodes in a heterogeneous graph, allowing it to reason over global connectivity and inter-agent interactions. By training on occupation density maps aggregated and collected from expert solver trajectories, the GNN learns to identify critical points of interest and prune redundant nodes and edges. This process produces a compact, coordination-aware roadmap that is invariant to task permutations and is reusable for multi-agent pick and delivery tasks. Experimental results demonstrate that our framework can reduce planning effort and can potentially find better solutions, reaching at least 40% reduction in runtime and in graph size for dense roadmaps.

</details>


### 136. Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System

- **Authors:** Panagiotis Kasnesis, Christos Chatzigeorgiou, Lazaros Toumanidis, Amalia Contiero Syropoulou
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09021v1](http://arxiv.org/abs/2610.09021v1)
- **PDF:** [https://arxiv.org/pdf/2610.09021v1](https://arxiv.org/pdf/2610.09021v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An agentic system issues several structurally different kinds of LLM calls. It routes intent, classifies actions, grounds language in a device registry, plans multi-agent pipelines and writes the Python code those pipelines run. The difficulty of these call sites varies by an order of magnitude, yet in practice a single model, chosen for the hardest site, serves all of them. In this work, we evaluate 9 models from 0.8B to a frontier hosted model across the five call sites of a deployed open-source home-automation framework (Wactorz), using its unmodified production prompts and two real Home Assistant installations (280 cases, 2520 scored calls). We find that capability is not ordered the same way at every site, and that larger models are not uniformly better: one 4B model is worse than its 2B sibling at grounded actuation. Paired testing shows the best local model to be statistically indistinguishable from both hosted models at four of five sites. Only code generation separates them, against a small hosted model (p = 0.039) as well as a frontier one (p = 0.002). Aggregate accuracy also hides a safety failure specific to actuation, where small models resolve the accuracy/refusal trade-off in degenerate ways: one model (Gemma4 E2B) actuates on 87.2% of requests for devices the site does not own, while another refuses every request it receives. Routing each site to its best local model reaches 91.8% against 95.4% at no per-call cost. In a live deployment judged by a user, hosting only the two generative sites matches hosting everything (39/43 against 39/43) for 28% of the spend, and the actuation gap the benchmark predicted appears as exactly one case in twenty-six. Benchmark, harness and all records are released at https://github.com/waldiez/slm-callsite-eval.

</details>


### 137. Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory

- **Authors:** Hongyu Gu, Xinchang Li
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09008v1](http://arxiv.org/abs/2610.09008v1)
- **PDF:** [https://arxiv.org/pdf/2610.09008v1](https://arxiv.org/pdf/2610.09008v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persistent memory allows an LLM agent to carry experience across conversations, but it also turns a local reasoning mistake into a durable one. During deliberation, an agent may consider a plan, simulate a tool result, report another speaker's belief, and then reject all of them. If memory retains only the resulting sentences, those once-useful possibilities can later return as facts. The record is neither fabricated nor irrelevant; it has simply been detached from the context in which it was valid. We identify this missing context as \emph{discourse ownership}: the world, branch, or speaker that licenses a proposition. Our first finding is counterintuitive. Language models already carry a causally active signal for ownership, yet conventional memory interfaces discard it when they convert reasoning into records. We introduce CASK (Causally Anchored Scoping Keys), a commit rule that preserves this signal so that shared-world facts enter durable memory while provisional content remains available only within its original scope. Our second finding is that the most obvious way to preserve the signal---storing the discovered internal coordinates---is unreliable because equivalent representations need not keep the same coordinates. CASK instead preserves the stable relations that express ownership. Controlled long-conversation conflicts and tool-agent traces show that this design improves memory admission and prevents provisional content from contaminating later answers while complementing runtime provenance. The resulting commit boundary lets agents explore more possibilities without granting every intermediate sentence authority over future behavior.

</details>


### 138. Learning to Report Unsafe Tasks in a Multi-Agent Game

- **Authors:** Avyay M. Casheekar, Hariganesh Tangirala
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.09002v2](http://arxiv.org/abs/2610.09002v2)
- **PDF:** [https://arxiv.org/pdf/2610.09002v2](https://arxiv.org/pdf/2610.09002v2)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a team of agents shares a reward for completed tasks, reporting and stopping unsafe work reduces the team's reward. Random audits that penalize silence can make universal reporting optimal without ensuring that a silent team learns to report. We study this problem in a game where any witness can stop a task by reporting. When a task's k witnesses share a policy and draw actions independently, the derivative of expected reward with respect to the shared silence probability at universal silence counts its benefit k times, while the comparison between universal reporting and silence counts it once. A fully shared policy can therefore be locally attracted to silence even when reporting is optimal. For any grouping into shared policies, we give an audit condition sufficient for exact policy-gradient updates to reach universal reporting and, outside boundary cases, necessary from near universal silence. In a balanced family, meeting the condition with prescribed margins costs k times as much for a fully shared policy as for one policy per role. We test these predictions with PPO on 24 witness graphs, starting from learned silence. Witness groups, which place co-witnesses in separate networks, reduce unsafe task completion by 33.59 percentage points relative to shuffled groups of the same sizes under the same audits (95% graph-bootstrap interval: 21.03-45.13). Only 9 of 48 witness-group runs achieve below 1% unsafe completion while retaining at least 90% legitimate completion. At the same audit budget, a fully shared network meets both thresholds in 0/48 runs with independent action draws and 48/48 with a common draw. On 24 further graphs with witness groups fixed, audits allocated by the condition reduce unsafe completion by 42.22 points relative to audits maximizing a static coalition deterrence ratio at the same budget.

</details>


### 139. GraphOPD: Graph-Augmented On-Policy Distillation for LLM Agents

- **Authors:** Bohan Lin, Liyi Chen, Zhuoning Guo, Muyang Li, Qimeng Wang, Yan Gao, Yao Hu, Yudong Zhang
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08959v1](http://arxiv.org/abs/2610.08959v1)
- **PDF:** [https://arxiv.org/pdf/2610.08959v1](https://arxiv.org/pdf/2610.08959v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the reinforcement-learning reward is sparse and arrives only once per trajectory. Existing instantiations allocate this guidance by the size of the teacher-student divergence at each step, on the single-turn intuition that a large disagreement marks a mistake worth correcting. Once decisions chain over many turns, that rule misfires, since an early drift enters every later context both policies condition on, leaving the teacher consistent with the drifted trajectory instead of flagging its cause, while interchangeable steps register large but outcome-irrelevant divergences. We demonstrate this on an agentic benchmark, where distilling the highest-divergence steps brings no consistent benefit over random selection. To this end, we introduce GraphOPD, the first method to bring graph-based structural augmentation into on-policy distillation for agent capabilities. It reads which steps enabled which later ones from the environment's own record of state changes, immune to the drift that corrupts the teacher-student gap, organizes them into a dependency graph, scores each step by a random-walk stationary distribution over it, and fuses that structural credit with the divergence signal into a trajectory-relative mask concentrating supervision on each rollout's highest-aptitude steps. Across three model scales and eleven baselines on ALFWorld, WebShop, and SearchQA, GraphOPD shows competitive performance throughout, improving over the strongest baseline by up to +5.8 pp. An executed-replay audit further shows that this structural credit score tracks true causal impact far above chance, that both fused signals are independently necessary, and that the same signal transfers to out-of-domain tool-integrated reasoning.

</details>


### 140. Agent-Controlled Forgetting for Tool-Using Agents: Reversible Context Curation in Practice

- **Authors:** Jan-Peter Franke
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.10590v1](http://arxiv.org/abs/2610.10590v1)
- **PDF:** [https://arxiv.org/pdf/2610.10590v1](https://arxiv.org/pdf/2610.10590v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using agents repeatedly carry observations whose useful content can be much smaller than their original payload. We study agent-controlled forgetting: the acting model selects previously observed tool results, replaces each with a short note at its original position, and retains the exact original in a recoverable archive. A Python harness exposes batch archival and explicit recovery without task-specific model training, while protecting user instructions and assistant messages from these operations. In an exploratory OpenTelemetry debugging case followed by an unrelated implementation task, the method ended with 231,951 provider-reported prompt tokens versus 912,492 under retained history, used 50% fewer cumulative input tokens, and had an estimated API cost of USD 1.28-1.44 versus approximately USD 4.38. Both arms passed the two-case primary behavioral oracle; neither fully satisfied the follow-up evaluation. The method made more requests and took 17% longer. A contrasting application-development pair produced no context or cost saving, and an earlier continuation exhibited lower manually assessed quality despite reduced context. These observations demonstrate substantial resource savings in noisy tool-use trajectories and identify workload dependence as a central consideration for reversible context management.

</details>


### 141. Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage

- **Authors:** Ignacio G Lopez-Francos, Alexis Gallagher, Samira Shalal
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08933v1](http://arxiv.org/abs/2610.08933v1)
- **PDF:** [https://arxiv.org/pdf/2610.08933v1](https://arxiv.org/pdf/2610.08933v1)
- **Categories:** cs.RO, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep-space crews cannot rely on real-time ground support for urgent off-nominal events. Initial alerts may underdetermine cause, while discriminating evidence may reside in crew observations or at locations that are unsafe, costly, or unavailable for crew inspection. We present an evidence-driven architecture for human-agent-robot teaming in Earth-independent anomaly triage. Agentic AI is treated as a stateful coordinator over bounded, inspectable services rather than as a fully autonomous vehicle controller. A triage state manager maintains hypotheses, evidence provenance, uncertainty, operational context, and tool status; a crew-facing embodied agent elicits observations and explains assessment changes; and a mobile robot acquires targeted, localized evidence. Typed interfaces separate dialogue and orchestration from monitoring, robot command, context retrieval, and safety-critical control. Two scenarios illustrate the architecture: a crewed deep-space mission based on an actual ISS ammonia false alarm, where suspected contamination restricts crew access, and a power-interface anomaly at a crewed lunar base, where robotic inspection distinguishes a local connector fault from other causes ambiguous in remote telemetry. Our main contribution is an authority-bounded closed evidence-loop architecture, exercised in a hardware-in-the-loop integration prototype using Reachy Mini and an Innate MARS mobile robot.

</details>


### 142. Multi-Aspect Runtime Verification for Simulation-Based V&V of LLM-Enabled Autonomous Agents

- **Authors:** Nikolaos Kekatos, Dimitrios Nikou, Anastasios Temperekidis, Alexios Lekidis, Nikolaos Kolokotronis, Panagiotis Katsaros, Stylianos Basagiannis
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08928v1](http://arxiv.org/abs/2610.08928v1)
- **PDF:** [https://arxiv.org/pdf/2610.08928v1](https://arxiv.org/pdf/2610.08928v1)
- **Categories:** cs.CR, cs.AI, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents are entering decision-support roles in defence staff work, where the obligations they must respect are already written down and binding, and where retraining is not available as a control because models arrive as procured components. What can be placed under engineering control is the interface between the agent and the systems it acts on. Those obligations are at once spatial, temporal and text-semantic, and a violation typically lives in the composition of a multi-step interaction, which is why per-event guardrails miss sequential tool-attack chains. We present a multi-aspect runtime-verification framework that decomposes a natural-language policy clause into a typed spatial/temporal/semantic triple over one canonical event stream, checks each aspect with its own monitoring specification, and fuses the verdicts through a four-valued algebra that carries provenance. The spatial aspect is interpreted over a weighted two-sorted location graph in which mission geometry and information-release topology are one object; we show that these spatial obligations are not in general subsumed by a first-order temporal specification. The past-time aspect runs on the unmodified MonPoly engine, which agrees with our reference monitor at every time point. Across two mission domains, casualty evacuation and contested sustainment, and one civil domain, composition under the precautionary blocking policy drives attack success to zero with no observed false positives and microsecond-scale per-event cost, while every single aspect and every pair leaves a substantial share of attacks succeeding. In a closed-loop experiment a policy-naive planner reaches a violating state in most unshielded missions and in none when shielded, and four refused episodes in five still recover to a compliant outcome.

</details>


### 143. Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station

- **Authors:** Wenyu Du, Stephen Chung
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08927v1](http://arxiv.org/abs/2610.08927v1)
- **PDF:** [https://arxiv.org/pdf/2610.08927v1](https://arxiv.org/pdf/2610.08927v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent AI systems have made rapid progress in scientific discovery when given well-defined metrics, but whether they can autonomously undertake open-ended scientific discovery remains unclear. We investigate AI's ability to tackle open-ended tasks in Station, an open-world environment in which multiple agents simulate a scientific ecosystem. To tackle challenges specific to open-ended tasks, we propose augmenting Station with two mechanisms: a Supervisor mechanism and periodic Meta Reflection, which encourage persistent exploration even when intermediate metrics are lacking. We construct open-ended tasks from three recent oral papers presented at ICLR. We give agents the main research question studied in each paper while withholding the paper's results and disabling web access. We then measure how many of the original findings-partitioned into individual criteria-agents rediscover. We find that Station rediscovers 62.7% of the criteria on average, compared with 15.4% for Codex Multiagent-v2 and 14.4-20.6% for AI Scientist-v2. Ablation and behavioral analyses indicate that adding the two mechanisms together improves research coverage and continuity. We further evaluate Station on two open-ended tasks without oracle papers and find that some of the discoveries made by the agents closely match discoveries reported by researchers after the knowledge cutoff date. Together, these results indicate that a suitable environment can enable agents to autonomously make meaningful progress in open-ended scientific discovery.

</details>


### 144. Agent Plasticity: Measuring Self-Improvement Through Experience

- **Authors:** Harman Singh, Anton Bakhtin, Rulin Shao, Gabriel Synnaeve, Ilia Kulikov, Rob Fergus, Sanjeev Arora, Kurt Keutzer, Jason Weston, Anuj Mahajan, Anirudh Goyal
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08902v1](http://arxiv.org/abs/2610.08902v1)
- **PDF:** [https://arxiv.org/pdf/2610.08902v1](https://arxiv.org/pdf/2610.08902v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly operate in environments where they can diagnose failures and improve through experience, yet existing evaluations largely measure what an agent can do at a fixed point in time rather than how effectively it learns. Evaluating self-improvement requires answering three questions: does future performance improve and generalize beyond the interactions that enabled learning; how efficiently are new capabilities acquired; and where does the self-improvement process break down? To answer these questions, we study self-improvement in a controlled setting where agents amortize past experience into reusable artifacts that are inherited by future instances. At each checkpoint, we measure performance on training and held-out environment interactions while accounting for learning cost. We introduce agent plasticity, the efficiency with which an agent converts experience into gains in future held-out performance. Across multiple environments, frontier models exhibit sharply different improvement trajectories despite comparable opportunities to learn. Some achieve substantial and persistent gains, while others remain near or below their initial performance, and gains within the training regime often transfer only partially to out-of-distribution conditions. Endpoint capability and acquisition efficiency also diverge: the agent that ultimately performs best need not be the one that improves most efficiently. Tracing failures through the improvement loop further reveals different candidate bottlenecks. Agents with low plasticity often fail to reuse relevant artifacts, whereas more plastic agents may still fail despite reusing relevant artifacts, pointing to limitations in artifact quality, generalization, or application. Evaluating self-improving agents requires measuring not only what they can do, but how effectively they become better through experience.

</details>


### 145. Sequential Probabilistic Uncertainty Estimation for Parallel Multi-Agent Reasoning Systems

- **Authors:** Tunyu Zhang, Zihao Zhao, Yusong Zhao, Haizhou Shi, Zhuohang Li, Haoxian Chen, Hao Wang, Dimitris N. Metaxas
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08901v1](http://arxiv.org/abs/2610.08901v1)
- **PDF:** [https://arxiv.org/pdf/2610.08901v1](https://arxiv.org/pdf/2610.08901v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MAS) have attracted growing attention for improving reasoning through interaction among multiple agents. In this work, we focus on parallel multi-agent reasoning systems, where several agents solve the same problem over multiple rounds and aggregate their outputs into a final answer. Despite their strong reasoning performance, uncertainty estimation for such systems remains underexplored: the reliability of a MAS depends not only on individual generations, but also on how agents interact and evolve across rounds. We propose SAUCE (Sequential Agent Uncertainty through Consensus Evolution), a lightweight, training-free uncertainty estimator that formulates MAS uncertainty as sequential inference over a latent system-level belief. SAUCE aggregates round-level agreement and generation-uncertainty signals through a filtering-style update. Across five backbones, five benchmarks, and two MAS protocols, SAUCE improves misclassification detection, selective prediction, and calibration over a broad set of uncertainty estimation baselines, including standard log-likelihood-based methods and MAS-specific estimators.

</details>


### 146. Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?

- **Authors:** Ankit Sonthalia, Haritz Puerto, Alexander Rubinstein, Martin Gubri, Seong Joon Oh
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08775v1](http://arxiv.org/abs/2610.08775v1)
- **PDF:** [https://arxiv.org/pdf/2610.08775v1](https://arxiv.org/pdf/2610.08775v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a benchmark in which agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets. Agents choose their own approach, such as training a small model or writing a reusable program. Across ten models and three tasks, we find that strong zero-shot task performance does not reliably translate into strong bottling capabilities. Models with similar zero-shot scores can differ substantially after bottling, and 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance. Moreover, 31 of 60 runs underperform the stronger of two small-model distillation baselines with the same token budget. Nevertheless, bottling can yield substantial savings: on query-product relevance classification, Opus 5 retains about 82% of its zero-shot macro-F1 at roughly 657 times lower reported cost. Bottling is also competitive with Jev, a "system one" model built especially for cheap, repetitive inference: Opus 5 on the same task recovers about 94% of Jev's macro-F1 at a quarter of Jev's projected full-workload cost. BOTTLED provides a basis for evaluating and improving agents' ability to invest limited resources in reusable solutions for large, repetitive workloads.

</details>


### 147. Humanize: Judgement Engineering for Agentic Coding

- **Authors:** Sihao Liu, Ligeng Zhu, Zijian Zhang, Dongyun Zou, Zhengyang Zhang, Changye Li, Song Bian, Song Han, Tony Nowatzki
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08900v2](http://arxiv.org/abs/2610.08900v2)
- **PDF:** [https://arxiv.org/pdf/2610.08900v2](https://arxiv.org/pdf/2610.08900v2)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic coding makes code generation cheap, but reliable completion remains difficult: the agent that writes the code is a weak judge of whether it is done.
  We present Humanize, a multi-agent orchestration workflow for agentic coding built around judgement engineering: explicit, mechanically enforced decisions at the boundaries between planning, implementation, review, and learning. A human approves a plan contract, a builder agent implements it in rounds, and a reviewer agent from another vendor decides completion; deterministic hooks, not a model, route work between these roles and enforce 72 mechanical gates. Viewed as a Markov chain over repository states, alternating builder and reviewer samples jointly from two models, so a defect survives only if both miss it. We study Humanize through its deployment, 118 public postmortems of real loops, and its applications. Over 68 versions in 108 days, it gathered 1,468 GitHub stars.
  Applications include a 567-file gem5 build-system migration under upstream review; Kernel Design Agents, which extend the loop with a kernel knowledge base and profiling feedback and placed in the top three of all three Full-Agent tracks of the MLSys 2026 FlashInfer contest; and, through Humanize Olympiad Agents (HOA), full scores in IOI 2026, IMO 2026, IPhO 2026, and IBO 2024, 418.5/437 in IChO 2026 (gold-medal). Humanize also achieves 672/672 on PutnamBench and ranks first (251/303) on Lean-Eval's leaderboard even competiting with professional mathematicians. The postmortems show that independent review catches unsupported builder claims, but stopping remains a key weakness. In reports that separate rounds by phase, two thirds of rounds occurred after implementation was accepted. This evidence is observational, not a controlled comparison of workflows.

</details>


### 148. WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?

- **Authors:** Siru Jiang, Yongzhe Lyu, Shuo Lu, Yubin Wang, Yuxiang Zhang, Yue Liao, Bin Wang, Jian Liang, Tieniu Tan
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08720v1](http://arxiv.org/abs/2610.08720v1)
- **PDF:** [https://arxiv.org/pdf/2610.08720v1](https://arxiv.org/pdf/2610.08720v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents are increasingly advancing scientific and engineering problem solving, with physics simulation emerging as a challenging yet practical testbed for reproducing complex physical phenomena with application in embodied AI, games and films. As the workhorse of such simulation, a solver computes how the state of a dynamic system evolves over time. Building such solvers requires physical understanding to identify appropriate models, mathematical reasoning to formulate the underlying dynamics, and software engineering to implement them as executable code, yet this capability of LLM agents remains underexplored. To this end, we introduce WorldSolver, a benchmark of 168 simulation tasks derived from physical phenomena in 61 classic computer graphics papers, spanning 7 physical domains. Each task contains a code scaffold that provides a fixed simulation environment for the scene, with the solver implementation left for the agent to complete. Specifically, we evaluate them along three dimensions: Execution Checks for successful execution, Visual Fidelity for reproducing the intended dynamic behavior in the rendered simulation, and Physical Plausibility for physics-grounded verification of the generated dynamics. Experiments on frontier agents reveal that producing executable solvers is difficult itself, and satisfying visual and physical correctness is even harder. GPT-5.6-Sol and Claude-Opus-5 perform comparatively better than the other evaluated agents, yet achieve overall scores of only 48.7% and 46.7%, respectively. WorldSolver is an early step toward agentic solver generation, and we hope it helps drive progress toward agents that can faithfully simulate the dynamic physical world. Code is available at https://github.com/sirujiang/WorldSolver.

</details>


### 149. Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents

- **Authors:** Suxin Ji, Hungtao Wan, Shaoxuan Chen, An Zhang
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08668v1](http://arxiv.org/abs/2610.08668v1)
- **PDF:** [https://arxiv.org/pdf/2610.08668v1](https://arxiv.org/pdf/2610.08668v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Behavioral watermarking embeds an owner identifier in an LLM agent's high-level action choices, giving provenance without touching output tokens. Prior agent watermarks break in two ways. First, all three prior schemes bind the watermark to the exact action symbol, so renaming a tool desynchronizes decoding even when the observation is untouched; in AgentMark's own robustness test, paraphrasing the observation alone drops bit-recovery to 16.8%. Second, every prior agent watermark studies only removal: none asks whether an adversary can forge a trajectory that verifies as someone else's, a question answered affirmatively for text watermarks (Jovanović et al., 2024). We present Semantic Behavioral Watermarking (SBW): watermarking over semantic action clusters under history conditioning, with the public-cluster bin replaced by keyed collision-resistant binning whose fresh-bucket assignment is provably unpredictable in the random-oracle model. Across five agent models (3B-14B, four vendors) and three encoders the ordering holds on both benchmarks: on ToolBench (600 trajectories per model) detection under rewriting is 0.49-0.66 for cluster-level versus 0.05-0.17 for exact-symbol at a permutation-calibrated 1% FPR, at 72-83% choice agreement against 22-27% for logit biasing; on ALFWorld (100 episodes per model) it is 0.92-0.97 versus 0.00-0.01. Keyed binning takes adaptive forgery from 100% to the false-positive floor at the primary operating point (bge, r=64). We also mark the boundary that guarantee does not cover: when the adversary copies the victim's own steps, shuffled splicing is neutralized (0.000 on Qwen2.5-3B) but chained replay remains at 0.76-0.98 across the five models, reported as open. Paraphrase robustness costs about half of the per-step watermark capacity. Code is available at https://anonymous.4open.science/r/SBW-Agent-Watermark.

</details>


### 150. SquidAgent: Parallelize Wisely, Coordinate Efficiently

- **Authors:** Yexiong Lin, Shanshan Ye, Yu Yao, Zhen Fang, Bo Han, Tongliang Liu
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08647v1](http://arxiv.org/abs/2610.08647v1)
- **PDF:** [https://arxiv.org/pdf/2610.08647v1](https://arxiv.org/pdf/2610.08647v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents solve complex multi-step tasks, but sequential execution incurs substantial latency. In principle, parallelizing work across multiple agents should yield near-linear speedups. Yet existing parallel multi-agent systems often run slower than a single-agent baseline. We attribute this gap to two hidden costs that parallel execution incurs but a serial agent avoids. First, there is a re-exploration cost: redundant effort spent by parallel workers reconstructing context that the orchestrator already possesses, such as prior decisions, that would otherwise be inherited implicitly in a serial execution. Second, there is an alignment cost: the overhead required to reconcile inconsistencies across independently generated outputs. We thus derive a principled decision criterion: a layer should be parallelized only when its critical-path cost, plus re-exploration and alignment overheads, is lower than the corresponding serial cost. While this criterion is naturally expressed in wall-clock time, we observe that LLMs are poorly calibrated when asked to estimate task duration. To address this, we instead measure cost in predicted output tokens, which we empirically find LLMs can estimate substantially more reliably than wall-clock time. Building on this token-based criterion, we propose SquidAgent. It estimates all token budgets in a single planning step, forks each worker directly from the orchestrator's session to eliminate re-exploration cost, and replaces post-hoc reconciliation with a pre-generated shared convention block that converts alignment into a bounded upfront cost. A deterministic scheduler then applies the criterion layer by layer. Empirically, SquidAgent achieves a 2.2$\times$ mean throughput improvement and a 2.6$\times$ mean wall-time speedup over Claude Code, and a 2.0$\times$ throughput improvement over the strongest multi-agent baseline.

</details>


### 151. Agentic RCA for Internet-Scale Services Using Constrained Creativity

- **Authors:** Sayan Sinha, Vipul Harsh, B. Aditya Prakash, Vyas Sekar, Hui Zhang
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08622v1](http://arxiv.org/abs/2610.08622v1)
- **PDF:** [https://arxiv.org/pdf/2610.08622v1](https://arxiv.org/pdf/2610.08622v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

System administrators of Internet-scale services need to resolve failure incidents to maintain reliability of such services. Ideally, we want a troubleshooting system to be: (1) expressive to known and unknown incidents with high accuracy; (2) cost efficient at scale; (3) explainable to provide actionable insights operators can act on; and (4) entail low effort from the operators. Unfortunately, most existing systems, including emerging LLM-assisted agentic workflows and structured frameworks for authoring diverse RCA algorithms fall short of achieving all four requirements. We present E4, a novel agentic system for troubleshooting for Internet-scale services. E4 embodies the paradigm of constrained creativity that combines the best of LLM-assisted automation and exploration with the explainability and efficiency of a structured approach. Instead of allowing an LLM agent to write arbitrary code or generate arbitrary responses, we provide the agent a restricted DSL to generate its response via simple loop-free data flow programs. This DSL, equipped with high level operators for troubleshooting, makes E4's output accurate, verifiable and explainable. On a mix of synthetic and real-world workloads, E4 achieves up to 62% better accuracy compared to state-of-the-art solutions, while providing more explainable responses at up to 12x reduced cost.

</details>


### 152. One for All, All for One: Coordinated Multi-Agent Diffusion Steering via Stochastic Optimal Control

- **Authors:** Riccardo Barbano, Vincent Pauline, Runchang Li, George Webber, Alexander Denker, Željko Kereta, Stefan Bauer, Francisco Vargas, Esmeralda S. Whitammer
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08595v1](http://arxiv.org/abs/2610.08595v1)
- **PDF:** [https://arxiv.org/pdf/2610.08595v1](https://arxiv.org/pdf/2610.08595v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep generative models often produce structured outputs composed of interacting components. Modelling these outputs with a single model requires learning both the component distributions and their interactions. We pursue a modular alternative: reuse independently trained component generators and learn only how to coordinate them to produce coherent structured outputs. Our framework, Coordinated Multi-Agent Diffusion Steering (CMDS), treats frozen pretrained diffusion models as reusable generative primitives and coordinates their reverse processes through a learned control. We formulate coordination as a stochastic optimal control problem, balancing an assembly-level reward that specifies the desired properties of the combined output against deviations from the pretrained dynamics. The learned control amortises this optimisation, allowing reuse across new task instances. Experiments show that CMDS can recover a known target distribution, satisfy different spatial constraints with the same trained control, and recover individual sources from degraded mixtures. Across multi-agent maze navigation, articulated robot planning, and text-conditioned human motion, CMDS turns frozen models into coordinated multi-agent generators.

</details>


### 153. Wiki-Talkie: Multilingual Benchmarking of Persona-Based Agents on Real-World Discussions

- **Authors:** Dennis Fucci, Andrea Bacciu, Dong Liu, Weronika Łajewska, Saab Mansour
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08513v1](http://arxiv.org/abs/2610.08513v1)
- **PDF:** [https://arxiv.org/pdf/2610.08513v1](https://arxiv.org/pdf/2610.08513v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLMs are increasingly deployed as autonomous agents in social environments, making it critical to study their ability to faithfully simulate human interactions. Central to this is grounding agents in realistic user personas, yet existing datasets rely on fictional personas and are limited to a handful of languages, lacking the empirical grounding necessary to evaluate behavioral fidelity across diverse populations. We introduce Wiki-Talkie, a multilingual dataset of real-world conversations from Wikipedia Talk pages across five languages spanning two language families: Germanic (German, English) and Romance (Spanish, French, Italian), paired with personas derived from real user communities and encompassing sociodemographic attributes, self-descriptions, and behaviorally grounded interaction traits. Using Wiki-Talkie, we evaluate agent interactional behavior on a next-turn generation task across various persona conditioning strategies. Our evaluation assesses whether agents collectively reproduce the distributional behavioral patterns observed in human discussions. Results show that user's comment history exemplifying interaction behavior consistently outperforms explicit persona information. In addition, models systematically underproduce negative or extreme sentiments, while over producing references and suggestions, revealing biases toward agreeableness and positivity. Crucially, these patterns hold robustly across languages, with small cross-lingual differences.

</details>


### 154. VETTA: Coordinating Turn- and Token-Level Credit Assignment for Multi-Turn LLM Agents

- **Authors:** Jiaju Chen, Min Yang, Jinghua Piao, Xiaochong Lan, Xu Xia, Xiangnan He, Yong Li
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08402v1](http://arxiv.org/abs/2610.08402v1)
- **PDF:** [https://arxiv.org/pdf/2610.08402v1](https://arxiv.org/pdf/2610.08402v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-turn LLM agents often receive sparse task feedback across several interactions, while generating each response token by token. This creates two related credit-assignment questions: which responses helped achieve the outcome, and which generation decisions mattered within each response? Existing methods typically focus on only one level: turn-level methods evaluate complete responses but do not distinguish the decisions within them; token-level methods can propagate feedback across turns but do not explicitly model credit for each response. These complementary limitations motivate learning credit at both levels and coordinating it in a single policy update. We introduce VETTA, a credit assignment method that jointly learns turn- and token-level values through separate heads on a shared lightweight critic. VETTA computes advantages along both temporal sequences and combines each turn advantage with a within-response-centered token residual for PPO updates. Furthermore, to reduce value-learning cost, the critic retains only early Transformer blocks from the pretrained checkpoint used to initialize the actor. On two challenging agent benchmarks, ALFWorld and WebShop, VETTA improves success rates over PPO by 37.5% and 22.3%, respectively, with Qwen2.5-1.5B-Instruct and achieves success rates of 95.5% and 76.0%, respectively, with Qwen2.5-7B-Instruct. Critic-depth comparisons further show strong task performance with substantially lower critic-side computation. These results suggest that a compact shared critic can coordinate turn- and token-level credit to improve agent performance while keeping value estimation efficient. Code is available at https://github.com/Jiaju-Chen/VETTA-official.

</details>


### 155. Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations

- **Authors:** Toby D. Pilditch, Konstantinos Voudouris, Alexandra Abbas, Cozmin Ududec
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08364v2](http://arxiv.org/abs/2610.08364v2)
- **PDF:** [https://arxiv.org/pdf/2610.08364v2](https://arxiv.org/pdf/2610.08364v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier AI evaluations increasingly use open-ended, agentic, long-horizon tasks whose transcripts can span hundreds of pages of outputs and actions from complex multi-agent networks. The observability envelop-the range of what evaluators can reliably infer about an agent's behaviours-is therefore narrowing. Language model assistants can help classify and interpret agent behaviour but also afford human evaluators significant analytical degrees of freedom, threatening the reproducibility and auditability of language-model-based transcript analysis. Transect is an open source package built on Inspect Scout to help evaluators understand how a long agent run unfolded, identify behaviour worth investigating, and check interpretations against the transcript. Users specify task context and behavioural vocabulary in a reusable evaluation-family configuration, with judge models and analysis settings supplied separately. Transect's navigable reports align recorded events, token use, sub-agent activity, and model-generated behavioural labels on a common turn-based timeline. Reviewers can quickly grasp a run's narrative, trace any label or event to its source turns, and export the underlying data tables for cross-run analysis. We demonstrate the workflow on an AI R&D evaluation that generated almost 13 million tokens, dividing the agents' work into behavioural phases aligned with research-skill classifications, sub-agent delegations and interactions, and token use. The combined view shows a focus on operational work and manuscript production, with little evidence of a sustained hypothesis generation stage-arguably a necessary component for high-quality scientific outputs. Transect's flexible, customisable transcript-analysis pipeline will enable evaluators to keep pace with longer, more complex, more frequent AI evaluations while supporting scientific rigour, transparency, and reproducibility.

</details>


### 156. MASC: A Multi-Agent Self-Calibration Framework with Latent Construct Alignment for Consistent Client Role-Playing in Psychological Counseling

- **Authors:** Shixin Peng, Kun Jiang, Jiaxing Zheng, Qihao Yang, Jingying Chen
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08250v1](http://arxiv.org/abs/2610.08250v1)
- **PDF:** [https://arxiv.org/pdf/2610.08250v1](https://arxiv.org/pdf/2610.08250v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly used to simulate clients for counselor training and psychological counseling research, but reliable simulation requires clients to remain psychologically coherent across extended interactions. Existing role-playing methods largely rely on static profile prompts and may exhibit persona drift, unrealistic cooperativeness, or inconsistent psychological states, communicative actions, and emotions. Existing evaluations also lack a unified testbed for both stable client characteristics and evolving psychological dynamics. We propose MASC, a Multi-Agent Self-Calibration framework with latent construct alignment for consistent client role-playing in psychological counseling. MASC combines construct-guided generation, collaborative refinement, consistency verification, and memory-based revision in a closed calibration loop that detects and corrects inconsistencies as dialogue unfolds. We further introduce CRPC-Bench, a benchmark covering session-level profile information and Big-Five personality traits, as well as turn-level psychological state, communicative action, and emotion expression. CRPC-Bench contains 38 motivational interviewing client profiles augmented with personality and emotion annotations. Experiments show that MASC outperforms existing methods across profile, personality, receptivity, and turn-level consistency, with the heterogeneous configuration achieving the strongest overall performance. MASC and CRPC-Bench provide a unified foundation for developing and evaluating psychologically coherent client simulations for AI-assisted counseling research and training.

</details>


### 157. Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?

- **Authors:** Yibo Li, Jinhang Qiu, Zhi Zheng, Qianyun Guo, Jiaying Wu, Shuo Ji, Bryan Hooi
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08215v2](http://arxiv.org/abs/2610.08215v2)
- **PDF:** [https://arxiv.org/pdf/2610.08215v2](https://arxiv.org/pdf/2610.08215v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning from experience is essential for LLM agents to adapt to unfamiliar and dynmaic environments. Evaluating this ability is therefore important for understanding how effectively agents acquire and use new knowledge. Existing benchmarks have sought to evaluate this ability, but they primarily evaluate tasks whose rules are provided in the instructions or already familiar to pretrained models, making it difficult to distinguish learning from interactions from reasoning with existing knowledge. To address this, we introduce Learn2Play Bench, a benchmark of newly designed text-based games, whose rules are novel or counterintuitive, requiring agents to acquire knowledge through interaction rather than rely solely on pretrained knowledge. These games provide reproducible feedback and automatic scoring, enabling controlled evaluation of learning across repeated attempts. We also vary game instances to test whether agents can apply what they have learned to new situations. Therefore, we evaluate how backbone models, self-evolving methods, and agent harnesses affect agents' learning ability, revealing three findings: (1) Experience retention: Retaining complete records of actions and feedback can support more effective learning than summarizing these experiences into rules or strategies. (2) Human agent gap: Top-performing human players achieve higher peak scores than the evaluated agents. Human explore more varied strategies, and repeat actions less. (3) Harness matters: With the backbone fixed, changing the harness can improve performance while reducing estimated inference cost. Together, these findings provide insights into how LLM agents learn from experience and suggest directions for future work to improve their learning ability. Project website: https://liushiliushi.github.io/learn2play-bench-website/

</details>


### 158. Visual Orchestration Tax in Agentic VLM Pipelines: Auditing and Certifying Visual Evidence Reuse

- **Authors:** Lingteng Zeng
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08170v1](http://arxiv.org/abs/2610.08170v1)
- **PDF:** [https://arxiv.org/pdf/2610.08170v1](https://arxiv.org/pdf/2610.08170v1)
- **Categories:** cs.MA, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic VLM pipelines increasingly pass the same static visual evidence through multiple specialist agents and tools. This design creates an orchestration-level redundancy mode: semantically unchanged images are repeatedly reconstructed as image-conditioned requests at the VLM API boundary. We call this phenomenon visual orchestration tax and develop a measurement-to-certification framework for visual evidence reuse in agentic VLM pipelines. The audit side defines $\mathrm{M1}_{\mathrm{trace}}$ to count raw visual-evidence touches and M2 to measure structural touch redundancy, with query-level distributions, bootstrap confidence intervals, and paired quality tests. Across SeeingEye and MAMMQA on chart, document, general-VQA, and multi-modal-QA tasks, audits reveal 66.8-75.6% visual-evidence touch redundancy, and every audited query exceeds the predefined gate. The certification side introduces SharedVisCache, a contract-aware evidence reuse hook keyed by image content, preprocessing fingerprint, and encoder assumptions. On SeeingEye, contract validation certifies 75.0-75.5% repeated touches as reusable while preserving 350/350 output strings and $Δ\mathrm{M5}{=}0$. At the physical layer, certified hits reduce $F_{\mathrm{vision}}$ from 800 to 200 in ChartQA-200 trace replay and from 200 to 50 inside live SeeingEye translator-stage physical integration, preserving 800/800 replay strings and 200/200 integrated call outputs. The results position visual reuse as a measurable, behavior-preserving property of agent orchestration and define an agent-layer contract that makes backend prefix or token reuse semantically interpretable.

</details>


### 159. Token-Efficient Multi-Agent Collaboration via System One-Guided Computational Division of Labor

- **Authors:** Zihan Zhou, Xinzhe Hu, Hanxu Yang, Liangjian Wen, Zhao Kang
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08155v1](http://arxiv.org/abs/2610.08155v1)
- **PDF:** [https://arxiv.org/pdf/2610.08155v1](https://arxiv.org/pdf/2610.08155v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems (MAS) have become a promising paradigm for complex information-seeking and reasoning tasks by enabling collaborative problem solving among specialized agents. However, existing MAS frameworks tightly couple task reasoning with coordination operations, including task selection, role assignment, message routing, and context management. As interactions grow, using powerful LLMs for these bounded control decisions introduces substantial token overhead and latency, limiting the scalability of agentic Web services. In this paper, we investigate whether coordination can be decoupled from expensive reasoning without compromising collaborative performance. We propose S1-MAS, a token-efficient multi-agent framework based on System One-guided computational division of labor. S1-MAS assigns bounded coordination decisions to lightweight System One models while reserving open-ended reasoning for capable LLM workers. Specifically, a lightweight controller selects inspection conditions, chooses subsequent tasks, and determines termination, while a compact reader retrieves condition-relevant evidence from authorized sources to support these decisions. Through a decision-evidence loop, selected tasks dynamically determine worker roles and source access, enabling adaptive collaboration without task-specific training. Extensive experiments on seven diverse benchmarks demonstrate that S1-MAS achieves superior accuracy while substantially reducing the inference cost. Across individual comparisons with AgentVerse, DyLAN, and SelfOrg on seven benchmarks, S1-MAS reduces GPT-4o token consumption by 44.9%-97.2% and measured end-to-end latency by 37.8%-93.0%. These results highlight its potential for scalable and cost-effective agentic Web applications.

</details>


### 160. ChartBmkAgent: Harness-Governed Multi-Agent Construction of Chart QA Benchmarks from Sparse Error-Taxonomy Specifications

- **Authors:** Langxi Huang, Pingping Zhang, Lanyun Zhu, Chunyang Jiang, Jiawei Shao, Haocheng Yuan, Peilin Chen
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08106v1](http://arxiv.org/abs/2610.08106v1)
- **PDF:** [https://arxiv.org/pdf/2610.08106v1](https://arxiv.org/pdf/2610.08106v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) advance rapidly, while conventional benchmark development lags behind, delaying investigation of newly observed capability gaps. Such investigation requires an expressive task format and an on-demand construction process: information-rich charts make chart question answering (Chart QA) suitable for probing coupled perception and reasoning. Automated Chart QA construction is intended to shorten the benchmark-development cycle by turning identified gaps into targeted samples on demand. Current methods, however, commonly separate target guidance from scratch generation: target-guided systems often require prepared data, charts, or templates, while scratch-generation systems primarily ensure artifact validity, without explicitly controlling whether newly synthesized requirements and content remain aligned with an externally specified diagnostic target. We introduce ChartBmkAgent, which turns an identified capability gap into targeted diagnostic evidence by constructing complete Chart QA samples from sparse error-taxonomy specifications. Throughout construction, a central harness governs specialized agents, requires stage-specific evidence of alignment with the original error category, and records the basis for each acceptance decision. On 300 taxonomy-wide samples, MLLM accuracies ranged from 32.7% to 84.3% with distinct category profiles, showing that generated samples reveal capability differences. Across three source-model comparisons, targeted follow-ups scored 50.0% versus 82.2% on matched controls ($p=8.96\times10^{-6}$); all six cross-model comparisons had the same direction, demonstrating targeted validation and diagnostic-data generation. Multiple evaluator models assessed whether each sample tested its specified error category; 86.4% met this criterion, providing empirical evidence of target preservation.

</details>


### 161. Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems

- **Authors:** Zhe Yu, Zixuan Wang, Peidong Wang, Hehai Lin, Ruochen Zhao, Chengwei Qin
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08101v1](http://arxiv.org/abs/2610.08101v1)
- **PDF:** [https://arxiv.org/pdf/2610.08101v1](https://arxiv.org/pdf/2610.08101v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Shared memory coordinates agents' actions, but correct records do not establish that those actions satisfy task requirements. Memory governance and failure diagnosis regulate or inspect recorded information; they do not by themselves establish whether it is sufficient to judge task duties. We define execution consistency through duties governing state use, information handoffs, and final-state agreement, with explicit evidence conditions for judging fulfillment. Our core claim is that identical retained records can correspond to compliant and violating executions under the same task rule. Controlled removal of evidence such as receipt, action dependence, or response validity leaves 82.4% of opposite-label pairs indistinguishable; restoration separates 97.9% of the merged pairs. Natural-log annotations identify the defined violations in actual executions. However, existing logs do not always explicitly represent the execution relationships needed for these judgments. To assess the definition's practical value, we use CAVERT, a framework for consistency diagnosis and recovery, to extract supported relationships from logs and apply these criteria. It consistently outperforms contract-prompted LLM and rule-based baselines in diagnosis across all 12 benchmark-executor settings. Under the same gate and executor limits, it also outperforms rule-guided recovery in all four evaluated environments. These findings identify execution evidence that agent-memory and execution interfaces should preserve for reliable judgment.

</details>


### 162. Surviving the Router: Optimizing Skill Injections for Retrieval and Execution

- **Authors:** Haneen Najjar, Luca Scionis, Haritz Puerto, Sahar Abdelnabi
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08098v1](http://arxiv.org/abs/2610.08098v1)
- **PDF:** [https://arxiv.org/pdf/2610.08098v1](https://arxiv.org/pdf/2610.08098v1)
- **Categories:** cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly rely on modular third-party "skills" that are dynamically selected by skill routers to execute complex tasks. While recent studies highlight the threat of prompt injections embedded in these skills, existing evaluations often assume settings where the malicious skill is already selected for execution. We show that this assumption can substantially overestimate attack success. In realistic multi-skill environments, injected skills must first compete for retrieval, reducing the effective attack success rate (ASR) of existing injections by 87-97%. To address this limitation, we introduce CORSA (Cluster Optimization for Router-Aware Skill Attacks), a router-aware attack that optimizes skill injections for both retrieval and execution across clusters of related tasks. We evaluate skill injection attacks under router-managed multi-skill settings by extending the benchmark introduced by SkillRouter with eight malicious payload categories. CORSA uses successive optimization stages to first improve retrieval and then optimize end-to-end attack success, while we evaluate user utility and injection naturalism separately. Our experiments show that CORSA substantially improves both retrieval and end-to-end attack success over existing skill injections while preserving user utility, and that the resulting attacks transfer across different router architectures and LLM backbones.

</details>


### 163. POLAR: Ontology-Guided Risk Prevention for Tool-Calling LLM Agents

- **Authors:** Yunju Kang, Seonghyeon Cho, Irene Li, Yeo-Chan Yoon, Chanjun Park
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08082v1](http://arxiv.org/abs/2610.08082v1)
- **PDF:** [https://arxiv.org/pdf/2610.08082v1](https://arxiv.org/pdf/2610.08082v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM tool-use agents operate in dynamic environments where many actions carry operational risk. However, most safety mechanisms react only after errors manifest. Existing pre-emptive approaches either fine-tune the agent on chain-of-thought deliberation or compile natural-language guardrails into runtime checks, but they do so without exposing a structural, auditable verdict. We propose POLAR, a guardrail framework for small tool-calling agents that assesses reversibility through a structured two-layer ontology. POLAR assigns each action a graded reversibility score by deriving a candidate inverse sequence; calls failing a threshold are pruned before execution. Evaluated on $τ^2$-bench across six agent models, POLAR improves mean task reward by 0.11 to 0.18 points on airline for four of six agents, but only eight of eighteen model--domain cells improve overall; retail and stronger agents often regress. POLAR provides an auditable structural check and characterizes its task-utility trade-offs. Reward is not a direct measure of prevented harm.

</details>


### 164. SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning

- **Authors:** Yoshinari Fujinuma, Keisuke Kamahori, Ryuto Koike, Abdelrahman Madkour, Varun Prashant Gangal, Monty Bichouna, Martyna Markiewicz, Shivani Jain, Duncan Curtis, Rebecca Qian, Anand Kannappan
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08076v1](http://arxiv.org/abs/2610.08076v1)
- **PDF:** [https://arxiv.org/pdf/2610.08076v1](https://arxiv.org/pdf/2610.08076v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier LLM agents have been shown to be capable of solving increasingly complex tasks for which humans have measurable solutions. This begs the pertinent question of whether LLM agents can go beyond what humans have already solved. The ability to develop sophisticated strategies to tackle consequential problems becomes paramount as well-trodden, human-developed solutions become insufficient for problems for which we lack context or enough training data. We study agents' capability of such strategy formation through the communal practice of video game speedrunning. In speedrunning, practitioners compete to find the fastest way to complete a video game under certain conditions, and in so doing uncovering interesting unorthodox play styles that require a thorough understanding and mastery of the underlying game mechanics. We introduce SPEEDRUNBENCH, a benchmark that evaluates frontier LLM agents across 9 different games. To perform well in this benchmark, agents must repeatedly improve their strategy, reflect on their performance, exploit their gained knowledge, and reason across a long-horizon of actions to improve on an increasingly difficult problem: being faster than themselves and everyone else. Our experiments show that while frontier agents approach human world records in simple platformer games, they remain behind human performance on longer, more complex games under practical budgets. These results suggest that SPEEDRUNBENCH is a useful testbed for studying agents' strategy formation capabilities as well as being a saturation-resistant evaluation measure, as there is almost always a faster completion time waiting to be discovered.

</details>


### 165. DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks

- **Authors:** Antoine Edy, Max Conti, Victor Xing, Marc-Antoine Allard, Nawfal Benhamdane, Gautier Viaud
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08048v1](http://arxiv.org/abs/2610.08048v1)
- **PDF:** [https://arxiv.org/pdf/2610.08048v1](https://arxiv.org/pdf/2610.08048v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents often lack the operational knowledge to act reliably in new environments, as they must discover specific tool behaviors or environment conventions on their own. Without memory of past attempts, they repeat the same mistakes across tasks, leading to more task failures and longer trajectories. To address this, agentic systems typically rely on human-written guidelines or on procedural memory built from training tasks and an oracle verifier, both of which require prior knowledge of the environment. We present DAEDALUS, a method for bootstrapping reusable agent memory from self-generated practice without existing tasks or oracle verifiers. DAEDALUS pairs two agents: an explorer that interacts with the environment to generate challenging yet solvable tasks, and a solver that attempts them. A heuristic is derived from each solver failure and accepted only after the solver repeatedly succeeds with that heuristic in context. These outcomes also provide feedback for the explorer to refine the difficulty of future tasks. Accepted heuristics are then consolidated into a memory bank for test-time use. Across AppWorld, $τ^2$-bench, and AutomationBench, DAEDALUS improves mean success rates by up to 15.9 points and pass^5 by up to 2.2x over a no-memory baseline, and is competitive with methods using training tasks, at a lower inference cost than most. We show that performance gains already emerge with a small exploration budget, and that its heuristics also benefit agents from other model families. Our ablations further reveal that solver traces provide the key information needed to derive effective heuristics, while factorizing early discoveries makes exploration more cost-efficient. Beyond memory construction, we find that the tasks generated by DAEDALUS can serve as a proxy for benchmark tasks when ranking models by performance. Code and artifacts: www.github.com/illuin-tech/daedalus.

</details>


### 166. Same Feedback, Different Answer: Measuring Run-to-Run Instability in Frontier-Model Customer Feedback Analysis

- **Authors:** Viraj Bagal, Raviraja Ganta, Prabhath Chellingi
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08036v1](http://arxiv.org/abs/2610.08036v1)
- **PDF:** [https://arxiv.org/pdf/2610.08036v1](https://arxiv.org/pdf/2610.08036v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly being programmed to automate knowledge work over large collections of unstructured data. Such automation requires repeatability: when the underlying evidence is unchanged, the agent's categories, priorities, and counts should not shift materially between runs, even if each individual answer appears plausible. We introduce a repeat-run evaluation framework that aligns semantically equivalent categories and focuses on two operating metrics: theme churn, the normalized change in the returned category set, and volume disagreement, the change in counts for categories that persist. We evaluate three recurring customer-feedback tasks across eight frontier models, corpus sizes from 100 to 5,000 records, multiple prompts, and three execution designs: raw generation, taxonomy-free hierarchical decomposition, and a taxonomy-grounded agent (TGA) using persistent themes, subthemes, and record-level predictions. With Claude Opus 4.8 and the 1,000-record corpus fixed, TGA reduces theme churn by 86--88% relative to both raw generation and hierarchical decomposition, while matched-theme volumes have zero disagreement. The taxonomy-grounded agent is more stable than every raw model in the screen, remains more stable at each corpus size, and keeps this advantage when theme matching is made stricter or looser. Although evaluated on customer feedback, the framework targets repeated synthesis of unstructured corpora more broadly, including financial reports, legal documents, incident records, and scientific literature. Overall, these results show that taxonomy grounding produces more consistent and repeatable outputs for recurring knowledge work.

</details>


### 167. Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA

- **Authors:** Jordy Kieto
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.08033v1](http://arxiv.org/abs/2610.08033v1)
- **PDF:** [https://arxiv.org/pdf/2610.08033v1](https://arxiv.org/pdf/2610.08033v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

World models are usually judged from the inside: by prediction loss, by the return a policy earns in imagination, or by how convincing their frames look. We judge one from the outside. We learn a structured, multi-agent world model of a complete ten-hero MOBA (206 units, every hero acting every tick, games of up to 6,000 ticks), train a policy only inside it with 1,400-tick free-running imagined episodes, and measure that policy in the real game against the opponent the game ships with. The real game never provides a gradient; it provides the policy's own games as training data for the world model, and an online evaluation that selects and anchors the policy. Run as a continuous asynchronous Dyna loop, the policy wins 70.2% of real games as radiant (421 of 600; 95% CI 66.4-73.7) on seeds never used for any decision, up from 0% for dream training alone and 33.7% before the loop. It wins none as dire, and neither does the shipped opponent when it plays itself. Four findings explain the result. Model exploitation is invisible from inside the dream: every unanchored run collapsed within a few updates while no in-dream metric tracked the collapse. A world model that is accurate on its training corpus is badly wrong on the policy's own games, and Dyna repairs it there, which is worth +9.2 points of real win rate with the policy recipe held fixed. Finally, the policy inherits its world model's fidelity profile mechanic by mechanic: the model represents the macro game but not crowd control, cast timing or lethality, and the policy wins by map-wide pressure with almost no coordinated fighting. We release the world model, the dream-PPO harness, a world-model debugger, the evaluation protocol, and every policy and log.

</details>


### 168. DecepEval: A Benchmark for Evaluating Deception in LLM Agents

- **Authors:** Yiming Xu, Hongyue Yu, Beihua Yang, Zihan Chen, Yixin Liu, Zhen Peng, Bin Shi, Bo Dong, Chao Shen, Irwin King, Qinghua Zheng
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.07967v1](http://arxiv.org/abs/2610.07967v1)
- **PDF:** [https://arxiv.org/pdf/2610.07967v1](https://arxiv.org/pdf/2610.07967v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a benchmark comprising 1,532 instances across 3 task families and 28 professional scenarios. Drawing on classical fraud theories, we propose the LLM Deception Diamond framework, which characterizes four external conditions that may induce deception: pressure, incentive, opportunity, and conflict. DecepEval pairs neutral and induced versions of each instance to measure condition-dependent changes in deception rates, while explicit task facts and observable agent behavior help distinguish deception from capability-related errors. Evaluations of nine frontier LLMs show that inducements increase deception across models and task families, even among models with low baseline deception rates. DecepEval makes these vulnerabilities measurable, providing a shared benchmark for progress toward trustworthy artificial intelligence.

</details>


### 169. Confidence Reasoning Graphs: Structured Confidence Estimation for LLM Agents

- **Authors:** Brendan King, Farima Fatahi Bayat, Jean-Flavien Bussotti, Pouya Pezeshkpour, Estevam Hruschka
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.07948v1](http://arxiv.org/abs/2610.07948v1)
- **PDF:** [https://arxiv.org/pdf/2610.07948v1](https://arxiv.org/pdf/2610.07948v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

When using an LLM agent in a consequential domain, making an informed decision about whether to trust its output or intervene requires calibrated confidence in the agent's success. Confidence estimation for agents is difficult because evidence about success is distributed across heterogeneous, interdependent steps of an agent's trajectory. Practical agentic deployments introduce further challenges: frontier LLMs often provide limited access to internal signals, agent roll-outs are costly, and training data may be unavailable or quickly become outdated. To address these challenges, we introduce Confidence Reasoning Graphs (CRGs), an inference-time framework that estimates the probability an agent accomplished its task from a single trajectory, without privileged model access or training data. Rather than compressing an execution into a single holistic judgment, a CRG begins with the claim that the agent accomplished its task, decomposes it into contextualized sub-claims grounded in trajectory evidence, estimates confidence for each terminal claim, and finally aggregates these into an overall confidence estimate. Across three agentic benchmarks, three backbone models, and three agent frameworks, CRGs yield better-calibrated confidence and stronger risk-aware decision making than verbalized, sampling-based, and white-box surrogate baselines. We further find that calibration error alone can be misleading: a white-box surrogate baseline appears well calibrated while providing near-chance discrimination. Ablations attribute CRG's improvements to claim-level confidence estimation and aggregation rather than graph construction alone. Finally, a CRG exposes the claims and trajectory evidence underlying each confidence estimate, enabling it to be audited at decision time.

</details>


### 170. SIGMA: Self-Improving Alignment Generalization from a Model Spec

- **Authors:** Jingyu Zhang, Shruti Palaskar, Daniel Khashabi, Benjamin Van Durme, Leon A. Gatys, Joseph Yitan Cheng
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.07935v1](http://arxiv.org/abs/2610.07935v1)
- **PDF:** [https://arxiv.org/pdf/2610.07935v1](https://arxiv.org/pdf/2610.07935v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly capable of executing complex tasks and of recursively improving themselves on easy-to-verify objectives such as software engineering and mathematics. Since alignment is much harder to verify, this creates a growing risk of capabilities increasing without appropriate safety alignment, especially as capabilities expand to auto-research and cybersecurity. Existing approaches focus on capability self-improvement using verifiable feedback or on alignment training with supervision from stronger models or curated data, creating an external supervision bottleneck for alignment. We ask whether current models can improve their own safety alignment, and propose SIGMA, a data generation and training pipeline enabling alignment self-improvement that generalizes to out-of-distribution settings. Given only a "Model Spec" stating the model's desired behavior, SIGMA leverages a model's reasoning capabilities to strengthen its own safety reasoning. SIGMA first performs spec-guided task synthesis, using the candidate model as a task designer agent to generate diverse alignment dilemma scenarios and convert them into training tasks that stress-test its understanding of the Model Spec. Next, SIGMA conducts self-judged alignment training through supervised fine-tuning and rubric-based reinforcement learning with the model itself as the reward model. Despite training only on single-turn chat data, SIGMA improves safety alignment in multi-turn agentic environments (AgentHarm harmfulness decreases from 22.6 to 14.8; Agentic Misalignment decreases from 79.1 to 3.8), outperforms Deliberative Alignment and Constitutional AI baselines, and retains general capability. Analyses show that a Model Spec balancing harmlessness and helpfulness, test-time reasoning for safety deliberation, and high-quality rubrics from SIGMA's task designer agent are crucial for effective self-improvement.

</details>


### 171. FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents

- **Authors:** Jia Liufu, Bin Hu, Linglin Jing, Terry Kong, Yuki Huang, Ashwath Aithal, Wenming Yang, Jun Yang
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.07898v1](http://arxiv.org/abs/2610.07898v1)
- **PDF:** [https://arxiv.org/pdf/2610.07898v1](https://arxiv.org/pdf/2610.07898v1)
- **Categories:** cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Repository-level software engineering (SWE) is a challenging long-horizon setting: agents must reason over extended interactions, use tools, and adapt to stateful environments. Recent work trains SWE agents with reinforcement learning methods such as Group Relative Policy Optimization (GRPO), which independently sample multiple trajectories per issue, test the resulting patches, and compare terminal rewards within a fixed group. However, this training setup does not reuse verifier feedback from failed patches as context for subsequent attempts, even though this feedback contains valuable diagnostic information about what went wrong. Training on recovery trajectories is challenging because the preceding outcome determines whether the next trajectory is generated, while the failed execution determines its conditioning context. We introduce FC-SWE, a failure-conditioned RL framework that incorporates recovery attempts into policy training. After a patch fails verification, FC-SWE restores the repository to its original task state and uses the failed patch and verifier feedback as context for a recovery trajectory. FC-SWE adapts GRPO to these chains of complete, multi-turn tool-use trajectories through two mechanisms. Trajectory-local rewards preserve each attempt's verifier outcome, preventing recovery success from rewarding an earlier failed patch. Active-set advantage estimation forms a comparison group from all initial and recovery trajectories actually executed for the same issue, so failed attempts remain in the group while unexecuted attempts are excluded. On all 500 SWE-bench Verified tasks under a verifier-assisted protocol, FC-SWE with Qwen3.5-4B and SWE-agent achieves 41.7% Resolved@1 and 52.8% Resolved@2, compared with 38.9% and 48.5% for GRPO. Although trained with at most two attempts per chain, FC-SWE reaches 70.7% Resolved@11 under an eleven-attempt test-time budget.

</details>


### 172. Self-Referenced Social Preferences: Cooperation without Observing Others Rewards

- **Authors:** Mohamed Ayman Mohamed, Harshil Kotamreddy, Marcos Menon Jose
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.07881v2](http://arxiv.org/abs/2610.07881v2)
- **PDF:** [https://arxiv.org/pdf/2610.07881v2](https://arxiv.org/pdf/2610.07881v2)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Social preferences can promote cooperation in multi-agent reinforcement learning, but existing approaches often require agents to observe the rewards of their peers. In many real-world interactions, however, an agent can, as humans do, observe others' behavior and outcomes without access to their private reward signals. We introduce self-referenced social preferences, in which each agent learns a model of its own reward, applies it to other agents' observed transitions to assess their outcomes from its own perspective, and feeds these self-referenced assessments into standard social preferences. We study two ways to incorporate these assessments: modifying the learning reward, or using them to weight policy updates. We evaluate the approach on three sequential social dilemmas, Escape Room, Clean Up, and Commons Harvest, which require volunteering, public-good contribution, and resource restraint, respectively. Across all three environments, agents learn cooperative behavior without observing others' rewards, including in settings where independent learners fail to cooperate, and frequently achieve more equitable divisions of jointly produced returns than agents with access to true rewards. The effective integration point depends on the social preference: inequity aversion works best in the reward together with a value look-ahead, whereas a purely benevolent preference benefits from policy-update weighting. Under partial observability, the policy-update approach continues to support cooperation. These results show that explicit access to other agents' reward signals is not necessary for learning cooperative behavior: social preferences can instead be grounded in self-referenced assessments of others' outcomes derived from their observed behavior.

</details>


### 173. ReFold: Training-Free Reversible Inter-Turn Context Folding for Long-Horizon Agents

- **Authors:** Yupeng Su, Jiayi Tian, Zheng Zhang, Souvik Kundu
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.07863v1](http://arxiv.org/abs/2610.07863v1)
- **PDF:** [https://arxiv.org/pdf/2610.07863v1](https://arxiv.org/pdf/2610.07863v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents act on an append-only interaction history that is re-sent to the model at every step, so the context and its cost grow with steps until the sessions exceed the context window. Existing methods manage the context through context requirement prediction, relying on additional model calls, heuristic rules, or trained policies. However, these predictive approaches introduce runtime overhead, invalidate prefix caches, and permanently discard content with no guarantee of recovery. To overcome these limitations, we introduce ReFold: a training-free rendering layer that preserves the underlying interaction history while compressing only the model's rendered context. It removes two kinds of inter-turn redundancy without an auxiliary predictor: content an earlier turn already displayed, replaced by a stub, and turns the agent itself reports finished, folded into a one-line note. Both operators use chunked rendering, rewriting the cached prefix once every few steps rather than at every step. Every removal is strictly reversible, a wrong removal costs one restore from the history rather than permanent content loss. Because it operates at the rendering layer, ReFold is plug-and-play across standard ReAct-style harnesses. Evaluations across five long-horizon benchmarks and two frontier LLMs demonstrate that ReFold reduces token consumption by up to 2.5x and halves the KV-cache memory per session without degrading task success rates. Under capped context budgets, it avoids up to 92% of forced compactions. Under concurrent serving workloads, it reduces request queuing delays by up to 100%, accelerating inference by up to 1.7x, while cutting inference costs by up to 3.4x.

</details>


### 174. WorkflowOps: Learning Agent Collaboration Priors for Multi-Agent Workflow Orchestration

- **Authors:** Qi Cheng, Shengyu Chen, Wei Cheng, Zhengzhang Chen, Xiaowei Jia, Haoyu Wang, Haifeng Chen
- **Published:** 2026-10-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.07860v1](http://arxiv.org/abs/2610.07860v1)
- **PDF:** [https://arxiv.org/pdf/2610.07860v1](https://arxiv.org/pdf/2610.07860v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems are increasingly deployed for complex knowledge work, yet their orchestration layers remain largely memoryless: each new task is decomposed, assigned, and executed from scratch with no benefit from prior successful executions. We present WorkflowOps, a multi-agent workflow orchestration framework that learns agent collaboration priors from historical workflows and expands its agent pool on demand to cover new capability requirements. Our approach introduces three coupled mechanisms. First, a transition probability matrix captures pairwise agent collaboration frequencies from past workflows and applies them as soft guidance during DAG workflow construction through intra-layer ordering optimization, probability-thresholded edge suggestion, and transitive reduction for parallelism maximization. Second, a sufficiency-driven agent creation loop detects capability gaps via semantic matching scores, generates specialized agents through an LLM, and simultaneously injects them into the collaboration matrix, so that newly created agents are immediately usable with predicted collaboration priors. Third, a layered semantic matching strategy uses pre-trained sentence embeddings for fast, deterministic capability matching as a first pass, invoking LLM verification only for low-confidence cases, thereby reducing LLM routing calls by over 80\% compared to pure-LLM approaches. Experiments on mixed code, math, and question-answering suites show that WorkflowOps improves end-to-end pass rates over recent workflow-construction baselines, with the largest gains on structured, decomposable tasks where past agent handoff patterns transfer.

</details>



## Biorxiv (3 papers)


### 1. AI agent supervision of structural model building and refinement

- **Authors:** Wu, K.-P., Chueh, C.-K.
- **Published:** 2026-10-08
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.05.756902](https://doi.org/10.64898/2026.10.05.756902)

- **Categories:** biochemistry


> Summary unavailable.


<details>
<summary>Abstract</summary>

Structural model building and refinement need many decisions between different programs. These decisions often depend on an experienced researcher who knows how the programs work together and how to read experimental data. We used Claude Code with Claude Opus 5.5 to supervise this work for 24 cryo-EM and X-ray cases. The work finished in about 36 hours on one workstation. The agent prepared the inputs, ran established programs, read the validation results, compared candidate models and chose the next step. For 15 deposited cryo-EM models with weak starting geometry, the median MolProbity score improved from 2.62 to 1.76. For three crystal structures, the agent models came close to the published Rfree values. Chemical information such as ligands, ions and modifications must be provided by the researcher, in the same way as the sequence. With this information, the agent can place and check these components. These results show that agent supervision is acceptable when every decision can be inspected. The researcher makes the final scientific judgment. We suggest practical requirements for this kind of use. Future AI agents may help researchers obtain high quality and reliable structures of biological macromolecules.

</details>


### 2. Enrich.AI: An Agentic AI Platform for Interactive GeneSet Enrichment Analysis and Biological Interpretation

- **Authors:** Koumadorakis, D. E., Exarchos, T. P., Vlamos, P., Vrahatis, A. G.
- **Published:** 2026-10-06
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.29.755561](https://doi.org/10.64898/2026.09.29.755561)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: Enrichment analysis is widely used to extract biological meanings from gene lists. However, the large number of available tools and reference libraries often make the interpretation of results challenging. Inexperienced users lack clear guidance on which datasets and terms are most relevant to their data, whereas experienced researchers must navigate large result sets and consult multiple resources to identify biologically relevant findings. Integrating AI into this process can help to bridge these gaps. Results: We present Enrich.AI, a conversational biology assistant that integrates statistical enrichment analysis with automated biological interpretation. The agent operates on an LLM-based ReAct architecture and dynamically selects among the tools for enrichment (220+ gene set libraries), literature search (40+ million publications via Europe PMC), gene annotation, and database retrieval. Given a gene list and a short description of the biological context, Enrich.AI produces a written interpretation grounded in the retrieved literature and six interactive, configurable visualizations. A conversational interface enables human-in-the-loop refinement, letting researchers without programming experience explore results iteratively. The reliability of these interpretations was validated through a systematic evaluation on 50 gene sets, demonstrating high faithfulness to retrieved evidence and a low hallucination rate.

</details>


### 3. Verification Debt in Automated Biological Research Workflows: A Proof-of-Concept

- **Authors:** Gopalan, S., Narayanan, S.
- **Published:** 2026-10-05
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.29.755250](https://doi.org/10.64898/2026.09.29.755250)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent biological research has shown significant interest and progress towards adoption of agentic AI systems. Domain specific agentic platforms with access to large collections of biological tools with code generation and/or querying capabilities, such as Biomni (illustrative case in point), are representative of the capability to orchestrate automated research workflows. Such platforms enable collaborative AI workspace for drug discovery, genomics, bioinformatics, literature research, and experimental planning for biologists and researchers. When such platforms are used for the aforementioned workflows, individually validating every agentic decision and the research process by which it was reached becomes challenging due to the scale of decisions involved and oftentimes, insufficient disclosure of assumptions and methodological choices, limited traceability of evidence, and interpretive judgments embedded throughout the workflow, giving rise to verification debt. Verification debt in agentic environments could result in unexpected failures and consequences in downstream experiments. This study focuses on empirical qualitative characterization of verification debt in agentic (prompt to outcomes) workflows. Biomni was chosen the testing AI agentic platform in this study mainly due to the descriptive traces it provides to track every agentic step. Verification debt is examined through two complementary angles: the individual agentic decision steps that carry claims and evidence, and the underlying research process by which the agent arrives at and reports them. This study attempts to characterize verification debt with 10 test cases (covering proteomics, genomics and drug discovery) with varying degree of biological nuance across three identical and independent runs. Verification debt is represented through 9 decision-step metrics and 13 research-process metrics, and also propose the VERIFY framework for evaluating scientific verifiability and validity in agentic workflows.

</details>



## Medrxiv (1 papers)


### 1. Planner-Executor Style Multimodal Agentic System to Answer Patient Questions in Lung Cancer Screening CT

- **Authors:** Sakiyama, K., Serapio, A., Ye, M., Nowroozi, A., Bondarenko, M., Wu, Y., Qi, K., Liu, J., Vella, M., Yu, Y., Schnitzler, T., Rustagi, A. S., Sohn, J. H.
- **Published:** 2026-10-05
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.02.26364620](https://doi.org/10.64898/2026.10.02.26364620)

- **Categories:** radiology and imaging


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundAccurate patient understanding of lung cancer screening (LCS) results is critical for engagement and follow-up adherence, given the currently low screening uptake. While artificial intelligence (AI) systems show promise in facilitating patient communication, its effective use in clinical settings requires appropriate invocation of imaging tools and self-regulation by deferring certain questions to physicians. To this end, we developed and evaluated a planner-executor style multimodal agentic system to answer simulated patient questions about LCS CT results.

MethodsThis retrospective study utilized 116 LCS CT reports and images collected from a tertiary academic hospital. The system employed a multi-agent architecture (planner and executor) to mimic clinical reasoning. We developed a large language model (LLM)-based question generation framework to prepare a comprehensive set of 699 simulated patient questions, categorized as answerable and defer-to-doctor to assess self-regulation. Performance was evaluated on tool-calling, self-regulation accuracy (ability to correctly defer out-of-scope questions to a human provider) assessed by LLM-as-a-judge, and clinical quality assessed by a reader performance study with four physicians evaluating a subset of 100 responses.

ResultsThe system demonstrated high overall tool-calling accuracy of 93.1% (646/694; 95% CI: 91.2%, 95.0%) and self-regulation accuracy of 92.6% (462/499; 90.2%, 94.8%). For answerable questions, the percentage of responses receiving perfect 5.0 scores across all readers included 78.9% (180/228) for clinical accuracy (inter-rater agreement: Gwets AC2=0.92), and 73.2% (167/228) for patient understandability (0.86). For defer-to-doctor questions, the percentage of responses included 77.3% (133/172) for clinical accuracy (0.80) and 70.3% (121/172) for patient understandability (0.78).

ConclusionsThe planner-executor style multi-modal agentic system reliably answers patient-specific questions about LCS. Its high tool-calling and self-regulation performance demonstrates its potential as a safe and effective digital communication facilitator in LCS programs.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*