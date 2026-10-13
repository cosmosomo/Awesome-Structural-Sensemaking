# L2 特定结构与数据的专项可视化项目

L1 回答“图形能够怎样绘制、组织和交互”，L2 回答：给定一种真实的数据或系统结构，如何自动提取它的语义，再转化为适合分析的可视化。因此优先按“被可视化的对象及其结构”分类，而不是按用了哪个前端框架分类。

> 项目事实和判断来自 2026-10 调研报告，未逐项核验。标 ✓ 的展示页已访问核对。

## 代码依赖与模块解耦

输入通常是源代码、模块定义、依赖配置；输出包括依赖图、循环依赖报告和变更影响分析。

<!-- gen:catalog:L2/code-dependencies -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [dependency-cruiser](https://sverweij.github.io/dependency-cruiser/) | JavaScript/TypeScript 模块依赖分析。<br>依赖图、架构边界规则、违规依赖诊断。 | [仓库](https://github.com/sverweij/dependency-cruiser) | [展示页](https://sverweij.github.io/dependency-cruiser-repro-repo/458/) | [站点](https://sverweij.github.io/dependency-cruiser/) | 展示页是作者的 3D 图报告插件演示（issue 458），用它自己的源码和 React 仓库生成。 |
| [Madge](https://github.com/pahen/madge) | JavaScript 模块引用分析。<br>自动生成依赖关系图、发现循环依赖。 | [仓库](https://github.com/pahen/madge) | 待收集 | — | — |
| [pydeps](https://github.com/thebjorn/pydeps) | Python 模块导入分析。<br>导入网络、模块聚类、依赖结构。 | [仓库](https://github.com/thebjorn/pydeps) | 待收集 | — | — |
<!-- /gen -->

## 软件架构与代码理解

有三条技术路线，不应相互取代：

- **确定性的结构提取**：分析 `import`、函数调用、依赖规则。关系可追溯到代码事实，但无法仅凭依赖理解业务意义。
- **语义辅助的架构提炼**：结合源码解析与语义分析，把低层代码组织为组件、架构层和业务概念。
- **模型驱动的结构展示**：维护有明确含义的架构对象和关系，再呈现在不同视图中。

自动分析得到的“真实依赖”、人为定义的“设计架构”、运行时观测到的“实际调用”，本来就可能不一致。

<!-- gen:catalog:L2/software-architecture -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CodeBoarding](https://github.com/CodeBoarding/CodeBoarding) | 源码结构及架构语义分析。<br>自动归纳组件，形成分层架构解释与可视化。 | [仓库](https://github.com/CodeBoarding/CodeBoarding) | 待收集 | — | — |
| [Understand Anything](https://understand-anything.com/) | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 | [仓库](https://github.com/Egonex-AI/Understand-Anything) | [展示页](https://understand-anything.com/) | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析。 |
| [LikeC4](https://likec4.dev/) | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 | [仓库](https://github.com/likec4/likec4) | [展示页](https://likec4.dev/showcases/bigbank/) | [站点](https://likec4.dev/) | — |
<!-- /gen -->

## 流程、状态机与任务依赖

研究的是具备执行语义的结构：开始、结束、分支、条件、循环、等待、并发、任务状态。

<!-- gen:catalog:L2/workflows-and-state-machines -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [bpmn-js](https://github.com/bpmn-io/bpmn-js) | BPMN 流程模型的查看、编辑与扩展。<br>建立在 diagram-js 之上，可通过扩展机制增加覆盖层、标记和自定义交互。 | [仓库](https://github.com/bpmn-io/bpmn-js) | [展示页](https://demo.bpmn.io/) | — | — |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble)<br>（主分类 L2/ai-and-multi-agent） | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 待收集 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |
<!-- /gen -->

## Agent 与多智能体协作

多视角体系在这里作为一个完整子分类保留。

| 可视化层级 | 所展示的结构 | 需要寻找的专项能力 |
| --- | --- | --- |
| 全局协作层 | 全部 Agent、角色、直接与间接连接 | 复杂关系图、关系筛选、高亮 |
| 组织抽象层 | 部门、子团队、管理关系、Agent 聚合 | 多层嵌套、折叠与连线聚合 |
| 实际任务层 | 某次任务涉及的 Agent 和交接过程 | 任务路径提取、聚焦与背景弱化 |
| 业务逻辑层 | 业务动作、决策条件、执行顺序 | 将 Agent 表达为执行角色，而非唯一主体 |
| 个体决策层 | 单个 Agent 的粗粒度决策过程 | 决策节点、循环、状态转换 |
| 微观执行层 | 模型调用、工具执行、消息、事件 | Trace 树、时间轴、事件详情 |

**功能空白**：报告没有找到充分证据，表明任何单一项目已完整实现上述六种视角及其无损跨层切换。这是需要重点记录的空白，不应通过抽象描述掩盖。

AgentEnsemble 的双视图值得细看：分别导出计划依赖 DAG 和执行 Trace，在网页中以 Flow View 和 Timeline View 展示。值得研究同一任务在两张视图中的身份如何保持一致，计划依赖和真实执行如何联系，点击任务又如何进入工具调用或会话详情。

<!-- gen:catalog:L2/ai-and-multi-agent -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble) | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 待收集 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AgentPrism](https://github.com/evilmartians/agent-prism) | 可嵌入应用的 React Agent Trace UI 组件。<br>层次化调用树、执行时间、工具与模型调用；独立可复用的 Trace UI 设计。 | [仓库](https://github.com/evilmartians/agent-prism) | [展示页](https://agent-prism.evilmartians.io/) | [文档](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces) | Alpha；项目公开标注为 Alpha。 |
<!-- /gen -->

## Trace、调用链和执行过程

先区分三种不同的东西，它们可能互相映射，但不是同一份数据：

| 结构 | 含义 | 典型视图 |
| --- | --- | --- |
| 静态依赖图 | 系统设计中可能发生什么调用 | 依赖图、架构图 |
| 运行时 Trace | 某一次运行实际发生了什么 | 调用树、瀑布图、时间线 |
| 聚合服务拓扑 | 多次运行中观察到哪些服务之间存在调用 | 服务关系图、健康状态图 |

一个值得研究的数据流：Agent 执行事件，采集与结构化（Span、事件、属性、父子关系），查询、归一化与组织，最后得到调用树、时间瀑布图或任务关系图。这是抽象的数据处理模式，不表示下列项目之间存在全部实际依赖。

<!-- gen:catalog:L2/traces-and-timelines -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [OpenTelemetry GenAI 语义约定](https://github.com/open-telemetry/semantic-conventions) | 规定如何描述 AI / Agent / 工具调用等遥测事件。<br>数据到可视化链条的起点：Span、事件、属性、父子关系。 | [仓库](https://github.com/open-telemetry/semantic-conventions) | 待收集 | [文档](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | 生成式 AI 语义约定仍在演进。建库时记录具体版本和字段定义，不要当成永远稳定的统一标准。 |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | 为 LLM 应用采集追踪数据。<br>数据采集端。 | [仓库](https://github.com/traceloop/openllmetry) | 待收集 | — | — |
| [Jaeger](https://github.com/jaegertracing/jaeger) | 分布式 Trace 的采集、检索和可视化。<br>Trace 瀑布图等传统调用链视图。 | [仓库](https://github.com/jaegertracing/jaeger) | [展示页](https://www.jaegertracing.io/demo/) | — | Jaeger v1 已于 2025-12-31 终止支持，应使用 v2（官网文档摘要）。 |
| [Grafana Tempo](https://github.com/grafana/tempo) | Trace 后端，与服务图、指标视图整合。<br>Trace 与服务图、指标的联动。 | [仓库](https://github.com/grafana/tempo) | 待收集 | — | — |
| [AeroGraph](https://github.com/sgcpu/aerograph) | 面向自主 AI 工作流的调试与观测层：本地优先、只追加、可安全回放的存储。<br>ReactFlow 的 Trace 图，支持逐步回放和失败高亮；可从任意 span 分叉出另一条时间线，并用 Myers diff 比较两次运行在哪里分岔；追踪循环和幻觉式的 Agent 交接。 | [仓库](https://github.com/sgcpu/aerograph) | 待收集 | — | 不在调研报告里，来自前期收集，信息取自搜索到的 GitHub README。是早期的小众项目，成熟度和循环检测的实现方式未核实。 |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble)<br>（主分类 L2/ai-and-multi-agent） | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 待收集 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AgentPrism](https://github.com/evilmartians/agent-prism)<br>（主分类 L2/ai-and-multi-agent） | 可嵌入应用的 React Agent Trace UI 组件。<br>层次化调用树、执行时间、工具与模型调用；独立可复用的 Trace UI 设计。 | [仓库](https://github.com/evilmartians/agent-prism) | [展示页](https://agent-prism.evilmartians.io/) | [文档](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces) | Alpha；项目公开标注为 Alpha。 |
<!-- /gen -->

## 数据血缘

数据血缘和系统服务拓扑处理的系统通常比普通 Agent 演示复杂得多，也更重视故障分析、跨层关联和对运行状态的持续观察。DataHub、OpenMetadata 同时是成熟应用，主分类在 L3。

<!-- gen:catalog:L2/data-lineage -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Marquez](https://marquezproject.ai/) | 数据集、数据任务与血缘关系。<br>上下游关系、运行历史。 | [仓库](https://github.com/MarquezProject/marquez) | 待收集 | [站点](https://marquezproject.ai/) | — |
| [DataHub](https://github.com/datahub-project/datahub)<br>（主分类 L3/data-and-infrastructure） | 数据发现、治理与影响分析。<br>数据集、字段、流水线的血缘；从资产详情进入上下游影响网络，支持字段级钻取和影响分析。 | [仓库](https://github.com/datahub-project/datahub) | [展示页](https://datahub.com/demos/data-lineage-with-datahub/) | [文档](https://docs.datahub.com/) | 该展示页是录制的血缘功能演示，不是开放试用。 |
| [OpenMetadata](https://github.com/open-metadata/OpenMetadata)<br>（主分类 L3/data-and-infrastructure） | 数据资产管理与治理。<br>资产关系、字段级血缘；从数据目录导航到血缘关系。 | [仓库](https://github.com/open-metadata/OpenMetadata) | [展示页](https://sandbox.open-metadata.org/) | [文档](https://docs.open-metadata.org/latest/quick-start/sandbox) | 沙盒需要用 Google 账号登录。 |
<!-- /gen -->

## 系统服务拓扑与基础设施

SkyWalking 能从宏观服务拓扑进入监控、日志与 Trace；Kiali 围绕服务网格的流量关系。二者主分类在 L3。

<!-- gen:catalog:L2/infrastructure-topology -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Apache SkyWalking](https://skywalking.apache.org/)<br>（主分类 L3/data-and-infrastructure） | 服务性能监控与故障诊断。<br>服务、实例、接口、部署等层级；从宏观服务拓扑进入监控、日志与 Trace，多视图联动。其生态中出现了基础设施三维可视化的探索。 | [仓库](https://github.com/apache/skywalking) | 待收集 | [站点](https://skywalking.apache.org/) · [文档](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/) | 官网首页链接到在线 Demo（示例数据）；其 Horizon UI 有基础设施 3D 地图（官方博客 2026-06）。 |
| [Kiali](https://github.com/kiali/kiali)<br>（主分类 L3/data-and-infrastructure） | 服务网格运行观察。<br>流量图、服务关系、异常定位。 | [仓库](https://github.com/kiali/kiali) | 待收集 | [文档](https://kiali.io/docs/features/topology/) | — |
<!-- /gen -->

## 知识、文档、思想与认知地图

这组与代码、Trace 的最大区别是：原始对象往往没有明确的结构边界，需要在显式信息和隐式语义之间做大量工作。

- 链接网络：记录页面 A 链接到页面 B。
- 实体关系图：记录“技术 A 支撑产品 B”“概念 C 反驳观点 D”这类带类型的关系。
- 认知结构图：还要表达理论层次、论证依据、粒度、解释路径和多种关系的组织方式。

一个有漂亮 Graph View 的笔记工具，并不自动意味着它能表达立体的认知框架。

<!-- gen:catalog:L2/knowledge-and-cognition -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [NeoDash](https://github.com/neo4j-contrib/neodash) | 使用 Neo4j 图数据库查询构建交互看板。<br>图数据查询驱动的看板。 | [仓库](https://github.com/neo4j-contrib/neodash) | [展示页](https://neodash-gallery.graphapp.io/) | — | 维护状态待核查；相关仓库存在维护状态变化，需要明确标注。 |
| [Excalidraw](https://github.com/excalidraw/excalidraw)<br>（主分类 L1/canvas-2d-and-3d） | 可嵌入、可编辑的二维无限白板。<br>偏向人工绘图、自由表达、构思与注释。 | [仓库](https://github.com/excalidraw/excalidraw) | [展示页](https://excalidraw.com/) | — | — |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 | [仓库](https://github.com/Egonex-AI/Understand-Anything) | [展示页](https://understand-anything.com/) | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析。 |
| [AFFiNE](https://affine.pro/)<br>（主分类 L3/knowledge-workspaces） | 文档、知识库与无限白板。<br>将线性文本与空间组织结合。 | [仓库](https://github.com/toeverything/AFFiNE) | 待收集 | [站点](https://affine.pro/) | — |
| [Logseq](https://github.com/logseq/logseq)<br>（主分类 L3/knowledge-workspaces） | 双向链接、页面及知识块。<br>大纲、链接和知识图导航。 | [仓库](https://github.com/logseq/logseq) | [展示页](https://demo.logseq.com/) | — | — |
| [InfraNodus](https://infranodus.com/)<br>（主分类 L3/knowledge-workspaces） | 文本网络与结构探索。<br>文本与概念的网络、主题群落、结构空白分析。 | [仓库](https://github.com/noduslabs/infranodus) | [展示页](https://infranodus.com/graphs) | [站点](https://infranodus.com/) | 商业产品；GitHub 公共仓库包含较早期代码，不能等同于当前商业产品的全部功能。 |
<!-- /gen -->

## 技术生态与商业产品地图

对应最初提出的“技术地图 × 产品地图”。先区分四种范式：

| 范式 | 它在回答什么 | 代表 |
| --- | --- | --- |
| 分类景观地图 | 这个领域有什么类别、产品和项目？ | CNCF Landscape |
| 技术决策雷达 | 哪些技术值得采用、试验、观察或暂缓？ | Thoughtworks / Zalando Tech Radar |
| 项目生态分析 | 哪些项目发展活跃、影响力大、生态健康？ | OSS Insight、OSS Compass |
| 跨领域关系地图 | 哪些技术支撑哪些产品、解决哪些需求？ | 需要综合图谱、矩阵及多视角表示 |

前三种都很成熟，但都不能直接完成“技术—产品耦合地图”：Landscape 擅长分类分布，不擅长跨类别依赖；Tech Radar 表达的是研究者判断的采用建议。应从多个成熟范式中借鉴，而不是模仿其中一种。

<!-- gen:catalog:L2/technology-landscapes -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CNCF Landscape2](https://github.com/cncf/landscape2) | 基于结构化数据生成可筛选、可搜索的生态分类景观。<br>生态地图的数据组织和交互导航。 | [仓库](https://github.com/cncf/landscape2) | [展示页](https://landscape.cncf.io/) | — | — |
| [Zalando Tech Radar](https://github.com/zalando/tech-radar) | 使用技术雷达表达技术采用阶段与类别。<br>技术决策状态的雷达表达。 | [仓库](https://github.com/zalando/tech-radar) | [展示页](https://opensource.zalando.com/tech-radar/) | — | — |
| [Build Your Own Radar](https://github.com/thoughtworks/build-your-own-radar) | 从结构化技术条目生成交互技术雷达。<br>技术雷达生成器。 | [仓库](https://github.com/thoughtworks/build-your-own-radar) | [展示页](https://radar.thoughtworks.com/) | — | 官方托管版要求使用 Technology Radar 固定的象限和环名称，自定义名称需自行部署；据搜索结果为 AGPL 许可。 |
<!-- /gen -->

## 三维、高维与大规模关系探索

需要分别研究三个问题：

1. 图形是否能够容纳非常大量的节点和边？
2. 高维结构投影到二维或三维之后，哪些信息被保留，哪些被扭曲？
3. 三维交互是否真正降低了理解成本，还是只增加了空间操作成本？

<!-- gen:catalog:L2/spatial-and-high-dimensional -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [PyGraphistry](https://github.com/graphistry/pygraphistry) | 将图分析数据接入 GPU 图探索环境。<br>GPU 图探索。 | [仓库](https://github.com/graphistry/pygraphistry) | [展示页](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html) | — | — |
| [Embedding Projector](https://projector.tensorflow.org/) | 将高维向量降维到二维、三维，探索相似性与聚类。<br>高维结构投影后哪些信息被保留、哪些被扭曲。 | [仓库](https://github.com/tensorflow/embedding-projector) | [展示页](https://projector.tensorflow.org/) | — | 三维位置来自降维计算，不应理解为概念在原始高维语义空间中的真实坐标。 |
| [deck.gl](https://github.com/visgl/deck.gl)<br>（主分类 L1/chart-and-visualization-engines） | GPU 加速的大数据可视化框架。<br>大规模数据、地图图层、多视角渲染。 | [仓库](https://github.com/visgl/deck.gl) | [展示页](https://deck.gl/gallery/) | — | — |
| [React Force Graph](https://github.com/vasturiano/react-force-graph)<br>（主分类 L1/canvas-2d-and-3d） | 2D、3D、VR、AR 关系图。<br>官方示例含点击展开折叠、相机聚焦、方向箭头、动态数据和不同空间模式，对复杂图的空间交互有参考价值。 | [仓库](https://github.com/vasturiano/react-force-graph) | [展示页](https://vasturiano.github.io/react-force-graph/) | — | — |
| [Cosmos.gl](https://github.com/cosmosgl/graph)<br>（主分类 L1/canvas-2d-and-3d） | GPU 加速的力导向图。<br>使用 GPU 做布局计算与图形渲染，面向大规模网络。 | [仓库](https://github.com/cosmosgl/graph) | 待收集 | [文档](https://openjsf.org/blog/introducing-cosmos-gl) | — |
<!-- /gen -->
