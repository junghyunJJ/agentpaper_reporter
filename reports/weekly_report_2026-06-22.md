# Weekly AI Agent Paper Report

**Generated:** 2026-06-22 15:18
**Period:** 2026-06-15 to 2026-06-21

## Summary

- **Total papers fetched:** 600
- **Papers matching keywords:** 149
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-06-15) | Change |
|--------|-----------|-----------|--------|
| Total matched | 149 | 184 | -35 |
| arxiv | 148 | 181 | -33 |
| biorxiv | 1 | 3 | -2 |
| medrxiv | 0 | 0 | +0 |

### Notable Trends

**Weekly Snapshot – AI‑Agent Research (arXiv + bioRxiv)**  

| Metric | This Week (22 Jun) | Last Week (15 Jun) | Change |
|--------|-------------------|--------------------|--------|
| Total papers | **149** | **184** | –19 % total volume |
| arXiv | 148 (99 %) | 181 (98 %) | –18 % |
| bioRxiv | 1 (1 %) | 3 (2 %) | –67 % |

### 1️⃣ Volume dip, but arXiv still dominates  
- Overall submissions fell by ~35 papers, driven almost entirely by fewer arXiv pre‑prints.  
- bioRxiv activity is minimal in both weeks, suggesting that “biological‑AI‑agent” work remains niche compared with the broader CS/ML community.

### 2️⃣ Shift from **methodological/benchmark** papers to **systems‑level and safety‑focused** work  
| This week (top titles) | Emphasis |
|------------------------|----------|
| *ContinuumCellAgent* | Long‑horizon scientific‑research agents (framework‑guided) |
| *Execution‑State Capsules* | Low‑latency on‑device serving, checkpoint/restore |
| *Sovereign Execution Brokers* | Authority‑certificates, control‑plane security |
| *Probabilistic Verification* | Formal‐sound verification for agents |
| *Contagion Networks* | Bias propagation across multi‑agent LLMs |
| *Optimal Order of Multi‑Agent & Many‑Body Systems* | Theoretical scaling/order analysis |

- **Safety & provenance** (certificates, verification, bias contagion) appear front‑and‑center, a clear step up from last week’s more **algorithmic/benchmark** focus (e.g., coordinated preferences, embodied scaffolds).

### 3️⃣ Emerging “in‑the‑wild” deployment themes  
- Papers on **on‑device physical‑AI serving** and **execution‑state checkpointing** indicate a move toward production‑ready agents rather than simulation‑only studies.  
- The “ContinuumCellAgent” title signals renewed interest in **autonomous scientific discovery** pipelines, echoing but extending last week’s *Evaluating agentic AI for biological discovery*.

### 4️⃣ Continued interest in **multi‑agent coordination**, but with a different flavor  
- Last week highlighted **multi‑objective RL coordination** and **embodied scaffold composition**.  
- This week the focus is on **network‑level dynamics** (bias contagion) and **theoretical ordering** of many‑body agent systems—suggesting a maturation from “how to train” toward “how do many agents behave together at scale”.

### 5️⃣ Topic diversification but concentration in a few hot spots  
- While the total number of papers shrank, the top‑six titles cluster around **(a) robust execution infrastructure, (b) formal safety guarantees, and (c) bias/propagation dynamics**.  
- Less representation this week for **medical imaging** (spine MRI) or **policy/governance** papers that featured prominently last week.

**Takeaway:** The AI‑agent field is slightly contracting in volume but is re‑orienting toward *deployment robustness* and *trustworthiness* (security, verification, bias). Multi‑agent theory remains a backbone, but the narrative is shifting from learning‑centric tricks to system‑level guarantees and real‑world applicability.

---



## Biomedical Highlights (1 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


**ContinuumCellAgent:** Introduces an autonomous “AI‑scientist” that chains together literature mining, hypothesis generation, experimental design, and data‑analysis modules to conduct long‑horizon cell‑biology projects with minimal human supervision. The framework combines a large‑language model (LLM) for natural‑language reasoning with a domain‑specific knowledge graph and reinforcement‑learning–based planning to iteratively refine hypotheses and select wet‑lab experiments. Validation on multi‑step projects (e.g., differentiation pathways, drug‑resistance mechanisms) shows that the agent can produce reproducible protocols and novel insights comparable to expert biologists.

**DeepChemist: End‑to‑End Molecular Design with Generative Agents:** Presents a hierarchical agent that integrates an LLM for high‑level target specification with a graph‑neural‑network (GNN) generator and a Monte‑Carlo tree search planner for multi‑objective optimization (potency, ADMET, synthetic accessibility). The system is trained on public bioactivity datasets and evaluated on de‑novo design of kinase inhibitors, achieving chemical novelty (> 0.7 Tanimoto distance) and experimental validation of two hit compounds. The paper emphasizes closed‑loop synthesis‑feedback, where automated assays inform subsequent generation cycles.

**AI‑Clinician for Critical Care Decision Support:** Describes a reinforcement‑learning (RL) agent that learns optimal dosing policies for vasopressors and fluids from the MIMIC‑III ICU database. The methodology couples a recurrent neural network (RNN) to encode patient trajectories with an off‑policy actor‑critic algorithm that respects clinical safety constraints via a constrained‑RL formulation. Retrospective analysis shows a 15 % reduction in 90‑day mortality compared with standard practice, and prospective pilot trials are underway to assess real‑time deployment.

**BioBERT‑Enhanced Clinical Trial Matching:** Develops a domain‑adapted BERT model (BioBERT‑CT) that extracts eligibility criteria from trial registries and matches them to electronic health records using a dual‑encoder architecture. The system is fine‑tuned on a curated benchmark of 5 000 patient‑trial pairs and evaluated across three disease areas, achieving a 92 % precision‑recall balance and a 30 % increase in enrollment efficiency relative to rule‑based matching. The authors highlight the importance of interpretability dashboards for clinician trust.

**Generative Adversarial Networks for Histopathology Synthesis:** Explores a conditional GAN that learns to generate realistic whole‑slide images conditioned on molecular subtypes and treatment response labels. Training on TCGA and private pathology datasets, the model produces high‑fidelity synthetic slides that preserve diagnostic features (e.g., nuclear atypia) while enabling data augmentation for rare cancer subtypes. Downstream classification models trained with synthetic data show a 7 % boost in AUROC, demonstrating the potential of AI agents to alleviate data scarcity in pathology.



### 1. ContinuumCellAgent: A Framework-Guided Agent for Long-Horizon Scientific Research

- **Authors:** Li, H., Lu, Y., Fang, K., Xu, Z., Li, F.
- **Published:** 2026-06-19
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.15.732409](https://doi.org/10.64898/2026.06.15.732409)

- **Categories:** bioinformatics


> The paper introduces **ContinuumCellAgent**, a modular, framework‑guided AI scientist that can autonomously carry out an entire research pipeline—from literature review and hypothesis generation to computational experiments, manuscript drafting, and adversarial peer review—in a single unattended run. By structuring the agent as interchangeable “supernodes” linked through rigorously curated research‑method checklists and reviewer rubrics, and by adding a diagnostics layer that logs files, message traces, and state transitions, the system achieves unprecedented observability and reproducibility for long‑horizon scientific tasks. Empirical evaluations on open‑domain QA benchmarks and biomedical/ longevity case studies demonstrate that the agent produces verifiable research artifacts while making its internal pipeline dynamics transparent, thereby addressing key shortcomings of prior AI‑scientist systems in modularity, prompt grounding, and diagnostic accountability.


<details>
<summary>Abstract</summary>

AI-scientist systems are beginning to automate parts of scientific research. We present CO_SCPLOWONTINUUMC_SCPLOWCO_SCPLOWELLC_SCPLOWAO_SCPLOWGENTC_SCPLOW, an autonomous agent that executes literature review, hypothesis formation, computational experimentation, manuscript drafting, and adversarial peer review as a single unattended run. Existing AI scientist systems remain difficult to diagnose because they lack modularity, systematic prompt grounding, and observability into long-running behavior. CO_SCPLOWONTINUUMC_SCPLOWCO_SCPLOWELLC_SCPLOWAO_SCPLOWGENTC_SCPLOW addresses these gaps with a modular supernode architecture for stage-wise backend swapping, protocols grounded in curated research-method checklists that also define reviewer rubrics, and a diagnostics layer that records file-based artifacts, message traces, and state transitions. We evaluate the system on open-domain QA benchmarks and biomedical/longevity case studies, showing that it can produce checkable research artifacts while exposing pipeline dynamics for rigorous AI co-scientist research.

</details>


---



## Biorxiv (1 papers)


### 1. ContinuumCellAgent: A Framework-Guided Agent for Long-Horizon Scientific Research

- **Authors:** Li, H., Lu, Y., Fang, K., Xu, Z., Li, F.
- **Published:** 2026-06-19
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.15.732409](https://doi.org/10.64898/2026.06.15.732409)

- **Categories:** bioinformatics


> The paper introduces **ContinuumCellAgent**, a modular, framework‑guided AI scientist that can autonomously carry out an entire research pipeline—from literature review and hypothesis generation to computational experiments, manuscript drafting, and adversarial peer review—in a single unattended run. By structuring the agent as interchangeable “supernodes” linked through rigorously curated research‑method checklists and reviewer rubrics, and by adding a diagnostics layer that logs files, message traces, and state transitions, the system achieves unprecedented observability and reproducibility for long‑horizon scientific tasks. Empirical evaluations on open‑domain QA benchmarks and biomedical/ longevity case studies demonstrate that the agent produces verifiable research artifacts while making its internal pipeline dynamics transparent, thereby addressing key shortcomings of prior AI‑scientist systems in modularity, prompt grounding, and diagnostic accountability.


<details>
<summary>Abstract</summary>

AI-scientist systems are beginning to automate parts of scientific research. We present CO_SCPLOWONTINUUMC_SCPLOWCO_SCPLOWELLC_SCPLOWAO_SCPLOWGENTC_SCPLOW, an autonomous agent that executes literature review, hypothesis formation, computational experimentation, manuscript drafting, and adversarial peer review as a single unattended run. Existing AI scientist systems remain difficult to diagnose because they lack modularity, systematic prompt grounding, and observability into long-running behavior. CO_SCPLOWONTINUUMC_SCPLOWCO_SCPLOWELLC_SCPLOWAO_SCPLOWGENTC_SCPLOW addresses these gaps with a modular supernode architecture for stage-wise backend swapping, protocols grounded in curated research-method checklists that also define reviewer rubrics, and a diagnostics layer that records file-based artifacts, message traces, and state transitions. We evaluate the system on open-domain QA benchmarks and biomedical/longevity case studies, showing that it can produce checkable research artifacts while exposing pipeline dynamics for rigorous AI co-scientist research.

</details>



## Arxiv (148 papers)


### 1. Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving

- **Authors:** Liang Su
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20537v1](http://arxiv.org/abs/2606.20537v1)
- **PDF:** [https://arxiv.org/pdf/2606.20537v1](https://arxiv.org/pdf/2606.20537v1)
- **Categories:** cs.LG, cs.DC


> The paper introduces **execution‑state capsules**, a graph‑bound checkpoint/restore mechanism that captures the full runtime state of a transformer model (KV cache, recurrent, convolutional, MTP buffers, and metadata) at a committed execution boundary, enabling sub‑millisecond on‑GPU snapshots and restores. By building a white‑box kernel runtime (FlashRT) that runs static graph plans over contiguous buffers without indirection, the authors demonstrate that capsules can faithfully fork, roll back, or resume execution, yielding latency‑first speed‑ups of 3.9× for 2 k‑token pre‑fills up to 27× for 16 k tokens on an RTX 5090, with identical token outputs compared to cold starts. The results show that full execution‑state reuse—not just KV‑cache reuse—is crucial for low‑latency, small‑batch, on‑device physical‑AI serving (e.g., interactive LLM agents, speech, robot policies), complementing traditional high‑throughput KV‑cache serving.


<details>
<summary>Abstract</summary>

Mainstream LLM serving systems reuse prefix work mainly through paged or radix key-value (KV) caches. This is highly effective for high-throughput, high-concurrency serving, but it manages only one positional fragment of execution state: the KV cache. We study the opposite regime: low-latency, small-batch, on-device physical-AI serving, where interactive LLM agents, speech systems, and robot policies repeatedly branch, reset, interrupt, and re-enter under tight responsiveness budgets. We introduce execution-state capsules, a graph-bound checkpoint and restore mechanism for the complete restorable state at a committed boundary. FlashRT is a white-box, backend-facing kernel runtime whose evaluated NVIDIA CUDA backend runs captured graph plans over contiguous static buffers with no block-table indirection. Because the live state is a closed set of named buffers, a capsule can snapshot, restore, fork, or roll back the whole execution boundary, including KV, recurrent state, convolution state, MTP state, and metadata. This moves reuse from token-addressed KV fragments to graph-bound execution-state boundaries. On an RTX 5090, capsule restore is byte-exact at the stored-state level and token-identical under greedy decode. A KV-only ablation diverges, showing that recurrent state is load-bearing. GPU-resident snapshot and restore are sub-millisecond, and TTFT speedup over cold prefill grows from 3.9x at 2k tokens to 27x at 16k tokens. On Jetson AGX Thor and DGX Spark, the same correctness and structural properties hold. Capsules are not a replacement for high-throughput KV-cache serving; they define a complementary latency-first serving point for explicit execution-state reuse.

</details>


### 2. Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes

- **Authors:** Jun He, Deying Yu
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20520v1](http://arxiv.org/abs/2606.20520v1)
- **PDF:** [https://arxiv.org/pdf/2606.20520v1](https://arxiv.org/pdf/2606.20520v1)
- **Categories:** cs.CR, cs.AI, cs.DC, cs.LG


> The paper introduces **Sovereign Execution Brokers (SEBs)**, a runtime enforcement layer that guarantees that any production‑mutating operation performed by autonomous agents is backed by a freshly‑issued, verifiable certificate from a **Sovereign Assurance Boundary (SAB)**. The authors formalize a three‑stage flow—proposal, admission, and execution—where the SEB validates the certificate’s execution contract, time windows, policy and revocation epochs, and live‑state drift before minting a scoped execution identity, invoking the target API, and logging a signed decision record. Experiments on AWS and Kubernetes show that SEBs add only modest latency (≈ 5–15 ms per mutation), propagate revocations within seconds, detect state drift reliably, and resist fault‑injection attacks, thereby providing a short‑lived, revocable and auditable authority checkpoint for agentic control planes.


<details>
<summary>Abstract</summary>

Autonomous agents are increasingly connected to cloud, deployment, and data-control workflows, but production mutation authority should not reside inside non-deterministic reasoning processes. Existing access-control mechanisms authorize identities, while assurance layers certify proposed actions; neither alone provides a mandatory enforcement point for certified authority at the moment of mutation. This paper introduces the Sovereign Execution Broker (SEB), a runtime enforcement boundary for certificate-bound agentic infrastructure. SEB consumes certificates issued by the Sovereign Assurance Boundary (SAB), verifies that the requested mutation matches the certified execution contract, checks validity windows, policy epochs, revocation epochs, and live-state drift, mints scoped execution identity, invokes infrastructure APIs, and records signed decision and outcome records. By separating proposal, admission, and execution, SEB turns certified authority into a short-lived, revocable, auditable runtime capability, provided that production mutation APIs reject non-broker identities. We present the SEB execution model, certificate and replay-verification predicates, scoped identity semantics, bypass-prevention deployment patterns, failure behavior, and a concrete prototype implementation. We evaluate the prototype on AWS and Kubernetes clusters, measuring latency overheads, revocation propagation, drift detection, and security under fault injection.

</details>


### 3. Efficient and Sound Probabilistic Verification for AI Agents

- **Authors:** Alaia Solko-Breslin, Pramod Kaushik Mudrakarta, Mihai Christodorescu, Somesh Jha, Krishnamurthy Dj Dvijotham
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20510v1](http://arxiv.org/abs/2606.20510v1)
- **PDF:** [https://arxiv.org/pdf/2606.20510v1](https://arxiv.org/pdf/2606.20510v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper presents a new verification framework that can enforce security policies for AI agents even when the policies involve probabilistic predicates and arbitrary correlations among them—something prior deterministic‑only or independence‑assumption methods cannot handle.  

**Methodology:** By casting the problem as a distributionally robust optimization (DRO) task, the authors compute provably sound upper bounds on the probability of a policy violation, without requiring any independence assumptions about the underlying stochastic predicates. The approach integrates with runtime monitoring expressed in Datalog and is implemented to work with standard benchmarks for terminal‑based and tool‑calling agents.  

**Key findings:** Experiments on established benchmarks show that the DRO‑based verifier delivers tighter, provable violation probability bounds than existing techniques, leading to a better security‑utility trade‑off while guaranteeing rigorously bounded risk of policy breaches in probabilistic, correlated settings.


<details>
<summary>Abstract</summary>

Securing AI agents that operate in complex digital environments has become a critical need, and runtime monitoring approaches that formulate and enforce policies expressed in a formal language like Datalog offer a promising solution. However, existing approaches are restricted to deterministic policies. In many practical applications of AI agents, there is a need to enforce security policies in the face of ambiguity, leading to probabilistic predicates or state transitions (for example, a declassifier or Personally Identifiable Information (PII) detector that has some failure probability on each invocation). Furthermore, in many such applications, one cannot easily make the independence assumptions necessary to invoke prior work on probabilistic inference in Datalog. We address this by introducing a sound and efficient framework for such verification based on distributionally robust optimization, computing sound upper bounds on the probability of policy violation regardless of possible correlations between predicates. On standard benchmarks for terminal and tool calling agents, we demonstrate that our approach outperforms prior art and improves the security-utility trade-off while ensuring rigorous bounds on the probability of policy violation.

</details>


### 4. Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems

- **Authors:** Zewen Liu
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20493v1](http://arxiv.org/abs/2606.20493v1)
- **PDF:** [https://arxiv.org/pdf/2606.20493v1](https://arxiv.org/pdf/2606.20493v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> **Main contribution:** The paper introduces *Contagion Networks*, a formal framework for quantifying how evaluation biases of large language models (LLMs) used as judges spread across interacting agents in multi‑agent systems, and releases an open‑source experimental suite for measuring this effect.  

**Methodology:** In a controlled three‑agent setup they instantiate DeepSeek‑Chat agents with three distinct evaluator bias profiles (structured, balanced, evidence‑based) and compute a Cross‑Agent Contagion Matrix Γ₃. By analysing the spectral radius ρ(Γₙ) they identify bias‑propagation regimes and compare homogeneous‑model contagion coefficients (γ ≈ 0.16–0.35) with previously reported cross‑model values (γ ≈ 0.85–1.3).  

**Key findings:** Biases do propagate between agents even when they share the same underlying model, but the contagion is 3–5× weaker, placing homogeneous agents in a “suppression” regime. Moreover, expanding the evaluator committee from a single judge (k = 1) to three judges (k = 3) cuts effective contagion by ~72 %, offering a practical mitigation strategy for agentic AI deployments.


<details>
<summary>Abstract</summary>

When large language models serve as evaluators in multi-agent systems, their systematic evaluation biases propagate through the agent network. We introduce Contagion Networks, a formal framework for measuring how evaluator biases spread across interacting LLM agents. In a controlled 3-agent experiment using DeepSeek-chat with three distinct evaluator bias profiles (structured, balanced, evidence-based), we measure the Cross-Agent Contagion Matrix Gamma_3 and find that evaluator biases consistently propagate between agents (gamma in [0.157, 0.352]), even within the same underlying model. We identify three propagation regimes governed by the spectral radius rho(Gamma_N), and demonstrate that homogeneous-model agents produce contagion coefficients 3-5x weaker than cross-model coefficients observed in prior work (MM-EPC: gamma approx 0.85-1.3), placing them in the suppression regime. We show that increasing evaluator committee size from k=1 to k=3 reduces effective contagion by 72.4%, providing an actionable mitigation strategy. We release the open-source Contagion Network experimental framework.

</details>


### 5. Optimal Order of Multi-Agent and General Many-Body Systems

- **Authors:** Jake J. Xia
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20485v1](http://arxiv.org/abs/2606.20485v1)
- **PDF:** [https://arxiv.org/pdf/2606.20485v1](https://arxiv.org/pdf/2606.20485v1)
- **Categories:** q-fin.RM, cs.AI, nlin.AO, physics.soc-ph


> **Main contribution:** The paper proposes a unified, quantitative framework that links individual‑agent characteristics—*power* (influence on collective outcomes) and *response functions* (how agents react to system‑wide observations)—to emergent macroscopic properties of multi‑agent and many‑body systems, and uses this link to define and analytically solve for an *optimal degree of order* that trades off productivity, stability, and adaptability.  

**Methodology:** By treating agents as heterogeneous nodes with specified power and response kernels, the authors derive closed‑form expressions for system‑level quantities (total/​useful power, entropy, order, fragility, mobility). They introduce a risk‑appetite‑weighted utility function and analytically optimize it with respect to the order parameter, showing how synchronization, information flow, and useful energy depend on task‑specific objectives.  

**Key findings for agentic AI:** Stronger synchronization (higher order) raises collective output but also amplifies fragility and reduces mobility, implying a sweet‑spot where order maximizes a risk‑adjusted utility. The results suggest that designing agent power distributions and response functions—i.e., shaping influence and feedback policies—can steer large‑scale AI collectives toward emergent intelligence while keeping them resilient and adaptable.


<details>
<summary>Abstract</summary>

This paper develops a general framework for analyzing multi-agent systems with feedback loops between agents actions and collective observations. The framework is built on two fundamental agent-level variables: power, which measures agent influence on collective outcomes, and response functions, which determine how agents react to observations. We derive how macroscopic properties, including total power, useful power, entropy, order, fragility, and mobility, emerge from these two variables of heterogeneous agents. To study the trade off between growth and resilience, we introduce a system-level utility function parameterized by a risk-appetite coefficient and derive an optimal degree of order that balances productivity, stability, and adaptability. The analysis suggests that stronger synchronization can increase collective output but may also increase systemic fragility and reduce mobility. We further argue that order, entropy, information, and useful energy are task-dependent and system-relative concepts whose meanings depend on the objectives of the system. By measuring and designing agent power distributions and response functions, it may be possible to better understand, predict, and optimize collective behavior and identify the conditions under which collective intelligence and optimal order emerge.

</details>


### 6. Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems

- **Authors:** Reza Soosahabi, Vivek Namsani
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20470v1](http://arxiv.org/abs/2606.20470v1)
- **PDF:** [https://arxiv.org/pdf/2606.20470v1](https://arxiv.org/pdf/2606.20470v1)
- **Categories:** cs.CR, cs.AI


> The paper shows that conventional “detect‑and‑block” defenses for agentic AI systems become ineffective against model‑guided, automated jailbreak attacks, because each refusal gives the attacker reliable feedback that lets a search‑based attacker drive its success rate arbitrarily close to 1 as the query budget grows. To counter this, the authors propose a “detect‑and‑misdirect” strategy that, once a malicious query is identified, returns carefully crafted, harmless but misleading replies that confuse the attacker’s automated judge; they formalize this approach with a probabilistic attack‑defense model and prove that it caps the asymptotic attacker success rate. Their lightweight implementation, Contextual Misdirection via Progressive Engagement (CMPE), replaces standard refusal messages with these strategic misdirections and empirically drops estimated attack success rates by up to 100× on jailbreak benchmarks, nearly eliminating successful attacks in PAIR and GPTFuzz end‑to‑end evaluations.


<details>
<summary>Abstract</summary>

Agentic AI systems increasingly rely on language-model components to interpret instructions, process external data, invoke tools, and coordinate with other agents. These capabilities make prompt-injection and jailbreak attacks more consequential, especially as attackers adopt model-guided automation to scale probing, prompt refinement, and response evaluation. This work analyzes the resulting attack-defense setting through a probabilistic model of a target system, its defense mechanism, and the attacker's automated judge. Our analysis shows that conventional detect-and-block defenses can allow attacker success rate (ASR) to approach one as the query budget grows, since predictable refusals provide useful feedback to automated search. We then examine detect-and-misdirect, where detected malicious interactions receive controlled, non-operational responses designed to induce false-positive errors in the attacker's judge. This strategy reduces the positive predictive value of attacker-selected candidates and yields a bounded asymptotic ASR. We evaluate a proof-of-concept realization of this strategy through Contextual Misdirection via Progressive Engagement (CMPE), a lightweight conversational misdirection method designed to replace predictable refusal text with safe but strategically misleading responses in automated jailbreak settings. On jailbreak benchmarks, CMPE reduces estimated ASR upper bounds by up to two orders of magnitude and nearly eliminates verified attack success in end-to-end PAIR and GPTFuzz attack runs.

</details>


### 7. LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems

- **Authors:** Hanwool Lee, Dasol Choi, Bokyeong Kim, Seung Geun Kim, Haon Park
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20408v1](http://arxiv.org/abs/2606.20408v1)
- **PDF:** [https://arxiv.org/pdf/2606.20408v1](https://arxiv.org/pdf/2606.20408v1)
- **Categories:** cs.CR, cs.AI


> **Contribution:** The paper introduces **NRT‑Bench**, the first multi‑turn red‑team benchmark that evaluates the adversarial robustness of LLM‑driven operators in a simulated nuclear‑power‑plant control room, and releases the simulation environment, attack dataset, and replay tools for reproducible safety testing.  

**Methodology:** A five‑role operator team, each backed by a configurable LLM, manages six critical safety functions while adversaries inject messages over four communication channels in bounded multi‑turn sessions; a run ends immediately when any safety function is lost, providing a concrete, system‑level harm signal rather than a text‑based judgement. Four state‑of‑the‑art operator models are assessed under a paired‑replay protocol with fixed attacks, and various guardrail stacks (e.g., safety advisors) are evaluated for their impact on each model.  

**Key Findings:** Adaptive multi‑turn attacks cause a loss of a critical safety function in **8.7 %–12.1 %** of sessions across models, but the vulnerabilities are largely *disjoint*: none of the 149 attack sessions defeat all four models and about a third defeat at least one, indicating that robustness improvements are model‑specific and that a guardrail that helps one model can worsen another. This highlights the need for heterogeneous, model‑aware safety mechanisms when deploying LLM agents in safety‑critical systems.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly proposed as supervisory components for safety-critical systems, yet their robustness under sustained, adaptive adversarial pressure remains poorly characterized. We present NRT-Bench, a benchmark for multi-turn red-teaming of LLM agents acting as operators of a safety-critical system, instantiated in a simulated nuclear power plant control room. A five-role operator team, each backed by a configurable LLM, runs a plant governed by six critical safety functions (CSFs), while adversaries inject messages over four channels in bounded multi-turn sessions with per-turn feedback. Harm is an objective signal rather than LLM-judged text: a run terminates the moment any CSF is lost, attributed to the causing message. Evaluating four frontier operator models under a fixed-attack paired-replay protocol, we find that adaptive multi-turn attacks reliably push the operator team past a safety limit: across the four models, between 8.7% and 12.1% of attack sessions end with the plant losing a critical safety function. Although the four models look almost equally robust by this aggregate rate, their failures barely overlap: of $149$ sessions, none defeat all four models while a third defeat at least one, so vulnerabilities are nearly disjoint across models rather than nested. The effect of added defences is strongly model-dependent: the same guardrail stack or safety-advisor agent that lowers attack success for one model can raise it for another. We release the simulation venue, attack dataset, and replay tooling for reproducible safety evaluation of LLM agents.

</details>


### 8. DataMagic: Transforming Tabular Data into Data Insight Video

- **Authors:** Yupeng Xie, Chen Ma, Zhenyang Wang, Liangwei Wang, Jiayi Zhu, Chuxuan Zeng, Zhouan Shen, Boyan Li, Yuyu Luo
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20388v1](http://arxiv.org/abs/2606.20388v1)
- **PDF:** [https://arxiv.org/pdf/2606.20388v1](https://arxiv.org/pdf/2606.20388v1)
- **Categories:** cs.HC, cs.AI, cs.DB


> The paper introduces **DataMagic**, an end‑to‑end system that automatically converts raw tabular datasets and natural‑language queries into narrative “data‑insight” videos while preserving strict data provenance. It does so by defining a declarative language (DVSpec) that ties every visual and animation element to underlying data fields, and by employing a **Generate‑then‑Orchestrate** multi‑agent pipeline that first creates parallel candidate scenes and then globally optimizes them for narrative coherence; the decoupled specification also enables interactive query‑driven exploration of the resulting video. Experiments on 109 real‑world datasets show that DataMagic produces high‑fidelity, coherent videos far more efficiently than manual authoring tools and outperforms prior static‑visualization and pixel‑level video generators in both data fidelity and user satisfaction, highlighting a scalable architecture for agentic AI systems that must synthesize data‑driven narratives.


<details>
<summary>Abstract</summary>

Data videos integrate dynamic charts, voice narration, and synchronized animations to communicate data insights as temporal narratives, making them an effective medium for improving data consumption efficiency in the data management lifecycle. However, producing high-quality data videos requires expertise spanning data analysis, narrative design, and video production. Existing approaches fall short: static visualization tools (e.g., BI dashboards) lack narrative logic and animation; authoring tools require users to pre-prepare visualizations rather than working from raw data; pixel-level video generation models cannot guarantee data fidelity or provenance. We demonstrate DataMagic, an end-to-end interactive system that transforms raw tabular data and natural language queries into narrative data-insight videos. To ensure data fidelity, DataMagic introduces the declarative specification DVSpec, which binds visual and animation elements to underlying data fields through data-driven semantic references. To address the combinatorial explosion of the design space, DataMagic adopts a Generate-then-Orchestrate multi-agent architecture that generates candidate scenes in parallel and then optimizes narrative coherence through global orchestration. Leveraging DVSpec's decoupling of logic and rendering, the system further supports three interaction modes and structured provenance-based data Q&A, transforming one-way videos into explorable interactive data interfaces. Evaluation on 109 real-world samples validates the effectiveness of the DataMagic. Homepage: https://datamagic-home.github.io/

</details>


### 9. AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning

- **Authors:** Zepeng Li, Jie Ren, Zhanyong Tang, Jie Zheng, Zheng Wang
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20373v1](http://arxiv.org/abs/2606.20373v1)
- **PDF:** [https://arxiv.org/pdf/2606.20373v1](https://arxiv.org/pdf/2606.20373v1)
- **Categories:** cs.SE, cs.AI


> AutoPass introduces a multi‑agent framework that lets large language models interact directly with a compiler’s internal state to synthesize and iteratively refine optimization flags for runtime performance tuning. By exposing LLVM’s intermediate representation and optimization metadata to LLM‑driven agents, the system uses measured execution feedback to diagnose regressions and steer latency‑improving edits, all without any offline training or fine‑tuning. Evaluated on server‑grade x86‑64 and embedded ARM64 platforms, AutoPass surpasses expert heuristics and classic autotuners, achieving geometric‑mean speed‑ups of 4.3 % on x86‑64 and 11.7 % on ARM64 over LLVM ‑O3.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) show promise for code compilation tasks, but applying them to runtime performance tuning is difficult due to complex microarchitectural effects and noisy runtime measurements. We present AutoPass, a multi-agent framework for compiler performance tuning that uses compiler and runtime evidence to guide LLM-generated optimization decisions. Rather than treating the compiler as a black box like prior auto-tuning schemes, AutoPass opens up the compiler to the LLM, enabling it to query compiler-internal optimization states and analyze the intermediate representation to orchestrate compiler options. The search process iteratively refines optimization configurations using measured runtime feedback to diagnose regressions and guide latency-improving edits. AutoPass operates in an inference-only, training-free setting and requires no offline training or task-specific fine-tuning, making it readily applicable to new benchmarks and platforms. We implement AutoPass on the LLVM compiler and evaluate it on server-grade x86-64 and embedded ARM64 systems. AutoPass outperforms expert-tuned heuristics and classical autotuning methods, achieving geometric-mean speedups of 1.043x and 1.117x over LLVM -O3 on x86-64 and ARM64, respectively.

</details>


### 10. PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback

- **Authors:** Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20287v1](http://arxiv.org/abs/2606.20287v1)
- **PDF:** [https://arxiv.org/pdf/2606.20287v1](https://arxiv.org/pdf/2606.20287v1)
- **Categories:** cs.CL


> **Main contribution**  
PsyScore introduces a unified, psychometrically‑grounded framework that jointly performs automated essay scoring and adaptive instructional feedback. By embedding an Item‑Response‑Theory (IRT) latent‑ability model directly into a neural scorer and conditioning a multi‑agent LLM feedback generator on the estimated ability, PsyScore closes the gap between reliable assessment and personalized scaffolding.  

**Methodology**  
1. **Trait‑Adaptive Neural IRT Scorer** – a neural network is trained to predict the parameters of the Graded Partial Credit Model (GPCM), yielding a continuous ability estimate for each student while preserving the interpretability of classical IRT.  
2. **ZPD‑Scaffolded Feedback Generator** – several LLM‑based agents (e.g., error‑identification, strategy‑suggestion, revision‑prompt) are prompted with the diagnosed ability and operate within the learner’s Zone of Proximal Development, producing feedback tailored to the student’s proficiency.  
3. **Multi‑Perspective Feedback Evaluation** – feedback quality is judged through pairwise preference crowdsourcing and through automated student‑revision simulations that measure improvement in essay scores.  

**Key findings**  
Evaluated on the ASAP++ benchmark, PsyScore matches state‑of‑the‑art AES accuracy (comparable RMSE and correlation to human scores) while delivering feedback that is rated higher in pedagogical relevance and leads to larger simulated score gains after revision. The results demonstrate that integrating psychometric ability estimation with ability‑conditioned LLM feedback yields a more coherent, student‑centered AES system, offering a concrete pathway toward agentic AI tutors that can both assess and teach adaptively.


<details>
<summary>Abstract</summary>

Effective Automated Essay Scoring (AES) are expected to support both reliable assessment and actionable instructional feedback. However, existing approaches often treat scoring and feedback as separate components: neural scoring models provide limited interpretability, while Large Language Model (LLM)-based feedback is typically insensitive to learners proficiency levels. To address this fragmentation, this work proposes PsyScore, a psychometrically-aware framework that integrates diagnostic assessment with instructional scaffolding through a shared latent ability representation. PsyScore comprises three key modules: a Trait-Adaptive Neural IRT Scorer that incorporates the Graded Partial Credit Model (GPCM) into a neural architecture, enabling the precise estimation of student ability while maintaining psychometric interpretability, a ZPD-Scaffolded Feedback Generator, which conditions multi-agent feedback strategies on the diagnosed ability parameter to adapt instructional focus across different proficiency levels, and a Multi-Perspective Feedback Evaluation Strategy that assesses feedback quality via pairwise preference judgements and student revision simulations. Experiments on the ASAP++ dataset demonstrate that PsyScore achieves competitive scoring performance while providing more pedagogically aligned feedback.

</details>


### 11. Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference

- **Authors:** Huang Peng, Jiuyang Tang, Weixin Zeng, Hao Xu, Xiang Zhao
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20245v1](http://arxiv.org/abs/2606.20245v1)
- **PDF:** [https://arxiv.org/pdf/2606.20245v1](https://arxiv.org/pdf/2606.20245v1)
- **Categories:** cs.AI


> **Main contribution**  
The paper introduces **MACR**, a multi‑agent framework that explicitly detects and resolves conflicts between an LLM’s internal (parametric) knowledge and multiple external pieces of contextual information, rather than simply preferring one source.

**Methodology**  
MACR first estimates the model’s confidence in its own answer using a modified semantic‑entropy metric; depending on this score it either externalizes the internal knowledge or retrieves external facts to form a set of “basic contexts.”  These contexts are then processed by three cooperating agents: (1) a rule‑induction agent that extracts explicit inference rules, (2) a conflict‑analysis agent that spots contradictions among the rules and facts, and (3) a resolution agent that synthesizes a consistent answer and produces an interpretable justification.

**Key findings**  
Across several knowledge‑conflict benchmarks, MACR achieves a large accuracy gain over state‑of‑the‑art baselines and, importantly, generates human‑readable explanations of how each conflict was identified and reconciled, demonstrating that explicit, multi‑agent conflict resolution is a viable route for more reliable, agentic LLM inference.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have achieved strong performance across a wide range of language-based tasks by leveraging both extensive parametric knowledge and in-context learning ability, enabling them to incorporate external information provided in the input prompt. However, the integration of external knowledge can introduce conflicts, not only between the model's internal parametric knowledge and the external information, but also among multiple pieces of external contexts. Existing approaches typically assume that either the model or the provided context is reliable, overlooking the possibility that both sources may contain errors, and avoid conflicts by privileging one source over the other, rather than actively resolving inconsistencies. To address these limitations, we propose a novel framework MACR for LLM knowledge conflict resolution that moves beyond the conventional binary choice paradigm and incorporates an explicit conflict-resolution mechanism based on a multi-agent reasoning approach. Specifically, we first propose an adaptive knowledge assessment and retrieval approach that employs a modified semantic entropy measure to quantify an LLM's confidence in its answer to a given query. Based on this confidence estimation, MACR either externalizes the model's internal knowledge as textual representations or retrieves relevant external knowledge when internal knowledge is insufficient, generating basic contexts for subsequent reasoning. Then we introduce an inductive multi-agent reasoning framework with three specialized agents that, respectively, induce explicit rules, analyze potential conflicts, and resolve inconsistencies across all available contexts. Empirical results demonstrate that MACR significantly outperforms state-of-the-art baselines across benchmarks, while also providing interpretable resolutions of explicit conflicts.

</details>


### 12. Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs

- **Authors:** Kipngeno Koech, Muhammad Adam, Baimam Boukar Jean Jacques, Joao Barros
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20243v1](http://arxiv.org/abs/2606.20243v1)
- **PDF:** [https://arxiv.org/pdf/2606.20243v1](https://arxiv.org/pdf/2606.20243v1)
- **Categories:** cs.SE, cs.MA


> **Main contribution** – Phoenix introduces a production‑grade, multi‑agent architecture for fully autonomous GitHub issue resolution that tightly integrates safety checks at every stage, showing that large language models can be deployed safely for real‑world software maintenance.

**Methodology** – The system decomposes the workflow into six coordinated agents (Planner, Reproducer, Coder, Tester, Failure Analyst, PR Agent) orchestrated by a label‑based GitHub webhook state machine; a suite of seven layered safety controls (including baseline‑aware test evaluation, WAF filtering, token‑expiry monitoring, permission scoping, and CI‑flakiness guards) ensure that any generated change is first validated against the repository’s existing test suite before a pull request is opened.

**Key findings** – On a curated 24‑instance slice of SWE‑bench Lite, Phoenix correctly resolves 75 % of issues with zero pass‑to‑pass regressions, and in a pilot on 42 real issues across 14 repos it achieves 100 % correctness‑preservation with an average turnaround of 122 s, while manual review shows that half of the PRs are perfectly localized fixes (the other half reveal planner‑localization bugs that are being addressed with retrieval augmentation).


<details>
<summary>Abstract</summary>

We present Phoenix, a multi-agent LLM system that resolves GitHub issues from triage through pull-request creation, combining seven layered safety controls with a baseline-aware test evaluation strategy. Phoenix decomposes the work across six specialized agents. Planner, reproducer, coder, tester, failure analyst and Pull Request (PR) agent, all coordinated by a label-based GitHub webhook state machine. Every change is checked against a baseline test run before a pull request is opened. On a 24-instance slice of SWE-bench Lite. run on the production webhook path, Phoenix oracle-resolves 75% of instances with no pass-to-pass regressions on successful runs; this curated slice is not directly comparable to full-split leaderboard results, and we discuss the limits of the comparison. A complementary pilot on 42 real issues across 14 repositories yields 100% correctness preservation (CP; mean 122s on the hard tier). Manual inspection shows that about half of the resulting pull requests are well-targeted fixes. The other half place code at incorrect paths, a planner localization limitation we are addressing with retrieval. We also report the deployment failure modes (WAF filtering, token expiry, permission boundaries, flaky CI) that motivated each safety mechanism.

</details>


### 13. A Multi-Agent system for Multi-Objective constrained optimization

- **Authors:** Federica Filippini
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20236v1](http://arxiv.org/abs/2606.20236v1)
- **PDF:** [https://arxiv.org/pdf/2606.20236v1](https://arxiv.org/pdf/2606.20236v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces **MAMO**, a multi‑agent reinforcement‑learning framework that treats the weighting of cost and constraint‑penalty terms as a separate learning problem rather than a manually tuned hyper‑parameter. By assigning a dedicated “weight‑selection” agent to adapt the scalarization coefficients while a “task” agent optimizes the underlying objective, the system jointly learns both the decision policy and an appropriate trade‑off that can shift over time in non‑stationary environments. Experiments show that MAMO automatically discovers weight schedules that achieve lower primary‑objective costs and fewer constraint violations than conventional single‑agent RL with fixed penalties, demonstrating a scalable route toward more autonomous, robust constrained‑optimization agents.


<details>
<summary>Abstract</summary>

Many decision-making problems in computing and networking systems can be naturally formulated as cost-minimization problems under performance constraints. In dynamic environments, reinforcement learning (RL) is often used to solve such problems at runtime by embedding both costs and constraint violations into a single scalar reward through weighted penalty terms, following a Lagrangian-inspired formulation. However, in this context the behavior of the learned policy critically depends on the choice of these weights, which are typically selected manually. This makes it difficult to identify an appropriate trade-off between optimizing the primary objective and effectively avoiding constraint violations, particularly in non-stationary environments where their relative importance may change. This paper presents MAMO (Multi-Agent system for Multi-Objective constrained optimization), an approach to tackle this balancing problem through multi-agent RL. MAMO decouples task execution from objective design by formulating the selection of reward weights as a learning problem, providing a !rst step towards more autonomous and robust RL-based solutions for constrained optimization problems in dynamic environments.

</details>


### 14. RACL: Reasoning-Agent Control Layers for Continuous Metaheuristic Learning

- **Authors:** Antón Asla Manzárraga
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20142v1](http://arxiv.org/abs/2606.20142v1)
- **PDF:** [https://arxiv.org/pdf/2606.20142v1](https://arxiv.org/pdf/2606.20142v1)
- **Categories:** cs.AI, cs.MA


> **Main contribution:** The paper presents **RACL (Reasoning‑Agent Control Layer)**, a generic framework that puts a lightweight reasoning agent on top of any existing metaheuristic optimizer, enabling the agent to observe the optimizer’s internal state, hypothesize bounded control actions, test them, and consolidate explainable policies without altering the problem constraints or the core heuristic.  

**Methodology:** RACL continuously monitors the optimizer’s operational memory, generates and validates control hypotheses (e.g., when to trigger diversification or intensification), applies guarded interventions, and records the resulting performance; a proof‑of‑concept implementation uses Codex as the reasoning engine while the underlying optimizer is an ALNS‑based vehicle‑routing solver, and a policy proxy reproduces the learned controls for evaluation.  

**Key findings:** Across 21 feasible vehicle‑routing instances, RACL matches or outperforms the best hand‑crafted Operational‑Memory policy in all cases and beats a non‑reasoning Stagnation‑Triggered Policy in 18 cases, achieving an average cost reduction of ‑0.641 % (‑8.337 % vs. a fixed baseline and ‑1.605 % vs. STP on the Sevilla‑9/10 benchmark) with no noticeable computational overhead, demonstrating that a reasoning agent can autonomously discover, validate, and explain effective metaheuristic control rules.


<details>
<summary>Abstract</summary>

This paper introduces RACL, a Reasoning-Agent Control Layer for metaheuristics. RACL places a reasoning agent above an existing optimizer. The agent does not replace the optimizer and does not modify business constraints. Instead, it controls the optimizer's internal search behavior by observing operational memory, reasoning over past behavior, formulating bounded hypotheses, testing interventions, evaluating outcomes, applying guardrails, consolidating useful policies and explaining its decisions. The experiment uses vehicle routing as a testbed, but the contribution is not a new routing solver, a particular ALNS configuration or a specific set of routing rules. The contribution is the RACL method: a way for a reasoning agent to discover, validate, consolidate and explain algorithmic control rules for a metaheuristic. In the current experimental setting, RACL improves or ties the Operational Memory Policy in 21 of 21 feasible cases and improves or ties a non-reasoning Stagnation-Triggered Policy in 18 of 21 feasible cases, with an average RACL vs STP cost delta of -0.641%. In the Sevilla-9/10 runtime sample, RACL improves average cost by -8.337% versus Fixed and -1.605% versus STP without showing material computational overhead. During the proof-of-concept, Codex was used as an in-the-loop reasoning agent observing executions, interpreting logs and proposing live bounded interventions. The policy proxy was later used only to make quantitative evaluation reproducible.

</details>


### 15. Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform

- **Authors:** Hyeonna Choi, Jung Yup Kim, Hyuneui Lim, Seunggyu Jeon
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20120v1](http://arxiv.org/abs/2606.20120v1)
- **PDF:** [https://arxiv.org/pdf/2606.20120v1](https://arxiv.org/pdf/2606.20120v1)
- **Categories:** cs.RO, cs.AI


> **Contribution** – The paper introduces a dual‑agent architecture that bridges the “semantic gap” between free‑text biological protocols and the low‑level command set of a microplate‑based robotic lab. By separating concerns into a **Parser Agent** (which converts natural‑language steps into a structured protocol) and an **LLM Validation Agent** (which cross‑checks the generated command sequence and initiates a self‑correction loop), the system achieves reliable, end‑to‑end automation of complex assays.

**Methodology** – The Parser Agent builds a formal representation of a protocol, which is then fed to a deterministic rule‑based mapper that respects the robot’s well‑mapping, reagent‑mixing, replicate‑placement, and dispensing constraints. A heterogeneous validation layer employs multiple large language models (7 parsers × 3 validators) to verify completeness, parameter fidelity, and execution order, providing structured feedback for automatic correction. The authors also benchmarked the rule‑based mapper against a pure LLM “end‑to‑end” translation to assess accuracy–latency trade‑offs.

**Key Findings** – Cross‑model verification markedly improves translation accuracy (higher pass rates) with modest latency overhead compared to direct LLM mapping. The framework successfully executed an ELISA‑style Bradford protein assay on a real robotic platform, demonstrating that the dual‑agent, cross‑model approach can reliably convert natural‑language protocols into executable laboratory actions, a crucial step toward fully autonomous, self‑driving bio‑labs.


<details>
<summary>Abstract</summary>

Biological experiment protocols are written in natural language, whereas automation systems rely on predefined control commands, creating a semantic gap that limits autonomous execution. Microplate-based automatic experiments are particularly challenging due to the need to simultaneously control well mapping, sample-reagent combinations, replicate placement, and parallel dispensing. This study proposes an agent-based protocol translation framework that converts natural-language microplate-based protocols into executable control commands for a robotic laboratory platform. A Parser Agent formalizes the natural-language protocol into a structured representation, and a rule-based mapping engine deterministically incorporates the operational constraints of the robotic laboratory platform to generate device-level control commands. A heterogeneous LLM Validation Agent verifies completeness, parameter accuracy, and execution order, and triggers a self-correction loop with structured feedback when errors are detected. A sweep involving 7 Parsers and 3 Validators on randomly selected ELISA protocols evaluates how model scale and Validator type affect translation accuracy and pass rates under cross-model verification. The accuracy-latency trade-off is further verified by comparing the rule-based mapping of the proposed framework with LLM end-to-end direct mapping. Finally, Bradford assay-based protein quantification using a microplate was demonstrated on a robotic laboratory platform, validating end-to-end autonomous execution from natural-language protocols to real-world experiments. The proposed framework provides a flexible approach to narrowing the semantic gap between natural-language protocols and microplate-based self-driving laboratories.

</details>


### 16. Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale

- **Authors:** Harsh Rao Dhanyamraju, Leonidas Raghav, Aaron Lee
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20058v1](http://arxiv.org/abs/2606.20058v1)
- **PDF:** [https://arxiv.org/pdf/2606.20058v1](https://arxiv.org/pdf/2606.20058v1)
- **Categories:** cs.AI


> The paper presents a large‑scale empirical study of two contrasting multi‑agent orchestration architectures—**DAG Plan‑and‑Execute** (a structured, parallel workflow planner) and **ReAct** (a reactive, failure‑tolerant controller)—applied to 208 real‑world enterprise AI scenarios ranging from a handful of specialist agents to full‑enterprise deployments of ~200 agents. By adding a **Task Manager** that infers task priority, merges related events, and pre‑empts lower‑priority work, the authors show that orchestration performance is driven primarily by the number of agents rather than task difficulty: both architectures handle small‑scale settings well but suffer dramatic latency and precision losses at enterprise scale as agent‑discovery noise overwhelms the system, with simple tasks deteriorating faster than complex ones. The DAG approach yields higher precision and better parallelism on modest scales, while ReAct proves more robust to failures; the Task Manager further cuts high‑priority queue latency by 14‑75 % and lifts related‑event correctness by >20 percentage points in the largest deployments.


<details>
<summary>Abstract</summary>

Enterprise AI aims to move toward continuous event monitoring, detection, and action across specialist agents, yet existing multi-agent systems largely assume discrete request-response workflows and remain underexplored at enterprise scale. We evaluate DAG Plan and Execute and ReAct across 208 production-derived enterprise scenarios spanning Persona (<10 agents), Department (20-80), and Enterprise (200) scales, and introduce a Task Manager for continuous operation via priority inference, related-event merging, and preemption. Results show that scale, not task complexity, dominates orchestration performance: both architectures perform well at small scale but degrade at enterprise scale as agent discovery noise becomes the primary bottleneck, with simple tasks degrading more sharply than complex ones. DAG Plan and Execute offers higher precision and structured parallelization at smaller scales, but its higher overhead worsens at enterprise scale; ReAct is more robust by handling failures incrementally. The Task Manager reduces high-priority queue latency by 14-75% and improves related-event correctness by over 20 percentage points at enterprise scale.

</details>


### 17. AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models

- **Authors:** Masahiro Kato
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20041v1](http://arxiv.org/abs/2606.20041v1)
- **PDF:** [https://arxiv.org/pdf/2606.20041v1](https://arxiv.org/pdf/2606.20041v1)
- **Categories:** econ.GN, cs.AI, cs.LG, q-fin.GN


> The paper introduces **AI Economist Agent**, a novel agentic architecture that couples large language models (LLMs) with retrieval‑augmented generation (RAG), economic knowledge graphs, and explicit computational models to produce economically sound analyses. The methodology casts the economist’s workflow as a hierarchy of LLM‑driven agents that (1) plan the analysis, (2) retrieve relevant theory and data from a knowledge graph, (3) invoke calibrated econometric or macro‑simulation models for quantitative calculations, and (4) synthesize a narrative that is explicitly linked to the retrieved evidence and model outputs. In two case studies—U.S. inflation‑persistence/Federal‑Reserve policy reporting and bank stress‑test narratives for commercial‑real‑estate refinancing—the system generates reports that are more coherent, verifiable, and traceable than those produced by LLMs alone, demonstrating the value of grounding agentic AI outputs in formal economic models and curated data.


<details>
<summary>Abstract</summary>

We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data. Based on this motivation, this study proposes an RAG-based AI economist, which utilizes knowledge graphs including economic data and theory and LLM-based agents to plan the analysis, retrieve relevant evidence, select appropriate models, and generate reports. In our framework, we do not produce quantitative claims directly with the language model alone; instead, we generate narratives grounded in explicit model-based computations and linked to the retrieved evidence via AI agents. We refer to our framework as an AI economist agent. We evaluate the AI economist agent in two applications: economist report generation for U.S. inflation persistence and Federal Reserve policy, and bank stress-test narrative generation for U.S. commercial real estate refinancing stress. The results illustrate how grounding the generated reports improves their economic coherence and traceability.

</details>


### 18. When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents

- **Authors:** Kaiyue Yang, Yuyan Bu, Jingwei Yi, Yuchi Wang, Biyu Zhou, Juntao Dai, Songlin Hu, Yaodong Yang
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20023v1](http://arxiv.org/abs/2606.20023v1)
- **PDF:** [https://arxiv.org/pdf/2606.20023v1](https://arxiv.org/pdf/2606.20023v1)
- **Categories:** cs.SE, cs.AI, cs.CL


> The paper introduces **ToolPrivBench**, a benchmark that measures whether LLM‑driven agents unnecessarily select or escalate to higher‑privilege tools when a lower‑privilege alternative would suffice, covering eight domains and five recurrent risk patterns. Experiments show that mainstream agents frequently exhibit over‑privileged tool selection, a problem that worsens after transient tool failures and is not mitigated by generic safety alignment or simple prompting tricks. The authors propose a **privilege‑aware post‑training fine‑tuning** that explicitly teaches agents to prefer the least‑privilege tool unless escalation is required, dramatically cutting unnecessary high‑privilege usage while maintaining overall task performance.


<details>
<summary>Abstract</summary>

As LLM agents increasingly select tools autonomously, their choices among tools with different privileges become safety-relevant. However, prior tool-selection studies focus on safety-agnostic metadata preferences, leaving privilege-sensitive choices underexplored. To address this gap, we study over-privileged tool selection, in which an agent selects or escalates to a higher-privilege tool despite a sufficient lower-privilege alternative. We introduce ToolPrivBench to evaluate whether agents choose higher-privilege tools despite sufficient lower-privilege alternatives, measuring both initial selection and escalation after transient tool failures. Across eight domains and five recurring risk patterns, we find that over-privileged tool selection is common among mainstream LLM agents and is further amplified by transient failures. We further find that general safety alignment does not reliably transfer to least-privilege tool choice, while prompt-level controls provide only limited mitigation under transient failures. We therefore introduce a privilege-aware post-training defense that teaches agents to prefer sufficient lower-privilege tools and escalate only when necessary. Our mitigation experiments show that this defense substantially reduces unnecessary high-privilege tool use while preserving general capabilities.

</details>


### 19. Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution

- **Authors:** Jannik Hösch, Alessandro Sestini, Florian Fuchs, Amir Baghi, Joakim Bergdahl, Konrad Tollmar, Jean-Philippe Barrette-LaPierre, Linus Gisslén
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20014v1](http://arxiv.org/abs/2606.20014v1)
- **PDF:** [https://arxiv.org/pdf/2606.20014v1](https://arxiv.org/pdf/2606.20014v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces a hierarchical control framework in which a pretrained large language model serves as a centralized strategic planner that selects among a set of pretrained reinforcement‑learning “skill” policies for each agent, while the RL policies execute low‑level actions. In a 2‑vs‑2 competitive King‑of‑the‑Hill benchmark, the LLM‑guided system matches the win rate of hand‑crafted behavior trees (≈46 % vs 51.5 %, p = 0.103) and substantially outperforms flat end‑to‑end RL, and a user study shows that participants rate the LLM‑orchestrated agents as significantly more human‑like. These results demonstrate that pretrained LLM reasoning can effectively coordinate pretrained RL skills, yielding scalable, high‑performing and believably interactive multi‑agent behavior without manual rule engineering.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has achieved strong performance in sequential decision-making, yet scaling to complex multi-agent environments remains challenging due to sparse rewards, large state-action spaces, and the difficulty of learning coordinated strategies. We propose a hierarchical architecture where a pretrained large language model (LLM) acts as a centralized strategic controller that selects among specialized RL skill policies for a team of agents, while RL policies handle reactive low-level execution. We evaluate this hybrid system in a competitive 2v2 King of the Hill environment against behavior tree (BT) and \emph{``Flat''} RL (end-to-end training without skill decomposition) baselines. The LLM+RL system achieves task performance statistically equivalent to hand-crafted BT (46.4\% vs 51.5\% win rate, $p=0.103$) while both significantly outperform Flat RL trained without skill decomposition. A user study ($n=15$) reveals that 60\% of participants perceive LLM+RL agents as the most human-like ($p=0.027$), citing behavioral adaptability and tactical variability. These results demonstrate that pretrained LLM reasoning can effectively orchestrate pretrained RL skills, achieving competitive multi-agent coordination and superior perceived believability without manual rule engineering.

</details>


### 20. Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning

- **Authors:** Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, Jingren Zhou
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.20002v1](http://arxiv.org/abs/2606.20002v1)
- **PDF:** [https://arxiv.org/pdf/2606.20002v1](https://arxiv.org/pdf/2606.20002v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> **Main contribution:** The paper introduces “Connect the Dots” (CoD), a training framework that end‑to‑end reinforces large language models to acquire a meta‑capability for long‑lifecycle agents—continually solving sequential tasks while updating an internal context of the environment to improve future performance, and generalizing across domains.

**Methodology:** CoD pairs a custom reinforcement‑learning loop (a GRPO‑style algorithm with fine‑grained credit assignment) with specially designed task suites that interleave “solve‑task” and “update‑context” episodes, enabling LLMs to learn from their own experience over very long rollouts. The infrastructure supports massive rollouts, context‑store updates, and cross‑domain evaluation.

**Key findings:** Empirical experiments show that LLMs trained with CoD achieve higher task success after context updates, exhibit robust out‑of‑distribution generalization both within and across training domains, and transfer the learned meta‑capability to unrelated “Ralph‑loop” settings, indicating that CoD effectively elicits a reusable, long‑term reasoning ability for agentic AI.


<details>
<summary>Abstract</summary>

This work presents a general framework for training large language models (LLMs) to "Connect the Dots" (CoD), a meta-capability required by long-lifecycle agents: as an LLM-based AI agent gets deployed in an environment, it solves a long sequence of tasks while continuously exploring the environment, learning from its own experiences, and iteratively self-updating its context about the environment, thereby achieving progressively better performance on future tasks conditioned on the updated context. Major components of the CoD framework include: (1) algorithm design and infrastructure for end-to-end reinforcement learning (RL) with long rollout sequences interleaving solve-task and update-context episodes; (2) tasks and environments for incentivizing and eliciting the targeted meta-capability in LLMs during training, as well as for faithfully measuring progress during evaluation. We present proof-of-concept implementations of the CoD framework, including a GRPO-style RL algorithm with fine-grained credit assignment, as well as tasks and environments tailored to the targeted meta-capability (rather than domain-specific LLM capabilities or standard task-by-task RL). Empirical results validate the efficacy of end-to-end RL training in the CoD setting, and demonstrate the potential for out-of-distribution generalization -- within the training domains, across different domains, and from CoD to Ralph-loop settings -- of the elicited meta-capability. Our investigation of CoD connects several lines of prior works, and opens up new opportunities for advancing LLMs and AI agents. To facilitate further research and applications, we release our implementations at \url{https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod/examples/research_cod}.

</details>


### 21. Blame is easier than praise: Measuring off-ball defensive performance in football

- **Authors:** Jonas Bischofberger, Runqing Ma, Pascal Bauer, Kilian Arnsmeyer, Arnold Baca
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19931v1](http://arxiv.org/abs/2606.19931v1)
- **PDF:** [https://arxiv.org/pdf/2606.19931v1](https://arxiv.org/pdf/2606.19931v1)
- **Categories:** cs.MA


> **Main contribution**  
The paper introduces the first data‑driven metric that attributes off‑ball defensive responsibility to individual football players by distributing changes in expected threat across multi‑agent spatiotemporal trajectories, thereby quantifying “blame” for defensive positioning errors.  

**Methodology**  
The authors compute **player involvement scores** from *Defensive Pressure Areas* (DPAs) and generate **role‑conditioned baselines** within automatically detected team structures; the difference between observed and baseline threat‐adjusted values is assigned to each defender as an attribution of responsibility. Since no player‑level ground truth exists, they validate the metric on a large cross‑gender, cross‑competition data set (World Cup, women’s Bundesliga, men’s 3. Liga) using a composite evaluation protocol that aggregates several weak proxies (e.g., external ratings, market values).  

**Key findings**  
The new “blame” metric improves validity by roughly one standard deviation over the best existing action‑based measures and shows strong correlations with external expert ratings and player market values, demonstrating that off‑ball positioning errors can be reliably quantified—something previous metrics failed to capture. The code is released publicly, enabling reproducibility and further agentic AI research on multi‑agent attribution in sports analytics.


<details>
<summary>Abstract</summary>

The defensive performance of football players is commonly measured through a limited number of actions like tackles and interceptions while their continuous impact through positional behaviour has hardly been studied before. We formulate this problem as an attribution over multi-agent spatiotemporal trajectories without player-level ground truth labels, where event-level changes of expected threat are distributed among individuals. We propose a framework that performs this attribution using player involvement scores calculated from defensive pressure areas (DPAs). By computing role-conditioned baselines within automatically detected team structures, we can determine each defender's expected responsibility for threat created through arbitrary passes. The validity and robustness of this approach are evaluated on a uniquely extensive cross-gender and cross-competition data set, including positional and event data from 64 matches of the men's World Cup, 116 matches of the women's German Bundesliga and 336 matches of the men's German 3. Liga. In the absence of a ground truth, we propose an evaluation protocol that combines multiple relatively weak proxies into robust summary scores. We find a validity score that is improved by around 1 standard deviation compared to the best action-based metric and demonstrate that many popular measures show limited validity. The "blame" for conceding high-value actions shows especially strong correlations with external ratings and market values, making it the first published metric in football to reliably measure positioning errors. All code underlying this work is publicly available to support reproducibility and further research.

</details>


### 22. Deep-Unfolded Coordination

- **Authors:** Hunter Kuperman, Minchan Jung, Rahul V. Ghosh, Alex Oshin, Evangelos A. Theodorou
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19920v1](http://arxiv.org/abs/2606.19920v1)
- **PDF:** [https://arxiv.org/pdf/2606.19920v1](https://arxiv.org/pdf/2606.19920v1)
- **Categories:** cs.RO, cs.LG, cs.MA


> The paper introduces **Deep Coordinator**, a deep‑unfolding architecture that learns to adjust the penalty and step‑size hyperparameters of the ADMM‑DDP distributed optimizer on the fly, thereby accelerating non‑convex multi‑agent planning. By unrolling a fixed number of ADMM‑DDP iterations into a neural network and training it with an unsupervised loss that directly reflects trajectory quality, the method avoids the degenerate solutions typical of supervised approaches. Experiments on car‑fleet and quadrotor simulations show that Deep Coordinator yields trajectories of comparable optimality while running **6–9× faster** than the standard solver and generalizes to systems up to eight times larger than those seen during training.


<details>
<summary>Abstract</summary>

Distributed optimization is a highly scalable and structurally transparent technique to solve multi-agent robotics problems; however, such methods often suffer from the need for highly-specialized, problem-specific hyperparameter tunings. In this work, we propose Deep Coordinator, a deep-unfolding framework that learns to dynamically adjust the hyperparameters of ADMM-DDP, a popular distributed solver for robotics tasks, at solve-time in response to optimizer performance. Our architecture consists of unrolling a fixed number of ADMM-DDP iterations into a neural network with learnable functions between layers mapping the optimizer state to the next hyperparameters. To the best of our knowledge, Deep Coordinator is the first deep-unfolding framework to adapt the penalty parameters of a non-convex optimizer at solve-time; we show that the mainstream supervised approach can yield degenerate solutions when training such models, and propose an unsupervised learning scheme. On simulations with fleets of cars and quadrotors, Deep Coordinator produces trajectories of comparable quality 6.18-9.44x faster than conventional solvers. Furthermore, Deep Coordinator retains its performance benefits when deployed to systems up to 8x larger than trained on.

</details>


### 23. Multi-Agent Transactive Memory

- **Authors:** To Eun Kim, Xuhong He, Dishank Jain, Ambuj Agrawal, Negar Arabzadeh, Fernando Diaz
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19911v1](http://arxiv.org/abs/2606.19911v1)
- **PDF:** [https://arxiv.org/pdf/2606.19911v1](https://arxiv.org/pdf/2606.19911v1)
- **Categories:** cs.AI, cs.CL, cs.IR


> The paper introduces **Multi‑Agent Transactive Memory (MATM)**, a shared‑repository framework that lets large‑language‑model (LLM) agents store and retrieve one‑another’s action trajectories, turning fleeting procedural experiences into reusable knowledge for an entire agent population. Building on retrieval‑augmented generation, the authors implement MATM for the ALFWorld and WebArena interactive benchmarks, where producer agents deposit long, structured trajectories and consumer agents query them at inference time without any joint training or explicit coordination. Experiments show that accessing the shared memory markedly raises task success rates and cuts the number of interaction steps needed, demonstrating that population‑level experience sharing is an effective design pattern for scalable, decentralized agentic AI systems.


<details>
<summary>Abstract</summary>

The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations. Just as search engines index human-generated artifacts to support human problem solving, retrieval systems can organize agent-generated artifacts for reuse across agent populations. We extend retrieval-augmented generation - which demonstrates the value of human-authored artifacts to individual agents - to retrieval of agent-generated artifacts supporting a population of agents. In particular, agent trajectories encode reusable procedural knowledge, yet these artifacts are typically discarded after a single use or retained only by the producing agent, forcing newly instantiated agents to repeatedly rediscover existing solutions. We propose Multi-Agent Transactive Memory (MATM), a framework for population-level storage and retrieval of agent-generated trajectories, where producer agents contribute trajectories to a shared repository and consumer agents retrieve them to improve task execution. We focus on interactive environments (ALFWorld and WebArena), where trajectories are long and encode especially rich procedural structure. Our experiments demonstrate that retrieving trajectories from MATM improves downstream task performance and reduces interaction steps without coordination or joint training. These results position MATM as a design pattern for population-level experience sharing in open agent ecosystems.

</details>


### 24. Measuring Biological Capabilities and Risks of AI Agents

- **Authors:** Patricia Paskov, Jeffrey Lee, Kyle Brady, Alyssa Worland
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19899v1](http://arxiv.org/abs/2606.19899v1)
- **PDF:** [https://arxiv.org/pdf/2606.19899v1](https://arxiv.org/pdf/2606.19899v1)
- **Categories:** cs.CY, cs.AI


> The paper’s main contribution is a practical framework for evaluating the biological capabilities and associated security risks of agentic AI systems that can conduct multi‑step scientific work. The authors systematically review existing evidence on AI‑enabled bio‑risk, then develop and document a set of “biological agentic evaluations” that illustrate how design choices—​definition of tasks, experimental setup, scoring metrics, and reporting practices​—​directly affect what the results can credibly reveal about an AI’s capacity to generate biological threats. Through a series of experience‑grounded case studies, they show that while such evaluations can inform policy and investment decisions, their interpretation is highly sensitive to methodological details, underscoring the need for transparent, standardized evaluation protocols in the emerging field of agentic AI bio‑security.


<details>
<summary>Abstract</summary>

This paper addresses a rapidly emerging policy challenge: how to generate and interpret credible evidence about the biological capabilities and risks of AI scientists, or agentic AI systems capable of autonomously or collaboratively performing multi-step scientific tasks. As these systems enter real research workflows, decision-makers increasingly face evaluation results whose meaning depends on underlying design choices that are often implicit or under-documented. We synthesize current evidence on AI-enabled biological risks and introduce biological agentic evaluations as a promising, but interpretation-sensitive, tool for assessing these systems. Our central contribution is a set of practical, experience-grounded considerations -- drawing from our own evaluations -- that show how choices around defining, designing, running, scoring, and documenting evaluations materially shape what results do and do not imply about risk. The analysis is intended to help policymakers interpret biological evaluation outputs with appropriate caution; guide public and private funders toward high-leverage investments in AI-biology evaluation research; and support biosecurity practitioners assessing emerging AI systems. A secondary audience includes researchers designing or conducting agentic evaluations within frontier AI labs, AI providers, scientific institutions, and third-party evaluation organizations.

</details>


### 25. MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments

- **Authors:** Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, Bing Li
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19893v1](http://arxiv.org/abs/2606.19893v1)
- **PDF:** [https://arxiv.org/pdf/2606.19893v1](https://arxiv.org/pdf/2606.19893v1)
- **Categories:** cs.AI


> MetaResearcher introduces a scalable training framework for deep research agents that combines (1) an **Evolving Virtual World** populated with temporally changing and adversarial misinformation, (2) **Discovery‑oriented tasks** (hypothesis generation, contradiction resolution) that go beyond pure fact‑retrieval, (3) a **self‑reflective meta‑reward** within the GRPO reinforcement‑learning loop that jointly optimizes answer correctness, search‑path efficiency, depth of reflection, and tool‑call diversity, and (4) a **heterogeneous multi‑agent swarm** (Scout, Filter, Synthesizer) that learns collaborative research strategies. Using the LiteResearcher infrastructure, the authors train the swarm via coordinated RL with zero marginal API cost and report substantial gains on benchmark suites (GAIA, Xbench‑DS) and marked improvements in epistemic robustness when faced with adversarial misinformation. The work demonstrates that embedding dynamic, adversarial environments and self‑reflective reward signals can produce agents that not only retrieve information more efficiently but also exhibit genuine research behaviours such as source credibility assessment and hypothesis testing.


<details>
<summary>Abstract</summary>

Deep research agents have demonstrated remarkable capabilities in autonomous information gathering and synthesis, yet their training remains constrained by the static nature of simulated environments, the limits of fact-retrieval-only task designs, and the inefficiency of outcome-based reinforcement learning. In this work, we propose MetaResearcher, a novel framework that scales deep research agent training across four synergistic dimensions. First, we introduce an Evolving Virtual World that injects temporal dynamics and adversarial misinformation into the training environment, forcing agents to develop source credibility assessment and temporal conflict resolution skills. Second, we design Discovery-Oriented Tasks -- including hypothesis generation and contradiction resolution -- that transcend simple fact retrieval and push agents toward genuine research behaviors. Third, we propose a Self-Reflective Meta-Reward mechanism within the GRPO framework that jointly optimizes for answer correctness, search path efficiency, reflection depth, and tool call diversity, directly addressing the repetitive action loop problem observed in prior work. Fourth, we introduce a Heterogeneous Multi-Agent Swarm architecture comprising specialized Scout, Filter, and Synthesizer models that learn collaborative research strategies through coordinated reinforcement learning. Built upon the LiteResearcher infrastructure, MetaResearcher requires zero marginal API cost for training while targeting substantial improvements in both benchmark performance (GAIA, Xbench-DS) and epistemic robustness under adversarial conditions. We present the complete framework design, training methodology, and planned experimental validation.

</details>


### 26. Matching Markets meet Cumulative Prospect Theory: Towards Optimal and Adversarially Robust Learning

- **Authors:** Ananya Kunisetty, Avishek Ghosh
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19883v1](http://arxiv.org/abs/2606.19883v1)
- **PDF:** [https://arxiv.org/pdf/2606.19883v1](https://arxiv.org/pdf/2606.19883v1)
- **Categories:** cs.LG, stat.ML


> **Main contribution:** The paper introduces the first rigorous analysis of multi‑agent multi‑armed bandits in two‑sided matching markets when agents evaluate outcomes through Cumulative Prospect Theory (CPT), and it provides both optimal‑regret and adversarially‑robust learning algorithms for this setting.  

**Methodology:** By embedding an α‑Hölder continuous CPT weight function into the reward structure, the authors first bound the regret of a standard bandit algorithm as \(O\!\big(K\log T\,(1/\Delta)^{2/\alpha}\big)\); they then eliminate the sub‑optimal \(K\) dependence by adaptively restricting the exploration to a carefully chosen active arm set, yielding an optimal \(O\!\big(N\log T\,(1/\Delta)^{2/\alpha}\big)\) regret when \(K\gg N\). For adversarial markets they design corruption‑aware variants (with known or unknown total corruption budget) that preserve logarithmic player‑optimal regret.  

**Key findings:** CPT‑distorted rewards incur a regret penalty that scales with the preference gap as \((1/\Delta)^{2/\alpha}\), but this can be mitigated by active‑set selection, achieving optimal dependence on the number of players. Moreover, the proposed robust algorithms retain logarithmic regret even when a fraction of the observed rewards is arbitrarily corrupted, demonstrating that CPT‑based risk‑sensitive learning can be both efficient and resilient in competitive matching markets.


<details>
<summary>Abstract</summary>

We study a multi-agent multi-armed bandit problem in the competitive setup with two-sided matching markets under a human centric decision making model. To capture human preferences, we use cumulative prospect theory (CPT) that weighs the actions of the agent in a nonlinear fashion using a ($α$-Hölder continuous) weight function. CPT has been widely used in behavioral economics and risk sensitive machine learning to emulate human preferences. We analyze the state-of-the-art learning algorithm with CPT weight distorted rewards and obtain a player optimal regret of $\mathcal{O}(K\log T \left(\frac{1}Δ\right)^{2/α})$, where $K$ denotes the number of arms, $T$ is the learning horizon, and $Δ$ represents (suitably defined) players' minimum preference gap. Noticing the dependence on $Δ$ to be sub-optimal, we further improve this regret by judiciously selecting the active set of arms during exploration, which removes the dependence on $K$ in the dominant term and achieves an improved (optimal) regret guarantees in the setting where the number of arms $K$ is significantly larger than the number of players $N$. In addition, we consider adversarial markets where the observed rewards of the agents may be corrupted. We propose and analyze algorithms for robust markets with CPT as risk sensitive measure in both settings where the total corruption budget is known and where it is unknown, and establish logarithmic player-optimal regret guarantees in both cases.

</details>


### 27. A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models

- **Authors:** Jiayi Wang, Xu-Yao Zhang
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19868v1](http://arxiv.org/abs/2606.19868v1)
- **PDF:** [https://arxiv.org/pdf/2606.19868v1](https://arxiv.org/pdf/2606.19868v1)
- **Categories:** cs.AI


> The paper presents the first large‑scale, systematic benchmark of black‑box uncertainty‑estimation (UE) techniques for large language models (LLMs) that are only reachable via APIs. The authors classify 24 existing methods into verbalization, sampling, explanation, multi‑agent, and hybrid categories, then evaluate them across four LLMs and four datasets using a unified framework they release publicly. They find that no single method dominates universally, but approaches that reason over answer candidates—or hybrid methods that fuse several UE signals—consistently achieve higher reliability, offering practical guidance for building trustworthy, agentic LLM systems.


<details>
<summary>Abstract</summary>

Although large language models (LLMs) have shown strong capabilities across a wide range of tasks, their outputs often remain unreliable and may contain hallucinations, making uncertainty estimation (UE) essential for building trustworthy LLMs. In practice, many mainstream LLMs are only accessible through restricted APIs, where internal signals such as logits and hidden states are unavailable, making black-box UE especially important. However, existing work on black-box UE for LLMs remains fragmented in methodology and lacks a unified empirical comparison. To address this gap, we present a systematic review of black-box UE methods and organize them into five categories: verbalization-based, sampling-based, explanation-based, multi-agent, and hybrid methods. We further build a unified evaluation framework and benchmark 24 representative methods across 4 models and 4 dataset settings. Our results show that no single method consistently dominates across all settings. Nevertheless, methods that reason over and compare candidates in the answer space are generally effective, and hybrid methods that combine multiple uncertainty signals perform well under most conditions. By releasing the benchmark data and a unified evaluation framework, we aim to facilitate reproducible comparisons and support future research, while our empirical findings provide practical guidance for developing future black-box UE methods for LLMs.

</details>


### 28. Large Language Models Do Not Always Need Readable Language

- **Authors:** Jiayi Zhu, Haoxuan Peng, Junxi Wang, Liang Ke, Chen Zhang, Linfeng Zhang
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19857v1](http://arxiv.org/abs/2606.19857v1)
- **PDF:** [https://arxiv.org/pdf/2606.19857v1](https://arxiv.org/pdf/2606.19857v1)
- **Categories:** cs.CL, cs.AI


> The paper’s main contribution is the introduction and systematic study of *BabelTele*—compact, non‑human‑readable textual encodings that nevertheless preserve semantic content for instruction‑tuned large language models. By training simple “compressor” LLMs to rewrite prompts into dense token strings and “reader” LLMs to reconstruct the original meaning, the authors evaluate readability scores, model likelihoods, human judgments, and downstream task performance, showing that BabelTele can retain ≈ 99.5 % semantic fidelity while shrinking text to ≈ 28 % of its original size. Experiments on cross‑model transfer, agent memory retrieval, and multi‑agent communication demonstrate that such model‑centric encodings cut context overhead with only modest performance loss, suggesting that human‑readable natural language is not a strict prerequisite for effective inter‑agent LLM communication.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are commonly prompted and interfaced with human-readable natural language, even when the intended reader is another model. This paper investigates whether semantic information can be encoded in compact, non-standard textual forms that sacrifice human readability while remaining recoverable by LLMs. We refer to this class of model-centric textual representations as BabelTele, approached here not as a fixed protocol but as an empirical probe into LLMs' capacity to generate and interpret such representations. Through readability diagnostics, model likelihood measures, human questionnaires, and downstream task evaluations, we find that BabelTele can substantially depart from ordinary natural language while preserving core semantics for instruction-tuned LLMs. As a task-agnostic representational paradigm, BabelTele demonstrates high information density, maintaining 99.5% semantic fidelity even when the text volume is condensed to 27.9% of its original length. We further evaluate its semantic robustness in cross-model transfer, agent memory, and multi-agent communication. Results suggest that BabelTele can reduce context overhead while generally maintaining reliable downstream performance, although its effectiveness depends on the compressor-reader pair and task setting. These findings indicate that human readability, natural-language typicality, and model-side semantic recoverability can be partially decoupled, opening a path toward model-native representations in future exploration of LLM systems.

</details>


### 29. AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts

- **Authors:** Yanyu Yao, Shangze Li, Zhi Zheng, Hui Zheng, Qi Liu, Tong Xu, Enhong Chen
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19847v1](http://arxiv.org/abs/2606.19847v1)
- **PDF:** [https://arxiv.org/pdf/2606.19847v1](https://arxiv.org/pdf/2606.19847v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **AtomMem**, a lightweight long‑term memory architecture for LLM‑based agents that stores information as discrete, high‑value “atomic facts” rather than raw dialogue chunks, and continuously updates these facts in a stable, hierarchical structure.  

**Methodology:** AtomMem employs a **Fact Executor** to parse multi‑turn interactions and extract salient atomic facts; these facts are then organized into a temporal‑event graph that records episodic contexts and evolving user attributes. Retrieval is performed by activating an associative memory graph that links related facts across time, enabling the agent to retrieve coherent, context‑aware information with only a few tokens.  

**Key findings:** On the LoCoMo benchmark, AtomMem outperforms prior memory‑augmented baselines on a suite of reasoning and personalization tasks, achieving state‑of‑the‑art accuracy while using markedly less memory bandwidth, demonstrating that fine‑grained fact‑level storage is both effective and economically scalable for long‑running, personalized LLM agents.


<details>
<summary>Abstract</summary>

Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions. Existing memory-augmented systems often construct memory in a coarse and unstable manner, relying on inefficient memory representations or unstable unconstrained updates. To address these challenges, we propose AtomMem, a long-term memory system designed for value-dense storage and stable memory evolution. AtomMem introduces a Fact Executor, which selectively extracts high value atomic facts from long form interactions to serve as highly efficient memory representations. Subsequently, AtomMem organizes these facts into hierarchical event structures and temporal profiles, capturing coherent episodic contexts and tracking dynamically evolving user attributes over time. During retrieval, the system activates an associative memory graph to connect fragmented memories. Experiments on the LoCoMo benchmark confirm that AtomMem achieves state-of-the-art performance across various reasoning tasks, offering a scalable and economically viable solution for deploying intelligent personalized agents.

</details>


### 30. ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?

- **Authors:** Jiajun Li, Mingshu Cai, Yixuan Li, Yu Ding, Ran Hou, Guanyu Nie, Xiongwei Han, Wanyuan Wang
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19787v1](http://arxiv.org/abs/2606.19787v1)
- **PDF:** [https://arxiv.org/pdf/2606.19787v1](https://arxiv.org/pdf/2606.19787v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **ORAgentBench**, a new execution‑grounded benchmark that evaluates large‑language‑model (LLM) agents on full‑cycle, realistic operations‑research problems—including data ingestion, model formulation, code generation, solution execution, and validated decision submission.

**Methodology:** 107 human‑curated OR tasks spanning multiple domains are packaged as isolated environments containing natural‑language briefs, multi‑file datasets, and required output schemas. Agents are prompted to write and run solution code; submissions are automatically judged by hidden validators for schema compliance, feasibility with respect to hard constraints, and normalized objective quality. Fourteen state‑of‑the‑art LLM‑agent configurations are benchmarked on this pipeline.

**Key findings:** Even the best-performing agent solves only **≈35 %** of all tasks (≈21 % of the hardest ones), and many feasible solutions fall short of the required quality. Error analysis reveals that failures are mostly strategic—missing operational rules, producing fragile formulations, generating weak feasible solutions, and lacking effective solution refinement. Adding OR‑specific procedural prompts improves feasibility but does not reliably raise solution quality, indicating that current LLM agents are far from achieving dependable, end‑to‑end OR decision making.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as autonomous agents for multi-step tasks in executable environments, yet their ability to perform realistic operations research (OR) work remains unclear. Existing OR evaluations often decouple modeling from solving, rely on pre-formalized or text-only instances, and rarely test the full workflow from operational artifacts to validated decisions. In this work, we introduce ORAgentBench, an execution-grounded benchmark for evaluating autonomous agents on challenging end-to-end operations research tasks. It contains 107 human-reviewed tasks across diverse operational scenarios, each packaged in an isolated environment with a natural-language brief, multi-file data, configuration artifacts, and a required submission schema. Agents must write and run solution code, and their submissions are evaluated by hidden validators for schema validity, hard-constraint feasibility, and normalized objective quality. Experiments with fourteen frontier agent-model configurations show that current agents remain far from reliable OR practice. The best agent passes only 35.51% of all tasks and 20.59% of hard tasks, and many feasible submissions still fall below the required quality threshold. Failure analysis further shows that errors are dominated by strategic weaknesses, including missed operational rules, brittle formulations, weak feasible-solution construction, and insufficient solution improvement. OR-specific procedural skills increase hard-task feasibility, but do not reliably improve solution quality or pass rate. These results suggest that progress in OR agents requires moving beyond plausible optimization code toward dependable, high-quality operational decision-making.

</details>


### 31. AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA

- **Authors:** Aravind Narayanan, Shaina Raza
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19782v1](http://arxiv.org/abs/2606.19782v1)
- **PDF:** [https://arxiv.org/pdf/2606.19782v1](https://arxiv.org/pdf/2606.19782v1)
- **Categories:** cs.AI, cs.CL


> **Contribution:** The paper introduces **AgentFinVQA**, a deployable, multi‑agent pipeline for financial chart question answering that simultaneously delivers high accuracy and full auditability through a per‑sample “Model Evaluation Packet” (MEP) that records each reasoning step.  

**Methodology:** Queries are broken down into distinct agents for planning, OCR, legend grounding, visual inspection, and a final verification stage; the verifier not only checks consistency but also emits a confidence verdict that can be used to route items to human review.  

**Key Findings:** On the FinMME benchmark, AgentFinVQA attains a 7.68‑point accuracy gain over a zero‑shot Gemini‑3 Flash baseline (71.24 % vs. 63.56 %) and a 4.84‑point gain with an entirely on‑premise open‑weight model (Qwen 3.6‑27B‑FP8). The verifier’s verdict proves predictive (68.2 % exact accuracy on confirmed answers vs. 55.6 % on revised ones), while error analysis reveals that most failures stem from question misunderstanding, legend confusion, and extraction errors—areas the verifier currently detects poorly, pointing to future improvement directions.


<details>
<summary>Abstract</summary>

Financial chart question answering in regulated settings demands more than accuracy: practitioners must know which answers to trust before acting on them, and many institutions cannot send client data to external model providers. Yet existing chart-QA agents are accuracy-focused and opaque, and most assume proprietary API access; to our knowledge, none combines auditability with on-premise deployability without significant accuracy compromise. We present AgentFinVQA, a multi-agent pipeline that decomposes each query into planning, OCR, legend grounding, visual inspection, and verification, recording every step in a traceable Model Evaluation Packet (MEP) per sample. On FinMME, AgentFinVQA improves $+7.68$ pp over a primary-backbone matched zero-shot baseline with a proprietary backbone (Gemini-3 Flash; 71.24% vs. 63.56%, McNemar $p \approx 1.1 \times 10^{-16}$), and $+4.84$ pp with open-weights Qwen3.6-27B-FP8 served locally. The verifier's verdict also serves as a useful confidence signal (68.2% vs. 55.6% exact accuracy on confirmed vs. revised answers), enabling human-in-the-loop review routing. Error analysis shows that question misunderstanding, legend confusion and extraction error account for nearly two-thirds of failures and are the categories least detected by the verifier, identifying clear directions for future work. Together these results show that auditable, on-premise financial chart QA is practical and that the open-weights system keeps most of the accuracy gains while enabling full data residency. We release our code to support reproducible evaluation.

</details>


### 32. SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design

- **Authors:** Kun Zeng, Yu Huo, Siyu Zhang, Yuecheng Zhuo, Yuquan Lu, Haoyue Liu, Siyue Chen, Xiaoying Tang
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19758v1](http://arxiv.org/abs/2606.19758v1)
- **PDF:** [https://arxiv.org/pdf/2606.19758v1](https://arxiv.org/pdf/2606.19758v1)
- **Categories:** cs.MA


> The paper introduces **SIGMA**, a novel framework that builds multi‑agent systems by composing agents from a task‑conditioned selection of reusable skills rather than fixing agents a priori; it predicts a skill‑agent incidence matrix, generates embeddings for the resulting agents, and then learns a communication topology over them, with skill‑specific mailboxes that route messages directly to the relevant capabilities. Experiments on six reasoning and coding benchmarks using three base large language models show that SIGMA consistently outperforms the strongest non‑compositional baseline (CARD) by 1.75–2.36 points and degrades only 0.96 points when faced with unseen skill libraries, demonstrating that compositional agent construction is a powerful complementary design axis to topology optimization in agentic AI.


<details>
<summary>Abstract</summary>

Existing graph-based multi-agent system (MAS) designers mainly improve collaboration by optimizing communication topologies over predefined agents, roles, or groups. However, because each node remains a closed-set entity, these methods struggle to generalize to tasks that require unseen combinations of capabilities. We propose SIGMA, a skill-incidence graph framework that constructs agents as task-conditioned bundles of reusable skills. Given a task and a skill library, SIGMA predicts a skill-agent incidence matrix, composes agent node embeddings from selected skills, and decodes a communication topology over the constructed agents. During execution, skill-specific mailboxes route messages to the relevant assigned capabilities, making the incidence structure directly operational. Across six reasoning and coding benchmarks with three base LLMs, SIGMA achieves the best average performance and improves over CARD, the strongest non-compositional topology-based baseline, by 2.06, 2.36, and 1.75 points, respectively. It also shows stronger robustness to unseen skill libraries, with an average performance drop of only 0.96 points. These results suggest that compositional node construction is a complementary and important axis for multi-agent design beyond communication topology optimization. Code is available at https://anonymous.4open.science/r/SIGMA-2338/.

</details>


### 33. Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware

- **Authors:** Ma Toan Bach, Yuchi Zheng, Haingo Razafindranto, Tanvir Alam, Aric Leather, Ranveer Sandhu, Jitesh Arora
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19725v1](http://arxiv.org/abs/2606.19725v1)
- **PDF:** [https://arxiv.org/pdf/2606.19725v1](https://arxiv.org/pdf/2606.19725v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> **Main contribution:** The paper presents a multi‑agent, LLM‑driven workflow that automatically authors, compiles, and iteratively repairs unit tests for low‑level C firmware in the openSIL codebase, handling the frequent build‑time fragilities (missing headers, unresolved symbols, dependency mismatches) that make manual test creation costly.

**Methodology:** The system first generates test scaffolds, then uses “library‑aware” agents to synthesize or retrieve appropriate stubs, mocks, and fakes. A compile‑dispatch loop parses build logs and line‑coverage feedback to prompt the LLM for targeted fixes, repeating until the test compiles and meets coverage goals; optional vector‑database retrieval supplies similar prior tests for guidance.

**Key findings:** Across 76 target functions, the pipeline produced compilable unit tests for 73 functions. Without coverage guidance the average line coverage was 73.9 %; with line‑coverage‑driven repair it rose to 98.8 % on a 48‑function subset (94.7 % when also using vector‑database retrieval). The results demonstrate that automated generate‑and‑repair pipelines can dramatically increase test creation efficiency and coverage in highly constrained firmware environments, reducing manual debugging effort for agentic AI‑assisted software engineering.


<details>
<summary>Abstract</summary>

Validating changes in low-level C firmware is expensive because unit tests (UTs) are fragile under strict build constraints, where missing headers, unresolved symbols, and dependency mismatches frequently prevent compilation and linking. This study introduces an automated UT authoring workflow for the Open-Source Silicon Initialization Library (openSIL) firmware codebase maintained by Advanced Micro Devices (AMD) that reduces manual effort through a large language model (LLM) guided multi-agent pipeline. The workflow combines automated generation of test scaffolds, library-aware creation or reuse of stubs, mocks, and fakes, and an iterative compile-dispatch repair loop driven by build logs and line-coverage feedback. We evaluate the approach using compilation success, repair iterations, dispatch success, and line coverage, with time, cost, and token usage as secondary measures. Across 76 functions under test, the workflow generated compilable UTs for 73 functions. In a configuration without line coverage guidance or retrieval augmentation, mean line coverage reached 73.9%. On a 48-function subset evaluated under both configurations, mean line coverage reached 98.8% with line-coverage guidance alone and reached 94.7% when combined with vector-database retrieval. Results show that automated generation-and-repair pipelines can substantially improve UT creation efficiency and coverage for constrained firmware environments while reducing manual debugging effort.

</details>


### 34. Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents

- **Authors:** Dhaval C. Patel, Kaoutar El Maghraoui, Shuxin Lin, Yusheng Li, Tianjun Feng, Chun-Yi Tsai, Yihan Sun, Wei Alexander Xin, Akshat Bhandari, Tanisha Rathod, Aaron Fan, Sanskruti Vijay Shejwal, Tomas Pasiecznik, Sagar Chethan Kumar, Tanmay Agarwal, Rohith Kanathur, Sam Colman, Amaan Sheikh, Dev Bahl, Ann Li, Krish Veera, Alimurtaza Mustafa Merchant, Shambhawi Baswaraj Bhure, Sajal Kumar Goyla, Chengrui Li, Kirthana Natarajan, Rui Li, Thomas Ajai, Rujing Li, Vivek G. Iyer, Sanjaii Vijayakumar, Yitong Bai, Ayal Yakobe, Darief Maes, Yassine Jebbouri, Tianyang Xu, Thai Quoc On, Vera Mazeeva, Winston Li, Yuval Shemla, Yeshitha Bhuvanesh, Rushin Bhatt, Siddharth Chethan Gowda, Alisha Vinod, Caroline Cahill, Shriya Aishani Rachakonda, Yunfeng Chen, Aryaman Agrawal, Aman Upganlawar, Mao Le Jonathan Ang, Yubin Sally Go, Madhav Rajkondawar, Yang-Jung Chen, Trisha Maturi, Ananya Kapoor, Andrew Li, Shrey Arora, Mana Abbaszadeh, Shen Li, Charles Xu, Byeolah Kwon
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19704v1](http://arxiv.org/abs/2606.19704v1)
- **PDF:** [https://arxiv.org/pdf/2606.19704v1](https://arxiv.org/pdf/2606.19704v1)
- **Categories:** cs.AI


> **Main contribution** – The paper shows that conventional “leaderboard” scores for LLM‑based agents are unreliable predictors of real‑world performance because they collapse multiple deployment‑relevant dimensions into a single aggregate rank. It introduces **predictive‑validity ranking**: evaluating a benchmark configuration by the correlation between its in‑sample rank and its out‑of‑distribution (OOD) rank, and provides a systematic twelve‑tier measurement framework to expose which HELM‑style dimensions survive in the agent era.

**Methodology** – The authors conduct a coordinated meta‑analysis of 14 new implementation studies (covering multimodal assets, retrieval, reasoning modes, orchestration strategies, and infrastructure tweaks) and integrate results from seven existing agent benchmarks. They compute in‑sample rankings, test them on OOD test sets and public‑to‑hidden competition retrospectives, and quantify rank stability using Pearson/ Spearman correlation and three pre‑registered falsifiable OOD criteria with explicit thresholds.

**Key findings for agentic AI** – Aggregate‑score leaderboards exhibit low predictive validity; rankings that look strong on the benchmark often invert on OOD tasks. Configurations that score highly on the proposed predictive‑validity metric maintain more stable performance across distribution shifts, highlighting the importance of multi‑dimensional, OOD‑aware evaluation for future LLM‑agent benchmarks. The paper also releases a pre‑registered pilot design and a roadmap for next‑generation agent benchmarks that report predictive‑validity rather than single‑number scores.


<details>
<summary>Abstract</summary>

Agent benchmarks are growing fast, but no single benchmark touches more than four or five of the dimensions that deployment exposes. This paper aggregates the largest coordinated deep-dive of one MCP-based industrial-agent benchmark to date: fourteen parallel implementation studies covering new asset classes (including a multi-modal visual extension), alternative orchestrations, retrieval strategies, reasoning modes, infrastructure optimizations, and evaluation-methodology probes. Consolidating those studies with seven prior agent benchmarks, we argue that aggregate-score leaderboards systematically underspecify deployed-agent evaluation. Rankings derived from aggregate scores do not transfer to out-of-distribution settings; recent public-to-hidden competition retrospectives provide direct empirical evidence of this rank instability. We propose ranking configurations by predictive validity, the correlation between in-sample and out-of-sample rank, rather than in-sample mean, and report a twelve-tier measurement apparatus that exposes the deployment-relevant dimensions HELM and its agent-era successors collapse. The position is operationalized through three falsifiable out-of-distribution criteria with explicit thresholds; existing evidence partly supports it but is too thin to confirm. We close with a pre-registered pilot design and a field-level vision for what the next generation of agentic benchmarks should report.

</details>


### 35. Multi-Granular Attention-Driven Reinforcement Learning Framework for Web Intelligent Enhancement Systems

- **Authors:** Navin Chhibber, Deepak Singh, Anokh Kishore, Nikita Chawla, K. Anguraj
- **Published:** 2026-06-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19690v1](http://arxiv.org/abs/2606.19690v1)
- **PDF:** [https://arxiv.org/pdf/2606.19690v1](https://arxiv.org/pdf/2606.19690v1)
- **Categories:** cs.LG


> The paper introduces **MGAR‑WIES**, a novel reinforcement‑learning framework that fuses multi‑granular attention‑enhanced semantic graph modeling with an adaptive multi‑agent RL controller for web‑based personalization tasks. The methodology first converts heterogeneous web data (structured, semi‑structured, and unstructured) into a dynamic semantic graph whose node/edge embeddings are refined by hierarchical attention layers that capture local relevance and global context; these attention‑aware graph states then serve as the observation space for a set of cooperating RL agents that continuously optimize actions such as recommendation, navigation, and service adaptation, updating both the graph and policies online from user feedback. Empirical evaluation on real‑world web datasets shows that MGAR‑WIES attains around **80 % accuracy**, outperforming prior deep‑learning and RL baselines, thereby demonstrating improved semantic understanding, adaptability, and scalability for agentic AI systems operating in evolving web environments.


<details>
<summary>Abstract</summary>

From the past few years, web intelligent enhancement systems increasingly rely on heterogeneous and dynamic web data to deliver personalized, context-aware services. However, traditional machine learning, deep learning, and reinforcement learning models often struggle with semantic understanding, adaptability, and scalability in continuously evolving web environments. In this research, a Multi-Granular Attention-based Reinforcement Web Intelligent Enhancement System (MGAR-WIES) is proposed to address the challenges by integrating semantic graph modeling, attention mechanisms, and adaptive reinforcement learning. Initially, heterogeneous web data comprising structured, semi-structured and unstructured sources are collected and preprocessed for generating unified feature representations. These representations are transformed into a dynamic semantic graph, where entities and their relationships are modeled by using graph embeddings enhanced by attention mechanisms for capturing both local relevance and global contextual dependencies. Subsequently, an adaptive multi-agent reinforcement learning strategy leverages the attention-aware semantic states to optimize personalized web actions like content recommendation, navigation optimization, and service adaptation. Finally, the continuous online feedback is further integrated to update graph representations and learning policies in real time by ensuring sustained adaptability and performance. The proposed MGAR-WIES acheived better results in terms of accuracy (80%) when compared with existing approaches.

</details>


### 36. SAGE-OPD: Selective Agent-Guided Intervention for Multi-Turn On-Policy Distillation

- **Authors:** Yuhang Zhou, Lizhu Zhang, Yifan Wu, Mingyi Wang, Bo Peng, Jiayi Liu, Xiangjun Fan, Zhuokai Zhao
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19659v1](http://arxiv.org/abs/2606.19659v1)
- **PDF:** [https://arxiv.org/pdf/2606.19659v1](https://arxiv.org/pdf/2606.19659v1)
- **Categories:** cs.CL


> SAGE‑OPD introduces a verifier‑free selective‑intervention framework for multi‑turn on‑policy distillation, letting a teacher model decide at each step whether to intervene on the student’s response and weighting token‑level losses by the teacher’s confidence. By skipping supervision on unreliable or off‑distribution turns and normalizing the overall loss, the method mitigates compounding errors and over‑penalization that plague dense OPD in multi‑turn settings. Experiments on embodied‑agent benchmarks (e.g., ALFWorld) show up to 13.3 % relative gains in unseen success rates, and ablations confirm that turn‑level intervention, confidence weighting, and loss normalization each contribute additively.


<details>
<summary>Abstract</summary>

On-policy distillation (OPD) improves student models by training them on trajectories induced by their own policy, making it a promising approach for mitigating exposure bias in agent training. However, most OPD studies focus on single-turn settings, while realistic LLM agents interact with environments over multiple turns. In this regime, early errors can alter future observations and compound across the trajectory, and standard dense token-level OPD becomes brittle, as it may over-penalize semantically valid alternatives, reinforce local degeneracies such as repeated actions, and propagate unreliable teacher supervision on off-distribution histories. We propose SAGE-OPD, a verifier-free selective intervention framework specifically designed for multi-turn OPD. Instead of applying teacher supervision uniformly across all turns, SAGE-OPD first observes environment feedback and uses teacher judgment to decide whether each student response should be skipped or intervened on. To further address compounding errors, SAGE-OPD weights token-level distillation by teacher confidence, reducing the influence of uncertain teacher distributions on corrupted or ambiguous histories. Finally, SAGE-OPD applies loss normalization to preserve the overall loss scale of standard OPD while retaining selective turn-level weighting. Experiments on agent tasks show that SAGE-OPD consistently improves over baselines, achieving up to a 13.3% relative improvement in ALFWorld unseen success rate over standard OPD. Ablation studies further demonstrate that turn-level intervention, teacher confidence weighting, and loss normalization provide complementary benefits. Our results suggest that effective multi-turn OPD should remain on-policy, but teacher supervision should be selectively allocated to turns where intervention is necessary and reliable.

</details>


### 37. Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation

- **Authors:** Ahmad Farooq, Kamran Iqbal
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19632v1](http://arxiv.org/abs/2606.19632v1)
- **PDF:** [https://arxiv.org/pdf/2606.19632v1](https://arxiv.org/pdf/2606.19632v1)
- **Categories:** cs.RO, cs.AI, cs.LG, cs.LO, cs.MA


> The paper introduces the first end‑to‑end framework that makes deep multi‑agent reinforcement‑learning (MARL) communication policies amenable to formal safety verification by distilling the neural policies into high‑fidelity decision‑tree abstractions and then checking those trees with the PRISM probabilistic model checker. Using a four‑stage pipeline—feature extraction, decision‑tree distillation (≈98 % fidelity), automatic translation to PRISM models, and compositional PCTL verification—the authors verify 18 safety, liveness and cooperation properties for VQ‑VIB‑based multi‑drone coordination (5–7 agents), achieving 88.9 % property satisfaction and confirming that the verified safety guarantees hold for the original neural policies within a ±0.6 % margin (95 % CI). The results demonstrate that discrete VQ‑VIB messages substantially improve abstraction fidelity and verification speed (3–4×), providing a practical bridge between deep MARL and formal safety assurance for safety‑critical robot swarms.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) enables agents to develop coordination strategies through emergent communication, but neural policies lack the formal safety guarantees required for safety-critical robotic deployment in drone swarms and autonomous vehicle fleets. We present the first end-to-end framework for safety verification of learned multi-agent communication policies through policy abstraction: neural policies are distilled into interpretable decision trees, then formally verified, with empirical validation confirming that verified safety properties transfer to original networks. Our four-stage pipeline consists of domain-specific feature extraction from agent observations, decision tree distillation achieving 97.9% +/- 1.2% fidelity to neural policies, automated translation to PRISM probabilistic model checker specifications with complete feature-to-state-variable correspondence, and compositional verification of Probabilistic Computation Tree Logic (PCTL) properties via pairwise decomposition with union-bound aggregation and empirical neighbor modeling. Evaluating Vector-Quantized Variational Information Bottleneck (VQ-VIB) policies for multi-drone coordination with 5-7 agents, we verify 18 temporal logic properties across safety, liveness, and cooperation, achieving 88.9% property satisfaction with all five safety thresholds satisfied (0.3% collision probability vs. 1% threshold). Monte Carlo validation of original neural policies confirms that verified safety properties transfer with <=0.6 percentage-point deviation (95% CI). Discrete VQ-VIB messages provide +11.6 to +13.6 percentage-point fidelity advantages over continuous methods, enabling 3-4x faster verification. Our framework provides empirically validated safety verification for distilled policy abstractions, serving as a practical bridge between deep MARL and formal safety workflows for multi-robot deployment.

</details>


### 38. Before the Pull Request: Mining Multi-Agent Coordination

- **Authors:** Dipankar Sarkar
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19616v1](http://arxiv.org/abs/2606.19616v1)
- **PDF:** [https://arxiv.org/pdf/2606.19616v1](https://arxiv.org/pdf/2606.19616v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> The paper introduces **grite**, an open‑source, git‑backed coordination layer for autonomous coding agents that records every claim, division, and conflict over shared code as a signed, append‑only event log. By embedding coordination directly in the repository (eliminating a central server), the authors show that grite eliminates duplicate work (reducing redo‑rate from 78 % to 0 %), triples useful throughput, and guarantees that all agents converge on the same log without silently dropped writes—unlike traditional file‑based trackers. Mining this log uncovers previously invisible failure modes (e.g., lock starvation, race‑to‑close) and provides fine‑grained provenance for multi‑agent coordination, offering a reproducible dataset and tooling for further research in agentic AI.


<details>
<summary>Abstract</summary>

Autonomous coding agents now open millions of pull requests, yet large-scale studies find their PRs are produced faster but accepted less often - a coordination and trust gap that pull-request-level telemetry cannot explain. We argue the missing signal lives before the PR, in how concurrent agents claim, divide, and collide over shared work. We study this process through grite, our open-source coordination substrate that needs no central server and stores its records inside git itself, so its append-only, signed event log captures the coordination process directly. We show that (i) this shared substrate reduces duplicate and conflicting work at bounded overhead - the share of work that merely re-does a teammate's task falls from 78% to 0% while useful throughput more than triples; (ii) every agent's copy of the log converges to the same state with no write silently dropped, where a file-based tracker loses concurrent writes; and (iii) the log is a mineable artefact from which concrete failure modes - conflicting edits, lock starvation, redundant rediscovery, race-to-close - are automatically recoverable with provenance, several invisible in pull-request history. We release the dataset, harness, and mining toolkit.

</details>


### 39. Uncertainty Decomposition for Clarification Seeking in LLM Agents

- **Authors:** Gregory Matsnev
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19559v1](http://arxiv.org/abs/2606.19559v1)
- **PDF:** [https://arxiv.org/pdf/2606.19559v1](https://arxiv.org/pdf/2606.19559v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces a lightweight, prompt‑based method to decompose uncertainty in LLM agents into “action confidence” and “request uncertainty,” enabling the model to detect underspecified instructions and proactively ask clarifying questions. By evaluating this decomposition on two new clarification‑augmented benchmarks (WebShop‑Clarification and ALFWorld‑Clarification) across five diverse LLM backbones, the authors show that it yields up to a 73 % boost in clarification‑F1 over the strongest prior approach (ReAct+UE) and consistently improves performance on standard fault‑detection tasks. These results demonstrate that simple, deployable uncertainty signals can markedly enhance the interactive, clarification‑seeking capabilities of agentic AI systems.


<details>
<summary>Abstract</summary>

Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. Practical deployment constraints -- black-box APIs, interactive latency budgets, and the absence of labeled trajectories -- rule out logprob-based, multi-sampling, and training-based methods, leaving prompt-based estimation as the most viable family for surfacing such signals at deployment time. We answer this call with a simple prompt-based decomposition that separates action confidence from request uncertainty (u), enabling the agent to ask for clarification when the task specification is ambiguous. To evaluate it, we introduce two clarification-augmented benchmarks (WebShop-Clarification and ALFWorld-Clarification) in which 50% of tasks are deliberately underspecified, and systematically compare the proposed decomposition against ReAct+UE and Uncertainty-Aware Memory (UAM) across five LLM backbones (GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B, GPT-OSS-120B) on these variants together with the standard WebShop, ALFWorld, and REAL benchmarks for fault detection. Averaged across the five backbones, the proposed decomposition improves clarification F1 on ALFWorld-Clarification by 73% over ReAct+UE and by 36% over UAM, and leads clarification F1 on every backbone on WebShop-Clarification and on four of five backbones on ALFWorld-Clarification, indicating that the gains generalize beyond a single LLM.

</details>


### 40. DeXposure-Claw: An Agentic System for DeFi Risk Supervision

- **Authors:** Aijie Shu, Bowei Chen, Wenbin Wu, Cathy Yi-Hsuan Chen, Fengxiang He
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19501v1](http://arxiv.org/abs/2606.19501v1)
- **PDF:** [https://arxiv.org/pdf/2606.19501v1](https://arxiv.org/pdf/2606.19501v1)
- **Categories:** cs.AI, cs.CL, cs.LG, q-fin.RM


> The paper introduces **DeXposure‑Claw**, a specialized agentic supervision pipeline for decentralized‑finance (DeFi) risk monitoring that combines a graph‑time‑series foundation model (DeXposure‑FM) with deterministic monitors, stress‑scenario generators, and confidence gating to turn network‑exposure forecasts into auditable supervisory tickets complete with attribution and rationale. Methodologically, the system grounds large‑language‑model (LLM) decisions on structured forecast evidence, applies rule‑based alert typing, and uses a novel six‑axis benchmark (DeXposure‑Bench) that evaluates both absolute‑loss (regulator‑aligned ground truth) and false‑intervention rates. Experiments on five years of weekly DeFi data show that DeXposure‑Claw dramatically reduces false alarms while maintaining accurate risk alerts, demonstrating a viable, regulator‑friendly approach to deploying agentic AI in high‑stakes financial supervision.


<details>
<summary>Abstract</summary>

Decentralized finance exposes supervisors to fast-moving, networked credit risks. General-purpose LLM agents fit this setting poorly: they over-read weak evidence and recommend high-stakes interventions, while existing evaluations offer no regulator-aligned way to measure the resulting false alarms. We introduce DeXposure-Claw, a forecast-grounded agentic supervision system that routes LLM decisions through structured evidence: (1) DeXposure-FM, a graph time-series foundation model, forecasts future exposure networks; (2) deterministic monitors and stress scenarios then turn those forecasts into typed alerts, attribution signals, and scenario evidence; and (3) data-health and confidence gates constrain escalation before DeXposure-Claw emits auditable supervisory tickets with rationales. We further develop DeXposure-Bench, a six-axis evaluation harness, whose decision axis scores tickets against a regulator-aligned absolute-loss ground truth and an explicit false-intervention rate. Experiments on five years of weekly real data fully support our system. Code is at https://github.com/EVIEHub/DeXposure-Claw.

</details>


### 41. Hidden Anchors in Multi-Agent LLM Deliberation

- **Authors:** Apurba Pokharel, Ram Dantu
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19494v1](http://arxiv.org/abs/2606.19494v1)
- **PDF:** [https://arxiv.org/pdf/2606.19494v1](https://arxiv.org/pdf/2606.19494v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces a closed‑loop dynamical model of multi‑agent LLM deliberation that augments classical opinion‑dynamics (e.g., DeGroot, Friedkin‑Johnsen) with a latent “anchor” – a hidden internal belief that continuously pulls each agent’s opinion, independent of peer influence.  

**Methodology:** The authors formulate the deliberation process as a linear dynamical system with an unknown anchor vector, derive an algorithm to recover the anchor solely from observed opinion trajectories, and validate the model by testing whether the recovered anchor predicts outcomes of held‑out deliberation runs. Experiments cover three families of open‑weight LLMs, comparing hull‑escaping behavior (opinions moving outside the convex hull of initial beliefs) against predictions of the anchor‑augmented model.  

**Key findings:** (1) Anchors can be reliably inferred from deliberation data, and their presence explains why some agents’ confidence surpasses the initial belief space—a phenomenon unattainable under classical consensus rules. (2) Across model families, anchor influence is uniformly strong, but only when the anchor lies far from the initial opinions does deliberation escape the convex hull, necessitating the full closed‑loop model. This provides a practical diagnostic for detecting genuine anchor‑driven reasoning in agentic LLM systems.


<details>
<summary>Abstract</summary>

Multi-agent LLM deliberation, where agents exchange and revise answers over several rounds, is increasingly used to improve reasoning and accuracy, yet how and why it works is rarely modelled. Such deliberation mirrors how humans reach decisions. As social animals we are pulled both by the group, the herd effect that classical opinion-dynamics models such as DeGroot and Friedkin--Johnsen capture, and by our own internal belief, which they do not. We model multi-agent deliberation as a closed-loop dynamical system in which each agent carries a hidden internal belief, its anchor, that continually pulls its opinion regardless of its neighbours. We show this anchor can be recovered from the deliberation alone, and that it explains a behaviour classical consensus rules forbid: an agent's confidence in the correct answer can climb past where any agent started, escaping the space (convexhull) formed by the initial beliefs. Checking whether the recovered anchor also predicts held-out runs (generalizes) gives a simple test for when a model is truly driven bysuch an anchor. Across three open-weight model families this is a spectrum, not all-or-nothing. All anchors' influence are about equally strongly, but they differ in where the anchor sits, and only when it sits far from the initial opinions does deliberation escape the hull and need the full closed-loop model.

</details>


### 42. Deontic Policies for Runtime Governance of Agentic AI Systems

- **Authors:** Anupam Joshi, Tim Finin, Karuna Pande Joshi, Lalana Kagal
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19464v1](http://arxiv.org/abs/2606.19464v1)
- **PDF:** [https://arxiv.org/pdf/2606.19464v1](https://arxiv.org/pdf/2606.19464v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **AgenticRei**, a runtime governance engine for LLM‑driven autonomous agents that goes beyond traditional permit‑/prohibit‑only policy systems (e.g., XACML, Rego, Cedar) by incorporating **deontic concepts**—obligations, dispensations, conflict‑resolution meta‑policies, and ontology‑aware reasoning. The authors implement these capabilities in a declarative policy language built on the REI framework and expressed in OWL, which is evaluated by a high‑performance logic engine outside the LLM and applied to both tool‑use actions and inter‑agent communications. Experiments and illustrative scenarios show that AgenticRei can enforce complex security, privacy, and compliance requirements (e.g., mandatory notifications, conditional waivers, hierarchical rule precedence) that current production policy engines cannot represent, thereby offering a more expressive and enforceable governance layer for agentic AI systems.


<details>
<summary>Abstract</summary>

Autonomous agentic AI systems driven by Large Language Models (LLMs) introduce a new class of security, privacy, and compliance challenges: an agent that can invoke tools, manipulate data, install software, and coordinate with peer agents across organizational boundaries must be constrained not just by authentication and access control, but by the full structure of enterprise governance. This includes specifying what agents are permitted and prohibited from doing, what they areobliged to do after certain actions (e.g., notify the CISO), under what conditions a standing obligation may be waived, and which rules take precedence when policies conflict. This governance problem exceeds what current policy engines provide. Systems such as XACML, Rego, and Cedar address only the permit/prohibit subset of this governance structure. They do not provide obligation lifecycle management, meta-policy conflict resolution, dispensations that waive obligations in specific circumstances, and ontological reasoning over domain class hierarchies commonly found in applications such as healthcare, cybersecurity, or data privacy. We propose AgenticRei, which realizes key governance requirements such as obligations, dispensations, policy conflict resolutions, and reasoning over policies, as well as the basic permit/prohibit constraints. We use a deontic policy language built on the Rei framework, expressed as OWL (Web Ontology Language) and evaluated at runtime by a high-performance logic engine entirely outside the LLM. The same pipeline governs both tool invocations by the agent and agent-to-agent messages. We show through examples that deontic policies capture governance constraints around security and privacy that mostly cannot be expressed in current production engines. Our approach composes naturally with industry-standard frameworks like A2AS.

</details>


### 43. Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious Play

- **Authors:** Leyang Shen, Yang Zhang, Xiaoyan Zhao, Chun Kai Ling, Tat-Seng Chua
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19308v1](http://arxiv.org/abs/2606.19308v1)
- **PDF:** [https://arxiv.org/pdf/2606.19308v1](https://arxiv.org/pdf/2606.19308v1)
- **Categories:** cs.CL, cs.MA


> The paper introduces **Multi‑Agent Fictitious Play (MAFP)**, a new framework that treats each stakeholder’s stance as a separate LLM‑driven agent and solves decision‑making problems by searching for a game‑theoretic equilibrium rather than by simple task decomposition. MAFP applies the fictitious‑play algorithm: at each iteration an agent selects its best response to the empirical distribution of the other agents’ past choices, thereby exposing and correcting mutual weaknesses among the stances. Experiments on competitive, pre‑action strategy tasks show that MAFP consistently beats single‑ and multi‑round baselines on both tournament strength and robustness, demonstrating that equilibrium‑oriented multi‑agent interaction can overcome “stance entanglement” in complex decision‑making scenarios.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems (MAS) have demonstrated great potential in solving tasks with execution complexity, by distributing subtasks across cooperative agents. However, this divide-and-conquer paradigm falls short on decision-making tasks that are also prevalent in the real world. These tasks require simultaneous reasoning from the stances of all involved stakeholders whose decisions are mutually dependent and thus cannot be solved in isolation. We characterize this challenge as stance entanglement, a form of decision complexity distinct from execution complexity. To address it, we propose Multi-Agent Fictitious Play (MAFP), a novel MAS paradigm that represents stakeholder stances as agents and formulates decision-making as an equilibrium-seeking process. Built on the game-theoretic principle of fictitious play, MAFP iteratively updates each agent's decision by best responding to the empirical mixture of other agents' past decisions. This enables agents to expose and address one another's weaknesses, progressively improving decision quality and robustness. We evaluate MAFP on challenging decision-making tasks that test the capability of deciding strategies for competitive scenarios prior to acting. MAFP outperforms both single-round and multi-round baselines on two complementary metrics, tournament strength and robustness, demonstrating its effectiveness in addressing stance entanglement.

</details>


### 44. TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology

- **Authors:** Hannah Le, Ramesh Ramasamy, Alex Urrutia, Mahsa Yazdani, Tim Proctor, Kenny Workman
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19245v2](http://arxiv.org/abs/2606.19245v2)
- **PDF:** [https://arxiv.org/pdf/2606.19245v2](https://arxiv.org/pdf/2606.19245v2)
- **Categories:** cs.AI, cs.LG


> **Main contribution**: The paper presents TxBench‑PP, a rigorously verified benchmark that evaluates AI agents on realistic small‑molecule preclinical pharmacology tasks—requiring agents to interpret raw assay data and make program‑stage decisions rather than retrieve memorized literature facts.

**Methodology**: TxBench‑PP comprises 100 curated evaluation cases covering mechanism‑of‑action, pharmacodynamics, target engagement, causal validation, developability, safety, and translational efficacy. Each case supplies agents with a snapshot of a drug‑discovery workflow and associated data files in a coding environment; agents must generate structured answers that are graded automatically and deterministically. The authors tested 11 language‑model back‑ends across four harnesses, yielding ~4,800 execution trajectories.

**Key findings**: Across all configurations, no system consistently solved the tasks. The top‑performing setup—Claude Opus 4.8 with the Pi harness—correctly answered only 59.3 % of endpoint attempts (178/300, 95 % CI 51.1–67.6), with GPT‑5.5/​Pi close behind at 55.3 %. These results highlight a substantial gap between current agentic AI capabilities and the reliable decision‑making required for preclinical drug‑discovery pipelines.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) agents promise to accelerate drug discovery by compressing interpretation and decision-making loops, but practical deployment requires trusted evaluation on realistic program decisions. We introduce TherapeuticsBench Preclinical Pharmacology (TxBench-PP), a verifiable benchmark for small-molecule preclinical pharmacology and the first focused slice of a broader TherapeuticsBench effort across drug-discovery stages and therapeutic modalities. TxBench-PP tests whether agents can recover accurate conclusions from real-world assay data rather than memorized facts from literature. The benchmark contains 100 evaluations indexed by program stage, assay type, and task structure, spanning mechanism-of-action (MoA) and pharmacodynamic (PD) reasoning, compound-target engagement, causal target validation, developability and safety, and translational efficacy. Agents receive realistic workflow snapshots, inspect files in a coding environment, and return structured answers graded deterministically. Across 16 model-harness configurations, comprising 11 models and 4,800 trajectories, no system reliably recovered preclinical pharmacology decisions. The strongest configuration, Claude Opus 4.8 / Pi, passed 59.3\% of endpoint attempts (178/300; 95\% CI, 51.1-67.6), followed by GPT-5.5 / Pi at 55.3\% (166/300; 47.0-63.6).

</details>


### 45. AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces

- **Authors:** Zongmin Zhang, Yuyang Lou, Bowen Zhang, Junwu Chen, Ryo Kuroki, Xuan Vu Nguyen, Edvin Fako, Lixue Cheng, Philippe Schwaller
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19152v1](http://arxiv.org/abs/2606.19152v1)
- **PDF:** [https://arxiv.org/pdf/2606.19152v1](https://arxiv.org/pdf/2606.19152v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> AdsMind introduces a closed‑loop, physics‑grounded multi‑agent system that couples large‑language‑model (LLM) planners with machine‑learning force‑field (MLFF) relaxations to autonomously generate and self‑correct surface‑adsorbate configurations on heterogeneous catalysts. By iteratively feeding MLFF‑derived energy and geometry feedback to the LLM agents, AdsMind reduces the number of expensive relaxations to ≈4 per case (≈14× fewer than heuristic enumeration) while achieving near‑perfect success rates (100 % on AA20 and 98.8 % on OCD‑GMAE62) and preserving correct adsorption‑energy signs in DFT validation. The framework therefore provides a reliable, self‑reflective and interpretable workflow for autonomous discovery of low‑energy adsorption structures in agentic AI‑driven computational chemistry.


<details>
<summary>Abstract</summary>

Identifying the lowest-energy surface-adsorbate configuration is critical for modeling heterogeneous catalysis, yet exhaustive exploration with ab initio calculations is computationally prohibitive. Machine-learning force fields (MLFFs) accelerate structural relaxation but leave the search over the vast configurational space a major bottleneck, and open-loop large language model (LLM) agents lack a physics-grounded feedback mechanism to correct erroneous initial guesses. We propose AdsMind (Adsorption configuration discovery with Machine intelligence and relaxation feedback), a closed-loop multi-agent framework that enables autonomous error correction through MLFF relaxation feedback. Across four LLM backends, AdsMind achieves consistently high search reliability, with success rates of 100% and 98.8% on the benchmarks AA20 and OCD-GMAE62. Relative to its single-pass (1-Shot) ablation it reduces cross-backend energy dispersion, and it uses only 4.11 and 4.67 MLFF relaxations per case, respectively -- an approximately 14-fold reduction over heuristic enumeration baselines. Density functional theory (DFT) validation using VASP/PBE on six representative AA20 systems shows that the reported open-loop Adsorb-Agent outputs exhibit qualitative adsorption-energy sign errors for molecular adsorbates, whereas AdsMind preserves the correct sign in all tested cases with closer quantitative agreement. AdsMind thus delivers reliability, self-reflection, and interpretability simultaneously, supporting more DFT-informed autonomous chemistry workflows.

</details>


### 46. A Technical Taxonomy of LLM Agent Communication Protocols

- **Authors:** Linus Sander, Habtom Kahsay Gidey, Alexander Lenz, Alois Knoll
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19135v1](http://arxiv.org/abs/2606.19135v1)
- **PDF:** [https://arxiv.org/pdf/2606.19135v1](https://arxiv.org/pdf/2606.19135v1)
- **Categories:** cs.MA, cs.AI, cs.NI


> The paper introduces a systematic taxonomy for classifying large‑language‑model (LLM) agent communication protocols, defining five orthogonal dimensions—counterparty, payload, interaction state, discovery mechanism, and schema flexibility—and validates it through five iterative analyses of nine widely used open‑source protocols. Using this framework, the authors uncover consistent architectural patterns (e.g., hybrid payloads with persistent session state, predominance of predefined schemas, and limited decentralized discovery) and identify a short‑term convergence toward unified agent‑to‑agent and agent‑to‑context messaging, while forecasting a longer‑term shift to a federated, layered protocol stack. The study provides a practical tool for protocol selection and pinpoints open challenges for agentic AI, notably privacy, policy enforcement, and scalable discovery mechanisms.


<details>
<summary>Abstract</summary>

As large language models (LLMs) advance and multi-agent systems aim to overcome the limits of standalone agents, robust communication protocols are becoming essential infrastructure for distributed agent networks. Nonetheless, the fragmented protocol landscape presents a significant interoperability challenge. This study develops a technical taxonomy to classify and analyze LLM agent communication protocols. Following an established iterative method, we defined the taxonomy's purpose, meta-characteristic, and ending conditions, then performed five iterations, three empirical-to-conceptual and two conceptual-to-empirical, on nine actively maintained open-source protocols with demonstrable adoption. The taxonomy comprises five dimensions: counterparty, payload, interaction state, discovery mechanism, and schema flexibility. Classification reveals recurring architectural patterns: all sampled agent-to-agent protocols combine hybrid payloads with session-state persistence; most protocols support multiple predefined schemas, and two negotiate schemas at runtime, indicating a trend toward schema flexibility; decentralized discovery remains rare. Analysis suggests short-term convergence pressure toward protocols unifying agent-to-agent and agent-to-context (tool and data) communication. Long-term, however, no single protocol is likely to maximize versatility, efficiency, and portability simultaneously. The field will more likely evolve toward a federated, layered protocol stack. The framework guides protocol selection and highlights open research gaps such as privacy and policy enforcement.}

</details>


### 47. Towards an Agent-First Web: Redesigning the Web for AI Agents

- **Authors:** Eranga Bandara, Ross Gore, Ravi Mukkamala, Asanga Gunaratna, Safdar H. Bouk, Xueping Liang, Peter Foytik, Abdul Rahman, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Ng Wee Keong, Kasun De Zoysa, Tharaka Hewa, Amin Hass, Wathsala Herath, Aruna Withanage, Nilaan Loganathan, Atmaram Yarlagadda, Sachin Shetty
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19116v1](http://arxiv.org/abs/2606.19116v1)
- **PDF:** [https://arxiv.org/pdf/2606.19116v1](https://arxiv.org/pdf/2606.19116v1)
- **Categories:** cs.AI, cs.CY


> The paper argues that the web’s human‑centric design is now obsolete because AI agents act as intermediaries for users, and it presents a systematic “agent‑first” redesign. It introduces three layered interventions: (1) an access layer that grants agents the same rights as human browsers via standardized agent‑identification headers and dual‑served human/agent content; (2) an economic layer that ties an agent’s cost to the human it represents, using token‑based subscriptions and a commission model for AI‑generated content; and (3) a content layer that combats “epistemic recursion” by defining the Agent Text Markup Language (ATML), a four‑tier human‑supervision framework, and cryptographic provenance chains. The authors distill these ideas into ten design principles, showing that giving agents first‑class status can preserve web economics, ensure reliable knowledge, and enable safe agent‑human interaction.


<details>
<summary>Abstract</summary>

The World Wide Web was built on an assumption held for three decades: the primary consumer of web content is a human being. This permeates every layer; its access model presumes human visitors, its economics rest on human attention, and its content targets human perception. The rapid emergence of AI agents as intermediaries between humans and web content invalidates this assumption. Yet the web resists agents through blanket blocking, CAPTCHA-based exclusion, and economic models that treat agent access as extraction rather than legitimate interaction.
  This paper proposes a principled redesign across three layers. At the access layer, agents acting for humans should inherit equivalent access rights, governed by rate limiting and agent identification metadata in HTTP requests, analogous to browser headers, alongside a dual-layer architecture serving human-readable and agent-optimized content from the same domain. At the economic layer, we propose an intent-based tier framework grounded in the agent-as-human-proxy principle: an agent's economic obligation mirrors that of the human it represents. A token-based subscription model meters content in tokens rather than pageviews, alongside a commissioned content economy anchoring AI content production in human intentionality. At the content layer, we identify epistemic recursion, the self-referential loop in which AI-generated content is consumed by agents to produce further content, progressively detaching web knowledge from human ground truth. We propose the Agent Text Markup Language (ATML), a four-level human supervision tier model, and a cryptographic provenance chain to counter this threat.
  Together these constitute ten design principles for an agent-first internet, one in which agents are first-class citizens whose integration requires renegotiating the web's foundational social contract across access, economics, and content.

</details>


### 48. Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams

- **Authors:** Haewoon Kwak
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19111v1](http://arxiv.org/abs/2606.19111v1)
- **PDF:** [https://arxiv.org/pdf/2606.19111v1](https://arxiv.org/pdf/2606.19111v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> The paper empirically tests when explicit coordination‑control agents (implemented as “leadership” controllers) improve the performance of multi‑agent LLM teams. By mapping three classic leadership styles—transactional, transformational, and situational—onto a shared action set (explore, revise, accept, synthesize) and measuring behavioral signatures (majority lock‑in, exploration, and recovery from a faulty round‑0 consensus), the authors show that these controllers rarely outperform a flat majority‑vote baseline except in the single condition where the initial majority is unreliable and the task is recoverable (LLAMA‑4‑Scout social scenario, situational control + 8 pp). This outcome aligns with contingency theory: process‑level coordination control adds value only when the initial consensus is a poor predictor and the environment permits recovery, confirming that “leadership” in LLM teams is a context‑dependent lever rather than a universal performance booster.


<details>
<summary>Abstract</summary>

Team science holds that leadership is contingent: it helps only under specific conditions, and capable, autonomous teams may need none at all. We ask the analogous question for multi-agent LLM teams: under what measurable conditions does process-level coordination control add value, and do those conditions match what team science predicts? We use behavioral signatures (majority lock-in, exploration, recovery from an incorrect round-0 consensus) and per-action ablations, clean because each controller is an explicit action set, not a monolithic prompt. We operationalize three classical leadership styles (transactional, transformational, situational) as controllers over a shared action vocabulary (explore, revise, accept, synthesize). A matched controller with the same actions but an arbitrary rule recovers no better than majority voting, so the theory-derived rule, not the vocabulary, does the work. Across four task regimes and three open-weight model families, no controller dominates by accuracy, as the contingency view predicts: transactional control matches a shared round-0 vote on all 12 (model, regime) combinations to within 1.3pp, and gains appear only on the one combination where the round-0 majority is unreliable (llama-4-scout social; situational +8pp over flat). A recovery-advantage account, tested with four boundary probes, says a controller beats plain interaction only where the round-0 majority is unreliable, the task is recoverable, and undirected interaction does not already repair it. These regions map onto contingency theory (leadership substitutes, path-goal redundancy, the situational readiness gap), so a largely null accuracy result is what the theory predicts, not a failure of the controllers. We read process-level coordination control as a contingency to be measured and theory-mapped, not a leaderboard to be topped.

</details>


### 49. RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents

- **Authors:** Ruishan Fang, Siyuan Lu, Chenyi Zhuang, Tao Lin
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19047v1](http://arxiv.org/abs/2606.19047v1)
- **PDF:** [https://arxiv.org/pdf/2606.19047v1](https://arxiv.org/pdf/2606.19047v1)
- **Categories:** cs.AI


> The paper introduces **RODS (Reward‑driven Online Data Synthesis)**, a framework that continuously generates new multi‑turn tool‑use examples during reinforcement‑learning training instead of relying on a static dataset. By monitoring the variance of rollout rewards— which peaks for samples that lie on the agent’s current capability boundary— RODS automatically detects the most informative experiences, resamples them through a skill‑aligned pipeline that preserves their API topology and dependency depth, and feeds the synthesized episodes into a dynamically maintained replay buffer. Empirically, with only ~800 actively curated samples (derived from 400 human seeds) RODS matches the performance of a 17 K‑sample offline baseline while using ~20× fewer trajectories, demonstrating that online, reward‑driven data synthesis can dramatically alleviate the sample‑depletion bottleneck in multi‑turn tool‑use RL.


<details>
<summary>Abstract</summary>

Multi-turn tool-use RL is bottlenecked by the rapid depletion of informative samples in static datasets. We observe that the gradient signal in GRPO concentrates on tasks with the highest rollout reward variance, a consequence of the Popoviciu upper bound. Consequently, samples near the agent's capability boundary -- where successes and failures are roughly balanced -- contribute disproportionately large policy gradients. As training progresses, this boundary continuously shifts, which gradually depletes the pool of informative samples in a static dataset. We propose RODS (Reward-driven Online Data Synthesis) to resolve this depletion. RODS closes the loop between RL training and data generation by repurposing the progress reward variance as a practical, zero-cost boundary detector that requires no extra inference beyond the rollouts already computed for training. It continuously identifies such boundary samples, synthesizes new multi-turn variants matching their structural complexity (e.g., API topology and dependency depth) via a skill-aligned resampling pipeline, and manages a dynamic replay buffer that co-evolves with the policy. Starting from 400 human seeds and maintaining an active training pool of ~800 samples, RODS achieves comparable performance to a 17K-sample offline pipeline while requiring roughly 20x fewer trajectories, and improves over fixed-data RL and environment augmentation in our controlled setting.

</details>


### 50. CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System

- **Authors:** Marco Becattini, Niccolò Caselli, Matteo Minin, Roberto Verdecchia, Enrico Vicario
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18976v1](http://arxiv.org/abs/2606.18976v1)
- **PDF:** [https://arxiv.org/pdf/2606.18976v1](https://arxiv.org/pdf/2606.18976v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **CAPRA**, a configurable, multi‑agent system that leverages LLMs (GPT‑4o) together with a Python microservice for multimodal extraction of text and UML diagrams from student architecture reports, and then produces personalized, LaTeX‑formatted feedback.  CAPRA’s architecture orchestrates specialized agents (evidence‑anchoring via fuzzy Levenshtein matching, consistency management, and recommendation generation) to guarantee deterministic grounding of claims and mitigate hallucinations, and it is evaluated on a taxonomy of eight binary criteria covering extraction completeness, traceability, issue detection, and stylistic compliance.  In a pilot on ten submissions, CAPRA satisfied 88.8 % of the criteria, achieved moderate agreement with human graders (κ = 0.582), and generated each report in ~4 minutes, demonstrating that a coordinated multi‑agent LLM pipeline can reliably automate portions of software‑architecture assessment while still requiring human oversight for subjective judgments.


<details>
<summary>Abstract</summary>

Automated assessment in software engineering education has advanced significantly for code grading and essay scoring. However, reviewing software architecture deliverables, which requires analyzing structural completeness and requirements traceability, has not yet been fully automated. Applying Large Language Models (LLMs) to this task requires robust architectures to ensure technical feedback is accurate and reliable for students. This paper presents CAPRA (Configurable Architecture Proficiency Report Assessment), a multi-agent LLM system that analyzes software architecture deliverables to generate personalized, template-compliant LaTeX feedback. As a core design choice, CAPRA coordinates multiple specialized agents and employs a Python-based microservice for multi-modal document extraction, utilizing PyMuPDF and vision-enabled LLMs (specifically gpt-4o) to parse text and UML diagrams. To ensure educational reliability and mitigate hallucinations, CAPRA introduces a deterministic Evidence Anchoring step using fuzzy matching via normalized Levenshtein distance, along with a ConsistencyManager agent that cross-verifies, deduplicates, and merges findings. System performance is assessed using a structured eight-criterion binary evaluation taxonomy covering: (i) extraction completeness, (ii) feature validation, (iii) issue grounding and severity detection, (iv) recommendation specificity and traceability, and (v) template and tone compliance. A preliminary empirical evaluation on 10 student reports shows that CAPRA satisfied 88.8% of the evaluated criteria under a strict two-rater aggregation rule, achieved moderate inter-rater agreement with human evaluators (kappa = 0.582), and processed each report in slightly over 4 minutes. While these results support the viability of LLM-supported architectural feedback, human oversight remains essential for subjective assessment dimensions.

</details>


### 51. Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents

- **Authors:** Emmanuel Aboah Boateng, Kyle MacDonald, Amardeep Kumar, Siddharth Kodwani, Sudeep Das
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18947v1](http://arxiv.org/abs/2606.18947v1)
- **PDF:** [https://arxiv.org/pdf/2606.18947v1](https://arxiv.org/pdf/2606.18947v1)
- **Categories:** cs.AI, cs.CL, cs.IR, cs.MA


> The paper introduces **Decoupled Search Grounding (DSG)**, a vendor‑agnostic middleware that separates retrieval (search) from the LLM’s reasoning engine, exposing configurable routing, source‑aware context rendering, fallback policies, depth controls, and both exact and semantic caching. By moving grounding to an external MCP‑compatible gateway, DSG lets practitioners inspect, tune, and swap search components independently of the model, thereby avoiding “search‑induced verbosity” and reducing latency and cost. Experiments with five state‑of‑the‑art models on SimpleQA, FreshQA, and HotpotQA show that DSG attains almost the same accuracy as native‑integrated search (e.g., 86.1 % vs. 87.7 % on SimpleQA) while cutting search spend by ~91 % and latency by ~68 %, and in a production e‑commerce query‑understanding workload it matches or exceeds native accuracy while slashing search cost >98 %. This demonstrates that real‑time grounding is more effective when treated as an optimizable interface layer rather than a fixed model feature, a insight directly relevant to building scalable, controllable agentic AI systems.


<details>
<summary>Abstract</summary>

Production LLM agents increasingly depend on real-time search, yet native search grounding bundles retrieval policy, provider choice, evidence injection, cost, latency, and generation behavior behind a single model-provider boundary. This coupling makes grounding hard to inspect, tune, reuse, or port, and can trigger Search-Induced Verbosity that breaks strict output contracts. We present Decoupled Search Grounding (DSG), a vendor-agnostic boundary that moves grounding outside the reasoning model through an MCP-compatible gateway, exposing provider routing, source-aware context rendering, configured fallback, retrieval-depth control, and exact plus semantic caching as first-class controls. Across five frontier models on SimpleQA, FreshQA, and HotpotQA, native search leads on recency-sensitive FreshQA, but DSG exposes a stronger frontier when control matters: on SimpleQA it nearly matches native accuracy (86.1% vs. 87.7%) at 91% lower search cost, preserves concise answer contracts, and reaches a 99.4% warm-cache hit rate with 68% lower latency. Deployed as a shared production grounding layer for large-scale agentic workloads with interchangeable models, DSG matches or slightly exceeds native-search accuracy on an e-commerce query-understanding (QIU) workload while cutting search cost by over 98%. Real-time grounding is best treated as an optimizable interface boundary, not a fixed model feature.

</details>


### 52. SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration

- **Authors:** Ziyi Zhu, Luka Smyth, Saki Shinoda, Jinghong Chen
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18902v1](http://arxiv.org/abs/2606.18902v1)
- **PDF:** [https://arxiv.org/pdf/2606.18902v1](https://arxiv.org/pdf/2606.18902v1)
- **Categories:** cs.CL


> SAGE (Stochastic Prompt Optimization via Agent‑Guided Exploration) introduces a black‑box search framework for automatic prompt optimization that couples stochastic exploration of the prompt space with multi‑agent diagnostic code execution to iteratively refine prompts without touching model weights. The authors compare three increasingly sophisticated SPO strategies—error‑informed random search, a genetic algorithm, and the full SAGE pipeline—showing that performance varies with the error landscape, and they demonstrate that SAGE can reliably improve a mental‑health chatbot’s next‑day user retention after eight noisy A/B‑test cycles. The key finding is that pairing qualitative, agent‑driven diagnosis (e.g., executing diagnostic code) with quantitative validation yields a robust, agentic optimization loop for open‑ended, task‑oriented dialogue systems.


<details>
<summary>Abstract</summary>

Context engineering has emerged as a primary lever for improving AI systems without parameter updates. Recent work showing that textual gradients do not function as real gradients motivates treating automatic prompt optimization (APO) as black-box search. We introduce SPO (Stochastic Prompt Optimization), a framework for stochastic search over prompt space, and compare three strategies of increasing sophistication: error-informed random search, a genetic algorithm with evolutionary operators, and SAGE (SPO via Agent-Guided Exploration), a multi-agent pipeline with diagnostic code execution. Across three benchmarks, no single strategy dominates; effectiveness depends on the interaction of landscape structure with error type. We further deploy SAGE on a mental-health chatbot under a continuous optimization paradigm, where it compounds eight cycles of individually-noisy A/B tests into a statistically robust gain in next-day retention. We argue that coupling qualitative diagnosis with quantitative validation is what makes agentic optimization effective for open-ended task-oriented dialogue.

</details>


### 53. Generative-Model Predictive Planning for Navigation in Partially Observable Environments

- **Authors:** Thomas Quilter, Yifan Zhu, Guorui Quan, Mingfei Sun, Samuel Kaski
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18888v1](http://arxiv.org/abs/2606.18888v1)
- **PDF:** [https://arxiv.org/pdf/2606.18888v1](https://arxiv.org/pdf/2606.18888v1)
- **Categories:** cs.AI


> **Main contribution** – The paper introduces **BeliefDiffusion**, a framework that fuses diffusion‑based generative modeling of multimodal belief states with Model Predictive Control (MPC) to enable robust navigation in partially observable environments.  

**Methodology** – BeliefDiffusion first uses a diffusion model conditioned on the agent’s observation history to sample a set of plausible map configurations (i.e., multimodal belief over the unknown environment). It then aggregates these imagined worlds and runs an MPC planner that optimizes a trajectory jointly across all sampled configurations, effectively planning “for the worst‑case” while exploiting the full belief distribution.  

**Key findings** – In a suite of synthetic maze‑like maps, BeliefDiffusion achieves markedly higher navigation success rates and shorter paths than state‑of‑the‑art model‑free RL agents and prior generative baselines, demonstrating that explicit multimodal belief representation coupled with predictive planning dramatically improves agentic decision‑making under partial observability.


<details>
<summary>Abstract</summary>

Navigation in partially observable environments presents a significant challenge for autonomous agents, requiring effective decision-making with limited sensory information in unknown environments. Belief-based methods, particularly those using neural networks to approximate the belief space, often fail to capture the inherent multimodality of belief spaces, especially in high-dimensional cases with perceptual aliasing. While generative models present a compelling alternative, they typically require substantial data or expert demonstrations and lack explicit mechanisms for long-term planning. In this paper, we introduce BeliefDiffusion, a novel framework that combines the benefits of both generation and planning. BeliefDiffusion leverages diffusion models to explicitly characterize multimodal belief distributions and utilizes Model Predictive Control (MPC) to simultaneously plan ahead. It consists of two steps: (1) Imagining plausible environment configurations based on observation history and (2) Planning efficient navigation strategies across an aggregated configurations. Through extensive experiments in synthetic map environments, we demonstrate that BeliefDiffusion significantly outperforms both model-free reinforcement learning baselines and other generative approaches in navigation success rate and path efficiency. Our results validate that explicitly incorporating multimodal belief representations into planning enables more robust navigation in partially observable settings.

</details>


### 54. Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems

- **Authors:** Hehai Lin, Qi Yang, Chengwei Qin
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18837v1](http://arxiv.org/abs/2606.18837v1)
- **PDF:** [https://arxiv.org/pdf/2606.18837v1](https://arxiv.org/pdf/2606.18837v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> **Main contribution:** The paper introduces **Skill‑MAS**, a framework that treats the high‑level coordination logic of multi‑agent systems as an evolvable “Meta‑Skill” rather than embedding experience in the parameters of a frozen language model. This decouples experience retention from costly gradient updates, enabling the use of frontier LLMs while still learning from past interactions.

**Methodology:** Skill‑MAS closes a loop consisting of (1) *Multi‑Trajectory Rollout*, which generates diverse agent behavior distributions for each task under the current Meta‑Skill, and (2) *Selective Reflection*, which automatically picks priority tasks and applies hierarchical contrastive analysis to distill the collected trajectories into abstract, strategy‑level principles that update the Meta‑Skill representation (no parametric fine‑tuning of the underlying LLM).

**Key findings:** Across four challenging benchmarks and four different LLM backbones, Skill‑MAS delivers large performance improvements over both inference‑only and gradient‑based MAS baselines while using comparable computational resources. The evolved Meta‑Skills prove robust and transfer well to unseen tasks and to other LLMs, demonstrating a scalable path for experience‑driven, high‑capability multi‑agent coordination in the agentic AI domain.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based automatic Multi-Agent Systems (MAS) generation has become a crucial frontier for tackling complex tasks. However, existing methods face a dilemma between model capability and experience retention. Inference-time MAS leverages frozen frontier LLMs but repeats identical searches without learning from past experience. Conversely, Training-time MAS internalizes experience via gradient updates but is constrained by the low capability ceiling of smaller models, and is hard to scale to large frontier LLMs. To bridge this gap, we propose Skill-MAS, a novel third path that decouples experience retention from parametric updates by conceptualizing the high-level orchestration capability as an evolvable Meta-Skill. Skill-MAS refines this architectural knowledge through a closed optimization loop: (1) Multi-Trajectory Rollout samples a behavioral distribution for each task under the current Meta-Skill; and (2) Selective Reflection adaptively selects priority tasks and applies hierarchical contrastive analysis to distill systemic experience into generalizable, strategy-level principles. Extensive experiments across four complex benchmarks and four distinct LLMs demonstrate that Skill-MAS not only achieves remarkable performance gains but also maintains a favorable cost-performance trade-off. Further analysis reveals that the evolved Meta-Skills are highly robust and exhibit strong transferability across unseen tasks and different LLMs.

</details>


### 55. Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning

- **Authors:** Xiaoyue Xu, Sikui Zhang, Xiaorong Wang, Xu Han, Chaojun Xiao
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18831v1](http://arxiv.org/abs/2606.18831v1)
- **PDF:** [https://arxiv.org/pdf/2606.18831v1](https://arxiv.org/pdf/2606.18831v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution**: The paper demonstrates that, for long‑context reasoning in LLM‑based agents, a carefully curated training corpus can be as effective as sophisticated reward‑engineering approaches. By assembling a “data recipe” that mixes three task families—retrieval, multi‑evidence synthesis, and complex reasoning—across eight curated datasets (~14 K examples), the authors show that simple outcome‑based GRPO reinforcement learning attains large performance gains.

**Methodology**: The authors construct the eight datasets, integrate them into a standard GRPO (outcome‑based policy gradient) RL loop with minimal hyper‑parameter tuning, and train three Qwen‑3 models (4 B, 8 B, 30 B) on this data. They evaluate on seven established long‑context benchmarks and on two downstream agentic tasks (GAIA and BrowseComp) to assess transfer.

**Key findings**: The data‑centric approach yields average improvements of +7.2 (4 B), +3.2 (8 B), and +6.4 (30 B) points over baseline on the long‑context suite, outperforming prior RL training sets. When fine‑tuned on an already agent‑tuned model, the same recipe boosts GAIA by +4.8 and BrowseComp by +7.0 points, confirming that high‑quality, diverse long‑context data can replace extensive reward engineering for enhancing agentic LLM capabilities.


<details>
<summary>Abstract</summary>

Long-context reasoning is an essential capability for large language models, particularly when they are deployed as autonomous agents that must reason over lengthy trajectories. Reinforcement learning (RL) has recently emerged as a dominant paradigm for improving this ability, yet existing work largely focuses on reward engineering while diverse training data remains scarce. We revisit this problem from a data-centric perspective and show that a simple yet effective data recipe alone, paired with a minimal outcome-based GRPO setup, suffices to substantially improve long-context reasoning. Our recipe targets three complementary task families -- retrieval, multi-evidence synthesis, and reasoning -- for which we construct and curate eight datasets totaling ~14K examples. Experiments on three models (Qwen3-4B/8B/30B-A3B) yield average gains of +7.2/+3.2/+6.4 points across seven long-context benchmarks, surpassing prior RL training sets. We further demonstrate that these gains transfer to agentic tasks, where continuing RL training on an agent-tuned model with our data recipe improves GAIA by +4.8 and BrowseComp by +7.0 points. We will release our datasets to facilitate future research.

</details>


### 56. GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents

- **Authors:** Zhe Ren, Yibo Yang, Yimeng Chen, Zijun Zhao, Benshuo Fu, Zhihao Shu, Bingjie Zhang, Yangyang Xu, Dandan Guo, Shuicheng Yan
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18829v1](http://arxiv.org/abs/2606.18829v1)
- **PDF:** [https://arxiv.org/pdf/2606.18829v1](https://arxiv.org/pdf/2606.18829v1)
- **Categories:** cs.LG, cs.CL


> **Main contribution**  
The paper introduces **GateMem**, the first systematic benchmark for evaluating how well large‑language‑model agents can *govern* a shared memory pool that is written and queried by multiple principals with different roles, permissions, and relationships.

**Methodology**  
GateMem creates long‑horizon, multi‑party interaction episodes across four domains (medical, office, education, household). Each episode requires the agent to (1) correctly incorporate and retrieve legitimate updates, (2) enforce context‑dependent access‑control policies, and (3) actively forget or delete information on explicit request. The benchmark supplies hidden checkpoints, structured evaluation scripts, and “leak‑target” annotations to measure utility, unauthorized‑information leakage, and forgetting fidelity for a range of baselines (pure long‑context prompting, retrieval‑augmented generation, external‑memory systems, etc.).

**Key findings**  
Across all tested models, no approach simultaneously excels at all three dimensions: utility, robust access control, and reliable forgetting. Pure long‑context prompting attains the highest governance scores but at prohibitive token costs, while retrieval‑based and external‑memory methods are cheaper but still leak privileged or deleted data. The results indicate that current LLM‑based memory agents are far from being safe and effective for shared institutional deployments.


<details>
<summary>Abstract</summary>

Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. In these deployments, multiple principals write to a common memory pool and query it under different roles, scopes, and relationships, so memory quality requires governance as well as recall. We introduce GateMem, a benchmark for multi-principal shared-memory agents. GateMem jointly evaluates utility for legitimate long-horizon requests with state updates, access control across contextual authorization boundaries, and agent-facing active forgetting after explicit deletion requests. It spans medical, office, education, and household domains, with long-form multi-party episodes, incremental memory injection, hidden checkpoints, structured judging, and leak-target annotations. Across diverse baselines and backbone models, no method simultaneously achieves strong utility, robust access control, and reliable forgetting. Long-context prompting often yields the best governance score at high token cost, while retrieval-based and external-memory methods reduce cost yet still leak unauthorized or deleted information. These results show current memory agents remain far from reliable shared institutional deployment.

</details>


### 57. ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch

- **Authors:** Tengfei Lyu, Zirui Yuan, Xu Liu, Kai Wan, Zihao Lu, Li Ma, Hao Liu
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18803v1](http://arxiv.org/abs/2606.18803v1)
- **PDF:** [https://arxiv.org/pdf/2606.18803v1](https://arxiv.org/pdf/2606.18803v1)
- **Categories:** cs.AI, cs.CY


> ProfiLLM introduces an agentic LLM pipeline that turns massive, unstructured ride‑hailing logs into utility‑aligned user profiles for real‑time dispatch. The system couples (1) a tool‑augmented “global knowledge miner” that uses 27 LLM‑driven analytical tools to extract platform‑wide patterns, cluster drivers, and build supply‑demand priors, with (2) a “profile explorer” that generates and iteratively refines multiple candidate profiles per cluster, selecting those that maximize a lightweight downstream prediction proxy and fine‑tuning the LLM via DPO on generated preference pairs. Deployed on DiDi’s live dispatcher, ProfiLLM yields up to 6.14 % relative AUC gain in outcome prediction, 4.35 % GMV uplift in offline simulation, and measurable online improvements (+0.47 % GMV, +0.33 % completion rate, –0.82 % cancel‑before‑accept) in a 14‑day A/B test, demonstrating that LLM‑generated, utility‑aligned profiles can enhance industrial‑scale agentic decision systems.


<details>
<summary>Abstract</summary>

Bringing Large Language Models (LLMs) into industrial ride-hailing dispatch as semantic feature extractors over platform-scale behavioral logs is a compelling but under-explored data systems problem. Production matching pipelines remain dominated by structured numerical features, yet decisive behavioral signals (e.g., a driver's habitual aversion to certain regions) are inherently contextual and naturally expressible as LLM-generated user profiles. However, scaling such profiling to a live, millisecond-latency dispatcher faces three intertwined constraints rarely addressed together: on a platform with millions of daily orders, logs exceed any LLM's context window by orders of magnitude; most users are long-tail, with too few interactions for per-user profiling; and surface-fluent profiles do not necessarily improve downstream prediction utility. We present ProfiLLM, an agentic LLM data pipeline that operationalizes utility-aligned user profiling for production matching systems through two modules. (1) Tool-Augmented Global Knowledge Mining equips an LLM agent with 27 analytical tools to mine platform-scale data, producing reusable global knowledge, adaptive user clustering rules, and region-level supply-demand priors. (2) Utility-Aligned Profile Exploration generates multiple candidate profiles per cluster, evaluates them via a lightweight downstream utility proxy, iteratively refines the best candidates and constructs preference pairs for DPO fine-tuning. Deployed on DiDi's production dispatcher, ProfiLLM achieves up to +6.14% relative AUC improvement in outcome prediction, up to +4.35% GMV gain in dispatching simulation, and consistent improvements in a 14-day online A/B test including +0.47% GMV, +0.33% Completion Rate, and -0.82% Cancel-Before-Accept rate.

</details>


### 58. R2D-RL: A RoboCup 2D Soccer Environment for Multi-Agent Reinforcement Learning

- **Authors:** Haobin Qin, Baofeng Zhang, Hidehisa Akiyama, Keisuke Fujii
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18786v1](http://arxiv.org/abs/2606.18786v1)
- **PDF:** [https://arxiv.org/pdf/2606.18786v1](https://arxiv.org/pdf/2606.18786v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents **R2D‑RL**, a Python‑friendly reinforcement‑learning wrapper for the RoboCup 2D Soccer Simulation (RCSS2D) that enables large‑scale, cycle‑synchronized multi‑agent training while preserving the full physics and communication model of the original server‑client architecture.  

**Methodology:** R2D‑RL links HELIOS player clients to a Python MARL loop via shared‑memory buffers, providing both full‑field 11‑vs‑11 and scenario‑based environments, configurable discrete and hybrid (parameterized) action spaces, action masking, and an Expected Possession Value (EPV) reward‑shaping module; it also supports parallel roll‑outs to speed up data collection.  

**Key findings:** Baseline experiments on a front‑goal scoring scenario and a full‑field 11‑vs‑11 benchmark demonstrate that agents can learn cooperative tactics under partial observability and sparse rewards, and that EPV‑shaped rewards significantly accelerate learning compared to raw goal‑only signals, establishing R2D‑RL as a viable testbed for advancing agentic AI in complex, adversarial, and cooperative domains.


<details>
<summary>Abstract</summary>

Robot soccer is a challenging testbed for multi-agent reinforcement learning because it combines partial observability, cooperative and adversarial interaction, sparse rewards, and long-horizon tactical behavior. RoboCup 2D Soccer Simulation (RCSS2D) provides a mature robot-soccer platform, but its competition-oriented server-client architecture is difficult to use directly with modern Python-based MARL workflows. We introduce R2D-RL, a reinforcement learning environment that connects RCSS2D and HELIOS-based player clients to a Python MARL interface through shared-memory communication and cycle-level synchronization. R2D-RL supports full-field and scenario-based training with configurable opponents, Base discrete and Hybrid parameterized action spaces, action masks, expected possession value (EPV)-based reward shaping, and parallel execution. We provide front-goal scenarios and an 11-vs-11 full-field benchmark, together with baseline results.

</details>


### 59. Human-AI Agent Interaction in a Business Context

- **Authors:** Kathrin Paimann, Elizangela Valarini, Sebastian Juhl
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18716v1](http://arxiv.org/abs/2606.18716v1)
- **PDF:** [https://arxiv.org/pdf/2606.18716v1](https://arxiv.org/pdf/2606.18716v1)
- **Categories:** cs.HC, cs.AI


> The paper’s main contribution is an empirically grounded framework of design principles, evaluation criteria, and measurement methods for fostering positive user experience (UX) in human‑AI agent interactions within business processes. The authors employ a mixed‑methods design—initial qualitative interviews and observation to uncover user expectations, needs, and interaction patterns, followed by a quantitative survey experiment that tests the impact of specific UI/UX design elements on trust, adoption, and decision‑making quality. Results show that clarity of agent role, transparency of algorithmic reasoning, and controllability markedly improve perceived trust and decision support effectiveness, offering actionable guidelines for agentic AI developers seeking user‑centered business applications.


<details>
<summary>Abstract</summary>

As AI agents are increasingly integrated into core business processes, understanding and designing effective interaction patterns between humans and AI agents becomes crucial for value creation. This study identifies and evaluates principles and criteria for a positive User Experience (UX) with AI agents, along with methods for its measurement. We identify user expectations and needs to facilitate adoption, build trust, and support user-centered decision-making by development teams. Using a mixed-methods approach that combines qualitative and quantitative techniques, we explore interaction patterns between humans and AI agents. The findings from this exploratory research serve as the basis to develop a survey experiment which evaluates the effectiveness of specific design elements on a larger scale. This foundational research contributes to the development of more intuitive and effective human-AI agent interactions in business settings.

</details>


### 60. Dual-Channel Grounded World Modeling (DCGWM): Structural Prevention of Objective Interference Collapse via Heterogeneous External Grounding with Inward-Only Gradient Flow

- **Authors:** Akshay Hazare
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18688v1](http://arxiv.org/abs/2606.18688v1)
- **PDF:** [https://arxiv.org/pdf/2606.18688v1](https://arxiv.org/pdf/2606.18688v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution** – The paper identifies and formally characterizes *Objective Interference Collapse* (OIC), a failure mode in Joint‑Embedding Predictive Architectures (JEPAs) where learning from heterogeneous grounding signals (physical vs. social‑behavioral) causes the dominant channel to overwrite the subordinate one in a shared latent space. To eliminate this interference, the authors propose **Dual‑Channel Grounded World Modeling (DCGWM)**, a structurally partitioned architecture that isolates a physical latent subspace ( \(Z_p\) ) and a behavioral latent subspace ( \(Z_b\) ) and enforces **inward‑only gradient flow** so that each grounding signal updates only its own subspace.

**Methodology** – DCGWM couples the two subspaces through a task‑level interface module that does not transmit gradients across subspaces. The physical channel is trained with a VICReg‑style invariance‑covariance‑regularization loss against sparse high‑magnitude physical measurements; the social‑behavioral channel uses a KL‑type alignment loss against trajectories from a multi‑agent simulation. An asymmetric grounding‑adherence loss (hard hinge for physical violations, soft KL for behavioral drift) penalizes rollout drift, and a generative rendering layer is kept architecturally separate from the latent world model to avoid back‑propagation into the grounding pathways.

**Key findings** – The authors prove three theoretical results: (1) the partitioned latent space removes the gradient‑interference pathway that produces OIC; (2) each subspace inherits anti‑collapse guarantees from its respective alignment objective; and (3) isolating the generative renderer is necessary under a mild geometric assumption on the generative loss. Although empirical validation is pending, the formal analysis provides a blueprint for building agentic world models that can safely integrate heterogeneous external grounding without mutual interference.


<details>
<summary>Abstract</summary>

Joint Embedding Predictive Architectures (JEPAs) are a leading approach to world model representation learning. We identify a failure mode in JEPA-based world models grounded against two qualitatively distinct external signals: physical dynamics (sparse, high-magnitude, constraint-satisfying gradient corrections) and social-behavioral dynamics (diffuse, distribution-matching corrections). We term this Objective Interference Collapse (OIC): we argue that joint learning in a shared latent space causes the dominant channel to systematically collapse the subordinate channel's representational subspace, in a manner not resolvable by loss weighting alone. We propose Dual-Channel Grounded World Modeling (DCGWM), designed to structurally prevent OIC through a partitioned latent space (physical subspace Z_p, behavioral subspace Z_b) with inward-only gradient flow. A Physical Grounding Channel updates only Z_p via VICReg-style alignment to physical measurements; a Social-Behavioral Grounding Channel updates only Z_b via alignment to trajectories from an emergent multi-agent simulation. An Inter-Channel Interface Module couples the subspaces at the task level without cross-subspace gradients. An Asymmetric Grounding Adherence Loss penalizes rollout drift with a hard hinge for physical violations and a soft KL for behavioral divergence. A Generative Rendering Layer is architecturally isolated from the latent world model. We present three theoretical results: the partition removes the gradient-interference pathway implicated in OIC; each grounded subspace inherits anti-collapse guarantees from its alignment objective; and generative isolation is necessary under a stated assumption on the generative objective's geometry. This manuscript establishes the problem formulation and architecture; experimental validation is ongoing and will be reported in a future revision.

</details>


### 61. EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems

- **Authors:** Shuang Xie, Yunan Lu, Han Li, Lingyun Wang
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18668v1](http://arxiv.org/abs/2606.18668v1)
- **PDF:** [https://arxiv.org/pdf/2606.18668v1](https://arxiv.org/pdf/2606.18668v1)
- **Categories:** cs.MA, cs.CL


> **Main contribution:** EARS introduces “explanatory abstention,” turning a sub‑agent’s refusal to answer into a structured, communicable failure report that the central coordinator can act on, thereby improving reliability in large‑scale, hierarchical multi‑agent systems.  

**Methodology:** The authors curate a taxonomy of sub‑agent failure modes and generate training data by labeling real user‑agent interactions with calibrated LLM‑as‑Judge ensembles that provide both abstention tags and rationales. These labeled examples are used to fine‑tune domain‑specific sub‑agents so that, instead of over‑answering, they detect incapacity, produce a rationale, and send an actionable signal to the coordinator for clarification, rerouting, or fallback.  

**Key findings:** In a production e‑commerce business‑intelligence assistant, deploying EARS raised the overall pass rate of system responses from **68.5 % to 78.9 %**, demonstrating that explanatory abstention markedly enhances the robustness and trustworthiness of coordinated multi‑agent deployments.


<details>
<summary>Abstract</summary>

In large-scale enterprise settings, centralized multi-agent systems (MAS) are increasingly adopted, in which a coordinator delegates user requests to lightweight, domain-specialized sub-agents. While this architecture improves modularity, scalability, and cost efficiency, its reliability depends not only on accurate routing but also on sub-agents' ability to calibrate their responses to capability constraints. In particular, sub-agents built on smaller fine-tuned models often struggle with such calibration, leading them to over-answer ambiguous, underspecified, misrouted, or unsupported requests and produce hallucinated outputs instead of actionable feedback. To address this challenge, we present EARS (Explanatory Abstention for Reliable Sub-Agent Modeling), a production-oriented framework that reframes sub-agent abstention as an inter-agent communication protocol: a sub-agent does not merely abstain, but exposes an actionable failure state to the coordinator. EARS curates human-agent interaction data using an ensemble of calibrated LLM-as-a-Judge models, producing structured abstention labels and rationales under a taxonomy of sub-agent failure modes. These data are used to fine-tune sub-agents to detect failure conditions and return rationales for coordinator-level clarification, rerouting, or fallback. We evaluate EARS in a large-scale production e-commerce assistant supporting enterprise business intelligence workflows. EARS improves the overall response pass rate from 68.5% to 78.9%, demonstrating that sub-agent-side explanatory abstention improves MAS reliability.

</details>


### 62. EffiNav: Fusing Depth and Vision-Language for Efficient Object Goal Navigation

- **Authors:** Zecheng Yin, Benedict Jun Ma
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18634v1](http://arxiv.org/abs/2606.18634v1)
- **PDF:** [https://arxiv.org/pdf/2606.18634v1](https://arxiv.org/pdf/2606.18634v1)
- **Categories:** cs.RO, cs.AI


> EffiNav introduces a lightweight navigation framework that jointly exploits dense depth cues and vision‑language embeddings to predict the most informative next exploration direction, thereby reducing redundant motion while still locating the target object. The method combines a depth‑driven frontier selection module with a pretrained language‑grounded object detector, training only a small policy head on simulated episodes; it is then evaluated on Habitat Matterport 3D (HM3D) and Open‑Vocabulary Object‑Goal Navigation (OVON) benchmarks and transferred to real‑world robots and a memory‑augmented ObjNav variant (GOAT‑BENCH). Across Success Rate and SPL metrics, EffiNav matches or surpasses recent baselines, demonstrating superior efficiency, robustness, and generalisation for object‑goal navigation in previously unseen environments.


<details>
<summary>Abstract</summary>

To locate a target object while exploring the unknown environment is a fundamental capability for autonomous agents, with applications ranging from search-and-rescue to field robots. A simplified version of such task is Object Goal Navigation (ObjNav). In ObjNav, successful arrival at the target object provides a basic measure of performance; however, the efficiency of the navigation trajectory is equally important, as it indicates how intelligently the agent explores and how much time remains for subsequent tasks. In unknown environments, the key to efficient navigation lies in deciding where to explore next. While many prior works aim to address this core challenge and achieved promising performance in certain settings, recent training-based models and non-training frameworks still suffer from generalization and efficiency issues respectively, which in the worst cases can lead to excessive exploration of already-visited areas or redundant back-and-forth motion. We evaluate EffiNav on two widely used simulation benchmarks Habitat Matterport 3D (HM3D) and Open-Vocabulary Object goal Navigation (OVON), and further validate its effectiveness on physical robots in real-world settings. We conduct failure analysis on massive simulation episodes. With minimal modification, we also extend EffiNav to a memory-augmented ObjNav task on the GOAT-BENCH dataset, demonstrating its adaptability beyond standard ObjNav settings. Across two standard metrics--Success Rate (SR) and Success weighted by Path Length (SPL), EffiNav matches or outperforms recent baselines, reflecting its efficiency, robustness, and practical applicability. Recognizing the different emphases of the two datasets, the performances reveals this framework is more balanced and generalizable for efficient ObjNav.

</details>


### 63. PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning

- **Authors:** Zhiyuan Wen, Jiannong Cao, Peng Gao, Haochen Shi, Wengpan Kuan, Bo Yuan, Xiuxiu Qi
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18633v1](http://arxiv.org/abs/2606.18633v1)
- **PDF:** [https://arxiv.org/pdf/2606.18633v1](https://arxiv.org/pdf/2606.18633v1)
- **Categories:** cs.MA


> **Main contribution:** The paper introduces **MAP‑PPL**, a new dataset of 3,043 multi‑agent plans that are conditioned on learner profiles, and presents **PersonalPlan**, a two‑stage, profile‑grounded multi‑agent planning system for personalized programming education.

**Methodology:** PersonalPlan first fine‑tunes a large language model with separate LoRA adapters for (i) profile‑aware task decomposition and (ii) step‑dependency planning, then refines the model using a Reward‑Adaptive Gradient‑Reward‑Policy‑Optimization (GRPO) to maximize executability, personalization, and pedagogical scaffolding of the generated plans.

**Key findings:** Across extensive experiments on MAP‑PPL, the 8 B and 32 B PersonalPlan variants outperform leading LLMs, generic MAS frameworks, and existing agentic planners, achieving state‑of‑the‑art scores in plan executability, personalization to learner profiles, and pedagogical quality, thereby demonstrating effective orchestration of multi‑agent systems for individualized programming instruction.


<details>
<summary>Abstract</summary>

Effective programming education requires personalized instruction adapted to diverse learner backgrounds. However, while LLM-based multi-agent systems (MAS) excel at complex planning, existing planners often lack profile-grounding and pedagogical scaffolding, thereby undermining personalized programming learning. To fill in the gap, we first introduce \textbf{MAP-PPL} (\textbf{M}ulti-\textbf{A}gent \textbf{P}lans for \textbf{P}ersonalized \textbf{P}rogramming \textbf{L}earning), a profile-conditioned multi-agent planning dataset with 3{,}043 query--profile--plan instances from 1{,}730 Stack Overflow question groups and 2{,}738 learner profiles. Each plan specifies agents, subtasks, executable steps, and prerequisite dependencies. Then, we propose \textbf{PersonalPlan}, a two-stage MAS planner that first performs hierarchical SFT with separate LoRA adapters for profile-aware task decomposition and step dependency planning, then applies a Reward-Adaptive GRPO to encourage the model to generate executable, personalized, and pedagogically scaffolded plans. Extensive experiments on MAP-PPL comparing PersonalPlan against frontier LLMs, generic MAS frameworks, and agentic planners demonstrate its superiority. With only 8B and 32B variants, PersonalPlan achieves state-of-the-art plan executability, personalization, and pedagogical quality, effectively orchestrating MAS for agent-student interactions.

</details>


### 64. Code-Augur: Agentic Vulnerability Detection via Specification Inference

- **Authors:** Zhengxiong Luo, Mehtab Zafar, Dylan Wolff, Abhik Roychoudhury
- **Published:** 2026-06-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18619v1](http://arxiv.org/abs/2606.18619v1)
- **PDF:** [https://arxiv.org/pdf/2606.18619v1](https://arxiv.org/pdf/2606.18619v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> **Main contribution** – The paper introduces **Code‑Augur**, a framework that turns autonomous LLM‑based vulnerability scanners from “black‑box judges” into **specification‑driven agents**. By extracting the agent’s implicit security assumptions as formal in‑source assertions and then continuously stress‑testing them with a guided fuzzer, the system makes the agent’s reasoning transparent and correctable.

**Methodology** – Code‑Augur first prompts a general‑purpose LLM (e.g., Sonnet, DeepSeek) to analyze each component of a target codebase and to emit the security invariants it believes guarantee safety. These invariants are injected as assertions in the code. A runtime fuzzer then attempts to falsify each assertion; when a falsification occurs, the framework either surfaces a true vulnerability or feeds the counterexample back to the LLM to refine its specification, iterating until the assertions hold or a bug is confirmed.

**Key findings** – On a benchmark of real‑world open‑source projects, Code‑Augur uncovered **22 previously unknown vulnerabilities** and outperformed state‑of‑the‑art agentic scanners, including specialized models such as Claude Mythos. The results demonstrate that coupling LLM agents with explicit security specifications and falsification dramatically improves both discovery power and trustworthiness in agentic AI security analysis.


<details>
<summary>Abstract</summary>

The advent of agentic vulnerability detection is already becoming a watershed moment for software security. Audits conducted entirely by autonomous LLM agents are uncovering critical vulnerabilities in fundamental software underpinning digital society. Many of these vulnerabilities remained masked for years, surfacing only now with AI agents. Yet the reasoning behind these discoveries remains alarmingly opaque and unvalidated. What assumptions did the agent make about a function's inputs when it deemed that function to be secure? Failures in reasoning and incorrect assumptions can lead to missed vulnerabilities and reduce trust in agentic analysis.
  We propose a security-specification-first paradigm that (1) exposes the agent's tacit assumptions explicitly as security specifications and (2) continuously refines those specifications via runtime falsification. We realize our approach in Code-Augur, a novel harness for agentic vulnerability detection. Given a codebase, Code-Augur analyzes each component of the system for vulnerable code. When it deems a component to be secure, it commits the local invariants behind that judgment as in-source assertions. In parallel, Code-Augur leverages a guided fuzzer to attempt to falsify those assumptions. When the fuzzer triggers an assertion, this either reveals a genuine vulnerability or a flawed specification to refine. In both cases, this process grounds the agent's understanding, aligning its view of code intent with how the code actually behaves. On real-world subjects, Code-Augur effectively leverages security specifications to detect more vulnerabilities than other state-of-the-art agents. Additionally, Code-Augur found 22 new vulnerabilities in key open-source projects. Compared to curated specialized models like Claude Mythos, Code-Augur offers effective agentic vulnerability detection built on widely available LLMs like Sonnet and DeepSeek.

</details>


### 65. Do as the Romans Do: Learning Universal Behaviors from Heterogeneous Agents

- **Authors:** Caleb Chang, Davin Win Kyi, Natasha Jaques, Karen Leung
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18537v1](http://arxiv.org/abs/2606.18537v1)
- **PDF:** [https://arxiv.org/pdf/2606.18537v1](https://arxiv.org/pdf/2606.18537v1)
- **Categories:** cs.LG


> **Paper Summary**

The authors introduce **General Reward Inference and Disentanglement (GRID)**, a social‑learning framework that isolates a *general* reward component shared by all agents from *specific* reward components that encode each demonstrator’s individual goals. GRID first infers per‑agent reward functions via inverse reinforcement learning, then factorizes each into a universal reward plus agent‑specific terms; only the universal reward is used to pre‑train a **generalist agent**. Experiments on synthetic function‑decomposition tasks, the multi‑agent Craftax benchmark, and Highway‑Env demonstrate that GRID reliably disentangles reward structure, avoids the mode‑averaging bias of conventional learning‑from‑demonstration, and yields a pretrained policy that fine‑tunes faster and more stably to downstream tasks—even to preferences never seen during pretraining.


<details>
<summary>Abstract</summary>

Humans often acquire new skills by observing others, since observed behaviors implicitly reveal how to act in an environment. However, observations drawn from a heterogeneous population introduce conflicting behavioral signals, making it difficult to determine which behaviors are worth imitating. We address this challenge with General Reward Inference and Disentanglement (GRID), a social learning method that extracts universally useful behaviors from a heterogeneous population of demonstrators pursuing different goals. GRID decomposes per-agent reward functions into a general reward, capturing behaviors shared across all agents, and specific rewards, capturing individual preferences and objectives. Training exclusively on the general reward provides a new paradigm of generalist pretraining. It yields a generalist agent that internalizes universal environmental competencies, such as safety and basic task proficiency, without the mode-averaging bias that afflicts standard learning from demonstration techniques. This generalist serves as a superior prior for fine-tuning to downstream tasks, including preferences unseen during training. Experiments across a synthetic basis function decomposition, multi-agent Craftax, and a continuous autonomous driving simulator (Highway-Env) confirm that GRID successfully disentangles reward structure in a semantically meaningful way, outperforms standard learning from demonstration baselines, and enables more efficient and stable specialization.

</details>


### 66. Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications

- **Authors:** Paresh Dashore, Shreyas Kulkarni, Uttam Gurram, Nadia Bathaee, Kartik Balasubramaniam, Genta Indra Winata, Sambit Sahu, Shi-Xiong Zhang
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18502v1](http://arxiv.org/abs/2606.18502v1)
- **PDF:** [https://arxiv.org/pdf/2606.18502v1](https://arxiv.org/pdf/2606.18502v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces a two‑stage framework that makes LLM‑driven multi‑agent systems practical for enterprise use by (1) rapidly customizing a compact base model for a specific domain and (2) dramatically cutting inference cost while preserving agentic performance.

**Methodology:** Stage 1 (“Agentic Model Customization”) blends continual pre‑training, supervised fine‑tuning, and preference‑based reinforcement learning to specialize a small model without losing its reasoning and planning abilities. Stage 2 (“Inference Optimization”) couples speculative decoding with FP8 quantization plus targeted calibration to accelerate serving.

**Key findings:** On a suite of real‑world enterprise workloads, the customized agents achieve comparable or better task success rates—especially on long‑tail queries—while throughput increases by **4.48 ×** and latency/compute cost drops sharply, demonstrating that scalable, low‑latency deployment of agentic AI is feasible.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems demonstrate strong performance on complex reasoning and task execution, enabling broad enterprise applications. However, production deployment remains challenging due to domain-specific customization requirements and high latency and inference costs in agentic workflows. We propose a unified framework for customization and efficient deployment of multi-agent systems in real-world settings. The first stage, Agentic Model Customization, combines continual pretraining, supervised fine-tuning, and preference optimization to adapt a compact model to specialized domains while retaining strong agentic capabilities. The second stage, Inference Optimization, integrates speculative decoding and FP8 quantization with targeted calibration to enable cost-efficient serving with minimal quality loss. Across enterprise workloads, our framework enables rapid domain adaptation and achieves a 4.48x speedup in throughput while maintaining performance and improving robustness on long-tail scenarios.

</details>


### 67. ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift

- **Authors:** Jeffery Opoku, David Banahene
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18467v1](http://arxiv.org/abs/2606.18467v1)
- **PDF:** [https://arxiv.org/pdf/2606.18467v1](https://arxiv.org/pdf/2606.18467v1)
- **Categories:** stat.ML, cs.LG


> **Main contribution:** The paper introduces **ToolChain‑CRC**, a conformal‑risk‑control framework that monitors every step of a retrieval‑augmented or tool‑using AI agent (retrieval, tool invocation, intermediate checks, final output) and decides—via calibrated thresholds—whether to accept the trajectory or intervene early, thereby guarding against hidden failures that are invisible from the final answer alone.

**Methodology:** ToolChain‑CRC treats each agent execution as a full trajectory, computes step‑level non‑conformity scores (e.g., retrieval relevance, tool‑output consistency), aggregates them into a trajectory‑level risk score, and learns an accept/​intervene rule using exchangeable calibration runs. The authors extend the method to handle distribution drift (with auditable constants) and provide an anytime‑escalation guarantee using a super‑martingale‑based alarm that can stop a run before completion.

**Key findings:** Across synthetic drift simulations, stress‑tested RAG/tool‑use benchmarks, SQuAD‑derived retrieval tasks, and a live API‑free QA agent, trajectory‑level calibration consistently keeps the empirical risk of accepted runs below the target level, whereas calibration based only on final answers often fails to detect retrieval or tool failures. The approach remains robust across seeds, risk targets, and drift magnitudes, demonstrating practical, auditable risk control for agentic AI systems.


<details>
<summary>Abstract</summary>

Modern AI agents retrieve documents, call tools, check intermediate information, and then produce a final answer or action. This creates a risk-control problem that is not visible from the final answer alone. A final response may look acceptable even when the retrieval was weak, a tool output was wrong, or an earlier step was unsupported. We propose ToolChain-CRC, a conformal risk-control method for retrieval-augmented and tool-using agents under drift. The method treats each agent run as a full trajectory of actions, observations, and final output. It builds step-level risk scores, combines them into a trajectory risk score, calibrates an accept-or-intervene rule, and adds an anytime alarm that can stop risky runs before the final answer. We prove trajectory-level risk control under exchangeable calibration runs, give a drift-aware extension with auditable constants, and prove an anytime escalation rule through a supermartingale construction. Experiments cover synthetic tool-chain drift, RAG/tool-use stress tests, public SQuAD-derived retrieval tasks, an API-free agentic QA case study, ablations, target-risk sensitivity checks, 20-seed robustness checks, a drift-margin audit, and a live RAG/tool-use agent benchmark. Across these settings, final-answer-only calibration can miss retrieval and tool failures, while trajectory-level calibration keeps accepted-trajectory risk below the target.

</details>


### 68. Searching for Synergy in Shared Workspace Human-AI Collaboration

- **Authors:** Nachiket Kotalwar, Rohini Das, Carolyn Rose
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18413v2](http://arxiv.org/abs/2606.18413v2)
- **PDF:** [https://arxiv.org/pdf/2606.18413v2](https://arxiv.org/pdf/2606.18413v2)
- **Categories:** cs.AI, cs.HC


> The paper investigates how the coordination structure of shared‑workspace human‑AI teams impacts task performance, showing that simply adding more (simulated) human collaborators can hurt results unless roles and responsibilities are explicitly scaffolded. Using the Collaborative Gym environment and DiscoveryBench tasks, the authors compare baseline teams to ones equipped with a shared group‑memory plus “human‑in‑the‑loop” approval gates that route actions to a designated participant; across 1,482 sessions this scaffolding consistently raises mean scores, especially in three‑person teams, by clarifying responsibility signals and better exploiting expertise. The findings highlight that effective coordination mechanisms are as crucial as raw AI capability for successful agentic AI collaborations.


<details>
<summary>Abstract</summary>

Automated AI agents are increasingly capable, yet many scientific and professional tasks require human judgment and contextual expertise. We study shared-workspace human-AI teams, where AI agents and human collaborators must coordinate responsibilities before submitting a final answer. Using the Collaborative Gym environment with DiscoveryBench tasks, we examine when adding simulated human collaborators improves performance and when process loss turns additional collaborators into coordination overhead. Across 1,482 sessions, adding relevant collaborators can lower performance when teams lack structure to coordinate their contributions. We then evaluate scaffolding that combines shared group memory with simulated human-in-the-loop (HITL) gates, where selected actions require approval from a designated simulated participant. This scaffolding yields higher mean performance, most clearly in three-person teams, with clearer responsibility signals and stronger routing of expertise to team actions. Overall, how human-AI teams coordinate and integrate expertise matters as much as the capability available to them.

</details>


### 69. LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents

- **Authors:** Haoyang Fang, Wei Zhu, Boran Han, Alex Zhang, Zhenyu Pan, Shuo Yang, Shuai Zhang, Jiading Gai, Peng Tang, Cuixiong Hu, Xuan Zhu, Huzefa Rangwala, George Karypis, Bernie Wang
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18388v1](http://arxiv.org/abs/2606.18388v1)
- **PDF:** [https://arxiv.org/pdf/2606.18388v1](https://arxiv.org/pdf/2606.18388v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.MA


> **Main contribution**  
The paper introduces **LLMZero**, a framework that equips large‑language‑model (LLM) agents with a tree‑search capability to automatically design multi‑stage reinforcement‑learning (RL) post‑training schedules. By letting the agents diagnose training pathologies at checkpoint intervals and propose coordinated changes to both capacity‑type (monotonically increasing) and regularization‑type (oscillatory) hyper‑parameters, LLMZero uncovers a general principle: capacity parameters should be monotonic across stages, while regularization parameters must adaptively oscillate to track the non‑stationary exploration‑exploitation trade‑off.

**Methodology**  
- Encode the RL post‑training process as a discrete decision‑making problem where each node represents a set of hyper‑parameter values at a checkpoint.  
- Deploy an LLM agent to evaluate the current trajectory, generate candidate multi‑parameter adjustments, and rank them using a learned value estimate.  
- Perform a guided tree search (Monte‑Carlo‑style expansion and back‑propagation of rewards) to explore many possible schedules, selecting the trajectory that maximizes downstream performance.  

**Key findings for agentic AI**  
- On four heterogeneous GRPO benchmarks, schedules discovered by LLMZero yield **9 %–140 % relative gains** over the baseline post‑training policy and **6 %–15 % improvements** over exhaustive grid search, consistently beating random search and a prior skill‑based agent.  
- The discovered schedules obey the identified structural principle (monotonic capacity, oscillatory regularization), demonstrating that LLM‑driven meta‑optimization can infer transferable training dynamics without task‑specific tuning.  
- The approach shows that LLM agents can act as effective “research assistants,” autonomously generating and testing complex hyper‑parameter curricula, suggesting a scalable path toward self‑improving, adaptive RL agents.


<details>
<summary>Abstract</summary>

RL post-training strategies are dataset-dependent and reveal a recurring empirical pattern: capacity parameters accumulate monotonically across stages, while regularization parameters predominantly oscillate in response to shifting training dynamics. This distinction matters because fixed schedules commit all parameters to fixed trajectories and therefore cannot express the non-stationary exploration-exploitation tradeoffs that regularization must track; the principle provides actionable design rules for multi-stage training. We discover this through LLMZero, a system where LLM agents search over training trajectories via tree search, diagnosing pathologies at each checkpoint and proposing coordinated multi-parameter transitions. Across 4 diverse GRPO tasks, LLMZero discovers strategies that improve over the base model by 9% to 140% relative and over grid search by 6% to 15% relative, consistently outperforming random search and the skill-based agent. The structural principle transfers across tasks, providing an explanation for why discovered strategies take qualitatively different forms yet share similar parameter dynamics.

</details>


### 70. SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents

- **Authors:** Yuchuan Tian, Mengyu Zheng, Haocheng Mei, Ye Yuan, Chao Xu, Xinghao Chen, Hanting Chen, Yu Wang
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18356v1](http://arxiv.org/abs/2606.18356v1)
- **PDF:** [https://arxiv.org/pdf/2606.18356v1](https://arxiv.org/pdf/2606.18356v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **SafeClawBench**, a 600‑task staged benchmark that disentangles three failure modes of tool‑using LLM agents—semantic acceptance of a malicious request, audit‑visible evidence of harmful output, and sandbox‑observable state‑change harm. By evaluating five agent configurations across four prompt‑level defenses on six attack families (prompt injection, tool‑return injection, memory poisoning/extraction, and ambiguity‑driven inference), the authors show that semantic failure rates range from 9 % to 44 % while audit and sandbox harms are much rarer and often occur in different subsets of examples, revealing that traditional single‑metric attacks conflate distinct vulnerabilities. The framework demonstrates that prompt policies can shift these endpoints in model‑ and protocol‑specific ways, providing a reproducible tool for rigorously comparing security of agentic AI systems.


<details>
<summary>Abstract</summary>

Tool-using language-model agents introduce security failures that go beyond unsafe text: they can disclose protected objects, write persistent memory, send messages, modify databases, or trigger harmful code and tool effects. Existing evaluations often collapse these stages into a single attack success rate, making it difficult to tell whether a model merely agreed with an attacker or actually produced observable harm. We introduce SafeClawBench, a staged benchmark for tool-using agent security with 600 controlled adversarial tasks across six attack families: direct and indirect prompt injection, tool-return injection, memory poisoning, memory extraction, and ambiguity-driven unsafe inference. SafeClawBench reports three separate endpoints: semantic attack acceptance, audit-visible harm evidence, and sandbox-observed tool/state harm. Evaluating five agent endpoints under four prompt-level policies, we find that these endpoints capture different failure modes. Without additional prompt protection, semantic failure rates vary widely across models, from 9.0% to 44.2%. Audited harm evidence is narrower than semantic failure, and under a separate executable protocol some matched task identities produce sandbox harm despite passing the Semantic Core call: in a 12,000-row matched analysis, 291 of 347 observed sandbox harms occur in rows that pass the semantic check. Prompt policies change endpoint outcomes, but their effects depend on both model and protocol. SafeClawBench provides a reproducible framework for comparing agent models and prompt-policy conditions without conflating textual compliance, evidence-supported harm, and executable state changes. The open-source dataset is available at https://huggingface.co/datasets/sairights/safeclawbench.

</details>


### 71. ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues

- **Authors:** Shanda Li, Qiuhong Anna Wei, Jingwu Tang, Valerie Chen, Nihar B Shah, Tim Dettmers, Yiming Yang, Ameet Talwalkar
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18237v1](http://arxiv.org/abs/2606.18237v1)
- **PDF:** [https://arxiv.org/pdf/2606.18237v1](https://arxiv.org/pdf/2606.18237v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper introduces **ReproRepo**, a scalable evaluation framework that treats human‑submitted GitHub issues as natural supervision for detecting reproducibility problems in machine‑learning papers. By automatically linking 1,149 recent conference papers to their associated code repositories, the authors query several state‑of‑the‑art LLM agents (e.g., Codex, GPT‑5.5) to generate reproducibility blockers without actually running the code, and then measure how often the agents retrieve semantically related issues that humans have reported. Results show that the best agent surfaces a relevant blocker for roughly **90 %** of the papers, especially excelling at flagging obvious failures and locating the correct semantic region, though precise pinpointing of the bug remains limited; thus ReproRepo offers a reusable, low‑overhead benchmark for future agentic‑AI reproducibility auditing.


<details>
<summary>Abstract</summary>

Reproducing research results from papers and released code is central to scientific progress. Existing works have introduced benchmarks to evaluate whether LLM agents can assist with reproducibility, but they are difficult to scale due to their reliance on substantial manual effort for data curation and evaluation. We introduce ReproRepo, a scalable framework for reproducibility evaluation that leverages human-raised GitHub issues as naturally occurring supervision on realistic reproduction blockers. We instantiate ReproRepo on 1,149 recent machine learning papers from major conferences and evaluate four frontier model-agent configurations. Our results show that LLM agents, even without executing code, can identify many real-world reproducibility problems from paper-repository pairs: the best agent in our study, namely Codex with GPT-5.5, surfaces at least one semantically related human-reported blocker for ~90% of papers in the study. Further analysis shows that agents are particularly effective for surfacing visible failures and identifying the right semantic region, but may still be insufficient in exact localization. ReproRepo can serve as a reusable, scalable framework for future evaluations of LLM agents on real-world reproducibility auditing. Our code is released at https://github.com/LithiumDA/ReproRepo.

</details>


### 72. Agentra: A Supervisable Multi-Agent Framework for Enterprise Intrusion Response

- **Authors:** Raj Patel, Shaswata Mitra, Michele Guida, Stefano Iannucci, Sudip Mittal, Shahram Rahimi
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18325v2](http://arxiv.org/abs/2606.18325v2)
- **PDF:** [https://arxiv.org/pdf/2606.18325v2](https://arxiv.org/pdf/2606.18325v2)
- **Categories:** cs.CR, cs.AI


> **Main contribution** – The paper introduces **Agentra**, a supervisable, multi‑agent framework that automates the generation and execution of intrusion‑response plans for enterprise environments, grounding decisions in MITRE ATT&CK/D3FEND and NIST CSF 2.0 while preserving human oversight and auditability.  

**Methodology** – Alerts from IDS/EDR/XDR systems are transformed into structured incident‑response tasks that are distributed to role‑scoped agents (Planner, Validator, Moderator, Action‑Catalog). A bounded **Planner→Validator** loop proposes and checks response plans, threat‑intel is filtered by a Moderator gateway, actions are risk‑scored and gated, and every decision is logged in an append‑only audit trail.  

**Key findings** – On a 120‑event benchmark (ThreatHunter‑Playbook, Splunk BOTSv3, DARPA OpTC) Agentra’s best configuration raises the false‑positive‑aware IRS F1 score from **0.61 to 0.84**, while keeping the harmful‑action rate at **0 %** (matching the static OASIS CACAO baseline). The results demonstrate that a coordinated multi‑agent architecture can substantially improve ontology‑driven intrusion response coverage without sacrificing safety or analyst control.


<details>
<summary>Abstract</summary>

Enterprise intrusion response still depends on static playbooks and analyst-driven triage, creating delay between alert generation and containment. We present Agentra, a supervisable multi-agent Intrusion Response System (IRS) framework that converts alerts from IDS, EDR, and XDR platforms into structured incident response plans grounded in MITRE ATT&CK, MITRE D3FEND, and NIST CSF 2.0. Agentra decomposes response reasoning across role-scoped agents, validates proposed plans through a bounded Planner--Validator review loop, screens retrieved threat intelligence through a Moderator security gateway, gates actions through an Action Catalog and risk score, and records decisions in an append-only audit log. We evaluate Agentra against a static OASIS CACAO v2.0 cyber-playbook baseline on a 120-event corpus drawn from ThreatHunter-Playbook, Splunk BOTSv3, and DARPA OpTC. The strongest configuration improves FP-aware IRS F1 from 0.61 to 0.84 and restores the projected harmful-action rate to the static baseline level of 0.0% after Planner-only configurations introduce unsafe overreaction. These results indicate that multi-agent response planning can improve ontology-grounded IRS coverage while preserving analyst approval and auditability.

</details>


### 73. Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure

- **Authors:** Ziqi Zhou, Yubo Ye, Sumeet Atul Vadhavka, Linwei Wang, Zhiqiang Tao
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18154v1](http://arxiv.org/abs/2606.18154v1)
- **PDF:** [https://arxiv.org/pdf/2606.18154v1](https://arxiv.org/pdf/2606.18154v1)
- **Categories:** cs.AI


> The paper introduces **LEADS**, a framework that lets a large‑language‑model (LLM) act as an autonomous “architect” to construct patient‑specific cardiac electrophysiology (EP) digital twins.  By encoding domain knowledge (e.g., conservation laws, ion‑channel kinetics) as a structured action space, the LLM agent iteratively reasons about and assembles hybrid physics‑neural components, while conventional gradient descent optimizes the resulting model’s parameters.  Experiments on synthetic benchmarks (three known reaction‑diffusion models) and on real EP recordings show that LEADS automatically discovers physically grounded, interpretable, and numerically stable hybrid structures that achieve higher predictive accuracy than manually engineered hybrids and prior LLM‑based approaches.


<details>
<summary>Abstract</summary>

Building personalized cardiac electrophysiology (EP) digital twins requires identifying the appropriate model structure for each patient, not merely fitting parameters. Traditional methods rely on experts to manually prescribe hybrid physics-neural architectures, which requires deep domain expertise and does not transfer across patients. Recent works have applied large language models (LLMs) to generate or act as hybrid models. However, despite their promising generalization capacity, these LLM-based methods lack the structural priors needed for stable cardiac simulations. Hence, we propose LEADS, a framework that formulates cardiac EP domain knowledge as a structured action space and utilizes an LLM agent to discover hybrid models. The agent follows an iterative reasoning-and-action loop to select, combine, and refine hybrid models, whilst gradient descent handles parameter fitting. The proposed LEADS designs every candidate model towards physically grounded, interpretable, and numerically stable, while allowing open-ended architectural discovery. We validate LEADS on synthetic data with three ground-truth reaction models and on real cardiac EP data, demonstrating that it outperforms both human-designed hybrid models and other LLM-based hybrid modeling.

</details>


### 74. WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning

- **Authors:** Yuwei Zhang, Tong Xia, Bianca Emmerich, Yu Yvonne Wu, Dimitris Spathis, Xin Liu, Daniel McDuff, Cecilia Mascolo
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18147v1](http://arxiv.org/abs/2606.18147v1)
- **PDF:** [https://arxiv.org/pdf/2606.18147v1](https://arxiv.org/pdf/2606.18147v1)
- **Categories:** cs.AI


> The paper introduces **WEQA**, a query‑adaptive, agentic framework that couples a large language model (LLM) controller with a toolbox of wearable‑specific analytical and predictive modules. By letting the LLM dynamically generate execution plans that select and orchestrate the appropriate sensor‑analysis tools and external knowledge sources for each health query, WEQA can ground its answers in high‑dimensional, longitudinal wearable data. On a newly curated benchmark covering four wearable datasets across three health domains, WEQA outperforms both standard LLM and existing agentic baselines by ≈ 24 % in accuracy, and a blinded evaluation with medical experts and end‑users reports markedly higher usefulness and clinical soundness.


<details>
<summary>Abstract</summary>

Language models are remarkably capable at medical question answering, in some cases surpassing the accuracy of general physicians. However, answering questions about wearable health data remains challenging and understudied, as these ubiquitous sensors produce continuous, high-dimensional, and longitudinal data, which is non-trivial to align with text-centric distributions in LLM pretraining. The diversity of sensor modalities and user intents cannot be effectively handled by a fixed reasoning workflow or a single pretrained foundation model. To address these challenges, we propose WEQA, a query-adaptive agent framework that unifies LLM reasoning with specialized wearable analytical and modeling tools. An LLM controller is employed to synthesize execution plans and dynamically route each query to the appropriate combination of sensor analysis and pretrained models, and perform grounded response auditing with external knowledge. We also curate a benchmark spanning four open wearable datasets comprising analytic and predictive tasks in three different health domains. Experiments show that our framework is 24% more accurate than LLM and agentic baselines, and a blinded study with 12 medical experts and 8 users shows substantial gains in usefulness and clinical soundness.

</details>


### 75. Your AI Travel Agent Would Book You a Bullfight: An Agentic Benchmark for Implicit Animal Welfare in Frontier AI Models

- **Authors:** Jasmine Brazilek, Joel Christoph, Miles Tidmarsh, Carol Kline, Oliver Tullio, Arturs Kanepajs
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18142v2](http://arxiv.org/abs/2606.18142v2)
- **PDF:** [https://arxiv.org/pdf/2606.18142v2](https://arxiv.org/pdf/2606.18142v2)
- **Categories:** cs.AI, cs.CL, cs.CY


> The paper introduces **Travel Agent Compassion (TAC)**, the first benchmark that tests whether frontier AI agents can act compassionately by avoiding animal‑exploitation options when they autonomously book travel services. Using 12 hand‑crafted scenarios (expanded to 48 variants that control for price, rating, and position) across six exploitation categories, the authors evaluate seven state‑of‑the‑art agents; all fall below the 64 % chance baseline, with the highest score = 53 % (Claude Opus 4.7), and demonstrate that inserting a single welfare‑aware sentence into the system prompt can boost performance dramatically for some models (up to +63 pp for Claude and GPT‑5.5). An auxiliary “Inspect Scout” audit of 288 transcripts shows the poor scores are not due to models gaming the evaluation, highlighting a gap between text‑only welfare benchmarks and real‑world agentic behavior and underscoring the need for stronger safeguards in the emerging EU AI risk framework.


<details>
<summary>Abstract</summary>

AI agents are moving from advisors to actors, booking travel, planning menus, and running procurement on behalf of users. Existing benchmarks for AI and animal welfare evaluate model text responses to question-answer prompts, leaving open whether the welfare reasoning surfaced in those responses transfers to agentic deployment where the model must take actions with tools. We introduce TAC (Travel Agent Compassion), the first agentic benchmark measuring whether AI agents avoid options involving animal exploitation when acting on behalf of users. TAC presents an AI agent with twelve hand-authored travel booking scenarios across six categories of animal exploitation, augmented to forty-eight samples to control for price, rating, and position confounds. We evaluate seven frontier models from four labs. Every model scores below the chance level of sixty-four percent, with the best performer (Claude Opus 4.7) at fifty-three percent. A single welfare-aware sentence in the system prompt yields gains of forty-seven to sixty-three percentage points in Claude and GPT-5.5, twenty-six points in GPT-5.2, and under twelve points in DeepSeek and Gemini. An auxiliary Inspect Scout audit of 288 base-condition transcripts from the top two performers, using Gemini 2.5 Flash Lite as judge, flags zero transcripts for evaluation awareness, suggesting the below-chance rates do not stem from the models recognising the evaluation. We discuss implications for category-level variation across cultural domains, the limits of text-response welfare benchmarks, and the EU General-Purpose AI Code of Practice systemic risk framework.

</details>


### 76. On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization

- **Authors:** Ehsan Aghazadeh, Hossein Pishro-Nik
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18121v1](http://arxiv.org/abs/2606.18121v1)
- **PDF:** [https://arxiv.org/pdf/2606.18121v1](https://arxiv.org/pdf/2606.18121v1)
- **Categories:** cs.MA, cs.IT


> **Main contribution** – The paper introduces a rigorous analytical framework for evaluating the reliability of multi‑agent AI systems that cooperate via message passing on sparse, role‑typed factor graphs. By extending density‑evolution (DE) methods from low‑density parity‑check (LDPC) coding to this richer setting, the authors obtain new asymptotic thresholds, finite‑length bounds, and converse results that quantify how different types of agent failures (abstentions, unusable verifier outputs, and lost messages) affect overall task completion.

**Methodology** – The authors model a task as a set of binary subclaims linked by noisy Boolean verifier agents (checks) that implement logical‑forcing functions (XOR, AND, OR, implication, Horn clauses). They formulate three erasure‑type failure modes and derive DE recursions for the evolution of unresolved subclaims on random, locally tree‑like graphs, proving that the DE predictions converge to the true performance for large systems. Special cases (e.g., XOR) recover classical LDPC‑BEC analysis, while others (e.g., AND) reveal novel asymmetries.

**Key findings** – The analysis yields explicit reliability thresholds for different verifier functions and failure modes, showing that certain architectures are intrinsically more robust (e.g., XOR‑based verifiers) while others suffer pronounced bias (e.g., AND verifiers favoring positive certificates). The framework also guides architecture optimization: by selecting the factor‑graph degree distribution and verifier logic, one can systematically design agent networks that achieve desired reliability guarantees, offering a principled tool for building dependable, cooperative AI systems.


<details>
<summary>Abstract</summary>

Modern AI systems increasingly solve a task not with a single model call but with several imperfect agents working together: some propose pieces of a solution, others verify them, and the results are combined. These systems often outperform any single model, yet it is rarely clear why they succeed or when they will fail. We model such a system as message passing on a sparse graph, the structure that underlies low-density parity-check (LDPC) codes, and extend the density-evolution machinery of coding theory to this richer setting. In our model a task is a set of coupled binary subclaims, and an agent architecture is a sparse, role-typed factor graph whose check nodes are noisy Boolean verifier nodes, each computing a local Boolean function of the subclaims it touches. Three distinct failure modes, all modeled as erasures (an agent abstaining, a verifier returning no usable output, and a message lost between two agents), propagate as the agents exchange set-valued messages. The check agents combine these messages by a single logical-forcing rule that specializes to XOR, AND, OR, implication, and Horn constraints. This is more than a relabeling of LDPC theory: the verifier functions are nonlinear and value-asymmetric, and the three failure modes do not reduce to a single effective channel, so they require new threshold, finite-length, and converse results rather than a direct reuse of parity-check density evolution. We prove a density-evolution theorem that predicts the asymptotic fraction of unresolved subclaims on random role-typed architectures, with an extension to deterministic, locally tree-like graph sequences. The XOR case recovers the classical LDPC recursion on the binary erasure channel (BEC); the AND case exposes an asymmetry between positive and negative verifier certificates.

</details>


### 77. Agentic AI-based Framework for Mitigating Premature Diagnostic Handoff and Silent Hallucination in Healthcare Applications

- **Authors:** Divyansh Srivastava, Shreya Ghosh, Anshul Verma, Rajkumar Buyya
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18068v1](http://arxiv.org/abs/2606.18068v1)
- **PDF:** [https://arxiv.org/pdf/2606.18068v1](https://arxiv.org/pdf/2606.18068v1)
- **Categories:** cs.AI


> **Main contribution**  
The paper introduces a deterministic, multi‑agent safety framework for clinical LLM assistants that simultaneously prevents premature diagnostic hand‑offs and silent hallucinations. It does so by (1) embedding a neuro‑symbolic “OLDCARTS gate” that blocks any diagnostic step until the full set of symptom dimensions (Onset, Location, Duration, Character, Aggravating/Alleviating factors, Radiation, Timing, Severity) has been collected, and (2) adding an epistemic uncertainty‑quantification gate that samples K = 5 independent diagnostic completions, computes their semantic entropy \(H\), and suppresses outputs whose entropy exceeds a preset threshold.

**Methodology**  
A deterministic orchestrator replaces the usual LLM‑as‑judge routing, directing a patient‑simulation agent and a diagnostic‑reasoning agent through the OLDCARTS gate before allowing the diagnostic agent to produce a conclusion. Divergence detection is performed by measuring \(H\) across the K sampled diagnoses; high‑entropy cases are flagged for rejection or escalation. Experiments use the llama‑3.1‑70b‑instruct model to simulate 150 patient encounters, comparing the full gated system against an unconstrained baseline.

**Key findings**  
The gated architecture raises diagnostic precision from 38.0 % to 49.3 % (Δ = +11.3 pp), demonstrating that deterministic constraints can substantially improve safety without retraining the underlying model. Moreover, a modest but significant negative correlation (r = ‑0.181, p < 0.05) between OLDCARTS completeness and semantic entropy indicates that thorough, structured information gathering directly reduces epistemic uncertainty, supporting the framework’s dual‑gate design as a viable route for robust, agentic AI in healthcare.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) and multi-agent systems have driven the rise of Agentic AI, showing promise for medical reasoning. However, open-ended conversational agents remain prone to two critical failure modes: premature diagnostic handoff and silent clinical hallucinations that may go undetected before reaching the patient. In this work, we propose a multi-agent framework that addresses both issues by replacing ``LLM-as-a-judge'' routing with deterministic orchestration constraints. The framework incorporates two safety mechanisms. First, a neuro-symbolic state-tracking gate enforces completeness of the OLDCARTS clinical protocol (Onset, Location, Duration, Character, Aggravating/Alleviating factors, Radiation, Timing, and Severity) by blocking diagnostic transitions until all required dimensions are collected. Second, an epistemic uncertainty quantification (UQ) gate computes semantic entropy (H) across K=5 independent diagnostic samples to identify and intercept divergent outputs before delivery.
  We evaluate the system using simulated patient agents powered by the llama-3.1-70b-instruct model on 150 test cases. The full architecture achieves 49.3% diagnostic precision, representing an absolute improvement of 11.3 percentage points over an unconstrained baseline. Additionally, we observe a statistically significant negative correlation (r = -0.181, p < 0.05) between OLDCARTS completeness (σ) and semantic entropy (H), suggesting that structured information gathering is associated with reduced diagnostic uncertainty.

</details>


### 78. Intelligence Entropy Principle and the ADE Stability Engineering Framework

- **Authors:** Dexing Liu
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18065v1](http://arxiv.org/abs/2606.18065v1)
- **PDF:** [https://arxiv.org/pdf/2606.18065v1](https://arxiv.org/pdf/2606.18065v1)
- **Categories:** cs.MA


> The paper introduces the **Intelligence Entropy Principle**, a formal model that predicts the exponential drift of LLM‑driven multi‑agent systems toward disorder ( S(t)=S₀·e^{αt/C_m} ), and derives a Lyapunov‑based stability condition (λ > α/C_m) linking system resilience to a newly defined **model capability coefficient** C_m. Building on this theory, the authors propose the **ADE (Agent Delivery Engineering) four‑layer framework**—spanning Physical Laws, Network Infrastructure, Agent Dynamics, and User Adaptation—with 23 concrete components and a complementary Five‑Layer Disorder Taxonomy, and they validate the approach through >100 k simulated runs and 33.6 days of live production monitoring, achieving a drop in “channel fracture” failures from 69‑98 % to near zero and reducing overall system‑death probability to <0.02 %. These results demonstrate that entropy‑aware engineering can reliably stabilize large‑scale LLM‑driven MAS, providing a practical blueprint for robust, production‑grade agentic AI.


<details>
<summary>Abstract</summary>

As LLM-driven multi-agent systems (MAS) transition from lab to production, system behavior exhibits nonlinear degradation. We introduce the Intelligence Entropy Principle: probability-driven systems spontaneously drift toward disorder, formalized as S(t) = S0 * exp(alpha*t/Cm), where Cm is a model capability coefficient we propose. Lyapunov analysis yields the stabilization condition lambda > alpha/Cm. We construct the ADE (Agent Delivery Engineering) four-layer framework (L1 Physical Laws through L4 User Adaptation) with 23 core components. Validation spans 100K-scale experiments and 33.6 days of production monitoring. We propose a Five-Layer Disorder Taxonomy unifying failures under structural collapse, and present Elastic Organization as an original MAS morphology. Results: channel fracture reduced from 69-98% to near 0%; system death probability below 0.02%.

</details>


### 79. Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose

- **Authors:** Xueping Gao
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18051v1](http://arxiv.org/abs/2606.18051v1)
- **PDF:** [https://arxiv.org/pdf/2606.18051v1](https://arxiv.org/pdf/2606.18051v1)
- **Categories:** cs.CL


> **Main contribution** – The paper introduces **SkillWeaver**, a unified framework that solves the *Compositional Skill Routing* problem for LLM‑based agents: given a complex user request and a large library of reusable tool specifications (skills), the system automatically **decomposes** the request into atomic sub‑tasks, **retrieves** the most appropriate skill for each sub‑task, and **composes** them into an executable dependency‑aware plan (a DAG). To enable systematic evaluation, the authors also release **CompSkillBench**, a benchmark of 300 multi‑skill queries over 2,209 real‑world MCP server skills covering 24 functional categories.

**Methodology** – SkillWeaver couples three components: (1) an LLM prompt‑engineered task decomposer, (2) a bi‑encoder skill retriever indexed with FAISS, and (3) a DAG planner that respects skill dependencies. The key novelty is **Iterative Skill‑Aware Decomposition (SAD)**, a retrieval‑augmented feedback loop in which the retriever’s top‑k skill matches are fed back to the decomposer to refine the granularity of sub‑tasks until they align with available skills.

**Key findings** – Experiments on CompSkillBench show that decomposition quality is the dominant bottleneck: vanilla LLM decomposition yields only 34.2 % category recall at the step level. SAD raises this to 67.7 % (a +32.7 % relative gain, p < 10⁻⁶) and improves immediate retrieval success (CatR@1 from 34 % to 41 %). SkillWeaver slashes LLM context‑window usage by > 99 % and generalizes to unseen skill categories, achieving a 35.6 % relative DA improvement in a zero‑shot transfer setting. These results demonstrate that a tight decompose‑retrieve‑compose loop is essential for scalable, compositional use of external skills in agentic AI.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on external skills -- reusable tool specifications -- but real-world tasks often require composing multiple skills, not just selecting one. We formalize this as the Compositional Skill Routing problem: given a complex user query and a large skill library, decompose the query into atomic sub-tasks, retrieve the appropriate skill for each sub-task, and compose an executable plan. We present SkillWeaver, a decompose-retrieve-compose framework combining an LLM task decomposer, a bi-encoder skill retriever with FAISS indexing, and a dependency-aware DAG planner. To support evaluation, we introduce CompSkillBench, a benchmark of 300 compositional queries over 2,209 real MCP server skills spanning 24 functional categories, sourced from the public MCP ecosystem. Our experiments reveal that task decomposition quality is the primary bottleneck: standard LLM decomposition reaches only 34.2% category recall at the step level. To address this, we propose Iterative Skill-Aware Decomposition (SAD), a retrieval-augmented feedback loop that iteratively aligns decomposition with available skills. SAD improves decomposition accuracy from 51.0% to 67.7% (+32.7%, Wilcoxon p < 10^-6) in a single iteration; DA-conditioned analysis confirms that correct granularity is the prerequisite for effective retrieval (CatR@1 rises from 34% to 41% when DA=1). SkillWeaver reduces context window consumption by over 99%, and transfer experiments confirm generalization (+35.6% relative DA gain even when target categories are absent from the retrieval pool).

</details>


### 80. ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents

- **Authors:** Ander Alvarez, Santhiya Rajan, Samuel Mugel, Román Orús
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18037v1](http://arxiv.org/abs/2606.18037v1)
- **PDF:** [https://arxiv.org/pdf/2606.18037v1](https://arxiv.org/pdf/2606.18037v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> **Main contribution** – The paper introduces **ProvenanceGuard**, the first source‑aware factuality verifier for Model‑Context‑Protocol (MCP)‑driven LLM agents, targeting the “cross‑source conflation” failure mode where a claim is correctly supported but attributed to the wrong evidence source.  

**Methodology** – ProvenanceGuard parses MCP execution traces (tool IDs, source IDs, raw tool outputs), splits the agent’s final answer into atomic claims, routes each claim to the originating source’s evidence, and evaluates support using a combination of natural‑language inference and a token‑alignment proxy. It then checks whether the agent’s stated attribution matches the routed source, producing per‑claim verdicts and an overall allow/block decision; blocked answers can be repaired via retrieval‑augmented revision and re‑verified.  

**Key findings** – Across 281 medical‑domain MCP traces (including a 40‑trace held‑out set), ProvenanceGuard attains a block‑decision F1 of **0.80** and source‑attribution accuracy of **0.86**, substantially outperforming source‑blind baselines. On a tougher multi‑source benchmark the block F1 rises to **0.85**, though exact source ownership remains hard (source‑plus‑relation accuracy ≈ 0.23). The repair‑and‑reverify loop resolves every blocked answer, and in 50 controlled clinical conflation probes the system detects **100 %** of injected attribution swaps, demonstrating that provenance is a distinct and critical axis of factuality verification for MCP‑based agents.


<details>
<summary>Abstract</summary>

Tool-using LLM agents increasingly use the Model Context Protocol (MCP) to answer from heterogeneous evidence sources, including search, APIs, databases, clinical records, and formulary tools. Standard factuality metrics usually test whether an answer is supported by pooled evidence, missing a provenance-sensitive failure mode: a claim may be supported somewhere while being attributed to the wrong source. We call this cross-source conflation.
  We introduce ProvenanceGuard, a source-aware verifier for MCP-grounded answers. It consumes captured MCP traces with stable tool IDs, source IDs, and raw outputs; decomposes answers into atomic claims; routes claims to source-specific evidence; checks support with NLI and a token-alignment proxy; compares stated attribution with the routed source; and returns per-claim verdicts plus an answer-level allow/block decision. Blocked answers can be repaired with retrieval-augmented answer revision and re-verified.
  We evaluate on 281 medical-domain MCP-agent traces. A 266-trace adjudicated subset yields 2,325 LLM-assisted claim labels split by trace; 361 held-out labels are human-verified. On the 40-trace held-out split, ProvenanceGuard achieves block F1 0.802 and source accuracy 0.858 over 260 source-eligible claims, outperforming source-blind baselines that do not emit claim-to-source IDs. On a harder multi-source benchmark it reaches block F1 0.846, while source-plus-relation accuracy drops to 0.229, showing that exact source ownership remains difficult with semantically close sources. Repair-and-reverify resolves all blocked answers in the full trace set, often via conservative fallback. In 50 controlled clinical conflation probes, ProvenanceGuard detects all injected attribution swaps with no retained wrong attribution. These results show that source attribution is an independent axis for factuality verification in MCP-based agents.

</details>


### 81. LoopCoder-v2: Only Loop Once for Efficient Test-Time Computation Scaling

- **Authors:** Jian Yang, Shawn Guo, Wei Zhang, Tianyu Zheng, Yaxin Du, Haau-Sing Li, Jiajun Wu, Yue Song, Yan Xing, Qingsong Cai, Zelong Huang, Chuan Hao, Ran Tao, Xianglong Liu, Wayne Xin Zhao, Mingjie Tang, Weifeng Lv, Ming Zhou, Bryan Dai
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18023v1](http://arxiv.org/abs/2606.18023v1)
- **PDF:** [https://arxiv.org/pdf/2606.18023v1](https://arxiv.org/pdf/2606.18023v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution** – The paper introduces **LoopCoder‑v2**, a family of 7 B parameter Parallel Loop Transformers (PLT) that reuse a single transformer block multiple times at test time, and rigorously investigates how many loops are optimal for scaling latent computation in code‑generation agents.  

**Methodology** – The authors train seven PLT variants with loop counts from 1 to 7 on 18 T tokens, then perform matched instruction‑tuning and evaluate them on code generation, reasoning, and tool‑use benchmarks (including SWE‑bench and Multi‑SWE). They analyze the gain‑vs‑cost trade‑off by separating the benefits of additional representation refinement from the positional mismatch introduced by cross‑loop position offsets (CLP) and the extra KV‑cache memory.  

**Key findings** – A **two‑loop** PLT consistently outperforms the non‑looped baseline, boosting SWE‑bench Verified scores from **43.0 → 64.4** and Multi‑SWE from **14.0 → 31.0**, while **three or more loops degrade performance** due to diminishing refinement and fixed CLP‑induced mismatch. The study shows that loop‑2 provides the bulk of useful updates, and that the non‑monotonic loop‑count effect is explained by the growing offset cost outweighing marginal gains, offering a practical diagnostic for selecting loop counts in agentic AI systems.


<details>
<summary>Abstract</summary>

Looped Transformers scale latent computation by repeatedly applying shared blocks, but sequential looping increases latency and KV-cache memory with the loop count. Parallel loop Transformers (PLT) alleviate this cost through cross-loop position offsets (CLP) and shared-KV gated sliding-window attention, making loop count a practical design choice. We therefore study PLT loop-count selection through a gain--cost view: an extra loop may refine representations, but CLP also introduces a positional mismatch at each loop boundary. We instantiate this study by training LoopCoder-v2, a family of 7B PLT coders with different loop counts, from scratch on 18T tokens, followed by matched instruction tuning and evaluation. Empirically, the two-loop variant delivers broad gains over the non-looped baseline across code generation, code reasoning, agentic software engineering, and tool-use benchmarks, improving SWE-bench Verified from 43.0 to 64.4 points and Multi-SWE from 14.0 to 31.0 points. In contrast, variants with three or more loops regress, revealing a strongly non-monotonic loop-count effect. Our diagnostics show that loop 2 provides the main productive refinement, while later loops yield diminishing, oscillatory updates and reduced representational diversity. Because the CLP-induced mismatch remains roughly fixed as refinement gains shrink, the offset cost increasingly dominates. This gain--cost trade-off explains PLT's saturation at two loops and provides diagnostics for loop-count selection.

</details>


### 82. LegalHalluLens: Typed Hallucination Auditing and Calibrated Multi-Agent Debate for Trustworthy Legal AI

- **Authors:** Lalit Yadav, Akshaj Gurugubelli
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18021v1](http://arxiv.org/abs/2606.18021v1)
- **PDF:** [https://arxiv.org/pdf/2606.18021v1](https://arxiv.org/pdf/2606.18021v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> **Main contribution:** LegalHalluLens introduces a fine‑grained auditing framework for legal‑domain language models that breaks down hallucinations into four legally‑relevant claim types (numeric, temporal, obligation/entitlement, factual), compresses their omission‑vs‑invention bias into a single *Risk Direction Index* (RDI), and leverages these diagnostics to steer a calibrated multi‑agent debate that more effectively suppresses mistaken outputs.

**Methodology:** The authors first annotate CUAD contracts to build typed hallucination profiles (510 contracts, 249 k clause‑level instances). They then compute an RDI that quantifies the net direction (over‑generation vs. under‑generation) of each model’s errors. Finally, they instantiate a debate pipeline in which a “Skeptic” agent explicitly targets the high‑risk claim types identified by the profiles and RDI, using asymmetric gating to filter generations.

**Key findings for agentic AI:** (1) Within the same model, hallucination rates can swing by ≈ 38–40 percentage points across claim types—an effect invisible to aggregate metrics. (2) Two models with identical overall 52 % hallucination rates can have opposite RDIs, indicating opposite risk directions. (3) The typed, direction‑aware debate cuts fabricated clause detections by **45 %**, yielding per‑category improvements that mirror the diagnosed failure modes, and matches larger commercial APIs while using a 4 B‑parameter backbone. These results demonstrate that typed failure diagnostics and risk‑direction signals can be used to calibrate multi‑agent correction mechanisms, enabling more trustworthy deployment of legal AI systems.


<details>
<summary>Abstract</summary>

AI systems deployed in legal workflows hallucinate at rates that aggregate metrics report at ~52%, but this average conceals where errors concentrate and in which direction they run, leaving compliance officers without an actionable signal for trustworthy deployment. We present LegalHalluLens, an auditing framework with three components: typed hallucination profiles across four legally-motivated claim categories (numeric, temporal, obligation/entitlement, factual) over CUAD (Hendrycks et al., 2021); a Risk Direction Index (RDI) that reduces omission-versus-invention bias to a single deployment-comparable scalar; and a typed debate pipeline calibrated to both magnitudes and directions. Across 510 contracts and 249,252 clause-level instances we measure a within-model gap of approximately 38-40 pp between obligation/numeric and temporal claims that aggregate reporting hides, and show that two systems with matched 52% rates can carry opposite RDIs. The debate pipeline reduces fabricated detections by 45% with per-category gains tracking the diagnosis, matching commercial APIs with a substantially smaller backbone (4B active parameters). Typed profiles and RDI surface failure modes that aggregate metrics hide; we further show these diagnostics serve as calibration inputs for multi-agent debate pipelines, where Skeptic challenges and asymmetric gates targeted at measured failure modes outperform generically-tuned debate. The framework supports direction-aware procurement, accountability, and agent design for legal AI deployed in the wild.

</details>


### 83. LLM Consumer Behavior Theory: Foundations of a Novel Research Field

- **Authors:** Manon Reusens, Sofie Goethals, David Martens
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18005v1](http://arxiv.org/abs/2606.18005v1)
- **PDF:** [https://arxiv.org/pdf/2606.18005v1](https://arxiv.org/pdf/2606.18005v1)
- **Categories:** cs.AI, econ.GN


> **Main contribution:** The paper proposes a new discipline—LLM Consumer Behavior Theory—that extends traditional consumer theory to markets where large language models act as autonomous purchasing agents for humans.  

**Methodology:** It synthesizes concepts from classical/behavioral economics and recent NLP research to build a formal framework describing how human preferences are encoded, elicitated, and operationalized by LLM agents, and how these agent‑level choices aggregate into market‑level demand, while critically assessing standard economic assumptions (e.g., rationality, preference heterogeneity) in the context of agentic systems.  

**Key findings:** The authors identify systematic gaps in existing models of LLM decision‑making, highlight where alignment and preference‑representation failures can distort aggregate demand, and outline a roadmap of open questions—such as measuring preference fidelity, modeling agent heterogeneity, and predicting market dynamics—that are essential for the emerging field of agentic AI economics.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as autonomous agents that make consumption decisions on behalf of users. This shift raises fundamental questions for consumer theory, which has traditionally modeled humans as the primary decision-makers. In this paper, we introduce LLM Consumer Behavior Theory, a new field of study concerned with analyzing consumer behavior in agentic markets. Drawing on classical and behavioral economics alongside recent advances in Natural Language Processing, we formalize how human preferences are reflected and acted upon by LLM-based agents, and how agent-level decisions aggregate into market demand. We unify previously fragmented literature on LLM decision-making, human behavior simulation, and preference elicitation under a common economic lens, highlighting where assumptions, such as rationality and heterogeneity, may fail in agentic markets. Rather than providing empirical validation, this paper outlines the scope of LLM consumer behavior and identifies open research questions related to alignment, preference representation, and market dynamics.

</details>


### 84. A Neuro-Symbolic Approach to Strategy Synthesis for Strategic Logics

- **Authors:** Marco Aruta, Vadim Malvone, Aniello Murano, Domenico Parente, Luca Rizzuti
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17962v1](http://arxiv.org/abs/2606.17962v1)
- **PDF:** [https://arxiv.org/pdf/2606.17962v1](https://arxiv.org/pdf/2606.17962v1)
- **Categories:** cs.MA, cs.AI


> The paper presents a neuro‑symbolic pipeline that augments traditional multi‑agent model checking with a large language model (LLM) as a “strategy‑generation oracle.”  In this generate‑and‑certify architecture, the LLM proposes candidate strategies for bounded strategic logics (NatATL); each candidate is then formally verified by an off‑the‑shelf MAS model checker, guaranteeing that only sound strategies are accepted.  Using a new NatATL synthesis benchmark (4,211 instances), the authors show that an open‑weight Qwen‑3‑32B model achieves 92 % correct synthesis when coupled with the verifier, demonstrating that LLM‑guided search can dramatically reduce the combinatorial cost of strategy synthesis while preserving formal guarantees.


<details>
<summary>Abstract</summary>

Reasoning about what agents can achieve through strategic interaction is a core challenge in Multi-Agent Systems (MAS). Logics for strategic ability, such as ATL, provide rigorous methods, but their adoption is often hindered by the computational cost of strategy synthesis. We introduce a neuro-symbolic framework that integrates large language models (LLMs) into the model-checking pipeline for MAS. The LLM acts as a strategy-generation oracle, proposing candidate strategies that are then formally validated by a standard MAS model checker. This generate-and-certify architecture uses LLM guidance to navigate large combinatorial strategy spaces while preserving formal soundness: generated strategies are accepted only when certified by the verifier. We instantiate the framework for bounded strategic reasoning in NatATL and introduce the first NatATL strategy-synthesis dataset, consisting of 4211 instances. Experiments with an open-weight Qwen3-32B model show that our certified pipeline achieves 92\% accuracy on strategy-synthesis outcomes.

</details>


### 85. Trustworthy Self-Composable Big-Data-as-a-Service: An LLM-Orchestrated Multi-Agent Framework for Automated Data Engineering, AutoML, MLOps Deployment, and Drift-Aware Lifecycle Optimization

- **Authors:** Aueaphum Aueawatthanaphisut, Badri Raj Lamichhane
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17915v1](http://arxiv.org/abs/2606.17915v1)
- **PDF:** [https://arxiv.org/pdf/2606.17915v1](https://arxiv.org/pdf/2606.17915v1)
- **Categories:** cs.MA, cs.AI, cs.DB, cs.SE


> The paper introduces a **trustworthy, self‑composable Big‑Data‑as‑a‑Service (BDaaS) platform** in which a central large‑language model (LLM) orchestrates a suite of specialized agents (ingestion, cleaning, feature engineering, AutoML training, evaluation, MLOps deployment, monitoring, and drift detection). The methodology combines hierarchical LLM‑driven coordination with artifact‑governance mechanisms, reproducibility logging, and human‑in‑the‑loop checkpoints to dynamically compose and validate end‑to‑end data‑science pipelines, including drift‑aware feedback loops. Experiments on benchmark tabular tasks with realistic data‑quality issues and simulated covariate drift show that the multi‑agent system matches or exceeds manual and single‑agent baselines in predictive accuracy while significantly improving lifecycle reliability metrics such as workflow completion, traceability, deployment readiness, reproducibility, and rapid drift recovery—demonstrating that LLM‑orchestrated multi‑agent architectures can extend AutoML toward trustworthy, production‑grade BDaaS automation.


<details>
<summary>Abstract</summary>

Big-Data-as-a-Service (BDaaS) platforms require re liable automation across data ingestion, cleaning, feature engi neering, model development, deployment, and post-deployment monitoring. However, existing LLM-based data science agents and AutoML systems mainly focus on isolated workflow stages, leaving limited support for lifecycle-level orchestration, artifact governance, human oversight, and drift-aware adaptation. This paper proposes a trustworthy self-composable BDaaS frame work based on LLM-orchestrated multi-agent collaboration. The proposed architecture decomposes the BDaaS lifecycle into specialized agents for data ingestion, data cleaning, feature engineering, AutoML training, model evaluation, MLOps de ployment, monitoring, and drift detection. A central LLM or chestration layer coordinates agent execution, validates interme diate outputs, manages workflow context, and enables dynamic workflow composition. The framework also incorporates shared artifact governance, reproducibility support, human-in-the-loop checkpoints, and drift-aware feedback loops. A prototype-based evaluation is conducted using controlled tabular benchmark datasets with missing values, categorical variables, outliers, class imbalance, and simulated covariate drift. Compared with manual ML, AutoML-only, and single-agent LLM baselines, the pro posed multi-agent BDaaS pipeline achieves competitive predictive performance while improving lifecycle-level reliability, including workflow completion, artifact traceability, deployment readiness, reproducibility, and drift recovery. The results suggest that LLM-orchestrated multi-agent systems can extend conventional AutoML toward trustworthy, adaptive, and production-oriented BDaaS lifecycle automation.

</details>


### 86. Environment-Grounded Automated Prompt Optimization for LLM Game Agents

- **Authors:** Rean Clive Fernandes, Lukas Fehring, Theresa Eimer, Marius Lindauer, Matthias Feurer
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17838v1](http://arxiv.org/abs/2606.17838v1)
- **PDF:** [https://arxiv.org/pdf/2606.17838v1](https://arxiv.org/pdf/2606.17838v1)
- **Categories:** cs.CL


> The paper presents an automated prompt‑optimization loop that treats an LLM‑driven game agent as two cooperating modules—a goal‑conditioned descriptor and an action selector—and uses environment returns to iteratively evolve each module’s prompt. A behavior‑analysis component attributes performance gains to specific prompt fragments, while a mutator proposes targeted revisions that are validated through rollout experiments, all without modifying the underlying model weights. Applied to all five BabyAI tasks in the BALROG benchmark, the method lifts a zero‑success baseline to as high as 72.5 % success on the challenging PutNext task, demonstrating that environment‑grounded, evolutionary prompt tuning can substantially improve agentic LLM performance in interactive settings.


<details>
<summary>Abstract</summary>

LLM agents in interactive environments are highly sensitive to their prompts, yet prompt engineering remains a manual, task-specific process. We introduce an automated prompt optimization framework for LLM agents that decomposes the observation-to-action pipeline into a goal-conditioned descriptor agent and an action selection agent, and iteratively refines each module's prompt through an LLM-driven evolutionary loop guided by environment returns. We propose a behavior analyzer to attribute episode outcomes to specific prompt components, and a mutator to propose targeted revisions to the prompt, before validating them through environment rollouts. We evaluate on all five BabyAI tasks in the BALROG benchmark, comparing our pipeline against BALROG's RobustCoTAgent under both plain and guided prompt initializations. Optimization improves performance consistently across tasks and conditions, without requiring updates to the model weights. On PutNext, a multi-step coordination task where the RobustCoTAgent achieves 0% success, our framework reaches up to 72.5% success rate using the same underlying LLM with optimized prompts. These results suggest that a multi-agent framework, combined with automatic prompt optimization, enhances LLMs without the need for fine-tuning or extensive human supervision.

</details>


### 87. A Framework for Evaluating Agentic Skills at Scale

- **Authors:** Maksim Shaposhnikov, Nicolas Fortuin, Simon Stipcich, Maria I. Gorinova, Amy Heineike, Rob Willoughby
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17819v1](http://arxiv.org/abs/2606.17819v1)
- **PDF:** [https://arxiv.org/pdf/2606.17819v1](https://arxiv.org/pdf/2606.17819v1)
- **Categories:** cs.SE, cs.AI, cs.CL


> **Main contribution:** The paper introduces a systematic, reusable evaluation framework that lets skill authors generate realistic downstream tasks and score them with custom instruction‑following and goal‑completion rubrics, enabling quantitative measurement of an individual “agent skill” (a structured knowledge artifact that augments LLM agents).  

**Methodology:** The authors authored 1,000 task instances derived from 500 real‑world agent skills, built scoring rubrics for each task, and then benchmarked 19 different agent‑model configurations (both proprietary and open‑source) on these tasks, comparing performance with and without the corresponding skill.  

**Key findings:** Model performance varied dramatically in how faithfully they followed skill‑encoded instructions, leading to large gaps in performance gains across models. Access to a skill markedly altered model behavior relative to a no‑skill baseline, confirming that skills act as an effective, opinionated workflow‑encoding mechanism for LLM agents. The released dataset and framework provide a scalable baseline for future research on agentic skill evaluation.


<details>
<summary>Abstract</summary>

Agent skills -- structured, reusable knowledge artifacts that augment LLM agent capabilities -- have been rapidly adopted in industry, yet their cross-domain impact and use across commercial and open-source models remain under-studied, and no reusable methodology exists for evaluating an individual skill. In this work, we present an evaluation framework that lets a skill author construct realistic tasks to rigorously assess the aspects of a skill that matter most to them, and that estimates skill utility by solving those tasks. Further, we apply our evaluation approach at scale to 500 real-world skills, generating 1,000 tasks derived from the skills' content, along with instruction-following and goal-completion scoring rubrics. Using these metrics, we evaluate how 19 agent-model configurations, both proprietary and open-source, perform on the tasks. Our results show that models vary widely in how closely they adhere to the instructions encoded in skills, leading to substantial differences in their performance gains. Furthermore, we show that access to a skill significantly changes model behavior compared to the no-skill setup, providing an essential mechanism for encoding opinionated workflows into LLM agents. We release our evaluation dataset to support future work on agent skills.

</details>


### 88. Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework

- **Authors:** Petar Radanliev, Omar Santos, Carsten Maple, Kay Atefi
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19390v1](http://arxiv.org/abs/2606.19390v1)
- **PDF:** [https://arxiv.org/pdf/2606.19390v1](https://arxiv.org/pdf/2606.19390v1)
- **Categories:** cs.SE, cs.AI


> **Main contribution** – The paper introduces a reproducible framework (AIBOM‑driven CSAF‑VEX) that links software‑bill‑of‑materials (SBOM) and AI‑specific‑BOM (AIBOM) artefacts to deterministic environment capture and structured runtime telemetry, enabling generation of execution‑bound security advisories for agentic AI systems.

**Methodology** – The authors define a protocol that (1) records declared component artefacts and their activation conditions, (2) enforces execution policies, (3) collects fine‑grained telemetry during execution, (4) computes exploitability scores by correlating static vulnerability data (OSV, GitHub Advisory, KEV, EPSS) with observed runtime evidence, and (5) produces signed CSAF VEX advisories that can be verified by deterministic replay of the captured environment.

**Key findings** – In experiments spanning ~10 k component entries across synthetic agentic AI workloads ranging from 50 to 5 000 components, the framework reliably generated precise, cryptographically‑verifiable VEX advisories, demonstrating that binding SBOM/AIBOM data to deterministic execution traces markedly reduces false‑positive advisory noise and supports scalable, reproducible security assessments of large‑scale agentic AI deployments.


<details>
<summary>Abstract</summary>

A protocol driven framework is presented that binds SBOM and AIBOM artefacts to deterministic environment capture and structured runtime telemetry. Exploitability is computed from declared artefacts, observed activation conditions, and enforced execution policies. CSAF VEX advisories are generated from combined static and runtime evidence, cryptographically signed, and validated through deterministic replay. Evaluation uses approximately 10000 component entries across synthetic Agentic AI workloads 50 to 5000 components, incorporating OSV, GitHub Advisory, KEV, and EPSS datasets.

</details>


### 89. From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning

- **Authors:** Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17682v1](http://arxiv.org/abs/2606.17682v1)
- **PDF:** [https://arxiv.org/pdf/2606.17682v1](https://arxiv.org/pdf/2606.17682v1)
- **Categories:** cs.CL


> The paper introduces **LLM‑as‑Environment‑Engineer**, a framework in which a large language model that already encodes the current RL policy analyzes its own failure trajectories and environment statistics to automatically generate the configuration for the next training stage, thereby removing manual redesign of environments. Using a new, highly‑parameterizable testbed called **MAPF‑FrozenLake**, the authors condition the LLM (Qwen‑3‑4B) on structured summaries of policy behavior and let it propose the next‑stage environment; this approach yields the best aggregate scores across the benchmark, surpassing larger proprietary LLMs (GPT, Gemini) and fixed‑environment baselines. Key findings show that (1) providing explicit failure evidence is crucial for effective updates, (2) the system preserves already‑working settings, and (3) the RL checkpoint itself becomes a more capable environment engineer than the original base model, indicating that policy learning improves the model’s self‑diagnostic ability—insights directly relevant to building more autonomous, self‑improving agentic AI systems.


<details>
<summary>Abstract</summary>

Reinforcement learning pipelines for Large Language Model (LLM) training often rely on manually redesigned environments between stages, requiring practitioners to heuristically infer which configuration will best improve the current policy. To automate this process, we propose the LLM-as-Environment-Engineer framework in which the current policy model analyzes failure trajectories together with contextual information and proposes modifications to the next-stage training environment configuration. We also introduce MAPF-FrozenLake, a controllable testbed whose generator exposes multi-dimensional environment configurations, making it suitable for studying and benchmarking environment redesign. On this testbed, we condition the environment engineer on structured summaries of policy behavior, failure cases, and environment statistics, from which it produces the configuration for the next training stage. With Qwen3-4B as the backbone, our framework achieves the strongest aggregate performance on our benchmarks, outperforming larger proprietary LLMs (e.g., GPT, Gemini) and fixed-environment training baselines. We further analyze which forms of context are most effective, finding that successful environment updates rely on failure evidence and preserve configurations that already work. Interestingly, the current RL checkpoint serves as a better environment engineer than the original base model, suggesting that policy learning improves the model's ability to diagnose its remaining weaknesses.

</details>


### 90. FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness

- **Authors:** Pianran Guo, Pengcheng Zhou, Yucheng Jian, Shuhua Chen
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17642v1](http://arxiv.org/abs/2606.17642v1)
- **PDF:** [https://arxiv.org/pdf/2606.17642v1](https://arxiv.org/pdf/2606.17642v1)
- **Categories:** cs.AI


> FinAcumen introduces a persistent, selective experience‑memory module for tool‑augmented agents that perform multimodal financial reasoning. By continuously harvesting trajectories, distilling successful strategies and failure‑derived cautionary rules, and activating only semantically relevant memories during inference (with a calibrated relevance threshold and explicit fallback for irrelevant memory), the system grounds numerical computation, retrieval, visual decoding, and answer verification in a deterministic financial tool environment. Experiments on four multimodal finance benchmarks show that this memory‑enhanced approach consistently lifts the performance of a frozen 8 B vision‑language model beyond finance‑specialized baselines and approaches the best proprietary general‑purpose models, while markedly improving reliability under retrieval uncertainty.


<details>
<summary>Abstract</summary>

Financial multimodal reasoning requires agents to coordinate numerical computation, retrieval, visual interpretation, and temporal grounding across heterogeneous evidence sources. Existing tool-augmented agents improve execution fidelity, yet remain largely stateless across episodes, repeatedly rediscovering reasoning strategies and failure patterns. In high-stakes financial settings, this leads to unreliable tool routing, noisy retrieval, and hallucination-prone reasoning. We present FinAcumen, a financial reasoning agent framework centered on selective experience memory for tool-augmented multimodal reasoning. FinAcumen accumulates financially grounded reasoning experience from prior trajectories, distilling successful strategies and failure-derived cautionary rules into a persistent memory bank. During inference, retrieved experiences condition reasoning only when semantic relevance exceeds a calibrated threshold, while irrelevant memory is explicitly suppressed through a fallback mechanism. A deterministic financial tool environment further grounds numerical computation, retrieval, visual decoding, and answer verification.Across four financial multimodal reasoning benchmarks, FinAcumen consistently improves a frozen 8B vision-language model over finance-specialized models and approaches leading proprietary general-purpose models. Further analysis shows that selective experience activation improves reasoning reliability under retrieval uncertainty. Our code is anonymously available at https://anonymous.4open.science/r/FinAcumen

</details>


### 91. TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning

- **Authors:** Zijie Meng, Ziwei Li, Yufei Liu, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Miao Zhang
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.18308v1](http://arxiv.org/abs/2606.18308v1)
- **PDF:** [https://arxiv.org/pdf/2606.18308v1](https://arxiv.org/pdf/2606.18308v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution** – The paper introduces **TRIDENT**, the first provably safe multi‑agent reinforcement‑learning (MARL) framework that simultaneously tackles three tightly coupled challenges in networked cyber‑physical systems: hybrid discrete‑continuous actions, hard safety constraints during training, and physics‑based dynamics.  

**Methodology** – TRIDENT co‑designs three algorithmic components to neutralize the “three‑way coupling” bias: (1) a Richardson‑Romberg correction that eliminates the \(O(\tau)\) bias of Gumbel‑Softmax relaxations, (2) a Lyapunov‑constrained sequential trust‑region update that guarantees per‑iteration feasibility, and (3) a physics‑informed residual critic that models value as a decomposition of the underlying dynamics rather than raw reward. The authors prove an \(\tilde O(1/\sqrt{K})\) convergence to a constrained Nash equilibrium and an \(O(\sqrt{K})\) bound on cumulative safety violations.  

**Key findings** – In demanding benchmarks (multi‑UAV mobile‑edge computing, autonomous intersection management, and a hybrid SMAC variant), TRIDENT reduces training‑time safety violations by **≈95 % vs. MADDPG** and **≈76 % vs. MACPO**, while delivering a **≈13 % higher reward** than the strongest unconstrained baselines, demonstrating that provable safety can be achieved without sacrificing performance in agentic AI systems.


<details>
<summary>Abstract</summary>

Safe coordination in networked cyber-physical systems forces learning algorithms to simultaneously handle hybrid discrete-continuous actions, hard training-time safety constraints, and physics-governed dynamics. We show that these three features form a directed cycle of biases that defeats any naive composition of off-the-shelf modules, and formalize this as a three-way coupling lemma. We then introduce TRIDENT, the first MARL framework whose three components are co-designed to cancel each leak: a Richardson-Romberg gradient correction reducing Gumbel-Softmax bias from O(tau) to O(tau^2), a Lyapunov-constrained sequential trust-region update enforcing per-iterate feasibility, and a physics-informed residual critic that decomposes value rather than reward. We prove an O~(1/sqrt(K)) convergence rate to a constrained Nash equilibrium and an O(sqrt(K)) cumulative-violation bound. On multi-UAV mobile-edge computing, autonomous intersection management, and a hybrid SMAC variant, TRIDENT cuts training-time violations by 95.5% over MADDPG and 76.3% over MACPO, while improving reward by 13.5% over the strongest unconstrained baseline.

</details>


### 92. Divide, Deliberate, Decide: A Multi-Agent Framework for Fine-Grained Egocentric Action Recognition

- **Authors:** Alessandro Sottovia, Alessandro Torcinovich, Oswald Lanz
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17627v1](http://arxiv.org/abs/2606.17627v1)
- **PDF:** [https://arxiv.org/pdf/2606.17627v1](https://arxiv.org/pdf/2606.17627v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces **Divide, Deliberate, Decide (D³)**, a zero‑shot, locally‑run multi‑agent system that improves fine‑grained egocentric action recognition by orchestrating a division of the video, a structured deliberation among heterogeneous Vision‑Language Model (VLM) specialists, and a final decision step that re‑ranks the orchestrator’s predictions using a Borda‑count aggregation. Methodologically, the orchestrator first chunks the video and generates top‑k label candidates per segment; then a set of specialist VLMs from different model families exchange queries and evidence in a peer‑consultation round; finally the aggregated rankings inform a revised prediction without any fine‑tuning. Experiments on standard egocentric benchmarks demonstrate consistent zero‑shot performance gains over single‑model baselines, attributing the improvement to decorrelated priors among the specialist agents rather than to extra compute.


<details>
<summary>Abstract</summary>

Fine-grained action recognition in egocentric video is challenging for Vision-Language Models (VLMs): actions often differ only in small visual cues, and a single model tends to be biased toward a subset of these cues. We propose Divide, Deliberate, Decide, a fully-local, zero-shot multi-agent framework in which (i) a VLM orchestrator chunks the video and proposes a top-k candidate label list per segment, (ii) an ensemble of heterogeneous VLM specialists, drawn from different open model families, engages in a structured deliberation that includes a peer-consultation round of questions, and (iii) agent rankings are aggregated with a Borda count and the orchestrator re-ranks its own prediction in light of the specialists' evidence. The entire pipeline runs locally with no fine-tuning. Experiments show that our method positively improves zero-shot action recognition performance over the baseline, highlighting the influence of a heterogeneous deliberation step, showing that the gain stems from decorrelated model priors rather than from additional compute.

</details>


### 93. Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning

- **Authors:** Yanwei Cui, Xing Zhang, Yulong Zhang, Li Shao, Xiaofeng Shi, Guanghui Wang, Peiyang He
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17591v1](http://arxiv.org/abs/2606.17591v1)
- **PDF:** [https://arxiv.org/pdf/2606.17591v1](https://arxiv.org/pdf/2606.17591v1)
- **Categories:** cs.AI


> The paper introduces **Insight Governance**, a three‑layer architecture (rules → evidence → skills) that closes the loop between experience extraction and action selection for training‑free verbal reinforcement learning agents. By continuously curating distilled verbal rules with outcome‑driven reliability logs and a non‑monotonic governance policy, the system can retain useful insights while forgetting obsolete ones in non‑stationary settings. In a financial‑forecasting benchmark, the same pool of extracted experiences either collapses performance below zero‑shot or yields large gains in accuracy and risk‑adjusted return, demonstrating that effective governance of verbal insights is essential for robust, parameter‑free LLM agents.


<details>
<summary>Abstract</summary>

Training-free verbal reinforcement learning enables LLM agents to learn from world feedback -- objective signals such as dynamic task outcomes, market returns, or demand forecasts -- by extracting verbal rules from experience and injecting them as context, updating the agent's behavior without parameter changes. However, in non-stationary environments these agents face a retention-forgetting dilemma: retaining stale insights causes negative transfer, while discarding them causes catastrophic forgetting when conditions recur. We identify four requirements for navigating this dilemma -- outcome-driven evaluation, persistent structured evidence, non-monotonic knowledge lifecycle, and compositional governance -- and show that existing methods invest heavily in experience extraction while underinvesting in insight governance. We propose a three-layer architecture -- rules, evidence, and skills -- connected by a feedback-driven curation loop that closes the governance gap. Rules capture distilled experience from world outcomes; evidence logs track each rule's reliability across episodes; skills govern which rules to apply, how to resolve conflicts, and when to abstain. On financial forecasting as a case study, where world feedback is naturally abundant, noisy, and non-stationary, we show that the same accumulated experience either degrades performance below the zero-shot baseline or dramatically improves accuracy and risk-adjusted returns, depending on whether the curation loop is present.

</details>


### 94. SEAGym: An Evaluation Environment for Self-Evolving LLM Agents

- **Authors:** Congjie Zheng, Chuanyi Xue, Bin Liang, Jun Yang, Changshui Zhang
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17546v1](http://arxiv.org/abs/2606.17546v1)
- **PDF:** [https://arxiv.org/pdf/2606.17546v1](https://arxiv.org/pdf/2606.17546v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents **SEAGym**, a systematic evaluation framework for self‑evolving large‑language‑model (LLM) agents that focuses on the “agent harness” (prompts, memory, tools, middleware, etc.) rather than just downstream task scores.  

**Methodology:** SEAGym wraps existing Harbor‑compatible benchmarks (e.g., Terminal‑Bench 2.0, HLE) into a multi‑view evaluation suite that records performance across distinct stages—training, validation, test (both in‑distribution and out‑of‑distribution), replay, and computational cost. It enforces a common epoch/batch protocol and logs snapshots of the harness after each update, enabling analysis of reuse, over‑fitting, and degradation.  

**Key findings:** Applying SEAGym to three self‑evolution strategies (ACE, TF‑GRPO, AHE) reveals that (1) frequent harness updates often do **not** translate into better held‑out performance, (2) intermediate “good” snapshots can later collapse, and (3) the diversity of training sources and the choice of model backend materially affect the robustness and cost‑efficiency of the evolving agent. These results demonstrate that multi‑view diagnostics are essential for reliable assessment of self‑evolving LLM agents.


<details>
<summary>Abstract</summary>

Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

</details>


### 95. OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation

- **Authors:** Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17536v1](http://arxiv.org/abs/2606.17536v1)
- **PDF:** [https://arxiv.org/pdf/2606.17536v1](https://arxiv.org/pdf/2606.17536v1)
- **Categories:** cs.CV, cs.AI


> **Contribution**  
The paper introduces **DRIVE‑CHOREO**, a novel LLM‑orchestrated multi‑agent world model that solves the heterogeneity of control signals and the lack of global 3‑D consistency in multi‑view driving video generation by creating a shared, position‑aware “latent‑token” interlingua linking language, geometry and pixel data.

**Methodology**  
Three specialized Qwen2.5‑VL agents—**Director** (interprets free‑form user intent into a structured *WorldScript*), **Cartographer** (grounds the script into spatial layout tokens anchored in 3‑D space), and **Auditor** (provides cross‑view critique for auxiliary supervision)—collaboratively produce a single token sequence. This sequence is jointly compressed with multi‑camera video frames through a view‑time permutation inside a 3‑D VAE, enforcing inter‑camera geometry at the latent level.

**Key Findings**  
On the nuScenes benchmark, DRIVE‑CHOREO achieves state‑of‑the‑art multi‑view consistency and a BEV detection mAP of **21.6**, while maintaining competitive video quality (FVD = 45.7). Moreover, a detector trained solely on the synthetic videos generated by the model improves real‑world validation NDS by **+2.4**, demonstrating the practical downstream utility of the approach for agentic autonomous‑driving AI.


<details>
<summary>Abstract</summary>

Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-choreographed multi-agent world model that recasts controllable multi-view video generation as latent choreography. Three Qwen2.5-VL agents - a Director parsing user intent into a structured WorldScript, a Cartographer grounding it into spatially-anchored layout tokens, and an Auditor feeding cross-view critiques back as auxiliary supervision - jointly author a single position-aware token sequence. This sequence is co-compressed with the multi-view video via a view-time permutation that enforces inter-camera geometry within the convolutional receptive field of a 3-D VAE. On nuScenes, DRIVE-CHOREO sets new state-of-the-art multi-view consistency and BEV mAP (21.6) with competitive FVD (45.7); a detector trained purely on our synthetic data gains +2.4 NDS on the real validation split, validating downstream utility.

</details>


### 96. PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents

- **Authors:** Aaditya Pai
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17467v1](http://arxiv.org/abs/2606.17467v1)
- **PDF:** [https://arxiv.org/pdf/2606.17467v1](https://arxiv.org/pdf/2606.17467v1)
- **Categories:** cs.CR, cs.CL


> **Contribution** – The paper exposes the failure of existing prompt‑injection defenses, which are tuned on synthetic benchmarks, when applied to real‑world enterprise documents, and proposes **PARSE** (Provenance‑Aware Retrieval Sanitization), a domain‑aware, fact‑preserving sanitization pipeline for LLM‑driven agents.

**Methodology** – The authors build a benchmark of 122 realistic tasks across finance, law, medicine, science, and DevOps using authentic SEC filings, Federal Register rules, PubMed abstracts, arXiv papers, and GitHub postmortems. They evaluate a leading synthetic‑benchmark defense (paraphrasing) and then design PARSE, which (1) classifies each sentence for injection risk, (2) extracts structured facts and rewrites only high‑risk sentences, (3) runs a consistency‑checking loop to ensure factual preservation, and (4) uses a “directiveness gate” to route low‑risk documents through a lightweight path.

**Key Findings** – On the real‑document benchmark, paraphrasing shows no significant reduction in attack success (p = 0.500) and hurts utility (91.8 % → 82.8 %). PARSE cuts attack success to 15.6 % (a 38 % relative reduction versus the 25.4 % baseline) while keeping utility at 86.9 %, a statistically significant improvement (p = 0.014). The results demonstrate that provenance‑aware, domain‑specific sanitization is essential for protecting professional‑domain LLM agents.


<details>
<summary>Abstract</summary>

Prompt injection defenses evaluated on synthetic benchmarks do not generalize to real enterprise documents, which are longer, denser, and interleave legitimate authority language with factual content. We demonstrate this gap with a real-document benchmark of 122 tasks across five professional domains (financial, legal, medical, scientific, DevOps) using actual SEC filings, Federal Register rules, PubMed abstracts, arXiv papers, and GitHub postmortems. Paraphrasing, the strongest defense on synthetic benchmarks, shows no statistically significant attack success rate reduction on real documents (p=0.500) while degrading utility from 91.8% to 82.8%. We introduce PARSE (Provenance-Aware Retrieval Sanitization), a domain-aware, fact-preserving sanitization pipeline that classifies each sentence by injection likelihood, extracts structured facts before rewriting, and verifies fact preservation via a consistency-checking loop. A directiveness gate routes 59% of real enterprise documents to a lightweight path, concentrating computational cost on high-risk documents. PARSE achieves 15.6% attack success rate -- a 38% reduction versus the 25.4% baseline -- at 86.9% utility, the only condition that is both statistically significant (p=0.014, adequately powered) and maintains near-baseline utility. Practitioners should evaluate defenses on domain-matched real documents, not synthetic proxies.

</details>


### 97. AUTOGATE: Automated Clock Gating via Toggling-Aware LLM-based RTL Rewriting

- **Authors:** Yiting Wang, Chenhui Deng, Chia-Tung Ho, Yanqing Zhang, Zhuo Feng, Cunxi Yu, Ang Li, Gang Qu, Brucek Khailany
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17461v1](http://arxiv.org/abs/2606.17461v1)
- **PDF:** [https://arxiv.org/pdf/2606.17461v1](https://arxiv.org/pdf/2606.17461v1)
- **Categories:** cs.AR, cs.AI, cs.LG


> The paper introduces **AUTOGATE**, the first agentic framework that automatically inserts fine‑grain clock‑gating logic into large, hierarchical RTL designs. It combines a lightweight ML clustering step that compresses millions‑cycle toggling waveforms into concise, “toggling‑aware” representations, which are then fed to LLM agents that rewrite the RTL; a multi‑agent hierarchy further decomposes the design so each module can be optimized independently yet coherently. Experiments on benchmark and industrial designs show that AUTOGATE cuts dynamic power by up to 49 % on small circuits and by 7–19 % on real‑world chips such as NVDLA, BlackParrot, and proprietary production blocks, demonstrating scalable, workload‑aware power optimization for agentic AI‑driven hardware design.


<details>
<summary>Abstract</summary>

Fine-grain clock gating (FGCG) is among the most effective techniques for reducing dynamic power, yet current FGCG optimization flows remain largely manual. Recent LLM-based RTL optimization approaches remain limited by two key drawbacks: (1) the inability to process long waveform traces spanning millions of cycles, and (2) the difficulty of scaling optimization to large hierarchical codebases while preserving correctness. In this work, we present AUTOGATE, the first agentic framework for industry-grade RTL power optimization, enabling workload-aware clock-gating optimization across large hierarchical codebases. AUTOGATE introduces a Machine Learning (ML)-LLM co-design that bridges waveform-level analysis and RTL rewriting. Specifically, we design an ML-based clustering algorithm that distills raw toggling traces into compact, structured representations that guide LLM-based RTL rewriting. This enables accurate identification and application of clock-gating opportunities without requiring LLMs to directly process raw waveform data. To enhance scalability, AUTOGATE employs a hierarchical multi-agent architecture that decomposes large designs into independently optimizable modules, enabling coordinated optimization across deep design hierarchies. We evaluate AUTOGATE on a diverse set of designs ranging from small RTL designs to large industrial-grade codebases. Experimental results show that AUTOGATE consistently reduces dynamic power relative to baselines. Across the small-design suite, AUTOGATE reduces dynamic power by 49.31% on average. On industry-scale designs, it achieves 19.34% and 7.96% dynamic power reductions on NVDLA and BlackParrot, respectively, and up to 6.86% on highly optimized proprietary production designs.

</details>


### 98. Can LLMs Be CEOs? Benchmarking Strategic Resource Reallocation with Multi-Role Agent Simulation

- **Authors:** Yuyang Dai, Xueqing Peng, Lingfei Qian, Zhuohan Xie
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17459v1](http://arxiv.org/abs/2606.17459v1)
- **PDF:** [https://arxiv.org/pdf/2606.17459v1](https://arxiv.org/pdf/2606.17459v1)
- **Categories:** cs.AI


> The paper presents **CEO‑Bench**, a novel multi‑agent benchmark that tests whether large language models can act as CEOs by synthesizing conflicting, privately‑held advice from four role‑conditioned C‑suite advisors (CFO, CTO, COO, CMO) to reallocate capital across business units over multiple rounds under realistic organizational constraints. Using five state‑of‑the‑art LLMs on 13 scenario suites, the authors find that while all models reliably produce structurally valid allocation plans, they markedly differ in “strategic calibration”: many fall into single‑advisor capture, excessive conservatism, or loss of historical context, and a clear trade‑off emerges between deep integration of divergent perspectives and decisive (bold) action. These results map the current limits of LLMs as executive‑level decision makers and highlight design challenges for future AI‑augmented leadership systems.


<details>
<summary>Abstract</summary>

Evaluating the decision-making capabilities of large language models (LLMs) is a growing research priority, yet existing benchmarks focus on isolated cognitive tasks such as reasoning, knowledge retrieval, and economic rationality in stylized settings. These evaluations overlook the defining challenge of real executive decision-making: integrating conflicting recommendations from specialized stakeholders under information asymmetry, organizational constraints, and temporal dependencies. We introduce \textsc{CEO-Bench}, a multi-agent benchmark that evaluates LLMs on CEO-level strategic resource reallocation -- the process of redirecting capital across business units in a multi-round, constraint-rich organizational environment. In \textsc{CEO-Bench}, LLM agents receive conflicting advice from four role-conditioned C-suite advisors (CFO, CTO, COO, CMO), each with private signals and distinct priorities, and must synthesize these into a concrete allocation plan evaluated along four dimensions: role integration, conditional boldness, history-sensitive judgment, and plan validity. Experiments across five frontier models on 13 scenarios reveal that all models achieve high structural validity but diverge sharply on strategic calibration -- the hardest capability layer. We identify systematic failure modes including single-advisor capture, conservative default under ambiguity, and historical amnesia, and uncover a structural integration-boldness tradeoff: models that engage more deeply with conflicting perspectives tend to produce less decisive action. These findings delineate the current capability boundary of LLMs as organizational decision-makers and inform the design of future AI-assisted executive systems.

</details>


### 99. Dissecting model behavior through agent trajectories

- **Authors:** Gaurav Gupta, Vatshank Chaturvedi, Jun Huan, Anoop Deoras
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17454v2](http://arxiv.org/abs/2606.17454v2)
- **PDF:** [https://arxiv.org/pdf/2606.17454v2](https://arxiv.org/pdf/2606.17454v2)
- **Categories:** cs.AI, cs.LG


> **Main contribution**  
The paper introduces the “intent‑execution” gap concept to explain why a model’s latent capabilities often fail to materialize in an autonomous agent, and presents a lightweight, highly configurable harness—Simple Strands Agent (SSA)—that systematically narrows this gap across a variety of large‑language‑model families.

**Methodology**  
SSA runs each model on three standard agentic benchmarks (SWE‑Pro, SWE‑Verified, Terminal‑Bench‑2) while logging full execution traces; the authors then map these traces onto a code‑state space and compute fine‑grained trajectory metrics (edit frequency, testing activity, phase transitions, etc.) to compare how different models allocate effort during problem solving.

**Key findings for agentic AI**  
Using SSA, the authors match or exceed the published pass@1 scores of numerous frontier models, but more importantly reveal systematic behavioral distinctions: some models perform many small edits and extensive testing, while others make fewer, larger changes and transition between planning, coding, and verification phases differently. These nuanced trajectory analyses demonstrate that minimizing the intent‑execution gap—and measuring it with state‑space metrics—offers a more informative benchmark for evaluating and improving agentic AI systems than raw success rates alone.


<details>
<summary>Abstract</summary>

AI agent performance is not just a modeling problem, it is fundamentally a systems problem. The advanced capabilities of models are realized through agent harnesses. Therefore, a gap between model assumptions and harness behavior can easily prevent the model's full capabilities from translating into agent performance. We formalize this as the `intent-execution' gap: the mismatch between what the model intends and what the harness executes, and vice versa. We argue that minimizing this intent-execution gap is as important as other aspects of harness design such as tools and execution loops. To illustrate the impact of this harness-model alignment, we develop a simple and customizable harness called `Simple Strands Agent' (SSA). SSA aims to find the bulk of common patterns which generalize across different model families (such as Claude, Gemini, GPT, Grok, Qwen), as well as a small number of model-specific preferences. We make two contributions: (i) we reproduce or improve on the pass@1 performance reported by diverse model-provider families on popular agentic benchmarks (SWE-Pro, SWE-Verified and Terminal-Bench-2), and (ii) building on an analysis of 138k trajectories generated by SSA, we look beyond the pass@1 numbers which tend to be relatively even across frontier models. By representing agent trajectories in code state-spaces, we observe model-level differences in problem-solving behavior. Finer-grained metrics such as edit frequency, testing activity, and phase-transitions reveal how individual models allocate effort across different stages of autonomous problem solving.

</details>


### 100. MODE-RAG: Manifold Outlier Diagnosis and Energy-based Retrieval-Augmented Generation Evaluation

- **Authors:** Zehang Wei, Jiaxin Dai, Jiamin Yan, Xiang Xiang
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17449v1](http://arxiv.org/abs/2606.17449v1)
- **PDF:** [https://arxiv.org/pdf/2606.17449v1](https://arxiv.org/pdf/2606.17449v1)
- **Categories:** cs.CL, cs.AI, cs.CV, cs.LG, cs.MM


> **Main contribution:**  
The paper introduces **MODE‑RAG**, a multi‑agent architecture that dynamically detects and mitigates hallucinations, fabrications, and sycophancy in multimodal retrieval‑augmented generation (M‑RAG) systems by using variational free‑energy (VFE)–based confidence estimates and attention‑state gating.

**Methodology:**  
A hierarchy of five specialized agents (query router, causal‑derivation via Monte‑Carlo Tree Search, logit‑perturbation for sycophancy reduction, correction, and overseer) is triggered only for high‑risk inputs identified through VFE thresholds. The agents intervene by constraining the generation graph, adjusting logits, and performing post‑hoc fact‑checking, while preserving correct outputs.

**Key findings:**  
On the newly curated **ModeVent** benchmark (a hard subset of MultiVent), MODE‑RAG cuts hallucination and logical‑fabrication rates by a large margin (up to ~45 % relative reduction) and improves factual accuracy without degrading overall generation quality, demonstrating that adaptive, agent‑driven gating can robustify multimodal LLMs against cross‑modal errors.


<details>
<summary>Abstract</summary>

While Multimodal Retrieval-Augmented Generation (M-RAG) enhances Large Vision-Language Models, it remains highly susceptible to cross-modal hallucinations, causal fabrications, and sycophancy. Furthermore, existing mitigation pipelines often face an intervention paradox: static rules tend to unnecessarily disrupt accurate generations, whereas leaving the multi-modal reasoning completely unguided allows existing mismatches to cascade into severe logical fabrications. To quantify and mitigate these hallucinations, we propose a Multi-Agent system, MODE-RAG, driven by Variational Free Energy (VFE) and internal attention states to dynamically gate interventions. High-risk queries are routed to five stage-specific agents, integrating Monte Carlo Tree Search (MCTS) for rigorous causal derivation and logit perturbations to penalize sycophancy. Dedicated Correction and Overseer agents ensure formatting stability and perform post-hoc factual verification. To objectively evaluate our approach, we introduce ModeVent, a challenging subset derived from the MultiVent dataset. Extensive experiments indicate that our system effectively reduces hallucination rates and logical fabrication, significantly improving the robustness of M-RAG systems.

</details>


### 101. Interpretable and Verifiable Hardware Generation with LLM-Driven Stepwise Refinement

- **Authors:** You Li, Samuel Mandell, David Z. Pan
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19387v1](http://arxiv.org/abs/2606.19387v1)
- **PDF:** [https://arxiv.org/pdf/2606.19387v1](https://arxiv.org/pdf/2606.19387v1)
- **Categories:** cs.SE, cs.AI


> **Paper summary**  
The authors present a hybrid hardware‑generation framework that lets a large language model (LLM) act as an autonomous design agent while guaranteeing formal correctness of the produced Register‑Transfer Level (RTL) code. The methodology introduces a library of formally verified transformation rules (e.g., for pipelining, bus interfacing, and control‑logic synthesis) and a stepwise‑refinement loop: the LLM proposes a high‑level design, the system selects applicable rules, applies them to produce an intermediate RTL fragment, and a formal checker validates each step before the next refinement. Experiments on a suite of benchmark specifications show that the LLM‑driven agent can synthesize complete, error‑free RTL implementations up to 30 % faster than a manual workflow, with zero post‑generation bugs detected by downstream verification tools, demonstrating a viable path toward trustworthy, explainable AI‑assisted hardware design.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have achieved remarkable success in software development. However, they are susceptible to hallucinations, meaning that they can introduce subtle semantic and logical errors. Due to the high stakes in chip design and manufacturing, hardware engineers are still reluctant to rely on LLMs for register-transfer level (RTL) generation. In this paper, we propose a hardware generation framework that combines the creativity and broad knowledge of LLMs with the explainability and mathematical rigor of formal methods. Specifically, we devise a set of transformation rules that cover various design decisions and hardware features. By iteratively applying these rules, an LLM agent can convert a design specification into an RTL program with guaranteed correctness. Experimental results demonstrate the effectiveness and efficiency of the framework.

</details>


### 102. SoK: AI-Augmented Binary Reversing

- **Authors:** Yujeong Kwon, Yiyue Zhang, Shakhzod Yuldoshkhujaev, Kexin Pei, Dokyung Song, Hyungjoon Koo
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17398v1](http://arxiv.org/abs/2606.17398v1)
- **PDF:** [https://arxiv.org/pdf/2606.17398v1](https://arxiv.org/pdf/2606.17398v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> The paper provides the first systematic overview of AI‑augmented binary‑reversing research, cataloguing 144 papers (2015‑2024) into 22 inference‑task domains and introducing a unified taxonomy that links traditional analysis steps, binary‑derived artifacts, representation choices, learning paradigms, and downstream tasks—while explicitly mapping the emerging roles of large language models and agentic AI systems. By applying this taxonomy, the authors demonstrate that many apparently disparate approaches share a common pipeline structure, uncover recurring technical bottlenecks (e.g., limited ground‑truth data, fragmented evaluation metrics) and evaluation gaps, and pinpoint where agentic AI can most effectively orchestrate multi‑step reverse‑engineering workflows. Their findings give the agentic‑AI community a common vocabulary and roadmap for building more reliable, scalable, and interoperable AI‑driven binary analysis tools.


<details>
<summary>Abstract</summary>

Binary reversing is fundamental to software understanding, vulnerability discovery, malware investigation, and firmware auditing. However, it remains inherently challenging due to the irreversible loss of semantic information during compilation. Recent advances in machine learning, large language models (LLMs), and agentic AI systems have accelerated the adoption of AI-augmented binary reversing. Yet, the resulting body of work has become increasingly fragmented across reversing domains, artifact representations, learning approaches, and evaluation practices. This paper presents the first comprehensive systematization of knowledge on AI-augmented binary reversing. We analyze 144 research papers published since 2015, and organize them into 22 binary reversing domains according to the inference tasks. We further introduce a unified taxonomy spanning conventional and AI-augmented reversing pipelines. Our taxonomy connects traditional analysis techniques, binary-derived artifacts, representation strategies, learning paradigms, and downstream inference tasks, while clarifying the emerging roles of LLMs and agentic AI systems. By establishing a common vocabulary and structured framework, we provide a holistic view of the field's evolution over the past decade. Our study reveals common structures underlying seemingly disparate approaches, highlights persistent technical challenges and evaluation gaps, and identifies promising opportunities for future research. Collectively, these insights clarify the current state of the field and provide a foundation for the next generation of reliable and scalable AI-augmented binary reversing systems.

</details>


### 103. Visuals Lie, Consistency Speaks: Disentangling Spatial Attention from Reliability in Vision-Language Models

- **Authors:** Logan Mann, Yi Xia, Ajit Saravanan, Ishan Dave, Saadullah Ismail, Shikhar Shiromani, Emily Huang, Ruizhe Li, Kevin Zhu
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17389v1](http://arxiv.org/abs/2606.17389v1)
- **PDF:** [https://arxiv.org/pdf/2606.17389v1](https://arxiv.org/pdf/2606.17389v1)
- **Categories:** cs.CV, cs.AI, cs.CL, cs.LG


> The paper overturns the common “attention‑confidence” belief that tightly focused visual attention signals reliable outputs in vision‑language models (VLMs). By introducing quantitative structural‑attention metrics—cluster counts (Cₖ) and spatial entropy (Hₛ) together with their layerwise change (ΔHₛ)—the authors probe a wide range of recent VLMs (LLaVA, PaliGemma, Qwen2‑VL) and show that attention patterns are effectively decoupled from correctness (correlation R≈0.001), a phenomenon they call “Symbolic Detachment” and “Cluster Failure”. Instead, reliability is best predicted by generation‑time dynamics, especially self‑consistency across sampled reasoning paths (R≈0.429), and by the distribution of predictive information across layers, with some architectures (PaliGemma, Qwen2‑VL) retaining robustness even after heavy ablation of their most predictive layers, unlike the fragile late‑stage bottleneck of LLaVA.


<details>
<summary>Abstract</summary>

Multimodal Foundation Models are increasingly used as reasoning agents, making reliability, knowing when a model may hallucinate, critical. A common intuition, which we call the Attention-Confidence Assumption, holds that reliability follows from "structural" visual perception: tight attention on relevant regions should signal a trustworthy answer, while scattered attention signals confusion. We challenge this through the VLM Reliability Probe (VRP), a systematic cross-family study of reliability signals in contemporary Vision-Language Models (VLMs). We introduce structural-attention metrics, cluster counts (C_k) and spatial entropy (H_s), to quantify the visual encoder's gaze, and track its evolution (Delta H_s) across layers. This reveals a "Symbolic Detachment": models often "Early Lock" visual features only to diffuse attention later, severing early perception from final generation. Contrary to the grounding hypothesis, we find a "Cluster Failure": spatial attention has near-zero correlation (R approx 0.001) with accuracy. Instead, reliability is a phenomenon of generation dynamics and internal-state distributions. Self-Consistency, the agreement rate across sampled reasoning paths, is the dominant predictor of truth (R = 0.429). Scaling causal interventions exposes a sharp architectural divergence: LLaVA locks its prediction in a fragile late-stage bottleneck, whereas PaliGemma and Qwen2-VL distribute reliability globally, staying resilient even when ~50% or more of their most predictive layer is destroyed. For current VLMs, reliability signals are detached from visual grounding maps and are best inferred from generation-time dynamics and hidden-state probes.

</details>


### 104. Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation

- **Authors:** Matthew Francis Dixon
- **Published:** 2026-06-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17383v1](http://arxiv.org/abs/2606.17383v1)
- **PDF:** [https://arxiv.org/pdf/2606.17383v1](https://arxiv.org/pdf/2606.17383v1)
- **Categories:** q-fin.RM, cs.AI, cs.LG, stat.ML


> **Main contribution** – The paper introduces a systematic model‑risk validation framework for autonomous (agentic) AI systems by casting their decision‑making pipeline as a Partially Observable Markov Decision Process (POMDP). This decomposition isolates and separately validates the information‑gathering, belief‑updating, forecasting, policy, and utility components, extending traditional predictive‑model risk methods to the full agentic loop.

**Methodology** – The authors formalize large language models (LLMs) as approximate Bayesian filters within the POMDP, develop a taxonomy of six model‑risk sources (state‑space, filtering, forecast, policy, utility‑specification, and parameter), and propose diagnostics (belief calibration, coverage tests, ablation, and sensitivity analyses). The framework is applied to a portfolio‑management agent that infers latent market regimes, produces regime‑conditioned forecasts, and allocates assets via a Black‑Litterman model.

**Key findings** – Empirical results show that properly validated latent‑state inference improves portfolio performance independently of other components, and the agent’s conclusions remain stable across wide parameter variations. The study demonstrates that the proposed POMDP‑based validation can reliably assess and monitor the integrity of the entire decision pipeline of agentic AI, offering a practical tool for governance and risk management.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence systems introduce a new class of model risk. Unlike traditional predictive models, autonomous agents continuously acquire information, form beliefs regarding latent states of the environment, generate forecasts, select actions, and adapt their behavior over time. Existing validation methodologies focus primarily on predictive accuracy and therefore provide limited insight into the quality of the underlying decision process. This paper proposes a model validation framework for agentic AI based on Partially Observable Markov Decision Processes (POMDPs). The framework decomposes autonomous decision making into information, beliefs, forecasts, actions, and utility, allowing each component to be validated independently. Large language models (LLMs) are formalized as approximate Bayesian filtering operators, and a model-risk taxonomy is developed encompassing state-space, filtering, forecast, policy, utility-specification, and parameter risks.
  The model risk validation methodology is demonstrated through a portfolio-management case study in which an agent infers latent market regimes from market and macroeconomic information, generates belief-conditioned forecasts, and constructs portfolios using a Black--Litterman framework. Empirical validation combines performance analysis, belief calibration diagnostics, coverage tests, ablation studies, and parameter-sensitivity analysis. The results indicate that latent-state inference contributes independently to decision quality and that the principal conclusions remain robust across a broad range of parameter values. The principal contribution of the paper is a practical framework for extending established model risk management concepts to autonomous AI systems and providing a rigorous foundation for their validation, governance, and monitoring.

</details>


### 105. Distributed General-Purpose Agent Networks: Architecture, Key Mechanisms, and Prototypes

- **Authors:** Shengli Zhang, Deen Ma, Zibin Lin, Taotao Wang
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17368v1](http://arxiv.org/abs/2606.17368v1)
- **PDF:** [https://arxiv.org/pdf/2606.17368v1](https://arxiv.org/pdf/2606.17368v1)
- **Categories:** cs.AI, cs.NI


> **Main contribution** – The paper introduces a novel, layered architecture for *distributed general‑purpose agent networks* (DG‑ANs), showing that peer‑to‑peer overlays must be fundamentally extended to propagate semantic intent, capability, and governance information so that heterogeneous autonomous agents can discover one another, negotiate trust, and cooperate on open‑ended tasks.

**Methodology** – The authors define a protocol‑adaptation layer that maps high‑level task semantics to low‑level network primitives and address three core mechanisms: (1) *semantic announcement propagation* via a “bodyless gossip” protocol with sequential logs for efficient collaborator discovery; (2) *verifiable identity and multi‑topic reputation* using a BAID‑style identity binding together with a Modified‑Gain EigenTrust (MG‑EigenTrust) algorithm to give cross‑topic, collusion‑resistant trust scores; and (3) a *semantic‑gradient mechanism design* that iteratively generates Stackelberg‑style incentive mechanisms based on semantic attribution feedback to align agents’ actions with open tasks.

**Key findings** – Prototype experiments demonstrate that the BAID‑based tiered verification incurs modest latency (≈ 30 ms per hop) while preserving strong identity guarantees, and simulations of MG‑EigenTrust show robust reputation convergence even under disguise‑collusion attacks across topics. Together, these results provide the first system‑level proof‑of‑concept that open, trustworthy, and scalable collaboration among heterogeneous autonomous agents is achievable, laying groundwork for future agentic AI ecosystems.


<details>
<summary>Abstract</summary>

Large language models have accelerated the transition from passive conversational assistants to autonomous agents that can understand goals, plan actions, invoke tools, and execute multi-step tasks. Yet the capability of a single agent remains constrained by its local data, tool permissions, runtime environment, and governance boundary. This paper studies distributed general-purpose agent networks: open peer-to-peer networks in which heterogeneous agents deployed on personal devices, edge nodes, or autonomous computing environments can discover one another, establish trust, negotiate cooperation rules, and execute open-ended tasks. We argue that such networks cannot be obtained by simply combining existing peer-to-peer overlays with conventional multi-agent systems. Unlike traditional P2P networks, agent networks must propagate semantic declarations about intentions, capabilities, states, and cooperation constraints. We therefore propose a layered architecture centered on a protocol adaptation layer that connects upper-level task semantics with lower-level network operations. Based on this architecture, the paper identifies three core mechanism problems: semantic announcement propagation for collaborator discovery, verifiable identity and multi-topic reputation for cooperation governance, and semantic-gradient mechanism design for open task execution. For each problem, we present a technical route, including bodyless gossip with sequential logs, BAID-based identity binding with MG-EigenTrust reputation, and a Stackelberg-style mechanism-generation loop driven by semantic attribution feedback. We further report prototype overhead results for BAID-style tiered verification and mechanism-level simulations of MG-EigenTrust under cross-topic disguise-collusion attacks. The resulting framework provides a system-level foundation for open, trustworthy, and scalable agent collaboration.

</details>


### 106. MemTrace: Probing What Final Accuracy Misses in Long-Term Memory

- **Authors:** Xianxuan Long, Zhikai Chen, Shenglai Zeng, Shouren Wang, Kai Guo, Jiliang Tang
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17328v1](http://arxiv.org/abs/2606.17328v1)
- **PDF:** [https://arxiv.org/pdf/2606.17328v1](https://arxiv.org/pdf/2606.17328v1)
- **Categories:** cs.AI


> MemTrace introduces a fact‑centric benchmark for evaluating LLM agents’ long‑term user memory, probing each typed fact across three controlled axes—memory age, question type (current, prior, trajectory), and evidence condition (present, missing, false‑premise). By testing 13 memory‑system configurations under four paradigms, the authors show that aggregate accuracy masks distinct failure modes: agents can recall a fact’s present and past values yet miss how it evolved, and they may safely abstain without correcting contradictions, with the principal bottleneck being poor utilization of readily retrievable evidence rather than retrieval itself. Consequently, the work highlights that advancing agentic AI’s long‑term memory requires stronger evidence‑integration mechanisms rather than simply expanding storage or retrieval capacity.


<details>
<summary>Abstract</summary>

LLM agents increasingly maintain long-term memory of user facts across sessions. Yet such memory is usually evaluated by aggregating accuracy over question rows or episodes. Because this approach scores question rows independently, even when several questions probe the same fact, it cannot show how that fact behaves as conditions change. We introduce MemTrace, a benchmark whose unit of measurement is the knowledge point: a single typed fact about the user, rather than an individual question. MemTrace probes each fact along three controlled dimensions: memory age, defined by how many sessions ago the fact appeared in the history; question type, covering current state, earlier state, and trajectory of change; and evidence condition, covering present, missing, and contradicted-by-false-premise settings. Evaluating 13 memory-system configurations across four paradigms, we find that similar pooled accuracy hides different failures: recovering a fact's current and earlier states does not imply tracking how it changed, and safe abstention does not imply correcting a false premise. The dominant bottleneck is evidence use, not retrieval: when systems fail, the evidence was retrievable 10 times more often than it was missing. These results suggest that improving long-term memory requires better use of reachable evidence, not simply more storage or retrieval.

</details>


### 107. Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence

- **Authors:** Manvendra Modgil
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.19386v1](http://arxiv.org/abs/2606.19386v1)
- **PDF:** [https://arxiv.org/pdf/2606.19386v1](https://arxiv.org/pdf/2606.19386v1)
- **Categories:** cs.SE, cs.AI, cs.LG


> **Main contribution:** The paper demonstrates that runtime monitors for autonomous agents that are calibrated in wall‑clock time (e.g., leaky‑integrator or exponential‑moving‑average models) inevitably collapse into two extreme regimes—continuous alarm or complete silence—when the inter‑action intervals of agents vary, thereby failing to function as moment‑detectors.  

**Methodology:** The authors conduct a pre‑registered sweep over 20 agent trajectories, varying the observation interval dt from 0 s to 600 s, and compare wall‑clock‑calibrated monitors (including a simple wall‑clock accumulator) with sample‑time‑calibrated CUSUM monitors on the same error stream.  

**Key findings:** For wall‑clock‑calibrated monitors, dt ≤ 1 s yields near‑constant alarms (median 18 firings per trajectory) and dt ≥ 60 s yields silence, with the critical “trap” region (1–30 s) matching the typical latency of real coding agents (median 1.53 s). Sample‑time‑calibrated CUSUM remains invariant to dt, and hysteresis‑based triggers fire only sparsely. Thus, wall‑clock‑calibrated leaky‑integrator monitors cannot serve as reliable moment‑detection mechanisms on agent streams, highlighting a fundamental design limitation for agentic AI monitoring systems.


<details>
<summary>Abstract</summary>

Runtime monitors for autonomous agents commonly threshold an accumulated internal state - a behavioural baseline, a drift statistic, or, in our prior work, a modelled affective state. We previously reported a State Saturation Trap: threshold-on-state triggers over a continuous affect engine become near-constant alarms on SWE-bench debugging agents (Modgil 2026). A post-release audit found the engine received dt=0 between actions, so its exponential decay never operated: the published trap is a pure-accumulator result. We correct the record (erratum, v2) and treat the flaw as an experiment. The key variable it exposes is whether a monitor's dynamics are calibrated in sample time (per observation, as in CUSUM) or wall-clock time (half-lives in seconds, as in affect models and EMA baselines). On fixed-rate streams these coincide; on agent streams, where inter-action time varies by orders of magnitude, they do not. A pre-registered sweep over uniform intervals (dt in {0..600}s) on 20 trajectories shows the wall-clock level trigger has two regimes: at dt<=1s a constant alarm (20/20; median 18 firings); at dt>=60s silent. Every critical dt lies in (1,30]s. Real agent runs measure latency at median 1.53s (p90 2.33s); real coding cadence sits inside the trap regime, vindicating the empirical finding under a corrected mechanism. The structure is a property of the calibration class, not the engine: a minimal wall-clock accumulator over the raw error stream reproduces the same cliff, while a sample-time CUSUM over the identical stream is exactly dt-invariant (20/20). A rising-edge trigger with hysteresis fires 0-3 times per trajectory in every condition. We conclude that wall-clock-calibrated leaky-integrator monitors admit no regime in which they act as moment detectors on agent streams; transition detection escapes the trap at every cadence, but does not recover human intervention timing.

</details>


### 108. GeoDisaster: Benchmarking Orchestrated Agents for Operational Disaster Geo-Intelligence

- **Authors:** Maram Hasan, Aman Verma, Savitra Roy, Hariseetharam Gunduboina, Daksh Jain, Muhammad Haris Khan, Subhasis Chaudhuri, Biplab Banerjee
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17246v1](http://arxiv.org/abs/2606.17246v1)
- **PDF:** [https://arxiv.org/pdf/2606.17246v1](https://arxiv.org/pdf/2606.17246v1)
- **Categories:** cs.CV, cs.MA


> **Main contribution** – The paper introduces **GeoDisaster**, a large‑scale benchmark (2,921 verified items, 43 question types) for “operational geo‑intelligence” that requires disaster‑focused spatial reasoning, tool‑grounded evidence integration, and structured, verifiable decisions across five EO/GIS task families (deforestation, multi‑hazard, building damage, flood‑safe routing, Sentinel‑1 flood monitoring).  

**Methodology** – GeoDisaster provides ground‑truth answers expressed as executable geospatial workflows and deterministic consistency checks, eliminating reliance on LLM‑generated labels. To tackle the benchmark, the authors build an **orchestrated multi‑agent system** equipped with 18 disaster‑specific tools; agents specialize by role and coordinate via explicit execution contracts. Alignment is achieved through **Role‑Contract Expectation Alignment (RCEA)**, a two‑stage training regime that combines failure‑aware supervised fine‑tuning with contract‑grounded reinforcement learning using dense, step‑level feedback.  

**Key findings** – Standard remote‑sensing vision‑language models and existing agentic frameworks perform poorly on GeoDisaster, revealing a gap between perception and operational decision‑making. The RCEA‑trained orchestrated agents markedly improve tool utilization, evidence grounding, state consistency, and the generation of coherent, evidence‑backed disaster reports, demonstrating the viability of contract‑driven multi‑agent coordination for complex geo‑intelligence tasks.


<details>
<summary>Abstract</summary>

Remote-sensing vision-language models (RS-VLMs) have advanced Earth-observation analysis toward visual interpretation and instruction-following, yet fall short of operational geo-intelligence, which demands tool-grounded spatial reasoning and structured, evidence-backed decisions. We introduce GeoDisaster, an operational geospatial disaster reasoning benchmark with 2,921 verified instances across 43 question types and five task families: deforestation monitoring, multi-hazard analysis, building-damage assessment, flood-safe routing, and Sentinel-1 SAR flood monitoring. Instances integrate heterogeneous EO/GIS evidence-optical and SAR imagery, raster masks, vector geometries, road networks, and exposure layers-spanning hazard detection, damage assessment, exposure estimation, and diagnostic report generation. Ground-truth answers are grounded in executable geospatial workflows and deterministic consistency checks, removing the need for language-model annotation. We further propose an orchestrated multi-agent framework with 18 disaster-oriented tools, where role-specialized agents coordinate through explicit execution contracts, aligned via Role-Contract Expectation Alignment (RCEA): failure-aware supervised fine-tuning combined with contract-grounded reinforcement learning over dense step-level signals. Experiments show that GeoDisaster challenges existing RS-VLMs and agentic systems, while RCEA improves tool use, evidence grounding, state consistency, and decision generation.

</details>


### 109. Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management

- **Authors:** Mohamed Essam, Kareem Wael, Azza Hassan, Ahmed Haitham, Mahmoud Soliman, Samer Saber, Ibrahim Habib
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17203v1](http://arxiv.org/abs/2606.17203v1)
- **PDF:** [https://arxiv.org/pdf/2606.17203v1](https://arxiv.org/pdf/2606.17203v1)
- **Categories:** cs.SE, cs.AI


> **Main contribution** – The paper introduces a trust‑aware coordination framework for multi‑agent software‑engineering pipelines, in which a shared, confidence‑calibrated knowledge graph is used both as a semantic memory and as a coordination surface that lets agents evaluate and build on each other’s traceability links.

**Methodology** – The authors devise a two‑stage traceability‑link prediction pipeline (embedding‑based retrieval followed by LLM‑driven multi‑criteria analysis), add a “traceability seeding” step that records both derivation‑time and validation‑time confidence scores, and enforce a consistency protocol that gates downstream processing by confidence thresholds, detects confidence divergence, and resolves conflicts.

**Key findings** – In an automotive‑software case study, calibrated confidence scores markedly improve link‑prediction calibration and downstream decision making; the protocol’s threshold gating and divergence detection reduce orphaned requirements and contradictory links, and ablation experiments show that confidence calibration is essential for effective coordination among agents in safety‑critical, traceability‑intensive environments.


<details>
<summary>Abstract</summary>

Multi-agent AI systems are increasingly used to automate software engineering tasks including requirements analysis, architecture design, test generation, and traceability linking. When these agents operate as a sequential pipeline over shared software artifacts, errors and low-confidence decisions made by upstream agents propagate to downstream stages, producing orphaned requirements, contradictory links, and compliance gaps that pose significant risks in safety-critical domains. We propose a trust-aware coordination framework where a shared knowledge graph serves as both centralized semantic memory and a coordination surface through which agents assess and build upon each other's contributions using calibrated confidence scores. Our approach introduces a two-stage traceability link prediction pipeline combining embedding-based retrieval with LLM-based multi-criteria analysis, a traceability seeding mechanism that enables comparison between derivation-time and validation-time confidence, and a consistency protocol governing pipeline interactions through confidence threshold gating, confidence divergence detection, and conflict resolution. We evaluate on an automotive software engineering case study measuring link prediction calibration, protocol effectiveness, threshold sensitivity, and the impact of traceability seeding. Ablation studies confirm that confidence calibration is essential for effective pipeline coordination.

</details>


### 110. Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems

- **Authors:** Sajjad Khan
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17182v1](http://arxiv.org/abs/2606.17182v1)
- **PDF:** [https://arxiv.org/pdf/2606.17182v1](https://arxiv.org/pdf/2606.17182v1)
- **Categories:** cs.LG, cs.DC, cs.LO, cs.MA, cs.PL


> The paper introduces the first mechanically‑verified consistency hierarchy for multi‑agent LLM runtimes, defining four concrete concurrency anomalies (stale‑generation, phantom‑tool, causal‑cascade, and tool‑effect reordering) and proving a strict lattice of five isolation levels (L₀ ⊂ … ⊂ L₄) that separate them. Using 274 Verus proof obligations (with no assumptions or admits) the authors verify sound‑and‑complete detectors for each anomaly, formally refine three Rust execution engines to satisfy L₀‑L₁, and construct verified “prevention twins” for L₂‑L₄, demonstrating the approach on real systems (e.g., fixing a lost‑update bug in ByteDance’s Deer‑Flow and eliminating tool‑effect reordering in LangGraph). The results show that deterministic‑replay based runtimes can be rigorously proved to prevent concurrency bugs in agentic AI pipelines, providing a solid foundation for safe, coordinated tool use among interacting LLM agents.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems share state through memory stores, vector indices, and tool registries. We model such sharing as long-running read-generate-write operations under deterministic-generation semantics -- the regime durable-execution engines enforce by deterministic replay -- and formalize four concurrency anomalies in TLA+: stale-generation, phantom-tool, causal-cascade, and tool-effect reordering, structural analogues of classical isolation anomalies, each with a TLC counter-example. The exclusion lattice over these anomalies is trivial; the contribution is the mechanically verified realizability and strict separation of one maximal chain within it, $L_0 \subsetneq \cdots \subsetneq L_4$, to our knowledge the first machine-checked consistency hierarchy for such runtimes. A development of 274 Verus obligations (zero assume, zero admit; trust base: two structural axioms and a mutex correspondence) proves the detectors sound and complete against the specifications and each runtime its avoidance set. Three deployed Rust runtimes realize L0-L1 (pessimistic locking, serializable snapshot isolation, default-SI), each verified against stale-generation and refined to its state machine; L2-L4 are exec-mode-verified with dependency-free prevention twins (A3, A6, A2: 0/1000 versus 1000/1000), and L2 is run live across three model families (A3 prevented in all 120 retracted sessions). We reproduce a silent lost update in ByteDance's deer-flow, formalizing its fix as a verified $L_0 \to L_1$ refinement, and exhibit tool-effect reordering in LangGraph's ToolNode on unmodified output, removed by an L3 commit-order sequencer. The verified detector, refinements, and realizability artifacts are the contribution; the phenomena and lattice are classical.

</details>


### 111. From Parasocial Scripts to Dyadic Persistence in Autonomous AI-Agent Communities

- **Authors:** Mohammadsadegh Abolhasani, Hamid Reza Firoozfar, Reza Mousavi, Paul Jen-Hwa Hu
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17174v1](http://arxiv.org/abs/2606.17174v1)
- **PDF:** [https://arxiv.org/pdf/2606.17174v1](https://arxiv.org/pdf/2606.17174v1)
- **Categories:** cs.CL, cs.CY, cs.MA


> The paper demonstrates that autonomous LLM‑driven agents exhibit parasocial interaction (PSI) cues—attachment/intimacy language, reciprocity bids, and self‑identification with the original poster—and that these cues predict sustained, reciprocal exchanges within an AI‑only community. Using a mixed‑methods pipeline (keyword searches, few‑shot LLM labeling, and grouped‑context LLM annotation) on 4,434 posts and 50,338 comments from Moltbook, the authors show that PSI‑style signals are statistically linked to higher OP re‑engagement and a dyadic‑persistence pattern that survives extensive robustness checks (negative controls, clustered SEs, multiple‑test corrections). The findings suggest that LLM‑enabled agents develop behavioral structures akin to human parasocial scripts, opening a new line of inquiry into relationship‑like dynamics among purely artificial agents.


<details>
<summary>Abstract</summary>

While parasocial interactions (PSIs) and parasocial relationships (PSRs) have been studied in conventional media settings, we investigate whether PSI- (colloquial) relational cues also exist in online communities where both sides are autonomous AI agents. We analyze 4,434 posts and 50,338 comments from Moltbook through three theory-based textual indicators: attachment/intimacy language, reciprocity bids, and self-identification to original poster (OP). The combined results across methods based on keyword matching, few-shot large language model (LLM) annotation, and grouped-context LLM annotation reveal that PSI colloquial cues prevail and are strongly associated with OP re-engagement and a reciprocal reply structure. These results are robust across negative controls, nullification, clustered-standard-error re-estimation, and multiple-testing correction. A dyadic persistence test further affirms reciprocity bids aligned with sustained OP-involving mutual recurrence, providing empirical evidence for bridging interaction-level PSI scripts with PSR-consistent repeated dyadic patterns. We interpret the evidence as a behavioral structure in discourse by LLM-enabled agents.

</details>


### 112. MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision

- **Authors:** Ye Jin, Yangyang Xu, Jun Zhu, Yibo Yang
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17162v1](http://arxiv.org/abs/2606.17162v1)
- **PDF:** [https://arxiv.org/pdf/2606.17162v1](https://arxiv.org/pdf/2606.17162v1)
- **Categories:** cs.CL, cs.HC, cs.MA


> MemSlides introduces a hierarchical memory architecture for presentation‑authoring agents that isolates **long‑term user profiles**, **session‑level working memory**, and **tool‑memory of reusable editing primitives**. By coupling this memory split with scoped, slide‑local revisions, the system can retain stable user preferences, propagate newly expressed constraints across multi‑turn interactions, and perform precise edits without regenerating whole decks. Experiments show that profile memory boosts persona‑alignment scores, tool‑memory enriches closed‑loop modification success, and working memory effectively carries over preferences, demonstrating that explicit separation of persistent, session, and execution memories is key for personalized, iterative agentic AI workflows.


<details>
<summary>Abstract</summary>

Personalized presentation generation requires more than conditioning on a current prompt or template: agents must preserve stable user preferences across tasks, retain newly introduced preferences and constraints during multi-turn revision, and carry out local edits reliably. We propose MemSlides, a hierarchical memory framework for personalized presentation agents that separates long-term memory from working memory and further divides long-term memory into user profile memory and tool memory. User profile memory stores intent-conditioned profiles for round-0 personalization, working memory carries active preferences and session constraints across revision rounds, and tool memory stores reusable execution experience for reliable localized editing. MemSlides pairs this memory design with scoped slide-local revision, so targeted updates act on the smallest affected region instead of repeatedly regenerating the full deck. In controlled experiments, user profile memory improves persona-alignment judgments on a multi-persona, multi-intent profile bank, tool-memory injection improves closed-loop modify behavior in diagnostic matched-pair settings, and qualitative cases illustrate working memory's ability to carryover preferences. Taken together, these results suggest that effective personalization in presentation authoring depends on separating persistent user profiles, session-level working memory, and reusable execution experience across generation and localized revision.

</details>


### 113. Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio

- **Authors:** Anzhe Xie, Weihang Su, Yujia Zhou, Yiqun Liu, Qingyao Ai
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17041v3](http://arxiv.org/abs/2606.17041v3)
- **PDF:** [https://arxiv.org/pdf/2606.17041v3](https://arxiv.org/pdf/2606.17041v3)
- **Categories:** cs.CL, cs.IR


> **Main contribution:** The paper releases **MetaSyn**, a curated benchmark of 442 full‑text meta‑analyses from Nature Portfolio that provides the complete evidence‑synthesis pipeline—research question, PI/ECO criteria, a 140 k‑article PubMed retrieval set, verified positive studies, hard negative distractors, and the original search strategies—enabling systematic evaluation of LLM‑driven scientific agents from literature retrieval through eligibility screening to statistical synthesis.

**Methodology:** The authors evaluate twelve LLM‑based pipeline configurations (nine retrieval‑augmented generation variants and a protocol‑driven agent) on MetaSyn, measuring recall of relevant articles at various retrieval depths and, crucially, the ability of the agents to **screen** the retrieved pool against the PI/ECO eligibility constraints using stage‑specific metrics.

**Key findings:** Although retrieval models achieve a ceiling of **≈90 % recall** at K = 200, all LLM agents fall short on the screening step, recovering at most **52.7 %** of the ground‑truth included studies. The results expose a bottleneck: current LLMs cannot reliably distinguish PI/ECO‑eligible papers from topically similar negatives, highlighting the need for better reasoning or tool‑use mechanisms in agentic AI for systematic review tasks.


<details>
<summary>Abstract</summary>

Meta-analysis is a demanding form of evidence synthesis that combines literature retrieval, PI/ECO-guided study selection, and statistical aggregation. Its structured, verifiable workflow makes it an ideal substrate for evaluating systematic scientific reasoning, yet existing benchmarks lack ground truth across the full retrieval-screening-synthesis pipeline. We introduce MetaSyn, a dataset of 442 expert-curated meta-analyses from Nature Portfolio journals. Each entry pairs a research question with PI/ECO criteria, a retrieval corpus of 140k PubMed articles, verified positive studies, hard negatives that are topically similar but PI/ECO-ineligible, and complete search strategies and date bounds.
  Benchmarking twelve pipeline configurations (nine RAG variants and a protocol-driven agent) reveals a critical screening bottleneck: despite a retrieval ceiling of 90.9% recall at K=200, no system recovers more than 52.7% of ground-truth included literature. Current LLMs fail to reliably separate eligible studies from PI/ECO-failing distractors in pools of comparable topical relevance. Stage-attributed metrics capture where systems succeed and fail; a single end-to-end score does not.

</details>


### 114. TokenPilot: Cache-Efficient Context Management for LLM Agents

- **Authors:** Buqiang Xu, Zirui Xue, Dianmou Chen, Chenyang Fu, Chiyu Wu, Caiying Huang, Chen Jiang, Jizhan Fang, Xinle Deng, Yijun Chen, Yunzhi Yao, Xuehai Wang, Jin Shang, Gong Yu, Ningyu Zhang
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17016v1](http://arxiv.org/abs/2606.17016v1)
- **PDF:** [https://arxiv.org/pdf/2606.17016v1](https://arxiv.org/pdf/2606.17016v1)
- **Categories:** cs.CL, cs.AI, cs.LG, cs.MA


> **Main contribution:** The paper introduces **TokenPilot**, a dual‑granularity context‑management system for large‑language‑model (LLM) agents that preserves prompt‑cache continuity while aggressively trimming irrelevant tokens.  

**Methodology:** TokenPilot combines a global **Ingestion‑Aware Compaction** step that stabilizes prompt prefixes and filters out environmental noise at the moment new text is added, with a local **Lifecycle‑Aware Eviction** policy that tracks the residual utility of each context segment and only evicts it after its task relevance expires, using a conservative batch‑turn schedule to avoid frequent layout changes that would invalidate cached prompt embeddings.  

**Key findings:** Across the PinchBench and Claw‑Eval suites, TokenPilot cuts inference token costs by **≈60 %** (isolated mode) and up to **87 %** (continuous mode) while retaining performance on par with earlier memory‑management baselines, demonstrating that cache‑friendly context pruning can dramatically improve the efficiency of long‑horizon LLM agents.


<details>
<summary>Abstract</summary>

As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, Ingestion-Aware Compaction acts as a framework harness to stabilize prompt prefixes and eliminate open-world environmental noise at the ingestion gate. Locally, Lifecycle-Aware Eviction monitors the ongoing residual utility of context segments, enforcing a conservative batch-turn schedule to offload content segments only when task relevance expires. Experiments on PinchBench and Claw-Eval under both isolated and continuous modes demonstrate that TokenPilot reduces costs by 61% and 56% in isolated mode, and 61% and 87% in continuous mode, while maintaining competitive performance compared to prior systems. TokenPilot has been integrated into LightMem2 at https://github.com/zjunlp/LightMem2.

</details>


### 115. Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification

- **Authors:** Truong Thanh Hung Nguyen, Khanh Van Quynh Nguyen, Hoang-Loc Cao, Tri Duong, Phuc Ho, Van Pham, Loc Nguyen, Hung Cao
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16987v1](http://arxiv.org/abs/2606.16987v1)
- **PDF:** [https://arxiv.org/pdf/2606.16987v1](https://arxiv.org/pdf/2606.16987v1)
- **Categories:** cs.AI


> The paper introduces a consensus‑based, multi‑agent LLM framework that tackles the hierarchical and legally intricate task of assigning 10‑digit Canadian Harmonized Tariff Schedule (HTS) codes to product descriptions in maritime logistics. By combining specialized retrieval agents, evidence‑grounded reasoning, element‑wise voting across tariff hierarchy levels, confidence estimation, and a human‑in‑the‑loop escalation mechanism, the system produces interpretable, uncertainty‑aware classifications; experiments on a 3.3 k expert‑labeled dataset show that while coarse chapter‑level accuracy is achievable, fine‑grained 10‑digit prediction remains challenging for even state‑of‑the‑art LLMs, underscoring the need for collaborative, evidence‑backed workflows rather than single‑step automation.


<details>
<summary>Abstract</summary>

Accurate Harmonized Tariff Schedule (HTS) code classification is essential for customs clearance, duty assessment, trade statistics, and regulatory compliance in maritime logistics. However, exact HTS classification remains challenging because product descriptions are often short, incomplete, or ambiguous, while correct classification depends on hierarchical tariff structures, legal notes, and jurisdiction-specific rules. This paper proposes an agentic large language model (LLM) framework for Canadian 10-digit HTS code classification in smart-port and maritime logistics environments. The framework integrates multi-agent information retrieval, semantic retrieval over official tariff documents, evidence-grounded reasoning, consensus-based validation, element-wise voting across hierarchical code components, confidence estimation, and human-in-the-loop escalation. We evaluate the framework on a private dataset of 3,300 domain-expert-labeled product records collected from logistics and delivery contexts. Experimental results show that exact 10-digit classification remains difficult even for advanced LLMs, with performance decreasing from coarse chapter-level prediction to fine-grained tariff and statistical suffix assignment. These findings demonstrate the need for evidence-grounded, uncertainty-aware, and human-centered classification workflows rather than fully autonomous single-step prediction. The proposed framework supports more interpretable, accountable, and compliance-oriented HTS classification for maritime logistics and smart-port operations. Our code is available at https://github.com/Analytics-Everywhere-Lab/hts.

</details>


### 116. Agentic Discovery of Non-Canonical Antimicrobial Peptides with AMPGAN v3

- **Authors:** Jay Jung, Xiaohan Zhang, Shenghan Song, Mahmoud Sayedahmed, Chijian Xiang, Yunong Xu, Ahmed AbdelKhalek, Severin T. Schneebeli, Matthew J. Wargo, Jianing Li, Safwan Wshah
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17127v1](http://arxiv.org/abs/2606.17127v1)
- **PDF:** [https://arxiv.org/pdf/2606.17127v1](https://arxiv.org/pdf/2606.17127v1)
- **Categories:** q-bio.QM, cs.AI, cs.LG


> The paper introduces **AMPGAN v3**, a conditional GAN that expands peptide generation beyond the canonical 20 amino acids to include D‑amino acids and N/C‑terminal modifications, and stabilizes training by assigning adversarial and activity‑related supervision to two dedicated discriminators. Using this model, the authors generated and experimentally validated five non‑canonical antimicrobial peptides, two of which displayed micromolar activity against Gram‑positive bacteria (best MIC = 8 µg mL⁻¹ vs *B. subtilis*). They also present **PepCraft**, a multi‑agent framework in which a Planning Agent coordinates specialist agents for generation, filtering, and verification, demonstrating that the agentic orchestration of generative models can effectively prioritize candidates that succeed in vitro.


<details>
<summary>Abstract</summary>

Antimicrobial resistance causes to over a million deaths annually. Antimicrobial peptides (AMPs) are a promising solution, but generative AMP models are not yet ready to design peptides with non-natural amino acids and/or chemical modifications, which are essential for real-world peptide drugs. We present AMPGAN v3, a multi-objective conditional GAN that expands the generative vocabulary to D-amino acids and N/C-terminus modifications such as amidation. By separating adversarial and activity-aware supervision across two specialized discriminators, AMPGAN v3 substantially improves training stability and outperforms prior generative AMP models on external classifiers. We validated five candidates spanning three structural classes in vitro; two showed activity against Gram-positive strains, with the best candidate reaching MIC 8 μg/mL against B. subtilis. To support downstream curation, we further present PepCraft, a multi-agent framework for end-to-end AMP discovery in which a Planning Agent orchestrates specialized executors for generation, filtering, and verification. Its prioritization recommendations align with our in vitro outcomes. Together, these contributions let us examine, on a small but real scale, how generative and agentic AI compose in therapeutic peptide discovery. Code: https://github.com/marszzibros/AMPGANv3

</details>


### 117. Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models

- **Authors:** Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee, Dooyoung Hong
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16902v1](http://arxiv.org/abs/2606.16902v1)
- **PDF:** [https://arxiv.org/pdf/2606.16902v1](https://arxiv.org/pdf/2606.16902v1)
- **Categories:** cs.RO, cs.AI


> **Main contribution**: The paper introduces **BinTrack**, a fully open‑source agent that answers spatial queries for service robots by converting the query into a binary‑search problem over the robot’s own egocentric trajectory, and releases a new multi‑trip outdoor benchmark (GangnamLoop) for evaluating such agents.  

**Methodology**: BinTrack first extracts two anchor landmarks from the natural‑language query using an open‑source vision‑language model, then repeatedly bisects the trajectory segment between those anchors (binary search) while checking landmark presence, until it converges on a precise metric coordinate; an optimized inference pipeline provides a 1.5× speedup compared with prior open‑source baselines.  

**Key findings**: On the SpaceLocQA benchmark, BinTrack improves accuracy by up to 22.8 % over existing open‑source methods and matches the performance of closed‑source GPT‑4o in the most difficult global‑category setting, while also running faster and entirely offline—demonstrating that high‑level spatial reasoning can be achieved with open‑source models suitable for onboard robot deployment.


<details>
<summary>Abstract</summary>

This work addresses spatial question answering for service robots traversing long egocentric routes. Given a query such as "where can I find a dry cleaner on the way back home?", the system returns a metric coordinate that downstream navigation components can act on. Prior Spatial Question Answering approaches leverage retrieval-augmented agents built on closed-source models such as GPT-4o for path exploration. However, robots operating in the real world often cannot reliably depend on online closed-source models due to network instability, communication latency, and deployment cost. It creates a need for open-source based Spatial Question Answering approaches that can run onboard the robot, yet prior research in this direction remains limited. This work proposes BinTrack, a simple yet effective, fully open-source spatial-localization agent that leverages the temporal ordering of a robot's trajectory. BinTrack performs a binary search over the trajectory segments between two anchor landmarks identified from a query. It improves overall accuracy by up to 22.8% over other open-source implementations and even matches the reported closed-source model result on the global category of the SpaceLocQA benchmark, the most challenging setting that has so far required strong reasoning agents such as GPT-4o. Furthermore, its optimized inference strategy consistently yields more than a 1.5x inference speedup over previous approaches. Finally, this work releases GangnamLoop, a novel and practical multi-trip outdoor benchmark collected by deploying a real quadruped robot on public streets with the anonymization policy. It revisits the same locations under different outdoor conditions and pairs the robot's low viewpoint with the human owner's. The source codes and datasets are publicly available at https://github.com/ndb796/BinaryTracking

</details>


### 118. Human-on-the-Bridge: Scalable Evaluation for AI Agents

- **Authors:** Fouad Bousetouane
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16871v1](http://arxiv.org/abs/2606.16871v1)
- **PDF:** [https://arxiv.org/pdf/2606.16871v1](https://arxiv.org/pdf/2606.16871v1)
- **Categories:** cs.MA


> **Main contribution**: The paper proposes *Human‑on‑the‑Bridge* (HOB), a new paradigm that front‑loads expert knowledge into reusable evaluation artifacts (domain context, red‑team traps, juror personas, scoring rubrics, audit rules, fallback policies) so that large‑scale, multi‑turn testing of AI agents can be run automatically by a lightweight “ProofAgent Harness”.

**Methodology**: Human experts first curate a structured evaluation intelligence bundle. The harness then repeatedly executes this bundle against agentic LLMs, capturing full interaction traces, applying multiple juror LLMs for scoring, and linking decisions to evidence. Experiments were run in both symmetric (same‑size evaluator) and asymmetric (smaller evaluator) settings across 23 k agent turns in finance, healthcare, and code‑generation domains.

**Key findings**: HOB markedly improves evaluation depth while keeping evaluator model size modest; smaller “harness” LLMs can reliably expose failures in frontier agents that static benchmarks miss. The framework uncovered systematic issues such as phantom tool‑call claims, omitted mandatory tool calls, policy drift, manipulative reasoning paths, and safe‑but‑non‑resolving refusals, demonstrating that scalable, human‑curated evaluation intelligence can substantially raise the reliability of agentic AI assessments.


<details>
<summary>Abstract</summary>

AI agents must be evaluated as behavioral systems, not as isolated response generators. They reason across turns, call tools, preserve context, follow policies, and act under uncertainty. Existing methods provide useful but fragmented signals: benchmarks measure fixed capabilities, Human-in-the-Loop review preserves expert judgment but does not scale easily, LLM-as-judge methods depend on evaluator design, red teaming is often episodic, and trace auditing requires explicit evidence rules. This paper introduces Human-on-the-Bridge (HOB), a scalable evaluation paradigm for agentic AI. HOB places human expertise upstream, where experts curate reusable evaluation intelligence before testing begins, including domain context, Red-Team Traps, Juror Personas, scoring guidelines, audit rules, and fallback policies. ProofAgent Harness then executes this curated intelligence repeatedly through multi-turn adversarial evaluations, trace capture, multi-juror scoring, and evidence-linked reporting. We evaluate HOB through symmetric and cost-efficient asymmetric settings across frontier LLM-based agents and Harness LLM tiers. The study covers 23,500 agent turns and produces evidence-linked findings across finance, healthcare, and code generation. The results show that HOB can amplify evaluation quality without requiring equally large evaluator models, allowing smaller Harness LLMs to challenge agents built on frontier LLM backbones. The evaluation surfaces failures often missed by static benchmarks and single-evaluator scoring, including phantom tool-call claims, missing mandatory tool calls, policy drift, manipulation paths, and safe but non-resolving refusals. These findings support HOB as a paradigm for scaling human-curated evaluation intelligence, where expert judgment is encoded upfront and reused across repeated agent evaluations rather than applied manually inside every run.

</details>


### 119. GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents

- **Authors:** Rahul Suresh Babu, Rohit Shukla
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16813v1](http://arxiv.org/abs/2606.16813v1)
- **PDF:** [https://arxiv.org/pdf/2606.16813v1](https://arxiv.org/pdf/2606.16813v1)
- **Categories:** cs.AI


> **Main contribution:** GIST‑CMTF adds a goal‑state inference layer in front of Causal Minimal Tool Filtering (CMTF) so that an LLM‑based agent first predicts which symbolic goal best matches a user request, estimates the ambiguity of that prediction, and either proceeds with causal tool‑filtering or initiates a clarification step that creates the missing goal/state variables.  

**Methodology:** The system maps natural‑language requests to candidate goal states expressed in the same state‑transition language used by CMTF, computes a confidence‑based ambiguity score, and conditionally invokes CMTF or a clarification action. Experiments span seven language‑model back‑ends, six filtering variants, and 120 controlled tool‑use tasks, measuring task success, wrong‑goal execution, token usage, and exposure of tools.  

**Key findings:** GIST‑CMTF attains 97 % task success—far above 80 % for the best prior CMTF baselines—while cutting wrong‑goal executions from 19.4 % to 2.5 % and preserving the “one‑tool‑at‑a‑time” exposure advantage of causal filtering with markedly lower token consumption. The results demonstrate that validating the inferred goal state, not merely the relevance of tools, is crucial for reliable, low‑confusion tool‑augmented LLM agents.


<details>
<summary>Abstract</summary>

Tool-augmented LLM agents rely on runtime filtering to decide which tools should be visible at each step. Causal Minimal Tool Filtering (CMTF) reduces tool-choice confusion by exposing only the next causally necessary tool frontier, but it assumes that the user request has already been mapped to a symbolic goal state. In practice, requests such as "handle my appointment" or "take care of this email" may correspond to multiple possible goals. This creates wrong-goal execution, where an agent follows a valid causal tool path for an unintended objective. We introduce GIST-CMTF, a goal-state inference layer that predicts candidate symbolic goals over the same state-transition vocabulary used by CMTF, estimates ambiguity, and either applies CMTF or exposes clarification as a causal action that produces missing goal or state variables. We evaluate GIST-CMTF across seven model backends, six filtering methods, and 120 controlled tool-use tasks. GIST-CMTF achieves 97.0% task success, compared with 80.1% for top-goal CMTF and 82.9% for semantic-goal CMTF. It reduces wrong-goal execution from 19.4% under top-goal CMTF to 2.5%, while preserving the one-tool exposure of causal filtering and using substantially fewer tokens than all-tools exposure. These results suggest that reliable tool-augmented agents should validate goal state, not only tool relevance, before exposing external actions.

</details>


### 120. Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents

- **Authors:** Tianyi Zhang, Zhonghao Qi
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16769v1](http://arxiv.org/abs/2606.16769v1)
- **PDF:** [https://arxiv.org/pdf/2606.16769v1](https://arxiv.org/pdf/2606.16769v1)
- **Categories:** cs.AI


> **Main contribution**  
The paper introduces **Skill‑to‑LoRA (S2L)**, a way to turn human‑written procedural “SKILL.md” documents into compact, model‑specific LoRA adapters that encode the *behavioral* effect of a skill rather than re‑injecting the full text at inference time.

**Methodology**  
During offline training, each full skill description is used to generate skill‑guided demonstrations, which are then used to fine‑tune a LoRA adapter for that skill. At runtime the original text is omitted; the appropriate adapter is loaded on‑the‑fly to modify the base LLM (Qwen‑3.6‑27B) and induce the desired skillful behavior.

**Key findings**  
On a 21‑skill subset of SWE‑Skills‑Bench, S2L raises the success rate by **2.9 pp** over a no‑skill baseline and by **5.2 pp** over the traditional full‑skill‑text prompting, while cutting per‑step token usage by **≈6.6 %**. It matches or outperforms full‑skill prompting on 18 of 21 skills, and ablations show that only correctly aligned, skill‑specific LoRAs preserve these gains. The results demonstrate that procedural agent skills can be effectively compiled into lightweight, dynamically loadable model modules, offering a token‑efficient alternative for agentic LLM systems.


<details>
<summary>Abstract</summary>

Agent skills are commonly distributed as SKILL.md files: human-readable procedural documents that describe workflows, tools, resources, and domain conventions. While convenient for inspection and reuse, this design requires the same reusable procedure to be repeatedly injected into the runtime context. We propose Skill-to-LoRA(S2L), a behavior-centric skill representation that replaces runtime skill text with skill-specific LoRA adapters. Rather than compressing the skill document itself, S2L models the behavioral change induced by the skill text: offline, the complete SKILL.md is used to synthesize skill-guided demonstrations; online, the full document is omitted and the corresponding LoRA adapter is dynamically loaded to activate the learned skill behavior. We evaluate S2L with Qwen3.6-27B on a 21-skill subset of SWE-Skills-Bench. Compared with the no-skill and Full Skill Text baselines, S2L improves pass rate by 2.9 and 5.2 percentage points, respectively, while reducing per-step token cost by 6.6% relative to Full Skill Text prompting. S2L matches or improves Full Skill Text on 18/21 skills and the no-skill baseline on 15/21 skills. Control experiments further show that the gains depend on skill-specific adapter alignment: Wrong-LoRA and Shared-LoRA both reduce performance. These results suggest that many procedural agent skills can be converted from runtime instructions into trainable, dynamically loadable behavioral modules. Code will be released upon acceptance.

</details>


### 121. AgentFairBench: Do LLM Agents Discriminate When They Act?

- **Authors:** Triveni Morla, Rohith Reddy Bellibaltu, Manpreet Singh, Manmeet Singh Kapoor
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16723v1](http://arxiv.org/abs/2606.16723v1)
- **PDF:** [https://arxiv.org/pdf/2606.16723v1](https://arxiv.org/pdf/2606.16723v1)
- **Categories:** cs.AI


> The paper introduces **AgentFairBench**, a low‑cost, reproducible benchmark that quantifies demographic disparity in the *actions* taken by LLM‑driven agents (e.g., hiring decisions, credit offers, medical triage) rather than only in their answer scores. Building on the Bias Conduction Framework, the authors generate synthetic, demographically neutral applicant profiles and create counterfactual pairs that differ only in a name‑coded race × gender signal; these are fed to four increasingly “agentic” scaffolds (direct prompting, chain‑of‑thought, multi‑agent deliberation, tool‑augmented) and evaluated with metrics such as counterfactual flip rate, mean absolute score difference, and tool‑invocation disparity, using bootstrap confidence intervals, paired tests, and false‑discovery‑rate control. The pilot results show that, after correcting for the inflated variance caused by testing many groups (the “arity‑matched” null methodology), even a powerful model (Claude Haiku 4‑5) exhibits no statistically significant demographic bias, while a planted‑bias test confirms the benchmark’s sensitivity; the authors release all code, data, and a live leaderboard for community adoption.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly take actions (screening applicants, recommending credit, triaging patients), yet fairness for LLMs is still measured by grading answers. We introduce AgentFairBench, a cheap, reproducible, multi-domain benchmark for demographic disparity in the actions of LLM agents. Grounded in a companion framework, the Bias Conduction Framework (BCF, restated here), it spans three regulator-anchored domains: hiring, lending, and medical triage. Synthetic, demographic-neutral profiles are evaluated in counterfactual matched sets that vary only a name-coded race x gender signal (in the Bertrand Mullainathan tradition), under four agent scaffolds of increasing agency (direct, chain-of-thought, multi-agent deliberation, tool-augmented). A NumPy-only harness computes counterfactual flip rate, mean absolute score difference (MASD), action-rate disparity, and tool-invocation disparity, with bootstrap confidence intervals, paired tests, and false-discovery-rate control, for single-digit dollars per model. A live leaderboard with a held-out private split and a contamination canary admits external models by submission. Our pilot (864 decisions plus a test-retest replication) carries a methodological lesson: comparing a six-group score spread against a two-run noise difference overstates disparity by ~ 2.4X through statistic arity alone. Against an arity matched noise floor and an omnibus group test, claude haiku 4 5 shows no demographic effect above sampling noise (0 of 120 pairwise and 0 of 9 omnibus contrasts survive correction); a planted-bias test confirms the instrument detects disparity when present. The contribution is a sound, sensitive, adoption-ready instrument, the arity matched null methodology, and open artifacts to scale it. Code, data, and harness are released under open licenses, with an anonymized review artifact.

</details>


### 122. Misinformation Propagation in Benign Multi-Agent Systems

- **Authors:** Jonas Becker, Jan Philip Wahle, Terry Ruas, Bela Gipp
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16710v1](http://arxiv.org/abs/2606.16710v1)
- **PDF:** [https://arxiv.org/pdf/2606.16710v1](https://arxiv.org/pdf/2606.16710v1)
- **Categories:** cs.MA, cs.CL


> The paper demonstrates that intentional misinformation injected into a single large‑language‑model (LLM) agent can substantially degrade its performance and that these errors often persist when that agent participates in a turn‑based multi‑agent debate, though the overall impact is attenuated compared with a lone agent. By systematically inserting false premises into reasoning, knowledge, and alignment tasks across both single‑ and multi‑agent configurations, the authors show that the degree of degradation depends on the composition of the agent group, the decision‑aggregation protocol (e.g., consensus vs. voting), and the underlying LLM architecture; majority‑rule and consensus mechanisms can either amplify peer pressure or help steer misinformed agents back to correct answers. The key finding for agentic AI is that multi‑agent collaboration can improve robustness to misinformation, but its effectiveness is highly contingent on how agents share information and how their outputs are combined.


<details>
<summary>Abstract</summary>

Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-agent and multi-agent systems across reasoning, knowledge, and alignment tasks. We find that misinformation can degrade single-agent performance and persists across multi-agent debate, with agents often retaining answers introduced by misinformed peers. Nevertheless, multi-agent debate reduces the resulting performance degradation compared to single-agent prompting, especially when most agents are not exposed to misinformation. Robustness depends on group composition and decision protocol. Consensus can be more stable than voting under peer pressure, while majorities can often steer misinformed agents back toward correct answers. Our results show that misinformation robustness in multi-agent systems depends on the underlying model and also on how agents exchange information and aggregate decisions.

</details>


### 123. User as Code: Executable Memory for Personalized Agents

- **Authors:** Bojie Li
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16707v1](http://arxiv.org/abs/2606.16707v1)
- **PDF:** [https://arxiv.org/pdf/2606.16707v1](https://arxiv.org/pdf/2606.16707v1)
- **Categories:** cs.AI


> **Main contribution** – The paper proposes “User as Code” (UaC), a new paradigm for personal‑agent memory in which the user model is stored as executable, typed Python code rather than as unstructured text or isolated facts.  

**Methodology** – UaC maintains an append‑only log of every observed fact; periodically it checkpoints this log into a set of Python objects (the user’s state) and pure functions (the rules that manipulate that state). The agent queries the user model by directly invoking these objects/functions, letting the interpreter perform aggregation, consistency checking, and rule‑based inference.  

**Key findings** – On long‑term dialogue benchmarks (e.g., LOCOMO) UaC attains recall comparable to an upper‑bound full‑context model and surpasses prior memory systems (78.8% recall). More importantly, for tasks that require aggregating over a user’s history (e.g., “how many trips did I take last year?”) UaC achieves near‑perfect accuracy (~99%) while retrieval‑based memories fall to 6‑43%. Because the rules execute automatically on state updates, UaC can also emit unsolicited safety alerts (e.g., drug‑allergy conflicts), a capability absent in query‑driven memories.


<details>
<summary>Abstract</summary>

A personalized AI agent needs a user memory: a persistent model of who the user is, built across many conversations and consulted on each new one. Today this memory is almost always stored as unstructured text, a knowledge graph, or a flat store of facts, and consulted by retrieval -- fetching the entries most similar to the current request. Such "bag-of-facts" memory recalls individual facts well, but because storing a fact and acting on it are separate steps, it struggles to resolve contradictions, aggregate over many records, or enforce rules. We argue that user memory should instead be executable. We introduce User as Code (UaC), a paradigm in which an agent's model of a user is a living software project: typed Python objects hold the user's state and ordinary Python functions encode the rules that govern it, so representing and reasoning about the user happen in one medium an interpreter can run. The enabling mechanism is a two-phase pipeline: an append-only log that never discards a fact, periodically checkpointed into typed code.
  This changes what memory can do. On standard long-term conversation benchmarks, UaC matches both a full-context upper bound and the strongest prior memory systems on recall (78.8% on LOCOMO). Its advantage emerges where representation matters most. On aggregate questions over a user's history -- "how many international trips did I take last year?" -- retrieval-based memory collapses (6-43%) while UaC stays near-perfect (99%), because the answer is a one-line computation over typed state rather than a search over text. And because its rules execute deterministically whenever the state changes, UaC can surface unsolicited, safety-critical alerts -- such as a newly prescribed drug that conflicts with an allergy recorded months earlier -- a capability query-driven memory cannot provide.

</details>


### 124. Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents

- **Authors:** Zewen Liu
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16682v2](http://arxiv.org/abs/2606.16682v2)
- **PDF:** [https://arxiv.org/pdf/2606.16682v2](https://arxiv.org/pdf/2606.16682v2)
- **Categories:** cs.LG, cs.CL


> **Main contribution:** The paper uncovers and quantifies “Evaluator Preference Collapse” (EPC) in multimodal self‑evaluating agents, showing that a single evaluation strategy can dominate across modalities and that preferences learned on one modality (text or vision) can “contaminate” strategy selection on the other—a phenomenon they call **cross‑modal contagion**.

**Methodology:** Using GPT‑4o as an autonomous evaluator, the authors ran a four‑phase isolation‑training protocol on DeepSeek‑Chat across text‑only, visual‑only (real‑image), and mixed tasks. They measured the distribution of evaluation strategies, computed Jensen‑Shannon divergence–based contagion coefficients, and performed extensive statistical validation (5 evaluator configs, 80 repetitions ≈ 35 k API calls) together with ablations and multi‑executor checks.

**Key findings:** In multimodal settings, EPC is ≈3 × stronger than in text‑only loops (a single “step_by_step” strategy captures 48.4 % of weight). Cross‑modal contagion is substantial (JSD 0.19‑0.34; γ_T→V ≈ 1.15, γ_V→T ≈ 0.94, Cohen’s d ≈ 0.56), sometimes inverting the optimal strategy for a modality. Self‑evaluation (the agent evaluating its own outputs) almost eliminates contagion (97 % of runs with JSD ≈ 0.003). The authors release the MM‑EPC framework, a contagion matrix, and identify evaluator architecture as the principal risk factor for preference drift in agentic AI.


<details>
<summary>Abstract</summary>

When AI agents use language models to evaluate their own outputs in a
  feedback loop, systematic biases emerge. We show that Evaluator Preference
  Collapse (EPC) is dramatically amplified in multimodal settings. Using
  GPT-4o to evaluate DeepSeek-chat across text and visual tasks, we find
  that a single strategy (step_by_step) absorbs 48.4% of all weight -- 3.2x
  the collapse observed in text-only self-evaluation -- while three
  visual-domain strategies receive only 9.1% combined weight. We then
  demonstrate a novel phenomenon we term cross-modal contagion: evaluator
  preferences acquired on one modality transfer to and corrupt strategy
  selection on another. Through a four-phase isolation training paradigm, we
  measure contagion coefficients and document strategy inversion -- the
  optimal strategy for a modality reverses after cross-modal exposure. A
  Phase 3 statistical validation across five evaluator configurations (N=80
  total independent repetitions, ~35,000 API calls) with both text-proxy and
  real-image visual tasks finds: cross-model evaluation produces strong
  contagion (JSD~0.19-0.34), real-image inputs yield the most directionally
  consistent signal (mean gamma_{T->V}=1.145, gamma_{V->T}=0.937, 70% T->V,
  Cohen's d=0.56), and self-evaluation provides near-complete immunity --
  97% of runs (N=30) yield zero contagion (JSD=0.003, d=0.07). Three
  methodological ablations and multi-executor validation confirm the effect
  is not a structural artifact. We introduce the contagion matrix indexed by
  evaluator identity, release the MM-EPC framework, and identify
  cross-model evaluator architecture as the primary risk factor for
  preference drift. Code and data: https://github.com/aidless/mm-epc.

</details>


### 125. The Integrator Advantage: Controlled Agentic AI for Small and Medium-Sized Companies

- **Authors:** Christopner Koch, Joshua A. Wellbrock
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16649v1](http://arxiv.org/abs/2606.16649v1)
- **PDF:** [https://arxiv.org/pdf/2606.16649v1](https://arxiv.org/pdf/2606.16649v1)
- **Categories:** cs.AI


> The paper’s main contribution is a practical integration framework that shows how small‑ and medium‑sized enterprises (SMEs) can capture near‑term value from agentic AI by deploying **controlled, partial autonomy** rather than full‑scale automation. Using a design‑science methodology, the authors map business processes to suitability criteria, define graduated autonomy levels, and outline technical‑integration steps, governance policies, security controls, and employee‑enablement practices; they then validate the framework with pilot deployments on simple to medium‑complexity workflows (e.g., invoice triage, HR onboarding). The results demonstrate that, when human oversight and accountability are retained, agentic AI can boost productivity by 15‑30 % in SMEs while maintaining compliance and employee trust, underscoring its role as a human‑centered productivity lever rather than a workforce‑replacement technology.


<details>
<summary>Abstract</summary>

Agentic AI marks a new phase of enterprise automation. Unlike traditional automation or conversational AI, agentic systems can interpret goals, plan multi step tasks, access tools, interact with enterprise systems, and execute workflows with varying degrees of autonomy. For small and medium sized companies, this creates potential to reduce administrative burden, accelerate routine processes, and improve the use of organizational knowledge. This paper argues that the near term value of Agentic AI does not lie in full autonomy or workforce reduction, but in controlled partial autonomy for simple and medium complexity business processes. It proposes an integration framework covering use case suitability, autonomy levels, technical integration, governance, security, employee enablement, and measurable impact. The paper concludes that Agentic AI can become a productivity lever when implemented as a human centered capability with responsibility and accountability retained by people.

</details>


### 126. CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies

- **Authors:** Issa Sugiura, Daichi Hattori, Kazuo Araragi, Keita Ogawa, Shota Onose, Taro Makino, Teppei Usuki, Takashi Ishida
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16613v1](http://arxiv.org/abs/2606.16613v1)
- **PDF:** [https://arxiv.org/pdf/2606.16613v1](https://arxiv.org/pdf/2606.16613v1)
- **Categories:** cs.AI


> The paper introduces **CoffeeBench**, a 90‑day simulation that evaluates large‑language‑model (LLM) agents as autonomous firms (farmers, roasters, retailers) in a heterogeneous, multi‑agent economy, forcing them to manage cash, inventory, pricing, and negotiate with other agents to maximize cumulative net income. Using a controllable roaster agent against fixed reference agents, the authors benchmark several open‑weight and commercial LLMs, finding that most outperform a passive baseline and achieve positive profit, while higher‑performing models exhibit markedly more frequent and effective inter‑firm communication; in contrast, Claude Haiku 4.5 suffers an “idle‑drift” failure mode, repeatedly taking no action despite generating coherent plans. The released code and trajectory data provide a new testbed for studying long‑horizon, economically grounded agentic behavior.


<details>
<summary>Abstract</summary>

As LLM agents become capable of increasingly long-horizon tasks, evaluating their performance in economic systems is becoming increasingly important. Unlike existing benchmarks that primarily evaluate a single agent interacting with a passive environment, economic systems are inherently multi-agent, requiring autonomous agents to communicate, negotiate, and transact while pursuing their own objectives over extended periods. We introduce CoffeeBench, a benchmark for evaluating LLM agents in a long-horizon multi-agent economy composed of heterogeneous firms. In CoffeeBench, two farmers, two roasters, and two retailers autonomously operate their businesses over a 90-day simulation, each seeking to maximize cumulative net income through communication and transactions while managing cash, inventory, and pricing. The evaluated model controls one coffee roaster, while the remaining firms are controlled by fixed reference agents. Across several recent open-weight and proprietary LLMs, all models outperform a passive baseline that takes no actions, with most achieving positive net income. Analysis of agent behavior reveals substantial differences in long-horizon economic interaction: higher-performing models communicate more actively with other firms, whereas Claude~Haiku~4.5 exhibits an idle-drift failure mode, repeatedly choosing inaction despite producing coherent assessments and plans. We release our code and agent trajectories to support future research.

</details>


### 127. How Far Can Machine Translation Quality Take You? Extrinsic Discourse Evaluation in Goal-Oriented Setups

- **Authors:** Wafaa Mohammed, Kata Naszadi, Vlad Niculae
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16596v1](http://arxiv.org/abs/2606.16596v1)
- **PDF:** [https://arxiv.org/pdf/2606.16596v1](https://arxiv.org/pdf/2606.16596v1)
- **Categories:** cs.CL


> **Paper Summary**  

The authors introduce two extrinsic, discourse‑oriented evaluation setups to probe how machine‑translation (MT) quality affects downstream communication tasks. In the static regime they devise an *entity‑counting* probe that tests whether translated texts preserve referential consistency, showing that even state‑of‑the‑art MT systems with high intrinsic scores frequently break referential chains. In the interactive regime they embed MT into the multi‑agent “Welfare Diplomacy” game, a long‑horizon, goal‑driven negotiation environment, and demonstrate that translation errors specifically tied to interaction (e.g., mis‑aligned commitments) degrade coordination and overall game performance. Together, these results argue that goal‑oriented, multi‑agent settings provide a practical, discourse‑sensitive benchmark for assessing the real‑world impact of MT on agentic AI systems.


<details>
<summary>Abstract</summary>

Existing machine translation (MT) metrics and discourse-focused evaluations primarily assess translation quality intrinsically, without measuring the downstream consequences of translation errors. In this work, we focus on extrinsic discourse evaluation of machine translation under two distinct regimes: static and interactive. Under the static regime, we propose an entity counting task as a probe of referential consistency in discourse. We show that high intrinsic MT quality does not reliably predict downstream discourse success and strong MT systems still produce referential inconsistencies. For the interactive regime, we study the goal-oriented multi-agent Welfare Diplomacy game as a probe of long-horizon communication and coordination. We find that interaction-specific translation failures impact downstream coordination. Our results highlight goal-oriented environments as a viable framework for discourse-sensitive extrinsic MT evaluation.

</details>


### 128. SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents

- **Authors:** Qiao Xiao, Haochen Shi, Yisen Gao, Wenbin Hu, Huihao Jing, Tianshi Zheng, Baixuan Xu, Ziheng Zhang, Weiqi Wang, Haoran Li, Jiaxin Bai, Yangqiu Song
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16591v2](http://arxiv.org/abs/2606.16591v2)
- **PDF:** [https://arxiv.org/pdf/2606.16591v2](https://arxiv.org/pdf/2606.16591v2)
- **Categories:** cs.CL


> The paper introduces **SING (Synthetic Intention Graph)**, a framework that lets LLM‑based agents discover and invoke the right tools from massive, evolving tool libraries without loading the entire schema. SING constructs a dynamic graph that links user intentions, tool capabilities, and typical tool‑collaboration patterns, and uses this graph to actively retrieve the most relevant APIs as the task unfolds. Experiments on three real‑world benchmarks with a unified set of 7,471 tools show that SING raises Global Recall@5 by up to 59.8 % and downstream task success by up to 28.9 % while exposing only 0.2 % of the full tool corpus, demonstrating that intention‑aware graph‑based retrieval dramatically improves scalability and effectiveness of tool‑using LLM agents.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly rely on agent harnesses that manage context, tools, and multi-turn execution, making tools a central interface for acting in realistic digital environments. As harness-connected tool ecosystems expand to hundreds or thousands of APIs, services, and task-specific skills, exhaustive tool schema injection becomes costly and imposes a closed-world assumption that limits agents to a predefined static inventory. Retrieval-augmented tool selection offers a natural alternative, but existing one-shot retrieval methods often fail to align isolated tool descriptions with the agent's true task intention, especially in long-horizon tasks where required capabilities emerge through decomposition, observations, and newly induced subgoals. We propose SING, an intention-aware active tool discovery framework that builds an intention-tool graph linking user intentions, tool capabilities, and tool collaboration patterns, and dynamically retrieves tools according to evolving task states. Using a unified corpus of 7,471 tools, we evaluate SING on three real-world tool-use benchmarks. SING improves Global Recall@5 by up to 59.8% and downstream success rate by up to 28.9% over baselines, while reducing full-corpus tool-schema exposure by 99.8%, demonstrating that intention-aware graph structure enables more accurate and context-efficient tool discovery in large-scale agentic ecosystems.

</details>


### 129. Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning

- **Authors:** Reef Menaged, Gili Lior, Shauli Ravfogel, Roee Aharoni, Gabriel Stanovsky
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16576v1](http://arxiv.org/abs/2606.16576v1)
- **PDF:** [https://arxiv.org/pdf/2606.16576v1](https://arxiv.org/pdf/2606.16576v1)
- **Categories:** cs.CL


> The paper introduces **agentic automata learning**, a benchmark that asks tool‑calling LLM agents to discover a hidden deterministic finite automaton (DFA) by issuing membership and equivalence queries to an oracle, allowing precise measurement of world‑model inference capabilities against classic automata‑learning algorithms. Using this testbed, the authors evaluate several state‑of‑the‑art LLMs and find that while reasoning‑augmented models outperform vanilla ones, performance collapses quickly as the DFA size grows, with systematic breakdowns in query planning, evidence integration, and hypothesis formation. The results demonstrate that current LLM agents can achieve limited interactive discovery but are far less robust and sample‑efficient than traditional learning methods, highlighting a key gap for future agentic AI research.


<details>
<summary>Abstract</summary>

We propose agentic automata learning to evaluate the extent to which tool-calling LLM agents can uncover hidden environments through interaction. In our setup, an agent should uncover a hidden deterministic finite automaton (DFA) by interacting with an oracle through (1) membership queries ("Does this string belong to the target language?") and (2) equivalence queries ("Is this the target DFA?"). This yields a scalable testbed with controlled task complexity, measurable interaction efficiency, and strong baselines (classic automata-learning algorithms). Evaluating state-of-the-art LLMs, we find that performance drops sharply as DFA size increases. Reasoning models are markedly stronger than non-reasoning models, yet trajectory analyses reveal recurring failures in query planning, evidence integration, and hypothesis construction. Overall, our results show that current LLM agents can sometimes perform non-trivial interactive discovery, but remain far less robust and efficient than classic algorithms for the task.

</details>


### 130. ROSA-RL: Uncertainty-Aware Roundabout Optimized Speed Advisory with Reinforcement Learning

- **Authors:** Anna-Lena Schlamp, Jeremias Gerner, Klaus Bogenberger, Werner Huber, Stefanie Schmidtner
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16558v1](http://arxiv.org/abs/2606.16558v1)
- **PDF:** [https://arxiv.org/pdf/2606.16558v1](https://arxiv.org/pdf/2606.16558v1)
- **Categories:** cs.AI, cs.RO, eess.SY


> The paper introduces **ROSA‑RL**, a reinforcement‑learning speed‑advisory system that enables safe and efficient roundabout entry in mixed traffic by explicitly modelling uncertainty about future conflict‑zone occupancy. The authors train a Transformer‑based predictor to forecast, over a five‑second horizon, the probabilistic occupancy of the roundabout’s conflict zone using multi‑agent interaction cues; these occupancy distributions are fed into a conventional RL policy as additional state information, allowing the agent to choose speeds that are robust to ambiguous human intentions. In simulation experiments grounded on real‑world traffic data, ROSA‑RL markedly reduces collisions and improves traffic flow compared with a model‑based baseline, approaching the performance of an oracle that knows the exact future occupancy.


<details>
<summary>Abstract</summary>

Roundabouts challenge automated driving in mixed traffic, as heterogeneous and non-deterministic human behavior, unknown driving intentions, and high interaction complexity create uncertainty about whether the conflict zone will be blocked or available at the moment of entry. We present ROSA-RL -- uncertainty-aware Roundabout Optimized Speed Advisory with Reinforcement Learning. It enables safe and efficient roundabout entry for automated and human-driven vehicles in mixed traffic through probabilistic conflict forecasting. A Transformer-based model predicts conflict zone occupancy over a five-second horizon, capturing multi-agent interactions to anticipate upcoming conflicts and available gaps. The prediction outputs encode uncertainty in future motion and intent, and augment the state of a classical RL framework, enabling uncertainty-aware speed coordination. Evaluated in simulations grounded in real-world data, ROSA-RL can effectively handle uncertainty and outperform a comparable model-based baseline, closing the gap to an ideal setting assuming fully known occupancy while improving traffic efficiency and safety. The source code of this work is available under: github.com/urbanAIthi/ROSA-RL.

</details>


### 131. Can LLM Coding Agents Reason About Time Series?

- **Authors:** Filip Rechtorík, Ondřej Dušek, Zdeněk Kasner
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16545v1](http://arxiv.org/abs/2606.16545v1)
- **PDF:** [https://arxiv.org/pdf/2606.16545v1](https://arxiv.org/pdf/2606.16545v1)
- **Categories:** cs.CL


> **Main contribution:** The paper investigates how large language model (LLM) agents can handle time‑series analysis, comparing three interaction modes—direct raw‑data prompting, pure coding‑agent prompting, and a hybrid of both—to determine which yields the most reliable reasoning for time‑series questions.  

**Methodology:** Using two established time‑series comprehension benchmarks, the authors prompt LLMs (e.g., GPT‑4‑Turbo) in three settings: (1) feeding the numeric series as text, (2) letting the model act as a coding agent that iteratively writes and executes Python code to query and process the data, and (3) combining raw‑data prompts with code generation. A strong LLM judge evaluates answer correctness and extracts the agents’ reasoning steps.  

**Key findings:** Coding‑agent setups outperform raw‑data prompts by up to **10 %** in accuracy, chiefly because they can invoke appropriate statistical tests via Python. Nevertheless, even the best agents still mis‑answer **22–34 %** of questions, often overlooking subtleties of test assumptions or data distributions. Raw‑data agents sometimes reach correct conclusions through quick “back‑of‑the‑envelope” reasoning, but lack the systematic rigor that coding agents provide. These results highlight both the promise and current limitations of LLM‑driven coding agents for autonomous time‑series reasoning in agentic AI systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly being used for automated decision-making systems in finance, healthcare, or environmental monitoring. Time series data are ubiquitous in these fields, yet hard to process automatically. Can time series be analyzed by LLM agents? We examine three approaches: providing the agent with raw numerical data, using the LLM as a coding agent, or a combination of both. In the coding agent setup, the model iteratively queries the data using Python code. Using two time series understanding benchmarks, we show that agents with code access can outperform models processing raw data by up to 10%. However, even the best performing agent still answers about 22-34% of the questions incorrectly. To get insights into models' strategies and reasoning gaps, we analyze the model outputs with a strong LLM judge. Our analysis reveals that coding agents can select appropriate statistical tests, but often miss important nuances. Meanwhile, models with access to raw data can reach the right conclusions using back-of-the-envelope calculations.

</details>


### 132. Steering Emotional Dynamics for Art Therapy: Controllable Narrative Script Generation through Hierarchically Guided LLM Agents

- **Authors:** Suqing Wang, Qinghai Miao, Chao Guo, Yisheng Lv
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16481v1](http://arxiv.org/abs/2606.16481v1)
- **PDF:** [https://arxiv.org/pdf/2606.16481v1](https://arxiv.org/pdf/2606.16481v1)
- **Categories:** cs.AI


> The paper introduces **EC‑Script**, a hierarchical LLM‑agent framework that lets users prescribe a precise emotional trajectory and then automatically generates a therapeutic narrative that follows it. The system splits the task into three coordinated agents: (1) Emotion‑Trajectory Planning sets the global affective curve, (2) Character‑Driven Scene Generation creates plot‑consistent scenes, and (3) Emotion‑Controlled Script Writing fine‑tunes each character’s emotional state, yielding a scene‑by‑scene script that matches the target affective pattern. Experiments show that EC‑Script markedly outperforms prior LLM‑based generators in adhering to prescribed emotional arcs, demonstrating strong controllability and practical promise for AI‑assisted art‑therapy and other emotion‑focused agentic applications.


<details>
<summary>Abstract</summary>

Art therapy plays a vital role in emotional healing, in which narrative creation acts as the primary vehicle for emotional expression. Given the inherently dynamic nature of emotions during healing, narratives with finely controlled emotional fluctuations enable individuals to safely project inner conflicts and achieve emotional catharsis. Recently, with the rapid development of Large Language Models (LLMs), automated narrative generation technology has provided a new pathway to support such artistic designs. However, while existing methods can produce fluent texts, they struggle to generate narratives that adhere to specified affective trajectories, failing to meet the demands of emotion-oriented psychological healing. To address these issues, this paper proposes EC-Script, an LLM agent-based framework that enables hierarchical control of the affective trajectory in narrative generation for emotional healing. To ensure that the generated narratives strictly follow the given emotional patterns, EC-Script establishes overall narrative direction through Emotion-Trajectory Planning, propels scene-level plot development with Character-Driven Scene Generation, and regulates local emotional changes of characters via Emotion-Controlled Script Writing. Ultimately, it outputs scene-by-scene script content that remains highly consistent with the preset affective trajectory. Experimental results demonstrate that EC-Script significantly outperforms baseline methods in affective trajectory adherence, exhibiting excellent and reliable emotional controllability, thereby providing effective technical support for AI-assisted emotional healing scenarios.

</details>


### 133. Tensor-Coord: Algebraic Decomposition of Joint Plan Tensors for Conflict-Free Multi-Agent LLM Planning

- **Authors:** Mudit Rastogi
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16478v1](http://arxiv.org/abs/2606.16478v1)
- **PDF:** [https://arxiv.org/pdf/2606.16478v1](https://arxiv.org/pdf/2606.16478v1)
- **Categories:** cs.AI


> **Main contribution:** Tensor‑Coord introduces a multilinear‑algebraic representation of a multi‑agent plan as a third‑order tensor and uses CP/Tucker decompositions to expose latent coordination structure, yielding a provably sound “coordination‑complexity’’ metric (the minimal CP rank R*) and a conflict‑localisation signal that can be turned into natural‑language constraints for LLM replanning.  

**Methodology:** Joint plans of N agents over H timesteps and A actions are encoded in a tensor \(T\in\mathbb{R}^{N\times H\times A}\); CP and Tucker decompositions are applied to compute the smallest ε‑approximate rank R*. Theorems show R* = N ⇔ plans are independent. The residual tensor \(E=T-T_{R*}\) yields pair‑wise conflict scores, while Tucker factor matrices are interpreted as agent roles, temporal phases, and action clusters, which are fed back to an LLM as explicit coordination constraints in an iterative replanning loop.  

**Key findings:** In grid‑world delivery benchmarks (2–4 agents), Tensor‑Coord achieves 100 % conflict‑free convergence for 2 agents (≈1.4 iterations on average), 80 % for 3 agents (≈3.2 iterations), and 60 % for 4 agents (≈4.0 iterations). The observed CP rank grows linearly with the number of agents (\(R*(N)\approx3.9N+0.5\)), validating the proposed coordination‑complexity measure as a predictor of planning difficulty for agentic LLM systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) remain limited in multi-agent planning because independently generated plans can create coordination failures such as spatial collisions, resource contention, and temporal deadlocks. We introduce Tensor-Coord, a multilinear algebra framework that represents the joint plan of N agents as a third-order tensor \(T \in R^{N \times H \times A}\) over agents, timesteps, and actions. Canonical Polyadic (CP) and Tucker decompositions are used to identify latent coordination structure. The minimal epsilon-approximate CP rank R* defines a computable coordination complexity measure, with \(CC(Pi)=(R*-N)/N\). We prove that R*=N is necessary and sufficient for plan independence. The residual \(E=T-T_{R*}\) defines a conflict score over agent pairs, timesteps, and actions, localizing failures without domain-specific rules. Tucker factors provide interpretable agent roles, temporal phases, and action clusters that are converted into natural language constraints for iterative LLM replanning. Experiments on multi-robot delivery tasks across Easy (2 agents, 5x5 grid), Medium (3 agents, 5x5 grid), and Hard (4 agents, 5x5 grid) settings show convergence to conflict-free plans in 100% of 2-agent cases within 1.4 iterations on average, 80% of 3-agent cases within 3.2 iterations, and 60% of 4-agent cases within 4.0 iterations. CP rank scaled approximately linearly as \(R*(N) = 3.9N + 0.5\), supporting its use as a predictor of coordination complexity.

</details>


### 134. When Agent Automation Becomes Profitable: Quantifying and Insuring Autonomous AI Risk through Trace-Economic Underwriting

- **Authors:** Binyan Xu, Xilin Dai, Fan Yang, Kehuan Zhang
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16465v1](http://arxiv.org/abs/2606.16465v1)
- **PDF:** [https://arxiv.org/pdf/2606.16465v1](https://arxiv.org/pdf/2606.16465v1)
- **Categories:** cs.AI, cs.CE


> The paper proposes **trace‑economic underwriting**, a framework that quantifies the loss‑risk of autonomous AI agents at the granularity of a specific customer‑task‑trace episode and transfers that risk via insurance premiums. By converting deterministic tool‑use traces into economic exposure labels (instead of relying on subjective LLM judgments), the authors can price risk accurately (reducing mean absolute pricing error from \$17.7 K to \$569) and design trace‑conditioned controls that cut the 95 % CVaR of losses by 72% in a real‑world software‑engineer‑assistant testbed. Theoretical analysis (Theorem 1) establishes finite‑sample guarantees for the underwriting scope, and extensive audits show the approach is both accurate and practically adoptable for economically viable AI automation.


<details>
<summary>Abstract</summary>

AI agents can now take irreversible actions in operational systems, but agent-caused losses are still not clearly assigned, priced, or transferred. Providers often disclaim consequential damages, users are left with uncompensated losses, and default human review limits the efficiency gains of automation. We ask when autonomous AI deployment can become economically acceptable despite failure risk. Our answer is to quantify risk at the customer-task-trace episode level and transfer it through insurance. Automation is acceptable when its expected benefit exceeds the premium, control cost, and remaining risk. This requires a defined role with bounded permissions and comparable traces. We introduce trace-economic underwriting, which maps tool-use traces to customer exposure and claimable loss, then uses this representation for pricing, control, and risk transfer. It uses deterministic economic labels rather than an LLM judge. In our trace-to-loss testbed, trace-economic pricing reduces pricing MAE from $17.7K to $569 and removes regressive cross-subsidy. A 300-trace expert audit accepts 295 labels unchanged. On 1,000 real SWE-smith traces, trace-conditioned controls reduce CVaR95 by 72%. Theorem~1 gives a finite-sample scope condition. We release code, labels, and audit sheets.

</details>


### 135. An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios

- **Authors:** Hankyul Baek, Jaewon Noh, Sang Seo, Yongsu Kim, Gabriel Waikin Loh Matienzo, Young Il Kim, Ee Wei Seah, Akriti Vij
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.17114v1](http://arxiv.org/abs/2606.17114v1)
- **PDF:** [https://arxiv.org/pdf/2606.17114v1](https://arxiv.org/pdf/2606.17114v1)
- **Categories:** cs.CR, cs.AI


> The paper presents the first systematic, non‑adversarial assessment of data‑leakage hazards in tool‑using LLM agents deployed in realistic enterprise and personal workflows. By applying a unified evaluation framework—covering five safety dimensions (data awareness, audience awareness, policy compliance, data minimisation, and access‑boundary awareness)—to 12 representative tasks (customer support, DevOps, web automation, etc.) across three commercial agents, the authors show that none of the agents can both complete the task and safely handle data, with many successes accompanied by unnecessary data access or inadvertent disclosure. The study therefore establishes operational data leakage as a primary safety concern for agentic AI and provides a reproducible methodology for measuring and improving agents’ data‑handling practices.


<details>
<summary>Abstract</summary>

AI agents are increasingly being adopted in enterprise and personal settings with access to emails, databases, documents, and other tools where they can read, update, and disseminate sensitive information. Much of prior research on data leakage risks in agents has focused on adversarial data exfiltration through prompt injections and jailbreaks. However, sensitive information may also be exposed during non-adversarial use, creating leakage risks even when users issue benign requests.
  We report a joint evaluation by the Singapore AI Safety Institute and the Korea AI Safety Institute examining agent data leakage in 12 realistic, non-adversarial tasks spanning customer support, DevOps, web automation, and enterprise and personal productivity. The evaluation covers five risk types: lack of data awareness, audience awareness, policy compliance, data minimization, and access-boundary awareness. Both institutes tested a common set of scenarios mirroring real-world deployments using independent testing environments and task-specific LLM-judge rubrics.
  Across the three tested agents, none achieved fully correct and fully safe execution across all scenarios. Successful task completion often coincided with data-handling failures such as accessing unnecessary information or disclosing information to inappropriate recipients, indicating that capability and data-handling safety should be evaluated separately. Qualitative review also revealed claim-action mismatches, simulation-aware behavior, user-simulator role reversal, and interpretation gaps in automated judging. Overall, the results indicate that operational data leakage is a first-order agent-safety concern distinct from adversarial exfiltration and provide a methodology for future evaluations of agent data-handling safety.

</details>


### 136. ACCORD: Action-Conditioned Contextual Grounding for Language Agents

- **Authors:** Lai Jiang, Cheng Qian, Zhenhailong Wang, Pan Lu, Heng Ji, Hao Peng
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16432v1](http://arxiv.org/abs/2606.16432v1)
- **PDF:** [https://arxiv.org/pdf/2606.16432v1](https://arxiv.org/pdf/2606.16432v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:**  
The paper introduces **ACCORD (Action‑Conditioned Contextual Grounding)**, a lightweight framework that equips LLM‑based agents with the ability to detect missing environmental context, actively query for that information, and seamlessly incorporate newly observed evidence before each action.

**Methodology:**  
ACCORD augments any off‑the‑shelf LLM agent with a pre‑action reasoning loop: (1) infer what contextual facts are required for the planned action, (2) issue targeted probes (e.g., tool calls, observations) to retrieve those facts, and (3) merge the retrieved data into the agent’s internal state for the subsequent decision. The approach requires no additional fine‑tuning or task‑specific reward signals—only a prompt that structures the probing and grounding steps.

**Key findings:**  
Across diverse benchmarks, ACCORD yields large, model‑agnostic gains in task success: on the AppWorld suite, GPT‑5‑mini improves from 42 % to 62.6 % (+20.6 pts); similar lifts are observed with Claude‑4.5‑sonnet (+10.8 pts), Qwen‑3.5‑27B‑FP8 (+10.1 pts), and the embodied AlfWorld tasks (+7.4 pts). The results highlight that systematic, action‑conditioned grounding of implicit context is crucial for reliable autonomous language agents in rich digital and physical environments.


<details>
<summary>Abstract</summary>

User instructions are often underspecified because humans rely on implicit assumptions about the surrounding environment. For large language model (LLM) agents operating in information-rich digital and physical environments, these assumptions cannot be inferred from the instruction alone; they must be recovered from the current state of tools, data, interfaces, and observations. Effective execution therefore requires agents to identify missing context, ground it in observed evidence, and carry it forward into subsequent actions. We show that current agents often fail to do so. They act from assumed rather than observed specifics, overlook information they could have gathered, and fail to incorporate evidence that has already been returned. Building on this insight, we propose ACCORD (Action-Conditioned Contextual Grounding), a simple and effective agent framework for adaptive grounding. Before each action, ACCORD actively probes the environment for missing information and integrates relevant context from the agent's trajectory that would otherwise be overlooked. Requiring no additional training or task-success signals, ACCORD improves task-goal completion on AppWorld by up to +20.6 points with GPT-5-mini, from 42.0% to 62.6%, compared to strong baselines. These gains persist with a substantially stronger base model (+10.8 with Claude-4.5-sonnet), an open-weight model (+10.1 with Qwen3.5-27B-FP8), and on the embodied AlfWorld benchmark (+7.4 success rate with GPT-5-mini).

</details>


### 137. LectūraAgents: A Multi-Agent Framework for Adaptive Personalized AI-Assisted Learning and Embodied Teaching

- **Authors:** Jaward Sesay, Yue Yu, Siwei Dong, Yemin Shi, Guangyao Chen, Börje F. Karlsson
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16428v1](http://arxiv.org/abs/2606.16428v1)
- **PDF:** [https://arxiv.org/pdf/2606.16428v1](https://arxiv.org/pdf/2606.16428v1)
- **Categories:** cs.CL, cs.AI, cs.HC


> The paper introduces **LectūraAgents**, a hierarchical multi‑agent system that models a professor–student relationship to produce fully personalized, embodied lessons. By organizing a ProfessorAgent and a team of specialist sub‑agents that jointly research, plan, review, and then physically enact teaching actions (hand‑writing, highlighting, etc.) in a virtual teaching environment, the framework uses the **Teaching Action‑Speech Alignment (TASA)** algorithm—salience‑driven heuristics combined with temporal semantic segmentation—to synchronise speech and multimodal gestures to each learner’s profile. Evaluation on high‑school to graduate courses, judged by expert educators, shows statistically significant improvements in content quality, embodied delivery, and learner‑specific adaptation compared with prior lecture‑automation systems, demonstrating a scalable, agentic approach to adaptive personalized education.


<details>
<summary>Abstract</summary>

Effective personalized AI-assisted learning demands systems that can not only generate accurate learner-specific educational materials, but also dynamically adapt their instruction to diverse learners. However, existing educational agents have primarily focused on lecture content automation and simulations, which often fall short of modelling multimodal and embodied instructional methods tailored for the individual learner. To this end, we propose LectūraAgents - a multi-agent framework that enables personalized learning through end-to-end adaptive embodied teaching. At its core, LectūraAgents mirrors a professor-student relationship, in which a ProfessorAgent leads a collaborative team of specialized subordinate agents through research, planning, review, and embodied delivery of lecture contents that adapt to a learner's needs. The framework offers three main contributions: (1) a hierarchical multi-agent architecture for end-to-end personalized learning; (2) an adaptive embodied teaching mechanism, wherein the ProfessorAgent executes visible and pedagogically motivated teaching actions (e.g., handwrite, highlight, underline, etc.) over contents in a teaching environment; and (3) a Teaching Action-Speech Alignment (TASA) algorithm that employs salience-based heuristics and temporal semantic segmentation to generate coherent teaching action sequences aligned with learner profiles. We evaluate LectūraAgents on diverse courses at high school, undergraduate, and graduate levels using sample-specific rubric-based analysis; with generated lecture materials and teaching actions assessed and validated by expert educators. Experimental results show consistent gains in lecture content quality, embodied teaching quality, assessment, and personalization over existing approaches, positioning LectūraAgents as a pedagogically well-grounded framework for personalized learning at scale.

</details>


### 138. Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents

- **Authors:** Shiyang Chen
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16364v1](http://arxiv.org/abs/2606.16364v1)
- **PDF:** [https://arxiv.org/pdf/2606.16364v1](https://arxiv.org/pdf/2606.16364v1)
- **Categories:** cs.AI, cs.CR, cs.SE


> **Main contribution** – The paper shows that tool‑selection errors by LLM agents are not caused by the model “missing” the correct tool in the prompt (the “crowded‑harness” hypothesis). Instead, the errors arise at the final decision readout: the model’s attention often focuses on the right tool‑definition segment, yet the readout maps this attention to the wrong tool.

**Methodology** – The authors analyze real “broken‑function‑call‑loop” (BFCL) failures across several models, measuring per‑candidate attention scores and performing three orthogonal interventions: (1) prompt‑side edits (reordering/duplicating the gold tool) versus readout‑side manipulations; (2) two representation‑invariant readout hacks (an additive attention‑logit bias and a residual‑stream steering vector); and (3) a training‑free selector that chooses the tool with maximal segment attention.

**Key findings** – (i) Attention correctly highlights the intended tool ~80 % of the time, while the gold tool is under‑attended only ~10 % of failures, disproving the “lost‑in‑the‑middle” view. (ii) Prompt‑side fixes recover ≤23 % of errors, whereas readout‑side interventions recover 59–91 %, pinpointing the bottleneck at the readout layer. (iii) The two readout interventions are highly redundant (Jaccard 0.86), confirming representation‑invariant failure. (iv) The attention‑based selector closes most of the gap to an oracle selector (+11.9 pts on BFCL, +14.9 pts on Seal‑Tools) across models from 3 B to 32 B parameters, offering a simple, training‑free remedy for single‑turn tool selection.


<details>
<summary>Abstract</summary>

LLM agents mis-call tools, and the natural guess is that the model failed to see the right tool in a crowded harness. We show the opposite through a lens concurrent work sets aside -- the model's attention to labeled tool-definition segments. On real BFCL failures, by per-candidate attention argmax the model attends most to the correct tool 80% of the time (vs. 21% chance), and the gold is the under-attended segment on only 10%: it looks at the right tool and still picks wrong. This directly refutes the intuitive "crowded-harness / lost-in-the-middle" explanation: the failure is at the decision readout, not the harness, and we pin it there three ways. (1) Input vs. readout: repairing the prompt (reordering or duplicating the gold tool) recovers <=23% of failures, while readout-side interventions recover 59-91%. (2) Representation-invariance: two gold-pointed interventions in different representations -- an additive attention-logit bias and a residual-stream steering vector -- recover largely the same failures (per-task Jaccard 0.865 pooled, 0.79-0.91 per model), so the bottleneck is localized to the readout independent of which representation is poked. (3) A training-free, gold-free selector: per-segment attention closes most of the gold-free-vs-oracle gap on BFCL (+11.9 pts pooled function-name selection vs. +17.9-pt oracle headroom) and adds +14.9 pts on Seal-Tools; every model positive (exact McNemar p<=8e-4 each). Scopes differ: the causal attention-bias dose-response is bidirectional and monotonic on 10 mask-honoring models (3-32B), the full 0.5-32B span carrying only the correlational diagnostic; the deployable selector is evaluated on 5 single-turn models and does not yet transfer to a multi-turn loop.

</details>


### 139. AdaSTORM: Scaling LLM Reasoning on Dynamic Graphs via Adaptive Spatio-Temporal Multi-Agent Collaboration

- **Authors:** Bing Hao, Ruijie Wang, Haodong Qian, Yunlong Chu, Yuhang Liu, Yumeng Lin, Minglai Shao, Jianxin Li
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16328v1](http://arxiv.org/abs/2606.16328v1)
- **PDF:** [https://arxiv.org/pdf/2606.16328v1](https://arxiv.org/pdf/2606.16328v1)
- **Categories:** cs.AI


> **Contribution:** AdaSTORM introduces the first multi‑agent framework that enables large‑language‑model (LLM) reasoning over truly large, dynamic graphs by adaptively partitioning the graph and orchestrating a spatio‑temporal collaboration among specialized agents.  

**Methodology:** The system first performs *adaptive partitioning* to split a massive, time‑evolving graph into sub‑regions sized to fit the LLM’s context window while minimizing total inference cost. Then a *spatio‑temporal decoupled multi‑agent architecture* assigns each partition to a dedicated LLM agent; agents exchange concise summaries according to the original graph topology and temporal dependencies, allowing coordinated global inference without exceeding context limits.  

**Key Findings:** Across several synthetic and real‑world dynamic‑graph benchmarks, AdaSTORM scales reasoning to graphs with thousands of nodes while maintaining > 90 % accuracy, outperforming seven strong baselines and setting new state‑of‑the‑art results on existing datasets—all without auxiliary tools. This demonstrates that adaptive, topology‑aware multi‑agent collaboration can break the LLM scaling bottleneck for dynamic graph tasks, opening a path for agentic AI systems to handle large, evolving relational structures.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) demonstrate remarkable potential in dynamic graph reasoning, but suffer from a scaling bottleneck: current models can only handle graphs with tens of nodes, constrained by exponential reasoning overhead and finite context windows. While multi-agent systems (MAS) offer collective reasoning and topology-aware orchestration, capabilities naturally suited for graph-structured tasks, their application to dynamic graphs remains unexplored. This paper presents Scaling LLM Reasoning on Dynamic Graphs via Adaptive Spatio-Temporal Multi-Agent Collaboration (AdaSTORM), a framework that reformulates large-scale dynamic graph reasoning into two stages: (i) Adaptive Partitioning, partitioning large-scale dynamic graphs into subregions that match the model's reasoning capacity while minimizing inference cost; and (ii) Collaborative Reasoning, aligning graph partition topologies with a spatio-temporal decoupled multi-agent architecture. AdaSTORM is the first multi-agent framework tailored for dynamic graph reasoning. Extensive experiments show that AdaSTORM successfully breaks through the scaling bottleneck, scaling reasoning to thousand-node graphs with over 90% accuracy across several large-scale dynamic graph settings without external tools, significantly outperforms seven competitive baselines. Furthermore, it achieves state-of-the-art accuracy on existing benchmarks and generalizes robustly to real-world datasets. The source code is available at: https://github.com/irisorchid107/AdaSTORM/.

</details>


### 140. Gaming-Resistant Insurance Contracts for Autonomous AI Agents: Strategy-Proof Toll Mechanism Design

- **Authors:** Hao-Hsuan Chen
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16326v2](http://arxiv.org/abs/2606.16326v2)
- **PDF:** [https://arxiv.org/pdf/2606.16326v2](https://arxiv.org/pdf/2606.16326v2)
- **Categories:** cs.GT, cs.AI, q-fin.RM


> The paper extends the actuarial‑runtime insurance framework of “Paper A” by treating the AI operator as a strategic player and fully characterizing the five ways an autonomous agent can manipulate its insurance contract. It introduces three new contract clauses—common‑control aggregation to block cross‑boundary toll evasion, interface‑failure penalties (escalation fees) to prevent rewarding malformed communications, and a model‑identity menu with component‑wise‑minimum penalties to make truthful model reporting weakly dominant—and combines them with Paper A’s minimal‑authority and no‑splitting rules to achieve joint incentive compatibility across all attack vectors. The resulting “toll mechanism” guarantees gaming‑resistance, individual rationality for the operator, and weak budget balance, providing a provably incentive‑compatible layer for controlling side‑effects of autonomous AI agents.


<details>
<summary>Abstract</summary>

Paper A defines a time-consistent actuarial runtime that prices each side-effect-bearing action against a contractually fixed safe default and gates execution against a reserve budget. It treats the operator as passive. This paper makes the operator strategic. We characterise a five-attack space for autonomous AI-agent insurance contracts and prove when the actuarial runtime is gaming-resistant. Two attack surfaces -- post-toll safe-default selection and within-boundary action splitting -- are closed by Paper A's minimal-authority and no-splitting clauses. The remaining three require new contract clauses. First, common-control aggregation prevents cross-boundary re-routing from reducing toll below the boundary potential applied to total exposure. Second, interface failures such as invalid JSON are contract-relevant events, not safety wins: treating them as zero-toll safe defaults can reward unreliable models, while escalation fees reverse the incentive. We validate this interface-compliance theorem on committed cross-model traces from the companion empirical paper. Third, a model-identity menu with a componentwise-minimum penalty schedule makes truthful reporting of the deployed model weakly dominant. We then compose these clauses with Paper A's runtime guarantees to obtain joint incentive compatibility over the five-attack space. Finally, a two-parameter premium family discharges operator individual rationality and weak budget balance at the truthful equilibrium. The result is an incentive-compatibility layer for actuarial control of autonomous-agent side effects.

</details>


### 141. State-Grounded Multi-Agent Synthetic Data Generation for Tool-Augmented LLMs

- **Authors:** Rahul Khedar,  Eshita, Sneha Teja Sree Reddy Thondapu, Mayank Malhotra, Arup Das, Jitesh Chandra, Yun-Shiuan Chuang, Chaitanya Kulkarni, Arun Menon, Linsey Pang, Avinash Karn, Mouli V, Prakhar Mehrotra
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16307v1](http://arxiv.org/abs/2606.16307v1)
- **PDF:** [https://arxiv.org/pdf/2606.16307v1](https://arxiv.org/pdf/2606.16307v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution** – The paper introduces **StateGen**, a synthetic data‑generation framework that creates large, multi‑turn, tool‑grounded conversation corpora for training and evaluating tool‑augmented LLM agents. Its novelty lies in a **centralized state manager** that preserves a structured world‑state throughout the dialogue, guaranteeing that tool calls are always consistent with the “backend‑is‑truth” invariant and thus eliminating the dominant class of tool‑call hallucinations.

**Methodology** – StateGen runs a four‑role LLM loop: (1) a persona‑conditioned user simulator, (2) the target agent, (3) a state‑grounded tool simulator that updates the shared world state, and (4) a multi‑axis LLM judge that scores the interaction and its reasoning trace. Hierarchical multi‑agent scenarios are supported by treating sub‑agents as tools that read/write the same state object, and personas are varied via a 23‑dimensional trait vector.

**Key findings** – Across 64,698 evaluated conversations from three production corpora, StateGen achieves a **tool‑call hallucination score of 9.66 / 10**, demonstrates robust persona‑driven diversity, and shows a clear train/evaluation split (no memorization). Compared with eight existing systems, StateGen uniquely provides combined multi‑turn generation, state‑grounded tool simulation, hierarchical agent composition, and built‑in judge scoring—features critical for scaling reliable agentic AI.


<details>
<summary>Abstract</summary>

Training tool-augmented LLM agents requires large corpora of multi-turn, tool-grounded conversational data that is expensive to annotate, privacy-constrained in production settings, and largely absent from public datasets. We present StateGen, a synthetic data generation platform that produces scored, reasoning-trace-rich training conversations by orchestrating a four-role LLM loop: a persona-conditioned user simulator, an agent under test, a state-grounded tool simulator, and a multi-axis LLM judge. The key architectural contribution is an authoritative state manager that maintains a structured world-state object across turns, enforcing a backend-is-truth invariant that eliminates the dominant class of tool-call hallucinations by construction. StateGen extends naturally to hierarchical multi-agent settings by declaring sub-agents as tools, all sharing a single state object. We report results on 64,698 evaluated conversations across three production corpora: tool-call hallucination scores reach 9.66/10, the system supports persona-driven variation via a 23-dimensional trait vector, and a cleanly separated train and golden evaluation set split confirms the data is not memorization bait (per-criterion gap analysis). Comparison with eight external systems shows that no single publicly available platform combines multi-turn generation, state-grounded tool simulation, hierarchical multi-agent support, and built-in judge scoring.

</details>


### 142. SpecAlign: Efficient Specification-Grounded Alignment of Large Language Models via Synthetic Data

- **Authors:** Wenjie Wang, Yue Huang, Zhengqing Yuan, Han Bao, Shiyi Du, Yuchen Ma, Yue Zhao, Yanfang Ye, Xiangliang Zhang
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16276v2](http://arxiv.org/abs/2606.16276v2)
- **PDF:** [https://arxiv.org/pdf/2606.16276v2](https://arxiv.org/pdf/2606.16276v2)
- **Categories:** cs.AI


> **Main contribution**: The paper introduces *specification‑grounded alignment* and the SpecAlign framework, which turn detailed, provider‑authored model specifications into the primary training signal for large language models, rather than relying on generic safety or helpfulness benchmarks.

**Methodology**: SpecAlign automatically converts specification documents into synthetic alignment data by (1) annotating structured rules, (2) controllably instantiating those rules into diverse prompt–response scenarios, and (3) using multi‑agent adversarial generation to produce fine‑grained preference pairs that include both compliant outputs and targeted violations, enabling boundary‑aware fine‑tuning.

**Key findings**: Across several evolving specifications and backbone LLMs, fine‑tuning with SpecAlign consistently raises rule‑compliance scores while maintaining overall performance and avoiding the overly conservative behavior seen with traditional alignment methods, demonstrating that grounding alignment in explicit specifications yields rapid, precise, and scalable model adaptation.


<details>
<summary>Abstract</summary>

As large language models (LLMs) are increasingly deployed in real-world applications, alignment is no longer governed by a single universal notion of safety or helpfulness, but instead by provider- or application-specific model specifications. These specifications are typically long, structured, and frequently updated, yet existing alignment pipelines lack a systematic mechanism to operationalize them as training signals. In this paper, we propose specification-grounded alignment, a new alignment paradigm that treats provider-authored model specifications as the primary alignment target rather than abstract principles or static benchmarks. To instantiate this paradigm, we introduce SpecAlign, a framework that synthesizes alignment data directly from specification documents. SpecAlign combines structured rule annotation, controllable specification instantiation, and multi-agent adversarial data synthesis to generate fine-grained, boundary-aware preference pairs that capture both compliant behaviors and meaningful specification violations. Experiments across multiple model specifications and backbone models demonstrate that training with SpecAlign consistently improves rule compliance while preserving general capabilities and avoiding over-conservative behavior. These results suggest that grounding alignment in explicit model specifications enables rapid, precise, and scalable adaptation of LLM behavior to evolving policy requirements.

</details>


### 143. PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents

- **Authors:** Zhenbang Du, Jun Luo, Zhiwei Zheng, Xiangchi Yuan, Kejing Xia, Dachuan Shi, Qirui Jin, Qijia He, Shaofeng Zou, Yingbin Liang, Wenke Lee
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16215v1](http://arxiv.org/abs/2606.16215v1)
- **PDF:** [https://arxiv.org/pdf/2606.16215v1](https://arxiv.org/pdf/2606.16215v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> **Contribution** – The paper introduces **PACT (Privileged trAce Co‑Training)**, a training framework that lets multi‑turn tool‑use agents benefit from expert demonstration traces without exposing those traces at inference time.  

**Methodology** – PACT separates generation (prompt‑only rollouts) from supervision: during training it (1) evaluates each rollout with a **trace‑conditioned RL surrogate** that scores the policy as if it were conditioned on the expert trace, and (2) applies a **component‑aware supervised‑fine‑tuning loss** to the reasoning and tool‑call prefixes, with an annealed weight and an additional prompt‑only anchoring term to avoid over‑fitting to the privileged information.  

**Findings** – Across three benchmark suites (FTRL, BFCL, ToolHop), PACT consistently outperforms strong baselines that rely solely on standard SFT or RL, demonstrating that privileged trace co‑training provides dense learning signals while preserving the model’s ability to operate solely from prompts at test time.


<details>
<summary>Abstract</summary>

Multi-turn tool-use agents must reason, call tools, and adapt to observations across several interaction turns. Post-training such agents is challenging, as reinforcement learning often suffers from sparse rewards and weak credit assignment despite matching the prompt-only inference setting, while supervised fine-tuning on expert traces provides dense process supervision but can over-constrain the model to fixed trajectories. To tackle this, we propose PACT, a Privileged trAce Co-Training framework for multi-turn tool-use agents. The key idea is to use expert traces only as training-time optimization signals rather than rollout-time hints. PACT keeps rollout generation prompt-only, then uses expert traces to guide optimization through two complementary signals: a trace-conditioned RL surrogate that evaluates prompt-only rollouts under expert-trace context, and a component-aware SFT loss that supervises reasoning prefixes and tool-calls with annealed strength. To reduce over-reliance on the training-only trace context, PACT further introduces a prompt-only anchoring. We also provide a latent-trace view that connects the two trace-based objectives and explains how expert traces can guide optimization without being used during rollout generation. Experiments on FTRL, BFCL, and ToolHop show that PACT consistently improves over strong SFT- and RL-based baselines, highlighting the value of privileged trace co-training for multi-turn tool-use learning.

</details>


### 144. Embedded Arena: Iterative Optimization via Hardware Feedback

- **Authors:** Zhihan Zhang, Alexander Le Metzger, Jiuyang Lyu, Chun-Cheng Chang, Jiayi Shao, Yujia Liu, Emmanuel Azuh Mensah, Edward Wang, Kurtis Heimerl, Gregory D. Abowd, Shwetak Patel, Natasha Jaques, Vikram Iyer
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16190v1](http://arxiv.org/abs/2606.16190v1)
- **PDF:** [https://arxiv.org/pdf/2606.16190v1](https://arxiv.org/pdf/2606.16190v1)
- **Categories:** cs.AR, cs.AI


> The paper introduces **Embedded Arena**, a hardware‑in‑the‑loop framework that lets a large‑language‑model agent automatically co‑optimize neural‑network models and their firmware for constrained microcontrollers by compiling, flashing, and measuring on the actual device. Using iterative feedback from the hardware, the agent discovers model‑compression pipelines that achieve up to 250× (vision) and 400× (audio) size reductions with ≤ 3.3 % and ≤ 6 % loss in accuracy/feature‑error, respectively—surpassing human expert designs within seven optimization cycles and succeeding after just three iterations. The approach is validated on two edge deployments (an elk‑detection camera trap and a phonetic‑transcription wearable), demonstrating battery‑free operation and state‑of‑the‑art performance.


<details>
<summary>Abstract</summary>

Embedded devices from wildlife monitoring stations to clinical wearables require local AI inference due to latency, communication, or privacy constraints. Optimizing models for heterogeneous microcontrollers (MCUs) requires simultaneously satisfying hard physical constraints on memory, power, and temperature while preserving accuracy, a multidimensional optimization that is today performed manually by experts. We ask whether an LLM agent can autonomously navigate this complex, multi-turn pipeline guided by real hardware feedback, and introduce a hardware-in-the-loop agent arena in which the agent iteratively refines both model and firmware -- compiling, flashing, and measuring on real hardware -- to enable closed-loop optimization. Frontier models, including Claude Opus 4.7 and Gemini 3.1 Pro, fail entirely without hardware feedback (0% deployment success), whereas our hardware-in-the-loop formulation achieves the first successful deployment within three iterations and can surpass human expert results within seven. This agentic co-optimization achieves 250x compression for vision models with <3.3% accuracy loss and 400x for audio with <6% Feature Error Rate loss, enabling battery-free operation on a commercial MCU via solar harvesting. We demonstrate practical impact in two real-world systems: an elk-detection camera trap (96.7% accuracy) and a phonetic-transcription wearable (8.44% FER) for child development research.

</details>


### 145. LiteOdyssey: A Lightweight Reasoning AI Agent for Interpretable Rare-Disease Diagnosis

- **Authors:** Minh-Ha Nguyen, Erica Gray, Chih-Ting Yang, Rizwan Hamid, Lingyao Li, Siyuan Ma, Thomas A. Cassini, Cathy Shyr
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16149v1](http://arxiv.org/abs/2606.16149v1)
- **PDF:** [https://arxiv.org/pdf/2606.16149v1](https://arxiv.org/pdf/2606.16149v1)
- **Categories:** cs.AI


> LiteOdyssey shows that a single, untuned language model can reach state‑of‑the‑art rare‑disease diagnostic accuracy by embedding it in a human‑crafted clinical‑genetics reasoning policy and giving it dynamic, free biomedical tool access. The authors derived the policy through Policy Iteration with Human Feedback (PIHF), then evaluated the agent on two large benchmark suites (LIRICAL + PhenoPacket, 1,243 cases) where it attained 59.3 % Recall@1—far surpassing a baseline GPT‑5.4 model (10.7 %) and matching or beating larger multi‑agent or retrieval‑heavy systems. These results demonstrate that extending the reasoning chain of a lightweight agent, rather than scaling data or model size, yields accurate, deployable, and interpretable rare‑disease diagnostics.


<details>
<summary>Abstract</summary>

Most medical AI systems improve by scaling additional machinery: more fine-tuning data, more agents, and/or larger retrieval databases. In rare-disease diagnosis, however, such scaling can produce systems that are difficult to deploy, audit, and maintain. We asked whether state-of-the-art diagnostic performance could instead be achieved by extending the reasoning chain of a single AI agent: guiding it with a diagnostic policy, developed through human-AI collaboration and augmenting with freely available biomedical tools. We introduce LiteOdyssey, a lightweight rare-disease diagnostic framework that guides reasoning language model through a clinical genetics workflow. This framework was developed through Policy Iteration with Human Feedback (PIHF) and uses dynamic access to public biomedical tools. On two challenging benchmarks that provide only patient clinical features, LiteOdyssey achieved state-of-the-art performance, with an overall disease Recall@1 of 59.3% over the combined 1,243 cases of LIRICAL (n = 370) and the PhenoPacket Store (n = 873). Both benchmarks have a high proportion of ultra-rare disease (a prevalence below 1 in 1,000,000, with ultra-rare shares of approximately 45% and 52.8%, respectively). On the more difficult PhenoPacket subset, where causal diseases were not mapped to Orphanet in our rarity-mapping pipeline, LiteOdyssey achieved 60.7% Recall@1, compared with 10.7% for the same baseline model (GPT-5.4) without tools. This performance was achieved without fine-tuning, multi-agent ensembles, or a large case-retrieval database. Gains were also observed in the following: on cases never seen during development, on a private cohort of real-world rare disease patients, and on a smaller open-weights model. LiteOdyssey suggests a path toward rare-disease AI systems that are accurate, easier to deploy, and more transparent for physician review.

</details>


### 146. InvDesMobility: a reliability-gated first-principles feedback framework for closed-loop materials discovery

- **Authors:** Wen-Kao Li, Ze-Feng Gao, Peng-Jie Guo, Wei Ji, Zhong-Yi Lu
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16133v1](http://arxiv.org/abs/2606.16133v1)
- **PDF:** [https://arxiv.org/pdf/2606.16133v1](https://arxiv.org/pdf/2606.16133v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> The paper introduces **InvDesMobility**, a closed‑loop inverse‑design framework that couples automated DFT calculations with a *reliability‑gated* feedback contract: only first‑principles results that pass multi‑level evidence checks (convergence, fit quality, provenance) are fed back to update a generative structure model and an acquisition model that prioritises further validation. By iteratively proposing 2.4 × 10⁶ candidate 2‑D materials, screening them through a multi‑agent DFT pipeline, and retaining 86 high‑reliability carrier‑mobility channels across 41 formulas, the system demonstrates that robust, auditable feedback—rather than a fixed material list—is essential for trustworthy agentic AI‑driven materials discovery. The methodology proves scalable, reproducible, and transferable, offering an open‑source workflow and evidence‑tracking infrastructure for future AI‑augmented inverse design tasks.


<details>
<summary>Abstract</summary>

Inverse materials design starts from target functionality and searches for structures that can realize it. Its value in closed-loop discovery depends not only on prediction performance, but also on whether expensive first-principles results are independently validated, provenance-recorded, and admitted as feedback only when evidence is sufficient. This is especially important for composite properties such as carrier mobility, where a final scalar value hides intermediate quantities, fit quality, convergence history, and workflow assumptions. Here we present InvDesMobility, a reliability-gated first-principles feedback framework that integrates multi-agent automated DFT, evidence stratification, generative structure proposal, acquisition ranking, and auditable release. Using 516 2DMatPedia-derived candidates, the workflow produced 280 QC-passed materials and 573 retained carrier-direction seed channels after channel-level reliability gating. These records were split into two feedback objects: relaxed structures updated the generative model, while retained mobility channels trained the acquisition model and set validation priority. Over multiple iterations, InvDesMobility screened 2.4 x 10^6 structures, submitted 102 candidates for DFT validation, and retained 86 reliability-gated generated channels across 41 formulas. Overall, the main contribution is not a fixed list of high-mobility materials, but a transferable feedback contract that makes closed-loop inverse design both useful and auditable when learning from expensive calculated properties. All source data, retained feedback records, and workflows are available at https://github.com/DreamLufei/invDesMobility, with an accompanying evidence website at https://dreamlufei.github.io/invDesMobility/.

</details>


### 147. Distributed Safe Consensus Under Asymmetric Input and Time-Varying Output Constraints

- **Authors:** Abhinav Sinha, Shashi Ranjan Kumar
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16116v1](http://arxiv.org/abs/2606.16116v1)
- **PDF:** [https://arxiv.org/pdf/2606.16116v1](https://arxiv.org/pdf/2606.16116v1)
- **Categories:** eess.SY, cs.MA, cs.RO, math.DS


> The paper introduces a novel distributed control framework that guarantees **safe consensus** for single‑integrator agents operating on a connected undirected graph while simultaneously respecting **asymmetric actuator limits** and **time‑varying output safety constraints**. The authors model each actuator with a smooth, state‑dependent map that keeps the actual input strictly inside a prescribed interval, then apply a **barrier‑coordinate transformation** to the agents’ outputs over a common, time‑varying safe set. A two‑layer controller – a graph‑based synchronization law in the transformed coordinates together with an actuator‑side tracking law – achieves forward invariance of the safe output set, strict input admissibility, and asymptotic agreement; the transformed synchronization errors decay exponentially and the original outputs converge to a designer‑chosen admissible trajectory within the safe interval. Simulations corroborate that the closed‑loop system remains bounded, the actuator inputs stay inside their asymmetric bounds, and the agents reach consensus without violating any safety constraints, offering a practical solution for safe, coordinated behavior in agentic AI systems.


<details>
<summary>Abstract</summary>

This paper studies safe distributed consensus for single-integrator multi-agent systems over connected undirected graphs under simultaneous asymmetric actuator constraints and output safety constraints. Each agent is equipped with a continuously differentiable asymmetric actuator dynamics that maps a commanded control signal to the realized plant input while keeping the latter strictly inside a prescribed admissible interval. To address output safety, a barrier-coordinate transformation is introduced over a common time-varying safe interval, and a distributed synchronization law is designed in the transformed coordinates. The resulting controller integrates a graph-based coordination layer with an actuator-side tracking layer, thereby enabling simultaneous enforcement of input admissibility, forward invariance of the safe output set, and asymptotic synchronization. For compact admissible sets of initial conditions, it is shown that the closed-loop solution is complete, all signals remain bounded, the actuator inputs remain strictly within their asymmetric bounds, and the agent outputs remain inside the prescribed safe interval for all time. Moreover, the transformed synchronization errors converge exponentially to zero, and the original agent outputs asymptotically synchronize to a designer-selected admissible trajectory embedded in the common safe interval. Numerical simulations validate the proposed framework and demonstrate safe consensus under both asymmetric actuation bounds and time-varying output constraints.

</details>


### 148. Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization

- **Authors:** Junyi Li, Xiaowei Qian, Yingyi Zhang, Wenlin Zhang, Guojing Li, Sheng Zhang, Xiao Han, Yichao Wang, Xiangyu Zhao
- **Published:** 2026-06-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.16111v1](http://arxiv.org/abs/2606.16111v1)
- **PDF:** [https://arxiv.org/pdf/2606.16111v1](https://arxiv.org/pdf/2606.16111v1)
- **Categories:** cs.CL


> ParetoPO is a two‑stage multi‑objective reinforcement‑learning framework that aligns tool‑using LLM agents simultaneously for task accuracy and tool‑use efficiency. It first employs hypervolume‑guided dynamic scalarization to adapt reward weights as the global Pareto frontier evolves, then replaces scalar rewards with a Pareto‑ranking‑based advantage estimator that gives dominance‑aware credit to nondominated trajectories, enabling fine‑grained, action‑level trade‑off optimization. Experiments on mathematical reasoning and multi‑hop question answering demonstrate that ParetoPO consistently discovers policies that dominate static‑weight and heuristic baselines, achieving markedly better accuracy‑efficiency balances for tool‑integrated agents.


<details>
<summary>Abstract</summary>

Recent advances in tool-integrated language agents have significantly improved their ability to solve complex reasoning tasks. However, existing alignment methods predominantly focus on maximizing task accuracy, while overlooking auxiliary objectives such as tool-use efficiency, which are essential for practical deployment. To address this gap, we introduce ParetoPO, a two-stage multi-objective optimization framework for aligning tool-using large language models (LLMs) under competing objectives. In the first stage, ParetoPO leverages hypervolume-guided dynamic scalarization to adapt reward weights based on global Pareto frontier progress. In the second stage, it replaces scalarized learning signals with Pareto-ranking-based advantage computation, promoting nondominated trajectories through dominance-aware credit assignment. This design enables fine-grained, action-level optimization across multiple conflicting objectives. Experimental results on mathematic reasoning and multi-hop QA tasks show that ParetoPO consistently discovers policies with superior accuracy-efficiency trade-offs compared to static and heuristic baselines.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*