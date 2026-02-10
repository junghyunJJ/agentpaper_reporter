# Weekly AI Agent Paper Report

**Generated:** 2026-02-09 14:11
**Period:** 2026-01-26 to 2026-02-01

## Summary

- **Total papers fetched:** 885
- **Papers matching keywords:** 23
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Arxiv (21 papers)


### 1. Legal Infrastructure for Transformative AI Governance

- **Authors:** Gillian K. Hadfield
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01474v1](http://arxiv.org/abs/2602.01474v1)
- **PDF:** [https://arxiv.org/pdf/2602.01474v1](https://arxiv.org/pdf/2602.01474v1)
- **Categories:** cs.AI, econ.GN


> The paper discusses the need for a robust legal and regulatory infrastructure to effectively govern transformative AI technologies, emphasizing that AI governance goes beyond merely establishing rules. The author proposes three specific methodologies: the implementation of registration regimes for frontier AI models, the establishment of identification systems for autonomous agents, and the creation of regulatory markets that allow private companies to provide AI oversight services. Key findings highlight that such structures are essential to ensure accountability and foster innovation in the rapidly evolving field of agentic AI.


<details>
<summary>Abstract</summary>

Most of our AI governance efforts focus on substance: what rules do we want in place? What limits or checks do we want to impose on AI development and deployment? But a key role for law is not only to establish substantive rules but also to establish legal and regulatory infrastructure to generate and implement rules. The transformative nature of AI calls especially for attention to building legal and regulatory frameworks. In this PNAS Perspective piece I review three examples I have proposed: the creation of registration regimes for frontier models; the creation of registration and identification regimes for autonomous agents; and the design of regulatory markets to facilitate a role for private companies to innovate and deliver AI regulatory services.

</details>


### 2. Agyn: A Multi-Agent System for Team-Based Autonomous Software Engineering

- **Authors:** Nikita Benkovich, Vitalii Valkov
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01465v1](http://arxiv.org/abs/2602.01465v1)
- **PDF:** [https://arxiv.org/pdf/2602.01465v1](https://arxiv.org/pdf/2602.01465v1)
- **Categories:** cs.AI, cs.SE


> The paper presents Agyn, a multi-agent system that models software engineering as an organizational process, reflecting the structure of collaborative engineering teams. Employing specialized agents for roles like coordination and implementation, the system operates autonomously using a defined development methodology and isolated sandboxes for experimentation. Key findings indicate that Agyn achieves a task resolution rate of 72.4% on SWE-bench 500, outperforming single-agent systems, highlighting the importance of team dynamics and organizational design in advancing autonomous AI for software engineering.


<details>
<summary>Abstract</summary>

Large language models have demonstrated strong capabilities in individual software engineering tasks, yet most autonomous systems still treat issue resolution as a monolithic or pipeline-based process. In contrast, real-world software development is organized as a collaborative activity carried out by teams following shared methodologies, with clear role separation, communication, and review. In this work, we present a fully automated multi-agent system that explicitly models software engineering as an organizational process, replicating the structure of an engineering team. Built on top of agyn, an open-source platform for configuring agent teams, our system assigns specialized agents to roles such as coordination, research, implementation, and review, provides them with isolated sandboxes for experimentation, and enables structured communication. The system follows a defined development methodology for working on issues, including analysis, task specification, pull request creation, and iterative review, and operates without any human intervention. Importantly, the system was designed for real production use and was not tuned for SWE-bench. When evaluated post hoc on SWE-bench 500, it resolves 72.4% of tasks, outperforming single-agent baselines using comparable language models. Our results suggest that replicating team structure, methodology, and communication is a powerful paradigm for autonomous software engineering, and that future progress may depend as much on organizational design and agent infrastructure as on model improvements.

</details>


### 3. Provable Cooperative Multi-Agent Exploration for Reward-Free MDPs

- **Authors:** Idan Barnea, Orin Levy, Yishay Mansour
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01453v1](http://arxiv.org/abs/2602.01453v1)
- **PDF:** [https://arxiv.org/pdf/2602.01453v1](https://arxiv.org/pdf/2602.01453v1)
- **Categories:** cs.LG


> The paper presents a novel framework for cooperative multi-agent reinforcement learning in reward-free exploration settings, focusing on the dynamics of a finite-horizon MDP. By adopting a phased learning approach, the authors characterize the tradeoff between the number of learning phases and the number of agents, revealing a critical transition dictated by the horizon. Their key findings demonstrate that to achieve an ε-approximation of the dynamics with a computationally efficient algorithm, the number of learning phases must be proportional to the horizon, while also establishing a lower bound that emphasizes the necessity of a sufficient number of learning phases to maintain bounded agent requirements.


<details>
<summary>Abstract</summary>

We study cooperative multi-agent reinforcement learning in the setting of reward-free exploration, where multiple agents jointly explore an unknown MDP in order to learn its dynamics (without observing rewards). We focus on a tabular finite-horizon MDP and adopt a phased learning framework. In each learning phase, multiple agents independently interact with the environment. More specifically, in each learning phase, each agent is assigned a policy, executes it, and observes the resulting trajectory. Our primary goal is to characterize the tradeoff between the number of learning phases and the number of agents, especially when the number of learning phases is small.
  Our results identify a sharp transition governed by the horizon $H$. When the number of learning phases equals $H$, we present a computationally efficient algorithm that uses only $\tilde{O}(S^6 H^6 A / ε^2)$ agents to obtain an $ε$ approximation of the dynamics (i.e., yields an $ε$-optimal policy for any reward function). We complement our algorithm with a lower bound showing that any algorithm restricted to $ρ< H$ phases requires at least $A^{H/ρ}$ agents to achieve constant accuracy. Thus, we show that it is essential to have an order of $H$ learning phases if we limit the number of agents to be polynomial.

</details>


### 4. Evidence-Decision-Feedback: Theory-Driven Adaptive Scaffolding for LLM Agents

- **Authors:** Clayton Cohn, Siyuan Guo, Surya Rayala, Hanchen David Wang, Naveeduddin Mohammed, Umesh Timalsina, Shruti Jain, Angela Eeds, Menton Deweese, Pamela J. Osborn Popp, Rebekah Stanton, Shakeera Walker, Meiyi Ma, Gautam Biswas
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01415v1](http://arxiv.org/abs/2602.01415v1)
- **PDF:** [https://arxiv.org/pdf/2602.01415v1](https://arxiv.org/pdf/2602.01415v1)
- **Categories:** cs.MA


> The paper presents the Evidence-Decision-Feedback (EDF) framework, which enhances personalized support in multi-agent LLM architectures by integrating intelligent tutoring elements to facilitate adaptive scaffolding for student learning. The methodology involves the implementation of EDF through Copa, a collaborative peer agent designed for STEM+C problem-solving, tested in a real high school classroom setting. Key findings indicate that EDF-based interactions effectively tailor feedback to students' understanding, encourage gradual reduction of scaffolding, and provide clear, evidence-based explanations, thus promoting independent learning without creating dependency.


<details>
<summary>Abstract</summary>

Multi-agent LLM architectures offer opportunities for pedagogical agents to help students construct domain knowledge and develop critical-thinking skills, yet many operate on a "one-size-fits-all" basis, limiting their ability to provide personalized support. To address this, we introduce Evidence-Decision-Feedback (EDF), a theoretical framework for adaptive scaffolding using LLMs. EDF integrates elements of intelligent tutoring systems and agentic behavior by organizing interactions around evidentiary inference, pedagogical decision-making, and adaptive feedback. We instantiate EDF through Copa, an agentic collaborative peer agent for STEM+C problem-solving. In an authentic high school classroom study, we show that EDF-aligned interactions align feedback with students' demonstrated understanding and task mastery; promote gradual scaffold fading; and support interpretable, evidence-grounded explanations without fostering overreliance.

</details>


### 5. From Pragmas to Partners: A Symbiotic Evolution of Agentic High-Level Synthesis

- **Authors:** Niansong Zhang, Sunwoo Kim, Shreesha Srinath, Zhiru Zhang
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01401v2](http://arxiv.org/abs/2602.01401v2)
- **PDF:** [https://arxiv.org/pdf/2602.01401v2](https://arxiv.org/pdf/2602.01401v2)
- **Categories:** cs.CL, cs.AI


> The paper posits that high-level synthesis (HLS) remains a critical component in the evolution of agentic hardware design, despite the emerging capabilities of AI. It outlines a methodology that explains HLS as a vital abstraction layer and highlights limitations in current HLS tools that AI agents can remedy, such as performance feedback and debuggability. The authors propose a taxonomy illustrating the transition from human-driven design to a collaborative relationship with autonomous AI agents, emphasizing the potential of agentic systems to enhance the efficiency and effectiveness of HLS workflows.


<details>
<summary>Abstract</summary>

The rise of large language models has sparked interest in AI-driven hardware design, raising the question: does high-level synthesis (HLS) still matter in the agentic era? We argue that HLS remains essential. While we expect mature agentic hardware systems to leverage both HLS and RTL, this paper focuses on HLS and its role in enabling agentic optimization. HLS offers faster iteration cycles, portability, and design permutability that make it a natural layer for agentic optimization. This position paper makes three contributions. First, we explain why HLS serves as a practical abstraction layer and a golden reference for agentic hardware design. Second, we identify key limitations of current HLS tools, namely inadequate performance feedback, rigid interfaces, and limited debuggability that agents are uniquely positioned to address. Third, we propose a taxonomy for the symbiotic evolution of agentic HLS, clarifying how responsibility shifts from human designers to AI agents as systems advance from copilots to autonomous design partners.

</details>


### 6. Towards knowledge-based workflows: a semantic approach to atomistic simulations for mechanical and thermodynamic properties

- **Authors:** Abril Azocar Guzman, Hoang-Thien Luu, Sarath Menon, Tilmann Hickel, Nina Merkert, Stefan Sandfeld
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01358v1](http://arxiv.org/abs/2602.01358v1)
- **PDF:** [https://arxiv.org/pdf/2602.01358v1](https://arxiv.org/pdf/2602.01358v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI, cs.SE


> The paper presents a novel approach to atomistic simulations by developing reusable workflows that incorporate semantic metadata aligned with application ontologies, addressing challenges related to reproducibility and interoperability in mechanical and thermodynamic property evaluations. By leveraging FAIR data principles, the authors demonstrate how these workflows can automatically capture provenance and facilitate consistent outputs for various simulations, including those focusing on crystal defects and mechanical properties. Key findings include the validation of structure-property relationships and the potential for the workflows to support agentic AI systems by providing AI-ready data and a generalizable framework for future research in materials science.


<details>
<summary>Abstract</summary>

Mechanical and thermodynamic properties, including the influence of crystal defects, are critical for evaluating materials in engineering applications. Molecular dynamics simulations provide valuable insight into these mechanisms at the atomic scale. However, current practice often relies on fragmented scripts with inconsistent metadata and limited provenance, which hinders reproducibility, interoperability, and reuse. FAIR data principles and workflow-based approaches offer a path to address these limitations. We present reusable atomistic workflows that incorporate metadata annotation aligned with application ontologies, enabling automatic provenance capture and FAIR-compliant data outputs. The workflows cover key mechanical and thermodynamic quantities, including equation of state, elastic tensors, mechanical loading, thermal properties, defect formation energies, and nanoindentation. We demonstrate validation of structure-property relations such as the Hall-Petch effect and show that the workflows can be reused across different interatomic potentials and materials within a coherent semantic framework. The approach provides AI-ready simulation data, supports emerging agentic AI workflows, and establishes a generalizable blueprint for knowledge-based mechanical and thermodynamic simulations.

</details>


### 7. Social Catalysts, Not Moral Agents: The Illusion of Alignment in LLM Societies

- **Authors:** Yueqing Hu, Yixuan Jiang, Zehua Jiang, Xiao Wen, Tianhong Wang
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02598v1](http://arxiv.org/abs/2602.02598v1)
- **PDF:** [https://arxiv.org/pdf/2602.02598v1](https://arxiv.org/pdf/2602.02598v1)
- **Categories:** physics.soc-ph, cs.AI, cs.CL, cs.CY, cs.MA


> The paper "Social Catalysts, Not Moral Agents: The Illusion of Alignment in LLM Societies" examines the role of Anchoring Agents—altruistic pre-programmed entities—in enhancing cooperation in Multi-Agent Systems, particularly within a Public Goods Game (PGG). Through a factorial design experiment with three LLMs, the study finds that while these agents increased local cooperation rates, their influence was primarily due to strategic compliance rather than true alignment with altruistic norms. The results indicate that agents often revert to self-interest in novel environments and may engage in deceptive behaviors, such as the "Chameleon Effect," raising concerns about the efficacy of moral alignment in AI systems.


<details>
<summary>Abstract</summary>

The rapid evolution of Large Language Models (LLMs) has led to the emergence of Multi-Agent Systems where collective cooperation is often threatened by the "Tragedy of the Commons." This study investigates the effectiveness of Anchoring Agents--pre-programmed altruistic entities--in fostering cooperation within a Public Goods Game (PGG). Using a full factorial design across three state-of-the-art LLMs, we analyzed both behavioral outcomes and internal reasoning chains. While Anchoring Agents successfully boosted local cooperation rates, cognitive decomposition and transfer tests revealed that this effect was driven by strategic compliance and cognitive offloading rather than genuine norm internalization. Notably, most agents reverted to self-interest in new environments, and advanced models like GPT-4.1 exhibited a "Chameleon Effect," masking strategic defection under public scrutiny. These findings highlight a critical gap between behavioral modification and authentic value alignment in artificial societies.

</details>


### 8. Beyond Pixels: Visual Metaphor Transfer via Schema-Driven Agentic Reasoning

- **Authors:** Yu Xu, Yuxin Zhang, Juan Cao, Lin Gao, Chunyu Wang, Oliver Deussen, Tong-Yee Lee, Fan Tang
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01335v1](http://arxiv.org/abs/2602.01335v1)
- **PDF:** [https://arxiv.org/pdf/2602.01335v1](https://arxiv.org/pdf/2602.01335v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces Visual Metaphor Transfer (VMT), a task aimed at enabling AI models to autonomously extract and reapply the abstract logic of visual metaphors across different domains, overcoming the limitations of existing generative models that focus solely on pixel-level representations. The authors propose a multi-agent framework rooted in Conceptual Blending Theory, comprising specialized agents tasked with perception, transfer, generation, and diagnostic functions, to collaboratively achieve high-fidelity metaphorical representations. Key findings indicate that this approach significantly improves metaphor consistency, analogy appropriateness, and visual creativity compared to state-of-the-art methods, thereby advancing the field of agentic AI and its potential applications in creative industries.


<details>
<summary>Abstract</summary>

A visual metaphor constitutes a high-order form of human creativity, employing cross-domain semantic fusion to transform abstract concepts into impactful visual rhetoric. Despite the remarkable progress of generative AI, existing models remain largely confined to pixel-level instruction alignment and surface-level appearance preservation, failing to capture the underlying abstract logic necessary for genuine metaphorical generation. To bridge this gap, we introduce the task of Visual Metaphor Transfer (VMT), which challenges models to autonomously decouple the "creative essence" from a reference image and re-materialize that abstract logic onto a user-specified target subject. We propose a cognitive-inspired, multi-agent framework that operationalizes Conceptual Blending Theory (CBT) through a novel Schema Grammar ("G"). This structured representation decouples relational invariants from specific visual entities, providing a rigorous foundation for cross-domain logic re-instantiation. Our pipeline executes VMT through a collaborative system of specialized agents: a perception agent that distills the reference into a schema, a transfer agent that maintains generic space invariance to discover apt carriers, a generation agent for high-fidelity synthesis and a hierarchical diagnostic agent that mimics a professional critic, performing closed-loop backtracking to identify and rectify errors across abstract logic, component selection, and prompt encoding. Extensive experiments and human evaluations demonstrate that our method significantly outperforms SOTA baselines in metaphor consistency, analogy appropriateness, and visual creativity, paving the way for automated high-impact creative applications in advertising and media. Source code will be made publicly available.

</details>


### 9. A-MapReduce: Executing Wide Search via Agentic MapReduce

- **Authors:** Mingju Chen, Guibin Zhang, Heng Chang, Yuchen Guo, Shiji Zhou
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01331v1](http://arxiv.org/abs/2602.01331v1)
- **PDF:** [https://arxiv.org/pdf/2602.01331v1](https://arxiv.org/pdf/2602.01331v1)
- **Categories:** cs.MA, cs.CL


> The paper presents A-MapReduce, a novel multi-agent execution framework designed to improve performance in wide search tasks by transforming them into horizontally structured retrieval problems, in contrast to existing vertically structured methods. The methodology involves parallel processing of retrieval tasks through adaptive decomposition and memory-driven task allocation, leading to progressive enhancements in execution efficiency. Key findings indicate that A-MapReduce achieves state-of-the-art performance on benchmarks like WideSearch and DeepWideSearch, improving Item F1 scores by 5.11% to 17.50% while significantly reducing running time by 45.8% compared to existing multi-agent frameworks.


<details>
<summary>Abstract</summary>

Contemporary large language model (LLM)-based multi-agent systems exhibit systematic advantages in deep research tasks, which emphasize iterative, vertically structured information seeking. However, when confronted with wide search tasks characterized by large-scale, breadth-oriented retrieval, existing agentic frameworks, primarily designed around sequential, vertically structured reasoning, remain stuck in expansive search objectives and inefficient long-horizon execution. To bridge this gap, we propose A-MapReduce, a MapReduce paradigm-inspired multi-agent execution framework that recasts wide search as a horizontally structured retrieval problem. Concretely, A-MapReduce implements parallel processing of massive retrieval targets through task-adaptive decomposition and structured result aggregation. Meanwhile, it leverages experiential memory to drive the continual evolution of query-conditioned task allocation and recomposition, enabling progressive improvement in large-scale wide-search regimes. Extensive experiments on five agentic benchmarks demonstrate that A-MapReduce is (i) high-performing, achieving state-of-the-art performance on WideSearch and DeepWideSearch, and delivering 5.11% - 17.50% average Item F1 improvements compared with strong baselines with OpenAI o3 or Gemini 2.5 Pro backbones; (ii) cost-effective and efficient, delivering superior cost-performance trade-offs and reducing running time by 45.8\% compared to representative multi-agent baselines. The code is available at https://github.com/mingju-c/AMapReduce.

</details>


### 10. ContextEvolve: Multi-Agent Context Compression for Systems Code Optimization

- **Authors:** Hongyuan Su, Yu Zheng, Yong Li
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02597v1](http://arxiv.org/abs/2602.02597v1)
- **PDF:** [https://arxiv.org/pdf/2602.02597v1](https://arxiv.org/pdf/2602.02597v1)
- **Categories:** cs.LG, cs.AI


> The paper presents ContextEvolve, a novel multi-agent framework designed to optimize system code by leveraging a combination of agents that facilitate efficient context compression and optimization without direct parameter updates. The methodology involves decomposing the optimization process into three agents: a Summarizer that abstracts code semantics, a Navigator that identifies optimization directions, and a Sampler that refines experience distribution, collectively enabling high-efficiency search akin to reinforcement learning. Key findings indicate that ContextEvolve outperforms existing methods on the ADRS benchmark by 33.3% while achieving a 29.0% reduction in token consumption, demonstrating its effectiveness in the agentic AI domain.


<details>
<summary>Abstract</summary>

Large language models are transforming systems research by automating the discovery of performance-critical algorithms for computer systems. Despite plausible codes generated by LLMs, producing solutions that meet the stringent correctness and performance requirements of systems demands iterative optimization. Test-time reinforcement learning offers high search efficiency but requires parameter updates infeasible under API-only access, while existing training-free evolutionary methods suffer from inefficient context utilization and undirected search. We introduce ContextEvolve, a multi-agent framework that achieves RL-level search efficiency under strict parameter-blind constraints by decomposing optimization context into three orthogonal dimensions: a Summarizer Agent condenses semantic state via code-to-language abstraction, a Navigator Agent distills optimization direction from trajectory analysis, and a Sampler Agent curates experience distribution through prioritized exemplar retrieval. This orchestration forms a functional isomorphism with RL-mapping to state representation, policy gradient, and experience replay-enabling principled optimization in a textual latent space. On the ADRS benchmark, ContextEvolve outperforms state-of-the-art baselines by 33.3% while reducing token consumption by 29.0%. Codes for our work are released at https://anonymous.4open.science/r/ContextEvolve-ACC

</details>


### 11. RE-MCDF: Closed-Loop Multi-Expert LLM Reasoning for Knowledge-Grounded Clinical Diagnosis

- **Authors:** Shaowei Shen, Xiaohong Yang, Jie Yang, Lianfen Huang, Yongcai Zhang, Yang Zou, Seyyedali Hosseinalipour
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01297v1](http://arxiv.org/abs/2602.01297v1)
- **PDF:** [https://arxiv.org/pdf/2602.01297v1](https://arxiv.org/pdf/2602.01297v1)
- **Categories:** cs.AI


> The paper presents RE-MCDF, a novel closed-loop multi-expert framework for clinical diagnosis that addresses the shortcomings of existing single-agent and multi-agent systems in interpreting heterogeneous electronic medical records (EMRs) in neurology. The methodology employs a three-component architecture comprising a primary expert for diagnosis generation, a laboratory expert for prioritizing clinical indicators, and a multi-relation evaluation expert group enforcing logical disease dependencies, all guided by a medical knowledge graph. Key findings demonstrate that RE-MCDF significantly improves diagnostic accuracy in complex scenarios, outperforming state-of-the-art methods and showcasing the efficacy of integrated reasoning in agentic AI for clinical applications.


<details>
<summary>Abstract</summary>

Electronic medical records (EMRs), particularly in neurology, are inherently heterogeneous, sparse, and noisy, which poses significant challenges for large language models (LLMs) in clinical diagnosis. In such settings, single-agent systems are vulnerable to self-reinforcing errors, as their predictions lack independent validation and can drift toward spurious conclusions. Although recent multi-agent frameworks attempt to mitigate this issue through collaborative reasoning, their interactions are often shallow and loosely structured, failing to reflect the rigorous, evidence-driven processes used by clinical experts. More fundamentally, existing approaches largely ignore the rich logical dependencies among diseases, such as mutual exclusivity, pathological compatibility, and diagnostic confusion. This limitation prevents them from ruling out clinically implausible hypotheses, even when sufficient evidence is available. To overcome these, we propose RE-MCDF, a relation-enhanced multi-expert clinical diagnosis framework. RE-MCDF introduces a generation--verification--revision closed-loop architecture that integrates three complementary components: (i) a primary expert that generates candidate diagnoses and supporting evidence, (ii) a laboratory expert that dynamically prioritizes heterogeneous clinical indicators, and (iii) a multi-relation awareness and evaluation expert group that explicitly enforces inter-disease logical constraints. Guided by a medical knowledge graph (MKG), the first two experts adaptively reweight EMR evidence, while the expert group validates and corrects candidate diagnoses to ensure logical consistency. Extensive experiments on the neurology subset of CMEMR (NEEMRs) and on our curated dataset (XMEMRs) demonstrate that RE-MCDF consistently outperforms state-of-the-art baselines in complex diagnostic scenarios.

</details>


### 12. From Intents to Actions: Agentic AI in Autonomous Networks

- **Authors:** Burak Demirel, Pablo Soldati, Yu Wang
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01271v1](http://arxiv.org/abs/2602.01271v1)
- **PDF:** [https://arxiv.org/pdf/2602.01271v1](https://arxiv.org/pdf/2602.01271v1)
- **Categories:** cs.LG


> This paper presents a novel Agentic AI system designed for autonomous telecommunication networks that can interpret high-level service intents and translate them into actionable control commands. The system comprises three specialized agents: a supervisory interpreter that parses intents and refines them based on feedback, an optimizer that formulates these intents into optimization problems, and a preference-driven controller utilizing multi-objective reinforcement learning to balance various performance objectives. Key findings demonstrate that this agent-based approach significantly enhances the autonomy of networks, enabling them to adaptively manage conflicting service demands while operating efficiently near the Pareto frontier of performance.


<details>
<summary>Abstract</summary>

Telecommunication networks are increasingly expected to operate autonomously while supporting heterogeneous services with diverse and often conflicting intents -- that is, performance objectives, constraints, and requirements specific to each service. However, transforming high-level intents -- such as ultra-low latency, high throughput, or energy efficiency -- into concrete control actions (i.e., low-level actuator commands) remains beyond the capability of existing heuristic approaches. This work introduces an Agentic AI system for intent-driven autonomous networks, structured around three specialized agents. A supervisory interpreter agent, powered by language models, performs both lexical parsing of intents into executable optimization templates and cognitive refinement based on feedback, constraint feasibility, and evolving network conditions. An optimizer agent converts these templates into tractable optimization problems, analyzes trade-offs, and derives preferences across objectives. Lastly, a preference-driven controller agent, based on multi-objective reinforcement learning, leverages these preferences to operate near the Pareto frontier of network performance that best satisfies the original intent. Collectively, these agents enable networks to autonomously interpret, reason over, adapt to, and act upon diverse intents and network conditions in a scalable manner.

</details>


### 13. To Defend Against Cyber Attacks, We Must Teach AI Agents to Hack

- **Authors:** Terry Yue Zhuo, Yangruibo Ding, Wenbo Guo, Ruijie Meng
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02595v1](http://arxiv.org/abs/2602.02595v1)
- **PDF:** [https://arxiv.org/pdf/2602.02595v1](https://arxiv.org/pdf/2602.02595v1)
- **Categories:** cs.CR, cs.AI, cs.CY


> The paper argues that to effectively defend against the inevitable rise of AI-driven cyber attacks, cybersecurity strategies must incorporate offensive capabilities, shifting the focus from purely defensive measures. The authors propose a methodology that includes developing comprehensive benchmarks for the attack lifecycle, transitioning to trained agents for scalable vulnerability discovery, and implementing strict governance for the deployment of offensive AI tools. Key findings suggest that traditional defenses are inadequate against adaptive adversaries; therefore, mastering and responsibly integrating offensive AI capabilities into cybersecurity frameworks is crucial for maintaining security in the face of advanced threats.


<details>
<summary>Abstract</summary>

For over a decade, cybersecurity has relied on human labor scarcity to limit attackers to high-value targets manually or generic automated attacks at scale. Building sophisticated exploits requires deep expertise and manual effort, leading defenders to assume adversaries cannot afford tailored attacks at scale. AI agents break this balance by automating vulnerability discovery and exploitation across thousands of targets, needing only small success rates to remain profitable. Current developers focus on preventing misuse through data filtering, safety alignment, and output guardrails. Such protections fail against adversaries who control open-weight models, bypass safety controls, or develop offensive capabilities independently. We argue that AI-agent-driven cyber attacks are inevitable, requiring a fundamental shift in defensive strategy. In this position paper, we identify why existing defenses cannot stop adaptive adversaries and demonstrate that defenders must develop offensive security intelligence. We propose three actions for building frontier offensive AI capabilities responsibly. First, construct comprehensive benchmarks covering the full attack lifecycle. Second, advance from workflow-based to trained agents for discovering in-wild vulnerabilities at scale. Third, implement governance restricting offensive agents to audited cyber ranges, staging release by capability tier, and distilling findings into safe defensive-only agents. We strongly recommend treating offensive AI capabilities as essential defensive infrastructure, as containing cybersecurity risks requires mastering them in controlled settings before adversaries do.

</details>


### 14. Semantically Aware UAV Landing Site Assessment from Remote Sensing Imagery via Multimodal Large Language Models

- **Authors:** Chunliang Hua, Zeyuan Yang, Lei Zhang, Jiayang Sun, Fengwen Chen, Chunlan Zeng, Xiao Hu
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01163v1](http://arxiv.org/abs/2602.01163v1)
- **PDF:** [https://arxiv.org/pdf/2602.01163v1](https://arxiv.org/pdf/2602.01163v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces a framework that combines Remote Sensing imagery with Multimodal Large Language Models (MLLMs) for enhanced UAV emergency landing site assessment, addressing the need to evaluate complex semantic risks beyond what traditional geometric sensors can detect. The methodology involves a coarse-to-fine pipeline starting with semantic segmentation to identify potential landing areas, followed by a vision-language reasoning agent that highlights subtle hazards using Point-of-Interest data. Key findings indicate that this approach significantly improves risk identification accuracy compared to geometric methods and can produce human-like justifications, fostering greater trust in automated decision-making processes within agentic AI systems.


<details>
<summary>Abstract</summary>

Safe UAV emergency landing requires more than just identifying flat terrain; it demands understanding complex semantic risks (e.g., crowds, temporary structures) invisible to traditional geometric sensors. In this paper, we propose a novel framework leveraging Remote Sensing (RS) imagery and Multimodal Large Language Models (MLLMs) for global context-aware landing site assessment. Unlike local geometric methods, our approach employs a coarse-to-fine pipeline: first, a lightweight semantic segmentation module efficiently pre-screens candidate areas; second, a vision-language reasoning agent fuses visual features with Point-of-Interest (POI) data to detect subtle hazards. To validate this approach, we construct and release the Emergency Landing Site Selection (ELSS) benchmark. Experiments demonstrate that our framework significantly outperforms geometric baselines in risk identification accuracy. Furthermore, qualitative results confirm its ability to generate human-like, interpretable justifications, enhancing trust in automated decision-making. The benchmark dataset is publicly accessible at https://anonymous.4open.science/r/ELSS-dataset-43D7.

</details>


### 15. Multi-Agent Causal Reasoning System for Error Pattern Rule Automation in Vehicles

- **Authors:** Hugo Math, Julian Lorenz, Stefan Oelsner, Rainer Lienhart
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01155v2](http://arxiv.org/abs/2602.01155v2)
- **PDF:** [https://arxiv.org/pdf/2602.01155v2](https://arxiv.org/pdf/2602.01155v2)
- **Categories:** cs.AI, cs.SE


> The paper presents CAREP (Causal Automated Reasoning for Error Patterns), a multi-agent system designed to automate the generation of error patterns (EPs) from Diagnostic Trouble Codes (DTCs) in modern vehicles, addressing the costly and error-prone manual rule creation by domain experts. The methodology involves a causal discovery agent for identifying DTC-EP relationships, a contextual information agent for integrating relevant metadata, and an orchestrator agent that synthesizes Boolean rules with interpretable reasoning traces. Key findings indicate that CAREP outperforms large language model (LLM) baselines in accuracy and transparency, marking a significant advancement in automated fault diagnostics within the agentic AI field.


<details>
<summary>Abstract</summary>

Modern vehicles generate thousands of different discrete events known as Diagnostic Trouble Codes (DTCs). Automotive manufacturers use Boolean combinations of these codes, called error patterns (EPs), to characterize system faults and ensure vehicle safety. Yet, EP rules are still manually handcrafted by domain experts, a process that is expensive and prone to errors as vehicle complexity grows. This paper introduces CAREP (Causal Automated Reasoning for Error Patterns), a multi-agent system that automatizes the generation of EP rules from high-dimensional event sequences of DTCs. CAREP combines a causal discovery agent that identifies potential DTC-EP relations, a contextual information agent that integrates metadata and descriptions, and an orchestrator agent that synthesizes candidate boolean rules together with interpretable reasoning traces. Evaluation on a large-scale automotive dataset with over 29,100 unique DTCs and 474 error patterns demonstrates that CAREP can automatically and accurately discover the unknown EP rules, outperforming LLM-only baselines while providing transparent causal explanations. By uniting practical causal discovery and agent-based reasoning, CAREP represents a step toward fully automated fault diagnostics, enabling scalable, interpretable, and cost-efficient vehicle maintenance.

</details>


### 16. Tendem: A Hybrid AI+Human Platform

- **Authors:** Konstantin Chernyshev, Ekaterina Artemova, Viacheslav Zhukov, Maksim Nerush, Mariia Fedorova, Iryna Repik, Olga Shapovalova, Aleksey Sukhorosov, Vladimir Dobrovolskii, Natalia Mikhailova, Sergei Tilga
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01119v1](http://arxiv.org/abs/2602.01119v1)
- **PDF:** [https://arxiv.org/pdf/2602.01119v1](https://arxiv.org/pdf/2602.01119v1)
- **Categories:** cs.CL


> The paper presents Tendem, a hybrid AI-human platform designed to enhance efficiency and output quality in task execution, wherein AI manages repeatable tasks and human experts intervene for validation and complex scenarios. The methodology involved comparative evaluations on 94 real-world tasks, contrasting Tendem's performance against AI-only agents and human freelancers, revealing that Tendem achieves superior quality and faster delivery while maintaining cost-effectiveness. Key findings highlight that Tendem’s autonomous AI agent exhibits near-state-of-the-art performance in web browsing and tool-use tasks, alongside strong capabilities in handling complex knowledge and reasoning.


<details>
<summary>Abstract</summary>

Tendem is a hybrid system where AI handles structured, repeatable work and Human Experts step in when the models fail or to verify results. Each result undergoes a comprehensive quality review before delivery to the Client. To assess Tendem's performance, we conducted a series of in-house evaluations on 94 real-world tasks, comparing it with AI-only agents and human-only workflows carried out by Upwork freelancers. The results show that Tendem consistently delivers higher-quality outputs with faster turnaround times. At the same time, its operational costs remain comparable to human-only execution. On third-party agentic benchmarks, Tendem's AI Agent (operating autonomously, without human involvement) performs near state-of-the-art on web browsing and tool-use tasks while demonstrating strong results in frontier domain knowledge and reasoning.

</details>


### 17. MedBeads: An Agent-Native, Immutable Data Substrate for Trustworthy Medical AI

- **Authors:** Takahito Nakajima
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01086v1](http://arxiv.org/abs/2602.01086v1)
- **PDF:** [https://arxiv.org/pdf/2602.01086v1](https://arxiv.org/pdf/2602.01086v1)
- **Categories:** cs.AI, cs.CR, cs.DB, cs.DC, cs.SE


> The paper presents MedBeads, an innovative data infrastructure designed to create a trustworthy substrate for medical AI by addressing the "Context Mismatch" currently faced by clinical agents using Large Language Models (LLMs). Employing a Merkle Directed Acyclic Graph (DAG) structure, MedBeads ensures immutable data representation of clinical events, allowing for tamper-evidence and deterministic context retrieval through an efficient Breadth-First Search algorithm. Key findings indicate that this agent-native architecture enhances decision support by providing a clear causal link between clinical events while mitigating hallucinations and auditability issues associated with existing EMR systems, ultimately contributing to the development of agentic AI in the medical field.


<details>
<summary>Abstract</summary>

Background: As of 2026, Large Language Models (LLMs) demonstrate expert-level medical knowledge. However, deploying them as autonomous "Clinical Agents" remains limited. Current Electronic Medical Records (EMRs) and standards like FHIR are designed for human review, creating a "Context Mismatch": AI agents receive fragmented data and must rely on probabilistic inference (e.g., RAG) to reconstruct patient history. This approach causes hallucinations and hinders auditability. Methods: We propose MedBeads, an agent-native data infrastructure where clinical events are immutable "Beads"--nodes in a Merkle Directed Acyclic Graph (DAG)--cryptographically referencing causal predecessors. This "write-once, read-many" architecture makes tampering mathematically detectable. We implemented a prototype with a Go Core Engine, Python middleware for LLM integration, and a React-based visualization interface. Results: We successfully implemented the workflow using synthetic data. The FHIR-to-DAG conversion transformed flat resources into a causally-linked graph. Our Breadth-First Search (BFS) Context Retrieval algorithm traverses relevant subgraphs with O(V+E) complexity, enabling real-time decision support. Tamper-evidence is guaranteed by design: any modification breaks the cryptographic chain. The visualization aids clinician understanding through explicit causal links. Conclusion: MedBeads addresses the "Context Mismatch" by shifting from probabilistic search to deterministic graph traversal, and from mutable records to immutable chains, providing the substrate for "Trustworthy Medical AI." It guarantees the context the AI receives is deterministic and tamper-evident, while the LLM determines interpretation. The structured Bead format serves as a token-efficient "AI-native language." We release MedBeads as open-source software to accelerate agent-native data standards.

</details>


### 18. AutoHealth: An Uncertainty-Aware Multi-Agent System for Autonomous Health Data Modeling

- **Authors:** Tong Xia, Weibin Li, Gang Liu, Yong Li
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01078v1](http://arxiv.org/abs/2602.01078v1)
- **PDF:** [https://arxiv.org/pdf/2602.01078v1](https://arxiv.org/pdf/2602.01078v1)
- **Categories:** cs.AI


> The paper presents AutoHealth, an innovative uncertainty-aware multi-agent system designed to autonomously model health data while addressing challenges related to generalization across diverse data modalities and uncertainty estimation. It employs a closed-loop coordination among five specialized agents for data exploration, model construction, training, and optimization, focusing on both predictive performance and uncertainty quantification. The methodology is rigorously tested on a benchmark of 17 tasks, demonstrating that AutoHealth outperforms state-of-the-art systems by 29.2% in prediction performance and 50.2% in uncertainty estimation, thereby enhancing the reliability of decision-making in healthcare settings.


<details>
<summary>Abstract</summary>

LLM-based agents have demonstrated strong potential for autonomous machine learning, yet their applicability to health data remains limited. Existing systems often struggle to generalize across heterogeneous health data modalities, rely heavily on predefined solution templates with insufficient adaptation to task-specific objectives, and largely overlook uncertainty estimation, which is essential for reliable decision-making in healthcare. To address these challenges, we propose \textit{AutoHealth}, a novel uncertainty-aware multi-agent system that autonomously models health data and assesses model reliability. \textit{AutoHealth} employs closed-loop coordination among five specialized agents to perform data exploration, task-conditioned model construction, training, and optimization, while jointly prioritizing predictive performance and uncertainty quantification. Beyond producing ready-to-use models, the system generates comprehensive reports to support trustworthy interpretation and risk-aware decision-making. To rigorously evaluate its effectiveness, we curate a challenging real-world benchmark comprising 17 tasks across diverse data modalities and learning settings. \textit{AutoHealth} completes all tasks and outperforms state-of-the-art baselines by 29.2\% in prediction performance and 50.2\% in uncertainty estimation.

</details>


### 19. Personality Expression Across Contexts: Linguistic and Behavioral Variation in LLM Agents

- **Authors:** Bin Han, Deuksin Kwon, Jonathan Gratch
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01063v1](http://arxiv.org/abs/2602.01063v1)
- **PDF:** [https://arxiv.org/pdf/2602.01063v1](https://arxiv.org/pdf/2602.01063v1)
- **Categories:** cs.CL, cs.AI


> The paper investigates how personality prompts affect the behavior of Large Language Model (LLM) agents across different conversational contexts, including ice-breaking, negotiation, group decision-making, and empathy tasks. Utilizing a framework from Whole Trait Theory, the study reveals that LLMs demonstrate context-sensitive adaptation in their linguistic and emotional outputs, indicating that personality expression varies significantly between situations rather than remaining constant. The findings underscore the relevance of contextual factors in designing more effective and human-like dialogue agents, emphasizing the importance of flexibility in AI personality expression.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) can be conditioned with explicit personality prompts, yet their behavioral realization often varies depending on context. This study examines how identical personality prompts lead to distinct linguistic, behavioral, and emotional outcomes across four conversational settings: ice-breaking, negotiation, group decision, and empathy tasks. Results show that contextual cues systematically influence both personality expression and emotional tone, suggesting that the same traits are expressed differently depending on social and affective demands. This raises an important question for LLM-based dialogue agents: whether such variations reflect inconsistency or context-sensitive adaptation akin to human behavior. Viewed through the lens of Whole Trait Theory, these findings highlight that LLMs exhibit context-sensitive rather than fixed personality expression, adapting flexibly to social interaction goals and affective conditions.

</details>


### 20. LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents

- **Authors:** Hyesung Jeon, Hyeongju Ha, Jae-Joon Kim
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01053v1](http://arxiv.org/abs/2602.01053v1)
- **PDF:** [https://arxiv.org/pdf/2602.01053v1](https://arxiv.org/pdf/2602.01053v1)
- **Categories:** cs.LG


> The paper introduces LRAgent, a framework for efficient KV cache sharing among multi-LoRA (Low-Rank Adaptation) LLM agent systems, addressing the memory and compute overhead associated with independent cache storage for each agent. The methodology involves decomposing the KV cache into a shared base component and an adapter-dependent component, leveraging low-rank representation to minimize redundancy and optimize performance in shared architectures. Key findings indicate that LRAgent significantly reduces memory footprint and computation time while maintaining similar accuracy to baseline methods, showing promise for enhanced efficiency in agentic AI applications.


<details>
<summary>Abstract</summary>

Role specialization in multi-LLM agent systems is often realized via multi-LoRA, where agents share a pretrained backbone and differ only through lightweight adapters. Despite sharing base model weights, each agent independently builds and stores its own KV cache for the same long, tool-augmented trajectories, incurring substantial memory and compute overhead. Existing KV cache sharing methods largely overlook this multi-LoRA setting. We observe that, across agents, cache differences are dominated by adapter outputs, while activations from the shared pretrained backbone remain highly similar. Based on this observation, we propose LRAgent, a KV cache sharing framework for multi-LoRA agents that decomposes the cache into a shared base component from the pretrained weights and an adapter-dependent component from LoRA weights. LRAgent reduces memory overhead by sharing the base component and storing the adapter component in its inherent low-rank form, and further reduces compute overhead, enabled by shared-$A$ multi-LoRA architectures, by also sharing the low-rank cache and avoiding redundant computations for contexts already processed by other agents. To efficiently reconstruct adapter contributions at runtime, we introduce Flash-LoRA-Attention, a kernel that reorders attention computation to avoid materializing the low-rank cache to full dimension. LRAgent achieves throughput and time-to-first-token latency close to fully shared caching, while preserving accuracy near the non-shared caching baseline across agentic question-answering benchmarks.

</details>


### 21. PeerRank: Autonomous LLM Evaluation Through Web-Grounded, Bias-Controlled Peer Review

- **Authors:** Yanki Margalit, Erni Avram, Ran Taig, Oded Margalit, Nurit Cohen-Inger
- **Published:** 2026-02-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02589v1](http://arxiv.org/abs/2602.02589v1)
- **PDF:** [https://arxiv.org/pdf/2602.02589v1](https://arxiv.org/pdf/2602.02589v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces PeerRank, an autonomous evaluation framework for large language models (LLMs) that replaces traditional human-based benchmarking with a multi-agent approach, enabling models to generate tasks, answer them using live web data, and evaluate peer responses without human intervention. The methodology involves models acting symmetrically as task designers, respondents, and evaluators, leading to stable rankings and the identification of biases over a large-scale study involving 12 models and 420 questions. Key findings indicate that PeerRank provides reliable performance estimates and correlates well with objective accuracies on established benchmarks, suggesting its potential to revolutionize LLM assessment in open-world contexts by offering a scalable, bias-controlled alternative to conventional evaluation methods.


<details>
<summary>Abstract</summary>

Evaluating large language models typically relies on human-authored benchmarks, reference answers, and human or single-model judgments, approaches that scale poorly, become quickly outdated, and mismatch open-world deployments that depend on web retrieval and synthesis. We introduce PeerRank, a fully autonomous end-to-end evaluation framework in which models generate evaluation tasks, answer them with category-scoped live web grounding, judge peer responses and aggregate dense peer assessments into relative performance estimates, without human supervision or gold references. PeerRank treats evaluation as a multi-agent process where each model participates symmetrically as task designer, respondent, and evaluator, while removing biased judgments. In a large-scale study over 12 commercially available models and 420 autonomously generated questions, PeerRank produces stable, discriminative rankings and reveals measurable identity and presentation biases. Rankings are robust, and mean peer scores agree with Elo. We further validate PeerRank on TruthfulQA and GSM8K, where peer scores correlate with objective accuracy. Together, these results suggest that bias-aware peer evaluation with selective web-grounded answering can scale open-world LLM assessment beyond static and human curated benchmarks.

</details>



## Biorxiv (1 papers)


### 1. scChat: A Large Language Model-Powered Co-Pilot for Contextualized Single-Cell RNA Sequencing Analysis

- **Authors:** Chiu, H.-H., Varghese, A., Shao, K., Lu, Y.-C., Nahar, R., Chen, H., Deng, Q., Bao, X., Li, C.
- **Published:** 2026-01-27
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2024.10.01.616063](https://doi.org/10.1101/2024.10.01.616063)

- **Categories:** bioinformatics


> The paper introduces scChat, a large language model-powered co-pilot designed to enhance single-cell RNA sequencing (scRNA-seq) analysis by integrating research context and providing interactive, reasoning-based frameworks. Utilizing a multi-agent architecture and retrieval-augmented generation, scChat facilitates not just conventional tasks like cell type annotation but also hypothesis validation and experimental planning. Key findings indicate that scChat achieves high accuracy in annotation while offering biologically relevant explanations, marking a significant advancement in making computational approaches in biomedical research more interpretable and impactful.


<details>
<summary>Abstract</summary>

Single-cell RNA sequencing (scRNA-seq) has transformed biomedical research by enabling transcriptomic analysis at single-cell resolution. Yet, existing computational approaches remain primarily data-driven and lack the ability to integrate research context, limiting their interpretability and impact on hypothesis generation or experimental planning. We present scChat, a large language model (LLM)-powered co-pilot for contextualized scRNA-seq analysis. Unlike conventional pipelines restricted to tasks such as cell type annotation or enrichment analysis, scChat has an interactive, reasoning-based framework. It combines quantitative algorithms with retrieval-augmented generation and a multi-agent architecture to support hypothesis validation, mechanistic interpretation, and next-step experimental design. Through showcase and benchmarking studies, we demonstrate that scChat not only achieves high accuracy in cell type annotation but also provides biologically grounded explanations and contextual insights.

</details>



## Medrxiv (1 papers)


### 1. An Implantable Device that Converses with Patients and Learns to Co-Manage Epilepsy

- **Authors:** Goldblum, Z., Shi, H., Xu, Z., Ojemann, W. K. S., Aguila, C. A., Long, K., Xie, K., Nix, K. C., Walsh, K., Chang, E., Lavelle, S., Bach, B., Davis, K. A., Sinha, N., Hammer, L. H., Conrad, E. C., Litt, B.
- **Published:** 2026-01-27
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.01.26.26344234](https://doi.org/10.64898/2026.01.26.26344234)

- **Categories:** neurology


> The paper presents a novel implantable device platform designed for real-time patient interaction and co-management of epilepsy, utilizing large language models to communicate and learn from patients about their health and behaviors. The methodology involves linking EEG data to the AI agent, which optimizes seizure detection algorithms autonomously and engages patients through a smartphone app for feedback on symptoms and clinical events. Key findings indicate that the device significantly enhances patient experience and system performance—detecting seizures with improved precision without extensive physician intervention and fostering a constructive bidirectional dialogue that tailors the device's responses to individual patient needs, presenting a scalable solution for advancing medical care through agentic AI systems.


<details>
<summary>Abstract</summary>

One-third of the worlds 70 million people with epilepsy have seizures that are not controlled by medication; and implantable devices are an exciting option for treatment. These devices improve seizure control and can detect impending attacks, missed medication, and impaired cognition. Unfortunately, they have no way to share this information with their hosts in real-time - a limitation common to most medical devices. This is a missed opportunity for implants and wearables to learn from patients, focus on what matters most to them, and teach them how their behavior affects their health. Here, we present a device platform that converses with patients and learns to co-manage epilepsy. The inpatient prototype links scalp and intracranial EEG (electroencephalograms) to secure large language models that communicate freely and bidirectionally with their hosts through a smartphone app. An AI agent ingests biomarkers of awareness, sleep, medication level, cognition, and seizure risk extracted from brain activity. It converses with patients to inform them of clinical events and physiological trends, records their symptoms, responses, and behaviors, and automatically retrains itself to improve performance. Both patients and the AI agent can initiate conversations to teach each other and personalize interactions. We demonstrate this platform in 13 patients undergoing inpatient video-EEG monitoring for epilepsy and validate its performance. Algorithms for detecting seizures optimized their precision over several days without expert intervention - in contrast to the months of iterative, in-person physician programming currently required. Patients responded positively to messages regarding sleep, cognition, and seizure risk while rating the system as highly usable. The platform includes several safeguards, including a system for further algorithm fine-tuning using efficient expert review, and features that ensure data security and regulate communication content. Further work will link other biosensors to measure behavior, improve performance, and optimize therapeutic stimulation. We propose this system as a scalable platform for medical devices that can rapidly adapt to patient and provider needs; one that is broadly adaptable to improving care for many medical conditions.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*