# 板块 2 可视化技术与应用生态

这是整个库最大的实证主体。按技术抽象程度分三层。

| | L1 底层技术 | L2 专项可视化 | L3 综合应用 |
| --- | --- | --- | --- |
| 研究主体 | 一种通用能力或组件 | 一类特定数据与问题的可视化方案 | 一个完整的实际产品 |
| 典型输入 | 节点、边、表格、坐标、布局约束 | 代码依赖、Trace、知识关系、任务数据 | 用户任务、业务数据、系统运行状态 |
| 核心产出 | 画布、图形、编辑器、布局能力 | 可理解、可分析的专题视图 | 完整工作流程和交互体验 |
| 典型例子 | G6、React Flow、D3、ELK | 代码依赖图、Agent Trace Viewer | Dify、n8n、DataHub |
| 评价重点 | 灵活性、性能、复杂交互实现能力 | 数据语义、视图质量、分析能力 | 业务闭环、跨视图联动、工作效率 |

- [L1 底层可视化技术](L1-foundational-technologies/README.md)
- [L2 特定结构与数据的专项可视化项目](L2-specialized-visualizations/README.md)
- [L3 成熟应用与综合交互系统](L3-integrated-applications/README.md)

## 两个容易混淆的地方

1. **同一个项目可能横跨多个层级。** LikeC4 既有建模语言，也有架构可视化和完整的交互查看器；Langfuse 的 Trace Viewer 是一项专项可视化能力，但 Langfuse 整体是综合可观测性产品。库里记录项目的主要定位，用 `also` 记录其他定位，避免同一资料复制多处。
2. **三个层级之间不一定存在代码依赖。** 如果没有核实源码，不应因为两个产品采用类似的图形，就认定上层产品使用了某个底层库。真实依赖只在有源码或官方文档证据时记录。

## 跨层索引：同一个问题，从底层技术到成熟应用

三列表示同一研究方向在不同抽象层级上的代表，不代表右侧产品一定使用左侧项目的源码。没有链接的是泛称，不是具体项目。

<!-- gen:matrix: -->
| 研究方向 | L1 通用技术能力 | L2 专项项目或可视化 | L3 综合应用 |
| --- | --- | --- | --- |
| 软件架构 | [AntV G6](https://g6.antv.antgroup.com/)、[ELK.js](https://github.com/kieler/elkjs)、[Graphviz](https://graphviz.org/) | [dependency-cruiser](https://sverweij.github.io/dependency-cruiser/)、[CodeBoarding](https://codeboarding.org/) | [Nx](https://github.com/nrwl/nx)、[LikeC4](https://likec4.dev/)、[Backstage](https://github.com/backstage/backstage) |
| 业务流程 | [diagram-js](https://github.com/bpmn-io/diagram-js)、[React Flow](https://reactflow.dev/)、[AntV X6](https://github.com/antvis/X6) | [bpmn-js](https://github.com/bpmn-io/bpmn-js)、流程运行视图 | [Node-RED](https://github.com/node-red/node-red)、[n8n](https://github.com/n8n-io/n8n)、[Dify](https://dify.ai/) |
| Agent 协作 | 图引擎、布局、事件流 | [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble)、[AgentPrism](https://github.com/evilmartians/agent-prism) | [AgentScope 2.0](https://github.com/agentscope-ai/agentscope)、[LangGraph / Studio](https://github.com/langchain-ai/langgraph) |
| Trace | 时间线组件、数据查询与渲染 | [AgentPrism](https://github.com/evilmartians/agent-prism)、任务执行时间图 | [Langfuse](https://github.com/langfuse/langfuse)、[Arize Phoenix](https://github.com/Arize-ai/phoenix)、[Comet Opik](https://www.comet.com/site/products/opik/)、[Jaeger](https://github.com/jaegertracing/jaeger) |
| 数据血缘 | 图引擎、矩阵、布局算法 | 字段血缘图、数据依赖查看器 | [DataHub](https://github.com/datahub-project/datahub)、[OpenMetadata](https://github.com/open-metadata/OpenMetadata) |
| 服务拓扑 | 图布局、GPU 渲染 | 流量拓扑、服务关系视图 | [Kiali](https://github.com/kiali/kiali)、[Apache SkyWalking](https://skywalking.apache.org/) |
| 知识地图 | [D3.js](https://github.com/d3/d3)、[Sigma.js](https://www.sigmajs.org/)、无限画布 | 文本知识网络、概念抽取 | [AFFiNE](https://affine.pro/)、[Kumu](https://kumu.io/)、[Logseq](https://github.com/logseq/logseq) |
| 生态地图 | [D3.js](https://github.com/d3/d3)、[Apache ECharts](https://echarts.apache.org/)、筛选组件 | [CNCF Landscape2](https://github.com/cncf/landscape2)、[Build Your Own Radar](https://github.com/thoughtworks/build-your-own-radar) | [CNCF Landscape](https://landscape.cncf.io/)、[OSS Insight](https://ossinsight.io/) |
| 高维数据探索 | [UMAP（umap-learn）](https://github.com/lmcinnes/umap)、[openTSNE](https://github.com/pavlin-policar/openTSNE)、[regl-scatterplot](https://github.com/flekschas/regl-scatterplot)、[ScatterGL](https://github.com/PAIR-code/scatter-gl)、[Plotly.js](https://github.com/plotly/plotly.js) | [Embedding Projector](https://projector.tensorflow.org/)、[pca3d](https://rdrr.io/cran/pca3d/f/vignettes/pca3d.rmd)、[HiPlot](https://github.com/facebookresearch/hiplot)、[Facets](https://pair-code.github.io/facets/)、[KeplerMapper](https://github.com/scikit-tda/kepler-mapper)、[dtour](https://dtour.dev)、[Embedding Atlas](https://apple.github.io/embedding-atlas/)、[UpSet](https://upset.app/)、[Voyager](https://idl.uw.edu/papers/voyager) | [Nomic Atlas](https://docs.nomic.ai/atlas/datasets/data-maps/how-atlas-works/1-key_terms)、[Orange](https://orangedatamining.com/) |
| 三维与大规模关系探索 | [Three.js](https://github.com/mrdoob/three.js)、[3d-force-graph](https://github.com/vasturiano/3d-force-graph)、WebGL、GPU 图计算 | [React Force Graph](https://github.com/vasturiano/react-force-graph)、[PyGraphistry](https://github.com/graphistry/pygraphistry)、[VRNetzer](https://github.com/menchelab/VRNetzer)、iCAVE、[GeoGraphViz](https://github.com/ASUcicilab/GeoGraphViz) | 专业图探索与 AI 分析平台 |
<!-- /gen -->

## 看全部项目

[`catalog/INDEX.md`](../catalog/INDEX.md) 按层级和分类列出全部条目，包含开源项目与展示页。
