# Weekly AI Agent Paper Report

**Generated:** 2026-08-03 12:41
**Period:** 2026-07-27 to 2026-08-02

## Summary

- **Total papers fetched:** 731
- **Papers matching keywords:** 164
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-07-27) | Change |
|--------|-----------|-----------|--------|
| Total matched | 164 | 113 | +51 |
| arxiv | 163 | 113 | +50 |
| biorxiv | 0 | 0 | +0 |
| medrxiv | 1 | 0 | +1 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (1 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. A Privacy-Preserving Zero-Code Conversational Statistical Analysis System for Clinical Research Using Agentic AI and Local R Execution

- **Authors:** Yang, S., Chen, V. L., Ng, W. H., Zhang, S., Qiu, S., Zhu, J., Hsieh, T. Y.-J., Ji, F., Yeo, Y. H.
- **Published:** 2026-08-02
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.30.26359367](https://doi.org/10.64898/2026.07.30.26359367)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background Clinical data analysis typically requires statistical programming skills, whereas cloud-based artificial intelligence (AI) agents risk exposing sensitive patient records. We developed and functionally validated a privacy-preserving, zero-code conversational statistical analysis framework that translates natural-language clinical research requests into executable R workflows while strictly retaining raw patient data within local computing environments. Methods Orchestrated by the n8n engine, the system integrates the DeepSeek-Reasoner model with a Pinecone vector database for retrieval-augmented generation (RAG), grounding statistical selection in curated biostatistical guidance and R templates. Core functionalities include data schema perception, interactive data cleaning, requirements refinement, and local R code execution via a controlled command-line interface. System performance was evaluated by replicating a published prognostic model study on metabolic dysfunction-associated steatotic liver disease (MASLD). Findings All core analytical workflows, including data cleaning, multivariable Cox proportional hazards modeling, model diagnostics, and publication-ready tables and figures (e.g., baseline characteristics, Schoenfeld residuals, receiver operating characteristic curves, and forest plots), were executed solely through natural-language dialogues without manual coding. The external large language model actively clarified analytical prompts while receiving zero row-level patient data. Interpretation Decoupling remote cloud reasoning from local code execution lowers the technical threshold for clinicians conducting data-driven research while safeguarding data privacy. This architecture provides a practical, scalable, and reproducible framework for converting natural-language clinical questions into executable statistical workflows. Funding National Natural Science Foundation of China (82473291), Shaanxi Province "Three Qin Scholars" Innovation Team Project (2023001), and Fundamental Research Funds for the Central Universities (xtr062023003).

</details>


---



## Medrxiv (1 papers)


### 1. A Privacy-Preserving Zero-Code Conversational Statistical Analysis System for Clinical Research Using Agentic AI and Local R Execution

- **Authors:** Yang, S., Chen, V. L., Ng, W. H., Zhang, S., Qiu, S., Zhu, J., Hsieh, T. Y.-J., Ji, F., Yeo, Y. H.
- **Published:** 2026-08-02
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.30.26359367](https://doi.org/10.64898/2026.07.30.26359367)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background Clinical data analysis typically requires statistical programming skills, whereas cloud-based artificial intelligence (AI) agents risk exposing sensitive patient records. We developed and functionally validated a privacy-preserving, zero-code conversational statistical analysis framework that translates natural-language clinical research requests into executable R workflows while strictly retaining raw patient data within local computing environments. Methods Orchestrated by the n8n engine, the system integrates the DeepSeek-Reasoner model with a Pinecone vector database for retrieval-augmented generation (RAG), grounding statistical selection in curated biostatistical guidance and R templates. Core functionalities include data schema perception, interactive data cleaning, requirements refinement, and local R code execution via a controlled command-line interface. System performance was evaluated by replicating a published prognostic model study on metabolic dysfunction-associated steatotic liver disease (MASLD). Findings All core analytical workflows, including data cleaning, multivariable Cox proportional hazards modeling, model diagnostics, and publication-ready tables and figures (e.g., baseline characteristics, Schoenfeld residuals, receiver operating characteristic curves, and forest plots), were executed solely through natural-language dialogues without manual coding. The external large language model actively clarified analytical prompts while receiving zero row-level patient data. Interpretation Decoupling remote cloud reasoning from local code execution lowers the technical threshold for clinicians conducting data-driven research while safeguarding data privacy. This architecture provides a practical, scalable, and reproducible framework for converting natural-language clinical questions into executable statistical workflows. Funding National Natural Science Foundation of China (82473291), Shaanxi Province "Three Qin Scholars" Innovation Team Project (2023001), and Fundamental Research Funds for the Central Universities (xtr062023003).

</details>



## Arxiv (163 papers)


### 1. AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers

- **Authors:** Tianyu Huai, Tingshuo Fan, Xinchi Chen, Yining Zheng, Yuxin Wang, Shuang Chen, Jie Zhou, Xuanjing Huang
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29626v1](http://arxiv.org/abs/2607.29626v1)
- **PDF:** [https://arxiv.org/pdf/2607.29626v1](https://arxiv.org/pdf/2607.29626v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLMs evolve from code completion systems into autonomous scientific agents, evaluating their ability to conduct experiments has become increasingly important. Existing benchmarks typically focus on static code generation, paper replication, or final answer correctness, but do not directly assess whether agents can interpret experimental evidence and use it to guide subsequent hyperparameter decisions. To address this gap, we introduce AgentHPOBench, a sequential benchmark comprising 30 executable machine learning tasks across seven research categories. Each task begins with a validated baseline run, after which an agent performs several sequential interventions. At each step, the agent observes the accumulated configurations, metrics, and logs before proposing the next valid configuration. We evaluate 12 widely used agents and conventional HPO baselines under a unified protocol. The results show that current agents exhibit measurable experimental optimization ability across domains, but still face clear limitations in sustained iterative refinement, complex log diagnosis, and consistent progress toward reported reference performance.

</details>


### 2. Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts

- **Authors:** Sergey Salishev
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29496v1](http://arxiv.org/abs/2607.29496v1)
- **PDF:** [https://arxiv.org/pdf/2607.29496v1](https://arxiv.org/pdf/2607.29496v1)
- **Categories:** cs.LG, cs.FL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study transcript management for fixed, finite-precision causal Transformers. A transcript is partitioned into channels of bounded blocks. Each transition consults a fixed visible suffix and may append one block, leaving the model, weights, and token protocol unchanged. The operation $P_c:=\PopContext(c)$ deletes the newest block on channel $c$ and exposes its predecessor.
  We model the layer by the Transcript-Managed Transducer $\TMTn{k}$: one finite controller, $k$ channels, and per-round actions from stay, push, and pop under a caller-driven status map. Fixed visible windows encode as finite symbols. The pop-free Restricted Transcript-Managed Transducer $\RTMTn{k}$ is the standard append-only layer and, for every fixed $k$, realizes exactly the deterministic finite-state transductions. The same holds for every fixed finite agent population under a monotone protocol that appends, routes, and copies visible blocks.
  Admitting $\{P_c\}_{c=1}^k$ restores pop. Newest-first, a pop-enabled channel is a stack; compiling to the Hopcroft--Ullman presentation transfers the classical hierarchy: $\DCFL$ for $k=1$ and $\RE$ for every $k\ge2$. Orchestrated one-channel agents match one controller with $k$ channels, so two pop-enabled transcripts---in one agent or two---suffice for universality. Simulation costs and invariance to fixed block size and visible radius are stated. The bounds fix precision, alphabets, blocks, visibility, controller state, and population; growing exact context, hidden-block access, writable stores, and unbounded \textbf{Spawn} add further state.

</details>


### 3. AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair

- **Authors:** Michael Fu, Qiyue Mei, Patanamon Thongtanunam, Kla Tantithamthavorn
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29422v1](http://arxiv.org/abs/2607.29422v1)
- **PDF:** [https://arxiv.org/pdf/2607.29422v1](https://arxiv.org/pdf/2607.29422v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated vulnerability repair aims to reduce the time and effort required to patch security flaws from a vulnerability triage report. Recent agentic AI approaches have shown promising results in automated program repair. However, vulnerability repair demands richer program context than general bug repair - context that security engineers routinely assemble in practice but that existing agentic approaches do not engineer. We identify three critical gaps: code-structure context capturing cross-file data flows and memory operation patterns, runtime-execution context revealing crash semantics and memory origins, and commit-history context recovering how fragile code patterns were introduced. We present AgenticRepair, an agentic vulnerability repair framework that addresses the gaps through multi-faceted program context engineering. AgenticRepair orchestrates three specialized LLM subagents to engineer the contexts, which are then embedded into the memory of a dedicated repair subagent for context-conditioned patch synthesis. Evaluated on SEC-Bench comprising 300 real-world instances with sanitizer-based patch verification, AgenticRepair achieves a 73% success rate, substantially outperforming the strongest baseline by 29%. Our ablation study confirms that the three context facets are mutually complementary, and that multi-agent scaffolding and base-model capacity each play an essential role. Collectively, these findings establish multi-faceted program context engineering as a promising design direction for agentic vulnerability repair.

</details>


### 4. Beyond Component Testing: Validating Agentic AI Systems

- **Authors:** Fabio Orazio Mirto, Luca D'Agati, Giuseppe Tricomi, Stefano Silvestri, Francesco Longo, Antonio Puliafito, Giovanni Merlino
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29405v1](http://arxiv.org/abs/2607.29405v1)
- **PDF:** [https://arxiv.org/pdf/2607.29405v1](https://arxiv.org/pdf/2607.29405v1)
- **Categories:** cs.AI, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems act through multi-step trajectories that combine planning, tool use, memory, interaction, and adaptation. This behavior stretches validation practice beyond component testing and one-shot input--output evaluation, because acceptable system behavior now depends on how decisions unfold over time and under changing environmental conditions. This survey synthesizes 257 papers spanning agent evaluation, software assurance, cyber-physical systems, runtime monitoring, and regulatory guidance in order to characterize the validation problem for agentic systems. The review is organized around a five-dimension taxonomy covering behavioral, safety, temporal, regulatory, and multi-agent concerns, and uses that taxonomy to map current approaches and expose recurrent coverage gaps. The analysis shows that behavioral evaluation is comparatively mature, while temporal validity, runtime evidence maintenance, regulatory legibility, and open-ended multi-agent systems assurance remain under-developed. Three cross-domain case studies (medical care, industrial operations, smart-mobility systems) provide operational illustrations of how the five taxonomy dimensions recur in safety-critical settings, grounded in the failure patterns documented in the reviewed literature. The paper concludes with a lifecycle-oriented research agenda centered on bounded-autonomy specifications, adversarial trajectory generation, runtime monitoring, and audit-ready evidence structures. The central claim is that trustworthy deployment of agentic AI depends on validating trajectories in context rather than assessing isolated components alone.

</details>


### 5. Zero-Mem: Zero-Token Memory Operations for LLM Agents

- **Authors:** Yilin Xiao, Zhehan Zhu, Yujing Zhang, Jin Chen, Zijin Hong, Luyao Zhuang, Qinggang Zhang, Shengyuan Chen, Xiaocao Ouyang, Lingfei Ren, Xiao Huang
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29377v1](http://arxiv.org/abs/2607.29377v1)
- **PDF:** [https://arxiv.org/pdf/2607.29377v1](https://arxiv.org/pdf/2607.29377v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents need memory to act consistently over long interactions, yet many systems use additional LLM calls to operate that memory. Generating intermediate records and mediating their retrieval adds recurring token and time costs, while omitted or merged details can obscure the original evidence. We ask whether structured memory access requires generation at all. Zero-Mem introduces \emph{zero-token memory operations}: no step outside final question answering invokes an LLM or consumes LLM input or output tokens; encoder computation is accounted for separately. Zero-Mem preserves original interaction traces as its source of record. It organizes the traces in two complementary ways. An entity--context graph exposes connections across interactions, while a temporal hierarchy preserves conversational locality and session state. For each query, Zero-Mem weighs the two views, retrieves from both, and follows their structure to recover supporting relations or surrounding context. Deterministic calibration first discards conflicting evidence and then keeps the reader's answer grounded in the retrieved traces. Only the final-QA reader invokes an LLM. Across long-memory and long-context question-answering benchmarks, Zero-Mem achieves competitive performance while eliminating LLM calls and LLM-token consumption from memory operations. With the same final-QA reader and context budget, it reduces memory-operation time cost by 57.6\% relative to the fastest compared baseline. Ablations support the contribution of the two views and their query-dependent coordination. Overall, the results show that structured agent memory need not generate an intermediate representation of the past. After peer review, the code and implementation details will be available at \textcolor{blue}{https://github.com/TheMoon0815/Zero-mem}.

</details>


### 6. SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery

- **Authors:** Jiamin Wu, Peishan Xiang, Jingyang Chen, Yuqing Zhu, Yuxi Li, Ling Luo, Qihao Zheng, Jialiang Zu, Yongchao Wu, Mindong Liu, Haitao Wu, Chaofan Hu, Yijie Sun, Yuqi Hang, Yu Zhu, Shuo Li, Yue Fan, Shiyang Feng, Wanghan Xu, Tianlei Zhang, Jie Zhang, Wenlong Zhang, Bo Zhang, Kai Wang, Lei Bai, Mianxin Liu, Wanli Ouyang, Jiulin Du, Chunfeng Song
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29347v1](http://arxiv.org/abs/2607.29347v1)
- **PDF:** [https://arxiv.org/pdf/2607.29347v1](https://arxiv.org/pdf/2607.29347v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern neuroscience relies on integrating multi-scale, multimodal datasets to uncover the neural principles underlying intelligence. However, analytical challenges posed by highly heterogeneous data and fragmented workflows increasingly constrain discoveries. Here we introduce SeekBrain, an autonomous multi-agent framework designed to accelerate neuroscience discovery through domain-grounded hierarchical planning and cross-modal data analysis. SeekBrain dynamically constructs a repertoire of analysis recipes extracted from code-paper pairs. By coupling this codified expertise with agentic planning and execution engines, the framework scalably generates hypotheses and analytical pipelines on demand. Systematic evaluation on the expert-annotated BrainArena benchmark demonstrates that SeekBrain substantially outperforms state-of-the-art agent baselines across various analysis tasks. Crucially, when deployed in real-world research, SeekBrain integrated behavioral, neural, and anatomical data to reveal structured, distributed neural representations of larval zebrafish behavior and a shared axis of regional decoding strength across the brain in a mouse decision-making task. These results establish SeekBrain as a scalable and practical tool for accelerating data-driven discoveries in neuroscience.

</details>


### 7. Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents

- **Authors:** Minghui Pan, Jiayuxuan Yang, Yuanyuan Yuan, Yu Jiang, Zhenpeng Chen
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29254v1](http://arxiv.org/abs/2607.29254v1)
- **PDF:** [https://arxiv.org/pdf/2607.29254v1](https://arxiv.org/pdf/2607.29254v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents extend large language models (LLMs) with external tools, enabling them to perform complex tasks and translate model outputs into consequential real-world actions. Yet LLMs often become substantially less safe when deployed as agents, and the source of this degradation remains poorly understood. In this paper, we identify schema-formatted tool specifications as a primary source of agent safety degradation and show, through white-box representation analysis, that they weaken the model's internal refusal signals and contribute to unsafe tool execution. Building on this finding, we propose SafeKeep, an inference-time safeguard that decouples safety judgment from tool execution: it assesses requests using flattened textual tool specifications while retaining the original schema-formatted specifications for execution. Across two representative benchmarks and four LLMs, including both white-box and black-box models, SafeKeep increases the average refusal rate for harmful requests from 23.8% to 70.6% and reduces the average attack success rate under observation-level prompt injection from 25.6% to 2.5%. It also outperforms existing safeguards and preserves task-handling capability. We release the code and data at https://github.com/snowcatsmoking/SafeKeep .

</details>


### 8. Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation

- **Authors:** Goutham Ramakrishnan, Megha Sharma
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29250v1](http://arxiv.org/abs/2607.29250v1)
- **PDF:** [https://arxiv.org/pdf/2607.29250v1](https://arxiv.org/pdf/2607.29250v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Small language models (SLMs) are attractive for agentic deployment due to low latency, reduced cost, and on-device privacy, yet they struggle with tool-use tasks where training data is scarce and noisy. Unlike larger models, SLMs cannot compensate for low-quality supervision through sheer capacity, making data quality the critical bottleneck. We present Data Turnstile, an open-source framework that takes user-defined API specifications and generates high-quality synthetic training data for function calling. Turnstile decomposes multi-turn tool-use interactions into constrained, stepwise generation with validation and error-feedback loops, providing fine-grained control over API diversity, conversation complexity, and output correctness. We demonstrate effectiveness of domain adaptation with Turnstile data on two challenging function calling benchmarks. On the BFCL single-turn benchmark, a Qwen3-0.6B fine-tuned on Turnstile data without chain-of-thought achieves 75.9% overall accuracy (versus 67.4% for the base model with thinking enabled), closing the gap with thinking-enabled Qwen3-1.7B (78.4%) and Qwen3-4B (79.9%) despite being 3$\times$ and 7$\times$ smaller respectively. On $τ^2$-bench, a multi-turn agentic benchmark, Turnstile-trained Qwen3-1.7B achieves 31.1% pass^1 on the Telecom domain, improving 4.7$\times$ over its 6.6% base and surpassing Qwen2.5-32B-Instruct (27.4%), a model 19$\times$ larger. Turnstile-trained Qwen3-0.6B achieves 24.6%, improving 7$\times$ over its 3.5% base and approaching the 32B model (53$\times$ larger). We release Data Turnstile along with a dataset spanning 1,000+ APIs and 100K+ multi-turn interactions.

</details>


### 9. Don't Mix Rewards, Mix Policies: Policy Decomposition and Optimization for Multi-Reward RL

- **Authors:** Ruiming Liang, Yi Zhong, Yizhen Yuan, Yinan Zheng, Tianyi Tan, Tianyue Wang, Haiyun Guo, Jinqiao Wang, Xianyuan Zhan
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29246v1](http://arxiv.org/abs/2607.29246v1)
- **PDF:** [https://arxiv.org/pdf/2607.29246v1](https://arxiv.org/pdf/2607.29246v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern large language models (LLMs) are expected not just to answer correctly, but to adapt their behavior to different human values and use cases. As a result, multi-reward reinforcement learning (RL) has become an increasingly important problem for LLMs, where each reward captures a different aspect of desired behavior. However, optimizing with multiple rewards suffers from a more severe alignment tax issue, where different optimization objectives can trade off or even conflict with each other, leading to unstable and inefficient post-training. In this work, we propose PRISM, a new multi-reward RL framework built upon the idea of policy-space decomposition and composition. Instead of compositing different rewards, PRISM optimizes a set of standalone positive policies and a global negative policy. This alleviates the potential conflict during multi-reward policy optimization, while enabling controllability during inference by flexible policy composition. Experiments on scientific reasoning, tool-use reasoning, and helpfulness-safety alignment show that PRISM consistently outperforms existing multi-reward RL baselines, with extra controllability for inference-time preference control.

</details>


### 10. CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents

- **Authors:** Blaise Delattre, Cong Wang, Yang Cao
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29190v1](http://arxiv.org/abs/2607.29190v1)
- **PDF:** [https://arxiv.org/pdf/2607.29190v1](https://arxiv.org/pdf/2607.29190v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using LLM agents act on typed tool returns, records pairing provenance and categorical fields with numerical values. Runtime permission gates generally authorize the observed return and action, leaving the decision unprotected against small errors in how the return was bound to its source. We ask whether a candidate action stays authorized over a declared neighborhood of plausible correctly bound returns: one admissible binding fault plus bounded numerical drift. We prove that certifying the categorical and numerical channels separately does not compose: perturbations that are safe on each channel alone can jointly turn the same action unsafe. CAGE certifies this joint neighborhood directly, enumerating the discrete branches exactly and certifying the continuous perturbation within each branch. Across synthetic, policy-as-code, regulatory, and real-transaction settings, CAGE removes the in-budget false allows that accurate pointwise gates admit, while keeping a useful fraction of decisions autonomous. When the policy is executable, CAGE-Exact certifies the policy itself; otherwise CAGE-Lip and CAGE-RS certify a learned gate under an explicit, measured fidelity assumption.

</details>


### 11. Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory

- **Authors:** Jinghan Xu, Yiyong Xiao, Wanru Shao, Hankai Liu, Xinjin Li
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29167v1](http://arxiv.org/abs/2607.29167v1)
- **PDF:** [https://arxiv.org/pdf/2607.29167v1](https://arxiv.org/pdf/2607.29167v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context. We identify memory provenance laundering: during LLM-based memory consolidation, an external observation may be rewritten as apparent user history or workflow support, preserving an action trigger while erasing the low-trust source that should limit its authority. Existing prompt filters, content sanitizers, and tool guards do not enforce source-authority non-amplification after lossy memory consolidation. We formalize this boundary and instantiate it as Provenance-Preserving Memory Fire wall (PPMF), a lightweight memory middleware that preserves platform-maintained provenance and authorizes tool calls by matching action risk to the authority of action-relevant memories. In our schema-grounded evaluation with fixed risk policies, vulnerable consolidated memories reach up to 1.000 attack success rate(ASR); with intact platform-maintained provenance, confirmation, and risk labels, no evaluated unauthorized high-risk action passes the PPMF gate while confirmed benign actions and targeted low-risk memory use remain executable.

</details>


### 12. Autonomous Repair for Multi-Agent Systems via Monte-Carlo Tree Search

- **Authors:** Hanxiao Lu, Tianyi Zhang
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29055v1](http://arxiv.org/abs/2607.29055v1)
- **PDF:** [https://arxiv.org/pdf/2607.29055v1](https://arxiv.org/pdf/2607.29055v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) are increasingly deployed to solve complex tasks. In case of incorrect or unsatisfactory outputs, users have to manually locate agent mistakes by inspecting agent trajectories (i.e., {\em failure attribution}) and provide feedback to refine the outputs (i.e., {\em repair}). Despite some recent work in MAS failure attribution, automated mechanisms to recover from such mistakes remain largely unexplored. To bridge this gap, we propose MARS, a search-based framework that formulates MAS repair as a Monte Carlo Tree Search (MCTS) process and navigates the vast space of potential repairs via diagnosis-guided expansion with taxonomy-augmented evaluation. Unlike standard MCTS, which evaluates a complete simulation via full rollout, MARS evaluates the agent trajectory using partial rollout to reduce token consumption. Furthermore, we introduce StateMAS, a large-scale MAS repair benchmark with 1,310 replayable multi-agent failure trajectories spanning four types of agent architectures and four LLM backbones. Experiments on StateMAS demonstrate that MARS consistently outperforms state-of-the-art methods, achieving an absolute improvement from 3.0\% to 12.1\% across all settings, while maintaining a comparable token consumption cost. The ablation study further confirms that taxonomy-augmented evaluation and diagnosis-guided expansion are critical to achieving these performance gains.

</details>


### 13. TransMem: Transforming Hidden States into Memory for Large Language Models

- **Authors:** Haodong Lei, Junming Liu, Yirong Chen, Pinlong Cai, Botian Shi, Ding Wang, Hongsong Wang
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.29032v1](http://arxiv.org/abs/2607.29032v1)
- **PDF:** [https://arxiv.org/pdf/2607.29032v1](https://arxiv.org/pdf/2607.29032v1)
- **Categories:** cs.MA, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly operate over long interaction histories, where effective reasoning requires identifying and exploiting task-relevant evidence distributed across past observations and actions. However, useful information encoded in previously computed representations is often underutilized during subsequent generation. We propose \textbf{TransMem}, a lightweight inference-time parametric memory module that transforms sparse historical hidden states from a frozen LLM backbone into reusable memory representations. TransMem uses a lightweight gating network to dynamically apply the latent intervention to the current hidden states, without repeatedly encoding the preceding context. To learn transferable memory utilization rather than task-specific knowledge, we introduce evidence-conditioned self-distillation. A memory-augmented student processes the full context and matches the predictive distribution of an evidence-only teacher that shares the same frozen backbone. Experiments on LoCoMo, HotpotQA, and MemoryAgentBench demonstrate consistent improvements across different model architectures and scales. TransMem yields gains of 11.58--29.25 $F_1$ on LoCoMo and 10.20--13.03 $F_1$ on HotpotQA, while improving the average MemoryAgentBench accuracy from 29.54\% to 40.00\%. These results establish sparse historical hidden states as an effective and efficient memory substrate for long-context LLM agents. Our code is available at https://github.com/Haodong-Lei-Ray/TransMem.

</details>


### 14. Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled Beam Arbitration for Strict Zero-Shot Image Captioning

- **Authors:** Duy Tran Thanh, Thien-Phuc Doan, Long Nguyen-Vu, Ngo Tan Vu Khanh
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28986v1](http://arxiv.org/abs/2607.28986v1)
- **PDF:** [https://arxiv.org/pdf/2607.28986v1](https://arxiv.org/pdf/2607.28986v1)
- **Categories:** cs.CV, cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Zero-shot image captioning (ZIC) describes images without paired image-caption supervision during captioner training, relying on text-only corpora and frozen pretrained image-text scorers. Existing retrieval-augmented methods score image-text alignment once, at retrieval, then commit the captioner's autoregressive beam under language-model probability alone, leaving the decoder without further visual grounding feedback. Progress has stalled, with no method improving on the strict-regime best since 2024.
  We propose Adjudicated Captioning, an inference-time multi-agent framework that restores grounding feedback at multiple checkpoints over an unchanged IFCap captioner. First, we install a stronger frozen Retrieval Encoder at the input. Second, between retrieval and decoding we insert a frozen Cross-Attention Verifier that re-ranks the top-9 retrievals to top-5. Third, at the output beam we attach a learned Reranker pairing TriFuse, a multilayer perceptron, with MemAttend, a memory-attended transformer, the pipeline's only learned components; both are trained self-supervised by Borda-consensus distillation across the three frozen scorers, using no paired image-caption labels and no reference captions.
  Under the inductive headline protocol, with rerankers fit on the disjoint COCO Karpathy validation beam and applied frozen to test, the framework reaches CIDEr 117.6 and SPICE 21.9 on COCO Karpathy, up from 108.0 and 20.3 for IFCap, a +9.6 CIDEr gain, and +7.7 above NES, the strongest synthetic-image-augmented method at 109.9, without retraining the captioner. A training-free fixed-fusion baseline reaches 115.8 CIDEr, so +7.8 of the +9.6 gain comes from the non-learned architectural intervention and the remaining +1.8 from the learned rerankers. The same recipe transfers off-COCO without captioner retraining: +8.1 CIDEr on Flickr30k Karpathy and +5.7 on NoCaps overall.

</details>


### 15. Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models

- **Authors:** Jin-woo Lee, Minkyung Song, Junghyun Oh, Seunghoon Han, Soyoung Park, Gwangseon Jang, Sungsu Lim
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28979v1](http://arxiv.org/abs/2607.28979v1)
- **PDF:** [https://arxiv.org/pdf/2607.28979v1](https://arxiv.org/pdf/2607.28979v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Heterogeneous Large Language Model (LLM) systems increasingly rely on shared contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures. Consequently, each model must repeatedly prefill or store caches for the same context, limiting the scalability of multi-model reasoning and long-context generation. We propose Mixture-of-Translators(MoT), a cache translation framework that maps context KV caches from a source LLM into the cache space of a target LLM. Unlike prior approaches that depend on a single projection path or global shared latent space, MoT uses multiple translator modules to capture diverse source--target mappings. To further reduce residual translation error, we introduce a Context Correction Loss that aligns the replayed target trajectory with the native target trajectory. We reveal two competing failure modes in cache translation: propagated translation shift from early injection and last-state shift from late injection. MoT addresses them through translator mixtures and target-side correction. Across homogeneous and heterogeneous translations among Qwen2.5, GPT-2, and OPT models, MoT preserves downstream QA performance, including Qwen2.5-7B-scale translation with 51.0% average closed-set QA accuracy and 0.43 average extractive QA F1. In practical case studies, MoT enables quality-preserving memory reuse for multi-agent reasoning and retains 96.3% of direct-context quality in long-context cache-augmented generation, demonstrating scalable KV cache reuse across heterogeneous LLMs.

</details>


### 16. MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations

- **Authors:** Qiming Shi, Yulong Tao, Linbo Jin, Zhaolu Kang, Yibo Dou, Jiawen Zhu, Tianjun Pan, Shaokang Fu, Chengyu Wang, Siyue Li, Yaping Cheng, Di Weng, Chengfu Huo
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28956v1](http://arxiv.org/abs/2607.28956v1)
- **PDF:** [https://arxiv.org/pdf/2607.28956v1](https://arxiv.org/pdf/2607.28956v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents are increasingly evaluated as autonomous tool users, yet most benchmarks focus on bounded tasks with immediate success criteria. Real-world deployments often require Long-Term Coherence, the capacity to preserve purposeful behavior across extended horizons while adapting decisions to accumulated evidence. Evaluating this capacity requires a persistent environment in which actions constrain future choices, feedback arrives at heterogeneous delays, and incoherent behavior produces measurable cumulative effects. Seller-side e-commerce provides a suitable setting for this evaluation through recurrent and interdependent decisions over Product Sourcing, Listing and Pricing Control, Cash-Flow Management, and Mixed-Latency Feedback Adaptation. We introduce MerchantBench, a 365-day order-level simulation grounded in 98,843 real e-commerce product records and equipped with 26 tools for agent interaction. MerchantBench couples promptly observable Upstream Supplier Events with delayed Downstream Order Outcomes, requiring agents to follow individual order lifecycles and revisit earlier decisions. We evaluate eight LLMs under two agent frameworks in 48 runs, each spanning 365 simulated days. Our results reveal a substantial gap between even the latest LLMs and human participants, with the best LLM configuration attaining only 27.3\% of the mean final net assets achieved by human participants.

</details>


### 17. NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability

- **Authors:** Duo Xu, Faramarz Fekri
- **Published:** 2026-07-31
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28942v1](http://arxiv.org/abs/2607.28942v1)
- **PDF:** [https://arxiv.org/pdf/2607.28942v1](https://arxiv.org/pdf/2607.28942v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recently Large Language Models (LLMs) have been increasingly deployed as autonomous agents in applications such as self-reflection, retrieval-augmented generation, and scientific discovery. In these settings, agents must act based on limited observations rather than full environmental states, leading to partial observability. This introduces several key challenges: belief state inference, task objective misalignment, and planning under uncertainty. Prior approaches typically condition actions on full or summarized action-observation histories whose redundant and irrelevant information can mislead the decision making of LLM agent. Inspired by human cognition, we propose a novel neuro-symbolic fast-slow thinking (NeSyFS) framework for LLM agent, addressing the challenges introduced by partial observability in a unified approach. We use a knowledge graph (KG) to represent the belief state, providing triplets as context for every module of NeSyFS. The fast-thinking module performs reactive action, while slow-thinking conducts a new uncertainty-aware planning by following the high-level structure of twisted sequential Monte Carlo (TSMC) algorithm. To mitigate the misalignment of task objective, a reflection module is used to reflect fast-thinking actions, and also switches to the slow-thinking module whenever reactive actions repeatedly fail. Experiments on three representative benchmarks, i.e. ALFWorld, Webshop, and ScienceWorld, demonstrate significant advantages over previous methods.

</details>


### 18. Open-Source LLM-Driven Formal Verification: A Multi-Agent Pipeline for RTL Repair

- **Authors:** Ha Trung Tran
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28877v1](http://arxiv.org/abs/2607.28877v1)
- **PDF:** [https://arxiv.org/pdf/2607.28877v1](https://arxiv.org/pdf/2607.28877v1)
- **Categories:** cs.AR, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Verification consumes the majority of modern chip design effort, yet the formal verification tools that provide mathematical guarantees of correctness remain expensive and restrictively licensed. While large language models (LLMs) have shown promise for hardware design, existing approaches to RTL repair validate their results through simulation - which exercises only a subset of inputs - or rely on commercial tools, and few combine formal proof with an entirely open-source toolchain. In this paper, we present a multi-agent pipeline that couples an LLM with an open-source formal backend (Yosys, SymbiYosys, and Z3) to repair RTL through counterexample-guided iteration: the framework generates formal properties, verifies the design, and feeds counterexamples back to the LLM until the design is proved correct by k-induction or an iteration budget is exhausted. Through an ALU case study, we show that the pipeline can detect and repair a real functional bug with a formal proof of correctness. Across a six-benchmark suite, one design is repaired reliably, and we characterize four distinct failure modes: bounded-cover vacuity, specification ambiguity, temporal-logic bugs, and multi-property pressure. We frame this work as a feasibility study with a detailed failure analysis, and additionally report a practical limitation of the Yosys bind directive relevant to the open-source formal verification community.

</details>


### 19. Validation Evidence in LLM Repair Agents: How Much of What Passes Actually Tests the Bug?

- **Authors:** Xiaonan Xu, Wenjing Wu
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28871v1](http://arxiv.org/abs/2607.28871v1)
- **PDF:** [https://arxiv.org/pdf/2607.28871v1](https://arxiv.org/pdf/2607.28871v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a repair agent runs a test and sees it pass, the result is treated as evidence about the reported defect. We measure how often that treatment is warranted. BSG-VA (buggy-state/candidate-state/gold-fix validation analysis) captures each validation command at its exact working-tree state, extracts a test-only patch, and replays the command on the original buggy code (B), the candidate state (S), and the developer gold fix (G). The captured outcome and the replay results assign every event an evidence role, from gold-aligned bug-discriminating through regression-only to misleading. Across 3,730 events in 643 rollouts on 110 tasks, 46.0% of positive comparable events carry no bug-discriminating information; 23.8% of baseline rollouts, with no feedback injected, close with a patch whose entire positive evidence base is of this kind. A three-arm experiment tests whether returning the B-replay outcome to the agent changes this pattern. Bug-contrast feedback reduces evidence-inadequate closure by 7.8 percentage points relative to an attention-matched reminder (p = 0.0029) and raises bug-discriminating evidence by 7.4 points (p = 0.011), with no detectable cost to repair success. Both estimates fall below the prespecified 10-percentage-point smallest effect size of interest, so practical magnitude remains uncertain. Roughly a third of the improvement traces to the reminder alone; across two exploratory replications, varying the scaffold and the model, the B-replay content adds a detectable increment only with gpt-5.6-sol under the unconstrained tool-use loop. BSG-VA applies post hoc to any replayable repair trajectory that preserves the required code states and execution environment.
  Keywords: program repair agents, validation evidence, test adequacy, large language models, software quality, controlled experiment.

</details>


### 20. CyberNeuro: A Privacy-Preserving Agentic Workbench for Cohort-Scale Neuroimage and Clinical Data Analysis

- **Authors:** Ran Ren, Junhong Tong, Yunxi Kong, Yiyao Chen, Yucheng Li, Kunhao Zhou, Shaoqi Wang, Yuxiang Tao, Shuheng Cao, Zhihao Fan, Marissa DiPiero, Tingting Dan, Guorong Wu
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28841v1](http://arxiv.org/abs/2607.28841v1)
- **PDF:** [https://arxiv.org/pdf/2607.28841v1](https://arxiv.org/pdf/2607.28841v1)
- **Categories:** cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite tremendous success in neuroimaging methodology, making large-scale, high-dimensional datasets ready for AI/ML applications remains a critical operational bottleneck. Conventional workflows require extensive manual effort across metadata curation, pipeline execution, post-processing quality control, and data management, a burden that disproportionately excludes laboratories with limited manpower and computational infrastructure. To address this real-world barrier, there is an urgent need for scalable, cost-effective computational platforms that democratize advanced neuroimaging analytics and accelerate discoveries in mental health and clinical translation. Capitalizing on multi-agent LLM breakthroughs, we introduce CyberNeuro, an agentic workbench with a tailored local LLM-model ('WandaMind') for automated neuroimaging and health-data analysis. Driven by four dedicated agents (Planner, Validator, Dispatcher, and Reporter) communicating via a secure MCP bridge and a pinned execution layer, CyberNeuro enables researchers to execute complex workflows using natural language while maintaining clinical-grade data privacy. On the public NeuroBench suite, CyberNeuro increases held-out domain accuracy from 40% to 69% over the baseline model. Beyond automated metrics, the platform integrates a human-in-the-loop verification panel to ensure rigorous biomedical quality control. Across the same end-to-end 10-batch cohort workflow suite, the local WandaMind configuration completed all tasks with an estimated aggregate token count of about 10.6% using WandaMind and 61.7% using cloud providers of token usage, compared to Neuroclaw, respectively. The platform and its production-ready modules are available at https://wanda-cyberbench.com.

</details>


### 21. The AnyLog Edge Data Fabric

- **Authors:** Roy Shadmon, Mark Davidson, Eric Aquaronne, Massimiliano Pinto, Ori Shadmon, Moshe Shadmon
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28836v1](http://arxiv.org/abs/2607.28836v1)
- **PDF:** [https://arxiv.org/pdf/2607.28836v1](https://arxiv.org/pdf/2607.28836v1)
- **Categories:** cs.ET, cs.MA, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Industrial and autonomous systems increasingly depend on AI, automation, and real-time coordination to act on operational data as it is generated. Yet conventional architectures often require that data to pass through centralized platforms before decisions can be made. Cloud systems remain valuable for training, reporting, and long-term analytics, but they add latency and external dependencies to the critical decision path and become harder to scale as each new site adds additional edge devices and data. As intelligence spreads across machines, sites, facilities, and vehicles, continued dependence on centralization will constrain response time, resilience, scalability, and autonomous operation.
  This paper presents the AnyLog Edge Data Fabric, an agent- and edge-based platform that manages operational data at its source while presenting distributed data, assets, compute resources, and services as one logical system. Through its Distributed Metadata Layer, Virtual Data Lake, Unified Namespace, Single System Image, and Model Context Protocol, authorized users, applications, automation services, and AI agents can discover, query, process, and act on distributed resources without knowing where they are hosted. Queries and computation execute at the agents holding the relevant data, so only requests and results traverse the network. This preserves local ownership, reduces data movement, supports continued operation during connectivity disruptions, and enables repeatable deployment from validated digital-twin configurations. AnyLog provides a cloud-like operating model for distributed SQL, real-time automation, Edge AI, federated learning, and resilient decision-making without a single point of failure or any dependence on centralized infrastructure.

</details>


### 22. Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures

- **Authors:** Harsh Raj, Vipul Gupta, Anas Mahmoud, Razvan-Gabriel Dumitru, Darvin Yi, Aakash Sabharwal, Yunzhong He
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28802v1](http://arxiv.org/abs/2607.28802v1)
- **PDF:** [https://arxiv.org/pdf/2607.28802v1](https://arxiv.org/pdf/2607.28802v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing evaluations often reduce agent failures to system-level outcomes, obscuring where the fault originated and which intervention would improve the agent system. This creates a repair-assignment problem: the same visible failure may call for model post-training, harness engineering, environment redesign, or benchmark repair depending on its source. Because agent behavior emerges from interactions among models, harnesses, users, tools, memory, and environments, outcome-level labels are often insufficient for improvement. Most failure taxonomies do little to resolve this problem because they are benchmark-specific and lack a shared structure. We introduce an interaction-centric taxonomy that localizes failures to the interactions in which they originate and identifies the responsible component. It organizes 41 failure modes by assigning each to an edge between two components and a fault side indicating where the repair belongs. This makes the taxonomy actionable: model-side failures identify targets for post-training, harness-side failures point to scaffolding and tool-integration fixes, and environment or grader failures reveal evaluation conditions requiring redesign. The schema applies across agent architectures, from coding assistants to long-horizon personal assistants and multi-agent systems. We ground the taxonomy in worked examples from public benchmarks, model system cards, published reports, and logged agent trajectories, and evaluate its reproducibility using independent reasoning agents as judges. Across four frontier models, the strongest judge reaches Cohen's $κ=0.76$ against human category labels, suggesting that the categories capture shared structure rather than annotator-specific preferences.

</details>


### 23. AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis

- **Authors:** Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28618v1](http://arxiv.org/abs/2607.28618v1)
- **PDF:** [https://arxiv.org/pdf/2607.28618v1](https://arxiv.org/pdf/2607.28618v1)
- **Categories:** cs.CL, cs.AI, cs.IR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a result, scientists and AI agents need to locate relevant information, verify their provenance, and assemble cross-paper answers manually. We present AskChem, a claim-centered infrastructure for cross-paper chemistry search. AskChem changes the unit of retrieval from the paper to the provenance-carrying claim: each paper is converted into atomic, typed claims, each grounded by a source DOI and a verbatim quote or an explicit evidence locator. Over this shared claim store, AskChem exposes complementary structures for search and synthesis: a stabilized faceted taxonomy for hierarchical retrieval and browsing, an evidence graph linking claims through relations, and an exploratory living taxonomy that situates indexed papers under scientific principles. AskChem currently indexes 2.4M claims from 147K papers and provides a web interface, as well as REST, SDK, and MCP access for AI agents. On AskChem-Bench, grounding a GPT-5.5 reader in AskChem yields 100% resolvable DOIs, compared with 88.3% without retrieval, and the highest citation density among five tested systems. AskChem is live at https://askchem.org.

</details>


### 24. PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks

- **Authors:** Manyi Wang, Junjielong Xu, Pinjia He
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28587v1](http://arxiv.org/abs/2607.28587v1)
- **PDF:** [https://arxiv.org/pdf/2607.28587v1](https://arxiv.org/pdf/2607.28587v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

SWE-bench-like benchmarks are widely used for evaluating LLM's issue resolution capability. They typically follow a common construction pipeline: each PR (Pull Request) is paired with its linked issue by extracting issue references from the PR description; the issue description is used as the problem statement, and the PR patch serves as the test oracle. However, due to the inherent complexity of developing and maintaining large repositories, such PR-Issue pairings are often misaligned in practice. In this work, we systematically study SWE-bench Verified instances, finding that 13.6% exhibit misalignment across five patterns in eleven fine-grained scenarios. To enable reliable and scalable construction of those benchmarks in the future, we propose PAIChecker, a multi-agent system for checking PR-Issue misalignment in SWE-bench-like benchmarks. Specifically, PAIChecker adopts a three-phase design that combines specific pattern identification, cross-agent label synthesis, and code-level validation, thereby enabling more accurate, generalizable, and progressively verified detection. Experiments on SWE-Gym and SWE-bench Multilingual show that PAIchecker achieves the best performance across all four LLM backbones, reaching up to 92.12% and 91.67% binary accuracy, respectively.

</details>


### 25. MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems

- **Authors:** Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28527v1](http://arxiv.org/abs/2607.28527v1)
- **PDF:** [https://arxiv.org/pdf/2607.28527v1](https://arxiv.org/pdf/2607.28527v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning. MANTA achieves the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.

</details>


### 26. AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration

- **Authors:** Xinxing Ren, Qianbo Zang, Ziyan Wang, Caelum Forder, Suman Deb, Peter Carroll, Zekun Guo
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28430v1](http://arxiv.org/abs/2607.28430v1)
- **PDF:** [https://arxiv.org/pdf/2607.28430v1](https://arxiv.org/pdf/2607.28430v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Understanding large codebases is a long-horizon task for Large Language Model (LLM) agents: answering a single question can require building and running the software, tracing execution across files, and synthesizing evidence over tens of minutes. On SWE-Atlas QnA, a benchmark of long-horizon questions over production repositories, a single Claude Code agent (Opus 4.6) resolves only 32.3% of tasks. Dividing the work among agents with clean contexts mitigates this limitation. However, the subtasks of code comprehension are interdependent. One agent's findings can rewrite another's task, so agents must coordinate during execution, not only at phase boundaries. Existing multi-agent systems support such exchange only between phases, through staged handoffs or synchronized rounds. Communication and work remain mutually exclusive. A discovery made mid-execution cannot be shared until the next boundary. We present AgentRadio, an asynchronous message-passing layer that equips coding-agent harnesses with three primitives: threads, messages, and waiting for mentions. The last runs as a background task, surfacing teammates' messages without interrupting foreground work, so each agent remains passively aware of its peers and folds new findings into its ongoing task. Under a five-phase protocol of division of labor and negotiation, four agents organized by AgentRadio resolve 62.1% of tasks, 29.8 points above a single agent and above Claude Code with the newer Opus 4.8 (57.2%). Rubric-level analysis shows the gain growing with task difficulty, consistent with mid-course correction as the underlying mechanism. Our code is available at https://github.com/Coral-Protocol/AgentRadio.

</details>


### 27. Paying for Honesty Without Knowing the Truth: Reputation-Penalty Design for LLM Marketplace Agents

- **Authors:** Mingdai Yang, Shicheng Fan, Kejing Yu, Duohao Wang, Li Sun, Hao Peng, Philip S. Yu, Zhiwei Liu
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28330v1](http://arxiv.org/abs/2607.28330v1)
- **PDF:** [https://arxiv.org/pdf/2607.28330v1](https://arxiv.org/pdf/2607.28330v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly act as autonomous merchants that write their own product listings, and under competitive pressure, they fabricate attributes to win sales. Even under instructions to be honest, they fabricate attributes in a majority of listings across models. A platform's obvious remedy---verifying each claim against the truth---is unavailable, because it observes only a noisy, biased complaint signal, never the ground truth. We design CARP, a reputation-penalty mechanism with a deadband that forgives complaint noise and a state-dependent severity that counters reputation-driven detection erosion. CARP requires no product-level ground truth and is robust to strategic gaming. CARP protects consumers by suppressing the sales volume of low-rated liars while sparing honest sellers. Paired with SPARC, it closes most of the consumer-welfare gap relative to a perfect-information oracle, without ever accessing the truth. It also achieves the best welfare of the policies we compare. We further show that this felt penalty becomes behaviorally binding through SPARC, a byte-clean code-gated reflection mechanism: LLM merchants fabricate when lying is free but restrain themselves when fabrication costs them sales, a self-interested response rather than compliance. We trace this distinction to penalty-gated self-correction reasoning, and observe the binding across models, with supporting confidence intervals.

</details>


### 28. One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence

- **Authors:** Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28317v1](http://arxiv.org/abs/2607.28317v1)
- **PDF:** [https://arxiv.org/pdf/2607.28317v1](https://arxiv.org/pdf/2607.28317v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A single human must audit $N$ LLM agents under a budget of $B \ll N$ audits per round, guided by self-reported confidence that may be adversarially miscalibrated and by correlated errors. We model this as budgeted noisy inspection over a two-level Gaussian copula and locate the miscalibration threshold $δ^*$ past which confidence-ranked auditing is \emph{worse} than random. Two a-priori expectations reverse: $δ^*$ \emph{rises} as the budget shrinks, and cross-family correlation is not low---shared difficulty dominates lineage. Five open-weight LLMs show operationally useless (near-constant) confidence, point estimates at or beyond the flip though CIs straddle it; a proprietary model is informative and lands below it. We give a quantitative criterion for \emph{vacuous} oversight, and replaying policies on recorded traces confirms the ordering.

</details>


### 29. MemHarness: Memory Is Reconstructed, Not Replayed

- **Authors:** Rong Wu, Daocheng Fu, Licheng Wen, Xuemeng Yang, Shu Zou, Jianbiao Mei, Yuxin Wang, Hairong Zhang, Yu Yang, Tao Hu, Cong Zhang, Botian Shi, Pinlong Cai
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28272v1](http://arxiv.org/abs/2607.28272v1)
- **PDF:** [https://arxiv.org/pdf/2607.28272v1](https://arxiv.org/pdf/2607.28272v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation. This ``replay'' paradigm ignores the gap between the abstract, general nature of stored experience and the concrete, ever-changing states encountered at decision time, frequently causing negative transfer. In contrast, humans rarely recall past experiences verbatim; instead, they reorganize and adapt retrieved memories to fit the present context. Inspired by this, we propose MemHarness, a framework that equips LLM agents to actively harness and reconstruct past experiences based on the present context. At each decision step, a unified policy model critiques and reconstructs the retrieved experience conditioned on the current state, producing context-grounded guidance before acting. This reconstructive ability emerges naturally through end-to-end training with GRPO. Experiments on ALFWorld and WebShop show that MemHarness substantially outperforms pure RL and static memory-augmented baselines, demonstrating strong robustness in out-of-distribution (OOD) scenarios. Furthermore, our analyses reveal that this reconstruction objective not only prevents negative transfer but also serves as latent guidance during training, fundamentally improving the agent's intrinsic reasoning capabilities.

</details>


### 30. Agentic Metaverse Services: A New As-a-Service Paradigm

- **Authors:** Xiaofei Xu, Quan Z. Sheng, Zhongjie Wang, Boualem Benatallah, Xiao Wang, Ruipeng Han
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28242v1](http://arxiv.org/abs/2607.28242v1)
- **PDF:** [https://arxiv.org/pdf/2607.28242v1](https://arxiv.org/pdf/2607.28242v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative Artificial Intelligence (GenAI) is reconstructing the digital virtual world, upgrading agents through enhancing their abilities in autonomous learning, multi-modal interaction, content generation, and collaborative decision-making. In particular, the shift from conversational chatbots to agentic AI, the most recent significant technical breakthrough of GenAI, has brought a new form of services, agentic services and Agent-as-a-Service (AaaS), in which the agent's abilities are encapsulated, such as perception, decision-making, execution, collaboration, and content generation, to provide the customized agent services to users. The metaverse is a virtual ecosystem for human life, work, creation, and entertainment, supported by the new generation of digital technologies. Through combining agentic services and the metaverse, an Agentic Metaverse Service, denoted as AMServ, is produced for metaverse business processing, as a new form of metaverse service. The AaaS in the metaverse environment, denoted as Meta-AaaS, as an approach to realize AMServ, has become a new paradigm of agentic services and service computing. This paper overviews the evolution and new features of agents and services empowered by GenAI, reveals the roles and principles of agentic services in the metaverse environment, presents the forms, characteristics, and principles of the AMServ and the Meta-AaaS, discusses the typical application examples of the AMServ and the Meta-AaaS, and finally points out the new tendencies and research directions of the AMServ and the Meta-AaaS. The AMServ and the Meta-AaaS will bring great opportunities to human society and services in the AI era, and promote the rapid development of emerging service industries in the future.

</details>


### 31. EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents

- **Authors:** Luigi Sigillo, Matteo Silvestri, Francesco Tabaro, Rajat Bhatnagar, Syed Irtaza Mubashar, Matt Jeffryes, Daljit Nijjer, Vittorio Perera, Ola Spjuth, Julio Saez-Rodriguez, Melissa Harrison, Fabio Petroni
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28229v1](http://arxiv.org/abs/2607.28229v1)
- **PDF:** [https://arxiv.org/pdf/2607.28229v1](https://arxiv.org/pdf/2607.28229v1)
- **Categories:** cs.CL, cs.AI, cs.IR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The web is increasingly accessed by AI agents rather than humans. Every agent needs knowledge, especially in the life-sciences, where agentic pipelines are growing fast. Access to the literature is a crucial part of that need, and resources such as Europe PMC, with over 40M indexed records, are widely used to meet it. Yet these resources were not built for AI agents: they take keywords and complex syntax and return whole papers, so every agent must learn the syntax, issue several searches, and read full papers to find the evidence it needs. We introduce EMBL AI Librarian, a knowledge layer that upgrades the Europe PMC interface for AI agents: an agent asks in natural language and receives evidence that answers it. A single LLM orchestrates the whole knowledge retrieval process: it plans complementary subqueries executed by the live Europe PMC search engine, then reads the selected papers and locates the relevant evidence. We evaluate Librarian across four benchmarks: literature synthesis, claim verification, open-domain question answering, and downstream biology tasks such as protocol questions and sequence manipulation. On ScholarQABench, Librarian improves Citation F1 by more than $16$ points over strong recently published baselines. Used as the retrieval layer of an existing claim-verification pipeline, it increases agreement with expert consensus; and on the open-form LitQA2 benchmark, a GPT-5.4 agent scores about $8$ points higher when grounded in Librarian than with web search. Overall, our results show that equipping life-science agents with the Librarian knowledge layer improves performance across a range of tasks. We release our code publicly at https://github.com/petroni-lab/librarian

</details>


### 32. Integrating AI into Requirements Quality Learning in Software Engineering Education: A TPACK-Guided Empirical Study

- **Authors:** Hansika Ekanayake Mudiyanselage, Rohan Jai Dharmaraj, Malik Abdul Sami, Zheying Zhang
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28176v1](http://arxiv.org/abs/2607.28176v1)
- **PDF:** [https://arxiv.org/pdf/2607.28176v1](https://arxiv.org/pdf/2607.28176v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid adoption of generative Artificial Intelligence (AI) in software engineering (SE) practice creates a need for pedagogically grounded approaches to AI integration in SE education, especially in conceptually intensive subjects such as requirements engineering (RE). This study examines a TPACK-guided integration of a multi-agent AI tool into a master-level RE assignment on requirements quality analysis. Using a mixed-methods design (N=100; 72 submissions analysed), we examine how structured assignment design shaped students' AI use, affected their understanding of user story quality criteria, and influenced their perceptions of AI's benefits and limitations. Results show that students used the AI tool selectively, mainly as support for analysis and evaluation rather than automation. Alignment improvements were most evident for structurally concrete requirements quality dimensions, such as value articulation and testability, while negotiability showed mixed effects. Students reported conditional trust, active refinement, and increased awareness of quality criteria, alongside moderate usability challenges. The findings show that TPACK-guided scaffolding can align AI affordances with pedagogical goals and RE content, offering design guidance for responsible AI integration in RE education.

</details>


### 33. MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck

- **Authors:** Dongyi Liu, Haixing He, Xiaobao Wu, Jia Li
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28103v1](http://arxiv.org/abs/2607.28103v1)
- **PDF:** [https://arxiv.org/pdf/2607.28103v1](https://arxiv.org/pdf/2607.28103v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. To address these challenges, we propose Memory Intent-Aware Neural Denoising(MIND), a lightweight defense framework for memory injection attack. Our preliminary analysis reveals that benign and poisoned trajectories exhibit distinguishable relationships between the initial user intent and subsequent behavior. Building on this observation, MIND employs an intent-aware Information Bottleneck(IB) to extract compact intent--behavior representations from the initial intent and turn-level behavior. The IB preserves intent-relevant cross-turn attack signals while filtering task-irrelevant and repetitive information, and a lightweight detector identifies malicious memories from the resulting representations. As such, MIND mitigates information redundancy in multi-turn contexts while avoiding the overhead of repeated LLM auditing. Extensive experiments show that MIND reduces attack success rates while preserving task accuracy and inference efficiency. Notably, on ReAct-StrategyQA, MIND reduces mean ASR-r and ASR-a by 55.4% and 55.3%, respectively, while matching the undefended agent in average accuracy and latency.

</details>


### 34. SKILL-KD: Contrastive Skill Distillation for LLM Agents

- **Authors:** Qiming Shi, Yibo Dou, Jiawen Zhu, Yulong Tao, Linbo Jin, Zhaolu Kang, Yunfan Zhou, Di Weng
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28048v1](http://arxiv.org/abs/2607.28048v1)
- **PDF:** [https://arxiv.org/pdf/2607.28048v1](https://arxiv.org/pdf/2607.28048v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Skill-based prompting has become a practical mechanism for improving large language model (LLM) agents, yet existing skill acquisition methods often treat skills as experience summaries, memory entries, or direct summaries of successful demonstrations. This creates a mismatch for weaker student agents: when a student fails because it lacks task knowledge or operational strategy, its failed trajectory may not contain enough evidence to infer the missing behavior, while the teacher trajectory may be too implicit to be internalized as reusable guidance. We propose SKILL-KD, a contrastive skill distillation framework that treats skills as an explicit distillation medium between agents of different capabilities. Given a student failure and the teacher trajectory on the same task, SKILL-KD distills their actionable discrepancy into a textual skill patch, evaluates the patch by re-running the student, and iteratively refines the patch when the student still fails. To prevent repeated local updates from causing skill drift, SKILL-KD further maintains trace-linked edit histories and performs Drift-Aware Skill Consolidation, deciding whether each patch should add a new rule, delete or modify an existing rule, or be skipped. Across five agent benchmarks and two student settings, SKILL-KD consistently improves frozen student agents over fixed-model adaptation baselines.

</details>


### 35. ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents

- **Authors:** Xingjian Wu, Xuhang Zhu, Xingchen Liu, Junlin Liu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28037v1](http://arxiv.org/abs/2607.28037v1)
- **PDF:** [https://arxiv.org/pdf/2607.28037v1](https://arxiv.org/pdf/2607.28037v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM-based agents are deployed in complex, multi-step workflows, a critical evaluation gap has emerged: most existing benchmarks judge only final outcomes, unable to distinguish reliable reasoning from lucky success or attribute failures to specific process deficiencies, hindering attribution in long-horizon tasks.
  In this work, we present ClawTrack, a dual-assessment benchmark that simultaneously measures what an agent achieves (Task Score) and how it achieves it (Process Score). ClawTrack comprises 320 tasks across 8 domains with 25+ deterministic mock services. A Process Grader scores each reasoning turn along four dimensions (goal alignment, efficiency, information utilization, and result verification), anchored by 12,541 task-specific rubric items. Evaluating 21 models over 16,000+ trials, we find that: (1) process scores effectively attribute success and failure to specific reasoning dimensions, filtering lucky passes invisible to outcome-only evaluation; (2) the four dimensions are complementary, with result verification as the systematic bottleneck; (3) the framework is robust to evaluator choice across different judge LLMs; and (4) process-based trajectory filtering yields consistent post-training improvements across model scales.

</details>


### 36. DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness

- **Authors:** Debin Meng, Jiaming Yang, Zefang Zong, Tengyue Xu, Haining Xie, Yang Li, Peng Chen
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28033v1](http://arxiv.org/abs/2607.28033v1)
- **PDF:** [https://arxiv.org/pdf/2607.28033v1](https://arxiv.org/pdf/2607.28033v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) and LLM-based agents are increasingly being deployed to automate complex workflows, promising to revolutionize data management and processing. However, existing benchmarks predominantly focus on simplified Text-to-SQL translation or data analysis, leaving the critical and complex domain of end-to-end data engineering largely unexplored. To bridge this gap, we introduce DataClawEval, the first comprehensive benchmark designed specifically to evaluate the end-to-end task completion capabilities of autonomous agents in real-world data engineering scenarios. Built upon production-grade code authored by professional enterprise data engineers, it comprises 100 rigorous, end-to-end tasks spanning five execution engines: PySpark, MySQL, HiveSQL, PrestoSQL/Trino, and FlinkSQL. Rather than non-deterministic LLM-as-a-judge scoring, each task is executed within a case-specific, isolated sandbox and graded by deterministic, rule-based scripts. Evaluating 16 frontier agents exposes critical limitations: The strongest model attains only 74.9 overall, and no single model dominates, as each excels on a different engine, revealing strict domain specialization rather than omnipotent proficiency. Thus, autonomous data engineering remains a formidable, unresolved challenge. We release our dataset, containerized environments, and deterministic evaluation scripts at https://github.com/Dicemy/DataClawEval/tree/master

</details>


### 37. SKIMIX: Multi-Agent Harness-Time Scaling with Skill Mixture for Dynamic Harness Engineering

- **Authors:** Jia Luo
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27994v1](http://arxiv.org/abs/2607.27994v1)
- **PDF:** [https://arxiv.org/pdf/2607.27994v1](https://arxiv.org/pdf/2607.27994v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly rely on large skill libraries, but selecting, combining, and maintaining skills remains difficult. We propose SKIMIX, a multi-agent framework in which agents with different skill portfolios collaborate through iterative refinement. SKIMIX combines embedding-based skill retrieval, submodular anti-dilution routing, and adaptive skill evolution. Across six reasoning benchmarks, multi-agent collaboration substantially improves open-ended mathematical reasoning but offers limited or negative gains on multiple-choice tasks. Agent-count scaling is non-monotonic, and most improvements arise during the first refinement round. These results show that task characteristics determine whether skill-level ensembles help and provide practical guidance for scalable agent design.

</details>


### 38. TAPO: Transition-Aware Policy Optimization for LLM Agents

- **Authors:** Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu, Shudong Liu, Zhan Su, Zhuojian Li
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27973v1](http://arxiv.org/abs/2607.27973v1)
- **PDF:** [https://arxiv.org/pdf/2607.27973v1](https://arxiv.org/pdf/2607.27973v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recently, Reinforcement Learning (RL) has emerged as a crucial paradigm for the post-training of Large Language Model (LLM) agents. However, existing methods predominantly rely on sparse task rewards for policy optimization, failing to fully exploit another class of inherently dense supervisory signals naturally present during online interaction: environmental feedback following action execution. Recent theoretical studies suggest that generalization in multi-step, goal-oriented tasks hinges on predictive knowledge of environmental consequences. Inspired by this, we propose TAPO: Transition-Aware Policy Optimization for LLM Agents, a unified training framework that alternates between policy optimization and transition supervision. Beyond standard RL updates, TAPO repurposes rollout data to apply action-conditioned next-observation prediction supervision on a shared backbone model. This approach enhances the model's sensitivity to environmental transition dynamics and action consequences while concurrently optimizing the policy. It serves as a computationally lightweight, plug-and-play enhancement module for existing agent RL algorithms, requiring no additional expert data, extra sampling costs, or inference-time overhead. We conduct systematic experiments on WebShop and ALFWorld, integrating foundation models of various scales with different policy optimization algorithms. Empirical results demonstrate that TAPO consistently improves task performance over pure policy optimization baselines.

</details>


### 39. MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation

- **Authors:** Dawei Wang, Di Zhao, Xinyuan Liu, Marci Chi Ma, Xiaoyang Liu, Chengming Zhou, Gary Ushaw, Richard Davison
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27967v1](http://arxiv.org/abs/2607.27967v1)
- **PDF:** [https://arxiv.org/pdf/2607.27967v1](https://arxiv.org/pdf/2607.27967v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Credit assignment is a fundamental challenge in cooperative multi-agent reinforcement learning, particularly in embodied AI settings characterized by limited and delayed feedback as well as dynamically changing numbers of active agents. We propose MARS-RA, a framework that reformulates credit assignment as a rank aggregation problem using contribution-based pairwise comparisons among agents generated by large multimodal models. This shift from absolute to relative estimation ensures robustness against noise and dynamic agent participation, converting comparison results into contribution scores for potential-based reward shaping. We provide theoretical justification for the convergence and robustness of the proposed framework, and show that Shapley values can be used as an interpretive reference. Experimental results on challenging tasks of different types indicate that MARS-RA can guide agents toward effective cooperation.

</details>


### 40. $Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems

- **Authors:** Peilin Feng, Suorong Yang, Soujanya Poria
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27958v1](http://arxiv.org/abs/2607.27958v1)
- **PDF:** [https://arxiv.org/pdf/2607.27958v1](https://arxiv.org/pdf/2607.27958v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory is central to long-horizon LLM agents, yet existing memory systems primarily preserve interaction content rather than modeling which agents can be trusted and under what conditions. This limitation is particularly important in multi-agent systems, where a central model may be unable to directly verify plausible or correlated peer responses. We introduce $Σ$-Mem, an online reliability memory that records historical competence evidence for individual peers and peer relationship evidence across the peer set. Both forms of evidence are maintained as real symmetric states and updated from post-decision correctness feedback. By Weyl's inequality, the spectral change caused by each event-level update is bounded, enabling stable online adaptation without retraining the underlying models. $Σ$-Mem provides a general write-and-read interface: the same memory can be used for residual steering of a central model, response-free peer routing, or reliability-weighted voting. Across five Qwen-family models, $Σ$-Mem adapts to counterfactual reliability shifts and generalizes to unseen peers and task domains. Direct memory readouts also outperform majority voting and the best fixed peer over the full OOD evaluation set. Moreover, performance improves consistently as more correctness feedback becomes available, indicating that $Σ$-Mem progressively accumulates actionable reliability information. These results establish reliability memory as a reusable foundation for adaptive coordination in LLM-based multi-agent systems.

</details>


### 41. Argonaut: Interactive Visual Exploration for Distributed Optimization

- **Authors:** Srijoni Majumdar, Chuhao Qin, Evangelos Pournaras
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27946v1](http://arxiv.org/abs/2607.27946v1)
- **PDF:** [https://arxiv.org/pdf/2607.27946v1](https://arxiv.org/pdf/2607.27946v1)
- **Categories:** cs.MA, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Distributed discrete-choice optimization in decentralized settings is often hard to explore and navigate: disentangling what other agents choose, how their choices are interdependent, and how they collectively reach a global objective quickly becomes intractable as the system scales. The major limitation is observability of the search process. Existing methods are largely centralized and offer limited support, visualizing only the final solution or providing algorithm backends over a fixed dataset, so how a solution is reached stays a black box. We present Argonaut, a lightweight, containerized optimization dashboard that enables interactive, visual exploration of the entire search process for multi-agent discrete-choice optimization in decentralized settings. Users upload datasets, construct agents and options, modify the decision space and its parameters on the fly, and run multiple algorithm backends to inspect how each configuration shapes local agent decisions and the resulting global objective. By uniting system construction, optimization, and analysis in one interactive loop, the first of its kind, Argonaut makes distributed discrete-choice optimization a human-in-the-loop process rather than a one-shot, black-box computation. We evaluate Argonaut on real-world household-electricity, shared-mobility, and sensor-data-exchange datasets scaling to 5600 agents and up to 1M solutions under brute force. Built on a Node.js interface with extensible Java and Python optimization backends, it maintains a typical runtime of 200 agents over 100 decision attributes in under 30 seconds.

</details>


### 42. Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis

- **Authors:** Linus Sander, Fengjunjie Pan, Vahid Zolfaghari, Andre Schamschurko, Nenad Petrovic, Alois Knoll
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27942v1](http://arxiv.org/abs/2607.27942v1)
- **PDF:** [https://arxiv.org/pdf/2607.27942v1](https://arxiv.org/pdf/2607.27942v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems have the potential to enable collective intelligence and scale toward solving highly complex tasks through coordinated ensembles of specialized agents. However, despite their theoretical potential, the architectural design space remains largely non-systematized and lacks broadly established design principles. Furthermore, the scalability characteristics of such systems are only partially understood so far. This paper makes two contributions. We first distill four design principles for scalable MAS architectures from a structured analysis of prior work: simplicity, elastic feedback, sequential workflows with optional loops, and summary-based communication. We operationalize these principles in a reference architecture whose topology is formalized as a constrained directed workflow graph, and we evaluate four configurations of increasing complexity on a standardized benchmark of terminal-based system engineering tasks using two LLMs of differing capability. Our findings show that scaling yields measurable accuracy improvements with approximately linear cost growth, but only when the underlying LLM exceeds a minimum capability threshold. Performance peaks at intermediate complexity, then degrades due to timeouts and evaluation limitations. In addition, persistent consistency issues emerge as a central challenge across all scaling levels. These results provide concrete design guidance for practitioners and highlight consistency and evaluation standardization as key targets for future research.

</details>


### 43. From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents

- **Authors:** Xu Xia, Jinghua Piao, Min Yang, Xiaochong Lan, Jiaju Chen, Yong Li
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27937v1](http://arxiv.org/abs/2607.27937v1)
- **PDF:** [https://arxiv.org/pdf/2607.27937v1](https://arxiv.org/pdf/2607.27937v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent work on LLM agents is shifting from external capability elicitation to capability internalization, enabling agents to retain useful skills without retrieval at inference time. On-policy self-distillation (OPSD) offers a promising direction, but many existing methods typically supervise students by scoring actions along student-generated trajectories. Such supervision has two limitations: teacher preferences are not validated by environment outcomes, and action-level scores underuse information from student rollouts, teacher rollouts, and their behavioral relationship. We therefore advocate outcome-verified teacher supervision and comparative learning over teacher-student trajectories. Based on this view, we propose Outcome-Verified Comparative Self-Distillation (OVCSD). OVCSD organizes failed student rollouts into a prefix tree, adaptively invokes a skill-conditioned teacher from student-reached states, and retains only outcome-verified successful continuations. It then applies localized comparative learning at the first state-aligned divergence and distills the post-divergence teacher suffix to transfer completion behavior. Experiments on ALFWorld and WebShop across three model scales show that OVCSD consistently outperforms skill-free RL and existing self-distillation baselines, achieving up to 29.7 and 5.4 absolute success-rate gains over the strongest baselines on ALFWorld and WebShop, respectively, while adding less than 3% privileged interaction during training.

</details>


### 44. MMHBench: A Multi-Perspective Benchmark for Mental Health Understanding in Long-Form Videos

- **Authors:** Jinpeng Hu, Erqiang Wang, Shan Wang, Zhuo Li, Peipei Song, Xun Yang, Meng Wang
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27895v1](http://arxiv.org/abs/2607.27895v1)
- **PDF:** [https://arxiv.org/pdf/2607.27895v1](https://arxiv.org/pdf/2607.27895v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mental health understanding in long-form videos requires nuanced reasoning over observable behavior, interpersonal context, and latent psychological states. Existing benchmarks largely reduce this task to coarse-grained classification, providing limited insight into whether models truly understand psychological phenomena or rely on superficial correlations. To address this limitation, we introduce MMHBench, a comprehensive multimodal benchmark for multi-perspective mental health understanding, comprising 268 long-form videos and 2,184 carefully curated questions. MMHBench organizes the evaluation into two complementary settings: (1) third-person assessment, consisting of 605 questions that focus on the interpretation of observable behaviors and multimodal evidence, and (2) first-person perspective-taking, comprising 1,579 questions that require perspective-conditioned reasoning to identify the interpretation of the mental state supported by the available multimodal evidence. We propose a Multi-Agent Question Generation (MAQG) framework that simulates diverse social roles to synthesize questions from multiple perspectives. The generated questions are refined through multi-role feedback and iterative optimization, followed by expert-guided verification to ensure quality and validity. Extensive evaluation of 22 representative multimodal large language models (MLLMs), spanning both open-source and leading closed-source models, demonstrates that long-form video mental health understanding remains highly challenging.

</details>


### 45. ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents

- **Authors:** Stef Cuyckens, Mihaela Jivanescu, Jun Yin, Chao Fang, Marian Verhelst
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27879v1](http://arxiv.org/abs/2607.27879v1)
- **PDF:** [https://arxiv.org/pdf/2607.27879v1](https://arxiv.org/pdf/2607.27879v1)
- **Categories:** cs.AR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents optimize the power, performance, and area (PPA) of register-transfer-level (RTL) designs by iterating over edits, synthesis, and PPA analysis, paying a dollar cost for every LLM call. Prior agents report the quality reached without its normalized cost, attribute that quality to an engineered cross-design memory, and hold the reasoning effort of every call fixed. We propose Ares with three corresponding innovations. (1) We introduce a normalized dollar cost per LLM call reported alongside the figure of merit (FoM), enabling fair comparison across effort levels and optimizers. (2) Using this accounting, we find the construction of the long-term memory matters little. An engineered memory brings no dependable gain over a plain concatenation of the same experience. (3) We instead adapt the per-call reasoning effort by escalating to deeper reasoning only once progress at a lower effort stalls, via a patience counter fit on 21 training designs, allocating reasoning where it pays rather than uniformly across all iterations. On three test designs unseen during training, the effort policy lowers the FoM by 23-27% where the best fixed effort reaches 16-23%, at equal normalized cost. Ares closes up to 83% of the gap from an LLM-drafted multiply-accumulate unit to its highly hand-optimized counterpart, and reaches a 25% deeper FoM than state-of-the-art Dr. RTL at 12% of its tokens.

</details>


### 46. An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding

- **Authors:** Yanyu Ren, Yunfeng Bai, Xizheng Wang, Li Chen, Dan Li
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27877v1](http://arxiv.org/abs/2607.27877v1)
- **PDF:** [https://arxiv.org/pdf/2607.27877v1](https://arxiv.org/pdf/2607.27877v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent vibe coding promises to accelerate software development, yet existing benchmarks rely on synthetic environments that ignore practical time and monetary costs, conflate reasoning with communication, and reward only superficial completion. We introduce multi-agent from-scratch evaluation benchmark, MSEval, evaluating multi-agent coding on real-world tasks. Grounded in 10 authentic, full-stack projects across 10 domains, MSEval scores performance using hierarchical requirements and deterministic rubrics.
  Its execution engine, LegoGent, tests 10 collaboration topologies where agents coordinate via periodic sync intervals and deploy through native CI/CD pipelines. Concurrently, the automated grader TAgent dynamically probes implementations to jointly measure functional success, latency, and prefix-cached token cost. Across 100 runs, MSEval reveals that organizational topology rivals model capability in shaping the speed--cost--quality trade-off. For identical tasks and models, varying the topology shifts scores by over 30 points and doubles wall-clock time. Structured pipelines converge fastest with the highest quality, whereas heavy managerial oversight degrades performance. Ultimately, MSEval establishes a rigorous, reproducible standard for measuring how multi-agent teams actually build software. The benchmark is released at https://github.com/robinren03/MSEval.

</details>


### 47. FinanceHarness: Autonomous Financial Deep Research Framework

- **Authors:** Yijia Xiao, Rujun Han, Yanfei Chen, Zifeng Wang, Ke Jiang, Zhongying CuiZhu, Vishy Tirumalashetty, Wei Wang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27853v1](http://arxiv.org/abs/2607.27853v1)
- **PDF:** [https://arxiv.org/pdf/2607.27853v1](https://arxiv.org/pdf/2607.27853v1)
- **Categories:** cs.CL, cs.AI, q-fin.CP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Powered by advances in LLMs and autonomous agents, deep research has become one of the most widely adopted agentic products. However, most deep research systems write general-purpose reports, which are inadequate for financial deep research. Financial research demands specialized knowledge to analyze historical patterns and forecast upcoming events. Automating financial deep research therefore requires both a layered harness to drive the research agent and a verifiable, point-in-time benchmark that prevents leakage of future information. We present FinanceHarness, a harness that runs finance-oriented tools and practitioner-guided workflows, automating financial deep research end to end: environment and data construction, the agent execution loop, and reward modeling. We further propose FinanceGym, comprising thesis-driven research questions and rubrics that combine pre-cutoff and post-cutoff criteria. Professional expert validation yields an 82% pass rate. Even leading LLMs and agents score below 40% on the rubrics, showing that FinanceGym is challenging and leaves substantial headroom. With the same open-weight backbone, FinanceHarness improves the overall rubric score from 25.3% to 32.4%. FinanceHarness is available at https://github.com/Yijia-Xiao/FinanceHarness.

</details>


### 48. Code Is the Body: Agent-Owned Software Bodies for Recursive Evolution and Descent

- **Authors:** Roy Zhao, Zhenyu Zhao
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28691v1](http://arxiv.org/abs/2607.28691v1)
- **PDF:** [https://arxiv.org/pdf/2607.28691v1](https://arxiv.org/pdf/2607.28691v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personalized AI agents are often configurable without giving users control over the artifacts that determine their future behavior. We present OurArk, an architecture for persistent personal agents centered on an agent-owned software body: an identity-bearing, inspectable, and versioned artifact under human custody. The body contains behavior-defining code, prompts, tools, skills, policies, tests, and evolution mechanisms. Memories and credentials remain private instance state, while model inference is treated as a replaceable external service. OurArk defines governed self-evolution and recursive descent over the same body. Self-evolution produces isolated candidate changes that are validated, reviewed, and merged under human control, enabling human-agent co-development of the agent's software body. Descent creates an independently versioned descendant with a distinct identity, mission, history, and fresh private-state boundary; compatible descendants can themselves source further descent. After divergence, direct-parent changes and peer skills can be inspected for selective local adaptation. We implement the architecture in the open-source Genesis creation engine and Enoch reference agent. A four-agent, three-descent linear lineage and executable regression tests demonstrate recursive creation, inherited validation contracts, isolated body changes, human-controlled review, and failed-update recovery. OurArk provides a concrete substrate for personal agents that people can possess, govern, specialize, and evolve over time.

</details>


### 49. ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory

- **Authors:** Yongye Su, Wujiang Xu, Chaoji Zuo, Elisa Bertino
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27773v1](http://arxiv.org/abs/2607.27773v1)
- **PDF:** [https://arxiv.org/pdf/2607.27773v1](https://arxiv.org/pdf/2607.27773v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on long-term memory to support multi-session interaction and personalization. However, existing agent memory systems are designed around forward-only evolution, continuously accumulating, consolidating, and overwriting knowledge, with no principled mechanism to inspect, version, or revert prior states. This makes agents brittle under corrections, concept drift, and memory corruption, particularly after they have already been exposed to subsequent information. We present ChronoMem, a semantic version-control layer for agentic memory integrated into the production-ready, open-source Agent Development Kit by Google. ChronoMem commits whole-memory snapshots at each memory write, maintains structured version histories, and supports natural-language rollback requests by mapping undo intents to concrete historical versions through hybrid lexical and semantic retrieval, rank fusion, and reranking. We further introduce a post-exposure evaluation protocol that tests whether an agent can behave counterfactually after rollback by answering queries and summarizing history as if future updates had never occurred. On long-horizon conversational benchmarks augmented with evolving memory states and rollback tasks, ChronoMem substantially improves rollback-consistent question answering and history summarization relative to prompt-only and retrieval-only baselines, while achieving strong performance in semantic version selection. To our knowledge, ChronoMem is the first open-source system and benchmark for systematic semantic global memory rollback in LLM agents.

</details>


### 50. VeriSkill: A Self-Evolution Framework for Program Verification Skills

- **Authors:** Changguo Jia, Tianqi Zhao, Zhiyou Xiao, Weiming Zhang, Minghui Zhou
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27733v1](http://arxiv.org/abs/2607.27733v1)
- **PDF:** [https://arxiv.org/pdf/2607.27733v1](https://arxiv.org/pdf/2607.27733v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automating program verification with LLM agents requires generating specifications, annotations, auxiliary lemmas, and tool invocations, all of which depend on reusable skills. A natural remedy is skill self-evolution: distilling skills from trajectories and refining them through feedback. However, existing evolution methods struggle with program verification tasks because they cannot reliably identify skill-specific failures or extract actionable signals from opaque verifier feedback. In this paper, we propose VeriSkill, a self-evolution framework built for program verification. It attributes verification failures to skill deficiencies, distills diagnostic signatures into reusable lessons, and iteratively refines candidate skills, admitting only revisions that improve verification performance while preserving program semantics. Experiments show that VeriSkill consistently outperforms all baselines across multiple verification tools, agent frameworks, and LLM backends.

</details>


### 51. Baikal: Structured Search for Deep Research over Data Lakes

- **Authors:** Dhruv Agarwal, Rishitha Guttapalle Mohan, Aarti Kumari, Ashi Sinha, Athulya Anil, Kavitha Srinivas, Horst Samulowitz, Andrew McCallum
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27726v1](http://arxiv.org/abs/2607.27726v1)
- **PDF:** [https://arxiv.org/pdf/2607.27726v1](https://arxiv.org/pdf/2607.27726v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep research over data lakes requires an LLM agent to investigate evidence across thousands of heterogeneous tables and passages to synthesize a report. Existing methods perform iterative retrieval and generation, letting accumulated context determine what to investigate next, which can overexploit locally promising evidence and fail to cover distinct semantic regions under a fixed budget. To address this, we cast deep research over data lakes as a budgeted search problem and present Baikal - a framework that clusters heterogeneous evidence into semantic regions, then searches over them adaptively to balance exploration and exploitation. Within each selected region, Baikal generates and investigates region-grounded subquestions, using finding quality as rewards to update region-level value estimates and guide search under policies ranging from random and LLM-guided selection to Bayesian $ε$-greedy and UCB. We evaluate Baikal on 15 queries each over HybridQA and TAT-QA data lakes containing 10,993 and 2,757 tables, respectively, together with 227K Wikipedia passages and 13K financial report passages. We assess research quality with a new rubric covering groundedness, relevance, diversity, and utility, and use GPT-5-mini to score Baikal and strong baselines, including DeepSearcher and an OpenCode research agent with retrieval and clustering variants. Across both data lakes, Baikal performs strongly under several region-selection policies; its best configuration improves report scores over the strongest baselines by 28% on HybridQA and 36% on TAT-QA. Our analyses attribute these gains to organizing and exploring semantic evidence regions, which improves groundedness and diversity and yields more useful findings under the same subquestion budget. These results demonstrate the value of structured semantic exploration for systematic research and discovery over heterogeneous data lakes.

</details>


### 52. MECA: A Mechanism-Centered Agent for Constructing Well-Specified and Valuable Mathematical Conjectures

- **Authors:** Wentao Long, Yunfei Zhang, Chenyi Li, Zaiwen Wen
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27709v1](http://arxiv.org/abs/2607.27709v1)
- **PDF:** [https://arxiv.org/pdf/2607.27709v1](https://arxiv.org/pdf/2607.27709v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automatically constructing well-specified and valuable mathematical conjectures remains a central challenge in AI-assisted mathematical discovery. Many existing open problems and conjectures are often too broad, underspecified, or difficult to connect to plausible proof or refutation strategies. We view a mathematical mechanism as a structure or reasoning principle that connects the assumptions of a candidate problem to its target conclusion, such as an inequality, invariant, decomposition, or reduction to an intermediate claim. We present MECA (MEchanism-centered Conjecture Agent), a multi-agent framework that constructs conjectures by jointly developing candidate statements and their supporting mechanisms. Explorer agents propose mechanisms, test how they apply, and revise the candidate conjecture accordingly, while critic agents assess their mathematical validity and research value. Their feedback guides changes to the assumptions, scope, and conclusion. Through this process, MECA transforms broad research directions into precise conjectures with substantive mathematical support while retaining a clearly identified unresolved core. We evaluate MECA in two complementary settings. First, we compare it with a generate-and-revise baseline on reconstructing preselected target-paper conclusions from target-conditioned but article-blind source materials. Second, we construct 100 semi-open problems from literature-derived seeds and existing open problems and evaluate them through independent proof and refutation attempts by automated provers. Our results indicate that mechanism-centered refinement produces well-specified and research-worthy conjectures that remain challenging for current automated provers.

</details>


### 53. SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

- **Authors:** Yang Zhou, Zixuan Huang, Sunzhu Li, Zhuo Yang, Chen Zhang, Shunian Chen, Caijun Yan, Jianyao Xu, Shunyu Liu, Weijie Fu, Peiliang Li, Xiaozhi Chen, Yuxiang Cai
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27703v1](http://arxiv.org/abs/2607.27703v1)
- **PDF:** [https://arxiv.org/pdf/2607.27703v1](https://arxiv.org/pdf/2607.27703v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) are increasingly used in embodied agents to interpret visual inputs, reason about spatial relationships, and make task-level decisions based on that reasoning. However, a fundamental capability mismatch remains: general VLMs can reason about the overall task but often miss the visual details that determine success, while specialist vision models can capture those details but cannot translate them into task-level decisions. In this work, we propose SpatialCLI, a framework that teaches VLMs to reason with spatial tools and progressively internalize the specialist perceptual capabilities they provide. SpatialCLI proceeds in three stages: (1) Call exposes specialist vision models as spatial tools to augment the VLM's perception; (2) Learn uses Cold-Start SFT and agentic RL to improve tool use; and (3) Internalize verbalizes successful tool-use trajectories to internalize specialist perceptual capabilities. We further introduce SpatialCLI-Bench, a 516-example benchmark for compositional perception across localization, segmentation, depth, and pose. On MindCube, SpatialCLI raises Qwen3-VL-8B-Instruct from 29.3% to 84.6% with tools, surpassing GPT-5.6 Sol with tools (72.1%), while retaining 73.8% without tools after internalization.

</details>


### 54. Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness

- **Authors:** Fouad Bousetouane
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27677v1](http://arxiv.org/abs/2607.27677v1)
- **PDF:** [https://arxiv.org/pdf/2607.27677v1](https://arxiv.org/pdf/2607.27677v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are moving into production workflows where they retrieve information, call tools, maintain state, and act on behalf of users or organizations, but many release decisions still rely on capability signals, demos, or behavioral tests that do not show whether an agent is ready to operate under production constraints. Capability is therefore not production readiness. This paper introduces the ProofAgent Index (PAI), a governance readiness index for AI agents. PAI combines four dimensions of deployment evidence: Evaluation, Context, Compliance, and Governance. Evaluation measures observed behavior, Context measures the operating environment that shapes that behavior, Compliance measures alignment with applicable rules and controls, and Governance measures whether the organization can authorize, monitor, audit, and control the agent during operation. PAI is implemented inside ProofAgent Harness, an open source infrastructure for auditable AI agent evaluation and governance. Validation across two heavily regulated domains, healthcare and finance, shows that PAI carries held out readiness signal and separates higher risk from lower risk configurations. The results show that context engineering strongly changes reliability, capability improves behavior but does not determine readiness, and governance evidence must remain visible rather than averaged away. PAI reframes agent release from a faith based deployment decision into an auditable readiness decision.

</details>


### 55. HALO: Heterogeneous Admission through Localized Obligations for Safe Agentic Execution

- **Authors:** Taewoo Park, Kyeonghyun Yoo, Kiseok Kim, Seunghyun Yoo, Hwangnam Kim
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27636v1](http://arxiv.org/abs/2607.27636v1)
- **PDF:** [https://arxiv.org/pdf/2607.27636v1](https://arxiv.org/pdf/2607.27636v1)
- **Categories:** cs.AI, cs.RO, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent agentic AI systems may return a heterogeneous response containing notices, requests, handoffs, and actions. Conditions can change before external use, so components from the same response need not remain supported together. Rejecting the whole response discards useful components, whereas checking components independently can leave a dependent without its prerequisite. We present Heterogeneous Admission with Localized Obligations (HALO), a runtime protocol that preserves supported components whose declared prerequisites also remain supported, rechecks each exact action before dispatch, and allows blocked actions to be replaced only by fresh candidates. HALO matched all 96 admission expectations and passed all 20 protocol tests. In structured-response replay, it retained 248/248 supported components, including 128/128 unaffected by unrelated changes, while a whole-response policy retained 0/248. Across ten cold-start PX4/Gazebo sessions, HALO blocked every tested stale route, observed no matching stale setpoint, and completed all fresh recoveries.

</details>


### 56. What makes prompts a graph: necessary and sufficient conditions for prompt graph engineering

- **Authors:** Sandeco Macedo
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27578v1](http://arxiv.org/abs/2607.27578v1)
- **PDF:** [https://arxiv.org/pdf/2607.27578v1](https://arxiv.org/pdf/2607.27578v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prompts stopped being isolated strings some time ago. In real systems, one model call feeds another, retrieval interleaves with generation, routers branch, and aggregators merge parallel results. Practice converged on a single structure to hold this together: the graph. Frameworks such as LangGraph, DSPy, and Prompt Flow expose it openly, and research systems already optimize it automatically. The vocabulary, however, lags behind. Graph names, variously, a reasoning topology inside one sampling strategy, a multi-agent conversation, or an orchestration artifact, while prompt engineering still evokes writing one good string. What is missing is a reference definition treating prompts as nodes of an explicit, executable, improvable graph. We build that definition through conceptual analysis over sources with persistent identifiers, complemented by primary grey literature. We reconstruct the genealogy of the idea, from dataflow graphs and build systems, through prompt chaining and the thought topologies (chain, tree, graph), to graphs compiled and optimized as artifacts. We then propose a constitutive definition of prompt graph engineering, state its four conditions (explicit structure, separation between structure and prompt content, executable semantics, and the graph as a first-class engineering artifact), and operationalize them as an inclusion and exclusion test. We draw the boundary against six neighboring concepts and apply the test to six real systems (LangGraph, DSPy, Prompt Flow, AutoGen, CrewAI, and Claude Code subagents); it includes and excludes consistently. We close with a research agenda organized along four design tension axes. The contribution is an operational definition and a shared vocabulary for a practice that industry already exercises daily without naming precisely.

</details>


### 57. DeepResearch Agent System

- **Authors:** Yong Huang, Yulu Huang, for the team Collaboration
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27562v1](http://arxiv.org/abs/2607.27562v1)
- **PDF:** [https://arxiv.org/pdf/2607.27562v1](https://arxiv.org/pdf/2607.27562v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The DeepResearch Agent System is a large language model system engineered for deep information retrieval, multi-step reasoning, and autonomous research tasks. Built upon a sparse activation architecture with 30 billion total parameters of which only 3 billion are activated per token, the system achieves state-of-the-art performance on multiple agent search benchmarks while delivering 3.2 times faster inference compared to dense counterparts of equivalent scale. The system supports a 128K-token context window with hierarchical attention mechanisms that yield 18.7% accuracy and 23.4% recall improvements over standard long-context approaches. A dual-mode reasoning engine provides both a ReAct paradigm for basic multi-step problem solving and an IterResearch mode for high-performance iterative research with up to 20 reasoning steps, collectively delivering a 31.2% accuracy improvement over single-pass baselines. Multi-tool coordination integrates retrieval, computation, web search, and file parsing modules to achieve 92.1% tool-use accuracy. A reinforcement learning optimization framework based on the GRPO algorithm provides token-level policy gradients that improve training stability by 35% and accelerate convergence by 42%. An automated data synthesis pipeline with seed-based expansion achieves a 92.5% usability rate. Benchmark results include 87.3% on Humanity's Last Exam, 85.3% on BrowserComp Chinese, and 91.2% on WebWalkerQA. The system is fully open-sourced, including data synthesis, training, and inference code, and supports applications in academic research, business analysis, R&D support, and education.

</details>


### 58. Training Skills Like Parameters via Self-Supervised Semantic Diffusion

- **Authors:** Mo Li, Zixin Yin, Ting Cao, Yunxin Liu
- **Published:** 2026-07-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27557v1](http://arxiv.org/abs/2607.27557v1)
- **PDF:** [https://arxiv.org/pdf/2607.27557v1](https://arxiv.org/pdf/2607.27557v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) demonstrate remarkable general instruction-following capabilities, they often fall short of human experts in highly specialized, open-ended domains such as creative screenwriting. Prior approaches typically adopt post-training, yet both supervised fine-tuning and reinforcement learning require weight access that closed-source frontier models do not offer, and demand heavy compute. Moreover, what is learned is tied to a single checkpoint and cannot be inspected by humans. Recent advancements in agentic continual learning instead attempt to bridge this gap by accumulating external textual skills. However, these methods heavily rely on costly human expert annotations or unreliable LLM-as-a-judge feedback for reflection. To overcome this bottleneck, we propose a novel, unsupervised self-evolving agent framework inspired by the corruption-and-reconstruction paradigm of diffusion models. Instead of relying on explicit external scoring, we leverage existing high-quality human artifacts to construct self-supervised signals. Training then follows the familiar loop of neural network training, forward, loss, and backward, with the loss coming from contrasting the agent's reconstruction against the human original. What is updated is not model weights but an external library of textual skills. We evaluate our framework on the challenging task of short drama screenwriting. Experimental results demonstrate that our method enables the agent to autonomously extract and internalize highly generalizable skills, significantly enhancing its domain-specific generation capabilities. Furthermore, this self-contrastive reflection paradigm offers a scalable pathway for agents to teach themselves the production of complex, high-quality human artifacts, without requiring external supervision.

</details>


### 59. ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping

- **Authors:** Cristian Leo, Anton Dykyi, Danny Cortegaca, Daniel Begimher, Prakash Jha
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27528v1](http://arxiv.org/abs/2607.27528v1)
- **PDF:** [https://arxiv.org/pdf/2607.27528v1](https://arxiv.org/pdf/2607.27528v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Threat modeling is essential for secure software development, yet manual analysis of cloud-native architectures is slow and demands scarce security expertise. We present ThreatForest, a multi-agent system that generates structured attack trees from source code repositories, maps attack steps to adversary tactics, techniques, and procedures (TTPs) from a pluggable set of frameworks (MITRE ATT&CK, CAPEC, and cloud-specific threat matrices), and synthesizes actionable mitigations. ThreatForest decomposes threat modeling into a multi-stage agent pipeline -- repository analysis, context refinement, threat generation, parallel attack-tree construction with TTP mapping and mitigation synthesis, and report generation -- orchestrated as a directed graph with deterministic verification gates, bounded retries, and three human-in-the-loop validation points. A domain-specific sentence-transformer maps each attack step to candidate techniques by cosine similarity; we show empirically that this embedding stage, not the surrounding pipeline, is the dominant accuracy bottleneck. We evaluate ThreatForest across seven application domains on a sixteen-dimension rubric, scored by a panel of independent LLM raters with an adversarial verification pass and expert review. Panel-measured quality reaches 0.63-0.68 (on a 0-1 scale) for threat statements, attack trees, and mitigations, but only 0.29 for embedding-only TTP mapping -- a gap stable across all seven domains that isolates the binding constraint. A controlled single-call baseline on the same model more than doubles mapping defensibility, pinning the limitation on the embedding encoder rather than the multi-agent design. To our knowledge, ThreatForest is the first end-to-end system that turns a code repository into TTP-mapped attack trees with evidence-based mitigations across adversary frameworks, with a reusable framework for benchmarking such systems.

</details>


### 60. Belief Coevolution in a Social Network of Generalist and Specialist Large Language Models

- **Authors:** Germans Savcisens, Samantha Dies, Courtney Maynard, Tina Eliassi-Rad
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27512v1](http://arxiv.org/abs/2607.27512v1)
- **PDF:** [https://arxiv.org/pdf/2607.27512v1](https://arxiv.org/pdf/2607.27512v1)
- **Categories:** cs.CL, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed in multi-agent environments. However, the processes by which beliefs form and propagate among interacting LLMs remain poorly understood. We introduce CoevolveSim, a framework for studying belief diffusion within networked LLM populations. CoevolveSim allows us to isolate and study three factors: domain specialization, social-role assignment, and social network structure. Within this framework, generalist and specialist LLM agents exchange and revise beliefs. In each round, an LLM agent observes a summary of its neighbors' beliefs before updating its own. We run 1,280 controlled simulations spanning four scenarios, two network structures, and 20 medical-indication statements. We find that persona-style role assignment and network structure reshape individual belief revision but have minimal effect on population-level consensus. In contrast, introducing (finetuned) specialist LLMs more than doubles the shift in consensus and gives rise to consistent asymmetries in exerted influence. We further show that simple persistence-based opinion-dynamics models reproduce collective outcomes in all-generalist LLM populations, whereas heterogeneous LLM populations require population-level belief composition to reproduce consensus and agent identity to predict individual belief transitions. Our results indicate that realistic simulation of belief diffusion in multi-agent LLM systems requires a diverse set of underlying LLMs, not persona prompting alone.

</details>


### 61. Skill Use or Skill Theater? Evaluating the Reasoning Backroom in Skill-Augmented Language Agents

- **Authors:** Jinwei Hu, Yi Qi, Xinmiao Huang, Youcheng Sun, Yi Dong, Xiaowei Huang
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27484v1](http://arxiv.org/abs/2607.27484v1)
- **PDF:** [https://arxiv.org/pdf/2607.27484v1](https://arxiv.org/pdf/2607.27484v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reusable skills are becoming a standard interface for extending language agents with task procedures. Yet evaluators usually infer skill use from visible reasoning or the agent's own attribution. These signals show what the agent appears to use, not whether the skill changed its decision. We ask whether skill-augmented agents exhibit a \textbf{Reasoning Backroom}, a systematic gap between stated skill use and intervention-measured influence. We introduce BACKTRACE, an evaluation framework that pairs each skill-conditioned answer with a matched no-skill counterfactual, intervenes on skill meaning, wording, identity, content, and assignment, and elicits attribution only after the answer is committed. We instantiate the framework as BACKROOMBench, a verified testbed spanning controlled logic and competition mathematics, multiple skill conditions, single-agent and multi-agent settings, and diverse model families. Our evaluation reveals a pervasive provenance failure. Across models and domains, stated skill use often remains stable while causal reliance and signed utility vary, producing both silent uptake and performative use. Behavioral effects follow procedural content more reliably than displayed skill identity, whereas stated attributions respond strongly to artifact availability. Observational detectors based on direct skill-use claims, text mentions, trace similarity, and an LLM judge do not identify which decisions actually depend on the skill. In multi-agent systems, skill influence can survive communication even after its source is lost, while no-skill teams still name skills and sources that were never supplied. These findings establish the Reasoning Backroom as a general AI provenance problem whose audit requires intervention.

</details>


### 62. Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems

- **Authors:** Xu Zheng, Zhuomin Chen, Chaohao Lin, Hua Wei, Haifeng Chen, Wei Cheng, Dongsheng Luo
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27443v1](http://arxiv.org/abs/2607.27443v1)
- **PDF:** [https://arxiv.org/pdf/2607.27443v1](https://arxiv.org/pdf/2607.27443v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model~(LLM)-based agents have demonstrated exceptional performance across a wide range of complex interactive tasks. However, they often struggle with long-horizon interactive tasks common in domains, such as embodied AI. The complexity and vast action spaces in these settings lead to compounding errors, where a single suboptimal action can derail an entire trajectory, causing the agent to exhaust its limited step budget on inefficient or unrecoverable paths. To overcome this without costly fine-tuning, we draw inspiration from software debugging, where execution logs are analyzed to preemptively catch errors. We propose \textit{Trajectory Graph Copilot}, a novel framework that acts as a ``copilot'' for LLM agents by diagnosing potential action errors before they are executed. At its core,\textit{Graph Debugger} models historical trajectories as a probabilistic graph and uses a Graph Neural Network to identify sequential action patterns that frequently lead to failure. Functioning as a proactive diagnostic sandbox, our method provides early warnings on potentially flawed actions, prompting the agent to self-correct. This pre-action error diagnosis prevents costly mistakes, significantly enhancing the agent's ability to complete long-horizon tasks successfully. The extensive experiments on four benchmarks with three LLM agents demonstrate a $14.69\%$ pass ratio improvement on average.

</details>


### 63. Auditing Emergent LLM-Agent Collaboration through Cooperation-Obligation Coupling

- **Authors:** Zuyuan Zhang, Hanqing Yang, Carlee Joe-Wong, Tian Lan
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27429v1](http://arxiv.org/abs/2607.27429v1)
- **PDF:** [https://arxiv.org/pdf/2607.27429v1](https://arxiv.org/pdf/2607.27429v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-agent systems can solve complex tasks through dynamic self-organization and emergent cooperation. Auditing this process is essential because plausible intermediate or final outputs can conceal incomplete or unsupported work and poorly allocated responsibility, ultimately compromising response quality. While existing approaches may record messages, tool calls, provenance, or task dependencies, an auditability gap exists as they do not jointly represent what work remains, who is responsible for it, and what evidence justifies each work-state transition. We address this auditability gap by proposing \emph{Integrated Cooperation-Obligation REpresentation} (iCORE). It creates a unified encoding $X=(G,Q,Π)$ integrating observable interactions as a cooperation graph $G$, evolving work and assignments as an obligation graph $Q$, and the audit map $Π$ linking them with verifiable properties and evidence. This iCORE representation enables the auditor to certify two complementary properties: {Work soundness}, where every active decision-relevant work assertion must have a finite justification through $G$ and $Π$; and {Agent-assignment stability}, which requires that no feasible alternative agent improve the declared contribution value for an evaluated obligation by more than $ε$. We establish local-to-global soundness and assignment-regret guarantees and a performance bound under stated conditions. iCORE is an instrumentation layer over workflows. Numerical results show that the full coupled state exactly reconstructs soundness and assignment defects in two execution modes and that, relative to passive full-state observation, iCORE-Audit yields absolute trajectory-quality improvements of $11.5\%$ and $26.4\%$ in controlled and real-LLM execution, respectively, with corresponding absolute terminal-performance improvements of $15.1\%$ and $31.0\%$.

</details>


### 64. SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis

- **Authors:** Xiaoyi Bao, Yuanzhen Xie, Yunzhi Tan, Jinghang Gu, Zhongqing Wang, Chu-Ren Huang, Bo Hu, Zang Li
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27360v1](http://arxiv.org/abs/2607.27360v1)
- **PDF:** [https://arxiv.org/pdf/2607.27360v1](https://arxiv.org/pdf/2607.27360v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent self-evolution has primarily focused on learning how to act, while overlooking an equally important capability: learning to discover what an agent does not know. Existing approaches typically assume that failure discovery is given, focusing on how to repair failures once they are identified. We ask whether blind-spot diagnosis itself can be learned. We thus study diagnosis as an agent capability separate from execution, and exclude two alternative sources of progress: executor adaptation and human supervision. Under these constraints, performance cannot improve through executor updates or annotated examples, forcing all improvements to originate from the learned diagnostic capability. We propose SkillMentor, which trains a Mentor policy via reinforcement learning to generate diagnostic tasks, identify recurrent failure modes, and curate them into reusable corrective skills. Across AppWorld and BFCLv3, SkillMentor improves executor performance by an average of 44.2%. These results suggest that blind-spot diagnosis is a learnable capability, enabling self-evolution without updating executor weights or relying on human-curated data.

</details>


### 65. Can AI agents conduct open-ended AI research? Early evidence from two case studies

- **Authors:** Peter Kirgis, Sayash Kapoor, Andrew Schwartz, Stephan Rabanser, David Africa, Konstantinos Voudouris, Viet Nguyen, Toby Pilditch, Magda Dubois, Harry Coppock, Cozmin Ududec, Nitya Nadgir, Matilda Orona, Tilman Bayer, Derrick Chan-Sew, Yue Ling, Abhishek Shetty, Helen Toner, Gillian Hadfield, Seth Lazar, Steve Newman, Shoshannah Tekofsky, Rishi Bommasani, Arvind Narayanan
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27191v1](http://arxiv.org/abs/2607.27191v1)
- **PDF:** [https://arxiv.org/pdf/2607.27191v1](https://arxiv.org/pdf/2607.27191v1)
- **Categories:** cs.AI, cs.CY, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a third way to measure progress towards AI R\&D automation. An agent takes on the central, open-ended research question of a high-quality unpublished paper, and the paper's original authors grade its output. We call these shadow evaluations. We ran shadow evaluations on two unpublished NeurIPS 2026 submissions, giving frontier agents six days and thousands of dollars of compute. The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors. We identify five recurring failure modes: poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift. A robustness check with a second model and scaffold reproduced these failures. We release the expert reviews, survey responses, agent repositories, and logs. Our results provide early evidence that today's agents can do the engineering of AI research, but struggle with critical parts of the research lifecycle.

</details>


### 66. Partner Capability Estimation for Task-Agnostic Adaptation in Ad-Hoc Teamwork

- **Authors:** Peter Tisnikar, Maja Swieczkowska, Benteng Ma, Gerard Canal, Matteo Leonetti
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27177v1](http://arxiv.org/abs/2607.27177v1)
- **PDF:** [https://arxiv.org/pdf/2607.27177v1](https://arxiv.org/pdf/2607.27177v1)
- **Categories:** cs.AI, cs.HC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective collaboration with novel and diverse partners is a crucial skill for autonomous agents. Most current ad-hoc teamwork (AHT) approaches assume that agents will collaborate on a single, fixed task and that the partner's capabilities, their ability to successfully execute the desired action, are already known. In reality, a partner's true capabilities are often hidden, and human collaborators may act sub-optimally on tasks with multiple valid strategies. To address these limitations, we extend ad-hoc teamwork into a multi-task setting by re-framing it as a problem of joint planning with decentralised execution under hidden partner capabilities. We introduce CE-CM (Capability Estimation via Contextual Models), an approximate Bayesian method that infers task-invariant capability vectors. By using simulation-based sampling, the agent estimates capabilities and induces a contextual Multi-agent Markov Decision Processes for planning. This approach requires no population pre-training and refines its beliefs online from just a few tasks. To account for human unpredictability, we propose CE-CM-Div, an extension that evaluates capability hypotheses against diverse planner rollouts rather than a single optimal trajectory. Simulated experiments demonstrate that CE-CM rapidly recovers hidden capabilities, reduces infeasible action assignments, and adapts to changes over time. Furthermore, in an offline human study of 225 trajectories from 15 participants, CE-CM-Div substantially improved capability estimates over the baseline CE-CM method. Our results suggest capability-based modelling is a promising interpretable, task-agnostic representation in the studied settings, demonstrating that accounting for behavioural diversity is essential for robust human-AI teaming.

</details>


### 67. OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding

- **Authors:** Jingbo Zhou, Yusai Zhao, Qi Bao, Jingjia Cao, Zhenghai Chen, Chang Gao, Kaiqi Guo, Muxin Guo, Mingxuan Li, Xinjiang Lu, Yanru Ma, Yixiong Xiao, Zenghui Zhang, Le Zhang, Hua Wu
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27155v1](http://arxiv.org/abs/2607.27155v1)
- **PDF:** [https://arxiv.org/pdf/2607.27155v1](https://arxiv.org/pdf/2607.27155v1)
- **Categories:** cs.AI, cs.CL, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly expected to assist users in completing tasks. However, existing benchmarks provide limited support for evaluating whether agents can carry out office-suite workflows at a reasonable cost. We introduce OmegaUse-OfficeVal, a benchmark for evaluating LLM agents on long-horizon office-suite tasks with task-level economic grounding. The benchmark comprises 100 tasks derived from office-suite requests proposed by practitioners and adapted through a privacy-preserving process. On average, these tasks require 2.32 hours of human labor to complete. An important feature of the benchmark is that each task is paired with two economic signals: human labor time and task price proxy. These signals enable direct comparisons between human costs and LLM inference costs, as well as value-weighted evaluation. To support stable evaluation, we develop code-based verifiers from fine-grained rubrics. We evaluate several frontier LLMs together with a human baseline. Although all evaluated LLMs are substantially cheaper and faster than human workers, they have not yet approached human-level deliverable quality. The code and dataset are fully open-sourced, and more information is available on our project website: https://omegause-officeval.github.io.

</details>


### 68. AgentMap: Joint Equivalence and Subsumption Discovery for Ontology Matching

- **Authors:** Yiping Song, Jiaoyan Chen, Renate Schmidt, Hui Yang, Wen Zhang
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27130v1](http://arxiv.org/abs/2607.27130v1)
- **PDF:** [https://arxiv.org/pdf/2607.27130v1](https://arxiv.org/pdf/2607.27130v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Ontology matching (OM) has traditionally been formulated as either equivalence discovery or subsumption matching. The existing OM systems identify only one type of semantic correspondence and cannot simultaneously discover equivalence and subsumption mappings. In this paper, we introduce Hybrid Ontology Matching (HOM), a new OM task that unifies equivalence and subsumption discovery, and accordingly propose a Large Language Model (LLM)-based multi-agent OM framework AgentMap that is implemented by a series of interdependent semantic decisions. Given a concept in the source ontology, AgentMap integrates semantic retrieval, hierarchical search, and collaborative multi-agent LLM reasoning to progressively explore the target ontology, identifying either the equivalent concept, if one exists, or the most fine-grained subsumer. We further extend four OM datasets for a HOM benchmark and evaluate AgentMap under hybrid, equivalence-only, and subsumption-only settings. Experimental results show that AgentMap achieves promising performance on the hybrid setting, and at the same time outperforms equivalence matching and subsumption matching baselines on the equivalence-only and subsumption-only settings, respectively.

</details>


### 69. Multi-Agent Planning with Spatio-Temporal and Topological Constraints using STL-GO

- **Authors:** Sheryl Paul, Vidisha Kudalkar, Anand Balakrishnan, Lars Lindemann, Alberto Speranzon, Jyotirmoy V. Deshmukh
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28679v1](http://arxiv.org/abs/2607.28679v1)
- **PDF:** [https://arxiv.org/pdf/2607.28679v1](https://arxiv.org/pdf/2607.28679v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent planning problems arise in a variety of engineering applications, such as multi-robot wildfire fighting and unmanned aerial inspection in factories. A particular challenge is the existence of spatio-temporal (i.e., when and/or where an agent should do what) and topological constraints (i.e., how agents should interact), as typically formalized via the notion of graphs. Over the last years, various frameworks have been proposed that can capture such constraints via spatio-temporal logics. We focus here on spatio-temporal logic with graph operators (STL-GO), a recent formalism that supports reasoning about multiple agents and their topologies, such as sensing, communication, and task topologies. In this paper, we consider the problem of planning multi-agent paths that satisfy constraints written in STL-GO. This problem is particularly challenging due to the need of encoding multiple, potentially time-varying graphs via the graph operators inherent to STL-GO. We present two encodings of this problem, one based on mixed-integer programming (MIP) and another based on satisfiability modulo theory (SMT), with soundness guarantees. We provide a unified interface for specifying agent constraints, their graph topologies, and the STL-GO specification, enabling seamless use of both methods and facilitating direct comparison between them. We evaluate both encodings on a multi-UAV search-and-rescue benchmark, ablating over team size and graph complexity, highlighting the expressiveness of the proposed encodings under dynamic multi- graph interactions.

</details>


### 70. Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents

- **Authors:** Yicheng Feng, Yan Zhang, Yan Cheng, Wei Qi
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27083v1](http://arxiv.org/abs/2607.27083v1)
- **PDF:** [https://arxiv.org/pdf/2607.27083v1](https://arxiv.org/pdf/2607.27083v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents increasingly depend on diverse external services such as search engines, databases, and connectors, agent harnesses face a fundamental tool-selection challenge: acquiring too few tools leaves the task under-informed, while too many adds cost, context load, and privacy exposure. Routers and retrievers can rank candidate tools by relevance, but a ranking alone does not determine how many are worth selecting. Existing approaches leave acquisition under heterogeneous costs unaddressed. We formulate this decision as cost-aware marginal decision-focused stopping (CAM-DF) over ranked tool prefixes, with CAM-DF-lite as a compact interpretable variant. We train directly on the offline gap between stopping now and the best continuation: its sign labels the decision, its magnitude weights each error by the payoff at stake. We prove this objective is Bayes-aligned with the stopping target and that score-only rules are suboptimal under heterogeneous costs. We evaluate on 1,343 tasks across five tool-use domains. On $τ$-bench Retail, CAM-DF attains the highest payoff among deployable methods, with gains over a predict-then-threshold baseline across all five ranking sources and two cost regimes. Our approach is state-of-the-art under heterogeneous costs and high cost pressure, with larger gains under weaker rankings. In live execution, CAM-DF exposes the agent to 37\% fewer tools than full access while maintaining comparable task success. The CAM-DF family is a lightweight pre-execution plugin that turns existing tool rankings into lower-cost acquisition decisions without fine-tuning the underlying LLM.

</details>


### 71. TREK: A Travel Reasoning and Evaluation Kit for LLM Agents in Complex Trip Planning

- **Authors:** Jinhu Qi, Wentao Zhang, Siu Man Ng, Feiyang Xu, Yanyu Chen, Yaoman Li, Irwin King
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26977v1](http://arxiv.org/abs/2607.26977v1)
- **PDF:** [https://arxiv.org/pdf/2607.26977v1](https://arxiv.org/pdf/2607.26977v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Travel planning is a demanding stress test for tool-using LLM agents: a usable itinerary is a single artifact that must be right along many axes at once - every flight, hotel, and attraction must exist and be bookable, the days must be physically traversable, the total must clear a budget, and the plan must serve a traveler whose needs are only partly stated. Existing agent benchmarks reward these properties one at a time and grade the final output with soft or LLM-judged rubrics, which cannot certify that a returned plan is executable and are neither reproducible nor auditable. We introduce TREK (Travel Reasoning and Evaluation Kit), a benchmark for feasible itinerary synthesis: producing a single plan that is jointly constraint-correct, hallucination-free, spatio-temporally executable, budget-valid, and responsive to the traveler's unstated persona needs. TREK comprises 800 multi-constraint tasks - 533 feasible and 267 provably infeasible with typed route/entity/budget causes - over a synthetic, internally consistent knowledge base of 212,530 records across 375 cities and 13 personas, served through a production-style tool sandbox of validated RESTful APIs. Every task is scored by a fully deterministic, rule-based evaluator with no LLM judge and ships a human-verified gold reference that scores a perfect 1.0 under that same evaluator, so the ceiling is demonstrably achievable and every remaining gap is an agent limitation rather than scorer strictness. Evaluating 15 LLM agents across nine constraint dimensions, we find that even the strongest (GPT-5.6) produces a fully-feasible plan on only 46.2% of solvable tasks, with a median of 6.6% and a floor of 0.0%; satisfying travelers' unstated needs emerges as the universal bottleneck, unsolved even at the frontier. We release the dataset, tool sandbox, deterministic evaluator, and agent code as a fully reproducible benchmark.

</details>


### 72. What Does It Take to Detect an AI Agent? Minimal Feature Sets for Behavioral Detection under Browser Automation

- **Authors:** Vishisht Choudhary, Lukas Schmidt, Anne Zoë Kenntner, Feras Skhab, Michel Osswald, Jens Ernstberger
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26935v1](http://arxiv.org/abs/2607.26935v1)
- **PDF:** [https://arxiv.org/pdf/2607.26935v1](https://arxiv.org/pdf/2607.26935v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Bot detectors deployed at scale treat traffic as binary: human or bot. This assumption breaks when AI agents browse the web through browser automation, a traffic class that is neither and that binary classifiers structurally cannot represent. We present a three-class detection framework distinguishing humans, bots, and AI agents, and show that the binary-vs-agent confusion is architectural: a binary human-vs-bot detector misroutes agent sessions because its label space lacks an agent class. On our controlled benchmark, an MLP binary classifier misclassifies 39.1% of real AI agents as human and a SAINT binary transformer misclassifies 34.5%; adding an explicit agent class yields per-class agent F1 = 1.000 in all 30 runs (3 model families $\times$ 10 seeds). To measure evasion resistance, we construct a five-level evasion ladder spanning passive observation, GAN-generated trajectories, and replay of real human cursor data ($n = 2299$ evasion sessions). Across 10 seeds and 3 model families we observe zero agent misses in 22990 per-seed predictions. The discriminative signal is a browser-automation artifact, not evidence of agent reasoning: Playwright does not emit the raw pointer-move and wheel-delta streams a physical input device produces, and this absence signature survives trajectory manipulation. Exhaustive search over all feature subsets of size 1-5 (9401 GBMs) shows that two behavioral features (mouse_event_rate, teleport_click_ratio) give 100% observed agent recall at every evasion level with agent precision 0.994; five features lift macro-F1 to 0.991. The signal is redundantly encoded: removing teleport_click_ratio leaves agent detection at 100%. The single-feature regime is degenerate, flagging every agent only by collapsing the classifier to always predict "agent". Two features robustly isolate agents; five separate all three traffic classes at macro-F1 $\geq 0.99$.

</details>


### 73. Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models

- **Authors:** Ashish Prajapati, Om Mohite
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26922v1](http://arxiv.org/abs/2607.26922v1)
- **PDF:** [https://arxiv.org/pdf/2607.26922v1](https://arxiv.org/pdf/2607.26922v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM pipeline systems break down the task among multiple roles for better reasoning, but are benchmarked mainly with large-scale commercial models. In this study, we investigate Parishad, a structured multi-agent system involving five roles, by deploying it on Qwen2.5-7B-Instruct, a local model, on two datasets: GSM8K (500 questions) and HumanEval (164 questions), compared with prompting directly and two-call self-refinement. The multi-agent system drops GSM8K accuracy from 75.0\% to 45.0\% with JSON data format due to the error accumulation problem. With plaintext format, the accuracy is restored to 82.0\%. A two-call self-refinement strategy (V1) can achieve 86.2\% accuracy on GSM8K, with 7.4$\times$ lower token usage. However, the same V1 implementation on HumanEval---where direct accuracy is already 96.3\%---actively destroys performance (66.5\%). A task-aware gated redesign (V2) applied to HumanEval preserves accuracy at 95.1\%. Our results demonstrate that communication format and implementation details determine outcomes more than architectural complexity, and that simpler approaches match or outperform multi-agent pipelines for local 7B model deployment. All code and data are released.

</details>


### 74. Think Short, Defer Smart, Act, and Repeat: Calibrated Reasoning and Uncertainty-Aware Deferral for Edge LLM Agents

- **Authors:** Amirmohammad Farzaneh, Osvaldo Simeone
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26865v1](http://arxiv.org/abs/2607.26865v1)
- **PDF:** [https://arxiv.org/pdf/2607.26865v1](https://arxiv.org/pdf/2607.26865v1)
- **Categories:** stat.ML, cs.AI, cs.IT, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents following the ReAct paradigm are promising enablers of complex multi-step tasks, including multi-hop question answering, code generation, and control of physical AI systems. Yet, when deployed at the edge, they must tightly manage their reasoning budget while remaining reliable and deferring to a cloud-side model only when local uncertainty is too high to act safely. We propose Think Short, Defer Smart (TSDS), a framework that synergistically integrates a lightweight convergence probe, which halts on-device reasoning once the intended action has stabilized, with a perplexity-based deferral rule that escalates uncertain actions to a cloud-side model. Both mechanisms are jointly calibrated on end-to-end episode trajectories via a multi-objective Learn-Then-Test (LTT) procedure, providing simultaneous finite-sample guarantees on expected episode reward and cloud-call rate. We evaluate TSDS on four ReAct benchmarks spanning arithmetic reasoning (GSM8K), multi-hop question answering (HotpotQA), code generation (MBPP), and multi-step embodied planning (household robot), and compare against thought-calibration-only and calibrated-deferral-only standalone baselines. TSDS reduces per-episode thinking compute by 43%-73% over deferral-only baselines across HotpotQA, MBPP, and the household robot task, while maintaining certified reward and cloud-call rate guarantees.

</details>


### 75. Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents

- **Authors:** Jiwon Jang, Kisu Yang, Heuiseok Lim, Hyunwoo Park
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.27275v1](http://arxiv.org/abs/2607.27275v1)
- **PDF:** [https://arxiv.org/pdf/2607.27275v1](https://arxiv.org/pdf/2607.27275v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Post-training quantization to 4-bit weights is widely reported to be nearly lossless. We test this claim for multi-turn, tool-calling agents, where it now matters most. On $τ^2$-bench, across two open-weight model families in dense and MoE variants and two domains (eight cells, 456 episodes each, at 16-, 8-, and 4-bit weights), quantization indeed looks free on the standard metric. No cell shows a score change that survives multiple-comparison correction, and in the cell that carries the largest process damage, equivalence testing bounds the change within $\pm$7.5 points. The process tells a different story. Quantization amplifies the failure the model already exhibits at full precision (tool-name hallucination in telecom, with the same directional trend in retail entity errors) by up to 2.5$\times$ in volume (+17.6 points per task), while creating essentially no new failures. The failure set is the same at every precision (rank correlation $\geq$ 0.94, 0.18% novel events). The score stays flat because the benchmark's ten-error budget absorbs the extra failures. Shrinking the budget to two errors re-exposes a score gap of 17 points, and it does so only in the one cell where quantization added error volume, exactly as the masking account predicts. A targeted error-repair prompt, run for five telecom models at every precision, removes the damage exactly and only where it lives. Both diagnostics, the per-channel error rate and success under a shrinking budget, come from logs benchmarks already collect; we suggest reporting them alongside task reward.

</details>


### 76. Forecasting Trajectory-Level Safety Risks in Black-Box Multi-Turn Interactions

- **Authors:** Shi Lin, Peng Qian, Dinghao Liu, Renjie Sun, Sifan Wu, Dezhang Kong, Chenpei Wang, Xun Wang
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26820v1](http://arxiv.org/abs/2607.26820v1)
- **PDF:** [https://arxiv.org/pdf/2607.26820v1](https://arxiv.org/pdf/2607.26820v1)
- **Categories:** cs.LG, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models (LLMs) evolve from standalone assistants into autonomous agents, ensuring their safety requires shifting beyond pointwise risk assessment to understand how risks emerge and unfold over long-horizon trajectories. In multi-turn interactions, malicious intent can be decomposed across seemingly harmless turns and gradually reconstructed through interaction trajectories, eventually resulting in safety failures. Existing safeguards remain largely reactive, detecting manifested violations while lacking the ability to predict latent risk evolution and enable preemptive prevention. To address this limitation, we propose Recast, a safety risk forecasting framework that advances LLM safeguarding beyond turn-level violation detection to trajectory-level risk prediction. Recast first retrieves risk-relevant evidence from both short-term dialogue progression and long-term historical context via a dual-scale trajectory view. It then models compositional risk evolution by capturing the current risk configuration and its temporal dynamics. Finally, a causal temporal encoder learns latent risk evolution patterns and predicts the distribution of future risk emergence turns. Extensive experiments across 7 risk categories show that Recast predicts 88.3% of future safety failures with an average lead time of 2.41 turns, while maintaining a false alarm rate of 12.3%, showcasing the effectiveness of trajectory-level forecasting in identifying emerging risks before safety violations occur.

</details>


### 77. SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response

- **Authors:** Lehan Wang, Boli Chen, Ruixue Ding, Pengjun Xie, Jinwei Huang, Zhendong Liu, Shuo Wang, Tao Lei, Xin Ouyang, Xiaomeng Li
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26791v1](http://arxiv.org/abs/2607.26791v1)
- **PDF:** [https://arxiv.org/pdf/2607.26791v1](https://arxiv.org/pdf/2607.26791v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly adopted in real-world security operations with access to host artifacts and command-line interfaces (CLIs), making it critical to thoroughly assess their security capabilities. However, existing cybersecurity benchmarks focus on pre-compromise settings where agents are placed in a clean and idealized environment before an attack occurs. This leaves the post-compromise setting underexplored. To address this gap, we introduce SecRespond, the first benchmark for evaluating LLM agents on the post-compromise incident-response workflow. Given a forensic disk snapshot of a compromised host together with the alerts, vulnerability scans, and baseline checks reported by a host security product, agents are required to produce forensic reports on intrusions, baseline risks, and vulnerability risks, together with a remediation plan. We instantiate this task across 10 cyber ranges, each constructed from a distinct compromised cloud host, spanning 4 entry-point types, 21 ATT&CK techniques, and 5 operating systems. We evaluate 23 frontier LLMs on the OpenCode agent harness. Experimental results show that although current agents can reliably uncover the problems exposed by alerts, they struggle to proactively investigate the disk for silent intrusions and to produce comprehensive, verified remediation plans, with no model achieving complete detection and remediation on any single range. This reveals a fundamental bottleneck in building agents for real-world incident response. The benchmark is publicly available at https://github.com/Alibaba-NLP/qqr/tree/main/data/secrespond.

</details>


### 78. SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution

- **Authors:** Zhiyuan Yao, Yuxin Chen, Zhengxi Lu, Zishan Xu, Yueqing Sun, Yifu Guo, Yuquan Lu, Zhengzhou Cai, Kangning Zhang, Zhuowen Han, Zi-Han Wang, Ziang Ye, Qi Gu, Xunliang Cai, Weiwen Liu, Yongliang Shen
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26784v1](http://arxiv.org/abs/2607.26784v1)
- **PDF:** [https://arxiv.org/pdf/2607.26784v1](https://arxiv.org/pdf/2607.26784v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents often encounter related yet distinct tasks that share reusable solution patterns. Yet standard agentic reinforcement learning treats tasks as independent episodes, while existing approaches to skill learning either focus on repeated attempts of one task or use pipelines with multiple stages that entangle extraction, retrieval, and execution. We introduce SkillRise, a unified reinforcement learning framework for learning skills across tasks. SkillRise organizes related instances into progressively challenging sequences and uses a single policy to alternate between task solving and curating an evolving skill document passed directly to the next task. Decoupled credit assignment across tasks supervises solving with the current task outcome and curation with discounted downstream outcomes. Experiments on ALFWorld, WebShop, and ScienceWorld show that SkillRise achieves the strongest Pass@1 performance among the compared methods, with gains over the strongest baseline ranging from 2.3 to 8.5 percentage points. Although trained across distinct tasks, its learned curation policy remains effective for repeated attempts on the same task. Further analysis reveals scaling at test time across tasks: performance improves with longer sequences of related tasks even when each task is attempted only once. This trend suggests that SkillRise reuses transferable skills across tasks rather than benefiting from repeated sampling of the same task. SkillRise further retains strong performance while substantially reducing the runtime overhead of skill learning pipelines with multiple stages. Together, these results provide a simple and efficient training paradigm for LLM agents to extract, refine, and reuse transferable skills across tasks.

</details>


### 79. Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM

- **Authors:** Huixiang Zhang, Mahzabeen Emu
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26773v1](http://arxiv.org/abs/2607.26773v1)
- **PDF:** [https://arxiv.org/pdf/2607.26773v1](https://arxiv.org/pdf/2607.26773v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Latent communication in large language model (LLM)-based multi-agent systems (MAS) transmits continuous internal representations instead of text, but greater representational capacity does not establish that the receiver uses task-relevant information. End-task performance alone also cannot reveal whether an observed effect depends on message presence, content generated for the evaluated example, or information supplied by a separate agent. We introduce a causal audit that applies controlled message replacements at the boundary where the sender-produced representation enters the receiver. Four message settings support five measurements of encoded sender information, receiver sensitivity to message presence and identity, the task value of example-specific content, and the additional value supplied by a separate agent. We apply the audit to latent relay with Qwen3-4B and Qwen3-8B on GSM8K, ARC-C, and MATH-500. On GSM8K, the Qwen3-4B overall performance effect of -1.00 percentage point decomposes into a -6.17-point effect retained by an other-example message and a +5.17-point effect attributable to example-specific content; both component directions reverse at 8B. On MATH-500, the Qwen3-4B gain of 15.00 points comprises 8.33 points retained by an other-example message and 6.67 points attributable to example-specific content, while the 8B gain is dominated by the former component. Self-substitution comparisons further show that example-specific content and other-agent value are distinct. These results show that aggregate accuracy does not identify how a latent message affects the receiver and motivate controlled message comparisons as a standard evaluation for latent communication.

</details>


### 80. Metis: Memory Foundation Model

- **Authors:** Zeyu Zhang, Ziliang Guo, Yihang Sun, Xichong Zhang, Xixuan Hao, Zehao Lin, Yang Zhang, Xiaoyan Zhao, Tong Shen, Bo Tang, Zhi-Qin John Xu, Junchi Yan, Haofen Wang, Xu Chen, Feiyu Xiong, Zhiyu Li, Tat-Seng Chua
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26760v1](http://arxiv.org/abs/2607.26760v1)
- **PDF:** [https://arxiv.org/pdf/2607.26760v1](https://arxiv.org/pdf/2607.26760v1)
- **Categories:** cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in AI agents have increasingly internalized native capabilities into their underlying foundation models, giving rise to multimodal foundation models and large reasoning models. However, agent memory is still primarily implemented through external modules, leaving the native memory capability largely unexplored. In this paper, we take a first step toward this direction by introducing memory foundation models, which empower foundation models with native memory capabilities. We formalize native memory from two perspectives: a persistent and dynamically evolving memory state within the backbone, and native memory procedures that autonomously store and utilize information through model computation. We show that native memory offers advantages in architecture, end-to-end optimization, and efficiency. Based on this formulation, we propose Metis, the first prototype of memory foundation models. Metis introduces a new architecture that equips a foundation model with a native memory state, allowing historical information to be compressed into the model and accessed through memory attention. We construct large-scale memory-specific training data and introduce multiple optimization objectives to acquire these native memory procedures through mid-training. The online memory maintenance of Metis is gradient-free, and the memory update requires only a forward pass. At inference time, all learned model weights remain frozen, while the native memory states are autonomously transformed through standard forward computation. Through extensive experiments, we show that Metis exhibits native memory capabilities and further provide a detailed analysis of its strengths, limitations, and behaviors. To facilitate future research on memory foundation models, we release our project and model checkpoints.

</details>


### 81. ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding

- **Authors:** Xinkui Zhao, Enbo Chen, Yifan Zhang, Chang Liu, Guanjie Cheng, Naibo Wang, Yueshen Xu
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.28678v1](http://arxiv.org/abs/2607.28678v1)
- **PDF:** [https://arxiv.org/pdf/2607.28678v1](https://arxiv.org/pdf/2607.28678v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning. However, existing agentic memory approaches often discard fine-grained dentity cues under aggressive compression and segment-wise processing. They also rely heavily on vector similarity retrieval, which can surface semantically related yet identity-mismatched evidence, leading to entity confusion, error propagation, and hallucinated answers.
  We propose ViSAGE, a multimodal agentic memory framework that constructs self-correcting, entity-centric memories. Specifically, ViSAGE anchors entity identity via cross-modal binding over long temporal ranges. It then applies bidirectional memory refinement to propagate delayed identity evidence, retroactively unifying historical records and improving future reasoning. We also introduce multi-agent cross-verification to assess retrieved evidence under an identity-evidence alignment onstraint, enabling abstention instead of unsupported answers when evidence is missing. Extensive results demonstrate that ViSAGE consistently outperforms the strongest baseline, achieving 5.9% higher accuracy.

</details>


### 82. UrbanDS: A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks

- **Authors:** Zhilun Zhou, Jianghao Yu, Yuming Lin, yongjun yang, Sun Yongquan, Depeng Jin, Yong Li
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26724v1](http://arxiv.org/abs/2607.26724v1)
- **PDF:** [https://arxiv.org/pdf/2607.26724v1](https://arxiv.org/pdf/2607.26724v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents have been widely applied in automating data science tasks. However, existing methods typically rely on a limited set of provided datasets, and they face challenges in data-intensive scenarios that require discovering and leveraging relevant information from large-scale and heterogeneous data repositories. Urban tasks are representative examples of such scenarios, as urban data are not only large-scale and multi-sourced, but also exhibit complex spatial, temporal, and semantic relationships. To address these challenges, we propose UrbanDS, a graph-guided LLM multi-agent system for data-intensive urban tasks. We first construct a unified dataset graph to organize reusable dataset skills and the relationships among datasets. Specifically, we develop a Data Profiling Agent that constructs a skill for each dataset. Moreover, a Relation Agent identifies relationships among datasets and integrates these relationships into the dataset graph. At runtime, a Planner Agent retrieves task-relevant datasets from the graph and generates execution plans. Multiple Execution Agents then perform data processing and analysis, while their execution progress and intermediate results are shared through a common memory. Finally, a Report Agent synthesizes the experimental logs into a report, which can be further refined based on user feedback. To systematically evaluate the capability of agents in handling data-intensive urban scenarios, we further construct UrbanDS-Bench, an urban data science benchmark covering representative data analysis and modeling tasks. Experiments on both general and urban benchmarks demonstrate that UrbanDS consistently outperforms existing data science agents on data-intensive tasks. Furthermore, UrbanDS has been deployed on the urban operations platform of Dongxihu District, Wuhan, demonstrating its effectiveness in real-world urban applications.

</details>


### 83. PowerAtlas: Towards Electricity-Computing Co-Scheduling for Power Systems

- **Authors:** Kaiwen Jiang, Siya Xu, Ziyue Zhu, Chao Yang, Anh Tuan Luu, Haoran Luo
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26710v1](http://arxiv.org/abs/2607.26710v1)
- **PDF:** [https://arxiv.org/pdf/2607.26710v1](https://arxiv.org/pdf/2607.26710v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid growth of AI workloads is turning data centers into large-scale, volatile, yet spatiotemporally flexible grid loads, creating an urgent need for coordinated electricity-computing scheduling. Under stringent grid constraints, schedules from general-purpose large language models (LLMs) are often infeasible, causing line-flow violations and unserved load. We present PowerAtlas, an LLM-agent framework for electricity-computing co-scheduling that integrates historical instances, domain knowledge, and physical constraints to produce joint decisions satisfying both grid operational rules and the service-level agreements (SLAs) of computing tasks. Working with a provincial power utility in China, we built an experimental electricity-computing network and validated the decision loop on real data-center data; from de-identified operational data we further constructed ECBench, a benchmark of 2,000 scheduling instances with oracle-optimal solutions. Experiments across eleven LLMs demonstrate the effectiveness of PowerAtlas under realistic physical operating conditions, with consistent feasibility and cost gains across three open-weight backbones. Our code is publicly available at https://github.com/JAVA-Jiang/PowerAtlas.

</details>


### 84. Graph Is the Verifier: Agentic Reinforcement Learning for Interprocedural Vulnerability Detection

- **Authors:** Yikun Li, Ting Zhang, Jiakun Liu, Jinfeng Jiang, Yuheng Yieh, Yixin Yang, Wen Bin Leow, Yide Yin, Yintong Huo, Eng Lieh Ouh, Lwin Khin Shar, David Lo
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26656v1](http://arxiv.org/abs/2607.26656v1)
- **PDF:** [https://arxiv.org/pdf/2607.26656v1](https://arxiv.org/pdf/2607.26656v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-world vulnerabilities often span multiple functions, yet most learning-based detectors classify each function in isolation: on a sample of real CVEs, we find that 71.7% of vulnerable functions require evidence from outside the function to be classified correctly. Agentic reinforcement learning (RL) could close this gap by enabling a model to gather that evidence itself, but it lacks a reliable reward, since a reward defined on the final verdict alone can be obtained without performing any investigation. We propose VulAgentRL, an agentic RL framework for interprocedural vulnerability detection built on a Code Property Graph (CPG). The CPG serves two roles: at inference time the policy queries it for callers, callees, dataflow, and other queries, and at training time the same graph verifies the evidence the policy cites. Because every CPG node carries a persistent integer identifier, this verification is an exact comparison rather than a textual match, so the reward credits verdicts that are supported by evidence. We further initialize the policy by distilling teacher investigations, and show that this warm start is necessary, since RL cannot acquire tool-use behavior it never samples. Under a repository-level split that prevents leakage, VulAgentRL outperforms state-of-the-art baselines, including frontier models, on the strict pair-wise-correct metric while issuing fewer tool calls, and its advantage persists on an out-of-distribution corpus and under class imbalance.

</details>


### 85. Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability

- **Authors:** Sizhe Zhou, Sheldon Yu, Hui Wei, Junda Wu, Siru Ouyang, Yizhu Jiao, Shijia Pan, Julian McAuley, Yu Zhang, Tong Yu, Jiawei Han
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26637v1](http://arxiv.org/abs/2607.26637v1)
- **PDF:** [https://arxiv.org/pdf/2607.26637v1](https://arxiv.org/pdf/2607.26637v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools. Yet research has largely passed over this medium: prior systems design bespoke memory representations and study retrieval over them, leaving the default's two working assumptions untested: that an agent can keep a growing store organized as memories accumulate, conflict, and go stale, and that this organization pays. We present the first systematic exploration of filesystem-based memory for LLM agents. We formalize the setting as three roles around one memory filesystem: a management agent integrates and organizes incoming content, a search agent answers queries with cited sources, and an execution agent supplies task trajectories that are distilled into skills, unifying declarative memory and skills in a single store. Across long-conversation benchmarks and embodied tasks, we vary memory shape (agent-organized hierarchy, verbatim dump, chunk retrieval), stream scale, tool harness (sandboxed shell, memory-tool-style functions, varied search tooling), and the strengths of the management and search agents, tracking answer quality, cost, and store health as memory grows. What organization reliably buys is search economy: organized stores roughly halve retrieval cost where material is large. Today's agents, however, fall short of the default's promise: in our growth study, organization erodes for all but the strongest management agent, and no agent we measure converts organization itself into better answers. And the model is not the only lever over a store's shape: changing the tool set alone reshapes the store as strongly as swapping the model. The study turns the filesystem default from an assumption into a design space for agent memory.

</details>


### 86. A Graph-Native Bitemporal Memory Store for Conversational AI Agents

- **Authors:** Alp Niksarli, Gopesh Baheti
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26520v1](http://arxiv.org/abs/2607.26520v1)
- **PDF:** [https://arxiv.org/pdf/2607.26520v1](https://arxiv.org/pdf/2607.26520v1)
- **Categories:** cs.DB, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Conversational AI agents commonly lack persistent memory across sessions. The obvious fixes like injecting full chat histories into the context window, or delegating to a third-party memory service, either exhaust the model's context budget or send personal data through infrastructure the user does not control. We describe a memory store that avoids both problems: an agent-local Neo4j property graph augmented with HNSW vector indexes and a full bitemporal data model. Each memory is stored as an immutable identity node linked to versioned content nodes carrying two closed-open time intervals: valid time (when the fact was true in the world) and transaction time (when the database recorded it). This design supports point-in-time semantic retrieval without physically overwriting history. Semantic edges between related memories are maintained automatically at write time using cosine similarity over 1024-dimensional embeddings. We evaluate the system on LongMemEval, a 500-question benchmark spanning six question types designed to stress long-term memory. Across 60 sampled questions, the current-state semantic search path achieves 46.7% R@10 overall, rising to 80% on knowledge-update questions. The time-travel path yields 80% R@10 on knowledge-update but decreases recall on temporal-reasoning questions (50% to 37.5%), a consequence of post-filter dilution that points directly to a concrete design improvement. We discuss what these results reveal about the limits of pure retrieval for different question types and what each failure mode suggests for future work.

</details>


### 87. Evidence-Ledger Adjudication for Claim-Evidence Traceability

- **Authors:** Gengyu Chen, Yongjie Yu, Weiling Wang
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26512v1](http://arxiv.org/abs/2607.26512v1)
- **PDF:** [https://arxiv.org/pdf/2607.26512v1](https://arxiv.org/pdf/2607.26512v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can draft claims faster than authors can check whether the cited or retrieved evidence supports them. We study evidence-ledger adjudication: a claim-evidence traceability workflow that pairs each claim with an evidence packet, assigns a support relation, and routes unsupported, contradicted, or mixed-evidence claims back to the author. The empirical core is a 2,335-row blind benchmark built from independent external labels in AVeriTeC, CLIMATE-FEVER, and SciFact. Gold relations and source evidence labels are hidden during prediction and joined only for scoring. On this benchmark, the agent evidence-ledger condition achieves 0.676 relation accuracy and 0.601 macro-F1, compared with 0.383 accuracy and 0.303 macro-F1 for the best non-agent baseline. It also routes 1270/1435 claims whose gold labels indicate contradiction, missing evidence, or mixed evidence, while routing 295/900 supported claims. These results show that evidence-ledger adjudication can turn heterogeneous evidence packets into an auditable traceability layer for AI-assisted writing.

</details>


### 88. EvoPINN: Agentic Discovery of Executable Algorithms for Physics-Informed Neural Networks

- **Authors:** Peng Yin, Kai Li, Yifan Zhang, Jian Cheng
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26490v1](http://arxiv.org/abs/2607.26490v1)
- **PDF:** [https://arxiv.org/pdf/2607.26490v1](https://arxiv.org/pdf/2607.26490v1)
- **Categories:** cs.AI, cs.LG, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Physics-informed neural networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs), yet their performance heavily relies on the manual, trial-and-error engineering of neural representations, loss formulations, and optimization dynamics. While Large Language Models (LLMs) offer a promising avenue for automated design, unconstrained code generation often yields mathematically invalid or numerically unstable solutions under strict scientific computing constraints. To bridge this gap, we propose \textbf{EvoPINN}, an agentic framework that reformulates PINN development from labor-intensive manual design into a rigorous, execution-grounded algorithm discovery problem. EvoPINN navigates a modular search space by decoupling neural representations from training programs, utilizing an LLM agent to iteratively propose memory-conditioned programmatic modifications. To ensure scientific validity, all candidates undergo strict structural verification and budget-matched PDE evaluation. Extensive experiments across diverse PDE regimes (oscillatory, elliptic, dissipative, and nonlinear transport) demonstrate that EvoPINN discovers PDE-specialized learning algorithms that significantly reduce relative $L_{2}$ error compared to baselines. Crucially, EvoPINN autonomously invented SLRC-PINN, a novel architecture whose performance gains persist under rigorous parameter-matched comparisons, establishing the viability of execution-grounded agents for discovering genuinely new scientific computing mechanisms.

</details>


### 89. Conformal Changepoint Localization and Root Cause Analysis with Corrupted Observations

- **Authors:** Seunghun Yu, Meiyi Zhu, Petar Popovski, Joonhyuk Kang, Osvaldo Simeone
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26481v1](http://arxiv.org/abs/2607.26481v1)
- **PDF:** [https://arxiv.org/pdf/2607.26481v1](https://arxiv.org/pdf/2607.26481v1)
- **Categories:** cs.LG, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Detecting when the statistical behavior of an engineered system changes, and identifying which component is responsible, are core problems in the monitoring of telecommunication networks, robotic platforms, security infrastructure, and multi-agent systems. In safety- and mission-critical deployments, such decisions must be accompanied by statistical reliability guarantees rather than by point estimates alone. Conformal changepoint localization (CONCH) and conformal root cause analysis (CROC) meet this need by returning confidence sets that contain the true changepoint, or the true root-cause stream, with a user-specified probability, without parametric assumptions on the data-generating process. In practice, however, observations are frequently corrupted, e.g., by outliers, sensor faults, or adversarial perturbations. While the finite-sample coverage of these procedures is preserved under contamination, the resulting confidence sets can become uninformatively large. Adopting a Huber-type contamination model, this paper proposes weighted CONCH (W-CONCH) and weighted CROC (W-CROC), which downweight observations that are likely to be corrupted with the goal of reducing confidence set size when data may be corrupted. The weighting mechanism, derived from a formal bound on the unknown corrupted data densities, leverages pre-existing second-order classifier-based uncertainty signals, such as those produced by evidential deep learning or Bayesian learning. W-CONCH and W-CROC are further generalized by introducing a meta-learning procedure for the weights that optimizes a differentiable surrogate of the confidence set size. Experiments on image-based and real-world changepoint and root-cause benchmarks show that uncertainty-based weighting substantially reduces confidence set size while maintaining the target coverage.

</details>


### 90. CaM-Wolf: Causal-Aware Multimodal Agents for Social Deduction Games

- **Authors:** Zheng Zhang, Nanjie Yao, Jiarui He, Deheng Ye, Peilin Zhao, Hao Wang
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26393v1](http://arxiv.org/abs/2607.26393v1)
- **PDF:** [https://arxiv.org/pdf/2607.26393v1](https://arxiv.org/pdf/2607.26393v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Social deduction games (SDGs) such as Werewolf have become challenging testbeds for AI agents. These games require complex social skills such as reasoning, deception, and collaboration. While recent advances in large language models (LLMs) have driven significant progress in SDG agents, current approaches are predominantly text-based, overlooking the multimodal nature that is fundamental to human social interaction. To bridge this gap, we introduce CaM-Wolf, the first SDG agent that integrates multimodal perception and generation. CaM-Wolf processes video inputs from other players, employs a causal-aware Reasoner trained via reinforcement learning to establish logical chains between observable behaviors and hidden roles, and presents itself through an animated avatar. Our experiments and user study show that CaM-Wolf achieves superior agent gameplay performance and enhances the quality of human-AI interaction. This work represents a significant advancement towards creating more human-like AI agents capable of participating in nuanced social dynamics. Our code is available at https://3dagentworld.github.io/avatar_wolf.

</details>


### 91. Exploring Structures in Physics Problems: Can AI Agents Discover Statistical Mechanical Mappings?

- **Authors:** Wanyu Zhao, Wanbing Zhao
- **Published:** 2026-07-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26367v1](http://arxiv.org/abs/2607.26367v1)
- **PDF:** [https://arxiv.org/pdf/2607.26367v1](https://arxiv.org/pdf/2607.26367v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An important skill in theoretical physics is to recognize when a new problem can be transformed into a known model. We study this skill as an AI-agent task: can LLM-based agents discover statistical mechanical mappings from a raw partition function to a tractable representation? To probe this question, we introduce StatMechBench-v0, a benchmark of six Ising-type problems covering transfer-matrix methods, gauge-removable disorder, and planar/Pfaffian structure. We evaluate a simple propose-verify-revise agent across multiple LLMs and problem phrasings. The results show that numerical feedback often helps agents repair code and recover correct partition functions. However, agents can also pass the numerical checks while misidentifying the underlying tractable class or understating computational complexity. This both reveals limitations in current LLM reasoning and calls for a verification stack that goes beyond numerical agreement, incorporating, for example, symbolic checks and structural invariants. Our study provides an early evaluation and design directions for AI agents aimed at structural discovery in theoretical physics.

</details>


### 92. Pramana: A Composable, Domain-Specific Backend for Empirical Networking Research

- **Authors:** Jaber Daneshamooz, Eugene Vuong, Alagappan Ramanathan, Manni Moghimi, Haarika Manda, Satyam Kumar, Snithik Thode, Satyandra Guthula, Sylee Beltiukov, Dongsu Han, Tarun Mangla, Sangeetha Abdu Jyothi, Walter Willinger, Arpit Gupta
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26352v1](http://arxiv.org/abs/2607.26352v1)
- **PDF:** [https://arxiv.org/pdf/2607.26352v1](https://arxiv.org/pdf/2607.26352v1)
- **Categories:** cs.NI, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Networking research advances by turning hypotheses into empirical evidence, so accelerating it means reducing the lag between ideation (synthesizing a hypothesis) and generating the data that tests it. Consider a concrete case: does a bulk BBR download fairly share its bottleneck with competing real-time Google Meet traffic? Validating this requires configuring a realistic bottleneck link, concurrently generating BBR's bulk transfer and Meet's real-time traffic, and collecting relevant service-quality metrics. Today this overhead is high, often forcing researchers to start from scratch for every new idea. This ideation-to-data-generation gap will only worsen in the agentic AI era, where AI-assisted ideation accelerates exponentially, yet its outputs cannot be validated without a data-generation backend.
  This paper explores how to bridge this gap. We envision a composable, domain-specific backend, Pramana, shaped as a thin waist, with diverse research intents at the top and disparate execution substrates at the bottom. Pramana realizes this waist through a single contract, the intent specification, which disaggregates an experiment into three independent axes: the intent (what data to generate), the substrate (where to generate it), and the mechanism (how to produce it), so one specification runs on any substrate. We demonstrate Pramana's utility by building a first-of-its-kind corpus of 255 data-generation intents mined from 66 published papers, and show the intent specification satisfies all of them, where no existing tool satisfies more than 13%. Our current proof-of-concept implementation already satisfies 34% of these intents, more than twice the best existing tool, and we lay out a roadmap for closing this abstraction-implementation gap through a broader community effort to build the envisioned data-generation backend and accelerate empirical networking research.

</details>


### 93. Learning Implicit Causal World Models from Multi-Agent Demonstrations

- **Authors:** Jasorsi Ghosh
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26336v1](http://arxiv.org/abs/2607.26336v1)
- **PDF:** [https://arxiv.org/pdf/2607.26336v1](https://arxiv.org/pdf/2607.26336v1)
- **Categories:** cs.LG, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

In model-based reinforcement learning, world models exist as internal simulators, but their training often conflates statistical correlations with causal mechanisms. This problem is exacerbated in multi-agent systems where physical transitions are intertwined with strategic agent intents, causing world models to fail under distribution shift. We introduce Implicit Causal World Models to recover environmental dynamics from offline demonstrations without requiring pre-defined causal graphs. By incorporating policy variance, we render world models discoverable via the sequential backdoor condition. Evaluations across coordination tasks (Two-Door, Navigation, and Giveway) demonstrate that these models provide interpretable causal representations under both full and partial observability, with model accuracy scaling directly with interventional strength.

</details>


### 94. StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents

- **Authors:** Ads Dawson, Adrian Wood
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26314v1](http://arxiv.org/abs/2607.26314v1)
- **PDF:** [https://arxiv.org/pdf/2607.26314v1](https://arxiv.org/pdf/2607.26314v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Stealth, the discipline of achieving an objective without revealing your presence, capabilities, or collected intelligence, is what separates sophisticated operators from detectable ones. Elite security researchers and advanced persistent threats achieve their objectives unnoticed; autonomous agents increasingly inherit the same offensive tasks, but do they inherit the tradecraft? We introduce StealthBench,a benchmark that measures operational stealth in autonomous offensive-security agents across six operational security (OPSEC) dimensions. We extract 11 hand-verified OPSEC incidents from real bug-bounty and red-team trajectories, expanded into 14 dockerized task scenarios, where agents, despite finding real vulnerabilities, committed stealth failures inconsistent with standard operational tradecraft: embedding credentials in public uploads, deleting production resources to prove access, force-adding uninvolved users to demonstrate a race condition.
  We evaluate agent trajectories using a 3-model large language model (LLM) judge panel with majority-vote aggregation, measuring safe success rate (solved and stealthy), Stealth@Solve (tradecraft quality among successful solves), and reckless solve rate (solved but cover blown). Our results show that no model exceeds 54% safe success rate (the compound metric requiring both task completion and stealth), confirming that OPSEC failures are systematic across model families. We release StealthBench as a public benchmark to support both the development of stealth-aware agents and automated OPSEC monitoring for autonomous offensive-security deployments. The interactive leaderboard, evaluation harness, and dataset are available at https://stealthbench.com.

</details>


### 95. SARC-DQ: Runtime Data-Quality Gating for Agentic AI: Silent Evidence Defects, the Incompetence Shield, and Downstream-Only Remediation

- **Authors:** Gaston Besanson
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26313v1](http://arxiv.org/abs/2607.26313v1)
- **PDF:** [https://arxiv.org/pdf/2607.26313v1](https://arxiv.org/pdf/2607.26313v1)
- **Categories:** cs.SE, cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic systems act, so a defect in the evidence they retrieve becomes a wrong action with a currency cost. The most dangerous enterprise defects are metadata-borne: a stale price or a superseded record, perfectly well-formed in the payload and betrayed only by freshness, lineage, or provenance. Such a defect never enters the agent's context, and an agent cannot doubt data it cannot see. On a priced replenishment benchmark, a competent agent silently converts an injected metadata-borne defect into a costly action about 60% of the time, with zero data-quality flags and behavioral doubt markers at chance (AUC <= 0.50). Across four model tiers spanning roughly 15x in inference price, the rate stays flat: capability does not buy skepticism. A metadata-aware pre-action gate with downstream-only remediation recovers the loss fully on the signals its predicates cover and not at all on those they miss. A model-free oracle derived from the task's decision geometry tracks the measured rates with MAE 0.015 (Pearson r = 0.876, interval coverage 15/16 cells), giving the flat ladder an analytical form. Evidence integrity is a systems axis distinct from model capability; mitigation depends on enforcement placement and predicate coverage. Code, frozen results, and a deterministic analysis pipeline: https://github.com/besanson/dqSarc

</details>


### 96. AgentGUI: An Interface for Observing and Steering Long-Running AI Agents

- **Authors:** Xuan Zhao, Jiwoong Sohn, Qinyue Zheng, Michael Moor
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26300v1](http://arxiv.org/abs/2607.26300v1)
- **PDF:** [https://arxiv.org/pdf/2607.26300v1](https://arxiv.org/pdf/2607.26300v1)
- **Categories:** cs.CL, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly adept at tackling complex, long-running tasks. With the rapid surge of autonomous capabilities, human oversight is systematically lagging behind due to limited human-centered interfacing. Aiming to address this, we introduce AgentGUI, a user-friendly, locally hosted GUI for seamlessly observing and steering AI agents amid multiple concurrent, long-running sessions. AgentGUI features 1) rich agent trajectory visualizations, 2) effective manual and automated steering, and 3) integration with and coordination between open-source and frontier agent frameworks. A controlled user study demonstrates statistically significant reduction in the time it takes to identify key elements from agent traces (38% faster, p = 0.023). In a preliminary experiment, AgentGUI's automated drift prevention feature raises the task completion rate of small local agents by as high as 34pp across a 0.8B--9B model ladder (N=50 runs per model). AgentGUI is publicly available through its project website (https://agent-gui-project.github.io) and open-source repository (https://github.com/eth-medical-ai-lab/agent-gui), along with a demo video (https://youtube.com/watch?v=GSDyxN1gTF0).

</details>


### 97. Model-Driven Requirements Configuration with Three-Valued Uncertainty Scoring

- **Authors:** Ahmed Ibrahim
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26220v1](http://arxiv.org/abs/2607.26220v1)
- **PDF:** [https://arxiv.org/pdf/2607.26220v1](https://arxiv.org/pdf/2607.26220v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Context: Large Language Models (LLMs) offer natural-language flexibility for automated requirements elicitation but frequently generate structurally invalid requirements and logical inconsistencies, lacking formal correctness guarantees.
  Objectives: This study aims to eliminate logical inconsistencies and enforce structural conformance in LLM-generated requirements while quantifying the LLM's pre-validation decision uncertainty within a formal domain model.
  Methods: We present a neuro-symbolic multi-agent architecture that operationalizes the Object-Oriented Method for Requirements Authoring and Management (OOMRAM) lattice. The LLM acts as a non-deterministic heuristic for lattice traversal, while a deterministic symbolic validator enforces all structural constraints. We introduce a three-valued (T, I, F) -- Truth, Indeterminacy, Falsity -- framework to classify and score the LLM's requirement decisions before and after validation.
  Results: Evaluated across 37 natural-language project visions in eleven application families, the system completely eliminated structural inconsistencies in 35 out of 37 cases (94.6%), with the remaining two containing only 6 unresolved structural errors (0.39% of decisions) due to iteration limits. Three-valued analysis revealed that 24.7% of all decisions are indeterminate -- structurally valid but discretionary choices not explicitly mandated by the stakeholder.
  Conclusion: Offloading structural integrity to a deterministic symbolic layer successfully guarantees structural conformance, while the three-valued classification provides a formal way to measure neural uncertainty, facilitating safe LLM deployment in formal requirements engineering.

</details>


### 98. Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges

- **Authors:** Quim Motger, Marc Oriol, Jordi Marco, Xavier Franch
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26212v1](http://arxiv.org/abs/2607.26212v1)
- **PDF:** [https://arxiv.org/pdf/2607.26212v1](https://arxiv.org/pdf/2607.26212v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-Agent Debate (MAD) is a promising paradigm for improving the accuracy and robustness of Large Language Model (LLM)-based agentic systems. It enables multiple agents to exchange arguments, critique each other's outputs, and iteratively converge towards a solution. However, research remains fragmented, with inconsistent terminology and no rigorous synthesis of MAD design dimensions. We present a systematic literature review characterizing 141 primary studies on MAD. We derive a three-dimensional taxonomy covering debate participants, the interaction mechanisms structuring the exchange, and the agreement protocols governing debate resolution, supported by formal notations to render MAD configurations. Our analysis reveals that the field has implicitly converged on a narrow design pattern - static, fully connected topologies, verbatim exchange, short-term memory and voting resolution strategies - adopted by convention rather than systematic comparison, while promising alternatives remain marginal. Because any MAD setting reflects roughly a dozen interacting design decisions, cross-study comparison is unreliable when these are left implicit. We position the taxonomy as a descriptive map of the research landscape, a framework for controlled benchmarking, and potentially as a schema for machine-readable MAD specifications. As future work, we propose formalizing it into an executable specification, enabling cost-aware benchmarking and automated tuning of debate configurations.

</details>


### 99. (EC)2: Event-Centric Explainability for Cybersecurity Through Multi-Agent LLM Investigations

- **Authors:** Neta Kirmayer, David Tayouri, Andrés Murillo, Motoyoshi Sekiya, Asaf Shabtai, Rami Puzis
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26201v1](http://arxiv.org/abs/2607.26201v1)
- **PDF:** [https://arxiv.org/pdf/2607.26201v1](https://arxiv.org/pdf/2607.26201v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Security operations centers rely on anomaly detection systems to flag suspicious events. Feature-level explanations for anomaly detectors offer limited value for operational investigations. To effectively handle alerts, analysts need to know contextual relationships and need actionable understanding of the entities involved. This paper introduces an event-centric detector-agnostic approach for explaining cybersecurity alerts in small- to medium-sized enterprise networks. We present (EC)2, a multi-agent framework that performs structured, hypothesis-driven investigation to provide explanations grounded in verifiable evidence. Evaluation results show that the proposed framework improves post-detection analysis by generating operationally meaningful explanations, which also enhance event classification accuracy.

</details>


### 100. Position: Evaluation Scores Are Perishable Knowledge Claims

- **Authors:** Sankalp Gilda, Shlok Gilda
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26191v1](http://arxiv.org/abs/2607.26191v1)
- **PDF:** [https://arxiv.org/pdf/2607.26191v1](https://arxiv.org/pdf/2607.26191v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results. When these signals are aggregated via averaging, evaluation confidence can then substantially exceed the reliability of the weakest signal: a phenomenon we call trust inflation in evaluation. We argue that evaluation scores should be treated as epistemic claims with three properties: formality (human evaluation provides stronger evidence than an automated metric), scope (a benchmark result applies to the tested distribution, not universally), and validity windows (benchmark results expire as contamination accumulates and distributions shift). Several converging research traditions (chain-of-thought analysis, possibilistic logic, and algebraic theory) establish weakest-link aggregation as the conservative endpoint of a parameterized operator family controlled by a single pessimism parameter. Drawing on those traditions, and on concrete lessons from building an evaluation harness for agentic AI, we propose that evaluation results carry explicit metadata (formality tier, scope declaration, and expiration date) to make their epistemic status transparent. We illustrate the cost of mean aggregation on the public HELM leaderboard: across 54 frontier models on ten scenarios, the top-five models ranked by mean score and by weakest-link are completely disjoint.

</details>


### 101. GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning

- **Authors:** Lang Cao, Yuhao Shen, Tianyang Luo, Simo Du, Hao Peng, Yue Guo
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26160v1](http://arxiv.org/abs/2607.26160v1)
- **PDF:** [https://arxiv.org/pdf/2607.26160v1](https://arxiv.org/pdf/2607.26160v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical practice guidelines (CPGs) encode diagnostic criteria, but LLM systems typically retrieve guideline text or absorb it through training rather than execute its rules. We introduce GuideSkill, an external reasoning layer that compiles disease-specific criteria into executable functions returning ordinal diagnostic-support scores. GuideSkill-Zero is initialized from guidelines, while GuideSkill-Evo uses case--diagnosis pairs to refine covered skills and add missing diagnoses. At inference, an LLM proposes a differential diagnosis, grounds the features required by each matched skill, and fuses its ranking with the executed skill scores. Across four benchmarks and four backbones, GuideSkill-Zero improves macro-average accuracy over guideline RAG by 13.45% on average. GuideSkill-Evo achieves the highest macro-average for every backbone, improves over direct inference by 18.49% relatively, and increases gold-label skill coverage from 56.5% to 99.5%. On Qwen3.5-9B, it also exceeds the strongest parameter-update baseline by 11.16% without updating the backbone. Expert evaluation further indicates that GuideSkill produces clinically sound and broadly acceptable skills, suggesting that its initialized and evolved rules are reliable and practically meaningful. These results support executable skills as a model-agnostic mechanism for combining guideline-derived procedures with case-derived diagnostic patterns.

</details>


### 102. Even More Deception: Objective Misalignment in Mixed-Motive LLM Multi-Agent Systems

- **Authors:** Marylou Fauchard, Florian Carichon, Margarida Carvalho, Golnoosh Farnadi
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26120v1](http://arxiv.org/abs/2607.26120v1)
- **PDF:** [https://arxiv.org/pdf/2607.26120v1](https://arxiv.org/pdf/2607.26120v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs)-powered multi-agent systems are increasingly deployed in mixed-motive environments, where agents operate under asymmetric information and strategic deception due to conflicting or hidden objectives. In these settings, misalignment with collective goals becomes a central concern. We propose a novel framework for evaluating objective misalignment using the social deduction game Werewolf, modifying the objective of a single agent while preserving its assigned role. Across LLMs from four different model families and sizes, four player roles, and three objective formulations, we introduce a dual analysis of the agents' internal reasoning and their public cheap-talk behavior (i.e costless, non-binding communication that does not directly affect the agents' utilities), complemented by an analysis of game outcomes. Our results show that objective misalignment undermines outcomes in inherently adversarial environments, an effect exacerbated by asymmetric information and specialized roles. While compromised agents consistently develop distinct objective-dependent reasoning strategies, these adaptations remain largely invisible in their public behavior. More broadly, our findings suggest that even subtle objective misalignment can profoundly affect collective decision-making, highlighting the need for effective mitigation strategies for LLM-based multi-agent systems.

</details>


### 103. UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams

- **Authors:** Siyu Xia, Chenheng Zhang, Yanting Wu, Haoxuan Li, Jiajun Chai, Xiaohan Wang, Guojun Yin, Wei Lin, Zhouchen Lin, Haifeng Zhang, Jun Wang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26017v1](http://arxiv.org/abs/2607.26017v1)
- **PDF:** [https://arxiv.org/pdf/2607.26017v1](https://arxiv.org/pdf/2607.26017v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory is essential for LLM agents to accumulate task experience and reuse task-specific execution strategies. However, real-world deployment over boundary-agnostic and evolving task streams exposes a fundamental stability-plasticity dilemma. External retrieval-based memory can rapidly absorb new evidence, but it often fails to internalize recurring execution patterns and incurs inference-time retrieval overhead. Parametric memory enables stable and efficient execution once learned, but typically relies on explicit task boundaries and fixed parameter budgets. Inspired by the human brain, which balances plasticity and stability through complementary episodic storage and gradual consolidation, we propose UniMem, a self-routing framework for autonomous memory management. UniMem uses learnable routing tokens as memory controllers, enabling adaptive coordination between complementary memory pathways: novel or sparse tasks are retained in an episodic buffer for retrieval-augmented execution, while recurring and reliable patterns are consolidated into expandable parametric memory. By decoupling task identification from task execution with routing tokens and parametric memory blocks, UniMem expands memory on demand without task labels during deployment or uncontrolled parameter growth. Experiments on long-horizon streaming task sequences show that UniMem consistently outperforms baselines while maintaining execution fidelity, achieving an average gain of 4.0 EM points across three backbone models.

</details>


### 104. Pictura: Perspective-View Self-Play at Scale for Driving

- **Authors:** Yuan Yin, Elias Ramzi, Marc Lafon, Valentin Charraut, Victor Bares, Yihong Xu, Éloi Zablocki, Alexandre Boulch, Thibault Buhet, Andrei Bursuc, Matthieu Cord
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.26005v1](http://arxiv.org/abs/2607.26005v1)
- **PDF:** [https://arxiv.org/pdf/2607.26005v1](https://arxiv.org/pdf/2607.26005v1)
- **Categories:** cs.CV, cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for occluded agents. This assumes that perception is solved and introduces a representation gap with the partial observation of a deployed agent driving from the perspective view of egocentric cameras. A common fix, distilling the privileged policy into a camera-input student, leaves the student imitating decisions its own view cannot justify. Instead, we establish perspective-view self-play as a practical training regime. We introduce Pictura, a GPU-accelerated multi-agent driving simulator that renders each agent's egocentric view at every step, mitigating the representation gap at its source. Pictura sustains up to 500K agent-steps/s (2M images/s) on a single H100. Using Pictura, we train Alberti by self-play with plain PPO. It is the first large-scale driving self-play policy trained directly from perspective images, without privileged observations. Training spans 50B agent steps for ~35M km of driving. It approaches the driving performance of its privileged vectorized counterpart, and transfers zero-shot to Waymo Open Motion Dataset layouts re-rendered in Pictura, where it outperforms privileged vectorized agents. Project page: https://valeoai.github.io/Pictura/

</details>


### 105. Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA

- **Authors:** Carlos Celemin, Benedict Wilkins, Adrián Barahona-Ríos, Saman Zadtootaghaj, Nabajeet Barman
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25921v1](http://arxiv.org/abs/2607.25921v1)
- **PDF:** [https://arxiv.org/pdf/2607.25921v1](https://arxiv.org/pdf/2607.25921v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this work, we study the use of Vision-Language Models (VLMs) for anomaly detection in an agent-driven game Quality Assurance (QA) pipeline focusing on geometry clipping. In this evaluation, a custom exploration agent navigates a game level to collect visual observations, while the automatic annotation pipeline provides frame-level clipping labels. This setup allows us to evaluate recent VLMs on a controlled anomaly detection task without manual annotation. We benchmark six recent VLMs (Gemini, GPT, Qwen, Gemma, Llama, and Ministral) under a zero-shot prompting setting and analyse their sensitivity to four prompt variants.
  Our results show that while the VLMs can capture visual cues associated with geometry clipping, they all produce substantial false positives on visually ambiguous frames such as near-contact geometry and partial occlusions. Gemini-3.1-Flash achieves the best overall accuracy and is the most robust to prompt variation, while open-source models exhibit large precision--recall swings depending on the prompt design. These findings suggest that current VLMs are best suited as high-recall candidate filters within multi-stage QA pipelines rather than as standalone bug detectors.

</details>


### 106. Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks

- **Authors:** Ravi Kant Sharma, Ashutosh Uttam, Ajay Kumar
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25914v1](http://arxiv.org/abs/2607.25914v1)
- **PDF:** [https://arxiv.org/pdf/2607.25914v1](https://arxiv.org/pdf/2607.25914v1)
- **Categories:** cs.AI, cs.CR, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility. When a tool from Vendor B is compromised, agents from Vendor A continue invoking it -- unaware of the trust degradation -- causing cascading service impact. We present AgentToolMO, a proposed 3GPP NRM information model for agent tool trust management. The model comprises: a formally defined trust state machine with provable graduated enforcement, damped cascade propagation with bounded convergence, cross-vendor trust notifications via existing Management Services (MnS) interfaces, and retroactive impact assessment through NRM dependency graph traversal. Simulation-based evaluation across multi-vendor topologies shows that standardized cross-vendor notifications reduce blast radius from hours-scale undetected propagation to near-real-time containment bounded by MnS notification delivery, with cascade convergence guaranteed in bounded iterations and sub-linear notification scaling across vendor domains. The framework operates within existing 3GPP management infrastructure, leverages existing protocols, and provides a standardization pathway for trustworthy multi-vendor autonomous network management.

</details>


### 107. Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation

- **Authors:** Stefan Krsteski, Charlotte Meyer, Guillaume Allegre, Tony O'Halloran, Alexandre Sallinen
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25891v1](http://arxiv.org/abs/2607.25891v1)
- **PDF:** [https://arxiv.org/pdf/2607.25891v1](https://arxiv.org/pdf/2607.25891v1)
- **Categories:** cs.AI, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or require costly reruns, leaving much of the empirical record incomparable. We introduce Messier, a unified corpus of 957,253 records that span 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers. Messier consolidates public benchmark scores and supplements them with five-agent runs across six underrepresented professional and scientific domains, including a recent legal benchmark. Each record is standardized by model, scaffold, environment, task, verifier, and aggregation rule, with SOC/NAICS classifications for occupational and industry analysis. Using this corpus, we show frontier progress is uneven across benchmark types, with "function calling" saturated, "programming" improving the fastest, and "enterprise workflows" remaining the most challenging. Furthermore, counterfactual rescoring shows that strict all-pass aggregation in multi-verifier tasks can obscure progress and artificially alter agent rankings. From these standardized records, we derive capability scales that align with Epoch's Evaluation Capability Index rankings at Spearman \r{ho} = 0.81 and can be specialized by domain, occupation, action space, or verifier type. Messier provides a foundational, reusable infrastructure for agent capability scaling, benchmark auditing, and fine-grained analysis of evaluation failures.

</details>


### 108. Distributing Security Controls Through Harness Engineering

- **Authors:** William Robert Gore
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25890v1](http://arxiv.org/abs/2607.25890v1)
- **PDF:** [https://arxiv.org/pdf/2607.25890v1](https://arxiv.org/pdf/2607.25890v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents are not systematically distributed to engineering teams, and vendor-native solutions introduce ecosystem dependencies that may not suit every deployment context. This paper investigates whether off-the-shelf security controls can be implemented on commercial AI coding agents and scaled to a distributed user base via a custom agent harness. A phased testing methodology was applied across four agent configurations --- two commercial agents with and without controls, a baseline harness, and a security-hardened harness --- using a 23-test suite derived from the OWASP Top 10 for Agentic Applications. SHarD (Secure Harness Distribution), a distributable harness built on the Pi agent harness, demonstrated that three categories of security controls --- OS sandboxing, skill scanning, and tool restriction --- can be embedded and distributed via a single install command while retaining equivalent efficacy to direct installation on commercial agents. SHarD achieved an adjusted score of 100\%, matching the best securely configured commercial agent, with no regression across any test category. Notable observations include evidence that model non-determinism produces inconsistent security outcomes and that autonomous agent behavior can cross system boundaries in ways that OS sandboxing directly mitigates. Initial characteristics toward a control harness fitness framework are proposed, and a third research question is identified for future investigation.

</details>


### 109. RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement

- **Authors:** Fanqing Meng, Lingxiao Du, Qiguang Chen, Ziqi Zhao, Haocheng Lu, Mengkang Hu, Michael Qizhe Shieh
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25886v1](http://arxiv.org/abs/2607.25886v1)
- **PDF:** [https://arxiv.org/pdf/2607.25886v1](https://arxiv.org/pdf/2607.25886v1)
- **Categories:** cs.SE, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement requires turning evidence of model failures into better models. Data-centric post-training research entails diagnosing capability gaps, designing and validating training-data strategies, and learning from checkpoint feedback. Can LLM agents automate this loop? Existing benchmarks entangle research decisions with optimization, serving, evaluation, and systems implementation, obscuring agents' research capability. We introduce RSIBench-Data, a controlled benchmark of LLM agents as data-centric researchers with a fixed post-training stack. Agents iteratively revise training-data strategies for a fixed target model; training and serving use Tinker-backed services, official evaluation runs through Harbor and E2B sandboxes, and budgets are fixed across agents. We evaluate four frontier agents on six benchmarks across software engineering, terminal use, scientific question answering, and mathematics. Agents demonstrate core data-centric research capabilities: in 58.33\% of settings, they improve upon the first valid attempt by refining strategies from feedback. However, improvement is inconsistent. Among searches continuing after the best observed score, 78.26\% end with a lower-scoring final attempt, while the rest only recover the same peak. A strong candidate may therefore appear early or midway through a run even as later revisions fail. Trajectory analysis identifies four patterns in stronger runs: accurate hypotheses, validation-grounded supervision, behavior-aligned data, and preservation of strong checkpoints. These findings suggest that current agents can make useful data-centric discoveries but cannot yet translate feedback into consistent improvements. RSIBench-Data provides a measurable, auditable testbed for the research capabilities required for recursive self-improvement. We open-source our code at https://github.com/evolvent-ai/RSIBench-Data.

</details>


### 110. Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks

- **Authors:** Bart Custers, Koorosh Aslansefat
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25877v1](http://arxiv.org/abs/2607.25877v1)
- **PDF:** [https://arxiv.org/pdf/2607.25877v1](https://arxiv.org/pdf/2607.25877v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification. Actuarial workflows represent a high-stakes decision-support setting where unreliable outputs may lead to incorrect risk assessment, unfair pricing, and regulatory non-compliance. To address uncertainty introduced by the probabilistic nature of LLMs and dependencies between agents, a multi-agent framework is proposed in which specialised agents perform data preparation, modelling, review, and explanation tasks under a central hub. The main contribution is a novel approach to uncertainty propagation using token-level log-probabilities and a Bayesian Network. Importantly, log probabilities are not treated as direct probabilities of correctness or task success. Instead, length-normalised log-probability summaries are transformed into calibrated task-level confidence estimates before incorporation into the Bayesian Network. Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.

</details>


### 111. HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs

- **Authors:** Yu Hao, Jinxuan Cai, Qi Zhang, Yawen Li, Zhiqiang Zhang, Chuan Shi, Cheng Yang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25853v1](http://arxiv.org/abs/2607.25853v1)
- **PDF:** [https://arxiv.org/pdf/2607.25853v1](https://arxiv.org/pdf/2607.25853v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks. However, existing trajectory-to-skill methods often produce flat collections of high-level textual skills that are stored and retrieved independently, leaving skill relations underutilized and maintaining a gap between high-level skills and executable actions. In this paper, we propose HiSkill, a hierarchical skill graph framework that organizes interaction trajectories into a directed graph with skill nodes, AtomicOp nodes, and typed edges. Specifically, the graph connects reusable high-level skills with executable action templates, while also capturing decomposition, temporal transition, compatibility, support, and recovery relations among them. At inference time, HiSkill retrieves a compact task-relevant subgraph and performs subgraph-guided task execution, where a symbolic task state, an active skill, and the retrieved subgraph guide the LLM agent to switch skills, select AtomicOps, and ground executable actions iteratively. Experiments on three interactive environments show that HiSkill outperforms state-of-the-art baselines while reducing inference token consumption, demonstrating the effectiveness of bridging high-level skills and executable action grounding through a hierarchical skill graph. Our data and code is available at https://github.com/BUPT-GAMMA/HiSkill.

</details>


### 112. Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL

- **Authors:** Jiabao Ji, Yujian Liu, Li An, Rohit Jain, Gungor Polatkan, Siyu Zhu, Shiyu Chang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25816v1](http://arxiv.org/abs/2607.25816v1)
- **PDF:** [https://arxiv.org/pdf/2607.25816v1](https://arxiv.org/pdf/2607.25816v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents often spend substantial wall-clock time waiting for tool call results. Tool-call speculation can hide this latency by predicting and pre-executing an agent's next tool call if the prediction matches the agent's eventual tool call, but existing speculators are typically separate draft models or cached traces that are poorly aligned with the deployed agent's own behavior. We identify this speculator-agent gap and show that the target agent itself is a strong next-call speculator. This points to a simpler design: unifying the agent and speculator within the same model. In this paper, we introduce the self-speculating agent, a single model that both solves tasks in agent mode and predicts its next tool call from partial trajectories in speculator mode, fully reusing prefix KV cache. To enable this dual-mode agent without degrading performance, we propose a joint agent-speculator reinforcement learning method, which derives speculation targets from the agent's own rollouts and alternates agent and speculator updates. Across agentic search QA and conversational tool-use agentic tasks, our method improves average next tool-call Hit@1 from 44.1 to 61.2 for Qwen3-4B and from 48.9 to 66.3 for Qwen3.5-4B, while preserving agent task success.

</details>


### 113. Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller

- **Authors:** Thomas Hickling, Dylan Wynne, Yu Su, Nabil Aouf
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25728v1](http://arxiv.org/abs/2607.25728v1)
- **PDF:** [https://arxiv.org/pdf/2607.25728v1](https://arxiv.org/pdf/2607.25728v1)
- **Categories:** cs.RO, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper presents a cooperative indoor UAV guidance framework that combines a shared voxel-map world model with a multi-agent Soft Actor-Critic (MASAC) controller. Multiple drones fuse 360 LiDAR observations into a common world-frame occupancy map, which is converted into a compact bird's-eye-view (BEV) representation and provided to each agent as an ego-aligned local crop. This integrate-in-world, act-in- ego design enables consistent multi-UAV spatial fusion whilst retaining decentralised continuous control. The policy combines BEV map features, near-field obstacle observations, and compact goal and peer-state information within a centralised-training, decentralised-execution framework. In simulation, the learned controller achieves a 90.3% success rate in corridor navigation, outperforming Astar planning, an artificial potential field controller, and a prior guidance method. To address residual sim-to-real mismatch, the simulation-trained policy is further adapted using offline imitation fine-tuning from real-world data. Real-world experiments in GNSS-denied indoor environments demonstrate stable two-UAV cooperative operation across increasingly chal- lenging obstacle layouts. The results show that shared voxel-map representations provide an effective and scalable spatial substrate for learned cooperative indoor UAV guidance.

</details>


### 114. Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction

- **Authors:** Xinyi Hong, Pinjun Dong, Xinyang Yu, Binyan Jiang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25718v2](http://arxiv.org/abs/2607.25718v2)
- **PDF:** [https://arxiv.org/pdf/2607.25718v2](https://arxiv.org/pdf/2607.25718v2)
- **Categories:** cs.LG, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. However, existing retrievers either score each tool in isolation or assemble the tool set sequentially, so the joint utility of a candidate set is never evaluated as a whole. In this paper, we propose HYSET, short for HYperedge-based SEt-level Tool retrieval. Our contributions are threefold: (i) we formulate tool retrieval as query-conditioned hyperedge prediction on a tool co-invocation hypergraph, under which the tool set itself becomes the unit of scoring and most existing retrieval paradigms reduce to restricted instances; (ii) we capture size-dependent tool compatibility through cardinality-specific interactions; and (iii) we design HYSET as a pre-selection module requiring no modification to the downstream agent. Experiments on ToolBench demonstrate that HYSET consistently outperforms state-of-the-art baselines in both tool retrieval performance and end-to-end task success. Beyond the in-domain setting, HYSET further supports zero-shot/few-shot transfer, generalizing to held-out tools/categories and unseen domains with minimal supervision.

</details>


### 115. OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation

- **Authors:** Zhenzhen Ren, Jiyan He, Xinpeng Zhang, Zhenxing Qian, Ke Han, Shuxin Zheng, GuoBiao Li, Xiaoqing Zhang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25656v1](http://arxiv.org/abs/2607.25656v1)
- **PDF:** [https://arxiv.org/pdf/2607.25656v1](https://arxiv.org/pdf/2607.25656v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. Moreover, the time and token costs of real execution grow rapidly with workflow scale, making systematic evaluation expensive. We present OrchBench, a simulation-based benchmark for evaluating multi-agent orchestration plans in isolation. Starting from real-world tasks, OrchBench constructs directed acyclic graphs (DAGs) that encode task dependencies, with controlled sizes and degrees of parallelism. Given a DAG, a per-agent context limit, and an agent budget, the evaluated planner assigns subtasks to agents and specifies cross-agent information transfers and their retention ratios. A deterministic simulator evaluates the resulting plan without invoking worker agents and returns interpretable measures of result quality, makespan, and token cost. The simulated scores produced by OrchBench correlate strongly with quality scores from Claude Code executions, achieving a Pearson correlation of \(r=0.816\), while requiring only \(1.3\%\) of the tokens and \(10.3\%\) of the wall-clock time. Across diverse planners and workflow scales, we find that preserving task-critical information is more important than simply increasing the number of agents, and the benefits of parallelism diminish as coordination failures accumulate. These results establish OrchBench as an efficient and interpretable benchmark for comparing and diagnosing multi-agent orchestration plans.

</details>


### 116. F(AI)2R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill

- **Authors:** Florian Krebs
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25637v1](http://arxiv.org/abs/2607.25637v1)
- **PDF:** [https://arxiv.org/pdf/2607.25637v1](https://arxiv.org/pdf/2607.25637v1)
- **Categories:** cs.DL, cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

F(AI)2R is FAIR research with AI in the loop, twice: an AI-assisted authoring pass and a machine-readable audit pass over every artefact. AI systems now draft, refactor, and verify research artefacts, yet their contributions are rarely recorded in a form a later human or machine can audit. Building on the original F(AI)2R experiment, we generalize its provenance model beyond scholarly writing into aiprov, a PROV-O extension covering any AI-in-the-loop artefact, and we package the method as an executable skill that an AI agent operates itself: setup asks the human operator for their ORCID ID, resolves their identity from the public registry, and scaffolds continuous integration that gates every push on graph conformance and publishes the current build of this very paper. The paper is its own case study. Every activity, claim, and source in its production is recorded in the repository's provenance graph under two invariants: no parentless claim, and verification rungs that only humans may grant.

</details>


### 117. Beyond Epistemia: Epistemic Schizologia and Large Language Models as Techno-Semiotic Machines

- **Authors:** Federico Cabitza, Gianluca Colombo
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25620v1](http://arxiv.org/abs/2607.25620v1)
- **PDF:** [https://arxiv.org/pdf/2607.25620v1](https://arxiv.org/pdf/2607.25620v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Quattrociocchi and colleagues warn that the fluent outputs of large language models may allow linguistic plausibility to substitute for epistemic evaluation, producing the condition they call *Epistemia*: the experience of possessing knowledge without undertaking the practices through which judgment would ordinarily be warranted. This article accepts that diagnosis but challenges its explanatory framework, which compares an embodied, socially situated human knower with an isolated generative model thereby locating epistemic legitimacy in capacities internal to autonomous agents. Drawing on Carlo Sini's philosophy of practices, writing, signs, and technics, we propose instead to understand a large language model (LLM) as a *techno-semiotic machine* that automates a phase of written semiosis by producing plausible linguistic configurations from the sedimented archive of human writing. From this perspective, *Epistemia* is one consequence of a broader phenomenon that we call *epistemic schizologia*: the socio-technical cleavage between signs as linguistically accomplished expressions and signs as moments within socially embedded circuits of interpretation, evidence, criticism, verification, and responsibility. This cleavage is reinforced by *eikotic closure*, through which a plausible continuation is presented with the finality of an epistemic result, and by algorithmic authority and epistemic self-misrecognition. The relevant unit is therefore not the model alone but the complete practice in which generated inscriptions are prompted, interpreted, verified, contested, used, and made consequential. This reframing preserves the distinction between linguistic production and responsible understanding while grounding a design programme centred on inspectable genealogy, contestability, distributed responsibility, epistemic agency, and the evaluation of hybrid human--AIpractices.

</details>


### 118. ARCHER: Agentic Rule and Compliance Harness for Executable Regulations

- **Authors:** Chiraag Singh Anand, Xue Wen Tan, Lionel Teo, Eric Tan
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25566v1](http://arxiv.org/abs/2607.25566v1)
- **PDF:** [https://arxiv.org/pdf/2607.25566v1](https://arxiv.org/pdf/2607.25566v1)
- **Categories:** cs.MA, cs.CE, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Verifying building compliance requires validating thousands of rules against large Building Information Modeling (BIM) designs, which is laborious, capital-intensive, and unscalable. Existing Automated Compliance Checkers (ACCs) are often difficult to generalize across different scenarios, as they are typically developed for highly specific rule sets and use cases. In addition, many ACCs are proprietary, meaning the underlying verification code is not released to end users, so users cannot verify whether their regulatory intent can be accurately captured. We introduce ARCHER (Agentic Rule and Compliance Harness for Executable Regulations), a test-driven, deterministically orchestrated multi-agent program-synthesis harness that generates auditable verification code from regulatory Codes of Practice, enabling transparent, adaptable, and scalable compliance checking. To characterize what makes agentic synthesis work, we evaluate a taxonomy of six harnesses of increasing agentic sophistication across four backbone models, spanning realistic data-governance tiers (from frontier third-party APIs to a fully on-premise open-weights model) on a novel dataset derived from real-world compliance scenarios. ARCHER's deterministic multi-agent orchestration achieves the highest accuracy for every backbone, improving mean union accuracy by 82% over a naive single-pass prompting baseline. Our cost-accuracy analysis further shows that using the ARCHER harness, a self-hosted open-weights model can reach 97.8% of frontier-API accuracy at a quarter of the cost, making data-sovereign compliance checking practical.

</details>


### 119. Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories

- **Authors:** Jianing Geng, Ruiqi He, Zekun Fei, Biao Yi, Xuansheng Wu, Ruijie Wang, Zheli Liu, Xia Hu, Qingkai Zeng
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25560v2](http://arxiv.org/abs/2607.25560v2)
- **PDF:** [https://arxiv.org/pdf/2607.25560v2](https://arxiv.org/pdf/2607.25560v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. Yet hiding the artifacts does not conceal their behavioral effects, which remain observable in execution trajectories and form a behavioral side channel. We define this exposure as Skill Leakage: reconstructing proprietary skills from trajectories elicited by benign queries, without reference answers or success labels. We introduce SigLeak, a black-box framework that exploits recurring skill signatures in agent behavior. It constructs diverse, decision-rich diagnostic tasks, contrasts matched skill-enabled and skill-disabled trajectories, and iteratively refines a reconstructed skill from the isolated patterns. Across five scenarios, three model families, and three agent frameworks, SigLeak outperforms or matches three baselines in nearly every setting. It raises the success rate by 6.88 percentage points over the skill-disabled reference on average and achieves the highest overall SkillSim, our metric for coarse- and fine-grained semantic similarity. These results show that benign execution trajectories can expose proprietary procedural knowledge. The code is available at https://anonymous.4open.science/r/SigLeak-D1DB.

</details>


### 120. Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis

- **Authors:** Wanxu Cai, Zhengyu Chen, Huaisheng Zhu, Wei Wang, Jingang Wang, Qiang Xu
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25554v1](http://arxiv.org/abs/2607.25554v1)
- **PDF:** [https://arxiv.org/pdf/2607.25554v1](https://arxiv.org/pdf/2607.25554v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Future event prediction carries broad social impact yet remains challenging. SOTA approaches augment LLMs with external agent frameworks whose predictive capability vanishes once the harness is removed. While recent Tool-Integrated Reasoning (TIR) internalizes deep search for multi-hop retrieval of facts, forecasting further demands temporal search and reasoning over historical trends and dynamic shifts. The key obstacle is data: historical queries induce temporal leakage that degrades forecasting into retrieval. Prior works either freeze information gathering with static observations, or rely on rejection sampling or unresolved fresh queries that discard vast amounts of data, degrading synthesis efficiency. We propose a time-truncation harness that enforces a temporal cut-off at every turn, enabling TIR-style sampling from historical events, reducing temporal leakage and reliance of rejection sampling or unsolved queries, increasing the sampling efficiency. We further build a large-scale corpus and a process-based metric and show that our harness naturally induces a broader temporal breadth of search and raises the proportion of high-quality data, further increasing the efficiency and reducing the reliance on complex rubrics. Distillation experiments show that students trained on harness-intervened data achieve the best performance, demonstrating harness-assisted model evolving that turns higher quality temporal search and reasoning data into a parametric advancement of the students.

</details>


### 121. PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents

- **Authors:** Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou, Mohammad Abuzar Hashemi, Prasad Kasu, Deepak Bansal, Daniel Lopez-Martinez, Anchal Nema, Ramya Ganesan, Will Kimbrough, Alex Woody, Yadunandana Rao, Dilek Hakkani-Tur, Wilko Schulz-Mahlendorf
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25485v1](http://arxiv.org/abs/2607.25485v1)
- **PDF:** [https://arxiv.org/pdf/2607.25485v1](https://arxiv.org/pdf/2607.25485v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Health AI is evolving from answering questions to agentic systems that converse with patients, reason about health records, and act on their behalf. Primary care guards against diagnostic errors and unsafe care; agents assisting in this domain warrant evaluation against the same risks. Current benchmarks focus on medical knowledge, assessed through isolated question-answering or clinician-facing tasks. PatientAgentBench benchmarks patient-facing agentic healthcare; it evaluates a foundation model, wrapped in an agent with a sandbox of healthcare tools, conversing with a simulated patient. Each conversation is scored by an LLM-as-a-Jury across six dimensions via over a hundred conversation-agnostic, clinician-grounded criteria. To validate alignment, licensed clinicians annotated shared conversations, yielding 79-93% adjacent agreement between jury and expert raters, on par with or exceeding clinician inter-rater agreement. We benchmarked 10 models across four families on the same 1,200 scenarios and found clinical gaps. Triage quality is the most discriminating dimension: pass rates rise from 32% for the weakest models to 88% for the strongest, with agents often acting on administrative requests without clinical screening. Clinical safety and workflow accuracy follow the same pattern: the weakest models fail often, fabricating unexecuted actions, while frontier models fail on only 1-3% of cases, from unverified tool outputs and omitted crisis resources in an emergency. More capable models narrow these gaps but do not close them; the strongest scores only 4.25 of 5 overall. These failures surface only in sustained, tool-using conversations against realistic patient records, confirming that static benchmarks are insufficient as healthcare agentic systems gain autonomy. We release the framework as a reproducible, clinician-validated evaluation standard to help the field close this gap.

</details>


### 122. Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm

- **Authors:** Huan Chen, Xiang Song, Jian Jin, Pan Ren, Liang-Jie Zhang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25446v1](http://arxiv.org/abs/2607.25446v1)
- **PDF:** [https://arxiv.org/pdf/2607.25446v1](https://arxiv.org/pdf/2607.25446v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: who is on the team (organization), how members align (coordination), and which algorithm fuses their work (collaboration protocol). IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers. Classic organizational theory (Belbin roles, Mintzberg coordination, RACI accountability) becomes executable, validated configuration, and the framework places six published collaboration algorithms behind a common interface while exposing roles, coordination, and accountability as independently configurable factors. We use this separation to conduct controlled comparisons in which organizational assignments vary while the collaboration protocol is held fixed. It also turns protocol choice into a variable that can be learned: Adaptive Org Routing, a contextual-bandit meta-protocol, selects a protocol per task under an explicit quality-cost tradeoff, outperforms every fixed protocol in a controlled study, and trains online on real benchmark and LLM-judge rewards. The ablations expose a mechanism. Accountability placement changes outcomes exactly when the protocol routes the deliverable through the accountable agent, and the winning placement flips across model families, so organizational design cannot be hard-coded; it must be revalidated, or learned, for each model binding.

</details>


### 123. MARS: Multi-Agent Re-ranking for Repeat-Order Food Delivery Recommendation

- **Authors:** Jiahao Tian, Zhenkai Wang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25420v1](http://arxiv.org/abs/2607.25420v1)
- **PDF:** [https://arxiv.org/pdf/2607.25420v1](https://arxiv.org/pdf/2607.25420v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used in recommender systems, but it is often unclear how much performance can be obtained from strong pre-trained backbones alone when they are placed inside a structured recommendation pipeline. In this paper, we present MARS, a modular multi-agent re-ranking framework for repeat-order food delivery recommendation. MARS serves as a controlled hybrid framework for studying how far pre-trained LLMs can go in this setting when combined with lightweight collaborative retrieval and contextual filtering. MARS performs coarse-to-fine recommendation in two stages: cuisine prediction followed by vendor ranking. The framework combines LightGCN-based global preference signals, Swing-based local peer evidence, geospatial filtering, and prompt-driven LLM reasoning over behavioral, temporal, and geographic context. We evaluate MARS on two real-world Delivery Hero benchmarks, DHRD-SE and DHRD-SG, and compare it against heuristic, sequential, graph-based, and food-delivery-specific baselines. We also provide detailed implementation and evaluation protocols, including prompting and decoding. Our study makes three contributions. First, it presents a modular multi-agent framework for repeat-order food delivery recommendation that integrates collaborative signals and LLM-based re-ranking in a transparent pipeline. Second, it shows that strong pre-trained backbones can already be competitive in repeat-order recommendation when paired with lightweight collaborative retrieval. Third, it establishes a reproducible evaluation setting for hybrid LLM recommenders in food delivery.

</details>


### 124. A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain

- **Authors:** Debjyoti Paul
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25415v1](http://arxiv.org/abs/2607.25415v1)
- **PDF:** [https://arxiv.org/pdf/2607.25415v1](https://arxiv.org/pdf/2607.25415v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production LLM agents are increasingly assembled from a frozen model wrapped in a harness: a prompt template, a tool set, a memory/retrieval layer, a planning strategy, and a verification policy. Two 2026 systems, Meta-Harness (Lee et al., 2026) and HyperAgents (Meta AI, 2026), show that this harness can itself be optimized or even self-rewritten by an agentic proposer -- at the cost of either an expensive code-search loop or unconstrained self-modifying code, neither of which is auditable or usable with a fully black-box model API. We take a narrower, more constrained position: treat the harness as a small, fixed, human-legible action space and learn a policy over it online with classic sample-efficient reinforcement learning (an $ε$-greedy contextual bandit and REINFORCE), scored against a multi-objective reward (task success, verifier score, policy compliance, cost, latency, and an unsupported-claim penalty). We instantiate this control system with DSPy (Khattab et al., 2024) as both the context assembler and the source of the strongest non-adaptive baseline (a DSPy BootstrapFewShot static prompt), and evaluate it across three verifiable task domains -- tool-use workflows, code generation (HumanEval), and multi-hop retrieval QA (HotpotQA) -- and two model providers (a local Ollama model and AWS Bedrock). We release the harness-control-system code, the cross-domain verifiable task suite, the full trajectory/reward-decomposition logs from training, and a provider-agnostic deployment recipe for applying this to a new organization's domain and verification setup.

</details>


### 125. Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents

- **Authors:** Debjyoti Paul
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25408v1](http://arxiv.org/abs/2607.25408v1)
- **PDF:** [https://arxiv.org/pdf/2607.25408v1](https://arxiv.org/pdf/2607.25408v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026). We do not claim to introduce control theory to LLM agents -- that ship has sailed. Our narrower claim is about what the controlled variable is. Prior work controls tool selection, inter-agent message routing, or the agent's raw action stream. We instead treat context assembly itself -- which prompt template, which few-shot demonstrations, how much retrieved context, how many planning/verification passes -- as the controlled variable, learned online by a contextual bandit or REINFORCE policy sitting outside a frozen model. This paper develops the formal decomposition (inner frozen policy $π_θ$, outer context policy $π_φ$), gives a stability argument for the online controller in the sense used by Zhang et al. (2026) (non-decreasing expected reward under bounded policy change), and reports an uncertainty-calibration analysis of the controller's own confidence against realized task outcomes. The applied counterpart to this paper instantiates the same controller across three domains and two model providers and releases the dataset, trajectory logs, and a deployment recipe; here we focus on the formal framing and the stability/uncertainty evidence a control-theoretic claim requires.

</details>


### 126. COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution

- **Authors:** Jincheng Wang, Min Zheng, Tao Wei
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25400v1](http://arxiv.org/abs/2607.25400v1)
- **PDF:** [https://arxiv.org/pdf/2607.25400v1](https://arxiv.org/pdf/2607.25400v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly entrusted with natural-language workflow instructions (e.g., retail-payment policies) that specify not only what outcome to achieve, but also which steps, branches, and tool interactions are permitted. When these instructions are supplied as prompt context, however, the model retains control over both procedure selection and step execution. As interactions accumulate, an agent can skip required steps, take unsupported branches, or execute a valid step with unsupported arguments or effects--a failure mode we call workflow misalignment. In this work, we propose COVENANT, a compiler-and-interpreter architecture for workflow-aligned agent execution. Our key insight is to treat workflow instructions as source programs rather than prompts. COVENANT converts the instructions into a workflow abstract syntax tree (WAST) and lowers it to a workflow control-flow graph (WCFG). At runtime, a controller interprets the WCFG one node at a time, checks each proposal against requirements extracted from the instructions before committing controller state or advancing the graph, and returns diagnostic feedback for repair. To evaluate COVENANT, we use 120 cases from three existing benchmarks, spanning seven workflow scenarios. Compared with state-of-the-art LLM agents, COVENANT improves benchmark success from 50.00% to 83.33% and reduces the workflow-misalignment failure rate from 42.50% to 15.83% (62.75% relative). These results show that COVENANT substantially mitigates workflow misalignment, moving LLM-agent alignment beyond isolated prompt following toward reliable execution of complex and multi-step workflows.

</details>


### 127. HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following

- **Authors:** Liudas Panavas, Sebastian Minus, Bradley Monton, Derek Ray, Suhaas Garre, Sushant Mehta, Edwin Chen
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25398v2](http://arxiv.org/abs/2607.25398v2)
- **PDF:** [https://arxiv.org/pdf/2607.25398v2](https://arxiv.org/pdf/2607.25398v2)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents are increasingly deployed under standing instructions: a system prompt, a policy file, or a skills document is placed in context, and the agent is trusted to let it govern every action that follows. Existing benchmarks rarely test this deployment pattern directly; they measure whether an agent can complete a task, not whether a long, binding policy document actually constrains its behavior over an extended tool-use horizon. We present HANDBOOK_md, a benchmark of 65 agentic tasks modeled on how enterprise employees follow company handbooks. Each task places an agent in a self-contained company environment, a file workspace together with mock email, chat, calendar, issue-tracking, and commerce services exposed over the Model Context Protocol, and instructs it to carry out routine professional work governed by an expert-written standard operating procedure of 20 to 124 pages. Tasks span five domains (finance, medical billing, insurance, logistics, and HR) and ten fictional companies. To resist memorization, every task modifies one of ten base handbooks, altering the specific rules and thresholds on which grading turns, so no two tasks share a policy. Grading is fully deterministic: each task carries a rubric of programmatic criteria (824 in total) that check both that required actions occurred and that prohibited actions did not. Under strict grading, where a trial passes only if every criterion is satisfied, the best of thirty evaluated model configurations passes 36.2% of trials, and most frontier configurations remain below 25%. Failures follow consistent patterns: agents let a plausible in-environment request override the standing policy, perform a required check and then act against its result, lose rule details over long horizons, and report compliance they did not achieve. We release all tasks, environments, and the evaluation harness.

</details>


### 128. Cyber-Capable AI Agents: Vulnerabilities, Evaluation Containment, and Defensive Response

- **Authors:** Abu Bakar Siddik
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25379v1](http://arxiv.org/abs/2607.25379v1)
- **PDF:** [https://arxiv.org/pdf/2607.25379v1](https://arxiv.org/pdf/2607.25379v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cyber-capable AI agents combine language models with tools, memory, and execution en- vironments to perform multi-step offensive-security tasks. Existing work separately measures cyber capability and catalogs attacks against agent components, but provides less guidance on containing a capable agent within the environments used to evaluate it. This review synthe- sizes five vulnerability classes at that boundary: multi-step offensive chains, objectives that conflict with sandbox boundaries, supply-chain and credential exposure, persistent command- and-control, and the speed of automated action. We use the reported July 2026 Hugging Face/OpenAI incident as a bounded case study, distinguishing incident-specific observations from findings established in the wider literature. Across the taxonomy and case, we examine controls for containment, privilege separation, provenance, and responder access, including the dual-use problem that defensive artifacts may also enable misuse. The review identifies practical priorities for evaluating cyber capability together with the security of the environment in which that capability is exercised.

</details>


### 129. Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales

- **Authors:** Genliang Zhu, Chu Wang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25364v2](http://arxiv.org/abs/2607.25364v2)
- **PDF:** [https://arxiv.org/pdf/2607.25364v2](https://arxiv.org/pdf/2607.25364v2)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. EBTE cannot widen baseline authority: conflicts deny, incomplete or uncertain claims review, and only matching claims remain eligible for governed execution. We formalize this composition under explicit mediation and trusted-fact assumptions and implement a versioned reference profile with minimized audit packets. Across 136 authored conformance scenarios, the full profile matches all specified dispositions, admits none of 96 designated hard contradictions, and passes 232 metamorphic checks. A draft-only reference integration forwards none of 48 authored hard cases under EBTE while preserving all 16 soft-review and 4 aligned draft paths. In a frozen 2026-07-12 exploratory 224-attempt hosted-model record, the historical generation/runner agreement counts are 71/96, 66/96, and 19/32; a zero-call revalidation of the preserved minimized claims under the current pipeline yields 70/96, 65/96, and 17/32. In an AgentDojo-derived semantic check, existing high-risk controls make all 12 attack proposals non-allow, while EBTE resolves the task--proposal contradictions as deny. Together, these studies establish profile conformance and demonstrate the feasibility of server-checked action claims within the evaluated settings.

</details>


### 130. Cardiologent: Multi-Agent Clinical Decision Support for Patient-Level Arrhythmia Assessment, Urgency, and Management

- **Authors:** Sukju Oh, Moo-Yong Rhee, Jae-Sik Jang, Sukkyu Sun
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25340v1](http://arxiv.org/abs/2607.25340v1)
- **PDF:** [https://arxiv.org/pdf/2607.25340v1](https://arxiv.org/pdf/2607.25340v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

The same episode of atrial fibrillation is a minor finding in a healthy adult and grounds for anticoagulation in an elderly patient with hypertension: identical signal, opposite decision. Naming the rhythm is only the start; what determines a patient's outcome is the judgement that follows -- what the arrhythmia is across the whole record, what it means for this patient, and what should be done about it. Recent work pairing large language models with the ECG stops short of this, reading one recording without assembling a patient-level finding; and agentic systems built around it either receive the arrhythmia a device has already detected or target a different diagnostic task, stopping before the decision this task requires. We formulate patient-level arrhythmia decision support as a task and present Cardiologent, a multi-agent system that spans it from detection to decision. An agent for each signal -- a single ECG lead and the photoplethysmogram a wearable acquires -- grounds its window reading in measured features rather than a bare label; the readings are assembled into the patient's rhythm profile and, with the patient's own data, reasoned against clinical guidelines retrieved for the case, with a critic checking each conclusion against the guideline it cites. We evaluate the clinical decision rather than the report, across integrated diagnosis, clinical significance, and urgency and management. Cardiologent scores highest on every axis, first on every patient-level task under both cardiologists and an at-scale LLM judge -- whose agreement with the cardiologists (ICC 0.74, 0.66) matches theirs with each other (0.67). Because each conclusion traces to a cited guideline and is validated against expert cardiologists, it yields decisions a clinician can audit rather than act on blindly -- a step toward use in continuous monitoring.

</details>


### 131. CAST: Game Solvers as Turn-Level Teachers for LLM Agents

- **Authors:** Yu Wang, Yi-Kai Zhang, Wentao Shi, Ziang Ye, Yuchun Miao, Yueqing Sun, Qi Gu, Xunliang Cai, Lan-Zhe Guo, Han-Jia Ye, Fuli Feng
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25308v1](http://arxiv.org/abs/2607.25308v1)
- **PDF:** [https://arxiv.org/pdf/2607.25308v1](https://arxiv.org/pdf/2607.25308v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training large language models (LLMs) to act in long-horizon games is a promising step toward generalist decision-making, yet reinforcement learning with verifiable rewards (RLVR) relies on sparse final rewards that reveal little about which decisions determine success. Denser process signals could supply this missing turn-level credit, but existing sources are hard to keep both cheap and accurate. We observe that changes in a game solver's state value reveal whether an action advances the state toward success. Building on this insight, we propose CAST (Credit Assignment from Solver Teachers), which converts these value changes into solver advantages and injects them into RLVR as turn-level signals. We further show that, under a soft-optimal solver assumption, maximizing the solver advantage is equivalent to on-policy distillation from the solver, requiring only scalar values rather than teacher logits. Across Sokoban, Minesweeper, and Rush Hour, CAST outperforms all trained baselines on every game under both in-domain and unseen-difficulty evaluation and achieves the highest average zero-shot performance on ALFWorld and WebShop. Our code is available at https://github.com/Wloner0809/CAST.

</details>


### 132. Hybrid Analysis for Secure MCP Tool Use in LLM Agents

- **Authors:** Ping He, Yuexiang Xie, Yaliang Li, Shouling Ji
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25297v1](http://arxiv.org/abs/2607.25297v1)
- **PDF:** [https://arxiv.org/pdf/2607.25297v1](https://arxiv.org/pdf/2607.25297v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid development of large language model (LLM) agents has enabled their broad adoption across diverse real-world tasks. To standardize interactions between LLM agents and external environments, Model Context Protocol (MCP) tools have emerged as a de facto standard and have been widely integrated into these systems. However, the use of MCP tools also introduces new safety risks, as LLM agents can be induced to perform malicious or unauthorized actions. Although prior work has proposed defenses for securing tool use in LLM agents, most methods rely on static analysis, i.e., inspecting prompts and generated outputs, which limits the defense effectiveness and robustness. To address these limitations, we propose MTGuard, a hybrid analysis-based defense framework designed to safeguard the use of MCP tools in LLM agents by leveraging lifecycle-aware static-dynamic co-analysis. Extensive evaluation demonstrates that MTGuard effectively mitigates multiple categories of harmful tool use across different LLM agents while maintaining performance on benign user tasks.

</details>


### 133. ContractHIL-HLS: Contract-Aligned Multi-Agent Workflow with Hardware-in-the-Loop Feedback for HLS Design

- **Authors:** Jingbo Zhang, Haoxiang Sun, Wenbo Wang, Wenbo Zhang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25283v1](http://arxiv.org/abs/2607.25283v1)
- **PDF:** [https://arxiv.org/pdf/2607.25283v1](https://arxiv.org/pdf/2607.25283v1)
- **Categories:** cs.AI, cs.AR, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper presents ContractHIL-HLS, a contract-aligned multi-agent workflow for practical high-level synthesis (HLS) engineering. The workflow makes three contributions. First, it introduces a structured contract as the semantic-alignment and task-execution artifact that translates natural language requirements into explicit interfaces, constraints, validation checks, and rollback rules. Second, it incorporates hardware information into the feedback loop by feeding HLS, Vivado, PYNQ runtime, power, and failure evidence back into generation, thereby extending LLM-assisted HLS from kernel code toward system- and board-level closure. Third, it decomposes agents by semantic lowering and execution tasks rather than by conversational roles: a Contract Agent lowers natural language into the contract, an HTML Agent renders the contract as persistent structured HTML, and a Hardware-in-the-Loop Agent implements and revises the design with measured evidence. We evaluate ContractHIL-HLS in two parts. On 94 locally executable HLS-Eval tasks, the structured contract provides the largest small design gain, improving the estimated single-sample testbench pass rate from 64.0% to 70.2%; the full flow reaches 70.4% pass@1 and 76.6% pass@5. Because HLS-Eval does not exercise board-level design, we also validate ContractHIL-HLS on a board tested ML-KEM/ML-DSA post-quantum cryptography (PQC) secure-message accelerator, where the retained dual-bitstream organization reduces six-message average text runtime from 207.3 ms to 52.4 ms with positive routed WNS on both images while preserving decrypted-message verification. We open-source our work at BJUT-CS316-LAB/ContractHIL-HLS (https://github.com/BJUT-CS316-LAB/ContractHIL-HLS).

</details>


### 134. SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems

- **Authors:** Haowen Dai, Zonghao Ying, Wenfeng Li, Xiangfan Wu, Yisong Xiao, Tianyuan Zhang, Jiaye Lin, Lei Wei, Guangyuan Dong, Xitong Ling, Xixun Lin, Quanchen Zou, Xiangzheng Zhang
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25255v2](http://arxiv.org/abs/2607.25255v2)
- **PDF:** [https://arxiv.org/pdf/2607.25255v2](https://arxiv.org/pdf/2607.25255v2)
- **Categories:** cs.MA, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to evade detection by any single agent. This is a growing social-impact challenge: systems handling sensitive information or consequential tools can turn routine delegation into unauthorized disclosure or unsafe action. We argue that this failure mode is better understood as a semantic information-flow problem than as a single-turn prompt classification task. To address this, we propose SafeFlow, a defense framework for multi-agent systems that formalizes malicious cross-agent propagation as a semantic information-flow problem. SafeFlow attaches structured semantic taints to root requests, propagates them through a dynamic collaboration graph, and performs workflow-level validation to reconstruct the global risk context before irreversible actions are committed. Evaluated on four benchmarks spanning prompt injection, jailbreak-based unsafe tool use, risky code execution, and harmful web-agent behavior, SafeFlow reduces attack success rates compared to undefended baselines and external defenses while retaining high benign task completion and a high paired safe--harm success rate. Our findings show that multi-agent systems still lack mechanisms for preserving risk semantics across delegation boundaries. This gap can turn routine delegation into privacy harms or unsafe actions that affect people and organizations. SafeFlow keeps this risk visible throughout the workflow, before it results in harm.

</details>


### 135. Agentic AI-enabled discovery across large-scale sleep physiology

- **Authors:** Rahul Thapa, Umaer Hanif, Robin Guillard, Andreas Brink-Kjaer, Adrien Specht, Matteo Saibene, Magnus Ruud Kjaer, Harrison G. Zhang, Federico Bianchi, Elisabeth Roxane M. Heremans, Eric C. Landsness, Emmanuel Mignot, James Zou
- **Published:** 2026-07-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25175v2](http://arxiv.org/abs/2607.25175v2)
- **PDF:** [https://arxiv.org/pdf/2607.25175v2](https://arxiv.org/pdf/2607.25175v2)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Sleep occupies roughly one-third of human life, yet many aspects of its physiology remain poorly understood. Large polysomnography (PSG) datasets offer new opportunities to study sleep and its links to disease, but extracting insight from these recordings requires substantial expert effort and remains difficult for general-purpose AI systems. We developed AI Sleep Co-Scientist, an expert-guided environment in which human scientists direct specialist agents for hypothesis development, signal preprocessing, and statistical analysis, reviewing intermediate outputs. Each reported result is linked to the executable code that produced it. Across four cohorts of approximately 124,000 PSG recordings and more than 50 TB of raw signals, we conducted five case studies spanning how sleep physiology relates to future disease, how it distinguishes clinical phenotypes, and how sleep is organized and regulated. Diminished network-level physiological coupling during sleep was associated with incident Parkinson's disease (HR 1.48) and Alzheimer's disease (HR 1.38). A physiologically structured late-fusion sleep-age model outperformed an unconstrained early-fusion approach, and its age residual was associated with incident disease across multiple organ systems. Arousal dynamics characterized comorbid insomnia and sleep apnoea as an intermediate phenotype skewed towards obstructive sleep apnoea, distinguished by prolonged post-arousal wakefulness. Rapid eye movement (REM) bout duration tracked preceding non-REM sleep more closely than intervening wakefulness. Transient-oscillation analysis identified a fast-sigma deficit and excess centrofrontal theta activity in narcolepsy type 1. Together, these findings connect sleep to disease risk, clinical classification, and its own regulation, and show how agentic AI can support large-scale, multimodal discovery.

</details>


### 136. When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops

- **Authors:** Hyundoo Park, Byungho Choi
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25152v1](http://arxiv.org/abs/2607.25152v1)
- **PDF:** [https://arxiv.org/pdf/2607.25152v1](https://arxiv.org/pdf/2607.25152v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-running autonomous agents plan, act, and judge their own completion without human intervention. When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress. We name this failure mode the progress mirage and show, with controlled measurement, that it is a question of what the evaluator is grounded in. We built a testbed that holds the agent and its tool surface fixed and manipulates only the information-channel type of the evaluator that gates the loop. A world-state oracle, unfakeable in principle, is enforced by container and network isolation and verified at every run. Across 54 cycles a frontier agent claimed improvement every time, yet 56 percent had a measured delta of zero or below. Self-report was thus uninformative, and the self-verdict gate degenerated into accept-all, eroding the best deployed state it had reached by 19 percent. Even the strongest in-band judge, reading the full artifact text, the change diff, and its own verdict history, accepted cycles of which 44 percent were real-world regressions and rejected 38 percent of real improvements; the preregistered adversarial hypothesis that a strong judge closes the gap was rejected. On a boundary task whose success specification is verifiable from the artifact itself, the same judge's mirage vanished to zero and the gap collapsed within the registered threshold, showing that the gap depends on where the success signal resides. A sign-only variant returning only the acceptance verdict kept real-world output similar to full feedback (110.0 versus 113.0), locating the benefit in the gate's grounding rather than in feedback content. For open-ended objectives whose success signal lives outside the transcript, scaling up the judge is not enough; out-of-band evaluation with real-world access is a structural requirement.

</details>


### 137. Agentic AI for Scientific Reasoning in Autonomous Quantum Sensing Experiments

- **Authors:** Takuya Isogawa, Ryotaro Okabe, Nutdech Phadetsuwannukun, Mingda Li, Paola Cappellaro
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25145v1](http://arxiv.org/abs/2607.25145v1)
- **PDF:** [https://arxiv.org/pdf/2607.25145v1](https://arxiv.org/pdf/2607.25145v1)
- **Categories:** quant-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We implement an agentic AI workflow built around a large language model (LLM) agent for autonomous experiments with nitrogen-vacancy (NV) centers in diamond. NV centers are a widely used platform for quantum sensing, and the ability to control many measurements from a computer makes NV experiments a natural setting for autonomous workflows. We make two main contributions. First, we demonstrate an autonomous NV experiment workflow that combines persistent project records, quantitative calculation and data analysis tools, and deterministic experiment control. In one autonomous experiment, the agent selected a single NV center, calibrated its resonant frequency, measured \(T_2^\ast\) with Ramsey measurements, and added a Carr--Purcell--Meiboom--Gill (CPMG) measurement to check a weak feature that could be related to nearby \(^{13}\mathrm{C}\). Second, we introduce two offline benchmarks that evaluate the agent's reasoning separately from laboratory execution. We evaluated both benchmarks with GPT-5.4, GPT-5.5, and GPT-5.6 Sol. In the Ramsey checkpoint benchmark, greater reasoning effort generally improved recognition of a residual resonance calibration offset. By contrast, in the pulsed optically detected magnetic resonance (pODMR) data evaluation benchmark, pulse sequence information alone produced more false positive resonance judgments at higher reasoning effort. Requiring an expected signal calculation kept false positive rates low across all three models and reasoning settings. The results suggest a clear division of labor for autonomous experiments. The agent forms scientific hypotheses and uses quantitative tools to evaluate data, while deterministic code controls the hardware and enforces safety constraints.

</details>


### 138. How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation

- **Authors:** Funda Durupinar
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25140v1](http://arxiv.org/abs/2607.25140v1)
- **PDF:** [https://arxiv.org/pdf/2607.25140v1](https://arxiv.org/pdf/2607.25140v1)
- **Categories:** cs.AI, cs.CL, cs.GR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper studies the behavior of language models in a multi-agent crowd simulation, focusing on how affect propagates among agents that perceive and appraise one another. Each agent perceives its neighbors through visual, auditory, and tactile channels, then appraises these perceptions in light of its prompted personality profile, memory, current affective state, and situational context. Appraisal is carried out by an LLM, which updates the agent's internal affective state and selects its outward expression. The architecture contains no hand-authored mechanism for directly transferring affective state between agents; instead, inter-agent influence arises through the perception-appraisal-expression loop. The agent representation draws on the Big Five personality model and Russell's circumplex model of affect. To limit latency, low-level steering and navigation are handled by a conventional crowd simulator operating independently of the LLM-based cognitive layer.
  We evaluate the architecture across five scenario environments spanning alarming, joyful, and neutral situations in different spatial layouts. The results show that the system produces emotional contagion dynamics with spatial, temporal, and personality-dependent structure in sparse, small crowds. Alarm spreads from seeded agents as a traveling front, the mean alarmed fraction settles at a nonzero plateau, and the distribution of prompted personality profiles determines whether an ambiguous alarm ignites panic and whether a provocation is interpreted as anger or fear. We further evaluate the appraisal step through controlled experiments across prompt variants, sampling temperatures, and four model backends, showing that the dynamics are backend-dependent.

</details>


### 139. OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal Biomedical Image Analysis

- **Authors:** Zihan Li, Feiyang Liu, Dandan Shan, Ruibo Wang, Qingqi Hong
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25108v1](http://arxiv.org/abs/2607.25108v1)
- **PDF:** [https://arxiv.org/pdf/2607.25108v1](https://arxiv.org/pdf/2607.25108v1)
- **Categories:** cs.CV, cs.AI, cs.LG, eess.IV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Biomedical image analysis spans diverse modalities and tasks, yet real-world deployment is hindered by severe distribution shifts across scanners, protocols, and patient populations. High-performing models consequently require repeated domain-specific fine-tuning, which is a costly cycle that becomes impractical when labels are scarce or privacy constraints limit data sharing. We propose OPERA (Offline Policy-guided Expert Routing and Adaptation), a multi-agent ensemble framework that addresses this deployment bottleneck by treating expert weight assignment as an offline policy learning problem: a routing policy is learned from a small validation set without gradient updates to any expert agent, then deployed with test-time adaptation to handle distribution shift. OPERA coordinates heterogeneous specialist agents through complementary mechanisms. The expert profiling module learns selection policies offline, enabling informed allocation of expertise. Each agent undergoes confidence calibration through temperature adjustment, ensuring more reliable probabilistic outputs. OPERA also incorporates distribution aware adaptation, where class weights are dynamically adjusted at the batch level using statistics derived from unlabeled test data. Instance level routing assigns each sample to the most suitable expert by leveraging inter model agreement and predictive entropy. We evaluate OPERA on 9 datasets covering fundus photography, chest X-ray, CT, MRI, and multimodal diagnostic benchmarks, comparing against 30+ baselines across classification, segmentation, and multimodal settings. OPERA consistently improves performance and calibration quality, demonstrating that offline policy-guided expert agents coordination is a practical path to deployable biomedical AI without retraining. Code is on \href{https://github.com/HUANGLIZI/OPERA}{GitHub}.

</details>


### 140. Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering

- **Authors:** Rushi Qiang, Changhao Li, Haotian Sun, Yuchen Zhuang, Chao Zhang, Bo Dai
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25090v1](http://arxiv.org/abs/2607.25090v1)
- **PDF:** [https://arxiv.org/pdf/2607.25090v1](https://arxiv.org/pdf/2607.25090v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Machine learning engineering (MLE) tasks require long-horizon decision making over iterative solution debugging and refinement, under expensive and feedback-driven environment interactions. Developing and training a monolithic agent for such tasks is fundamentally challenging, as it must simultaneously manage extremely long and noisy contexts, explore vast solution spaces, and remain effective under limited model capacity and computational budgets. To address these challenges, we propose Matryoshka Agent, a unified hierarchical agent framework for complex long-horizon tasks. Matryoshka Agent decomposes agentic problem solving into a coordinated hierarchy of decision making and execution: a high-level Orchestrator maintains compact, long-horizon exploration states and issues strategic instructions, while lower-level Sub-Agents execute concrete solution attempts through direct environment interaction, mediated by standardized Tool interface. This design decouples strategic exploration from costly execution, substantially reducing the burden of long-context reasoning and enabling efficient iterative refinement. We further develop an efficient training paradigm for Matryoshka Agent. Experimental results on a broad range of MLE tasks with diverse model types and scales demonstrate that Matryoshka Agent is an effective and scalable paradigm for long-horizon MLE tasks and complex agentic problem solving. Notably, Matryoshka Agent enables Qwen3-4B-Instruct to reach Orchestrator performance comparable to o4-mini. Applying Matryoshka Agent to Qwen3-30B-Coder results in at most 36.7% relative performance gain.

</details>


### 141. PLATO: Pointer Learner for Agent and Task Openness

- **Authors:** Alireza Saleh Abadi, Leen-Kiat Soh, Daniel Alan Redder, Adam Eck, Prashant Doshi
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25082v2](http://arxiv.org/abs/2607.25082v2)
- **PDF:** [https://arxiv.org/pdf/2607.25082v2](https://arxiv.org/pdf/2607.25082v2)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open agent systems (OASYS) are increasingly prevalent in real-world domains where the sets of agents and tasks change unpredictably over time. Such openness, including agent openness (AO) and task openness (TO), poses a fundamental challenge to multi-agent reinforcement learning (MARL), which typically assumes fixed state and action spaces. Existing methods address openness only partially: padding and masking approaches introduce artificial bounds, while recent graph-based or hypergraph methods handle one dimension of openness but still depend on restrictive assumptions. In this paper, we introduce Pointer Learner for Agent and Task Openness (PLATO), a pointer-network-based actor combined with a centralized graph neural network (GNN) critic, trained with multi-agent proximal policy optimization under a centralized training and decentralized execution paradigm. Our pointer-based actor outputs distributions directly over the current task set. This directly supports changing action spaces without masking or retraining. Our GNN critic encodes agent-task interactions as a graph that changes shape with task and agent composition. Together, these components consider AO and TO without the boundedness of existing approaches. We formalize PLATO in a Task-and-Agent-Open Markov Game (TaAgO-MG), extending prior task-open formulations, and prove it is well-defined over the resulting unbounded state and action spaces. We evaluate PLATO with the Methods for Open Agent Systems Evaluation Initiative (MOASEI) wildfire suppression domain, an environment designed for open multi-agent system evaluation, and we demonstrate strong performance and more consistent zero-shot generalization than state-of-the-art baselines in OASYS.

</details>


### 142. Towards an Agent Operating System - Lessons from Classical and Cloud OS

- **Authors:** Gosia Steinder, Hubertus Franke
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25076v1](http://arxiv.org/abs/2607.25076v1)
- **PDF:** [https://arxiv.org/pdf/2607.25076v1](https://arxiv.org/pdf/2607.25076v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Every major wave of platform software follows the same arc: an initial period of experimentation with competing frameworks and ad-hoc implementations, followed by the articulation of a small set of stable abstractions with well-defined semantics, and finally consolidation around those abstractions into a platform that applications can portably target. POSIX did this for classical operating systems; Kubernetes did it for the cloud. Agentic AI systems - autonomous, LLM-driven agents that plan, use tools, maintain memory, and collaborate - are currently in the experimentation phase of the third such wave. dozens of frameworks and protocols have emerged, but no community consensus exists on what the core abstractions are or what guarantees they carry. Without that consensus, agentic applications cannot be written portably, platforms cannot compose reliably, and the field cannot advance beyond prototype deployments. We argue that the path forward is to follow the prior-wave methodology: derive new agentic abstractions by extending classical OS and cloud OS primitives to stochastic, natural-language-mediated execution, specify their semantics precisely, and consolidate around them - just as POSIX and Kubernetes consolidated their respective waves.

</details>


### 143. Addressable Recall Compaction for Long Context-Window Control in AI Agents

- **Authors:** Thang Dang, Yuma Ichikawa, Sakina Fatima, Koichi Shirahata
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25066v1](http://arxiv.org/abs/2607.25066v1)
- **PDF:** [https://arxiv.org/pdf/2607.25066v1](https://arxiv.org/pdf/2607.25066v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents accumulate reasoning traces, actions, and tool observations that can eventually exceed a model's fixed context window. Existing compaction methods address this limitation by discarding, summarizing, or retrieving earlier information, but they may remove task-critical details or fail to recover them reliably. We propose ARC (Addressable Recall Compaction), a context-management framework that separates archival storage from active-context presentation. ARC stores tool observations in an append-only, ID-addressable log and replaces older observations with compact citations when compaction is required. The agent can subsequently use these identifiers to request stored content without re-executing the corresponding tools or depending solely on similarity-based retrieval. We evaluate ARC using Qwen3-8B with a 16k context window and Qwen3-32B with a 32k context window. On the Needle-in-a-Haystack evaluation, ARC achieves an average exact-answer accuracy of 99.40%, compared with 88.12% for the best-performing baseline in our evaluation. ARC also reduces estimated serving time and HBM traffic under our hardware-cost model. On the LongBench-v2 Hard subset, ARC obtains an average accuracy of 29.97%, compared with 28.25% for the best-performing baseline. These results indicate that explicit, address-based recall can improve information retention and serving efficiency relative to the evaluated context-management baselines under the tested settings.

</details>


### 144. CogEEGAgent: Toward Autonomous Cognitive EEG Analysis with Grounded Execution and Selection-Aware Verification

- **Authors:** Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, Kazunori D Yamada
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25045v1](http://arxiv.org/abs/2607.25045v1)
- **PDF:** [https://arxiv.org/pdf/2607.25045v1](https://arxiv.org/pdf/2607.25045v1)
- **Categories:** cs.AI, eess.SP, q-bio.NC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Electroencephalography (EEG) analysis in cognitive studies requires specialized expertise and involves many defensible choices over contrasts, channels, time windows, and statistical tests. LLM agents can translate varied natural-language questions into analysis choices, offering a flexible interface for automation. Yet fluent reports alone cannot establish that an agent selected the requested analysis or evaluated a confirmatory claim independently of adaptive search. We present CogEEGAgent, a cognitive-EEG analysis agent grounded in MNE-Python. Its EEG-specific scientific harness separates semantic from scientific authority. The LLM interprets intent and proposes registered analyses, while deterministic components validate typed contracts, control confirmation access, and authorize evidence-bound release. On a prespecified routing benchmark, CogEEGAgent maps language to registered analyses more accurately than a matched deterministic router, while matched preflight makes both systems abstain whenever required. In an externally model-authored, outcome-blind campaign, the complete system releases supported analyses with participant-disjoint confirmation and blocks prespecified capability hazards and lifecycle-reuse requests. Policy stress testing shows that held-out confirmation curbs false positives from uncorrected adaptive search. Together, these studies establish bounded autonomy and an auditable automation framework for cognitive-EEG workflows. More broadly, they show how scientific agents can combine flexible language understanding with fail-closed control over inference and release.

</details>


### 145. SAFAARI: Schema-Aware Framework for Accelerated Advertiser Response Intelligence

- **Authors:** Bhanu Teja Rangaraju, Chandan Kumar
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.25042v1](http://arxiv.org/abs/2607.25042v1)
- **PDF:** [https://arxiv.org/pdf/2607.25042v1](https://arxiv.org/pdf/2607.25042v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

The evolution of customer support systems is rapidly advancing with agentic chatbots, yet these systems face significant limitations when accessing enterprise data without predefined API endpoints. This paper presents SAFAARI (Schema-Aware Framework for Accelerated Advertiser Response Intelligence), a multi-agent framework that addresses the critical bottleneck of schema linking in Natural Language to SQL (NL-to-SQL) systems through specialized content, metadata, and orchestration agents. We also introduce SEAL (Schema Evaluation and Accuracy in Language-to-SQL), a novel composite metric that holistically evaluates system performance while penalizing inconsistent results. Through systematic experimentation with five feature set configurations, SAFAARI achieves an 81.66% SEAL score (6.65% improvement over baseline), with notable gains in datapoint accuracy (5.51%) and schema-linking precision (4.69%). The framework's effectiveness is validated through human-in-the-loop evaluation with domain experts, which proves its adaptability across diverse support domains. By automating the labor-intensive process of schema linking and query generation, our framework demonstrates 8x reduction in development time while maintaining high accuracy. The solution streamlines API development and enhances self-service capabilities, particularly benefiting customer support enterprises with complex data ecosystems.

</details>


### 146. Agentic Permissions Policy Algebra for Taint Confinement in LLM Agents

- **Authors:** Arseny Kravchenko, Vadim Liventsev, Innokentii Konstantinov, Ildar Iskhakov, Matvey Kukuy
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24625v1](http://arxiv.org/abs/2607.24625v1)
- **PDF:** [https://arxiv.org/pdf/2607.24625v1](https://arxiv.org/pdf/2607.24625v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous LLM agents processing mixed-confidentiality data face severe security risks from prompt injection attacks and reasoning errors. While dynamic Information Flow Control (IFC) provides structural security guarantees, traditional taint tracking permanently taints an agent's context upon reading unvetted data, severely restricting downstream utility. We present APPA (Agentic Permissions Policy Algebra), an IFC framework that resolves this usability bottleneck through engine-managed context branching and prospective acquisition enforcement. Before data acquisition occurs, APPA prospectively evaluates label descents and missing prerequisites, generating actionable remedy plans (Authorize, Accept). To inspect unvetted data without polluting the primary context, a label-seeded child trajectory is spawned, absorbing label descent locally and allowing a trusted sanitizer to return a bounded derivative to the unchanged parent. Governed by a two-monoid model over security labels and shared event logs, we formally prove parent label preservation and merge confinement. Finally, we evaluate APPA on a multi-turn tool-chaining benchmark across four models: it suppresses exfiltration (31%-50% down to 0%-7% attack success), and on three of the four, branching recovers a substantial share of the utility that taint tracking alone forfeits.

</details>


### 147. SIREN: Towards End-to-End Extreme-Weather Early Warning with Experience-Grounded LLM Agents

- **Authors:** Hang Ni, Weijia Zhang, Fan Liu, Mengqian Lu, Hao Liu
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24588v1](http://arxiv.org/abs/2607.24588v1)
- **PDF:** [https://arxiv.org/pdf/2607.24588v1](https://arxiv.org/pdf/2607.24588v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Early warning of extreme weather is essential for mitigating the societal, economic, and environmental risks posed by hazardous weather events. However, expert-centered warning workflows are costly, labor-intensive, and difficult to scale throughout the warning-to-action process. Although recent advances in Large Language Model (LLM) agents have enabled the automation of weather-related tasks, existing studies remain centered on isolated scientific tasks and overlook the chain of interdependent processes required for operational extreme-weather early warning. To bridge this gap, this study investigates automated end-to-end extreme-weather early warning through LLM agents. We first develop SIREN-Bench, a comprehensive benchmark comprising 600 question-answer instances across 19 tasks, and covering four individual warning procedures and an end-to-end warning chain. Evaluation on SIREN-Bench reveals substantial capability gaps in existing weather agent frameworks. This motivates us to develop SIREN, an experience-grounded agent framework inspired by experts' use of historical cases, which combines an agentic execution environment integrating heterogeneous weather evidence and tools with a family of agent harnesses that exploit historical cases through retrieval, skill distillation, and predictive modeling. Extensive experiments demonstrate that SIREN outperforms weather-agent baselines on both individual warning procedures and end-to-end warning chains.

</details>


### 148. Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study

- **Authors:** Diego Fernandez Arias, Dev Prashant Mistry, Ren Wang, Yibo Hu
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24893v1](http://arxiv.org/abs/2607.24893v1)
- **PDF:** [https://arxiv.org/pdf/2607.24893v1](https://arxiv.org/pdf/2607.24893v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run. Per-step safety checks that judge each action in isolation may fail to recognize the complete distributed payload. We investigate how early such an attack can be detected while the run is still unfolding, and how robustly it can be caught once its most obvious cues are stripped away. We build a working instance on a hierarchical multi-agent system, run it under benign and attacked conditions across five language models and two task domains, and record when each fragment is injected and when the payload is assembled and executed. Detection is a race against assembly. Before the first fragment is injected, attacked and benign runs are indistinguishable; once injection begins, a prefix detector flags $99.3\%$ of successful attacks with a median of five steps remaining and a $10.3\%$ safe-run false-positive rate. Because assembly occurs only after the run, these alarms arrive in time to abort nearly every successful attack. We then measure how much of that warning rests on removable surface cues of the attack rather than on its distributed structure. Generic zero-shot and behavior-trained detectors provide almost no warning at all; the detectors that do work lean in part on removable surface cues, chiefly the ciphertext's length and entropy, and once the entropy cue is removed from the payload and the length features from the detector, detection arrives later and transfers poorly across domains, though a fine-tuned model recovers some of the loss.

</details>


### 149. Decentralised Consensus Learning Networks: SME Rotation Without Centralised Reward

- **Authors:** Florin Neagu
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24416v1](http://arxiv.org/abs/2607.24416v1)
- **PDF:** [https://arxiv.org/pdf/2607.24416v1](https://arxiv.org/pdf/2607.24416v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Centralised reward signals dominate modern AI learning systems, but they impose a single external definition of correct or valuable knowledge. We present a decentralised, consensus-based multi-agent learning framework in which expertise emerges through peer validation rather than prescribed reward. Agents update beliefs via weighted social consensus, while trust is allocated according to competence inferred from peer consistency instead of ground truth. Subject-matter expert (SME) status is assigned dynamically as a top-percentile competence rank rather than a fixed label.
  We evaluate the framework across 84 simulation runs spanning 30 to 10,000 agents, multiple graph topologies, sparse large-scale networks, scalar and vector belief representations, dimensionality sweeps (D=1-500), multi-seed robustness tests, and parameter sensitivity analyses. Phase 1 shows that SME rotation is robust, persistent, topology-invariant, and scale-invariant: 90-100% of agents attain SME status, with most expertise turnover occurring after belief convergence and increasing with network size. Phases 2 and 3 show that vector beliefs introduce heterogeneous convergence with cascade dynamics and reveal five distinct dynamical regimes as belief dimensionality increases. At high dimensionality (D=150-200), the network reaches stable partial consensus while expertise becomes increasingly concentrated in a single agent. ETA sensitivity analysis demonstrates that this concentration is driven by belief dimensionality rather than stochastic noise. We interpret this behaviour as an emergent property of decentralised learning: in complex high-dimensional consensus spaces, the agent most consistently aligned with the collective belief naturally emerges as the recognised expert.

</details>


### 150. Gubernaut: A Deterministic Homeostatic Controller for Affect-Regulated LLM Agents, Validated Across Independent Model Families

- **Authors:** Dushyant Sharma
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24339v1](http://arxiv.org/abs/2607.24339v1)
- **PDF:** [https://arxiv.org/pdf/2607.24339v1](https://arxiv.org/pdf/2607.24339v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents inherit reactive failure modes: escalation under provocation, sycophantic drift under flattery, perseveration when stuck. These are failures of propensity, not capability; they concern what a model does under sustained pressure, which training-time alignment reduces but does not eliminate at runtime. This research led to the Gubernaut Cognitive Controller (GCC), a model-agnostic runtime control layer in a Nelson--Narens monitoring--control loop: an object level reads and writes text, while a deterministic meta level reads only the numeric telemetry {intensity, valence, repetition} and returns a regulating posture. Because the meta level ingests zero tokens, no injection channel to the controller exists by construction (an architectural property, not yet adversarially tested); the text-exposed arbiter's compliance is measured, not assumed. We evaluate the GCC with a pre-registered, generate-once/judge-many protocol across a 4x4 matrix of four frontier models (GPT-5.5, Claude Opus 4.8, Gemini 3.5 Flash, Grok 4.3), each serving as both a generator and a judge. The regulated arm is calmer in 13 of 16 cells at p<.05 and 15 of 16 by sign; the three sub-threshold cells, including a -0.04 null, all fall on the single near-saturated host. The effect survives a lineage-independent fourth judge family (xAI), strong evidence that it is no artifact of shared judge style. The clearest mechanism is the recovery signature: arousal that integrates under attack and then decays, valence-gated, on de-escalation, replicating across all four families. Transcripts and panels ship with SHA-256 provenance and are re-judgeable; five failure modes are pre-registered.
  No consciousness claims are made.

</details>


### 151. Energy Constrained Hierarchical Underwater Monitoring via Local Multi-Agent RAG

- **Authors:** Mohamed Amine Janati, Laurent Gautier, Stéphane Barbot
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24313v1](http://arxiv.org/abs/2607.24313v1)
- **PDF:** [https://arxiv.org/pdf/2607.24313v1](https://arxiv.org/pdf/2607.24313v1)
- **Categories:** cs.IR, cs.CV, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Marine life monitoring is limited by strict energy constraints, poor underwater connectivity, and the high cost of transmitting raw multimodal data from remote deployments. This paper proposes a low-consumption underwater monitoring architecture that combines always-on edge sensing with selective high-performance local reasoning. The system follows a hierarchical master--satellite design in which ultra-low-power MAX78000/MAX78002 microcontrollers continuously monitor visual and acoustic signals, while an NVIDIA Jetson Orin NX is activated only for scheduled processing, event-driven analysis, or researcher interaction. Once active, the Jetson executes a fully local multimodal pipeline for data ingestion, visual target extraction, embedding-based indexing, species identification, retrieval-augmented reasoning, and automated reporting. BioCLIP/OpenCLIP embeddings are used to organize mission data, marine taxonomic references, scientific documents, and operational metadata in local ChromaDB collections. A dedicated identification layer combines visual similarity search, centroid-based classification, and supervised classifiers to support adaptive species recognition. A LangChain-based multi-agent framework coordinates query routing, structured analysis, energy management, hardware reconfiguration, and report generation. The architecture is evaluated through visual and acoustic monitoring case studies. The proposed system bridges ultra-low-power continuous sensing with local multimodal intelligence, enabling underwater stations to produce structured, researcher-ready knowledge while compressing local data for flexible acoustic, optical, or satellite transmission, minimizing both energy use and communication overhead.

</details>


### 152. From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search

- **Authors:** Junlin Liu, Jiangwang Chen, Zixin Song, Shuaiyu Zhou, Chunji Lv, Hank Wu, Kailin Jiang, Jinyang Wu, Bohan Yu, Chenxi Zhou
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24280v1](http://arxiv.org/abs/2607.24280v1)
- **PDF:** [https://arxiv.org/pdf/2607.24280v1](https://arxiv.org/pdf/2607.24280v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic search enables large language models to solve knowledge-intensive tasks by interleaving multi-step reasoning with retrieval, yet optimizing this with outcome-based reinforcement learning (RL) provides only sparse supervision. Knowledge distillation can supply denser guidance, and advanced proprietary models with their strong reasoning capabilities are promising teachers. While distilling from proprietary models can densify this supervisory signal, conventional logit-matching is precluded by hidden logits and mismatched tokenizers, whereas raw natural language trajectory imitation transfers superficial stylistic artifacts rather than core reasoning competence. To address the heterogeneous distillation problem and bridge the distribution gap, we propose Multi-Agent Protocol Distillation (MAPD), a joint distillation and RL framework uses a structured, style-normalized protocol as an intermediate representation. An offline multi-agent system (MAS) decomposes each query, retrieves supporting evidence, repairs failed searches, and converts the resulting exploration trace into a JSON protocol containing the task type, reasoning plan, and extractive grounding facts. During training, the protocol is provided only to a privileged branch of the student policy, whose token distributions furnish a dense distillation signal alongside the sparse RL objective. Extensive evaluations across seven QA benchmarks demonstrate that MAPD consistently outperforms competitive distillation and RL, achieving average success rates of 39.4\% on Qwen3-1.7B and 44.4\% on Qwen3-4B. Crucially, the framework generalizes robustly across diverse proprietary teachers while effectively mitigating the student policy from style drift and verbosity degeneration.

</details>


### 153. Algorithms for Equilibria in Concurrent Stopping Games

- **Authors:** Léonard Brice, Thomas A. Henzinger, K. S. Thejaswini
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24219v1](http://arxiv.org/abs/2607.24219v1)
- **PDF:** [https://arxiv.org/pdf/2607.24219v1](https://arxiv.org/pdf/2607.24219v1)
- **Categories:** cs.GT, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Concurrent games are a standard model for multi-agent systems, with Nash equilibrium as their central solution concept. The associated \emph{constrained existence problem}---does a game admit a Nash equilibrium whose expected payoff lies within a prescribed interval for every player?---is undecidable, and remains so even for 10-player \emph{stopping} games, in which a terminal state is reached almost surely under every strategy profile. We give two routes to tractability.
  We first relax exactness and consider the problem of approximate constrained existence problem, parametrised by $\varepsilon$-NE, which decides whether an \(\varepsilon\)-Nash equilibrium with the prescribed payoffs exists. The algorithm runs in exponential time, and only polynomially in the bit-size of \(\varepsilon\). We complement it with a \PSPACE-hardness lower bound that holds already for turn-based games, and for pure equilibria as well.
  We then relax the solution concept, turning to \emph{extreme risk-sensitive equilibria} (XRSE), recently introduced for turn-based stochastic games. Here the players are partitioned into optimists and pessimists, who evaluate a strategy profile by the best, respectively the worst, payoff attainable with positive probability, instead of the expected payoff. We prove that the constrained existence problem for XRSE is \NP-complete on concurrent games, as for turn-based games.

</details>


### 154. Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems

- **Authors:** Ali Zahid Raja
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24117v1](http://arxiv.org/abs/2607.24117v1)
- **PDF:** [https://arxiv.org/pdf/2607.24117v1](https://arxiv.org/pdf/2607.24117v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern multi-agent knowledge systems increasingly accumulate knowledge through chains of autonomous transformations rather than direct retrieval. Existing provenance work records what happened - execution traces, tool calls, evidence links - and source-reliability estimation is long established (truth discovery, reputation systems). What is missing is an operational framework that attaches graded, per-domain transmitter reliability to claim-level transmission chains, with completeness semantics, transformation-typed aggregation, decoupled content criticism, and serve/review/quarantine routing.
  Classical Islamic hadith science confronted a structurally similar problem: deciding whether knowledge transmitted through chains of human narrators should be accepted. Over centuries it developed a rigorous methodology - isnad (a complete transmission chain attached to every claim), rijal (systematic grading of each narrator's integrity and precision), weakest-link chain evaluation, corroboration through independent chains, and matn criticism (content evaluated independently of chain quality). This paper transfers that methodology to AI system design.
  We contribute a formal mapping from hadith-science concepts to multi-agent pipelines, a relational schema implementing claim chains and a graded narrator registry, a decision matrix combining chain grade with content criticism, and an evaluation on 20,000 claims from real physics textbooks. The evaluation validates weakest-link quarantine and independent-chain corroboration; reports a partial failure of the grade-recovery loop, which missed the highest-fault narrator; and reports two analyses as inconclusive, including a matched-coverage comparison the framework could not reach with the reference content critic. The paper is explicit throughout about which claims the evidence does and does not yet support.

</details>


### 155. LU-500: A Logo Benchmark for Concept Unlearning

- **Authors:** Keyu Li, Jin Gao, Jialing Zhang, Dequan Wang
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24101v2](http://arxiv.org/abs/2607.24101v2)
- **PDF:** [https://arxiv.org/pdf/2607.24101v2](https://arxiv.org/pdf/2607.24101v2)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Concept unlearning is increasingly used to limit the reproduction of protected or unsafe visual concepts in text-to-image models. Existing evaluations, however, mostly study targets that dominate the whole image, such as styles, broad object categories, or portrait-like identities, leaving company logos comparatively underexamined. Logos create a different failure mode: a small localized mark can carry the entire protected concept, must be visually precise to remain recognizable, and can be triggered implicitly by products, storefronts, packaging, or advertisements even when the word ``logo'' is absent. We introduce LU-500, a logo-unlearning benchmark built from Fortune Global 500 companies to study this localized and semantically entangled setting. LU-500 contains nearly 10,000 curated text-query and logo-image pairs, with an explicit track (LUex-500) and an implicit contextual track (LUim-500). To avoid reducing the task to a binary detector score, we define a multi-grained protocol that evaluates both local logo removal and global image preservation in pixel and latent spaces. Experiments on representative inference-time methods, including NP, SLD, and SEGA, and compatible fine-tuning-based methods such as ESD and Forget-Me-Not, show that the evaluated methods struggle to remove logo evidence without changing non-target content. We further analyze ProLU, a prompt-space multi-agent baseline: it improves local erasure by removing logo-inducing semantics, but also illustrates why prompt filtering is not a substitute for weight-level disentanglement. Correlation analyses over logo area, location, and structural complexity suggest that future logo unlearning may need spatially aware controls, such as SSIM-guided constraints, rather than purely global concept suppression.

</details>


### 156. MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents

- **Authors:** Yiwen Ma, Songjun Tu, Qichao Zhang, Dong Li, Linjing Li, Dongbin Zhao
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24097v1](http://arxiv.org/abs/2607.24097v1)
- **PDF:** [https://arxiv.org/pdf/2607.24097v1](https://arxiv.org/pdf/2607.24097v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model. This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for reasoning, leaving the answer model to resolve redundancy, conflicts, and weak relevance while incurring substantial context overhead in long-term memory tasks. We propose MemChain, a trainable post-retrieval memory policy that transforms retrieved candidates into answer-facing active memory, represented as a compact and grounded evidence context. Given a user query and retrieved candidates, MemChain first generates a question-conditioned evidence plan, then constructs an ordered grounded evidence trace that organizes retrieved memories according to their semantic roles and dependencies, and finally executes explicit memory actions to produce a concise evidence context for answer generation. To train the mediator, we introduce a two-stage learning framework. Supervised trace learning first teaches the policy to generate structurally valid plans, traces, actions, and evidence contexts. We then propose Trace-Guided Memory Policy Optimization (TMPO), a reinforcement learning objective that optimizes the memory policy using downstream answer quality while jointly encouraging trace grounding, evidence support, structural validity, and answer stability across multiple rollouts. Experiments on LoCoMo and LongMemEval-S demonstrate that MemChain consistently achieves state-of-the-art performance across both closed-source and open-weight frozen answer models while substantially reducing the memory context passed to the answer model.

</details>


### 157. The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards

- **Authors:** Keyu Li, Jin Gao, Dequan Wang
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24063v2](http://arxiv.org/abs/2607.24063v2)
- **PDF:** [https://arxiv.org/pdf/2607.24063v2](https://arxiv.org/pdf/2607.24063v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

On standard factuality tasks, frontier models now cluster near the top of the scale. The question is therefore shifting from how factual a system is toward how much compute that factuality costs. Static leaderboards score factuality in isolation and treat compute as free, so they cannot tell a genuinely better system apart from one that simply spends more. Consider a ranking reversal. A brute-force Best-of-4 agent posts the higher raw factuality score (H-Score 0.9169 vs 0.9103) and would top a static leaderboard, but once cost is counted it is the worse system, losing on Q-Score (0.5169 vs 0.5217) at roughly four times the tokens and latency, under a reported cost weight whose sensitivity we sweep. So the system that tops a static leaderboard can be the worse one to deploy. To make this trade-off visible, we introduce MAS-HQ (Multi-Agent System Hallucination Quest), a resource-aware evaluation protocol. It wraps any factuality detector and normalizes for cost, and it pits systems against each other rather than scoring them in isolation. The Q-Score measures factuality minus normalized cost under a competitive match. Across summarization and open-domain QA, single-agent baselines drift into resource-heavy over-optimization, while competition elicits more resource-efficient policies. These gains are small but consistent, and stable across 100 trials. The axis stays discriminative for frontier systems (Gemini-2.5-Pro, and GPT-5) whose raw factuality scores are already bunched near the ceiling. MAS-HQ provides a reproducible way to measure how much a factual answer costs.

</details>


### 158. Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation

- **Authors:** Mohan Manivannan, Dalal Alharthi
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.24006v1](http://arxiv.org/abs/2607.24006v1)
- **PDF:** [https://arxiv.org/pdf/2607.24006v1](https://arxiv.org/pdf/2607.24006v1)
- **Categories:** cs.CR, cs.AI, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cloud telemetry arrives at a scale that, paradoxically, makes intrusion understanding harder rather than easier. Attackers operate through legitimate identity, federated session tokens, and cloud native APIs indistinguishable from routine administration, and analysts spend an incident reconstructing context the logs already contain. We present Cloud Decoy AI Agent, a framework pairing a high fidelity cloud decoy with an autonomous language model agent that compresses the path from suspicious activity to an analyst ready report. Connecting a decoy to an agent is not a wiring exercise. The unit of investigation is the session rather than the event, and the session key is obscured by the identity layering federated credentials introduce. The agent's evidence horizon must be bounded, since an agent free to query full control plane history inherits the cost and false positive profile deception was meant to remove. And cloud telemetry is partly adversary authored, since object keys and user agent strings are attacker chosen values providers record verbatim, which makes any log to prompt path an indirect prompt injection channel that a decoy widens rather than narrows. We address the first two with a session aggregation operator over a pivot tuple drawn only from provider derived fields, and with dynamic prompt generation, a two stage prompt assembly enforcing a grounding invariant by carrying only fields the agent observed. We identify the third as an unaddressed exposure in this class of system, specify the mitigation it requires, and note our prototype does not implement it. Across ten controlled AWS S3 scenarios, nine were reconstructed completely, no report contained an assertion untraceable to an observed artifact, and latency was four to five minutes. We also state what this evaluation does not establish and name the comparisons that would settle it.

</details>


### 159. HydroAgent: Formalizing Forecaster Expertise into Skill-Orchestrated Flood Forecasting Workflows

- **Authors:** Qingyi Yang, Siqian Qiu, Bing Li, Xu Shan, Jia Feng, Shunan Zhou, Xudong Zhou, Tiantian Xing, Jiale Guo, Xiaoyi Dong, Gaoyu Liu, Xiaohuan Liu, Haiqing Pu, Qingwen Deng, Xun Zhang, Zhongrun Xiang, Haiyang Qian, Ying Yan, Yongkang Xu, Nuo Lei, Tianlong Jia, Baoying Shan, Carlo De Michele
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.23983v1](http://arxiv.org/abs/2607.23983v1)
- **PDF:** [https://arxiv.org/pdf/2607.23983v1](https://arxiv.org/pdf/2607.23983v1)
- **Categories:** physics.geo-ph, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Operational flood forecasting depends on tacit forecaster expertise that is difficult to formalize, audit, and transfer. Although artificial intelligence methods have advanced flood prediction and model-error correction, most existing studies have not explicitly represented the tacit expert rules, review checkpoints, and workflow constraints that connect model outputs to operational warning decisions. To address this issue, we propose HydroAgent, a skill-orchestrated agent framework that embeds Large Language Models (LLMs) into a model-driven flood forecasting workflow, where each skill encodes explicit rules to bound LLM reasoning. We validated its effectiveness using five state-of-the-art LLMs in the South Yamhill River basin. Our results demonstrate that prior judgment captures observed peak flow and flood volume within 5% tolerance in 10 and 11 out of 14 events, with 5-fold cross-validation over 129 events yielding Pearson correlations of 0.62 and 0.84. Building on a high-baseline scheme library (average KGE 0.890), the guided scheme selection further improves KGE by 0.023-0.154, with simulated peak flow and flood volume falling within the prior judgment ranges for 14 and 13 out of 14 events. All five tested LLMs successfully execute the HydroAgent workflow with comparable judgment accuracy (40%-80%), while showing moderate performance variation and substantial cost differences. HydroAgent does not aim to replace human forecasters; instead, it translates their tacit expertise into an auditable and reproducible workflow, streamlining analytical steps and supporting more informed decision-making. This skill-orchestrated paradigm demonstrates how explicit rule boundaries can guide language model reasoning to complement physically based simulation in next-generation flood forecasting.

</details>


### 160. Moral Hazard in Multi-Agent Language Models

- **Authors:** Dane Malenfant
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.23982v2](http://arxiv.org/abs/2607.23982v2)
- **PDF:** [https://arxiv.org/pdf/2607.23982v2](https://arxiv.org/pdf/2607.23982v2)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperation can fail when socially valuable effort is costly, weakly observable, and mainly benefits others. Drawing on Holmström's team moral-hazard model, we introduce the Dialogue Moral Hazard Game, a controlled textual game that operationalizes this hidden-action structure for language agents. In each episode, an agent can preserve an immediate local reward or pay a query cost to reveal a hidden safety fact that primarily helps another agent's downstream decision. We evaluate seven open-weight language models and one frontier API model, decomposing behavior into query use, realized information transfer, local-reward preservation, unsafe choice, format validity, and team success. Base open-weight models commonly preserve local reward without team success or query without communicating information that changes the final decision. GPT-5.6 Sol reaches ceiling behavior in the primary setting, and autonomous sweeps respond strongly to query cost and team reward. In a 3,015-decision incentive-isolation experiment with scripted partners, its empirical query threshold tracks the Holmström-derived private-share boundary across nine query costs with mean absolute error 0.013. We then use supervised fine-tuning, RLOO, sequential SFT+RLOO, and GEPA prompt optimization as diagnostic update mechanisms where coverage permits. Their effects are heterogeneous: OLMo-7B shows the clearest mechanism-consistent weight-level improvement, whereas GEPA sometimes improves team success while reducing or eliminating costly queries. Thus, optimization can shift aggregate reward without recovering the intended cooperative mechanism, motivating evaluations that report mechanism-level behavior rather than team success alone.

</details>


### 161. SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving

- **Authors:** Yihui Zhang, Tianyu Wo, Jinghao Wang, Xiaoyang Sun, Menghao Zhang, Cangzhou Yuan, Li Li, Chunming Hu, Albert Y. Zomaya, Renyu Yang
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.23933v1](http://arxiv.org/abs/2607.23933v1)
- **PDF:** [https://arxiv.org/pdf/2607.23933v1](https://arxiv.org/pdf/2607.23933v1)
- **Categories:** cs.DC, cs.AI, cs.LG, cs.PF


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency. Persistent long-lived sandbox reservations incur excessive memory overhead at scale, while lazy on-demand instantiation generates severe cold-start penalties that degrade response performance under multi-tenant, multi-turn agent workloads. To resolve this dilemma, we present SpecBox, a runtime built around speculative sandbox preallocation tailored for dynamic LLM agent execution pipelines.
  At its core, SpecBox implements keyword matching and streaming semantic embedding to enable intent-driven sandbox prewarming, which identifies pending tool execution demands mid-LLM token generation and fully overlaps sandbox bootstrapping with model inference. To extend prewarming windows across sequential agent steps, the framework leverages context-aware stochastic prefetching atop a sandbox dependency graph to probabilistically forecast future sandbox switches ahead of execution. We complement these speculative mechanisms with two orthogonal optimizations: a semantic result cache that prunes redundant repeated sandbox invocations, and a dedicated out-of-band shared-memory transport plane that bypasses conventional network serialization to deliver zero-copy artifact transfers. Evaluated on high-concurrency multi-turn agent traces, our prototype demonstrates that SpecBox cuts P99 end-to-end latency by up to $2.9\times$ relative to the on-demand sandbox baseline, while slashing peak memory consumption by $45.9\%$ compared to permanently reserved sandbox deployments.

</details>


### 162. MemTX: Transactional Belief Commit for Stateful Agent Memory

- **Authors:** Xiaoyang Li, Yiqi Wang, Haohui Lu, Zhi Chen, Mo Li, Pingan Song, Mingkai Zheng, Taotao Cai
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.23929v2](http://arxiv.org/abs/2607.23929v2)
- **PDF:** [https://arxiv.org/pdf/2607.23929v2](https://arxiv.org/pdf/2607.23929v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects. Current agent memory systems treat every accepted write as immediately actionable truth, so a polluted tool result, a stale update, or a teammate's half-finished note can silently drive an irreversible action. We argue that a memory write is not a belief commit. We present MemTX, a transactional belief-commit protocol. Each record carries evidence, permissions, provenance, and validity. Writes are staged inside snapshot-isolated transactions and admitted by a validate-and-commit pipeline, irreversible tool calls are gated on in-flight belief state, and retracting a belief triggers typed cascading repair of its derived records and tool side effects. Two invariants, action-safety gating and cascade-repair completeness, are machine-checked by property-based testing and bounded exhaustive enumeration of 5.5 million protocol states, with zero violations. Across five backbones from three model families, MemTX leads all eight baselines with paired-McNemar significance on four backbones and statistically ties the best baseline on the fifth and strongest, while remaining the only method with zero downstream harm on every backbone. Backbone capability does not substitute for commit discipline.

</details>


### 163. SimBEV2X: A Large-Scale Dataset and Data Generation Tool for Multi-Task Vehicle-to-Everything Cooperative Perception

- **Authors:** Goodarz Mehr, Sepideh Gohari, Montasir Abbas, Azim Eskandarian
- **Published:** 2026-07-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.23910v1](http://arxiv.org/abs/2607.23910v1)
- **PDF:** [https://arxiv.org/pdf/2607.23910v1](https://arxiv.org/pdf/2607.23910v1)
- **Categories:** cs.CV, cs.LG, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative perception through vehicle-to-everything (V2X) communication can overcome the inherent physical limitations of individual autonomous vehicles, such as occlusions and limited sensor range. However, the development of robust V2X algorithms, particularly those relying on unified spatial representations like bird's-eye view (BEV) representation, is hampered by the lack of large-scale, multi-modal, multi-task datasets. Moreover, collecting and annotating a large set of synchronized, real-world multi-agent data is prohibitively expensive. This has resulted in a landscape where existing V2X datasets are notably limited in both size and scope. To overcome this, we introduce SimBEV2X, an advanced synthetic data generation tool built on the CARLA simulator. SimBEV2X automatically creates randomized driving scenarios to collect multi-modal sensor data alongside various types of ground truth including 3D bounding boxes with unique track IDs, HD map information, BEV segmentation maps, and semantic occupancy voxel grids from both vehicles and RSUs. We also present the SimBEV2X dataset, the largest V2X perception dataset to date. The dataset comprises 258 scenes, each involving up to 8 connected vehicles and up to 4 RSUs across a variety of road networks. The SimBEV2X dataset is an order of magnitude larger than existing V2X datasets and contains 102,200 frames, 588,520 lidar point clouds, more than 3 million images, over 27 million bounding boxes, and a comprehensive set of other annotations. Finally, we establish a strong baseline on the SimBEV2X dataset using CoopDet3D and propose CoBEVFusion, a novel architecture that combines CoopDet3D with fused axial attention (FAX) for context-aware multi-agent feature aggregation, resulting in superior performance. SimBEV2X, the SimBEV2X dataset, and CoBEVFusion are available at https://simbev2x.org and https://github.com/GoodarzMehr/SimBEV2X.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*