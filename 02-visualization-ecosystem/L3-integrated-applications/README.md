# L3 成熟应用与综合交互系统

研究的不是“这个产品有没有一张图”，而是可视化如何嵌入一个完整的产品工作流程，与搜索、编辑、分析、调试、管理、协作和决策等功能共同作用。

例如一个多智能体管理平台，主要任务可能是配置 Agent、定义任务、监控执行、发现异常、干预运行；协作图和 Trace 只是其中的两个界面。只截取它的流程图，就无法理解它为什么采用这种交互。

> 项目事实和判断来自 2026-10 调研报告，未逐项核验。标 ✓ 的展示页已访问核对。许可证与维护状态的提醒写在“备注”列。
> 同时保留开源项目和可体验的成熟商业产品两种资源，不为了坚持 Awesome 的开源传统而丢失重要的交互案例。

## AI 应用与工作流开发平台

Dify、Langflow、n8n、Node-RED 的重点已超出画图，进入完整的应用构建和执行闭环。

<!-- gen:catalog:L3/ai-development-platforms -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Dify](https://dify.ai/) | 构建、发布、运行 AI 应用。<br>工作流、知识检索及执行观察；节点编辑、测试、节点结果检查、应用管理。 | [仓库](https://github.com/langgenius/dify) | [展示页](https://marketplace.dify.ai/) ✓ | [站点](https://dify.ai/) | 含附加条件的许可证；官网自称 Source-available、Apache-2.0-derivative license（dify.ai，2026-10-13 访问）；具体附加条件在 GitHub 的 LICENSE 里，未核实。展示页是官方市场，含可复制的工作流模板。 |
| [Langflow](https://www.langflow.org/) | 构建和发布 Agent 工作流。<br>可视节点编排与执行测试；编辑、Playground、调试、API 发布的闭环。据官方文档可发布为 API 或 MCP 服务，并与可观测性平台集成。 | [仓库](https://github.com/langflow-ai/langflow) | [展示页](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/) ✓ | [站点](https://www.langflow.org/) · [文档](https://docs.langflow.org/) | 展示页是官网模板页之一；模板总览页 /templates 返回 404。 |
| [n8n](https://github.com/n8n-io/n8n) | 通用业务自动化及 AI 工作流。<br>自动化流程设计与执行诊断；节点编辑、运行历史、失败定位、重新执行。 | [仓库](https://github.com/n8n-io/n8n) | [展示页](https://n8n.io/workflows/) ✓ | — | 源码可见但有使用限制；docs.n8n.io 写明采用 Sustainable Use License 与 Enterprise License，均基于 fair-code 模式（2026-10-13 核对）；报告称其不是 OSI 意义上的开源。 |
| [Node-RED](https://github.com/node-red/node-red) | 事件驱动流程与设备、服务集成。<br>消息流的可视编排；部署、调试、运行时数据观察。 | [仓库](https://github.com/node-red/node-red) | [展示页](https://flows.nodered.org/) ✓ | — | — |
| [Flowise](https://flowiseai.com/) | LLM、工具与 Agent 流程构建。<br>Agentflow 图编辑器；条件、循环、状态与工具节点。 | [仓库](https://github.com/FlowiseAI/Flowise) | 待收集 | [站点](https://flowiseai.com/) · [文档](https://docs.flowiseai.com/) | 开源；已停止维护；官网 flowiseai.com/sunset 宣布停止运营：2026-07-29 代码冻结，2026-08-10 仓库转为公共归档，2026-08-31 终止支持；代码仍为 Apache 2.0，可自行 fork（2026-10-13 访问）。页面仍用将来时，仓库当前是否已归档需在 GitHub 上核实。 |
<!-- /gen -->

## Agent 开发、协作与管理平台

值得研究的不只是节点和连线，而是从“开发或管理行为”进入“运行结构”，再进入“具体事件和干预动作”。AgentEnsemble 的实时看板把任务执行事件与人工审核动作纳入同一交互过程，与单纯展示最终 Trace 图有明显区别。

<!-- gen:catalog:L3/agent-management -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AgentScope 2.0](https://github.com/agentscope-ai/agentscope) | Agent 团队编排、运行和观测。<br>团队及执行信息进入 Web UI；Agent 团队运行与实时观察。 | [仓库](https://github.com/agentscope-ai/agentscope) | 无：Studio 在本地运行，没有公开在线演示 | [文档](https://docs.agentscope.io/) | 维护状态待核查；报告称旧版独立 AgentScope Studio 已不再单独维护。doc.agentscope.io 的 Studio 页仍写着“The Studio is under fast development”，页脚年份是 2025，可能已过时；docs.agentscope.io 的 2.0.9 文档没有提到 Studio（2026-10-13 核对）。Studio 当前状态待核查。 |
| [LangGraph / Studio](https://github.com/langchain-ai/langgraph) | 图状态、任务路由与 Agent 开发。<br>图结构与运行状态、调试会话之间的关联。 | [仓库](https://github.com/langchain-ai/langgraph) | 无：Studio 需账号或在本地运行，没有公开演示 | [文档](https://docs.langchain.com/langsmith/studio) | LangGraph Studio / LangSmith Studio 有账号及运行环境要求。 |
| [AgentEnsemble](https://agentensemble.github.io/agentensemble/) | 团队任务编排和执行分析。<br>DAG、时间图、通过事件流实时更新的执行看板，以及人工审核交互，把任务执行事件与人工干预放进同一过程。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 无：Live Dashboard 在本地运行（localhost:7329），没有托管的公开演示 | [站点](https://agentensemble.github.io/agentensemble/) · [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AutoGen / AutoGen Studio](https://github.com/microsoft/autogen) | Agent 原型构建与团队交互。<br>智能体团队的可视化原型、运行测试；Studio 定位为原型，不是生产级应用。 | [仓库](https://github.com/microsoft/autogen) | 无：AutoGen Studio 在本地运行，没有托管的公开演示 | [文档](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html) | — |
<!-- /gen -->

## LLM 与 Agent 可观测性平台

产品化程度相对高，可用于比较 Trace 这种专项可视化如何融入完整的 AI 工程闭环。以 Langfuse 为例，可以从一次异常执行进一步进入提示词、测试数据和评测过程。迁移到认知地图：从一条不合理的结构关系，进入证据、分析原因，再修正原来的模型，而不只是对节点做视觉操作。

<!-- gen:catalog:L3/observability-platforms -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Langfuse](https://github.com/langfuse/langfuse) | 追踪、评测、提示词管理、数据集及实验。<br>Trace、调用详情、耗时、Token、成本及评测。可从一次异常执行进入提示词、测试数据和评测过程，形成分析、修改、再验证的闭环。 | [仓库](https://github.com/langfuse/langfuse) | [展示页](https://langfuse.com/docs/demo) ✓ | — | — |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | AI 应用追踪与质量评测。<br>基于 OpenTelemetry 的调用轨迹、问题诊断、评测分析。 | [仓库](https://github.com/Arize-ai/phoenix) | [展示页](https://phoenix-demo.arize.com/) ✓ | — | — |
| [Comet Opik](https://www.comet.com/site/products/opik/) | LLM / Agent 追踪、评测和监控。<br>多层调用、评测结果、运行监控。 | [仓库](https://github.com/comet-ml/opik) | 待收集 | [站点](https://www.comet.com/site/products/opik/) | — |
| [AgentOps](https://www.agentops.ai/) | Agent 执行记录、调试与成本观察。<br>会话回放、调用轨迹、成本。 | [仓库](https://github.com/AgentOps-AI/agentops) | 无：控制台需登录（app.agentops.ai 跳转到登录页），没有找到免登录的公开示例 | [站点](https://www.agentops.ai/) · [文档](https://docs.agentops.ai/v2/introduction) | — |
| [LangWatch](https://langwatch.ai/) | LLM 运行追踪、分析与评测。<br>Trace、质量指标与运行分析。 | [仓库](https://github.com/langwatch/langwatch) | [展示页](https://app.langwatch.ai/demo) | [站点](https://langwatch.ai/) | 展示页由前端渲染，内容以及是否免登录都没有确认。 |
<!-- /gen -->

## 软件架构、开发者平台与工程管理

- Nx 把“组成结构”和“任务结构”分开：模块之间存在依赖，不代表每次任务都会经过全部依赖路径。
- Backstage 把“实体关系图”嵌入开发者门户：实体中心视角、选择关系类型、控制深度、图与产品联动。

<!-- gen:catalog:L3/software-engineering-platforms -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Nx](https://github.com/nrwl/nx) | Monorepo 构建与任务管理。<br>把组成结构和任务结构分开：Project Graph 表示项目间依赖，Task Graph 表示实际构建任务及执行依赖。可聚焦项目、查看邻近项目、按文件夹分组、分析影响范围、导出图数据。 | [仓库](https://github.com/nrwl/nx) | [展示页](https://nx.dev/docs/features/explore-graph) | — | 展示页是官方文档页，据检索页面内嵌可交互的项目图示例，由 JS 加载，渲染情况未确认。 |
| [Backstage](https://github.com/backstage/backstage) | 开发者门户与软件服务目录。<br>Catalog Graph：实体中心视角，按关系和实体类别筛选，控制展开深度、方向和连线合并，并与实体详情联动。 | [仓库](https://github.com/backstage/backstage) | [展示页](https://demo.backstage.io/catalog) ✓ | [文档](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/) | 官方强调服务目录反映的是便于人理解的组织与软件模型，而不是所有实时关系的唯一真实来源。公开 Demo 站点上是否启用了关系图未确认。 |
| [Structurizr DSL](https://github.com/structurizr/dsl)<br>（主分类 L1/diagram-languages） | 统一 C4 架构模型及多视角定义。<br>把模型与视图分离：一份结构模型可以定义多张不同视角的图。 | [仓库](https://github.com/structurizr/dsl) | [展示页](https://docs.structurizr.com/example) ✓ | — | — |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 | [仓库](https://github.com/Egonex-AI/Understand-Anything) | [展示页](https://understand-anything.com/) ✓ | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析。 |
| [LikeC4](https://likec4.dev/)<br>（主分类 L2/software-architecture） | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 | [仓库](https://github.com/likec4/likec4) | [展示页](https://likec4.dev/showcases/bigbank/) ✓ | [站点](https://likec4.dev/) | — |
<!-- /gen -->

## 数据平台与基础设施管理

这些应用的图形大多围绕实际诊断任务组织。服务关系图上的一条边不仅表示“存在连接”，还可能关联请求量、错误率和耗时，用户可以沿着这条关系继续进入具体 Trace。

<!-- gen:catalog:L3/data-and-infrastructure -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [DataHub](https://github.com/datahub-project/datahub) | 数据发现、治理与影响分析。<br>数据集、字段、流水线的血缘；从资产详情进入上下游影响网络，支持字段级钻取和影响分析。 | [仓库](https://github.com/datahub-project/datahub) | [展示页](https://datahub.com/demos/data-lineage-with-datahub/) ✓ | [文档](https://docs.datahub.com/) | 该展示页是录制的血缘功能演示，不是开放试用。 |
| [OpenMetadata](https://github.com/open-metadata/OpenMetadata) | 数据资产管理与治理。<br>资产关系、字段级血缘；从数据目录导航到血缘关系。 | [仓库](https://github.com/open-metadata/OpenMetadata) | [展示页](https://sandbox.open-metadata.org/) ✓ | [文档](https://docs.open-metadata.org/latest/quick-start/sandbox) | 沙盒需要用 Google 账号登录。 |
| [Apache SkyWalking](https://skywalking.apache.org/) | 服务性能监控与故障诊断。<br>服务、实例、接口、部署等层级；从宏观服务拓扑进入监控、日志与 Trace，多视图联动。其生态中出现了基础设施三维可视化的探索。 | [仓库](https://github.com/apache/skywalking) | [展示页](https://demo.skywalking.apache.org/) ✓ | [站点](https://skywalking.apache.org/) · [文档](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/) | 官网首页链接到在线 Demo（Horizon UI，示例数据）和一个独立的 3D 基础设施地图交互演示（2026-10-13 访问）。 |
| [Kiali](https://github.com/kiali/kiali) | 服务网格运行观察。<br>流量图、服务关系、异常定位。 | [仓库](https://github.com/kiali/kiali) | 待收集 | [文档](https://kiali.io/docs/features/topology/) | — |
| [Grafana](https://github.com/grafana/grafana) | 观测数据看板与分析。<br>指标、日志、Trace、服务关系。 | [仓库](https://github.com/grafana/grafana) | [展示页](https://play.grafana.org/) ✓ | — | — |
<!-- /gen -->

## 知识组织、概念地图与认知工具

<!-- gen:catalog:L3/knowledge-workspaces -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AFFiNE](https://affine.pro/) | 文档、知识库与无限白板。<br>将线性文本与空间组织结合。 | [仓库](https://github.com/toeverything/AFFiNE) | [展示页](https://affine.pro/templates) ✓ | [站点](https://affine.pro/) | 展示页是模板库页面，不是在线试用；没有找到免登录的在线版本。 |
| [diagrams.net / draw.io](https://www.drawio.com/) | 通用结构图创建与编辑。<br>手动构造架构图、流程图、认知图。 | [仓库](https://github.com/jgraph/drawio) | [展示页](https://www.drawio.com/docs/diagram-types/) ✓ | [站点](https://www.drawio.com/) | — |
| [Kumu](https://kumu.io/) | 复杂系统、利益相关方和关系地图。<br>关系探索、视图定义、叙事展示。研究对象与软件流程编辑器明显不同。 | — | [展示页](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative) ✓ | [站点](https://kumu.io/) · [文档](https://docs.kumu.io/frequently-asked-questions/where-can-i-find-example-kumu-projects) | 商业产品；不能直接二次开发；作为可体验的交互案例收录。 |
| [Logseq](https://github.com/logseq/logseq) | 双向链接、页面及知识块。<br>大纲、链接和知识图导航。 | [仓库](https://github.com/logseq/logseq) | [展示页](https://demo.logseq.com/) ✓ | — | — |
| [InfraNodus](https://infranodus.com/) | 文本网络与结构探索。<br>文本与概念的网络、主题群落、结构空白分析。 | [仓库](https://github.com/noduslabs/infranodus) | [展示页](https://infranodus.com/graphs) ✓ | [站点](https://infranodus.com/) | 商业产品；官网说明开源的是一组支撑 InfraNodus 的工具（AGPL 许可），页脚列出 GitHub 上的 Workflows、Datasets、Tools API 和 GraphRAG MCP Server（infranodus.com，2026-10-13 访问）；报告所说“旧仓库不代表当前产品全部功能”未核实。 |
<!-- /gen -->

## 生态地图与产业分析产品

在完整产品中把可视化与筛选、搜索、详情、指标、时间分析等操作结合，可作为“技术地图和产品地图”的不同功能参考。

<!-- gen:catalog:L3/market-and-ecosystem-platforms -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CNCF Landscape](https://landscape.cncf.io/) | 大型生态分类数据与实际展示案例。<br>浏览技术类别、生态参与者、项目属性；表达分类与生态分布，不擅长展示大量跨类别依赖。 | [仓库](https://github.com/cncf/landscape) | [展示页](https://landscape.cncf.io/) ✓ | — | — |
| [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar) | 技术采用建议与趋势。<br>表达经过研究者判断的技术采用建议，而不是技术、产品、需求之间的完整关系。 | — | [展示页](https://www.thoughtworks.com/radar) ✓ | — | — |
| [OSS Insight](https://ossinsight.io/) | GitHub 项目和开发生态数据分析。<br>研究 GitHub 活跃度、生态指标及时间变化。 | [仓库](https://github.com/pingcap/ossinsight) | [展示页](https://ossinsight.io/) ✓ | — | — |
| [OSS Compass](https://oss-compass.org/) | 开源项目健康与生态指标分析。<br>多指标比较开源项目的生态表现。 | [仓库](https://github.com/oss-compass/compass-web) | [展示页](https://oss-compass.org/) ✓ | — | — |
<!-- /gen -->
