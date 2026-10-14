# 结构与图形范式的分类

这是第一板块的核心分类索引。按“结构加重点加任务”选画法，见 [怎么选画法](choosing-views.md)，那里的建议来自案例，并附证据。

| 结构家族 | 代表性图形 | 适合回答的问题 | 容易出问题的地方（整理者初稿，待核对） |
| --- | --- | --- | --- |
| 层级与包含 | 树状图、矩形树图、旭日图、冰柱图 | 什么包含什么？系统如何分层？ | 跨层级的横向关系看不出 |
| 一般关系网络 | 节点连线图、力导向图、弦图、邻接矩阵 | 谁和谁有关系？网络如何聚类？ | 网络变密后节点连线图易成“毛球”，矩阵更稳 |
| 依赖与拓扑 | 有向依赖图、DAG 图、设计结构矩阵 | 谁依赖谁？是否存在循环与耦合？ | 规模大时依赖图难读；矩阵需要排序才有信息 |
| 流程与控制 | 流程图、BPMN、泳道图、状态机图 | 一个过程如何分支、执行和转移？ | 并行和时间信息表达弱 |
| 时序与调用 | UML 时序图、Trace 瀑布图、甘特图、火焰图 | 谁在什么时间调用谁？耗时在哪里？ | 参与者多时时序图过宽；Trace 图看不出静态结构 |
| 流量与转化 | 桑基图、Alluvial 图、漏斗图 | 数量和资源如何流动、分配、转化？ | 节点和流太多时拥挤 |
| 多维属性 | 散点矩阵、平行坐标、雷达图、热力图、降维投影散点图、巡游、径向可视化、集合交集矩阵、拓扑摘要图 | 对象在哪些维度上存在差异？ | 降维后轴没有直接含义，距离和大小不能读；平行坐标的轴顺序影响能看到什么；详见[高维可视化](high-dimensional.md) |
| 空间与地理 | 地图、空间网络、3D 场景、高维几何的截面、沉浸式坐标轴 | 对象在真实或虚拟空间中的分布如何？ | 三维不一定比二维好（见[高维可视化](high-dimensional.md)） |
| 语义与知识 | 概念图、知识图谱、论证地图 | 概念之间有什么关系？判断有什么依据？ | 缺少统一语义时随意性大 |
| 动态与演化 | 动态网络、事件时间线、状态回放 | 系统如何随时间变化？ | |
| 多层与复合结构 | 嵌套复合图、多层网络、多视图架构图 | 如何同时理解整体、局部及跨层联系？ | 视图之间的一致性需要靠模型保证 |
| 因果与反馈（整理者补充） | 因果回路图、存量流量图 | 变量之间如何相互影响？有哪些反馈环？ | 容易画成“什么都连”，需要明确变量定义 |

前十一行来自调研报告；最后一行和“容易出问题的地方”一列是整理者的初稿，没有经过核验。

## 同一种结构，多种表示

即使处理的是相似的关系数据，选择不同的表示方式，就会形成完全不同的观察能力。例如依赖网络既可以画成节点连线图，也可以画成矩阵；层级结构加上大量跨节点连线，可以用层级边捆绑图；运行分析里的 Trace 瀑布图，把嵌套调用结构与时间信息结合。研究图形选择时，比较的是它们在具体任务上的表现，而不是视觉效果。

## 图形与展示页

“展示页”是能直接看到该图形效果的示例页。待收集的会逐步补上。

<!-- gen:forms: -->
| 结构家族 | 图形 | 展示页 |
| --- | --- | --- |
| 层级与包含 | 树状图 | [Tidy tree（D3）](https://observablehq.com/notebook-kit/ex/d3/tree) |
| 层级与包含 | 矩形树图 | [d3-hierarchy 集合，含 treemap（D3）](https://observablehq.com/collection/@d3/d3-hierarchy) |
| 层级与包含 | 旭日图 | [Zoomable sunburst（D3）](https://observablehq.com/@mbostock/d3-zoomable-sunburst) |
| 层级与包含 | 冰柱图 | [Icicle（D3）](https://observablehq.com/@d3/icicle/2) |
| 层级与包含 | 双曲树 | 待收集 |
| 一般关系网络 | 节点连线图 | [Sigma.js 示例](https://www.sigmajs.org/examples/) ✓ |
| 一般关系网络 | 力导向图 | [Force-directed graph（D3）](https://observablehq.com/@d3/force-directed-graph) |
| 一般关系网络 | 弦图 | [d3-chord 集合（D3）](https://observablehq.com/collection/@d3/d3-chord) |
| 一般关系网络 | 邻接矩阵 | [Vega-Lite adjacency matrix](https://observablehq.com/@vega/vega-lite-adjacency-matrix) |
| 一般关系网络 | 层级边捆绑图 | [Hierarchical edge bundling（D3）](https://observablehq.com/@d3/hierarchical-edge-bundling) |
| 依赖与拓扑 | 有向依赖图 | [dependency-cruiser 3D 图演示](https://sverweij.github.io/dependency-cruiser-repro-repo/458/) ✓ |
| 依赖与拓扑 | DAG 图 | [Dagre 交互演示](https://dagrejs.github.io/project/dagre-d3/latest/demo/interactive-demo.html) ✓ |
| 依赖与拓扑 | 设计结构矩阵 | [DSMweb：如何读 DSM](https://dsmweb.org/reading-a-dsm/) ✓ |
| 流程与控制 | 流程图 | [Mermaid 流程图](https://mermaid.js.org/syntax/flowchart.html) ✓ |
| 流程与控制 | BPMN | [bpmn.io 在线编辑器](https://demo.bpmn.io/) ✓ |
| 流程与控制 | 泳道图 | [draw.io 泳道流程图](https://www.drawio.com/docs/diagram-types/swimlane-diagrams/) ✓ |
| 流程与控制 | 状态机图 | [Mermaid 状态图](https://mermaid.js.org/syntax/stateDiagram.html) ✓ |
| 时序与调用 | UML 时序图 | [Mermaid 时序图](https://mermaid.js.org/syntax/sequenceDiagram.html) ✓ |
| 时序与调用 | Trace 瀑布图 | [Jaeger 在线演示](https://www.jaegertracing.io/demo/) ✓ |
| 时序与调用 | 甘特图 | [Mermaid 甘特图](https://mermaid.js.org/syntax/gantt.html) ✓ |
| 时序与调用 | 火焰图 | [Brendan Gregg 火焰图](https://www.brendangregg.com/flamegraphs.html) ✓ |
| 流量与转化 | 桑基图 | [d3-sankey 集合（D3）](https://observablehq.com/collection/@d3/d3-sankey) |
| 流量与转化 | Alluvial 图 | 待收集 |
| 流量与转化 | 漏斗图 | [Funnel charts（Plotly）](https://plotly.com/javascript/funnel-charts/) ✓ |
| 多维属性 | 散点矩阵 | [Scatterplot matrix（D3）](https://observablehq.com/@d3/splom/2)、[Brushable scatterplot matrix（D3）](https://observablehq.com/@d3/brushable-scatterplot-matrix) |
| 多维属性 | 平行坐标 | [Parallel coordinates（D3）](https://observablehq.com/notebook-kit/ex/d3/parallel-coordinates)、[Parallel coordinates（Plotly）](https://plotly.com/javascript/parallel-coordinates-plot/) ✓ |
| 多维属性 | 雷达图 | [Radar charts（Plotly）](https://plotly.com/javascript/radar-chart/) ✓ |
| 多维属性 | 热力图 | [D3.js Heatmap（社区笔记）](https://observablehq.com/@bbischof/d3-js-heatmap) |
| 多维属性 | 降维投影散点图 | [Embedding Projector](https://projector.tensorflow.org/)、[How to Use t-SNE Effectively（交互式文章）](https://distill.pub/2016/misread-tsne/) ✓ |
| 多维属性 | 巡游（Grand Tour） | [Visualizing Neural Networks with the Grand Tour（交互式文章）](https://distill.pub/2020/grand-tour/) ✓、[dtour](https://dtour.dev) ✓ |
| 多维属性 | 径向可视化（Radviz） | 待收集 |
| 多维属性 | 集合交集矩阵（UpSet） | [UpSet](https://upset.app/) ✓ |
| 多维属性 | 拓扑摘要图（Mapper） | [KeplerMapper 示例 notebook](https://kepler-mapper.scikit-tda.org/en/latest/notebooks/Cancer-demo.html) ✓ |
| 空间与地理 | 地图 | [deck.gl 图层示例](https://deck.gl/gallery/) ✓ |
| 空间与地理 | 空间网络 | [3D force-directed graph](https://vasturiano.github.io/3d-force-graph/) ✓ |
| 空间与地理 | 3D 场景 | [three.js 示例](https://threejs.org/examples/) ✓、[SkyWalking 3D 基础设施地图（交互演示）](https://skywalking.apache.org/3d-map-app/) ✓ |
| 空间与地理 | 高维几何的截面 | [Miegakure（四维解谜游戏）](https://miegakure.com) ✓ |
| 空间与地理 | 沉浸式坐标轴（VR） | 待收集 |
| 语义与知识 | 概念图 | 待收集 |
| 语义与知识 | 知识图谱 | [Understand Anything 演示](https://understand-anything.com/) ✓ |
| 语义与知识 | 论证地图 | [Argdown 第一个例子](https://argdown.org/guide/a-first-example.html) ✓ |
| 动态与演化 | 动态网络 | [Temporal force-directed graph（D3）](https://observablehq.com/@d3/temporal-force-directed-graph) |
| 动态与演化 | 事件时间线 | [Mermaid 时间线](https://mermaid.js.org/syntax/timeline.html) ✓ |
| 动态与演化 | 状态回放 | [21st.dev agent-trace 组件（时间线回放）](https://21st.dev/@n1m4mz/components/agent-trace) ✓ |
| 多层与复合结构 | 嵌套复合图 | [Cytoscape.js 复合图布局演示](https://js.cytoscape.org/demos/cose-bilkent-layout-compound/) ✓ |
| 多层与复合结构 | 多层网络 | 待收集 |
| 多层与复合结构 | 多视图架构图 | [LikeC4 Big Bank 示例](https://likec4.dev/showcases/bigbank/) ✓、[Structurizr C4 示例](https://docs.structurizr.com/example) ✓ |
| 因果与反馈 | 因果回路图 | [Kumu 因果回路图项目](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative) ✓ |
| 因果与反馈 | 存量流量图 | [Insight Maker 仿真模型（含浴缸、储蓄账户等存量流量例子）](https://www.insightmaker.com/tag/simulation?page=3) ✓ |
<!-- /gen -->
