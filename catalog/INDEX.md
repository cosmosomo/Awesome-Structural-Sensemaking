# 项目索引

> 本文件由 `scripts/build.py` 根据 `catalog/` 生成，请改 YAML，不要直接改这里。
> 条目信息来自 2026-10 调研报告。展示页来自报告原文或事后的搜索结果，除标 ✓ 的外都没有实际访问过。

共 85 个条目；有开源项目地址 83 个，有展示页 52 个（其中 0 个已访问核对，标 ✓）。

“待补”表示开源项目地址缺失，“待收集”表示展示页缺失；商业产品、规范和刊物没有仓库，用“—”表示。

## L1 底层可视化技术

### 通用图形与数据可视化

<sub>L1/chart-and-visualization-engines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [D3.js](https://github.com/d3/d3) | 底层数据驱动可视化工具集。<br>自定义视觉编码、层级、网络、布局与交互。 | [仓库](https://github.com/d3/d3) | [展示页](https://observablehq.com/collection/@d3/gallery) | — | — |
| [Vega-Lite](https://github.com/vega/vega-lite) | 声明式可视化语法。<br>用结构化描述定义图表，而不是逐元素绘制。 | [仓库](https://github.com/vega/vega-lite) | [展示页](https://vega.github.io/vega-lite/examples/) | — | — |
| [Apache ECharts](https://echarts.apache.org/) | 综合图表引擎。<br>图表类型、交互组件、大屏和业务看板。 | [仓库](https://github.com/apache/echarts) | [展示页](https://echarts.apache.org/examples) | [站点](https://echarts.apache.org/) | — |
| [Plotly.js](https://github.com/plotly/plotly.js) | 数据探索与交互图表。<br>多维统计图、科学可视化、交互分析。 | [仓库](https://github.com/plotly/plotly.js) | [展示页](https://plotly.com/javascript/) | — | — |
| [deck.gl](https://github.com/visgl/deck.gl) | GPU 加速的大数据可视化框架。<br>大规模数据、地图图层、多视角渲染。 | [仓库](https://github.com/visgl/deck.gl) | [展示页](https://deck.gl/gallery/) | — | — |

### 关系图与节点交互引擎

<sub>L1/graph-and-node-engines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AntV G6](https://g6.antv.antgroup.com/) | 通用关系图引擎：图布局、分组、交互。<br>Combo 嵌套、聚合、折叠，复杂关系布局。适合研究复杂网络的结构呈现。 | [仓库](https://github.com/antvis/G6) | [展示页](https://g6.antv.antgroup.com/manual/behavior/collapse-expand) | [站点](https://g6.antv.antgroup.com/) | — |
| [React Flow](https://reactflow.dev/) | React 节点和边编辑器。<br>自定义节点、子流程、连线编辑、业务组件集成。更适合研究复杂节点编辑器与工作流应用。 | [仓库](https://github.com/xyflow/xyflow) | [展示页](https://reactflow.dev/examples) | [站点](https://reactflow.dev/) | 官方展开折叠等部分高级示例属于付费 Pro 内容。 |
| [Cytoscape.js](https://js.cytoscape.org/) | 图模型、网络分析及扩展生态。<br>复合节点、图算法、复杂度管理。更适合研究复杂网络的结构呈现。 | [仓库](https://github.com/cytoscape/cytoscape.js) | [展示页](https://js.cytoscape.org/) | — | — |
| [Sigma.js](https://www.sigmajs.org/) | 基于 WebGL 的网络图渲染。<br>较大关系网络、节点探索，常与 Graphology 配合。 | [仓库](https://github.com/jacomyal/sigma.js) | [展示页](https://www.sigmajs.org/examples/) | [站点](https://www.sigmajs.org/) | — |
| [AntV X6](https://github.com/antvis/X6) | 图编辑引擎。<br>复杂节点编辑、连接桩、流程编辑器。 | [仓库](https://github.com/antvis/X6) | [展示页](https://x6.antv.antgroup.com/examples) | — | — |
| [diagram-js](https://github.com/bpmn-io/diagram-js) | 图形编辑能力底座，bpmn-js 建立在其上。<br>编辑器组件；业务流程方向的 L1 代表。 | [仓库](https://github.com/bpmn-io/diagram-js) | 待收集 | — | 报告只在正文和跨层索引里提到，没有给出地址；仓库地址由整理者补充。 |

### 布局与复杂度管理算法

<sub>L1/layouts-and-graph-algorithms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [ELK.js](https://github.com/kieler/elkjs) | 自动分层布局、连线布线、复合图布局。<br>复杂模块和任务 DAG。 | [仓库](https://github.com/kieler/elkjs) | [展示页](https://rtsys.informatik.uni-kiel.de/elklive/) | — | — |
| [Dagre](https://github.com/dagrejs/dagre) | 有向图层次布局。<br>工作流、依赖图。 | [仓库](https://github.com/dagrejs/dagre) | [展示页](https://dagrejs.github.io/project/dagre-d3/latest/demo/interactive-demo.html) | — | 展示页属于 dagre-d3。 |
| [Graphviz](https://graphviz.org/) | 多种图布局与渲染。<br>架构图、静态分析、依赖图。 | [仓库](https://gitlab.com/graphviz/graphviz) | [展示页](https://graphviz.org/gallery/) | [站点](https://graphviz.org/) | — |
| [d3-force](https://github.com/d3/d3-force) | 力导向模拟。<br>自由关系网络、动态关系图。 | [仓库](https://github.com/d3/d3-force) | [展示页](https://observablehq.com/collection/@d3/d3-force) | — | — |
| [Graphology](https://graphology.github.io/) | 图数据操作与算法生态。<br>关系分析、节点指标、图结构处理。 | [仓库](https://github.com/graphology/graphology) | 待收集 | [站点](https://graphology.github.io/) | — |
| [Cytoscape Complexity Management](https://github.com/iVis-at-Bilkent/cytoscape.js-complexity-management) | 大型复合图的展开、折叠与关系管理（Cytoscape.js 扩展）。<br>层次化复杂网络；节点、边及聚合关系的管理。 | [仓库](https://github.com/iVis-at-Bilkent/cytoscape.js-complexity-management) | 待收集 | — | README 带有演示链接，但地址没有拿到；需要 Cytoscape.js 3.2.0 以上以及 fcose、cmgm.js，README 称尚未发布到 npm 和 bower。 |
| [Cytoscape Expand Collapse](https://github.com/iVis-at-Bilkent/cytoscape.js-expand-collapse) | 复合节点的展开与折叠（Cytoscape.js 扩展）。<br>折叠复合节点及其内部的边。README 提供三个演示：基础版、可撤销版、同时折叠边和节点。 | [仓库](https://github.com/iVis-at-Bilkent/cytoscape.js-expand-collapse) | 待收集 | — | 已停止维护；npm README 称仓库不再维护，并指向同一团队的 cytoscape.js-complexity-management（搜索结果摘要）。 |

### 图形描述语言与模型驱动技术

<sub>L1/diagram-languages</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Mermaid](https://mermaid.js.org/) | 文本生成流程、时序、状态、结构图，适合 Markdown 文档。<br>快速将结构化文本转换为可读图形。 | [仓库](https://github.com/mermaid-js/mermaid) | [展示页](https://mermaid.live/) | [站点](https://mermaid.js.org/) | — |
| [PlantUML](https://plantuml.com/) | UML、时序、架构、组件等软件工程图。<br>软件工程图的文本描述。 | [仓库](https://github.com/plantuml/plantuml) | 待收集 | [站点](https://plantuml.com/) | — |
| [D2](https://d2lang.com/) | 声明式图形描述、容器嵌套、自动布局。<br>容器嵌套的文本描述。 | [仓库](https://github.com/terrastruct/d2) | [展示页](https://play.d2lang.com/) | [站点](https://d2lang.com/) | — |
| [Structurizr DSL](https://github.com/structurizr/dsl) | 统一 C4 架构模型及多视角定义。<br>把模型与视图分离：一份结构模型可以定义多张不同视角的图。 | [仓库](https://github.com/structurizr/dsl) | [展示页](https://docs.structurizr.com/example) | — | — |
| [LikeC4](https://likec4.dev/)<br>（主分类 L2/software-architecture） | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 | [仓库](https://github.com/likec4/likec4) | [展示页](https://likec4.dev/showcases/bigbank/) | [站点](https://likec4.dev/) | — |

### 二维无限画布与三维空间技术

<sub>L1/canvas-2d-and-3d</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Excalidraw](https://github.com/excalidraw/excalidraw) | 可嵌入、可编辑的二维无限白板。<br>偏向人工绘图、自由表达、构思与注释。 | [仓库](https://github.com/excalidraw/excalidraw) | [展示页](https://excalidraw.com/) | — | — |
| [tldraw](https://github.com/tldraw/tldraw) | 无限画布 SDK：自定义对象、多人协作。<br>无限画布上的自定义对象与协作。 | [仓库](https://github.com/tldraw/tldraw) | [展示页](https://examples.tldraw.com/) | — | 含附加条件的许可证；SDK 生产使用需符合其专有许可条件。 |
| [Three.js](https://github.com/mrdoob/three.js) | 通用三维场景渲染。<br>结构语义、布局和交互需自行构建。 | [仓库](https://github.com/mrdoob/three.js) | [展示页](https://threejs.org/examples/) | — | — |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | React 三维组件开发，基于 Three.js。<br>用 React 组织三维场景。 | [仓库](https://github.com/pmndrs/react-three-fiber) | [展示页](https://r3f.docs.pmnd.rs/getting-started/examples) | — | — |
| [React Force Graph](https://github.com/vasturiano/react-force-graph) | 2D、3D、VR、AR 关系图。<br>官方示例含点击展开折叠、相机聚焦、方向箭头、动态数据和不同空间模式，对复杂图的空间交互有参考价值。 | [仓库](https://github.com/vasturiano/react-force-graph) | [展示页](https://vasturiano.github.io/react-force-graph/) | — | — |
| [Cosmos.gl](https://github.com/cosmosgl/graph) | GPU 加速的力导向图。<br>使用 GPU 做布局计算与图形渲染，面向大规模网络。 | [仓库](https://github.com/cosmosgl/graph) | 待收集 | [文档](https://openjsf.org/blog/introducing-cosmos-gl) | — |

## L2 特定结构与数据的专项可视化项目

### 代码依赖与模块解耦

<sub>L2/code-dependencies</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [dependency-cruiser](https://sverweij.github.io/dependency-cruiser/) | JavaScript/TypeScript 模块依赖分析。<br>依赖图、架构边界规则、违规依赖诊断。 | [仓库](https://github.com/sverweij/dependency-cruiser) | [展示页](https://sverweij.github.io/dependency-cruiser-repro-repo/458/) | [站点](https://sverweij.github.io/dependency-cruiser/) | 展示页是作者的 3D 图报告插件演示（issue 458），用它自己的源码和 React 仓库生成。 |
| [Madge](https://github.com/pahen/madge) | JavaScript 模块引用分析。<br>自动生成依赖关系图、发现循环依赖。 | [仓库](https://github.com/pahen/madge) | 待收集 | — | — |
| [pydeps](https://github.com/thebjorn/pydeps) | Python 模块导入分析。<br>导入网络、模块聚类、依赖结构。 | [仓库](https://github.com/thebjorn/pydeps) | 待收集 | — | — |

### 软件架构与代码理解

<sub>L2/software-architecture</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CodeBoarding](https://github.com/CodeBoarding/CodeBoarding) | 源码结构及架构语义分析。<br>自动归纳组件，形成分层架构解释与可视化。 | [仓库](https://github.com/CodeBoarding/CodeBoarding) | 待收集 | — | — |
| [Understand Anything](https://understand-anything.com/) | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 | [仓库](https://github.com/Egonex-AI/Understand-Anything) | [展示页](https://understand-anything.com/) | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析。 |
| [LikeC4](https://likec4.dev/) | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 | [仓库](https://github.com/likec4/likec4) | [展示页](https://likec4.dev/showcases/bigbank/) | [站点](https://likec4.dev/) | — |

### 流程、状态机与任务依赖

<sub>L2/workflows-and-state-machines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [bpmn-js](https://github.com/bpmn-io/bpmn-js) | BPMN 流程模型的查看、编辑与扩展。<br>建立在 diagram-js 之上，可通过扩展机制增加覆盖层、标记和自定义交互。 | [仓库](https://github.com/bpmn-io/bpmn-js) | [展示页](https://demo.bpmn.io/) | — | — |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble)<br>（主分类 L2/ai-and-multi-agent） | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 待收集 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |

### Agent 与多智能体协作

<sub>L2/ai-and-multi-agent</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble) | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 待收集 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AgentPrism](https://github.com/evilmartians/agent-prism) | 可嵌入应用的 React Agent Trace UI 组件。<br>层次化调用树、执行时间、工具与模型调用；独立可复用的 Trace UI 设计。 | [仓库](https://github.com/evilmartians/agent-prism) | [展示页](https://agent-prism.evilmartians.io/) | [文档](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces) | Alpha；项目公开标注为 Alpha。 |

### Trace、调用链与执行过程

<sub>L2/traces-and-timelines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [OpenTelemetry GenAI 语义约定](https://github.com/open-telemetry/semantic-conventions) | 规定如何描述 AI / Agent / 工具调用等遥测事件。<br>数据到可视化链条的起点：Span、事件、属性、父子关系。 | [仓库](https://github.com/open-telemetry/semantic-conventions) | 待收集 | [文档](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | 生成式 AI 语义约定仍在演进。建库时记录具体版本和字段定义，不要当成永远稳定的统一标准。 |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | 为 LLM 应用采集追踪数据。<br>数据采集端。 | [仓库](https://github.com/traceloop/openllmetry) | 待收集 | — | — |
| [Jaeger](https://github.com/jaegertracing/jaeger) | 分布式 Trace 的采集、检索和可视化。<br>Trace 瀑布图等传统调用链视图。 | [仓库](https://github.com/jaegertracing/jaeger) | [展示页](https://www.jaegertracing.io/demo/) | — | Jaeger v1 已于 2025-12-31 终止支持，应使用 v2（官网文档摘要）。 |
| [Grafana Tempo](https://github.com/grafana/tempo) | Trace 后端，与服务图、指标视图整合。<br>Trace 与服务图、指标的联动。 | [仓库](https://github.com/grafana/tempo) | 待收集 | — | — |
| [AeroGraph](https://github.com/sgcpu/aerograph) | 面向自主 AI 工作流的调试与观测层：本地优先、只追加、可安全回放的存储。<br>ReactFlow 的 Trace 图，支持逐步回放和失败高亮；可从任意 span 分叉出另一条时间线，并用 Myers diff 比较两次运行在哪里分岔；追踪循环和幻觉式的 Agent 交接。 | [仓库](https://github.com/sgcpu/aerograph) | 待收集 | — | 不在调研报告里，来自前期收集，信息取自搜索到的 GitHub README。是早期的小众项目，成熟度和循环检测的实现方式未核实。 |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble)<br>（主分类 L2/ai-and-multi-agent） | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 待收集 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AgentPrism](https://github.com/evilmartians/agent-prism)<br>（主分类 L2/ai-and-multi-agent） | 可嵌入应用的 React Agent Trace UI 组件。<br>层次化调用树、执行时间、工具与模型调用；独立可复用的 Trace UI 设计。 | [仓库](https://github.com/evilmartians/agent-prism) | [展示页](https://agent-prism.evilmartians.io/) | [文档](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces) | Alpha；项目公开标注为 Alpha。 |

### 数据血缘

<sub>L2/data-lineage</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Marquez](https://marquezproject.ai/) | 数据集、数据任务与血缘关系。<br>上下游关系、运行历史。 | [仓库](https://github.com/MarquezProject/marquez) | 待收集 | [站点](https://marquezproject.ai/) | — |
| [DataHub](https://github.com/datahub-project/datahub)<br>（主分类 L3/data-and-infrastructure） | 数据发现、治理与影响分析。<br>数据集、字段、流水线的血缘；从资产详情进入上下游影响网络，支持字段级钻取和影响分析。 | [仓库](https://github.com/datahub-project/datahub) | [展示页](https://datahub.com/demos/data-lineage-with-datahub/) | [文档](https://docs.datahub.com/) | 该展示页是录制的血缘功能演示，不是开放试用。 |
| [OpenMetadata](https://github.com/open-metadata/OpenMetadata)<br>（主分类 L3/data-and-infrastructure） | 数据资产管理与治理。<br>资产关系、字段级血缘；从数据目录导航到血缘关系。 | [仓库](https://github.com/open-metadata/OpenMetadata) | [展示页](https://sandbox.open-metadata.org/) | [文档](https://docs.open-metadata.org/latest/quick-start/sandbox) | 沙盒需要用 Google 账号登录。 |

### 系统服务拓扑与基础设施

<sub>L2/infrastructure-topology</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Apache SkyWalking](https://skywalking.apache.org/)<br>（主分类 L3/data-and-infrastructure） | 服务性能监控与故障诊断。<br>服务、实例、接口、部署等层级；从宏观服务拓扑进入监控、日志与 Trace，多视图联动。其生态中出现了基础设施三维可视化的探索。 | [仓库](https://github.com/apache/skywalking) | 待收集 | [站点](https://skywalking.apache.org/) · [文档](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/) | 官网首页链接到在线 Demo（示例数据）；其 Horizon UI 有基础设施 3D 地图（官方博客 2026-06）。 |
| [Kiali](https://github.com/kiali/kiali)<br>（主分类 L3/data-and-infrastructure） | 服务网格运行观察。<br>流量图、服务关系、异常定位。 | [仓库](https://github.com/kiali/kiali) | 待收集 | [文档](https://kiali.io/docs/features/topology/) | — |

### 知识、文档与认知地图

<sub>L2/knowledge-and-cognition</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [NeoDash](https://github.com/neo4j-contrib/neodash) | 使用 Neo4j 图数据库查询构建交互看板。<br>图数据查询驱动的看板。 | [仓库](https://github.com/neo4j-contrib/neodash) | [展示页](https://neodash-gallery.graphapp.io/) | — | 维护状态待核查；相关仓库存在维护状态变化，需要明确标注。 |
| [Excalidraw](https://github.com/excalidraw/excalidraw)<br>（主分类 L1/canvas-2d-and-3d） | 可嵌入、可编辑的二维无限白板。<br>偏向人工绘图、自由表达、构思与注释。 | [仓库](https://github.com/excalidraw/excalidraw) | [展示页](https://excalidraw.com/) | — | — |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 | [仓库](https://github.com/Egonex-AI/Understand-Anything) | [展示页](https://understand-anything.com/) | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析。 |
| [AFFiNE](https://affine.pro/)<br>（主分类 L3/knowledge-workspaces） | 文档、知识库与无限白板。<br>将线性文本与空间组织结合。 | [仓库](https://github.com/toeverything/AFFiNE) | 待收集 | [站点](https://affine.pro/) | — |
| [Logseq](https://github.com/logseq/logseq)<br>（主分类 L3/knowledge-workspaces） | 双向链接、页面及知识块。<br>大纲、链接和知识图导航。 | [仓库](https://github.com/logseq/logseq) | [展示页](https://demo.logseq.com/) | — | — |
| [InfraNodus](https://infranodus.com/)<br>（主分类 L3/knowledge-workspaces） | 文本网络与结构探索。<br>文本与概念的网络、主题群落、结构空白分析。 | [仓库](https://github.com/noduslabs/infranodus) | [展示页](https://infranodus.com/graphs) | [站点](https://infranodus.com/) | 商业产品；GitHub 公共仓库包含较早期代码，不能等同于当前商业产品的全部功能。 |

### 技术生态与商业产品地图

<sub>L2/technology-landscapes</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CNCF Landscape2](https://github.com/cncf/landscape2) | 基于结构化数据生成可筛选、可搜索的生态分类景观。<br>生态地图的数据组织和交互导航。 | [仓库](https://github.com/cncf/landscape2) | [展示页](https://landscape.cncf.io/) | — | — |
| [Zalando Tech Radar](https://github.com/zalando/tech-radar) | 使用技术雷达表达技术采用阶段与类别。<br>技术决策状态的雷达表达。 | [仓库](https://github.com/zalando/tech-radar) | [展示页](https://opensource.zalando.com/tech-radar/) | — | — |
| [Build Your Own Radar](https://github.com/thoughtworks/build-your-own-radar) | 从结构化技术条目生成交互技术雷达。<br>技术雷达生成器。 | [仓库](https://github.com/thoughtworks/build-your-own-radar) | [展示页](https://radar.thoughtworks.com/) | — | 官方托管版要求使用 Technology Radar 固定的象限和环名称，自定义名称需自行部署；据搜索结果为 AGPL 许可。 |

### 三维、高维与大规模关系探索

<sub>L2/spatial-and-high-dimensional</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [PyGraphistry](https://github.com/graphistry/pygraphistry) | 将图分析数据接入 GPU 图探索环境。<br>GPU 图探索。 | [仓库](https://github.com/graphistry/pygraphistry) | [展示页](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html) | — | — |
| [Embedding Projector](https://projector.tensorflow.org/) | 将高维向量降维到二维、三维，探索相似性与聚类。<br>高维结构投影后哪些信息被保留、哪些被扭曲。 | [仓库](https://github.com/tensorflow/embedding-projector) | [展示页](https://projector.tensorflow.org/) | — | 三维位置来自降维计算，不应理解为概念在原始高维语义空间中的真实坐标。 |
| [deck.gl](https://github.com/visgl/deck.gl)<br>（主分类 L1/chart-and-visualization-engines） | GPU 加速的大数据可视化框架。<br>大规模数据、地图图层、多视角渲染。 | [仓库](https://github.com/visgl/deck.gl) | [展示页](https://deck.gl/gallery/) | — | — |
| [React Force Graph](https://github.com/vasturiano/react-force-graph)<br>（主分类 L1/canvas-2d-and-3d） | 2D、3D、VR、AR 关系图。<br>官方示例含点击展开折叠、相机聚焦、方向箭头、动态数据和不同空间模式，对复杂图的空间交互有参考价值。 | [仓库](https://github.com/vasturiano/react-force-graph) | [展示页](https://vasturiano.github.io/react-force-graph/) | — | — |
| [Cosmos.gl](https://github.com/cosmosgl/graph)<br>（主分类 L1/canvas-2d-and-3d） | GPU 加速的力导向图。<br>使用 GPU 做布局计算与图形渲染，面向大规模网络。 | [仓库](https://github.com/cosmosgl/graph) | 待收集 | [文档](https://openjsf.org/blog/introducing-cosmos-gl) | — |

## L3 成熟应用与综合交互系统

### AI 应用与工作流开发平台

<sub>L3/ai-development-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Dify](https://dify.ai/) | 构建、发布、运行 AI 应用。<br>工作流、知识检索及执行观察；节点编辑、测试、节点结果检查、应用管理。 | [仓库](https://github.com/langgenius/dify) | 待收集 | [站点](https://dify.ai/) | 含附加条件的许可证；使用定制许可证，不能简单标为标准 Apache-2.0。 |
| [Langflow](https://www.langflow.org/) | 构建和发布 Agent 工作流。<br>可视节点编排与执行测试；编辑、Playground、调试、API 发布的闭环。据官方文档可发布为 API 或 MCP 服务，并与可观测性平台集成。 | [仓库](https://github.com/langflow-ai/langflow) | 待收集 | [站点](https://www.langflow.org/) · [文档](https://docs.langflow.org/) | — |
| [n8n](https://github.com/n8n-io/n8n) | 通用业务自动化及 AI 工作流。<br>自动化流程设计与执行诊断；节点编辑、运行历史、失败定位、重新执行。 | [仓库](https://github.com/n8n-io/n8n) | [展示页](https://n8n.io/workflows/) | — | 源码可见但有使用限制；官方明确将自身归为 fair-code / source-available，不是 OSI 意义上的开源软件。 |
| [Node-RED](https://github.com/node-red/node-red) | 事件驱动流程与设备、服务集成。<br>消息流的可视编排；部署、调试、运行时数据观察。 | [仓库](https://github.com/node-red/node-red) | [展示页](https://flows.nodered.org/) | — | — |
| [Flowise](https://flowiseai.com/) | LLM、工具与 Agent 流程构建。<br>Agentflow 图编辑器；条件、循环、状态与工具节点。 | [仓库](https://github.com/FlowiseAI/Flowise) | 待收集 | [站点](https://flowiseai.com/) · [文档](https://docs.flowiseai.com/) | 维护状态待核查；报告称原始 GitHub 仓库存在归档状态，需核查当前版本和维护主体，不能把历史仓库与持续运营的服务直接等同。 |

### Agent 开发、协作与管理平台

<sub>L3/agent-management</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AgentScope 2.0](https://github.com/agentscope-ai/agentscope) | Agent 团队编排、运行和观测。<br>团队及执行信息进入 Web UI；Agent 团队运行与实时观察。 | [仓库](https://github.com/agentscope-ai/agentscope) | 待收集 | [文档](https://docs.agentscope.io/observe-and-evaluate) | 旧版独立 AgentScope Studio 已不再单独维护，研究应以 2.0 的当前能力为主。搜索到的 AgentScope Studio 文档仍写“快速迭代中”，与报告“不再单独维护”的说法不一致，待核查。 |
| [LangGraph / Studio](https://github.com/langchain-ai/langgraph) | 图状态、任务路由与 Agent 开发。<br>图结构与运行状态、调试会话之间的关联。 | [仓库](https://github.com/langchain-ai/langgraph) | 待收集 | [文档](https://docs.langchain.com/langsmith/studio) | LangGraph Studio / LangSmith Studio 有账号及运行环境要求。 |
| [AgentEnsemble](https://agentensemble.github.io/agentensemble/) | 团队任务编排和执行分析。<br>DAG、时间图、通过事件流实时更新的执行看板，以及人工审核交互，把任务执行事件与人工干预放进同一过程。 | [仓库](https://github.com/AgentEnsemble/agentensemble) | 待收集 | [站点](https://agentensemble.github.io/agentensemble/) · [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AutoGen / AutoGen Studio](https://github.com/microsoft/autogen) | Agent 原型构建与团队交互。<br>智能体团队的可视化原型、运行测试；Studio 定位为原型，不是生产级应用。 | [仓库](https://github.com/microsoft/autogen) | 待收集 | [文档](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html) | — |

### LLM 与 Agent 可观测性平台

<sub>L3/observability-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Langfuse](https://github.com/langfuse/langfuse) | 追踪、评测、提示词管理、数据集及实验。<br>Trace、调用详情、耗时、Token、成本及评测。可从一次异常执行进入提示词、测试数据和评测过程，形成分析、修改、再验证的闭环。 | [仓库](https://github.com/langfuse/langfuse) | [展示页](https://langfuse.com/docs/demo) | — | — |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | AI 应用追踪与质量评测。<br>基于 OpenTelemetry 的调用轨迹、问题诊断、评测分析。 | [仓库](https://github.com/Arize-ai/phoenix) | [展示页](https://phoenix-demo.arize.com/) | — | — |
| [Comet Opik](https://www.comet.com/site/products/opik/) | LLM / Agent 追踪、评测和监控。<br>多层调用、评测结果、运行监控。 | [仓库](https://github.com/comet-ml/opik) | 待收集 | [站点](https://www.comet.com/site/products/opik/) | — |
| [AgentOps](https://www.agentops.ai/) | Agent 执行记录、调试与成本观察。<br>会话回放、调用轨迹、成本。 | [仓库](https://github.com/AgentOps-AI/agentops) | 待收集 | [站点](https://www.agentops.ai/) · [文档](https://docs.agentops.ai/v2/introduction) | — |
| [LangWatch](https://langwatch.ai/) | LLM 运行追踪、分析与评测。<br>Trace、质量指标与运行分析。 | [仓库](https://github.com/langwatch/langwatch) | 待收集 | [站点](https://langwatch.ai/) | — |

### 软件架构、开发者平台与工程管理

<sub>L3/software-engineering-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Nx](https://github.com/nrwl/nx) | Monorepo 构建与任务管理。<br>把组成结构和任务结构分开：Project Graph 表示项目间依赖，Task Graph 表示实际构建任务及执行依赖。可聚焦项目、查看邻近项目、按文件夹分组、分析影响范围、导出图数据。 | [仓库](https://github.com/nrwl/nx) | 待收集 | [文档](https://nx.dev/docs/features/explore-graph) | — |
| [Backstage](https://github.com/backstage/backstage) | 开发者门户与软件服务目录。<br>Catalog Graph：实体中心视角，按关系和实体类别筛选，控制展开深度、方向和连线合并，并与实体详情联动。 | [仓库](https://github.com/backstage/backstage) | [展示页](https://demo.backstage.io/catalog) | [文档](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/) | 官方强调服务目录反映的是便于人理解的组织与软件模型，而不是所有实时关系的唯一真实来源。公开 Demo 站点上是否启用了关系图未确认。 |
| [Structurizr DSL](https://github.com/structurizr/dsl)<br>（主分类 L1/diagram-languages） | 统一 C4 架构模型及多视角定义。<br>把模型与视图分离：一份结构模型可以定义多张不同视角的图。 | [仓库](https://github.com/structurizr/dsl) | [展示页](https://docs.structurizr.com/example) | — | — |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 | [仓库](https://github.com/Egonex-AI/Understand-Anything) | [展示页](https://understand-anything.com/) | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析。 |
| [LikeC4](https://likec4.dev/)<br>（主分类 L2/software-architecture） | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 | [仓库](https://github.com/likec4/likec4) | [展示页](https://likec4.dev/showcases/bigbank/) | [站点](https://likec4.dev/) | — |

### 数据平台与基础设施管理

<sub>L3/data-and-infrastructure</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [DataHub](https://github.com/datahub-project/datahub) | 数据发现、治理与影响分析。<br>数据集、字段、流水线的血缘；从资产详情进入上下游影响网络，支持字段级钻取和影响分析。 | [仓库](https://github.com/datahub-project/datahub) | [展示页](https://datahub.com/demos/data-lineage-with-datahub/) | [文档](https://docs.datahub.com/) | 该展示页是录制的血缘功能演示，不是开放试用。 |
| [OpenMetadata](https://github.com/open-metadata/OpenMetadata) | 数据资产管理与治理。<br>资产关系、字段级血缘；从数据目录导航到血缘关系。 | [仓库](https://github.com/open-metadata/OpenMetadata) | [展示页](https://sandbox.open-metadata.org/) | [文档](https://docs.open-metadata.org/latest/quick-start/sandbox) | 沙盒需要用 Google 账号登录。 |
| [Apache SkyWalking](https://skywalking.apache.org/) | 服务性能监控与故障诊断。<br>服务、实例、接口、部署等层级；从宏观服务拓扑进入监控、日志与 Trace，多视图联动。其生态中出现了基础设施三维可视化的探索。 | [仓库](https://github.com/apache/skywalking) | 待收集 | [站点](https://skywalking.apache.org/) · [文档](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/) | 官网首页链接到在线 Demo（示例数据）；其 Horizon UI 有基础设施 3D 地图（官方博客 2026-06）。 |
| [Kiali](https://github.com/kiali/kiali) | 服务网格运行观察。<br>流量图、服务关系、异常定位。 | [仓库](https://github.com/kiali/kiali) | 待收集 | [文档](https://kiali.io/docs/features/topology/) | — |
| [Grafana](https://github.com/grafana/grafana) | 观测数据看板与分析。<br>指标、日志、Trace、服务关系。 | [仓库](https://github.com/grafana/grafana) | [展示页](https://play.grafana.org/) | — | — |

### 知识组织、概念地图与认知工具

<sub>L3/knowledge-workspaces</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AFFiNE](https://affine.pro/) | 文档、知识库与无限白板。<br>将线性文本与空间组织结合。 | [仓库](https://github.com/toeverything/AFFiNE) | 待收集 | [站点](https://affine.pro/) | — |
| [diagrams.net / draw.io](https://www.drawio.com/) | 通用结构图创建与编辑。<br>手动构造架构图、流程图、认知图。 | [仓库](https://github.com/jgraph/drawio) | [展示页](https://www.drawio.com/docs/diagram-types/) | [站点](https://www.drawio.com/) | — |
| [Kumu](https://kumu.io/) | 复杂系统、利益相关方和关系地图。<br>关系探索、视图定义、叙事展示。研究对象与软件流程编辑器明显不同。 | — | [展示页](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative) | [站点](https://kumu.io/) · [文档](https://docs.kumu.io/frequently-asked-questions/where-can-i-find-example-kumu-projects) | 商业产品；不能直接二次开发；作为可体验的交互案例收录。 |
| [Logseq](https://github.com/logseq/logseq) | 双向链接、页面及知识块。<br>大纲、链接和知识图导航。 | [仓库](https://github.com/logseq/logseq) | [展示页](https://demo.logseq.com/) | — | — |
| [InfraNodus](https://infranodus.com/) | 文本网络与结构探索。<br>文本与概念的网络、主题群落、结构空白分析。 | [仓库](https://github.com/noduslabs/infranodus) | [展示页](https://infranodus.com/graphs) | [站点](https://infranodus.com/) | 商业产品；GitHub 公共仓库包含较早期代码，不能等同于当前商业产品的全部功能。 |

### 生态地图与产业分析产品

<sub>L3/market-and-ecosystem-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CNCF Landscape](https://landscape.cncf.io/) | 大型生态分类数据与实际展示案例。<br>浏览技术类别、生态参与者、项目属性；表达分类与生态分布，不擅长展示大量跨类别依赖。 | [仓库](https://github.com/cncf/landscape) | [展示页](https://landscape.cncf.io/) | — | — |
| [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar) | 技术采用建议与趋势。<br>表达经过研究者判断的技术采用建议，而不是技术、产品、需求之间的完整关系。 | — | [展示页](https://www.thoughtworks.com/radar) | — | — |
| [OSS Insight](https://ossinsight.io/) | GitHub 项目和开发生态数据分析。<br>研究 GitHub 活跃度、生态指标及时间变化。 | [仓库](https://github.com/pingcap/ossinsight) | [展示页](https://ossinsight.io/) | — | — |
| [OSS Compass](https://oss-compass.org/) | 开源项目健康与生态指标分析。<br>多指标比较开源项目的生态表现。 | [仓库](https://github.com/oss-compass/compass-web) | [展示页](https://oss-compass.org/) | — | — |

## 第四板块 结构提炼与认知建模

### 结构提取

<sub>cognition/information-extraction</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Tree-sitter](https://github.com/tree-sitter/tree-sitter) | 程序源代码的语法树与增量解析。<br>输入是源码。语法事实不直接等于架构语义。 | [仓库](https://github.com/tree-sitter/tree-sitter) | [展示页](https://tree-sitter.github.io/tree-sitter/7-playground.html) | — | — |
| [Docling](https://github.com/docling-project/docling) | PDF、文档等的版面、标题、表格及文档结构提取。<br>输入是文档。文档结构不等于知识结构。 | [仓库](https://github.com/docling-project/docling) | [展示页](https://huggingface.co/spaces/docling-project/SmolDocling-256M-Demo) | — | 展示页是 SmolDocling 视觉语言模型的演示，不是 Docling 库本身。 |
| [Docling Graph](https://github.com/docling-project/docling-graph) | 从结构化文档内容进一步提取结构化实体与关系。<br>需要约束关系类型和语义准确性。 | [仓库](https://github.com/docling-project/docling-graph) | 待收集 | — | — |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 | [仓库](https://github.com/Egonex-AI/Understand-Anything) | [展示页](https://understand-anything.com/) | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析。 |

### 多层知识建模

<sub>cognition/multilevel-knowledge-modeling</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) | 对非结构化文本做实体关系抽取、社区分层、社区摘要。<br>路径：文本片段、实体关系与声明提取、图社区发现与层级聚类、各层级社区摘要、全局与局部检索。图社区层级不等于认知的逻辑抽象层级，只能作为辅助，不能替代语义分层。 | [仓库](https://github.com/microsoft/graphrag) | 待收集 | [站点](https://microsoft.github.io/graphrag/) · [文档](https://microsoft.github.io/graphrag/visualization_guide/) | 维护模式；官方文档显示仓库主要处于维护模式，适合作为研究参考，不能默认仍在持续扩展新功能。官方可视化指南建议把图导出为 GraphML 后用 Gephi 查看，没有专门的可视化器。 |
| [LightRAG](https://github.com/HKUDS/LightRAG) | 图结构检索与知识网络可视化。<br>检索结构与认知模型并不完全相同。 | [仓库](https://github.com/HKUDS/LightRAG) | 待收集 | — | — |

### 动态与演化的知识结构

<sub>cognition/evolving-knowledge-structures</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Graphiti](https://github.com/getzep/graphiti) | 带时间属性的实体和关系，保留来源。<br>时间化事实、原始 Episode、增量知识更新、显式或学习得到的关系类型；能区分“过去成立”“现在成立”和“存在冲突”。 | [仓库](https://github.com/getzep/graphiti) | 待收集 | [文档](https://help.getzep.com/graphiti/getting-started/overview) | — |

## 项目之间的关系

只记录报告或官方文档明确说明的关系。

| 项目 | 关系 | 对象 | 依据 |
| --- | --- | --- | --- |
| bpmn-js | uses | diagram-js | 报告：存在已明确的技术继承关系。 |
| CNCF Landscape2 | generates | CNCF Landscape | 报告：生成框架与具体景观实例之间的关系。 |
| AgentPrism | consumes | OpenTelemetry GenAI 语义约定 | 报告：AgentPrism 支持消费相关格式的数据。 |
| AgentEnsemble Viz | part-of | AgentEnsemble | 报告：AgentEnsemble 的可视化组件。 |
| React Three Fiber | uses | Three.js | 报告：基于 Three.js。 |
| Sigma.js | works-with | Graphology | 报告：Sigma.js 与 Graphology 配合。 |
| LikeC4 | compares-with | Structurizr DSL | 报告：二者都把模型与视图分离。 |
| Cytoscape Complexity Management | succeeds | Cytoscape Expand Collapse | expand-collapse 的 npm README 称不再维护，并指向 complexity-management（搜索结果摘要）。 |

## 上游 Awesome 清单

| 上游清单 | 优先用于 |
| --- | --- |
| [Awesome Dataviz](https://github.com/hal9ai/awesome-dataviz) | 板块 1：图表范式、视觉技术。 |
| [Awesome Node-Based UIs](https://github.com/xyflow/awesome-node-based-uis) | 板块 2 L1：节点图、编辑器与图交互。 |
| [Awesome Architecture Diagrams](https://github.com/hudsonkit/awesome-architecture-diagrams) | 板块 1 与 L2：架构表达。 |
| [Awesome Agent Observability](https://github.com/anhermon/awesome-agent-observability) | L2 / L3：Agent Trace 与可观测性。 |
| [Awesome LLM Observability](https://github.com/ContextJet-ai/awesome-llm-observability) | L2 / L3：LLM 运行与调试平台。 |
| [Awesome Multi-Agent Projects](https://github.com/xxiaoxiong/awesome-multi-agent-projects) | L3：多 Agent 真实系统与案例。 |
| [CNCF Landscape2](https://github.com/cncf/landscape2) | L2 / L3：技术生态地图。 |
| [Awesome AI Agents（e2b）](https://github.com/e2b-dev/awesome-ai-agents) | L3：AI Agent 项目全景，开源与闭源分开列出。前期提到的 Awesome AI Agents（搜索得到，未核对是否同一份）。 |
| [Awesome Multi-Agent Orchestrators](https://github.com/Agent-Analytics/awesome-multi-agent-orchestrators) | L3：多智能体编排器与运行时。搜索时找到，与前期提到的 Awesome Multi-Agent Workflows 不是同一份。 |
