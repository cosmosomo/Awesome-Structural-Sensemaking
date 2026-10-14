# 项目索引

> 本文件由 `scripts/build.py` 根据 `catalog/` 生成，请改 YAML，不要直接改这里。
> 条目信息来自 2026-10 调研报告。展示页来自报告原文或事后的搜索结果，除标 ✓ 的外都没有实际访问过。

共 100 个条目；有开源项目地址 96 个，有展示页 72 个（其中 64 个已访问核对，标 ✓）；另有 19 个本身没有展示页。
有 89 个开源项目地址已核对（标 ✓，鼠标悬停可看依据）：npm / PyPI 的包元数据、项目官网或官方文档里的源码链接，或 Go 模块代理指向的仓库与这里一致。其余没有核对，GitHub 页面本身没有访问。
“定位与值得研究”一列末尾的标记：✓ 表示这段说明的主要点在官方页面里都找到了依据（57 个）；△ 表示有些点没找到依据，写在备注里（38 个）；没有标记的没核对过。找不到依据不等于说法有误，官方页面由 JS 渲染读不到的、或者只是整理者的评价性判断，也会落在这一类。

“待补”表示开源项目地址缺失，“待收集”表示展示页缺失或还没找到；“无：…”表示这个条目本身不存在展示页（如规范、采集库、命令行工具）；商业产品、规范和刊物没有仓库，用“—”表示。

## L1 底层可视化技术

### 通用图形与数据可视化

<sub>L1/chart-and-visualization-engines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [D3.js](https://github.com/d3/d3) | 底层数据驱动可视化工具集。<br>自定义视觉编码、层级、网络、布局与交互。 ✓ | [仓库](https://github.com/d3/d3 "核对依据：npm 包元数据") ✓ | [展示页](https://observablehq.com/collection/@d3/gallery) | — | 开源 |
| [Vega-Lite](https://github.com/vega/vega-lite) | 声明式可视化语法。<br>用结构化描述定义图表，而不是逐元素绘制。 ✓ | [仓库](https://github.com/vega/vega-lite "核对依据：npm 包元数据") ✓ | [展示页](https://vega.github.io/vega-lite/examples/) ✓ | — | 开源 |
| [Apache ECharts](https://echarts.apache.org/) | 综合图表引擎。<br>图表类型、交互组件、大屏和业务看板。 △ | [仓库](https://github.com/apache/echarts "核对依据：npm 包元数据") ✓ | [展示页](https://echarts.apache.org/examples) ✓ | [站点](https://echarts.apache.org/) | 开源；官方页面没找到依据的说明：业务看板 |
| [Plotly.js](https://github.com/plotly/plotly.js) | 数据探索与交互图表。<br>多维统计图、科学可视化、交互分析。 △ | [仓库](https://github.com/plotly/plotly.js "核对依据：npm 包元数据") ✓ | [展示页](https://plotly.com/javascript/) ✓ | — | 开源；官方页面没找到依据的说明：数据探索、交互、多维 |
| [deck.gl](https://github.com/visgl/deck.gl) | GPU 加速的大数据可视化框架。<br>大规模数据、地图图层、多视角渲染。 ✓ | [仓库](https://github.com/visgl/deck.gl "核对依据：npm 包元数据") ✓ | [展示页](https://deck.gl/gallery/) ✓ | — | 开源 |
| [regl-scatterplot](https://github.com/flekschas/regl-scatterplot) | 基于 WebGL 的交互式二维散点图，面向大量数据点。<br>几十万以上的点如何做到可缩放、可选择、可编码；投影结果的前端落地。 ✓ | [仓库](https://github.com/flekschas/regl-scatterplot "核对依据：npm 包元数据声明的仓库") ✓ | [展示页](https://flekschas.github.io/regl-scatterplot/) ✓ | — | 开源；展示页由 WebGL 渲染，页面文字只有标题；说明依据是 npm 包的 README。 |

### 关系图与节点交互引擎

<sub>L1/graph-and-node-engines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AntV G6](https://g6.antv.antgroup.com/) | 通用关系图引擎：图布局、分组、交互。<br>Combo 嵌套、聚合、折叠，复杂关系布局。适合研究复杂网络的结构呈现。 △ | [仓库](https://github.com/antvis/G6 "核对依据：npm 包元数据") ✓ | [展示页](https://g6.antv.antgroup.com/en/manual/behavior/collapse-expand) ✓ | [站点](https://g6.antv.antgroup.com/) | 开源；官方页面没找到依据的说明：聚合 |
| [React Flow](https://reactflow.dev/) | React 节点和边编辑器。<br>自定义节点、子流程、连线编辑、业务组件集成。更适合研究复杂节点编辑器与工作流应用。 △ | [仓库](https://github.com/xyflow/xyflow "核对依据：npm 包元数据") ✓ | [展示页](https://reactflow.dev/examples) ✓ | [站点](https://reactflow.dev/) | 开源；官方 Pro Examples 页面把 Expand and Collapse 等高级示例列为 Pro 示例（2026-10-13 核对）；官方页面没找到依据的说明：业务组件集成 |
| [Cytoscape.js](https://js.cytoscape.org/) | 图模型、网络分析及扩展生态。<br>复合节点、图算法、复杂度管理。更适合研究复杂网络的结构呈现。 △ | [仓库](https://github.com/cytoscape/cytoscape.js "核对依据：npm 包元数据") ✓ | [展示页](https://js.cytoscape.org/) ✓ | — | 开源；官方页面没找到依据的说明：复杂度管理 |
| [Sigma.js](https://www.sigmajs.org/) | 基于 WebGL 的网络图渲染。<br>较大关系网络、节点探索，常与 Graphology 配合。 ✓ | [仓库](https://github.com/jacomyal/sigma.js "核对依据：npm 包元数据") ✓ | [展示页](https://www.sigmajs.org/examples/) ✓ | [站点](https://www.sigmajs.org/) | 开源 |
| [AntV X6](https://github.com/antvis/X6) | 图编辑引擎。<br>复杂节点编辑、连接桩、流程编辑器。 ✓ | [仓库](https://github.com/antvis/X6 "核对依据：npm 包元数据") ✓ | [展示页](https://x6.antv.antgroup.com/examples) ✓ | — | 开源 |
| [diagram-js](https://github.com/bpmn-io/diagram-js) | 图形编辑能力底座，bpmn-js 建立在其上。<br>编辑器组件；业务流程方向的 L1 代表。 ✓ | [仓库](https://github.com/bpmn-io/diagram-js "核对依据：npm 包元数据") ✓ | 无：底层库，演示见 bpmn-js | — | 开源；报告只在正文和跨层索引里提到，没有给出地址；仓库地址由整理者补充。 |

### 布局与复杂度管理算法

<sub>L1/layouts-and-graph-algorithms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [ELK.js](https://github.com/kieler/elkjs) | 自动分层布局、连线布线、复合图布局。<br>复杂模块和任务 DAG。 △ | [仓库](https://github.com/kieler/elkjs "核对依据：npm 包元数据") ✓ | [展示页](https://rtsys.informatik.uni-kiel.de/elklive/) | — | 开源；官方页面没找到依据的说明：分层（layered）布局、连线布线、复杂模块和任务 DAG 场景 |
| [Dagre](https://github.com/dagrejs/dagre) | 有向图层次布局。<br>工作流、依赖图。 | [仓库](https://github.com/dagrejs/dagre "核对依据：npm 包元数据") ✓ | [展示页](https://dagrejs.github.io/project/dagre-d3/latest/demo/interactive-demo.html) ✓ | — | 开源；展示页属于 dagre-d3。 |
| [Graphviz](https://graphviz.org/) | 多种图布局与渲染。<br>架构图、静态分析、依赖图。 △ | [仓库](https://gitlab.com/graphviz/graphviz "核对依据：项目官网 graphviz.org 页面里的 GitLab 链接") ✓ | [展示页](https://graphviz.org/gallery/) ✓ | [站点](https://graphviz.org/) | 官方页面没找到依据的说明：架构图、静态分析、依赖图 |
| [d3-force](https://github.com/d3/d3-force) | 力导向模拟。<br>自由关系网络、动态关系图。 ✓ | [仓库](https://github.com/d3/d3-force "核对依据：npm 包元数据") ✓ | [展示页](https://observablehq.com/collection/@d3/d3-force) | — | 开源 |
| [Graphology](https://graphology.github.io/) | 图数据操作与算法生态。<br>关系分析、节点指标、图结构处理。 △ | [仓库](https://github.com/graphology/graphology "核对依据：npm 包元数据") ✓ | 无：数据结构库，没有可视化界面 | [站点](https://graphology.github.io/) | 开源；官方页面没找到依据的说明：关系分析 |
| [Cytoscape Complexity Management](https://github.com/iVis-at-Bilkent/cytoscape.js-complexity-management) | 大型复合图的展开、折叠与关系管理（Cytoscape.js 扩展）。<br>层次化复杂网络；节点、边及聚合关系的管理。 △ | [仓库](https://github.com/iVis-at-Bilkent/cytoscape.js-complexity-management "核对依据：npm 包 cytoscape-complexity-management 的 homepage 字段") ✓ | [展示页](https://ivis-at-bilkent.github.io/cytoscape.js-complexity-management/demo/demo.html) ✓ | — | README 带有演示链接，但地址没有拿到；需要 Cytoscape.js 3.2.0 以上以及 fcose、cmgm.js，README 称尚未发布到 npm 和 bower；官方页面没找到依据的说明：大型、层次化、聚合关系 |
| [Cytoscape Expand Collapse](https://github.com/iVis-at-Bilkent/cytoscape.js-expand-collapse) | 复合节点的展开与折叠（Cytoscape.js 扩展）。<br>折叠复合节点及其内部的边。README 提供三个演示：基础版、可撤销版、同时折叠边和节点。 ✓ | [仓库](https://github.com/iVis-at-Bilkent/cytoscape.js-expand-collapse "核对依据：npm 包元数据") ✓ | [展示页](https://ivis-at-bilkent.github.io/cytoscape.js-expand-collapse/demo/demo-compounds-collapsed.html) ✓ | — | 开源；已停止维护；npm README 称仓库不再维护，并指向同一团队的 cytoscape.js-complexity-management（搜索结果摘要）。 |

### 降维与投影算法

<sub>L1/dimensionality-reduction</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [UMAP（umap-learn）](https://github.com/lmcinnes/umap) | UMAP 降维算法的 Python 实现。<br>文档讲了主要参数（n_neighbors、min_dist、n_components、metric）和交互式绘图的做法。 ✓ | [仓库](https://github.com/lmcinnes/umap "核对依据：PyPI 包元数据声明的仓库") ✓ | 无：算法库，没有独立的展示页；文档里有绘图示例。 | [文档](https://umap-learn.readthedocs.io/en/latest/) | 开源 |
| [openTSNE](https://github.com/pavlin-policar/openTSNE) | t-SNE 的可扩展、并行实现。<br>t-SNE 的参数怎样改变图（文档有参数指南）。 ✓ | [仓库](https://github.com/pavlin-policar/openTSNE "核对依据：PyPI 包元数据声明的仓库") ✓ | 无：算法库，没有独立的展示页；文档里有使用示例。 | [文档](https://opentsne.readthedocs.io/en/stable/) | 开源 |

### 图形描述语言与模型驱动技术

<sub>L1/diagram-languages</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Mermaid](https://mermaid.js.org/) | 文本生成流程、时序、状态、结构图，适合 Markdown 文档。<br>快速将结构化文本转换为可读图形。 ✓ | [仓库](https://github.com/mermaid-js/mermaid "核对依据：npm 包元数据") ✓ | [展示页](https://mermaid.live/) ✓ | [站点](https://mermaid.js.org/) | 开源 |
| [PlantUML](https://plantuml.com/) | UML、时序、架构、组件等软件工程图。<br>软件工程图的文本描述。 △ | [仓库](https://github.com/plantuml/plantuml "核对依据：plantuml.com/download 页面里的源码与发布链接") ✓ | 待收集 | [站点](https://plantuml.com/) | 官方页面没找到依据的说明：架构图（页面里只有导航条目 Archimate） |
| [D2](https://d2lang.com/) | 声明式图形描述、容器嵌套、自动布局。<br>容器嵌套的文本描述。 ✓ | [仓库](https://github.com/d2lang/d2) | [展示页](https://play.d2lang.com/) ✓ | [站点](https://d2lang.com/) | 仓库原写 terrastruct/d2；Homebrew 的 d2 公式（2026-10-13）已指向 d2lang/d2，npm 包 @terrastruct/d2 仍声明旧地址 terrastruct/d2。哪个是现在的主地址没能在项目官方页面里核实，所以仓库不标 ✓。 |
| [Structurizr DSL](https://github.com/structurizr/dsl) | 统一 C4 架构模型及多视角定义。<br>把模型与视图分离：一份结构模型可以定义多张不同视角的图。 △ | [仓库](https://github.com/structurizr/dsl) | [展示页](https://docs.structurizr.com/example) ✓ | — | 官方文档站页脚的 GitHub 链接指向 structurizr/structurizr（整个产品），没有单独写 DSL 的仓库；这里的 structurizr/dsl 是否仍是主仓库未核实；官方页面没找到依据的说明：模型与视图分离 |
| [LikeC4](https://likec4.dev/)<br>（主分类 L2/software-architecture） | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 ✓ | [仓库](https://github.com/likec4/likec4 "核对依据：npm 包元数据") ✓ | [展示页](https://likec4.dev/showcases/bigbank/) ✓ | [站点](https://likec4.dev/) | 开源 |

### 二维无限画布与三维空间技术

<sub>L1/canvas-2d-and-3d</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Excalidraw](https://github.com/excalidraw/excalidraw) | 可嵌入、可编辑的二维无限白板。<br>偏向人工绘图、自由表达、构思与注释。 △ | [仓库](https://github.com/excalidraw/excalidraw "核对依据：npm 包元数据") ✓ | [展示页](https://excalidraw.com/) ✓ | — | 开源；官方页面没找到依据的说明：“无限”画布、构思与注释 |
| [tldraw](https://github.com/tldraw/tldraw) | 无限画布 SDK：自定义对象、多人协作。<br>无限画布上的自定义对象与协作。 ✓ | [仓库](https://github.com/tldraw/tldraw "核对依据：npm 包元数据") ✓ | [展示页](https://examples.tldraw.com/) ✓ | — | 含附加条件的许可证；tldraw.dev/community/license 写明：默认条款下 SDK 许可只允许在开发中使用，生产环境需要试用许可或商业许可等（2026-10-13 核对）。 |
| [Three.js](https://github.com/mrdoob/three.js) | 通用三维场景渲染。<br>结构语义、布局和交互需自行构建。 ✓ | [仓库](https://github.com/mrdoob/three.js "核对依据：npm 包元数据") ✓ | [展示页](https://threejs.org/examples/) ✓ | — | 开源 |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | React 三维组件开发，基于 Three.js。<br>用 React 组织三维场景。 ✓ | [仓库](https://github.com/pmndrs/react-three-fiber "核对依据：npm 包元数据") ✓ | [展示页](https://r3f.docs.pmnd.rs/getting-started/examples) ✓ | — | 开源 |
| [React Force Graph](https://github.com/vasturiano/react-force-graph) | 2D、3D、VR、AR 关系图。<br>官方示例含点击展开折叠、相机聚焦、方向箭头、动态数据和不同空间模式，对复杂图的空间交互有参考价值。 ✓ | [仓库](https://github.com/vasturiano/react-force-graph "核对依据：npm 包元数据") ✓ | [展示页](https://vasturiano.github.io/react-force-graph/) ✓ | — | 开源 |
| [Cosmos.gl](https://github.com/cosmosgl/graph) | GPU 加速的力导向图。<br>使用 GPU 做布局计算与图形渲染，面向大规模网络。 ✓ | [仓库](https://github.com/cosmosgl/graph "核对依据：npm 包元数据") ✓ | [展示页](https://cosmos.gl/) | [文档](https://openjsf.org/blog/introducing-cosmos-gl) | 开源；展示页是 Storybook 示例站，页面标题是通用的 Storybook 标题，具体示例未确认。 |

## L2 特定结构与数据的专项可视化项目

### 代码依赖与模块解耦

<sub>L2/code-dependencies</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [dependency-cruiser](https://sverweij.github.io/dependency-cruiser/) | JavaScript/TypeScript 模块依赖分析。<br>依赖图、架构边界规则、违规依赖诊断。 △ | [仓库](https://github.com/sverweij/dependency-cruiser "核对依据：npm 包元数据") ✓ | [展示页](https://sverweij.github.io/dependency-cruiser-repro-repo/458/) ✓ | [站点](https://sverweij.github.io/dependency-cruiser/) | 开源；展示页是作者的 3D 图报告插件演示（issue 458），用它自己的源码和 React 仓库生成；官方页面没找到依据的说明：架构边界规则 |
| [Madge](https://github.com/pahen/madge) | JavaScript 模块引用分析。<br>自动生成依赖关系图、发现循环依赖。 ✓ | [仓库](https://github.com/pahen/madge "核对依据：npm 包元数据") ✓ | 无：命令行工具，输出静态图 | — | 开源；npm 上 madge 最近一次发布是 2024-08-05（v8.0.0），查询于 2026-10-13。 |
| [pydeps](https://github.com/thebjorn/pydeps) | Python 模块导入分析。<br>导入网络、模块聚类、依赖结构。 △ | [仓库](https://github.com/thebjorn/pydeps "核对依据：PyPI 包元数据") ✓ | 无：命令行工具，输出静态图 | — | 开源；官方页面没找到依据的说明：模块聚类 |

### 软件架构与代码理解

<sub>L2/software-architecture</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CodeBoarding](https://codeboarding.org/) | 源码结构及架构语义分析。<br>自动归纳组件，形成分层架构解释与可视化。 △ | [仓库](https://github.com/CodeBoarding/CodeBoarding "核对依据：PyPI 包元数据") ✓ | 待收集 | [站点](https://codeboarding.org/) | 开源；官方页面没找到依据的说明：架构语义分析、分层架构解释 |
| [Understand Anything](https://understand-anything.com/) | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 △ | [仓库](https://github.com/Egonex-AI/Understand-Anything "核对依据：项目官网 understand-anything.com 的 GitHub 链接") ✓ | [展示页](https://understand-anything.com/) ✓ | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析；官方页面没找到依据的说明：变更影响分析、先解析显式链接再用模型发现隐式关系、带类型的知识网络 |
| [LikeC4](https://likec4.dev/) | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 ✓ | [仓库](https://github.com/likec4/likec4 "核对依据：npm 包元数据") ✓ | [展示页](https://likec4.dev/showcases/bigbank/) ✓ | [站点](https://likec4.dev/) | 开源 |

### 流程、状态机与任务依赖

<sub>L2/workflows-and-state-machines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [bpmn-js](https://github.com/bpmn-io/bpmn-js) | BPMN 流程模型的查看、编辑与扩展。<br>建立在 diagram-js 之上，可通过扩展机制增加覆盖层、标记和自定义交互。 △ | [仓库](https://github.com/bpmn-io/bpmn-js "核对依据：npm 包元数据") ✓ | [展示页](https://demo.bpmn.io/) ✓ | — | 含附加条件的许可证；bpmn.io License（bpmn.io/license，2026-10-13 访问）：类似 MIT，但要求渲染出的图里指向 bpmn.io 的水印不得移除或改动，在网站或应用中必须完整可见、不被其他元素遮挡；官方页面没找到依据的说明：标记（markers）、自定义交互 |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble)<br>（主分类 L2/ai-and-multi-agent） | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 ✓ | [仓库](https://github.com/AgentEnsemble/agentensemble "核对依据：官方文档站 docs.agentensemble.net 的 GitHub 链接") ✓ | 无：Live Dashboard 在本地运行（localhost:7329），没有托管的公开演示 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |

### Agent 与多智能体协作

<sub>L2/ai-and-multi-agent</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble) | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 ✓ | [仓库](https://github.com/AgentEnsemble/agentensemble "核对依据：官方文档站 docs.agentensemble.net 的 GitHub 链接") ✓ | 无：Live Dashboard 在本地运行（localhost:7329），没有托管的公开演示 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AgentPrism](https://github.com/evilmartians/agent-prism) | 可嵌入应用的 React Agent Trace UI 组件。<br>层次化调用树、执行时间、工具与模型调用；独立可复用的 Trace UI 设计。 △ | [仓库](https://github.com/evilmartians/agent-prism "核对依据：npm 包元数据") ✓ | [展示页](https://agent-prism.evilmartians.io/) ✓ | [文档](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces) | Alpha；报告称项目公开标注为 Alpha。evilmartians.com 的博客、项目页和演示站正文里没有找到 Alpha 标注；搜索结果摘要称 GitHub README 标为 alpha，未核实；官方页面没找到依据的说明：工具调用与模型调用的展示 |

### Trace、调用链与执行过程

<sub>L2/traces-and-timelines</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [OpenTelemetry GenAI 语义约定](https://github.com/open-telemetry/semantic-conventions-genai) | 规定如何描述 AI / Agent / 工具调用等遥测事件。<br>数据到可视化链条的起点：Span、事件、属性、父子关系。 | [仓库](https://github.com/open-telemetry/semantic-conventions-genai "核对依据：opentelemetry.io 的 GenAI 约定页写明已迁到该仓库") ✓ | 无：规范文档，本身没有可视化 | [文档](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | 官方页面已写明 GenAI 语义约定迁到 open-telemetry/semantic-conventions-genai 仓库，opentelemetry.io 上的旧页面只剩迁移说明（2026-10-13 访问）。该约定仍在演进，建库时记录具体版本和字段定义，不要当成永远稳定的统一标准。 |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | 为 LLM 应用采集追踪数据。<br>数据采集端。 ✓ | [仓库](https://github.com/traceloop/openllmetry "核对依据：PyPI 包元数据") ✓ | 无：数据采集库，没有界面 | — | 开源 |
| [Jaeger](https://github.com/jaegertracing/jaeger) | 分布式 Trace 的采集、检索和可视化。<br>Trace 瀑布图等传统调用链视图。 △ | [仓库](https://github.com/jaegertracing/jaeger "核对依据：Docker Hub 上 jaegertracing/jaeger 页面里的 GitHub 地址") ✓ | [展示页](https://www.jaegertracing.io/demo/) ✓ | — | 官网下载页写明 Jaeger v1 已于 2025-12-31 终止支持，v2 是基于 OpenTelemetry Collector 的新主版本（2026-10-13 核对）；官方页面没找到依据的说明：采集、瀑布图 |
| [Grafana Tempo](https://github.com/grafana/tempo) | Trace 后端，与服务图、指标视图整合。<br>Trace 与服务图、指标的联动。 ✓ | [仓库](https://github.com/grafana/tempo "核对依据：官方文档页的“Create a GitHub issue”链接指向该仓库") ✓ | 无：后端服务，界面由 Grafana 提供 | — | — |
| [AeroGraph](https://github.com/sgcpu/aerograph) | 面向自主 AI 工作流的调试与观测层：本地优先、只追加、可安全回放的存储。<br>ReactFlow 的 Trace 图，支持逐步回放和失败高亮；可从任意 span 分叉出另一条时间线，并用 Myers diff 比较两次运行在哪里分岔；追踪循环和幻觉式的 Agent 交接。 | [仓库](https://github.com/sgcpu/aerograph "核对依据：Go 模块代理 proxy.golang.org 返回的模块来源（Origin.URL）") ✓ | 待收集 | — | 不在调研报告里，来自前期收集，信息取自搜索到的 GitHub README。是早期的小众项目，成熟度和循环检测的实现方式未核实。 |
| [AgentEnsemble Viz](https://github.com/AgentEnsemble/agentensemble)<br>（主分类 L2/ai-and-multi-agent） | 任务依赖 DAG 与实际执行 Trace 的双视图。<br>Flow View 看任务依赖、并发层级、关键路径；Timeline View 看真实起止时间、LLM 和工具调用。分别导出计划依赖 DAG 与执行 Trace。值得研究同一任务在两张视图中的身份如何保持一致，以及点击任务如何进入工具调用或会话详情。 ✓ | [仓库](https://github.com/AgentEnsemble/agentensemble "核对依据：官方文档站 docs.agentensemble.net 的 GitHub 链接") ✓ | 无：Live Dashboard 在本地运行（localhost:7329），没有托管的公开演示 | [文档](https://docs.agentensemble.net/guides/visualization/) | — |
| [AgentPrism](https://github.com/evilmartians/agent-prism)<br>（主分类 L2/ai-and-multi-agent） | 可嵌入应用的 React Agent Trace UI 组件。<br>层次化调用树、执行时间、工具与模型调用；独立可复用的 Trace UI 设计。 △ | [仓库](https://github.com/evilmartians/agent-prism "核对依据：npm 包元数据") ✓ | [展示页](https://agent-prism.evilmartians.io/) ✓ | [文档](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces) | Alpha；报告称项目公开标注为 Alpha。evilmartians.com 的博客、项目页和演示站正文里没有找到 Alpha 标注；搜索结果摘要称 GitHub README 标为 alpha，未核实；官方页面没找到依据的说明：工具调用与模型调用的展示 |

### 数据血缘

<sub>L2/data-lineage</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Marquez](https://marquezproject.ai/) | 数据集、数据任务与血缘关系。<br>上下游关系、运行历史。 ✓ | [仓库](https://github.com/MarquezProject/marquez "核对依据：项目官网 marquezproject.ai 的 GitHub 链接") ✓ | 待收集 | [站点](https://marquezproject.ai/) | — |
| [DataHub](https://github.com/datahub-project/datahub)<br>（主分类 L3/data-and-infrastructure） | 数据发现、治理与影响分析。<br>数据集、字段、流水线的血缘；从资产详情进入上下游影响网络，支持字段级钻取和影响分析。 △ | [仓库](https://github.com/datahub-project/datahub "核对依据：PyPI 包元数据") ✓ | [展示页](https://datahub.com/demos/data-lineage-with-datahub/) ✓ | [文档](https://docs.datahub.com/) | 开源；该展示页是录制的血缘功能演示，不是开放试用；官方页面没找到依据的说明：从资产详情进入上下游影响网络 |
| [OpenMetadata](https://github.com/open-metadata/OpenMetadata)<br>（主分类 L3/data-and-infrastructure） | 数据资产管理与治理。<br>资产关系、字段级血缘；从数据目录导航到血缘关系。 ✓ | [仓库](https://github.com/open-metadata/OpenMetadata "核对依据：PyPI 包元数据") ✓ | [展示页](https://sandbox.open-metadata.org/) ✓ | [文档](https://docs.open-metadata.org/latest/quick-start/sandbox) | 沙盒需要用 Google 账号登录。PyPI 上 openmetadata-ingestion 的许可证标为 Collate Community License Agreement（2026-10-13 核对）；整个项目的许可证未核实。 |

### 系统服务拓扑与基础设施

<sub>L2/infrastructure-topology</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Apache SkyWalking](https://skywalking.apache.org/)<br>（主分类 L3/data-and-infrastructure） | 服务性能监控与故障诊断。<br>服务、实例、接口、部署等层级；从宏观服务拓扑进入监控、日志与 Trace，多视图联动。其生态中出现了基础设施三维可视化的探索。 △ | [仓库](https://github.com/apache/skywalking "核对依据：官网 skywalking.apache.org 的 GitHub Issue Tracker 链接") ✓ | [展示页](https://demo.skywalking.apache.org/) ✓ | [站点](https://skywalking.apache.org/) · [文档](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/) | 官网首页链接到在线 Demo（Horizon UI，示例数据）和一个独立的 3D 基础设施地图交互演示（2026-10-13 访问）；官方页面没找到依据的说明：“部署”层级、多视图联动 |
| [Kiali](https://github.com/kiali/kiali)<br>（主分类 L3/data-and-infrastructure） | 服务网格运行观察。<br>流量图、服务关系、异常定位。 ✓ | [仓库](https://github.com/kiali/kiali "核对依据：官方文档页的“Create project issue”链接指向该仓库") ✓ | 待收集 | [文档](https://kiali.io/docs/features/topology/) | — |

### 知识、文档与认知地图

<sub>L2/knowledge-and-cognition</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [NeoDash](https://github.com/neo4j-labs/neodash) | 使用 Neo4j 图数据库查询构建交互看板。<br>图数据查询驱动的看板。 ✓ | [仓库](https://github.com/neo4j-labs/neodash "核对依据：Neo4j Labs 的 NeoDash 页面里的源码链接") ✓ | [展示页](https://neodash-gallery.graphapp.io/) ✓ | — | 维护状态待核查；Neo4j Labs 页面写明该文档对应 Labs 里“不受官方支持”的 NeoDash 版本，受支持的版本见 NeoDash commercial（2026-10-13 访问）；仓库原写 neo4j-contrib/neodash，页面里的源码链接是 neo4j-labs/neodash，已改。独立仓库的维护状态需在 GitHub 上核实；示例看板站（demo）用无头浏览器打开后页面写着 “The NeoDash sample gallery has been deprecated”，已弃用（2026-10-13）。 |
| [Argdown](https://argdown.org/) | 论证地图的文本标记语言及工具链。<br>用文本写出论证的前提与结论，渲染成论证地图；命令行工具可导出 SVG、DOT、HTML、JSON，另有 VS Code 扩展（据搜索结果摘要）。属于“语义与知识”家族里的论证地图。 ✓ | [仓库](https://github.com/argdown/argdown "核对依据：npm 包元数据") ✓ | [展示页](https://argdown.org/guide/a-first-example.html) ✓ | [站点](https://argdown.org/) | 不在调研报告里，是核对图形范式展示页时发现的。 |
| [Excalidraw](https://github.com/excalidraw/excalidraw)<br>（主分类 L1/canvas-2d-and-3d） | 可嵌入、可编辑的二维无限白板。<br>偏向人工绘图、自由表达、构思与注释。 △ | [仓库](https://github.com/excalidraw/excalidraw "核对依据：npm 包元数据") ✓ | [展示页](https://excalidraw.com/) ✓ | — | 开源；官方页面没找到依据的说明：“无限”画布、构思与注释 |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 △ | [仓库](https://github.com/Egonex-AI/Understand-Anything "核对依据：项目官网 understand-anything.com 的 GitHub 链接") ✓ | [展示页](https://understand-anything.com/) ✓ | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析；官方页面没找到依据的说明：变更影响分析、先解析显式链接再用模型发现隐式关系、带类型的知识网络 |
| [AFFiNE](https://affine.pro/)<br>（主分类 L3/knowledge-workspaces） | 文档、知识库与无限白板。<br>将线性文本与空间组织结合。 ✓ | [仓库](https://github.com/toeverything/AFFiNE "核对依据：官网 affine.pro 的 GitHub 与 License 链接") ✓ | [展示页](https://affine.pro/templates) ✓ | [站点](https://affine.pro/) | 展示页是模板库页面，不是在线试用；没有找到免登录的在线版本。 |
| [Logseq](https://github.com/logseq/logseq)<br>（主分类 L3/knowledge-workspaces） | 双向链接、页面及知识块。<br>大纲、链接和知识图导航。 △ | [仓库](https://github.com/logseq/logseq "核对依据：Homebrew cask 记录的下载来源（github.com/logseq/logseq/releases）") ✓ | [展示页](https://demo.logseq.com/) ✓ | — | 官方页面没找到依据的说明：大纲、知识图导航（官网由 JS 渲染，读不到） |
| [InfraNodus](https://infranodus.com/)<br>（主分类 L3/knowledge-workspaces） | 文本网络与结构探索。<br>文本与概念的网络、主题群落、结构空白分析。 ✓ | [仓库](https://github.com/noduslabs/infranodus) | [展示页](https://infranodus.com/graphs) ✓ | [站点](https://infranodus.com/) | 商业产品；官网说明开源的是一组支撑 InfraNodus 的工具（AGPL 许可），页脚列出 GitHub 上的 Workflows、Datasets、Tools API 和 GraphRAG MCP Server（infranodus.com，2026-10-13 访问）；报告所说“旧仓库不代表当前产品全部功能”未核实。 |

### 技术生态与商业产品地图

<sub>L2/technology-landscapes</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CNCF Landscape2](https://github.com/cncf/landscape2) | 基于结构化数据生成可筛选、可搜索的生态分类景观。<br>生态地图的数据组织和交互导航。 | [仓库](https://github.com/cncf/landscape2) | [展示页](https://landscape.cncf.io/) ✓ | — | — |
| [Zalando Tech Radar](https://github.com/zalando/tech-radar) | 使用技术雷达表达技术采用阶段与类别。<br>技术决策状态的雷达表达。 △ | [仓库](https://github.com/zalando/tech-radar "核对依据：官方页面 opensource.zalando.com/tech-radar 的源码链接") ✓ | [展示页](https://opensource.zalando.com/tech-radar/) ✓ | — | 官方页面没找到依据的说明：类别（象限） |
| [Build Your Own Radar](https://github.com/thoughtworks/build-your-own-radar) | 从结构化技术条目生成交互技术雷达。<br>技术雷达生成器。 ✓ | [仓库](https://github.com/thoughtworks/build-your-own-radar "核对依据：radar.thoughtworks.com 页面的 open source 链接") ✓ | [展示页](https://radar.thoughtworks.com/) ✓ | — | 官方托管版要求使用 Technology Radar 固定的象限和环名称，自定义名称需自行部署；据搜索结果为 AGPL 许可。 |

### 高维数据探索（投影、平行坐标、巡游、拓扑摘要）

<sub>L2/high-dimensional-exploration</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Embedding Projector](https://projector.tensorflow.org/) | 将高维向量降维到二维、三维，探索相似性与聚类。<br>高维结构投影后哪些信息被保留、哪些被扭曲。 △ | [仓库](https://github.com/tensorflow/embedding-projector) | [展示页](https://projector.tensorflow.org/) | — | 三维位置来自降维计算，不应理解为概念在原始高维语义空间中的真实坐标。 projector.tensorflow.org 和 TensorBoard Projector 插件文档都没有给出 embedding-projector 仓库的地址，这个地址未核实；官方页面没找到依据的说明：降维到二维三维、聚类、保留与扭曲了哪些信息 |
| [HiPlot](https://github.com/facebookresearch/hiplot) | Meta（原 Facebook AI Research）的交互式高维数据探索工具，以平行坐标图为核心。<br>每个维度一根轴、每条记录一条线：刷选、重排与删除轴、按另一根轴着色，用来看超参数与指标的关系。 ✓ | [仓库](https://github.com/facebookresearch/hiplot "核对依据：PyPI 包元数据声明的仓库") ✓ | [展示页](https://facebookresearch.github.io/hiplot/) ✓ | — | PyPI 最近一次发布是 2022-10-27（0.1.33），包元数据没有写许可证；“删除轴、按另一根轴着色”在 Meta AI 博客里有原文，文档页没有。 |
| [Facets](https://pair-code.github.io/facets/) | Google PAIR 的机器学习数据集可视化：Overview 逐特征看分布，Dive 按特征值摆放每个数据点。<br>特征成百上千时，先逐特征看总体分布与异常，再按特征分面、着色地看单条记录。 ✓ | [仓库](https://github.com/pair-code/facets "核对依据：PyPI 包元数据声明的仓库；项目站点的 Code 链接") ✓ | [展示页](https://pair-code.github.io/facets/) ✓ | — | 开源；PyPI 最近一次发布是 2023-05-24（facets-overview 1.1.1）；仓库当前是否仍在维护没有核实（GitHub 页面没有访问）。“特征成百上千”见 Google 开源博客 2017 年的发布文章。 |
| [KeplerMapper](https://github.com/scikit-tda/kepler-mapper) | 拓扑数据分析里 Mapper 算法的 Python 实现，把高维数据变成一张由聚类节点组成的小图。<br>投影、覆盖、聚类三步；节点和边的大小、颜色由用户指定的函数决定。 ✓ | [仓库](https://github.com/scikit-tda/kepler-mapper "核对依据：官方文档站首页的源码仓库链接") ✓ | [展示页](https://kepler-mapper.scikit-tda.org/en/latest/notebooks/Cancer-demo.html) ✓ | [文档](https://kepler-mapper.scikit-tda.org/en/latest/) | 开源；展示页是文档里的 notebook 示例，输出是预先生成的，不是在线交互。 |
| [dtour](https://dtour.dev) | 在浏览器里沿一串二维投影“巡游”高维数据的工具，支持引导式巡游、手动拖动投影和自动漫游。<br>点的身份怎样在投影之间保持；只有关键帧可解释，中间的插值只是帮助跟踪。 △ | [仓库](https://github.com/flekschas/dtour "核对依据：作者博客 lekschas.de 里的 dtour 仓库链接；PyPI 包 dtour 的说明里也链到 flekschas/dtour") ✓ | [展示页](https://dtour.dev) ✓ | — | 2026 年 5 月的论文（arXiv:2605.04306），论文作者的博客里给了仓库和网站地址；PyPI 上有同名包 dtour（MIT，0.5.1，2026-10-12 发布），元数据的仓库字段是空的，但包说明里的发布链接指向 flekschas/dtour，与这里的仓库一致；官方页面没找到依据的说明：官网 dtour.dev 正文由 JS 渲染，页面文字只有标题；说明依据是论文 HTML 版和作者博客 |
| [DataMapPlot](https://github.com/TutteInstitute/datamapplot) | 把嵌入的二维投影画成带标签的静态或交互式“数据地图”的 Python 库。<br>给簇的点加标签后自动排版；社区页列出了用它做的交互地图，包括 Semantic Map of GitHub。 ✓ | [仓库](https://github.com/TutteInstitute/datamapplot "核对依据：PyPI 包元数据声明的仓库") ✓ | [展示页](https://datamapplot.readthedocs.io/en/latest/) ✓ | — | 开源 |
| [Embedding Atlas](https://apple.github.io/embedding-atlas/) | Apple 的开源嵌入可视化工具：二维地图加密度等高线、自动聚类标签和元数据联动视图。<br>几百万个点的嵌入怎样低门槛地搜索、找近邻并联动过滤。 ✓ | [仓库](https://github.com/apple/embedding-atlas "核对依据：PyPI、npm 包元数据声明的仓库") ✓ | [展示页](https://apple.github.io/embedding-atlas/) ✓ | — | 开源 |
| [UpSet](https://upset.app/) | 用矩阵加条形图表示多个集合的交集，替代集合超过三四个以后的 Venn 图。<br>集合很多时怎样排序、聚合和查询交集；元素的属性怎样接在交集旁边。 ✓ | [仓库](https://github.com/visdesignlab/upset2 "核对依据：upset.app/implementations 页面的 Source Code 链接（UpSet 2）") ✓ | [展示页](https://upset.app/) ✓ | — | 2014 年原版 UpSet 的仓库是 VCG/upset，upset.app 的实现页同时列了两个；这里记的是新版 UpSet 2。 |
| [Voyager](https://idl.uw.edu/papers/voyager) | 把分面浏览和可视化推荐结合起来的探索工具：字段很多时自动给出一批候选图。<br>高维表格里不靠手工逐张指定图，而是浏览推荐的图；展示数据的变化而不是设计的变化。 ✓ | [仓库](https://github.com/vega/voyager "核对依据：npm 包元数据声明的仓库") ✓ | [展示页](https://vega.github.io/voyager/) ✓ | [站点](https://idl.uw.edu/papers/voyager) | 开源；npm 包 datavoyager 最近一次发布是 2022-06-14（2.0.0-alpha.24）。展示页由 JS 渲染，页面文字只有标题。 |
| [regl-scatterplot](https://github.com/flekschas/regl-scatterplot)<br>（主分类 L1/chart-and-visualization-engines） | 基于 WebGL 的交互式二维散点图，面向大量数据点。<br>几十万以上的点如何做到可缩放、可选择、可编码；投影结果的前端落地。 ✓ | [仓库](https://github.com/flekschas/regl-scatterplot "核对依据：npm 包元数据声明的仓库") ✓ | [展示页](https://flekschas.github.io/regl-scatterplot/) ✓ | — | 开源；展示页由 WebGL 渲染，页面文字只有标题；说明依据是 npm 包的 README。 |

### 三维空间与大规模关系探索

<sub>L2/3d-and-large-graphs</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [PyGraphistry](https://github.com/graphistry/pygraphistry) | 将图分析数据接入 GPU 图探索环境。<br>GPU 图探索。 △ | [仓库](https://github.com/graphistry/pygraphistry "核对依据：PyPI 包元数据") ✓ | [展示页](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html) ✓ | — | 开源；官方页面没找到依据的说明：GPU 图探索环境（正文只有导航条目） |
| [deck.gl](https://github.com/visgl/deck.gl)<br>（主分类 L1/chart-and-visualization-engines） | GPU 加速的大数据可视化框架。<br>大规模数据、地图图层、多视角渲染。 ✓ | [仓库](https://github.com/visgl/deck.gl "核对依据：npm 包元数据") ✓ | [展示页](https://deck.gl/gallery/) ✓ | — | 开源 |
| [React Force Graph](https://github.com/vasturiano/react-force-graph)<br>（主分类 L1/canvas-2d-and-3d） | 2D、3D、VR、AR 关系图。<br>官方示例含点击展开折叠、相机聚焦、方向箭头、动态数据和不同空间模式，对复杂图的空间交互有参考价值。 ✓ | [仓库](https://github.com/vasturiano/react-force-graph "核对依据：npm 包元数据") ✓ | [展示页](https://vasturiano.github.io/react-force-graph/) ✓ | — | 开源 |
| [Cosmos.gl](https://github.com/cosmosgl/graph)<br>（主分类 L1/canvas-2d-and-3d） | GPU 加速的力导向图。<br>使用 GPU 做布局计算与图形渲染，面向大规模网络。 ✓ | [仓库](https://github.com/cosmosgl/graph "核对依据：npm 包元数据") ✓ | [展示页](https://cosmos.gl/) | [文档](https://openjsf.org/blog/introducing-cosmos-gl) | 开源；展示页是 Storybook 示例站，页面标题是通用的 Storybook 标题，具体示例未确认。 |

### 系统动力学与因果建模

<sub>L2/systems-modeling</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Insight Maker](https://www.insightmaker.com/) | 在线的系统动力学与仿真建模：存量流量图、因果回路、基于主体的模型。<br>在浏览器里搭建并运行存量流量模型；公开的仿真模型库里有浴缸、储蓄账户等例子（据搜索结果摘要）。属于“因果与反馈”家族。 ✓ | 待补 | [展示页](https://www.insightmaker.com/tag/simulation?page=3) ✓ | [站点](https://www.insightmaker.com/) | 不在调研报告里，是核对图形范式展示页时发现的。是否开源、仓库地址未核实。 |
| [Kumu](https://kumu.io/)<br>（主分类 L3/knowledge-workspaces） | 复杂系统、利益相关方和关系地图。<br>关系探索、视图定义、叙事展示。研究对象与软件流程编辑器明显不同。 ✓ | — | [展示页](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative) ✓ | [站点](https://kumu.io/) · [文档](https://docs.kumu.io/frequently-asked-questions/where-can-i-find-example-kumu-projects) | 商业产品；不能直接二次开发；作为可体验的交互案例收录。 |

## L3 成熟应用与综合交互系统

### AI 应用与工作流开发平台

<sub>L3/ai-development-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Dify](https://dify.ai/) | 构建、发布、运行 AI 应用。<br>工作流、知识检索及执行观察；节点编辑、测试、节点结果检查、应用管理。 △ | [仓库](https://github.com/langgenius/dify "核对依据：官网 dify.ai 的 GitHub 链接") ✓ | [展示页](https://marketplace.dify.ai/) ✓ | [站点](https://dify.ai/) | 含附加条件的许可证；官网自称 Source-available、Apache-2.0-derivative license（dify.ai，2026-10-13 访问）；具体附加条件在 GitHub 的 LICENSE 里，未核实。展示页是官方市场，含可复制的工作流模板；官方页面没找到依据的说明：节点结果检查 |
| [Langflow](https://www.langflow.org/) | 构建和发布 Agent 工作流。<br>可视节点编排与执行测试；编辑、Playground、调试、API 发布的闭环。据官方文档可发布为 API 或 MCP 服务，并与可观测性平台集成。 △ | [仓库](https://github.com/langflow-ai/langflow "核对依据：PyPI 包元数据") ✓ | [展示页](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/) ✓ | [站点](https://www.langflow.org/) · [文档](https://docs.langflow.org/) | 开源；展示页是官网模板页之一；模板总览页 /templates 返回 404；官方页面没找到依据的说明：与可观测性平台集成、调试 |
| [n8n](https://github.com/n8n-io/n8n) | 通用业务自动化及 AI 工作流。<br>自动化流程设计与执行诊断；节点编辑、运行历史、失败定位、重新执行。 △ | [仓库](https://github.com/n8n-io/n8n "核对依据：npm 包元数据") ✓ | [展示页](https://n8n.io/workflows/) ✓ | — | 源码可见但有使用限制；docs.n8n.io 写明采用 Sustainable Use License 与 Enterprise License，均基于 fair-code 模式（2026-10-13 核对）；报告称其不是 OSI 意义上的开源；官方页面没找到依据的说明：AI 工作流 |
| [Node-RED](https://github.com/node-red/node-red) | 事件驱动流程与设备、服务集成。<br>消息流的可视编排；部署、调试、运行时数据观察。 △ | [仓库](https://github.com/node-red/node-red "核对依据：npm 包元数据") ✓ | [展示页](https://flows.nodered.org/) ✓ | — | 开源；官方页面没找到依据的说明：服务集成 |
| [Flowise](https://flowiseai.com/) | LLM、工具与 Agent 流程构建。<br>Agentflow 图编辑器；条件、循环、状态与工具节点。 ✓ | [仓库](https://github.com/FlowiseAI/Flowise "核对依据：官网 flowiseai.com 的 GitHub 链接") ✓ | 待收集 | [站点](https://flowiseai.com/) · [文档](https://docs.flowiseai.com/) | 开源；已停止维护；官网 flowiseai.com/sunset 宣布停止运营：2026-07-29 代码冻结，2026-08-10 仓库转为公共归档，2026-08-31 终止支持；代码仍为 Apache 2.0，可自行 fork（2026-10-13 访问）。页面仍用将来时，仓库当前是否已归档需在 GitHub 上核实。 |

### Agent 开发、协作与管理平台

<sub>L3/agent-management</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AgentScope 2.0](https://github.com/agentscope-ai/agentscope) | Agent 团队编排、运行和观测。<br>团队及执行信息进入 Web UI；Agent 团队运行与实时观察。 ✓ | [仓库](https://github.com/agentscope-ai/agentscope "核对依据：PyPI 包元数据") ✓ | 无：Studio 在本地运行，没有公开在线演示 | [文档](https://docs.agentscope.io/) | 开源；维护状态待核查；报告称旧版独立 AgentScope Studio 已不再单独维护。doc.agentscope.io 的 Studio 页仍写着“The Studio is under fast development”，页脚年份是 2025，可能已过时；docs.agentscope.io 的 2.0.9 文档没有提到 Studio（2026-10-13 核对）。Studio 当前状态待核查。 |
| [LangGraph / Studio](https://github.com/langchain-ai/langgraph) | 图状态、任务路由与 Agent 开发。<br>图结构与运行状态、调试会话之间的关联。 △ | [仓库](https://github.com/langchain-ai/langgraph "核对依据：PyPI 包元数据") ✓ | 无：Studio 需账号或在本地运行，没有公开演示 | [文档](https://docs.langchain.com/langsmith/studio) | 开源；LangGraph Studio / LangSmith Studio 有账号及运行环境要求；官方页面没找到依据的说明：任务路由 |
| [AgentEnsemble](https://agentensemble.github.io/agentensemble/) | 团队任务编排和执行分析。<br>DAG、时间图、通过事件流实时更新的执行看板，以及人工审核交互，把任务执行事件与人工干预放进同一过程。 △ | [仓库](https://github.com/AgentEnsemble/agentensemble "核对依据：官方文档站 docs.agentensemble.net 的 GitHub 链接") ✓ | 无：Live Dashboard 在本地运行（localhost:7329），没有托管的公开演示 | [站点](https://agentensemble.github.io/agentensemble/) · [文档](https://docs.agentensemble.net/guides/visualization/) | 官方页面没找到依据的说明：任务执行事件与人工干预放进同一过程 |
| [AutoGen / AutoGen Studio](https://github.com/microsoft/autogen) | Agent 原型构建与团队交互。<br>智能体团队的可视化原型、运行测试；Studio 定位为原型，不是生产级应用。 ✓ | [仓库](https://github.com/microsoft/autogen "核对依据：AutoGen Studio 官方文档页的 GitHub 链接") ✓ | 无：AutoGen Studio 在本地运行，没有托管的公开演示 | [文档](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html) | PyPI 上 autogen-agentchat 最近一次发布是 2025-09-30（v0.7.5），查询于 2026-10-13；包元数据没有声明仓库地址。 |

### LLM 与 Agent 可观测性平台

<sub>L3/observability-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Langfuse](https://github.com/langfuse/langfuse) | 追踪、评测、提示词管理、数据集及实验。<br>Trace、调用详情、耗时、Token、成本及评测。可从一次异常执行进入提示词、测试数据和评测过程，形成分析、修改、再验证的闭环。 △ | [仓库](https://github.com/langfuse/langfuse "核对依据：官网文档页的 GitHub 链接") ✓ | [展示页](https://langfuse.com/docs/demo) ✓ | — | 官方页面没找到依据的说明：从一次异常执行进入提示词 |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | AI 应用追踪与质量评测。<br>基于 OpenTelemetry 的调用轨迹、问题诊断、评测分析。 ✓ | [仓库](https://github.com/Arize-ai/phoenix "核对依据：PyPI 包元数据") ✓ | [展示页](https://phoenix-demo.arize.com/) ✓ | — | 源码可见但有使用限制；PyPI 上 arize-phoenix 的许可证是 Elastic-2.0，不是 OSI 意义上的开源许可（2026-10-13 核对）。 |
| [Comet Opik](https://www.comet.com/site/products/opik/) | LLM / Agent 追踪、评测和监控。<br>多层调用、评测结果、运行监控。 △ | [仓库](https://github.com/comet-ml/opik "核对依据：PyPI 包元数据") ✓ | 待收集 | [站点](https://www.comet.com/site/products/opik/) | 开源；官方页面没找到依据的说明：多层（嵌套）调用 |
| [AgentOps](https://www.agentops.ai/) | Agent 执行记录、调试与成本观察。<br>会话回放、调用轨迹、成本。 ✓ | [仓库](https://github.com/AgentOps-AI/agentops "核对依据：PyPI 包元数据") ✓ | 无：控制台需登录（app.agentops.ai 跳转到登录页），没有找到免登录的公开示例 | [站点](https://www.agentops.ai/) · [文档](https://docs.agentops.ai/v2/introduction) | 开源；PyPI 上 agentops 最近一次发布是 2025-08-29（v0.4.21），查询于 2026-10-13。 |
| [LangWatch](https://langwatch.ai/) | LLM 运行追踪、分析与评测。<br>Trace、质量指标与运行分析。 ✓ | [仓库](https://github.com/langwatch/langwatch "核对依据：官网 langwatch.ai 的 GitHub 链接") ✓ | [展示页](https://app.langwatch.ai/demo) | [站点](https://langwatch.ai/) | 展示页由前端渲染，内容以及是否免登录都没有确认。 |

### 软件架构、开发者平台与工程管理

<sub>L3/software-engineering-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Nx](https://github.com/nrwl/nx) | Monorepo 构建与任务管理。<br>把组成结构和任务结构分开：Project Graph 表示项目间依赖，Task Graph 表示实际构建任务及执行依赖。可聚焦项目、查看邻近项目、按文件夹分组、分析影响范围、导出图数据。 ✓ | [仓库](https://github.com/nrwl/nx "核对依据：npm 包元数据") ✓ | [展示页](https://nx.dev/docs/features/explore-graph) | — | 开源；展示页是官方文档页，据检索页面内嵌可交互的项目图示例，由 JS 加载，渲染情况未确认。 |
| [Backstage](https://github.com/backstage/backstage) | 开发者门户与软件服务目录。<br>Catalog Graph：实体中心视角，按关系和实体类别筛选，控制展开深度、方向和连线合并，并与实体详情联动。 △ | [仓库](https://github.com/backstage/backstage "核对依据：npm 包元数据") ✓ | [展示页](https://demo.backstage.io/catalog) ✓ | [文档](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/) | 开源；官方强调服务目录反映的是便于人理解的组织与软件模型，而不是所有实时关系的唯一真实来源。公开 Demo 站点上是否启用了关系图未确认；官方页面没找到依据的说明：图中节点与实体详情联动 |
| [Structurizr DSL](https://github.com/structurizr/dsl)<br>（主分类 L1/diagram-languages） | 统一 C4 架构模型及多视角定义。<br>把模型与视图分离：一份结构模型可以定义多张不同视角的图。 △ | [仓库](https://github.com/structurizr/dsl) | [展示页](https://docs.structurizr.com/example) ✓ | — | 官方文档站页脚的 GitHub 链接指向 structurizr/structurizr（整个产品），没有单独写 DSL 的仓库；这里的 structurizr/dsl 是否仍是主仓库未核实；官方页面没找到依据的说明：模型与视图分离 |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 △ | [仓库](https://github.com/Egonex-AI/Understand-Anything "核对依据：项目官网 understand-anything.com 的 GitHub 链接") ✓ | [展示页](https://understand-anything.com/) ✓ | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析；官方页面没找到依据的说明：变更影响分析、先解析显式链接再用模型发现隐式关系、带类型的知识网络 |
| [LikeC4](https://likec4.dev/)<br>（主分类 L2/software-architecture） | 不限固定层级的架构模型、视角投影与交互展示。<br>模型与视图分离：一份结构模型生成不同范围、不同视角的图，可分层钻取。既有建模语言，也有架构可视化和完整的交互查看器。 ✓ | [仓库](https://github.com/likec4/likec4 "核对依据：npm 包元数据") ✓ | [展示页](https://likec4.dev/showcases/bigbank/) ✓ | [站点](https://likec4.dev/) | 开源 |

### 数据平台与基础设施管理

<sub>L3/data-and-infrastructure</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [DataHub](https://github.com/datahub-project/datahub) | 数据发现、治理与影响分析。<br>数据集、字段、流水线的血缘；从资产详情进入上下游影响网络，支持字段级钻取和影响分析。 △ | [仓库](https://github.com/datahub-project/datahub "核对依据：PyPI 包元数据") ✓ | [展示页](https://datahub.com/demos/data-lineage-with-datahub/) ✓ | [文档](https://docs.datahub.com/) | 开源；该展示页是录制的血缘功能演示，不是开放试用；官方页面没找到依据的说明：从资产详情进入上下游影响网络 |
| [OpenMetadata](https://github.com/open-metadata/OpenMetadata) | 数据资产管理与治理。<br>资产关系、字段级血缘；从数据目录导航到血缘关系。 ✓ | [仓库](https://github.com/open-metadata/OpenMetadata "核对依据：PyPI 包元数据") ✓ | [展示页](https://sandbox.open-metadata.org/) ✓ | [文档](https://docs.open-metadata.org/latest/quick-start/sandbox) | 沙盒需要用 Google 账号登录。PyPI 上 openmetadata-ingestion 的许可证标为 Collate Community License Agreement（2026-10-13 核对）；整个项目的许可证未核实。 |
| [Apache SkyWalking](https://skywalking.apache.org/) | 服务性能监控与故障诊断。<br>服务、实例、接口、部署等层级；从宏观服务拓扑进入监控、日志与 Trace，多视图联动。其生态中出现了基础设施三维可视化的探索。 △ | [仓库](https://github.com/apache/skywalking "核对依据：官网 skywalking.apache.org 的 GitHub Issue Tracker 链接") ✓ | [展示页](https://demo.skywalking.apache.org/) ✓ | [站点](https://skywalking.apache.org/) · [文档](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/) | 官网首页链接到在线 Demo（Horizon UI，示例数据）和一个独立的 3D 基础设施地图交互演示（2026-10-13 访问）；官方页面没找到依据的说明：“部署”层级、多视图联动 |
| [Kiali](https://github.com/kiali/kiali) | 服务网格运行观察。<br>流量图、服务关系、异常定位。 ✓ | [仓库](https://github.com/kiali/kiali "核对依据：官方文档页的“Create project issue”链接指向该仓库") ✓ | 待收集 | [文档](https://kiali.io/docs/features/topology/) | — |
| [Grafana](https://github.com/grafana/grafana) | 观测数据看板与分析。<br>指标、日志、Trace、服务关系。 △ | [仓库](https://github.com/grafana/grafana "核对依据：npm 包元数据") ✓ | [展示页](https://play.grafana.org/) ✓ | — | 开源；官方页面没找到依据的说明：服务关系（play.grafana.org 由 JS 渲染，读不到） |

### 知识组织、概念地图与认知工具

<sub>L3/knowledge-workspaces</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [AFFiNE](https://affine.pro/) | 文档、知识库与无限白板。<br>将线性文本与空间组织结合。 ✓ | [仓库](https://github.com/toeverything/AFFiNE "核对依据：官网 affine.pro 的 GitHub 与 License 链接") ✓ | [展示页](https://affine.pro/templates) ✓ | [站点](https://affine.pro/) | 展示页是模板库页面，不是在线试用；没有找到免登录的在线版本。 |
| [diagrams.net / draw.io](https://www.drawio.com/) | 通用结构图创建与编辑。<br>手动构造架构图、流程图、认知图。 ✓ | [仓库](https://github.com/jgraph/drawio "核对依据：官网 drawio.com 的 GitHub 链接") ✓ | [展示页](https://www.drawio.com/docs/diagram-types/) ✓ | [站点](https://www.drawio.com/) | — |
| [Kumu](https://kumu.io/) | 复杂系统、利益相关方和关系地图。<br>关系探索、视图定义、叙事展示。研究对象与软件流程编辑器明显不同。 ✓ | — | [展示页](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative) ✓ | [站点](https://kumu.io/) · [文档](https://docs.kumu.io/frequently-asked-questions/where-can-i-find-example-kumu-projects) | 商业产品；不能直接二次开发；作为可体验的交互案例收录。 |
| [Logseq](https://github.com/logseq/logseq) | 双向链接、页面及知识块。<br>大纲、链接和知识图导航。 △ | [仓库](https://github.com/logseq/logseq "核对依据：Homebrew cask 记录的下载来源（github.com/logseq/logseq/releases）") ✓ | [展示页](https://demo.logseq.com/) ✓ | — | 官方页面没找到依据的说明：大纲、知识图导航（官网由 JS 渲染，读不到） |
| [InfraNodus](https://infranodus.com/) | 文本网络与结构探索。<br>文本与概念的网络、主题群落、结构空白分析。 ✓ | [仓库](https://github.com/noduslabs/infranodus) | [展示页](https://infranodus.com/graphs) ✓ | [站点](https://infranodus.com/) | 商业产品；官网说明开源的是一组支撑 InfraNodus 的工具（AGPL 许可），页脚列出 GitHub 上的 Workflows、Datasets、Tools API 和 GraphRAG MCP Server（infranodus.com，2026-10-13 访问）；报告所说“旧仓库不代表当前产品全部功能”未核实。 |

### 生态地图与产业分析产品

<sub>L3/market-and-ecosystem-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [CNCF Landscape](https://landscape.cncf.io/) | 大型生态分类数据与实际展示案例。<br>浏览技术类别、生态参与者、项目属性；表达分类与生态分布，不擅长展示大量跨类别依赖。 △ | [仓库](https://github.com/cncf/landscape) | [展示页](https://landscape.cncf.io/) ✓ | — | 仓库地址未核实：landscape.cncf.io 由 JS 渲染，读不到源码链接；官方页面没找到依据的说明：实际展示案例、浏览功能（landscape 页面由 JS 渲染，读不到） |
| [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar) | 技术采用建议与趋势。<br>表达经过研究者判断的技术采用建议，而不是技术、产品、需求之间的完整关系。 ✓ | — | [展示页](https://www.thoughtworks.com/radar) ✓ | — | — |
| [OSS Insight](https://ossinsight.io/) | GitHub 项目和开发生态数据分析。<br>研究 GitHub 活跃度、生态指标及时间变化。 ✓ | [仓库](https://github.com/pingcap/ossinsight "核对依据：官网 About 页的 GitHub 链接") ✓ | [展示页](https://ossinsight.io/) ✓ | — | — |
| [OSS Compass](https://oss-compass.org/) | 开源项目健康与生态指标分析。<br>多指标比较开源项目的生态表现。 ✓ | [仓库](https://github.com/oss-compass/compass-web) | [展示页](https://oss-compass.org/) ✓ | — | 官网 About 页只链到 GitHub 组织 github.com/oss-compass，具体到 compass-web 这个仓库未核实。 |

### 数据与嵌入探索平台

<sub>L3/data-exploration-platforms</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Nomic Atlas](https://docs.nomic.ai/atlas/datasets/data-maps/how-atlas-works/1-key_terms) | 把大规模文本或嵌入数据变成可在浏览器里探索的二维地图的云平台。<br>嵌入到二维用什么投影（UMAP 与自研投影按规模切换）、主题层级与标签、分享与筛选。 ✓ | — | 待收集 | [文档](https://docs.nomic.ai/atlas/datasets/data-maps/how-atlas-works/1-key_terms) | 商业产品；商业云平台，Python 客户端 nomic 在 PyPI（包元数据声明的仓库是 nomic-ai/nomic，客户端不是平台本身）；技术报告写明无法公开许多技术细节。没有收展示页：atlas.nomic.ai 静态读到标题“Nomic Atlas”，但无头 Chromium 实际打开（2026-10-14）会跳到 nomic.ai/developer，是 Nomic Agent API（面向建筑工程图纸与文档）的产品页，不是地图；atlas.nomic.ai/data/nomic/news 未登录时显示 Page Not Found；文档站仍在写 Atlas，没有链到公开示例地图。 |
| [Orange](https://orangedatamining.com/) | 开源的数据挖掘与可视化软件，用组件搭流程；可视化组件里有 Radviz、FreeViz 等多维投影。<br>VizRank 在众多可能的投影里替人挑出“有信息”的那几张；锚点可以拖动。 ✓ | [仓库](https://github.com/biolab/orange3 "核对依据：官网首页的 GitHub 链接；PyPI 包元数据") ✓ | 无：桌面软件，没有在线展示页。 | [站点](https://orangedatamining.com/) · [文档](https://orangedatamining.com/docs) | 开源；许可证 GPLv3+（PyPI 元数据）。 |

## 第四板块 结构提炼与认知建模

### 结构提取

<sub>cognition/information-extraction</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Tree-sitter](https://github.com/tree-sitter/tree-sitter) | 程序源代码的语法树与增量解析。<br>输入是源码。语法事实不直接等于架构语义。 ✓ | [仓库](https://github.com/tree-sitter/tree-sitter "核对依据：npm 包元数据") ✓ | [展示页](https://tree-sitter.github.io/tree-sitter/7-playground.html) ✓ | — | 开源 |
| [Docling](https://github.com/docling-project/docling) | PDF、文档等的版面、标题、表格及文档结构提取。<br>输入是文档。文档结构不等于知识结构。 ✓ | [仓库](https://github.com/docling-project/docling "核对依据：PyPI 包元数据") ✓ | [展示页](https://huggingface.co/spaces/docling-project/SmolDocling-256M-Demo) | — | 开源；展示页是 SmolDocling 视觉语言模型的演示，不是 Docling 库本身。 |
| [Docling Graph](https://github.com/docling-project/docling-graph) | 从结构化文档内容进一步提取结构化实体与关系。<br>需要约束关系类型和语义准确性。 ✓ | [仓库](https://github.com/docling-project/docling-graph "核对依据：PyPI 包元数据") ✓ | 待收集 | [文档](https://docling-project.github.io/docling-graph/) | 开源 |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 △ | [仓库](https://github.com/Egonex-AI/Understand-Anything "核对依据：项目官网 understand-anything.com 的 GitHub 链接") ✓ | [展示页](https://understand-anything.com/) ✓ | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析；官方页面没找到依据的说明：变更影响分析、先解析显式链接再用模型发现隐式关系、带类型的知识网络 |

### 多层知识建模

<sub>cognition/multilevel-knowledge-modeling</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) | 对非结构化文本做实体关系抽取、社区分层、社区摘要。<br>路径：文本片段、实体关系与声明提取、图社区发现与层级聚类、各层级社区摘要、全局与局部检索。图社区层级不等于认知的逻辑抽象层级，只能作为辅助，不能替代语义分层。 ✓ | [仓库](https://github.com/microsoft/graphrag "核对依据：PyPI 包元数据") ✓ | 无：命令行流水线，官方建议导出后用 Gephi 查看 | [站点](https://microsoft.github.io/graphrag/) · [文档](https://microsoft.github.io/graphrag/visualization_guide/) | 开源；维护状态待核查；报告称官方文档显示仓库主要处于维护模式；microsoft.github.io/graphrag 的首页、get_started、overview 页里没有找到这样的表述，GitHub README 未核实（2026-10-13）。官方可视化指南建议把图导出为 GraphML 后用 Gephi 查看，没有专门的可视化器。 |
| [LightRAG](https://github.com/HKUDS/LightRAG) | 图结构检索与知识网络可视化。<br>检索结构与认知模型并不完全相同。 | [仓库](https://github.com/HKUDS/LightRAG "核对依据：PyPI 包元数据") ✓ | 无：WebUI 需自行部署，没有公开在线演示 | — | 开源 |

### 动态与演化的知识结构

<sub>cognition/evolving-knowledge-structures</sub>

| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Graphiti](https://github.com/getzep/graphiti) | 带时间属性的实体和关系，保留来源。<br>时间化事实、原始 Episode、增量知识更新、显式或学习得到的关系类型；能区分“过去成立”“现在成立”和“存在冲突”。 △ | [仓库](https://github.com/getzep/graphiti "核对依据：PyPI 包元数据") ✓ | 无：开源库本身没有可视化界面，图浏览器在需账号的 Zep 控制台里 | [文档](https://help.getzep.com/graphiti/getting-started/overview) | 开源；官方页面没找到依据的说明：学习得到的关系类型 |

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
