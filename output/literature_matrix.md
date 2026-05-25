# 《多模态大模型在智能电网中的应用综述》文献检索与 Literature Matrix

检索日期：2026-05-21  
工作流：academic-research-suite / deep-research / literature review / Phase 2  
范围：真实文献检索、来源核验、去重、literature matrix；不写正文，不生成章节草稿。

## 1. 检索式与检索策略

### 1.1 中文检索式

面向 CNKI/知网，万方、维普作为补充线索，优先中文核心、学报类、权威行业期刊和网络首发论文。

- `("多模态大模型" OR "视觉语言模型" OR "大语言模型" OR "电力大模型") AND ("智能电网" OR "新型电力系统" OR "电力系统" OR "配电网")`
- `("多模态大模型" OR "视觉语言模型") AND ("电力巡检" OR "设备运维" OR "缺陷识别" OR "故障诊断")`
- `("检索增强生成" OR "RAG" OR "知识图谱" OR "多模态知识图谱") AND ("电力" OR "智能电网" OR "配网调度")`
- `("智能体" OR "多智能体" OR "Agent" OR "具身智能") AND ("电力系统" OR "配网调度" OR "电力巡检" OR "电力设备")`
- `("推理大模型" OR "DeepSeek" OR "类DeepSeek") AND ("电力系统" OR "电力装备" OR "故障诊断" OR "智能决策")`

### 1.2 英文检索式

面向 Google Scholar、IEEE Xplore、ACM Digital Library、Springer、ScienceDirect、arXiv、Semantic Scholar，优先出版社页面、会议官网、arXiv 和 DOI 页面。

- `("multimodal large language model" OR "vision-language model" OR "MLLM" OR "large language model") AND ("smart grid" OR "power system" OR "electric power system")`
- `("large language models" AND "power systems") AND (survey OR review OR applications OR challenges)`
- `("vision-language model" OR "multimodal learning") AND ("power inspection" OR "fault diagnosis" OR "defect detection")`
- `("retrieval augmented generation" OR RAG OR "knowledge graph") AND ("power system" OR "smart grid" OR "power dispatch")`
- `("multi-agent" OR "LLM agent" OR "embodied intelligence") AND ("power grid" OR "power system operation" OR "distribution network")`
- `("large language model" OR "foundation model") AND ("optimal power flow" OR "voltage control" OR "power scheduling")`

### 1.3 纳入、排除、验证与去重规则

- 纳入：2020-2026 年文献优先；直接涉及 LLM/MLLM 与智能电网、电力系统、能源系统；或作为 Transformer、CLIP、多模态指令微调、RAG、知识图谱、多智能体/Agent 的经典基础文献。
- 保留经典基础文献：不受近五年限制，例如 Transformer。
- 排除：仅泛泛谈 AI、与电力系统/智能电网主线弱相关、新闻资讯、无法确认基本元数据的材料。
- `verified`：可通过 DOI、出版社页面、IEEE/ACM/Springer/ScienceDirect/arXiv/NeurIPS/PMLR/OpenReview 等官方来源核验。
- `metadata verified`：可确认题名、作者、年份、期刊/会议/学位论文等元数据，但未能通过 DOI/出版社全文页进一步核验；主要用于中文 CNKI/网络首发/本地 PDF。
- `unverified`：只有间接线索，不作为核心引用。本矩阵未纳入 unverified 作为核心条目。
- 去重：同一论文 arXiv 与正式出版版本重复时保留正式出版版本，并在 URL/说明中保留 arXiv 线索；多数据库重复时只保留主条目；本地 PDF 与外部检索重复时合并为同一记录。

## 2. Literature Matrix

### A. 基础模型与关键技术

| # | 题目 | 作者 | 年份 | 来源/期刊/会议 | DOI 或 URL | 主要研究内容 | 与本综述的相关性 | Use Level | Evidence Role | Recommended Section | 验证状态 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 1 | Attention Is All You Need | Ashish Vaswani et al. | 2017 | NeurIPS 2017 | https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html | 提出 Transformer 架构，以自注意力替代循环/卷积结构。 | LLM、VLM、MLLM 的底层模型架构基础。 | Background | 支撑“大模型技术基础来自 Transformer 架构”。 | 技术基础与模型演进 | verified |
| 2 | Language Models are Few-Shot Learners | Tom B. Brown et al. | 2020 | NeurIPS 2020 | https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html | GPT-3 展示大规模语言模型的上下文学习与少样本能力。 | 解释大语言模型为何能迁移到电力问答、调度辅助、方案生成等任务。 | Background | 支撑“通用语言能力与上下文学习是电力大模型应用前提”。 | 技术基础与模型演进 | verified |
| 3 | Learning Transferable Visual Models From Natural Language Supervision | Alec Radford et al. | 2021 | ICML 2021, PMLR | https://proceedings.mlr.press/v139/radford21a.html | CLIP 通过图文对比学习获得零样本视觉分类能力。 | 是电力巡检图像识别、视觉语言模型、跨模态检索的重要技术源头。 | Background | 支撑“视觉-语言对齐可降低电力图像任务标注依赖”。 | 多模态感知与电力巡检 | verified |
| 4 | Visual Instruction Tuning | Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee | 2023 | NeurIPS 2023 | https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html | 提出 LLaVA，将视觉编码器与 LLM 连接并进行视觉指令微调。 | 支撑电力视觉语言大模型从“识别”走向“问答、解释、交互”。 | Background | 支撑“MLLM 可用于图像理解和自然语言交互式巡检”。 | 技术基础与模型演进 | verified |
| 5 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Patrick Lewis et al. | 2020 | NeurIPS 2020 | https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html | 提出 RAG，将参数化模型与非参数化检索记忆结合。 | 直接支撑电力规程、调度文档、应急演练知识增强。 | Background | 支撑“RAG 是降低幻觉并增强电力专业知识可追溯性的关键路径”。 | 知识图谱、RAG 与知识增强 | verified |
| 6 | A Survey on Knowledge Graphs: Representation, Acquisition, and Applications | Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka Marttinen, Philip S. Yu | 2022 | IEEE Transactions on Neural Networks and Learning Systems | https://doi.org/10.1109/TNNLS.2021.3070843 | 系统综述知识图谱表示、获取、补全和应用。 | 支撑电力多模态知识图谱、RAG 图增强检索的理论基础。 | Background | 支撑“知识图谱可为电力大模型提供结构化知识约束”。 | 知识图谱、RAG 与知识增强 | verified |
| 7 | ReAct: Synergizing Reasoning and Acting in Language Models | Shunyu Yao et al. | 2023 | ICLR 2023 | https://openreview.net/forum?id=WE_vluYUL-X | 将推理轨迹与行动调用交替生成，增强可解释和工具调用能力。 | 为电力系统中的 LLM Agent、调度辅助和人在回路决策提供方法依据。 | Background | 支撑“Agent 化大模型需要推理-行动闭环”。 | Agent、多智能体与具身智能趋势 | verified |
| 8 | AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework | Qingyun Wu et al. | 2023 | arXiv / Microsoft Research | https://arxiv.org/abs/2308.08155 | 提出多智能体对话框架，用多个 LLM Agent 协作完成复杂任务。 | 可类比电力调度、故障研判、应急演练中的多角色业务协同。 | Supporting | 支撑“多智能体协作是复杂电力业务流程自动化的可行范式”。 | Agent、多智能体与具身智能趋势 | verified |

**本组小结**

- 可支撑的综述论点：MLLM 在智能电网中的应用不是孤立技术，而是由 Transformer、LLM、视觉语言对齐、RAG、知识图谱、Agent 等技术链条共同支撑。
- 共同不足：基础文献多为通用 AI 领域成果，未处理电力系统的物理约束、实时安全、调度规程和数据保密问题。
- 本文承接方式：以这些基础技术作为“能力来源”，再转入电力场景中的适配、约束和落地难点。
- 后续重点引用：Vaswani et al. 2017；Radford et al. 2021；Lewis et al. 2020；Liu et al. 2023；Yao et al. 2023。

### B. 电力/能源大模型综述

| # | 题目 | 作者 | 年份 | 来源/期刊/会议 | DOI 或 URL | 主要研究内容 | 与本综述的相关性 | Use Level | Evidence Role | Recommended Section | 验证状态 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 9 | A Comprehensive Review on the Application of Large Language Models (LLMs) in Power Systems | Masoumeh Ghafari et al. | 2025 | IEEE Access | https://doi.org/10.1109/ACCESS.2025.3637226 | 综述 LLM 在电力系统中的应用、Transformer 基础、智能电网、OPF、需求响应、网络安全等。 | 与选题高度相关，可作为英文电力 LLM 综述对照。 | Core | 支撑“电力系统 LLM 应用已覆盖规划、运行、市场、网络安全等环节”。 | 研究现状分析 | verified |
| 10 | A Review of Large Language Models for Energy Systems: Applications, Challenges, and Future Prospects | Hamid Mirshekali et al. | 2025 | IEEE Access | https://doi.org/10.1109/ACCESS.2025.3610994 | 梳理 LLM 在能源系统中的预测、故障诊断、文档自动化、能量管理等应用。 | 为智能电网之外的综合能源系统视角提供支撑。 | Core | 支撑“智能电网 MLLM 应放在能源系统智能化的大背景中理解”。 | 研究现状分析；挑战与未来方向 | verified |
| 11 | Large Language Models Meet Energy Systems: Opportunities, Challenges, and Future Perspectives | Wen Zhang et al. | 2026 | Applied Energy | https://www.sciencedirect.com/science/article/abs/pii/S0306261925018069 | 综述 LLM 与能源系统结合的机会、挑战和未来方向。 | 可用于拓展能源系统与电力系统交叉应用场景。 | Core | 支撑“LLM 能源应用正在从文本问答扩展到运行决策和系统优化”。 | 电力/能源大模型综述 | verified |
| 12 | Large Language Models for Power System Applications: A Comprehensive Literature Survey | Muhammad Sarwar et al. | 2025 | arXiv | https://arxiv.org/abs/2512.13004 | 综述 2020-2025 年 LLM 在电力系统中的故障诊断、预测、网络安全、控制优化等应用。 | 与本文主题高度相近，但侧重 LLM，不完全覆盖 MLLM。 | Core | 支撑“英文文献已形成电力系统 LLM 应用综述基础”。 | 研究现状分析 | verified |
| 13 | Large Language Models in Power Systems toward Cognitive Intelligence: A Literature Review | Xiaoyi Fan et al. | 2025 | SSRN / Preprint | https://www.ssrn.com/abstract=6025593 | 从认知智能角度讨论 LLM 在新能源预测、微电网管理、负荷预测、电力交易，以及 RAG、PEFT、ICL、MLLM、多智能体扩展技术。 | 直接支撑“从任务智能到认知智能”的综述主线。 | Core | 支撑“电力系统大模型趋势正转向认知推理和多智能体协同”。 | 研究现状分析；未来方向 | metadata verified |
| 14 | 大语言模型在电力系统中的应用初探 | 牛泽原，李嘉媚，艾芊 | 2025 | 电网技术 | https://doi.org/10.13335/j.1000-3673.pst.2024.1483 | 初步探讨 LLM 在电力系统中的技术优势和应用路径。 | 中文核心电力期刊中的 LLM 电力应用基础文献。 | Core | 支撑“国内电力系统领域已开始系统讨论 LLM 应用”。 | 研究现状分析 | metadata verified |
| 15 | 新型电力系统中的大模型驱动技术：现状、机遇与挑战 | 李刚，方鸿，刘云鹏，杨强，赵晓林，汪佐宪 | 2024 | 高电压技术 | https://doi.org/10.13336/j.1003-6520.hve.20240863 | 讨论多模态大模型等技术在新型电力系统中的场景解析、语言描述、机遇与挑战。 | 国内较早聚焦“大模型 + 新型电力系统”的综述性论文。 | Core | 支撑“多模态大模型具备场景解析和业务交互潜力”。 | 电力/能源大模型综述；挑战 | metadata verified |
| 16 | 多模态大模型在电力领域的应用综述 | 向思屿，王译萱，邝俊威，杜佩珂，毛洋，刘春 | 2025 | 四川电力技术 | 本地 PDF；期刊元数据已确认 | 梳理多模态数据融合大模型在设备故障检测、智能电网管理、知识图谱结合等方面的应用。 | 与本文题名最接近，需作为同题中文综述对照并避免同质化。 | Core | 支撑“中文文献已开始直接综述电力 MLLM 应用，但仍需更系统矩阵化”。 | 相关工作；研究现状分析 | metadata verified |
| 17 | 电力系统大模型的关键科学问题、挑战与展望 | 杜博骏，钟非池，侯庆春，贾宏阳，张宁，康重庆 | 2026 | 中国电机工程学报 | https://doi.org/10.13334/j.0258-8013.pcsee.252554 | 梳理构建电力系统大模型的科学问题、应用形态、研究框架与挑战。 | 可作为本文挑战与未来方向的重要中文核心依据。 | Core | 支撑“电力系统大模型需要领域科学问题牵引，而非简单迁移通用模型”。 | 挑战与未来方向 | metadata verified |

**本组小结**

- 可支撑的综述论点：LLM/MLLM 在电力与能源系统中的应用已经从概念验证进入综述化阶段，覆盖预测、调度、故障、市场、网络安全、知识管理等多场景。
- 共同不足：多数综述仍以 LLM 为主，MLLM 的电力图像、视频、传感器、规程文本融合讨论不足；中文综述多偏场景列举，量化对比和方法谱系仍不充分。
- 本文承接方式：突出“多模态”主线，将图像、文本、时序、图结构、知识图谱与 Agent 统一到智能电网任务框架中。
- 后续重点引用：Ghafari et al. 2025；Mirshekali et al. 2025；Sarwar et al. 2025；李刚等 2024；杜博骏等 2026；向思屿等 2025。

### C. 多模态感知与电力巡检

| # | 题目 | 作者 | 年份 | 来源/期刊/会议 | DOI 或 URL | 主要研究内容 | 与本综述的相关性 | Use Level | Evidence Role | Recommended Section | 验证状态 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 18 | PowerVLM: A Vision-language Large Model for Power Systems Enhanced by Federated Learning and Model Pruning | 欧阳旭东，雒鹏鑫，何绍洋，崔艺林，张中超，闫云凤 | 2026 | 全球能源互联网 | https://doi.org/10.19705/j.cnki.issn2096-5125.20250306 | 构建面向电力系统的视觉语言大模型，并结合联邦学习与模型剪枝。 | 直接对应电力视觉语言模型与轻量化部署。 | Core | 支撑“电力巡检 MLLM 需要兼顾隐私、跨主体协同与边缘部署”。 | 多模态感知与电力巡检 | metadata verified |
| 19 | 基于多模态融合和数据增强的复杂电力系统设备缺陷识别关键技术研究 | 刘爽 | 2026 | 科技创新与应用 / 能源电力栏目 | https://doi.org/10.13535/j.cnki.10-1507/n.2026.05.18 | 讨论多模态时频图特征融合、决策级融合和基础大模型微调在设备缺陷识别中的应用。 | 支撑从单一图像识别到多源缺陷识别的演进。 | Supporting | 支撑“多模态融合与数据增强是复杂设备缺陷识别的关键”。 | 多模态感知与电力巡检 | metadata verified |

**本组小结**

- 可支撑的综述论点：巡检和设备缺陷识别是 MLLM 在智能电网中最具可见度的应用，核心价值在于图像/视频/文本/传感数据联合理解。
- 共同不足：公开数据集、跨区域泛化、边缘部署实时性、标准化评价指标不足；不少中文材料为学位论文或行业应用论文，证据层级有限。
- 本文承接方式：把巡检应用拆成“视觉识别-语义解释-自然语言交互-机器人任务规划-边缘部署”链条，而不是只列举图像分类任务。
- 后续重点引用：PowerVLM；刘爽 2026；CLIP；LLaVA。

### D. 故障诊断与设备运维

| # | 题目 | 作者 | 年份 | 来源/期刊/会议 | DOI 或 URL | 主要研究内容 | 与本综述的相关性 | Use Level | Evidence Role | Recommended Section | 验证状态 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 20 | 面向新型电力系统的故障诊断技术研究进展（二）：机器学习和大语言模型技术 | 张建良，张晓洁，麻涛，季瑞松 | 2025 | 实验技术与管理 | https://doi.org/10.16791/j.cnki.sjg.2025.12.007 | 综述机器学习和大语言模型在新型电力系统故障诊断中的进展。 | 为故障诊断章节提供综述基础和传统 ML 对照。 | Core | 支撑“故障诊断正在从机器学习向 LLM/MLLM 辅助诊断演进”。 | 故障诊断与设备运维 | metadata verified |
| 21 | 类DeepSeek范式在电力装备故障诊断中的应用模式 | 江秀臣，臧奕茗，谢子恒，琚钰瑶，刘亚东，盛戈皞 | 2025 | 高电压技术 | https://doi.org/10.13336/j.1003-6520.hve.20250724 | 分析类 DeepSeek 范式在电力装备故障机理挖掘、多状态参量理解、多模态联合诊断、轻量部署中的应用。 | 与推理大模型、低算力部署、故障诊断高度相关。 | Core | 支撑“推理型开源模型适合电力装备故障诊断的安全和边缘部署需求”。 | 故障诊断与设备运维；挑战 | metadata verified |
| 22 | 大模型指令微调驱动的电力故障抢修方案智能生成 | 邓养吾，刘梦琪，李荣生，杨阳，孙玮璠，程培强 | 2026 | 计算机集成制造系统，网络首发 | https://doi.org/10.13196/j.cims.2026.BPM06 | 通过大模型指令微调生成电力故障抢修方案。 | 支撑“生成式大模型可从诊断扩展到抢修方案生成”。 | Core | 支撑“电力故障处置需要可解释、可执行、可审查的生成方案”。 | 故障诊断与设备运维 | metadata verified |
| 23 | 电力设备数智化发展历程与大语言模型智能体应用展望 | 周远翔，陈健宁，赵亮，程佳玉，姜贵敏，骆柏锋 | 2025 | 高电压技术 | https://doi.org/10.13336/j.1003-6520.hve.20250672 | 回顾电力设备数智化历程，提出 LLM Agent 在运维智能化中的五层应用框架。 | 连接设备运维、数字孪生、智能机器人和 Agent。 | Core | 支撑“电力设备运维正从数字化走向 Agent 驱动的智能化”。 | 故障诊断与设备运维；Agent 趋势 | metadata verified |

**本组小结**

- 可支撑的综述论点：故障诊断与设备运维是 MLLM/LLM 电力应用的核心落地场景，覆盖故障识别、故障机理解释、抢修方案生成、预测性维护。
- 共同不足：多数研究仍停留在框架设想或单点案例；缺少跨设备、跨电压等级、跨区域的可复现实验和安全评估。
- 本文承接方式：强调“诊断-解释-处置-复盘”的闭环，并讨论大模型幻觉、责任边界和安全校核。
- 后续重点引用：张建良等 2025；江秀臣等 2025；邓养吾等 2026；周远翔等 2025。

### E. 调度控制与运行决策

| # | 题目 | 作者 | 年份 | 来源/期刊/会议 | DOI 或 URL | 主要研究内容 | 与本综述的相关性 | Use Level | Evidence Role | Recommended Section | 验证状态 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 24 | Large Language Models for Power Scheduling: A User-Centric Approach | Thomas Mongaillard et al. | 2024 | arXiv | https://arxiv.org/abs/2407.00476 | 使用多个 LLM Agent 将用户语音请求转为电动汽车充电资源分配优化问题。 | 支撑用户侧调度、需求响应和 LLM Agent 优化建模。 | Supporting | 支撑“LLM 可作为用户意图到优化模型的接口”。 | 调度控制与运行决策 | verified |
| 25 | Large Language Model as An Operator: An Experience-Driven Solution for Distribution Network Voltage Control | Xu Yang et al. | 2025 | arXiv | https://arxiv.org/abs/2507.14800 | 提出面向配电网电压控制的经验驱动 LLM 操作员框架，包括经验存储、检索、生成和修正。 | 直接对应配电网调度控制中的 LLM 决策辅助。 | Core | 支撑“LLM 可通过经验检索和自我修正参与配电网电压控制”。 | 调度控制与运行决策 | verified |
| 26 | PowerGraph-LLM: Novel Power Grid Graph Embedding and Optimization with Large Language Models | Fabien Bernier, Jun Cao, Maxime Cordy, Salah Ghamizi | 2025 | IEEE Transactions on Power Systems | https://doi.org/10.1109/TPWRS.2025.3596774 | 将电网图结构和表格特征嵌入 LLM，用于 OPF 问题。 | 支撑电网拓扑、表格数据与 LLM 融合的运行优化路线。 | Core | 支撑“电力运行决策中的 MLLM 应吸收图结构和物理约束”。 | 调度控制与运行决策 | verified |
| 27 | 人工智能大模型在电力系统运行控制中的应用综述及展望 | 张俊，徐箭，许沛东，陈思远，高天露，白昱阳 | 2023 | 武汉大学学报（工学版） | https://doi.org/10.14188/j.1671-8844.2023-11-008 | 综述 AI 大模型技术及其在源-输-配-用-设备五维运行调控中的应用展望。 | 国内运行控制方向的关键综述。 | Core | 支撑“大模型运行控制应用需覆盖源网荷储设备全环节”。 | 调度控制与运行决策 | metadata verified |
| 28 | 推理大模型赋能新型电力系统智能决策：原理、应用与展望 | 余涛，陈宗源，李鹏，潘振宁，刘羽彬，冯琨皓 | 2026 | 电力系统自动化，网络首发 | https://link.cnki.net/urlid/32.1180.TP.20260515.1601.005 | 讨论推理大模型赋能新型电力系统智能决策的原理、应用和展望。 | 对“推理能力 + 智能决策”主线高度相关。 | Core | 支撑“新型电力系统需要从感知智能迈向推理决策智能”。 | 调度控制与运行决策；未来方向 | metadata verified |
| 29 | 新型配电系统运行专用大模型关键技术展望 | 杨浩蓝，刘友波，李争博，张俊，蒲天骄，尚宇炜，刘俊勇 | 2025 | 中国电机工程学报，网络首发 | https://link.cnki.net/urlid/11.2107.TM.20250820.1724.039 | 展望面向新型配电系统运行的专用大模型关键技术。 | 支撑“电力大模型需要从通用大模型转向场景专用模型”。 | Core | 支撑“配电系统运行需要专用模型、专用知识和安全约束”。 | 调度控制与运行决策 | metadata verified |

**本组小结**

- 可支撑的综述论点：LLM/MLLM 正从电力知识问答扩展到运行控制、OPF、配电网电压控制、用户侧调度和智能决策。
- 共同不足：真实电网闭环部署证据仍少；LLM 生成动作的安全约束、物理可行性和责任归属仍未充分解决。
- 本文承接方式：将调度控制应用划分为“意图解析-模型构建-方案生成-安全校核-人机协同执行”。
- 后续重点引用：PowerGraph-LLM；Large Language Model as An Operator；张俊等 2023；余涛等 2026；杨浩蓝等 2025。

### F. 知识图谱、RAG 与知识增强

| # | 题目 | 作者 | 年份 | 来源/期刊/会议 | DOI 或 URL | 主要研究内容 | 与本综述的相关性 | Use Level | Evidence Role | Recommended Section | 验证状态 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 30 | HG-RAG: Hierarchical Graph-Enhanced Retrieval-Augmented Generation for Power Systems | Zhijun Shen, Xinlei Cai, Binye Ni, Zijie Meng, Zhanhong Huang, Tao Yu | 2026 | Electronics | https://doi.org/10.3390/electronics15071445 | 面向电力系统结构化长上下文文档，提出层次图增强 RAG，提高问答准确性、可追溯性和增量更新能力。 | 直接支撑电力调度知识问答、RAG 和知识图谱结合。 | Core | 支撑“电力 RAG 需要处理结构化长文档和实体关系依赖”。 | 知识图谱、RAG 与知识增强 | verified |
| 31 | 基于高级检索增强生成技术与多模态大模型的电力应急演练应用研究 | 李文超，蒲毅，白洋，艾夏冕，朱跃 | 2025 | 电脑知识与技术 | https://doi.org/10.14004/j.cnki.ckt.2025.1742 | 构建电力应急多模态知识库，结合向量检索、知识重构和跨模态融合生成应急演练方案。 | 与 RAG、应急演练、多模态知识库直接相关。 | Supporting | 支撑“RAG 可缓解电力应急演练中的知识滞后和幻觉问题”。 | 知识图谱、RAG 与知识增强 | metadata verified |
| 32 | 基于大语言模型构建面向能源数字网络的知识图谱 | 周爱华，潘森，乔俊峰，朱力鹏，李井泉，张肖杰 | 2026 | 电力信息与通信技术，网络首发 | https://link.cnki.net/urlid/10.1164.TK.20260415.0919.002 | 使用大语言模型构建能源数字网络知识图谱。 | 支撑 LLM 辅助电力/能源知识图谱构建。 | Core | 支撑“LLM 可降低能源知识图谱构建成本并增强知识抽取”。 | 知识图谱、RAG 与知识增强 | metadata verified |
| 33 | 基于多模态知识图谱的变电站设备智能运检关键技术研究 | 付旭辉 | 2025 | 中国矿业大学硕士专业学位论文 | 本地 PDF；学位论文元数据已确认 | 研究多模态知识图谱支持变电站设备智能运检的关键技术。 | 可作为变电站设备多模态知识组织案例。 | Supporting | 支撑“设备运检需要将图像、文本、设备关系融合为知识图谱”。 | 知识图谱、RAG 与知识增强 | metadata verified |

**本组小结**

- 可支撑的综述论点：知识图谱与 RAG 是电力 MLLM 落地的关键增强技术，能够缓解幻觉、增强可追溯性，并注入规程、设备台账、拓扑和历史案例。
- 共同不足：中文应用研究多为单场景构建，缺少跨系统共享本体、持续更新机制和标准化问答基准。
- 本文承接方式：将知识增强技术分为“知识抽取-图谱构建-检索增强-跨模态问答-可追溯生成”。
- 后续重点引用：HG-RAG；Lewis et al. 2020；Ji et al. 2022；周爱华等 2026；李文超等 2025。

### G. Agent、多智能体、具身智能与安全可信

| # | 题目 | 作者 | 年份 | 来源/期刊/会议 | DOI 或 URL | 主要研究内容 | 与本综述的相关性 | Use Level | Evidence Role | Recommended Section | 验证状态 |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 34 | Risks of Practicing Large Language Models in Smart Grid: Threat Modeling and Validation | Jiangnan Li, Yingyuan Yang, Jinyuan Sun | 2024 | arXiv | https://arxiv.org/abs/2405.06237 | 系统评估 LLM 在智能电网应用中的风险，提出威胁模型并用真实智能电网数据验证攻击。 | 是安全可信章节的关键英文证据。 | Core | 支撑“智能电网 LLM 应用必须先进行威胁建模和安全验证”。 | 挑战、安全可信与未来方向 | verified |
| 35 | 面向配网调度故障研判的多模态多智能体可信业务协同机制 | 崔豪驿，邓华，刁其先，鲍娌娜，武彬，王朝阳 | 2026 | 计算机集成制造系统，网络首发 | https://doi.org/10.13196/j.cims.2026.BPM17 | 面向配网调度故障研判，提出多模态多智能体可信业务协同机制。 | 直接对应多智能体、调度故障研判和可信协同。 | Core | 支撑“复杂电力业务需要多智能体分工协作与可信机制”。 | Agent、多智能体与具身智能趋势 | metadata verified |
| 36 | 电力系统自主智能决策范式设想：从知识数据融合、人在回路到具身自主智能 | 窦嘉铭，王小君，刘曌，刘畅宇，张沛，赵俊华，蒲天骄 | 2026 | 中国电机工程学报，网络首发 | https://doi.org/10.13334/j.0258-8013.pcsee.251444 | 提出电力系统自主智能决策范式，从知识数据融合、人在回路到具身自主智能。 | 是本文未来趋势章节的重要中文核心材料。 | Core | 支撑“电力系统智能决策应经历人机协同到具身自主的渐进路径”。 | Agent、多智能体与具身智能趋势；未来方向 | metadata verified |

**本组小结**

- 可支撑的综述论点：智能电网中的 MLLM 应用将朝 Agent 化、多智能体协同、人在回路、具身自主和安全可信方向演进。
- 共同不足：多智能体协作容易引入责任链不清、错误传播、越权调用和攻击面扩大；具身智能相关电力实证仍少。
- 本文承接方式：把未来趋势写成“能力增强”和“风险治理”双线并行，强调可信协同、权限边界、安全校核和人机共驾。
- 后续重点引用：Li et al. 2024；崔豪驿等 2026；窦嘉铭等 2026；ReAct；AutoGen。

## 3. 去重与剔除说明

- `PowerGraph-LLM` 同时存在 arXiv 与 IEEE Transactions on Power Systems 版本，本矩阵保留 IEEE 正式出版 DOI，arXiv 作为版本线索。
- `Large Language Models for Power Scheduling`、`Large Language Model as An Operator` 暂未发现正式出版版本，本矩阵保留 arXiv 主条目。
- 本地 `related_papers/` 中多个中文 PDF 存在重复下载，如 `基于多模态大模型的电力巡检图像智能识别`、`基于多模态知识图谱的变电站设备智能运检关键技术研究` 等，矩阵均合并为单条记录。
- 行业资讯、新闻类材料，如“广角.pdf”“光明电力大模型的能力与应用”等，可作为写作背景，不进入核心 literature matrix。
- `unverified` 条目未进入核心矩阵；若后续要扩展产业案例，可单独建立“产业实践材料表”。

## 4. 初步证据结构

- 技术基础：Transformer、GPT-3、CLIP、LLaVA、RAG、知识图谱、ReAct/AutoGen。
- 总体综述：英文 IEEE Access/Applied Energy/arXiv/SSRN 与中文电网技术、高电压技术、中国电机工程学报互补。
- 应用场景：巡检识别、设备缺陷、故障诊断、抢修生成、配电调度、OPF、电压控制、知识问答、应急演练。
- 关键趋势：领域专用大模型、多模态融合、RAG/知识图谱增强、Agent 化、多智能体可信协同、人在回路、具身智能。
- 主要挑战：数据质量与保密、物理约束、安全可信、可解释性、实时性、边缘部署、标准化评价与责任边界。
