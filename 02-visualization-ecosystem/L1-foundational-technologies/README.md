# L1 底层可视化技术

不能简单地把所有库并列。至少要区分图形渲染、关系图框架、布局计算、图形描述语言、空间引擎、交互画布六类。

> 项目事实和判断来自 2026-10 调研报告，未逐项核验。标 ✓ 的展示页已访问核对。

## 通用图形与数据可视化

区别主要在抽象程度。D3 给开发者较大的可视化设计自由；Vega-Lite 强调把可视化描述为声明式规格；ECharts、Plotly 提供大量现成图表；deck.gl 关注大数据规模下的图层组合与高性能渲染。

<!-- gen:catalog:L1/chart-and-visualization-engines -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [D3.js](https://github.com/d3/d3) | 底层数据驱动可视化工具集。<br>自定义视觉编码、层级、网络、布局与交互。 ✓ | [仓库](https://github.com/d3/d3 "核对依据：npm 包元数据") ✓ | [展示页](https://observablehq.com/collection/@d3/gallery) | — | 开源 |
| [Vega-Lite](https://github.com/vega/vega-lite) | 声明式可视化语法。<br>用结构化描述定义图表，而不是逐元素绘制。 ✓ | [仓库](https://github.com/vega/vega-lite "核对依据：npm 包元数据") ✓ | [展示页](https://vega.github.io/vega-lite/examples/) ✓ | — | 开源 |
| [Apache ECharts](https://echarts.apache.org/) | 综合图表引擎。<br>图表类型、交互组件、大屏和业务看板。 △ | [仓库](https://github.com/apache/echarts "核对依据：npm 包元数据") ✓ | [展示页](https://echarts.apache.org/examples) ✓ | [站点](https://echarts.apache.org/) | 开源；官方页面没找到依据的说明：业务看板 |
| [Plotly.js](https://github.com/plotly/plotly.js) | 数据探索与交互图表。<br>多维统计图、科学可视化、交互分析。 △ | [仓库](https://github.com/plotly/plotly.js "核对依据：npm 包元数据") ✓ | [展示页](https://plotly.com/javascript/) ✓ | — | 开源；官方页面没找到依据的说明：数据探索、交互、多维 |
| [deck.gl](https://github.com/visgl/deck.gl) | GPU 加速的大数据可视化框架。<br>大规模数据、地图图层、多视角渲染。 ✓ | [仓库](https://github.com/visgl/deck.gl "核对依据：npm 包元数据") ✓ | [展示页](https://deck.gl/gallery/) ✓ | — | 开源 |
| [regl-scatterplot](https://github.com/flekschas/regl-scatterplot) | 基于 WebGL 的交互式二维散点图，面向大量数据点。<br>几十万以上的点如何做到可缩放、可选择、可编码；投影结果的前端落地。 ✓ | [仓库](https://github.com/flekschas/regl-scatterplot "核对依据：npm 包元数据声明的仓库") ✓ | [展示页](https://flekschas.github.io/regl-scatterplot/) ✓ | — | 开源；展示页由 WebGL 渲染，页面文字只有标题；说明依据是 npm 包的 README。 |
<!-- /gen -->

## 关系图与节点交互引擎

与“复杂认知地图”关系最密切的一组。报告的初步判断：G6、Cytoscape.js 更值得用于研究复杂网络的结构呈现；React Flow、X6 更适合研究复杂节点编辑器与工作流应用；Sigma.js 是大型网络展示与探索的重要参考。这是按设计方向的归类，不是性能排名。

<!-- gen:catalog:L1/graph-and-node-engines -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AntV G6](https://g6.antv.antgroup.com/) | 通用关系图引擎：图布局、分组、交互。<br>Combo 嵌套、聚合、折叠，复杂关系布局。适合研究复杂网络的结构呈现。 △ | [仓库](https://github.com/antvis/G6 "核对依据：npm 包元数据") ✓ | [展示页](https://g6.antv.antgroup.com/en/manual/behavior/collapse-expand) ✓ | [站点](https://g6.antv.antgroup.com/) | 开源；官方页面没找到依据的说明：聚合 |
| [React Flow](https://reactflow.dev/) | React 节点和边编辑器。<br>自定义节点、子流程、连线编辑、业务组件集成。更适合研究复杂节点编辑器与工作流应用。 △ | [仓库](https://github.com/xyflow/xyflow "核对依据：npm 包元数据") ✓ | [展示页](https://reactflow.dev/examples) ✓ | [站点](https://reactflow.dev/) | 开源；官方 Pro Examples 页面把 Expand and Collapse 等高级示例列为 Pro 示例（2026-10-13 核对）；官方页面没找到依据的说明：业务组件集成 |
| [Cytoscape.js](https://js.cytoscape.org/) | 图模型、网络分析及扩展生态。<br>复合节点、图算法、复杂度管理。更适合研究复杂网络的结构呈现。 △ | [仓库](https://github.com/cytoscape/cytoscape.js "核对依据：npm 包元数据") ✓ | [展示页](https://js.cytoscape.org/) ✓ | — | 开源；官方页面没找到依据的说明：复杂度管理 |
| [Sigma.js](https://www.sigmajs.org/) | 基于 WebGL 的网络图渲染。<br>较大关系网络、节点探索，常与 Graphology 配合。 ✓ | [仓库](https://github.com/jacomyal/sigma.js "核对依据：npm 包元数据") ✓ | [展示页](https://www.sigmajs.org/examples/) ✓ | [站点](https://www.sigmajs.org/) | 开源 |
| [AntV X6](https://github.com/antvis/X6) | 图编辑引擎。<br>复杂节点编辑、连接桩、流程编辑器。 ✓ | [仓库](https://github.com/antvis/X6 "核对依据：npm 包元数据") ✓ | [展示页](https://x6.antv.antgroup.com/examples) ✓ | — | 开源 |
| [diagram-js](https://github.com/bpmn-io/diagram-js) | 图形编辑能力底座，bpmn-js 建立在其上。<br>编辑器组件；业务流程方向的 L1 代表。 ✓ | [仓库](https://github.com/bpmn-io/diagram-js "核对依据：npm 包元数据") ✓ | 无：底层库，演示见 bpmn-js | — | 开源；报告只在正文和跨层索引里提到，没有给出地址；仓库地址由整理者补充。 |
<!-- /gen -->

## 布局与复杂度管理算法

这一组经常被忽略，但对复杂认知地图可能比换一个渲染器更重要。要把结构聚合算法与视觉布局算法区分开：前者决定显示哪些对象、合并哪些关系，后者决定这些对象显示在哪里。

<!-- gen:catalog:L1/layouts-and-graph-algorithms -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [ELK.js](https://github.com/kieler/elkjs) | 自动分层布局、连线布线、复合图布局。<br>复杂模块和任务 DAG。 △ | [仓库](https://github.com/kieler/elkjs "核对依据：npm 包元数据") ✓ | [展示页](https://rtsys.informatik.uni-kiel.de/elklive/) | — | 开源；官方页面没找到依据的说明：分层（layered）布局、连线布线、复杂模块和任务 DAG 场景 |
| [Dagre](https://github.com/dagrejs/dagre) | 有向图层次布局。<br>工作流、依赖图。 | [仓库](https://github.com/dagrejs/dagre "核对依据：npm 包元数据") ✓ | [展示页](https://dagrejs.github.io/project/dagre-d3/latest/demo/interactive-demo.html) ✓ | — | 开源；展示页属于 dagre-d3。 |
| [Graphviz](https://graphviz.org/) | 多种图布局与渲染。<br>架构图、静态分析、依赖图。 △ | [仓库](https://gitlab.com/graphviz/graphviz "核对依据：项目官网 graphviz.org 页面里的 GitLab 链接") ✓ | [展示页](https://graphviz.org/gallery/) ✓ | [站点](https://graphviz.org/) | 官方页面没找到依据的说明：架构图、静态分析、依赖图 |
| [d3-force](https://github.com/d3/d3-force) | 力导向模拟。<br>自由关系网络、动态关系图。 ✓ | [仓库](https://github.com/d3/d3-force "核对依据：npm 包元数据") ✓ | [展示页](https://observablehq.com/collection/@d3/d3-force) | — | 开源 |
| [Graphology](https://graphology.github.io/) | 图数据操作与算法生态。<br>关系分析、节点指标、图结构处理。 △ | [仓库](https://github.com/graphology/graphology "核对依据：npm 包元数据") ✓ | 无：数据结构库，没有可视化界面 | [站点](https://graphology.github.io/) | 开源；官方页面没找到依据的说明：关系分析 |
| [Cytoscape Complexity Management](https://github.com/iVis-at-Bilkent/cytoscape.js-complexity-management) | 大型复合图的展开、折叠与关系管理（Cytoscape.js 扩展）。<br>层次化复杂网络；节点、边及聚合关系的管理。 △ | [仓库](https://github.com/iVis-at-Bilkent/cytoscape.js-complexity-management "核对依据：npm 包 cytoscape-complexity-management 的 homepage 字段") ✓ | [展示页](https://ivis-at-bilkent.github.io/cytoscape.js-complexity-management/demo/demo.html) ✓ | — | README 带有演示链接，但地址没有拿到；需要 Cytoscape.js 3.2.0 以上以及 fcose、cmgm.js，README 称尚未发布到 npm 和 bower；官方页面没找到依据的说明：大型、层次化、聚合关系 |
| [Cytoscape Expand Collapse](https://github.com/iVis-at-Bilkent/cytoscape.js-expand-collapse) | 复合节点的展开与折叠（Cytoscape.js 扩展）。<br>折叠复合节点及其内部的边。README 提供三个演示：基础版、可撤销版、同时折叠边和节点。 ✓ | [仓库](https://github.com/iVis-at-Bilkent/cytoscape.js-expand-collapse "核对依据：npm 包元数据") ✓ | [展示页](https://ivis-at-bilkent.github.io/cytoscape.js-expand-collapse/demo/demo-compounds-collapsed.html) ✓ | — | 开源；已停止维护；npm README 称仓库不再维护，并指向同一团队的 cytoscape.js-complexity-management（搜索结果摘要）。 |
<!-- /gen -->

## 降维与投影算法

高维数据要变成屏幕上的位置，先要有一个把维度压下来的算法。这一组只收算法实现；它们的输出怎么读、各自丢掉什么，见[高维可视化](../../01-theory/high-dimensional.md)。

<!-- gen:catalog:L1/dimensionality-reduction -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [UMAP（umap-learn）](https://github.com/lmcinnes/umap) | UMAP 降维算法的 Python 实现。<br>文档讲了主要参数（n_neighbors、min_dist、n_components、metric）和交互式绘图的做法。 ✓ | [仓库](https://github.com/lmcinnes/umap "核对依据：PyPI 包元数据声明的仓库") ✓ | 无：算法库，没有独立的展示页；文档里有绘图示例。 | [文档](https://umap-learn.readthedocs.io/en/latest/) | 开源 |
| [openTSNE](https://github.com/pavlin-policar/openTSNE) | t-SNE 的可扩展、并行实现。<br>t-SNE 的参数怎样改变图（文档有参数指南）。 ✓ | [仓库](https://github.com/pavlin-policar/openTSNE "核对依据：PyPI 包元数据声明的仓库") ✓ | 无：算法库，没有独立的展示页；文档里有使用示例。 | [文档](https://opentsne.readthedocs.io/en/stable/) | 开源 |
<!-- /gen -->

## 图形描述语言与模型驱动技术

LikeC4 和 Structurizr 不只是“画图语言”，更重要的是把模型与视图分离：一份结构模型可以定义多张不同视角的图。

<!-- gen:catalog:L1/diagram-languages -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Mermaid](https://mermaid.js.org/) | 文本生成流程、时序、状态、结构图，适合 Markdown 文档。<br>快速将结构化文本转换为可读图形。 ✓ | [仓库](https://github.com/mermaid-js/mermaid "核对依据：npm 包元数据") ✓ | [展示页](https://mermaid.live/) ✓ | [站点](https://mermaid.js.org/) | 开源 |
| [PlantUML](https://plantuml.com/) | UML、时序、架构、组件等软件工程图。<br>软件工程图的文本描述。 △ | [仓库](https://github.com/plantuml/plantuml "核对依据：plantuml.com/download 页面里的源码与发布链接") ✓ | 待收集 | [站点](https://plantuml.com/) | 官方页面没找到依据的说明：架构图（页面里只有导航条目 Archimate） |
| [D2](https://d2lang.com/) | 声明式图形描述、容器嵌套、自动布局。<br>容器嵌套的文本描述。 ✓ | [仓库](https://github.com/d2lang/d2) | [展示页](https://play.d2lang.com/) ✓ | [站点](https://d2lang.com/) | 仓库原写 terrastruct/d2；Homebrew 的 d2 公式（2026-10-13）已指向 d2lang/d2，npm 包 @terrastruct/d2 仍声明旧地址 terrastruct/d2。哪个是现在的主地址没能在项目官方页面里核实，所以仓库不标 ✓。 |
| [Structurizr DSL](https://github.com/structurizr/dsl) | 统一 C4 架构模型及多视角定义。<br>把模型与视图分离：一份结构模型可以定义多张不同视角的图。 △ | [仓库](https://github.com/structurizr/dsl) | [展示页](https://docs.structurizr.com/example) ✓ | — | 官方文档站页脚的 GitHub 链接指向 structurizr/structurizr（整个产品），没有单独写 DSL 的仓库；这里的 structurizr/dsl 是否仍是主仓库未核实；官方页面没找到依据的说明：模型与视图分离 |
| [LikeC4](https://likec4.dev/)<br>（主分类 L2/software-architecture） | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 ✓ | [仓库](https://github.com/likec4/likec4 "核对依据：npm 包元数据") ✓ | [展示页](https://likec4.dev/showcases/bigbank/) ✓ | [站点](https://likec4.dev/) | 开源 |
<!-- /gen -->

## 二维无限画布与三维空间技术

二维与三维应当归入表达载体，而不是认知层次。

<!-- gen:catalog:L1/canvas-2d-and-3d -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Excalidraw](https://github.com/excalidraw/excalidraw) | 可嵌入、可编辑的二维无限白板。<br>偏向人工绘图、自由表达、构思与注释。 △ | [仓库](https://github.com/excalidraw/excalidraw "核对依据：npm 包元数据") ✓ | [展示页](https://excalidraw.com/) ✓ | — | 开源；官方页面没找到依据的说明：“无限”画布、构思与注释 |
| [tldraw](https://github.com/tldraw/tldraw) | 无限画布 SDK：自定义对象、多人协作。<br>无限画布上的自定义对象与协作。 ✓ | [仓库](https://github.com/tldraw/tldraw "核对依据：npm 包元数据") ✓ | [展示页](https://examples.tldraw.com/) ✓ | — | 含附加条件的许可证；tldraw.dev/community/license 写明：默认条款下 SDK 许可只允许在开发中使用，生产环境需要试用许可或商业许可等（2026-10-13 核对）。 |
| [Three.js](https://github.com/mrdoob/three.js) | 通用三维场景渲染。<br>结构语义、布局和交互需自行构建。 ✓ | [仓库](https://github.com/mrdoob/three.js "核对依据：npm 包元数据") ✓ | [展示页](https://threejs.org/examples/) ✓ | — | 开源 |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | React 三维组件开发，基于 Three.js。<br>用 React 组织三维场景。 ✓ | [仓库](https://github.com/pmndrs/react-three-fiber "核对依据：npm 包元数据") ✓ | [展示页](https://r3f.docs.pmnd.rs/getting-started/examples) ✓ | — | 开源 |
| [React Force Graph](https://github.com/vasturiano/react-force-graph) | 2D、3D、VR、AR 关系图。<br>官方示例含点击展开折叠、相机聚焦、方向箭头、动态数据和不同空间模式，对复杂图的空间交互有参考价值。 ✓ | [仓库](https://github.com/vasturiano/react-force-graph "核对依据：npm 包元数据") ✓ | [展示页](https://vasturiano.github.io/react-force-graph/) ✓ | — | 开源 |
| [Cosmos.gl](https://github.com/cosmosgl/graph) | GPU 加速的力导向图。<br>使用 GPU 做布局计算与图形渲染，面向大规模网络。 ✓ | [仓库](https://github.com/cosmosgl/graph "核对依据：npm 包元数据") ✓ | [展示页](https://cosmos.gl/) | [文档](https://openjsf.org/blog/introducing-cosmos-gl) | 开源；展示页是 Storybook 示例站，页面标题是通用的 Storybook 标题，具体示例未确认。 |
<!-- /gen -->

## 支撑技术：结构的存储、提取与视图转换

一个能支持跨视角、跨粒度的复杂可视化系统，除了前端绘图和交互，还需要数据模型和数据处理能力。前端画布可能只是最后的表达层，核心能力往往在数据建模、结构提取、图查询和视图生成里。如果这些基础没有区分清楚，容易出现“换一种视角便要重新组织全部数据”的问题。

| 支撑能力 | 研究内容 | 代表技术 |
| --- | --- | --- |
| 结构化数据模型 | 如何统一表示实体、属性、类型与关系 | 属性图、RDF、JSON Graph |
| 图查询与分析 | 如何获取邻居、路径、子图、聚类和指标 | NetworkX、Graphology、Neo4j |
| 结构提取 | 如何将代码、文档、事件转为结构数据 | Tree-sitter、Docling、LLM 提取 |
| 跨层映射 | 如何保留父子层级、成员归属和跨模块关系 | 层级图模型、复合图、架构模型 |
| 视图生成 | 如何从统一模型生成不同的结构投影 | C4 / LikeC4 范式、图查询与视图配置 |
| 时序与事件 | 如何关联结构及其运行历史 | Trace、事件日志、时间属性图 |
| 证据追溯 | 如何让每个关系返回原始来源 | Provenance、引用、代码位置、运行记录 |

其中 Graphology、Tree-sitter、Docling 在目录里有条目；其余是技术名称，尚未建条目。
