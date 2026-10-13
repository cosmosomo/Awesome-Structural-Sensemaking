# 案例画廊：打开看是什么样子

> 本页由 `scripts/build.py` 根据 `catalog/case-gallery.json` 生成，请改数据，不要直接改这里。

每个案例收了三样东西：**展示页**（能直接看到或试一试的在线页面）、**图片**（官方页面上嵌的、**这个案例画出来的那张视图本身**：主视图的截图或论文里的结果图，点图片打开原图；架构图、方法流程图、数据模型图、设置面板、聊天界面、表单、模板和宣传页不收，它们在数据里标了 `shows`，不显示）、**网页**（最能说明它长什么样的官方页面）。图片只存地址，不转存，版权属于各自的来源。

- 展示页和网页由脚本逐个访问核对状态与标题（`scripts/check_gallery.py`）；图片核对了它真是图片、像素尺寸够大。
- 展示页大多是 JS 渲染的，只看 HTTP 状态不够，所以另用无头 Chromium 真实打开（`scripts/render_check.js`），记下页面文字量和 canvas、svg 的数量。这只能说明“打开后有内容”，不等于“展示得好”。
- 这些案例为什么这样归类、设计者怎么想，见 [案例表](case-analysis.md)；编码依据的官方原文见 [案例证据](case-evidence.md)。

<!-- gen:gallerystats: -->
97 个案例里，66 个有在线展示页（可操作 51、样例目录 11、视频或导览 1、需要登录 3），其中 66 个用无头 Chromium 实际打开过；49 个有官方图片，共 90 张。其余 31 个没找到在线展示页（命令行工具、规范、方法类，或官方页面读不到），原因写在各案例下。图片只存地址，不转存。
<!-- /gen -->

## 总表

“展示页”一列：**可操作**是能在页面里直接点、拖、试的；**样例目录**是一页列着许多样例，进去再挑；**视频/导览**是看别人演示。“—”是没找到（原因写在下面各案例里）。

<!-- gen:galleryindex: -->
| 案例 | 领域 | 主结构 | 展示页 | 图 | 网页 |
|---|---|---|---|---|---|
| [CNCF Landscape](https://landscape.cncf.io/) | 技术生态 | 集合与分类 | [可操作](https://landscape.cncf.io/) | 1 | 2 |
| [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar) | 技术生态 | 集合与分类 | [可操作](https://www.thoughtworks.com/radar) | — | 1 |
| [Zalando Tech Radar](https://github.com/zalando/tech-radar) | 技术生态 | 集合与分类 | [可操作](https://opensource.zalando.com/tech-radar/) | 1 | 1 |
| [Open Source AI Gap Map](https://www.aipotluck.org/map) | 开源生态评估 | 集合与分类 | [可操作](https://www.aipotluck.org/map/gap-map) | 2 | 2 |
| [Grafana](https://github.com/grafana/grafana) | 基础设施运维 | 表与多维属性 | [可操作](https://play.grafana.org/) | — | 1 |
| [Build Your Own Radar](https://github.com/thoughtworks/build-your-own-radar) | 技术生态 | 表与多维属性 | [可操作](https://radar.thoughtworks.com/) | — | 1 |
| [OSS Insight](https://ossinsight.io/) | 开源生态 | 表与多维属性 | [可操作](https://ossinsight.io/) | 1 | 1 |
| [OSS Compass](https://oss-compass.org/) | 开源生态 | 表与多维属性 | [可操作](https://oss-compass.org/os-situation) | 2 | 2 |
| [PyGraphistry](https://github.com/graphistry/pygraphistry) | 数据分析 | 表与多维属性 | — | 3 | 2 |
| [Wikidata Query Service 结果视图](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views) | 开放知识图谱 | 表与多维属性 | [可操作](https://query.wikidata.org/) | 1 | 1 |
| [Gapminder 气泡图](https://www.gapminder.org/tools/) | 国际发展统计 | 表与多维属性 | [可操作](https://www.gapminder.org/tools/) | — | 2 |
| [CodeBoarding](https://codeboarding.org/) | 软件工程 | 层级与树 | [可操作](https://app.codeboarding.org/CodeBoarding/CodeBoarding) | 3 | 2 |
| [LikeC4](https://likec4.dev/) | 软件工程 | 层级与树 | [可操作](https://playground.likec4.dev/w/bigbank/) | — | 1 |
| [AgentPrism](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces) | AI Agent 观测 | 层级与树 | [可操作](https://agent-prism.evilmartians.io/) | 2 | 1 |
| [Jaeger](https://github.com/jaegertracing/jaeger) | 分布式系统运维 | 层级与树 | [可操作](https://demo.jaegertracing.io/jaeger/) | — | 2 |
| [Grafana Tempo](https://github.com/grafana/tempo) | 分布式系统运维 | 层级与树 | — | — | 2 |
| [AgentScope 2.0](https://docs.agentscope.io/) | AI Agent 开发 | 层级与树 | — | 1 | 2 |
| [Langfuse](https://github.com/langfuse/langfuse) | AI 应用观测 | 层级与树 | [可操作](https://langfuse.com/docs/demo) | 2 | 2 |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | AI 应用观测 | 层级与树 | [可操作](https://phoenix-demo.arize.com/) | 1 | 2 |
| [Comet Opik](https://www.comet.com/site/products/opik/) | AI 应用观测 | 层级与树 | — | 2 | 2 |
| [AgentOps](https://www.agentops.ai/) | AI 应用观测 | 层级与树 | — | 2 | 1 |
| [LangWatch](https://langwatch.ai/) | AI 应用观测 | 层级与树 | [需登录](https://app.langwatch.ai/demo) | — | 1 |
| [AFFiNE](https://affine.pro/) | 知识管理 | 层级与树 | [样例目录](https://affine.pro/templates) | — | 2 |
| [Tree-sitter](https://github.com/tree-sitter/tree-sitter) | 软件工程 | 层级与树 | [可操作](https://tree-sitter.github.io/tree-sitter/7-playground.html) | — | 2 |
| [Docling](https://github.com/docling-project/docling) | 文档处理 | 层级与树 | [可操作](https://huggingface.co/spaces/docling-project/SmolDocling-256M-Demo) | — | 2 |
| [Nextstrain / Auspice](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html) | 流行病与基因组 | 层级与树 | [可操作](https://nextstrain.org/ncov/open/global/6m) | 2 | 2 |
| [OneZoom 生命之树](https://www.onezoom.org/introduction) | 生物分类 | 层级与树 | [可操作](https://www.onezoom.org/) | 2 | 2 |
| [Reactome 通路浏览器](https://reactome.org/userguide/pathway-browser) | 分子生物学通路 | 层级与树 | — | 3 | 2 |
| [CodeCity](https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf) | 软件演化与度量 | 层级与树 | — | — | 1 |
| [Treemap（磁盘空间）](https://www.cs.umd.edu/hcil/treemap-history/) | 文件系统与资源占用 | 层级与树 | [样例目录](https://d3-graph-gallery.com/treemap.html) | 3 | 2 |
| [火焰图](https://www.brendangregg.com/flamegraphs.html) | 性能剖析 | 层级与树 | [可操作](https://www.brendangregg.com/FlameGraphs/cpu-mysql-updated.svg) | 1 | 2 |
| [Universal Dependencies 依存树](https://universaldependencies.org/introduction.html) | 语言学 | 层级与树 | [可操作](https://universaldependencies.org/conllu_viewer.html) | — | 2 |
| [Wikipedia 摘要式写作](https://en.wikipedia.org/wiki/Wikipedia:Summary_style) | 百科写作 | 层级与树 | — | — | 2 |
| [Markmap](https://markmap.js.org/docs/markmap) | 知识管理与写作 | 层级与树 | [可操作](https://markmap.js.org/repl) | — | 2 |
| [ATLAS：用多个 LLM Agent 自动构建软件仓库分类体系](https://arxiv.org/abs/2606.21597) | 软件仓库分类 | 层级与树 | [可操作](https://atlas-taxonomy.netlify.app/) | — | 2 |
| [Speculora](https://speculora.com/) | 市场需求分析 | 层级与树 | [可操作](https://speculora.com/) | — | 2 |
| [AgentEnsemble Viz](https://docs.agentensemble.net/guides/visualization/) | AI Agent 开发 | 有向无环图 | — | — | 2 |
| [Marquez](https://marquezproject.ai/) | 数据工程 | 有向无环图 | — | 2 | 2 |
| [AgentEnsemble](https://agentensemble.github.io/agentensemble/) | AI Agent 开发 | 有向无环图 | — | — | 2 |
| [Nx](https://nx.dev/docs/features/explore-graph) | 软件工程 | 有向无环图 | [可操作](https://nrwl-nx-examples-dep-graph.netlify.app/?focus=cart) | — | 1 |
| [DataHub](https://docs.datahub.com/) | 数据工程 | 有向无环图 | [视频/导览](https://datahub.com/demos/data-lineage-with-datahub/) | — | 1 |
| [OpenMetadata](https://docs.open-metadata.org/latest/quick-start/sandbox) | 数据工程 | 有向无环图 | [需登录](https://sandbox.open-metadata.org/) | 2 | 1 |
| [Git 提交历史](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) | 版本控制 | 有向无环图 | [可操作](https://learngitbranching.js.org/) | — | 2 |
| [家谱图的交互可视化](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf) | 谱系与家族史 | 有向无环图 | — | — | — |
| [Software Heritage Graph Dataset](https://registry.opendata.aws/software-heritage/) | 源代码历史图谱 | 有向无环图 | — | — | 2 |
| [dependency-cruiser](https://sverweij.github.io/dependency-cruiser/) | 软件工程 | 一般图与网络 | [可操作](https://sverweij.github.io/dependency-cruiser-repro-repo/458/) | 1 | 1 |
| [Madge](https://github.com/pahen/madge) | 软件工程 | 一般图与网络 | — | — | — |
| [pydeps](https://github.com/thebjorn/pydeps) | 软件工程 | 一般图与网络 | — | — | 1 |
| [Understand Anything](https://understand-anything.com/) | 软件工程 | 一般图与网络 | [可操作](https://understand-anything.com/) | — | — |
| [bpmn-js](https://github.com/bpmn-io/bpmn-js) | 业务流程 | 一般图与网络 | [可操作](https://demo.bpmn.io/) | 2 | 2 |
| [NeoDash](https://github.com/neo4j-labs/neodash) | 图数据库应用 | 一般图与网络 | — | 1 | 1 |
| [Dify](https://dify.ai/) | AI Agent 开发 | 一般图与网络 | [样例目录](https://marketplace.dify.ai/templates) | 2 | 2 |
| [Langflow](https://www.langflow.org/) | AI Agent 开发 | 一般图与网络 | [样例目录](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/) | 1 | 2 |
| [n8n](https://github.com/n8n-io/n8n) | 业务自动化 | 一般图与网络 | [样例目录](https://n8n.io/workflows/) | — | 2 |
| [Node-RED](https://github.com/node-red/node-red) | 物联网与事件流 | 一般图与网络 | [样例目录](https://flows.nodered.org/) | 1 | 2 |
| [Flowise](https://flowiseai.com/) | AI Agent 开发 | 一般图与网络 | — | 2 | 2 |
| [LangGraph / Studio](https://docs.langchain.com/langsmith/studio) | AI Agent 开发 | 一般图与网络 | — | — | 2 |
| [AutoGen / AutoGen Studio](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html) | AI Agent 开发 | 一般图与网络 | — | — | 1 |
| [Backstage](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/) | 软件工程 | 一般图与网络 | [可操作](https://demo.backstage.io/catalog) | — | 1 |
| [Apache SkyWalking](https://skywalking.apache.org/) | 分布式系统运维 | 一般图与网络 | [需登录](https://demo.skywalking.apache.org/) | — | 1 |
| [Kiali](https://kiali.io/docs/features/topology/) | 服务网格运维 | 一般图与网络 | — | 1 | 2 |
| [diagrams.net / draw.io](https://www.drawio.com/) | 通用绘图 | 一般图与网络 | [可操作](https://app.diagrams.net/) | 3 | 2 |
| [Kumu](https://kumu.io/) | 系统与关系分析 | 一般图与网络 | [可操作](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative) | 2 | 1 |
| [InfraNodus](https://infranodus.com/) | 文本分析与知识发现 | 一般图与网络 | [可操作](https://infranodus.com/live/hourlydailynews?background=default&most_influential=bc&maxnodes=150&demo=1&defaultlabelsize=14&labelsizeratio=2&demo=1) | 3 | 2 |
| [Docling Graph](https://docling-project.github.io/docling-graph/) | 文档处理 | 一般图与网络 | [可操作](https://docling-project.github.io/docling-graph/usage/examples/) | — | 2 |
| [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) | 文本检索与知识建模 | 一般图与网络 | — | 2 | 2 |
| [LightRAG](https://github.com/HKUDS/LightRAG) | 文本检索与知识建模 | 一般图与网络 | — | — | 1 |
| [Graphiti](https://help.getzep.com/graphiti/getting-started/overview) | Agent 记忆 | 一般图与网络 | [可操作](https://app.getzep.com/playground) | — | 2 |
| [伦敦地铁图（Beck）](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/) | 交通 | 一般图与网络 | — | 1 | 2 |
| [SBGN 系统生物学图形标记](https://sbgn.github.io/specifications) | 分子生物学通路 | 一般图与网络 | [样例目录](https://sbgn.github.io/examples) | 3 | 2 |
| [ICIJ Offshore Leaks 数据库](https://offshoreleaks.icij.org/pages/howtouse) | 调查报道与金融 | 一般图与网络 | [可操作](https://offshoreleaks.icij.org/) | — | 1 |
| [VOWL / WebVOWL 本体可视化](https://semantic-web-journal.net/content/visualizing-ontologies-vowl-0) | 本体与语义网 | 一般图与网络 | — | — | 2 |
| [Hive Plot](https://mk.bcgsc.ca/linnet/) | 网络分析（生物与社会网络） | 一般图与网络 | [可操作](https://bost.ocks.org/mike/hive/) | 2 | 1 |
| [Gephi](https://gephi.org/desktop/) | 通用网络分析 | 一般图与网络 | [可操作](https://lite.gephi.org/) | 3 | 2 |
| [设计结构矩阵 DSM](https://dsmweb.org/reading-a-dsm/) | 工程系统与产品架构 | 一般图与网络 | — | 3 | 2 |
| [Luhmann 的卡片盒](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf) | 知识管理与写作 | 一般图与网络 | — | — | — |
| [Git.Top Atlas](https://git.top/atlas) | 开源生态导航 | 一般图与网络 | [可操作](https://git.top/atlas) | — | 2 |
| [SemRepo](https://arxiv.org/abs/2605.13310) | 研究软件知识图谱 | 一般图与网络 | [可操作](https://semrepo.org/sparql) | — | 2 |
| [MOSS（研究软件知识图谱）](https://pretalx.com/juliacon-2025/talk/3EVLR9/) | 研究软件知识图谱 | 一般图与网络 | — | — | 1 |
| [Ecosyste.ms](https://packages.ecosyste.ms/) | 开源数据基础设施 | 一般图与网络 | [可操作](https://packages.ecosyste.ms/) | — | 1 |
| [OpenDigger](https://open-digger.cn/en/) | 开源活动指标 | 一般图与网络 | [可操作](https://open-digger.cn/en/docs/user-docs/metrics/playground) | — | 2 |
| [deps.dev（Open Source Insights）](https://docs.deps.dev/) | 软件供应链 | 一般图与网络 | [可操作](https://deps.dev/) | 1 | 2 |
| [CodeGraph（面向源代码的开放分类知识图谱）](https://arxiv.org/abs/2609.29474) | 代码知识图谱 | 一般图与网络 | [样例目录](https://huggingface.co/datasets/halykoss/CodeGraph/viewer/) | 1 | 2 |
| [Argdown](https://argdown.org/) | 论证与讨论 | 命题与论证 | [可操作](https://argdown.org/sandbox/) | 1 | 2 |
| [Kialo 论证树](https://support.kialo.com/en/) | 论证与讨论 | 命题与论证 | [可操作](https://www.kialo.com/should-us-internet-platforms-be-able-to-remove-or-demote-speech-by-elected-public-figures-39863) | 1 | 2 |
| [CmapTools 概念图](https://cmap.ihmc.us/) | 教育与知识建模 | 命题与论证 | [样例目录](https://cmap.ihmc.us/docs/itinerary.php) | 1 | 2 |
| [图尔敏论证模型](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html) | 论证与写作 | 命题与论证 | — | — | 1 |
| [OpenTelemetry GenAI 语义约定](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | AI Agent 观测 | 序列与事件流 | — | — | — |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | AI Agent 观测 | 序列与事件流 | — | 1 | 2 |
| [Up and Down the Ladder of Abstraction](https://worrydream.com/LadderOfAbstraction/) | 交互式写作与抽象 | 序列与事件流 | [可操作](https://worrydream.com/LadderOfAbstraction/) | — | — |
| [LLNL 美国能源流向图](https://flowcharts.llnl.gov/) | 能源 | 流量网络 | [样例目录](https://flowcharts.llnl.gov/commodities/energy) | 1 | 2 |
| [Embedding Projector](https://projector.tensorflow.org/) | 机器学习 | 空间与几何 | [可操作](https://projector.tensorflow.org/) | 3 | 2 |
| [Circos](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/) | 比较基因组 | 空间与几何 | — | 3 | 1 |
| [Semantic Map of GitHub](https://stevenfazzio.com/semantic-github-map/) | 开源生态地图 | 空间与几何 | [可操作](https://stevenfazzio.com/semantic-github-map/) | — | 1 |
| [Map of GitHub](https://anvaka.github.io/map-of-github/) | 开源生态地图 | 空间与几何 | [可操作](https://anvaka.github.io/map-of-github/) | — | — |
| [Insight Maker](https://www.insightmaker.com/) | 系统建模 | 因果与反馈 | [样例目录](https://www.insightmaker.com/explore) | 3 | 2 |
| [Explorable Explanations](https://worrydream.com/ExplorableExplanations/) | 交互式写作 | 因果与反馈 | [可操作](https://worrydream.com/TenBrighterIdeas/) | 2 | 2 |
<!-- /gen -->

## 图与网络

<!-- gen:gallery:graph -->
#### [dependency-cruiser](https://sverweij.github.io/dependency-cruiser/)

<sub>软件工程 · 一般图与网络 · 重点：连通与邻域、先后与依赖方向</sub>　找出项目里不该有的、奇怪的模块依赖

- 展示页（可直接操作）：[Demo: 3D graph reporter plugin for dependency-cruiser (issue #458) \| dependency-cruiser-repro-repo](https://sverweij.github.io/dependency-cruiser-repro-repo/458/)（页面正文 'Results (interactive html):' 下列出两个交互式 HTML 结果：dependency-cruiser 自身的内部图（节点为 bald）和 react 模块图，并给出运行命令）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1110 字</sub>
- 网页：[dependency-cruiser](https://sverweij.github.io/dependency-cruiser/)（官方站首页，正文说明它分析 JavaScript、TypeScript 等项目的依赖；首页上没有找到截图，只作官方入口）

<a href="https://sverweij.github.io/dependency-cruiser-repro-repo/458/dependency-cruiser-bald-nodes.png"><img src="https://sverweij.github.io/dependency-cruiser-repro-repo/458/dependency-cruiser-bald-nodes.png" width="230" alt="dependency-cruiser"></a>

<sub>图：dependency-cruiser（[来源页](https://sverweij.github.io/dependency-cruiser-repro-repo/458/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#dependency-cruiser)</sub>

#### [Madge](https://github.com/pahen/madge)

<sub>软件工程 · 一般图与网络 · 重点：环与反馈、连通与邻域</sub>　生成模块依赖图，发现循环依赖

- 展示页：没有找到在线展示页<sub>（官方在线演示未找到：npm 元数据里的 homepage 指向 https://github.com/pahen/madge（按规则不访问），www.npmjs.com/package/madge 返回 403，未绕过）</sub>

<sub>[编码与原文摘录](case-evidence.md#madge)</sub>

#### [pydeps](https://github.com/thebjorn/pydeps)

<sub>软件工程 · 一般图与网络 · 重点：环与反馈、连通与邻域</sub>　在大型 Python 项目里发现循环导入，并只看某个模块周围的依赖

- 展示页：没有找到在线展示页<sub>（命令行工具，文档站未找到在线演示）</sub>
- 网页：[pydeps — pydeps 3.0.9 documentation](https://pydeps.readthedocs.io/en/latest/index.html)（文档首页，页面写明它主要通过 pydeps 命令行使用，用于 Python 模块依赖可视化）

<sub>[编码与原文摘录](case-evidence.md#pydeps)</sub>

#### [Understand Anything](https://understand-anything.com/)

<sub>软件工程 · 一般图与网络 · 重点：连通与邻域、包含与层次</sub>　接手代码库时弄懂它由什么组成、怎么连接，并把代码对应到业务领域

- 展示页（可直接操作）：[Understand Anything — Graphs that teach the codebase](https://understand-anything.com/)（首页 'Live Demo →' 按钮及 'Live Demo' 区块（'See what your code is really doing'，'Interactive Dashboard'））<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2358 字、svg 12 个</sub><sub> 打开后所见：首页；“Live Demo” 是页面上的一个按钮</sub>

<sub>[编码与原文摘录](case-evidence.md#understand-anything)</sub>

#### [bpmn-js](https://github.com/bpmn-io/bpmn-js)

<sub>业务流程 · 一般图与网络 · 重点：先后与依赖方向、对象上的度量</sub>　在浏览器里查看、创建和编辑 BPMN 流程图

- 展示页（可直接操作）：[BPMN Editor \| bpmn-js modeler Demo \| demo.bpmn.io](https://demo.bpmn.io/)（页面文字 'Open or create a BPMN diagram.'，可直接打开或新建 BPMN 图；示例图上写着 'Click the diagram and continue modeling.'，点击图即可继续编辑）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 472 字、svg 8 个</sub>
- 网页：[bpmn-js: BPMN 2.0 rendering toolkit and web modeler \| Toolkits \| bpmn.io](https://bpmn.io/toolkit/bpmn-js/)（概述页，用 Model、Embed and Annotate、Extend 三节介绍 bpmn-js 的功能，并配有对应插图）
- 网页：[bpmn-js walkthrough \| Toolkits \| bpmn.io](https://bpmn.io/toolkit/bpmn-js/walkthrough/)（教程页，用 overview.svg（架构图）与 data-model.png（数据模型图）说明 bpmn-js 的组成部分）

<a href="https://bpmn.io/assets/img/model.png"><img src="https://bpmn.io/assets/img/model.png" width="230" alt="Model BPMN 2.0 diagrams"></a> <a href="https://bpmn.io/assets/img/embed.png"><img src="https://bpmn.io/assets/img/embed.png" width="230" alt="Embed BPMN 2.0 diagrams into the application"></a>

<sub>图：Model BPMN 2.0 diagrams（[来源页](https://bpmn.io/toolkit/bpmn-js/)）；Embed BPMN 2.0 diagrams into the application（[来源页](https://bpmn.io/toolkit/bpmn-js/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#bpmn-js)</sub>

#### [NeoDash](https://github.com/neo4j-labs/neodash)

<sub>图数据库应用 · 一般图与网络 · 重点：对象上的度量</sub>　用图数据库里的查询结果搭交互看板

- 展示页：没有找到在线展示页<sub>（示例看板站 neodash-gallery.graphapp.io 无头浏览器打开后页面写着 “The NeoDash sample gallery has been deprecated. Check the late…）</sub>
- 网页：[Untitled - Neo4j Labs](https://neo4j.com/labs/neodash/)（Neo4j Labs 上的 NeoDash 页面，页面中嵌有 alt 为 neodash 的图片（见 images）。）

<a href="https://neo4j.com/labs/neodash/_images/neodash.png"><img src="https://neo4j.com/labs/neodash/_images/neodash.png" width="230" alt="neodash"></a>

<sub>图：neodash（[来源页](https://neo4j.com/labs/neodash/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#neodash)</sub>

#### [Dify](https://dify.ai/)

<sub>AI Agent 开发 · 一般图与网络 · 重点：先后与依赖方向、对象上的度量</sub>　搭建 AI 工作流，并逐节点测试、检查数据怎么流过去

- 展示页（样例目录）：[Dify Marketplace](https://marketplace.dify.ai/templates)（页面顶部有 'Plugins' 与 'Templates' 两个标签，Templates 下列出模板卡片，每张带 'View' 按钮（如 'AI Business Analyst'、'Offer Arena'）；部分卡片标注 'Verified by a Dify partner'。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 31600 字、svg 1 个</sub>
- 网页：[Dify - The Platform for Production-Ready Agentic Workflows](https://dify.ai/)（官网首页，列出 Workflow Studio、Knowledge Pipeline 等产品模块，并附对应截图）
- 网页：[Single Node - Dify Docs](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)（单节点运行调试的文档页，内嵌节点运行输出相关截图（alt：'When You Run Nodes One at a Time, Their Outputs Are Cached in the Variable'））

<a href="https://dify.ai/_astro/workflow.Dl7EY_X1_rPiFq.webp"><img src="https://dify.ai/_astro/workflow.Dl7EY_X1_rPiFq.webp" width="230" alt="Dify Workflow Studio canvas showing connected nodes for an AI workflow."></a> <a href="https://dify.ai/_astro/knowledge.COlULHvU_Z1dyyjQ.webp"><img src="https://dify.ai/_astro/knowledge.COlULHvU_Z1dyyjQ.webp" width="230" alt="Dify Knowledge Pipeline turning documents into an indexed knowledge base."></a>

<sub>图：Dify Workflow Studio canvas showing connected nodes for an AI workflow.（[来源页](https://dify.ai/)）；Dify Knowledge Pipeline turning documents into an indexed knowledge base.（[来源页](https://dify.ai/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#dify)</sub>

#### [Langflow](https://www.langflow.org/)

<sub>AI Agent 开发 · 一般图与网络 · 重点：先后与依赖方向</sub>　用拖拽组件搭 AI 流程，并在 Playground 里实时测试

- 展示页（样例目录）：[Call Classification Analytics \| Langflow \| Low-code AI builder for agentic and RAG applications](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)（模板页列出流程组件（如 Prompt、Agent、Transcription Result Parser、Model Provider）和示例提示词；页面有 'Use for Free' 与 'Share' 按钮（未点击核对是否需要登录）。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 7401 字、svg 74 个</sub>
- 网页：[Test flows in the Playground \| Langflow Documentation](https://docs.langflow.org/concepts-playground)（Playground 功能页，说明可以实时测试基于 LLM 的流程的响应，页面内嵌 Playground 界面与 agent 回复的截图）
- 网页：[What is Langflow? \| Langflow Documentation](https://docs.langflow.org/)（官方文档首页，内嵌 Basic Prompting 流程的截图）

<a href="https://docs.langflow.org/assets/images/workspace-basic-prompting-c16e2f001725aa6dc1bc479f22aa11df.png"><img src="https://docs.langflow.org/assets/images/workspace-basic-prompting-c16e2f001725aa6dc1bc479f22aa11df.png" width="230" alt="Basic Prompting flow in Langflow"></a>

<sub>图：Basic Prompting flow in Langflow（[来源页](https://docs.langflow.org/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#langflow)</sub>

#### [n8n](https://github.com/n8n-io/n8n)

<sub>业务自动化 · 一般图与网络 · 重点：跨视图的同一对象、时间与演化</sub>　工作流在生产中失败后，把当时的执行数据带回编辑器里调试

- 展示页（样例目录）：[Discover 13200 Automation Workflows from the n8n's Community](https://n8n.io/workflows/)（页面列出社区工作流模板（标题写 'Discover 13200 Automation Workflows'），并有按分类浏览的入口：AI、Sales、IT Ops、Marketing、Document Ops、Support、Other。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 16182 字、svg 126 个</sub>
- 网页：[Debug executions \| Build \| n8n Docs](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)（文档页，主题为调试执行（Debug executions），属于 Understand executions 章节；静态 HTML 中可用图片只有图标，无功能截图）
- 网页：[View executions for a single workflow \| Build \| n8n Docs](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)（文档页，主题为查看单个工作流的执行记录；静态 HTML 中可用图片只有图标，无功能截图）

<sub>[编码与原文摘录](case-evidence.md#n8n)</sub>

#### [Node-RED](https://github.com/node-red/node-red)

<sub>物联网与事件流 · 一般图与网络 · 重点：连通与邻域、对象上的度量</sub>　把节点连起来搭事件驱动的流，并看消息在流里是什么样

- 展示页（样例目录）：[Library - Node-RED](https://flows.nodered.org/)（页面写着 'Find new nodes, share your flows and see what other people have done with Node-RED'，有 'Filter Nodes'、'Flows'、'Collections' 等入口，可浏览社区分享的 flows 与节点。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2367 字</sub>
- 网页：[Editor Guide : Node-RED](https://nodered.org/docs/user-guide/editor/)（编辑器指南，目录包括 Workspace、Flows、Nodes、Wires、Groups、Subflows 等章节，并附编辑器窗口截图）
- 网页：[Sidebar: Debug messages : Node-RED](https://nodered.org/docs/user-guide/editor/sidebar/debug)（调试消息侧边栏页，内嵌 Debug 侧边栏的截图）

<a href="https://nodered.org/docs/user-guide/editor/images/editor-default.png"><img src="https://nodered.org/docs/user-guide/editor/images/editor-default.png" width="230" alt="Editor window"></a>

<sub>图：Editor window（[来源页](https://nodered.org/docs/user-guide/editor/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#node-red)</sub>

#### [Flowise](https://flowiseai.com/)

<sub>AI Agent 开发 · 一般图与网络 · 重点：先后与依赖方向、时间与演化</sub>　可视化搭建带条件、循环、人工介入的多 Agent 流程

- 展示页：没有找到在线展示页<sub>（flowiseai.com 没有可打开的在线 demo 或 playground：'Get Started' 指向 cloud.flowiseai.com/signin，按地址判断需要登录，未打开核对…）</sub>
- 网页：[Agentflow V2 \| FlowiseAI](https://docs.flowiseai.com/using-flowise/agentflowv2)（Agentflow V2 功能文档，页面内嵌多张截图，其中一张为全部节点（文件名 v2-all-nodes））
- 网页：[Introduction \| FlowiseAI](https://docs.flowiseai.com/)（文档首页，内嵌一张介绍用的 GIF（FlowiseIntro.gif，未打开核对内容））

<a href="https://docs.flowiseai.com/~gitbook/image?url=https%3A%2F%2F823733684-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F00tYLwhz5RyR7fJEhrWy%252Fuploads%252FDOgMs2ywc1bdE09oa10c%252FFlowiseIntro.gif%3Falt%3Dmedia%26token%3D55bbcbc6-e586-4a79-8923-20c2b39e7bf9&width=768&dpr=3&quality=100&sign=ecfa638621ad32883f2cd872c1dec2cc&sv=3"><img src="https://docs.flowiseai.com/~gitbook/image?url=https%3A%2F%2F823733684-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F00tYLwhz5RyR7fJEhrWy%252Fuploads%252FDOgMs2ywc1bdE09oa10c%252FFlowiseIntro.gif%3Falt%3Dmedia%26token%3D55bbcbc6-e586-4a79-8923-20c2b39e7bf9&width=768&dpr=3&quality=100&sign=ecfa638621ad32883f2cd872c1dec2cc&sv=3" width="230" alt="flowise"></a> <a href="https://docs.flowiseai.com/~gitbook/image?url=https%3A%2F%2F823733684-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F00tYLwhz5RyR7fJEhrWy%252Fuploads%252Fgit-blob-c20ed065f28758e800bcdcc22531d70ca7df5547%252Fv2-all-nodes.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5eb56a7b24905589d49585b8414dc2d1&sv=3"><img src="https://docs.flowiseai.com/~gitbook/image?url=https%3A%2F%2F823733684-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F00tYLwhz5RyR7fJEhrWy%252Fuploads%252Fgit-blob-c20ed065f28758e800bcdcc22531d70ca7df5547%252Fv2-all-nodes.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5eb56a7b24905589d49585b8414dc2d1&sv=3" width="230" alt="flowise"></a>

<sub>[编码与原文摘录](case-evidence.md#flowise)</sub>

#### [LangGraph / Studio](https://docs.langchain.com/langsmith/studio)

<sub>AI Agent 开发 · 一般图与网络 · 重点：先后与依赖方向、时间与演化</sub>　调试 Agent 的状态：回到某个检查点重放，或分叉出另一条路径

- 展示页：没有找到在线展示页<sub>（未找到 LangGraph Studio 的官方公开 demo。WebSearch 也没有找到官方 live demo。）</sub>
- 网页：[LangSmith Studio - Docs by LangChain](https://docs.langchain.com/langsmith/studio)（页面介绍 Studio：'Studio is a specialized agent IDE that enables visualization, interaction, and debugging of agentic systems'，并说明 Graph mode 与 Chat mode。页面上没有截图。）
- 网页：[Use the graph API - Docs by LangChain](https://docs.langchain.com/oss/python/langgraph/use-graph-api)（页面有多张图结构示意图（并行执行、条件分支等，alt 为页面原文），并说明 'LangGraph provides built-in utilities for visualizing your graph'。）

<sub>[编码与原文摘录](case-evidence.md#langgraph)</sub>

#### [AutoGen / AutoGen Studio](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)

<sub>AI Agent 开发 · 一般图与网络 · 重点：先后与依赖方向、时间与演化</sub>　快速原型化 Agent 团队并观察它们的消息流

- 展示页：没有找到在线展示页<sub>（未找到官方托管的 AutoGen Studio 在线演示。页面说明它是研究原型（'not meant to be a production-ready app'）…）</sub>
- 网页：[AutoGen Studio — AutoGen](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)（官方用户指南，说明 AutoGen Studio 是低代码界面（'AutoGen Studio is a low-code interface built to help you rapidly prototype AI agents'），并列出可视化创建团队（JSON 或拖拽）和 Playground 等界面。页面上没有截图。）

<sub>[编码与原文摘录](case-evidence.md#autogen)</sub>

#### [Backstage](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)

<sub>软件工程 · 一般图与网络 · 重点：连通与邻域、关系上的类型与量</sub>　看清软件目录里的对象各自由谁拥有、依赖谁、提供什么 API

- 展示页（可直接操作）：[Backstage Demo](https://demo.backstage.io/catalog)<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2113 字、svg 129 个</sub><sub> 打开后所见：打开是 Backstage 的 Catalog 页：All Components（16 个），左侧可按 Kind、Type、Owner、Lifecycle 过滤，点组件进详情</sub>
- 网页：[Viewing entity relationships \| Backstage Software Catalog and Developer Platform](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)（说明在 Catalog 里点开组件名称后，页面中的 Relations 区域显示该实体与相关实体的关系）

<sub>[编码与原文摘录](case-evidence.md#backstage)</sub>

#### [Apache SkyWalking](https://skywalking.apache.org/)

<sub>分布式系统运维 · 一般图与网络 · 重点：连通与邻域、对象上的度量</sub>　从拓扑进入追踪、指标、日志，弄清运行系统的状况

- 展示页（需要登录）：[SkyWalking Horizon UI](https://demo.skywalking.apache.org/)（官网首页入口文字为 'Try the cloud-native Showcase'（入门页锚点 #qs-showcase））<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 343 字、svg 3 个</sub><sub> 打开后所见：打开是 “Welcome to SkyWalking”，要选 Continue with GitHub 或 Google</sub>
- 网页：[General Service \| Apache SkyWalking](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)（Horizon UI 仪表盘说明页，页面链接列出 Services Dashboard、Mesh Dashboard、AI Agent Overview 等仪表盘）

<sub>[编码与原文摘录](case-evidence.md#skywalking)</sub>

#### [Kiali](https://kiali.io/docs/features/topology/)

<sub>服务网格运维 · 一般图与网络 · 重点：连通与邻域、关系上的类型与量</sub>　看服务网格里的流量，快速发现 mTLS、延迟、错误问题

- 展示页：没有找到在线展示页<sub>（kiali.io 首页及拓扑、健康功能页没有链接到在线演示或 playground；功能页只链接到 Travel Demo 教程（需要自己安装到集群里），不算可直接打开的展示页）</sub>
- 网页：[Topology \| Kiali](https://kiali.io/docs/features/topology/)（Kiali 拓扑图功能页，页内有拓扑图、命名空间概览和侧边栏等截图）
- 网页：[Health \| Kiali](https://kiali.io/docs/features/health/)（Kiali 健康状态功能页，页内有健康概览、图上健康状态等截图）

<a href="https://kiali.io/images/documentation/features/topology-graph.png"><img src="https://kiali.io/images/documentation/features/topology-graph.png" width="230" alt="Topology graph"></a>

<sub>图：Topology graph（[来源页](https://kiali.io/docs/features/topology/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#kiali)</sub>

#### [diagrams.net / draw.io](https://www.drawio.com/)

<sub>通用绘图 · 一般图与网络 · 重点：连通与邻域</sub>　快速画出任意类型的图

- 展示页（可直接操作）：[Flowchart Maker & Online Diagram Software](https://app.diagrams.net/)（draw.io 功能页写明其 'free online diagram editor at app.diagrams.net'）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 566 字、svg 67 个</sub><sub> 打开后所见：打开是空白画布加左侧图形库（General、Misc、Advanced 等），可直接画图</sub>
- 网页：[Example technical diagrams \| draw.io](https://www.drawio.com/docs/diagram-types/)（按图类型列出示例图，页面示例图的 alt 包括 gitflow、C4 组件图、UML 类图、用例图、序列图、部署图等。）
- 网页：[An overview of draw.io's features \| draw.io](https://www.drawio.com/docs/features/)（功能概览页，写有可用 'Enter a text description and let an AI tool generate the diagram' 生成图表、可切换暗色模式（Diagram in dark mode），以及导入导出多种格式（Import and export many formats）等功能。）

<a href="https://www.drawio.com/img/blog/gitflow-example.png"><img src="https://www.drawio.com/img/blog/gitflow-example.png" width="230" alt="An example gitflow diagram"></a> <a href="https://www.drawio.com/img/blog/c4-component.png"><img src="https://www.drawio.com/img/blog/c4-component.png" width="230" alt="An example C4 component diagram"></a> <a href="https://www.drawio.com/img/blog/bpmn-example.png"><img src="https://www.drawio.com/img/blog/bpmn-example.png" width="230" alt="An example BPMN diagram"></a>

<sub>图：An example gitflow diagram（[来源页](https://www.drawio.com/docs/diagram-types/)）；An example C4 component diagram（[来源页](https://www.drawio.com/docs/diagram-types/)）；An example BPMN diagram（[来源页](https://www.drawio.com/docs/features/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#drawio)</sub>

#### [Kumu](https://kumu.io/)

<sub>系统与关系分析 · 一般图与网络 · 重点：连通与邻域、关系上的类型与量</sub>　把复杂的关系整理成地图，找出关键人物与关系

- 展示页（可直接操作）：[Hewlett Foundation Madison Initiative • Kumu](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative)<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 5899 字、canvas 24 个、svg 1 个</sub><sub> 打开后所见：打开是 “The Madison Initiative- 2016” 地图：左侧是文字说明，右侧是节点连线的关系图（节点按类型着色，图例在左下）</sub>
- 网页：[Tour](https://kumu.io/tour)（页面用截图和动图介绍 Kumu 的制作、筛选与装饰功能，正文如 'Create maps by hand, or import existing data.'、'Style your maps with data-driven decorations.'、'Discover insights through automated calculations.'）

<a href="https://assets.kumu.io/production/public/assets/marketing/screenshots/metrics-2b9a140553c4460249a36275da807a638254ef01618fed5d4d1dcf298000c856.jpg"><img src="https://assets.kumu.io/production/public/assets/marketing/screenshots/metrics-2b9a140553c4460249a36275da807a638254ef01618fed5d4d1dcf298000c856.jpg" width="230" alt="Metrics"></a> <a href="https://assets.kumu.io/production/public/assets/marketing/screenshots/reid-hoffman-profile-d2e1e480844bd8ab603b39615f520bf90282cd3b3a690207985891f2c12894f4.jpg"><img src="https://assets.kumu.io/production/public/assets/marketing/screenshots/reid-hoffman-profile-d2e1e480844bd8ab603b39615f520bf90282cd3b3a690207985891f2c12894f4.jpg" width="230" alt="Reid hoffman profile"></a>

<sub>图：Metrics（[来源页](https://kumu.io/tour)）；Reid hoffman profile（[来源页](https://kumu.io/tour)）</sub>

<sub>[编码与原文摘录](case-evidence.md#kumu)</sub>

#### [InfraNodus](https://infranodus.com/)

<sub>文本分析与知识发现 · 一般图与网络 · 重点：群落与相似、连通与邻域</sub>　在一大段文字里找出主要话题群和它们之间的结构空白

- 展示页（可直接操作）：[InfraNodus - hourlydailynews by live - Text Network Graph](https://infranodus.com/live/hourlydailynews?background=default&most_influential=bc&maxnodes=150&demo=1&defaultlabelsize=14&labelsizeratio=2&demo=1)（页面文字写明 'To change visibility, use the Filter menu above or select topics or nodes on the graph'（用上方 Filter 菜单，或点选图上的主题、节点来改变可见内容），顶部有 'visible graph / whole text / top graphs / all graphs' 切换，页面里有 'AI Text Tools' 面板）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1584 字、canvas 6 个、svg 63 个</sub><sub> 打开后所见：打开是 hourlydailynews 的文本网络图：按主题着色的词节点与连线，左侧是原文列表，下方有 AI Insights 面板</sub>
- 网页：[Create Your First Knowledge Graph from Any Text (No Code) - InfraNodus.Com](https://infranodus.com/tutorial/create-your-first-knowledge-graph)（教程页，说明把任意文字变成可交互的知识图谱，页面正文区分 'Topics View' 与 'Concepts View' 两个视图（页面文字：'1 Topics View 2 Concepts View'）。）
- 网页：[Text Network Analysis and Visualization — InfraNodus.Com](https://infranodus.com/use-case/text-network-analysis)（用例页，写有 'Represent your text as a network and apply advanced graph theory tools for topic modeling, classification, and structural gap detection.'，页面嵌有 Chinese Medicine、Google 搜索结果等文本网络图。）

<a href="https://infranodus.com/images/front/graph-visualization-popular-tweets.jpg"><img src="https://infranodus.com/images/front/graph-visualization-popular-tweets.jpg" width="230" alt="Graph visualization of the most popular tweets"></a> <a href="https://infranodus.com/images/front/graph-visualization-coronavirus-tweets.jpg"><img src="https://infranodus.com/images/front/graph-visualization-coronavirus-tweets.jpg" width="230" alt="Network Graph of the Tweets on Coronavirus"></a> <a href="https://infranodus.com/images/front/graph-chinese-medicine-tcm.jpg"><img src="https://infranodus.com/images/front/graph-chinese-medicine-tcm.jpg" width="230" alt="Mind Map of Chinese Medicine"></a>

<sub>图：Graph visualization of the most popular tweets（[来源页](https://infranodus.com/graphs)）；Network Graph of the Tweets on Coronavirus（[来源页](https://infranodus.com/graphs)）；Mind Map of Chinese Medicine（[来源页](https://infranodus.com/graphs)）</sub>

<sub>[编码与原文摘录](case-evidence.md#infranodus)</sub>

#### [Docling Graph](https://docling-project.github.io/docling-graph/)

<sub>文档处理 · 一般图与网络 · 重点：连通与邻域、关系上的类型与量</sub>　把文档变成带显式语义关系的知识图，用于需要精确实体连接的场合

- 展示页（可直接操作）：[Overview - Docling Graph Documentation](https://docling-project.github.io/docling-graph/usage/examples/)（示例总览页按输入格式（URL Input、Markdown Input、DoclingDocument Input）和领域（Billing Document、ID Card、Insurance Policy、Rheology Research）分类，并列出 Workflow 1: URL → Extract → Visualize。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 5323 字、svg 12 个</sub>
- 网页：[Visualization - Docling Graph Documentation](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)（讲交互式 HTML 可视化，页面列出 Zoom and pan 等功能，并给出 open outputs/visualization.html 的打开方法。）
- 网页：[Docling Graph Documentation](https://docling-project.github.io/docling-graph/)（项目首页，目录下有 What is Docling Graph? 的介绍。）

<sub>[编码与原文摘录](case-evidence.md#docling-graph)</sub>

#### [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)

<sub>文本检索与知识建模 · 一般图与网络 · 重点：群落与相似、包含与层次</sub>　回答关于整个语料库的整体性问题，以及关于具体实体的局部问题

- 展示页：没有找到在线展示页<sub>（官网与可视化指南中没有官方在线演示或 playground。WebSearch 只找到社区项目 graphrag-visualizer 与 graphrag-workbench，不是官方，也未找到可直接打开的托管页…）</sub>
- 网页：[Welcome - GraphRAG](https://microsoft.github.io/graphrag/)（官方首页，嵌有 Figure 1 知识图谱图，正文说明图中圆圈是实体、大小表示度数、颜色表示社区。）
- 网页：[Visualization Guide - GraphRAG](https://microsoft.github.io/graphrag/visualization_guide/)（可视化指南，讲如何把输出的 graph.graphml 导入 Gephi，页面含 Gephi 界面截图。）

<a href="https://microsoft.github.io/graphrag/img/GraphRag-Figure1.jpg"><img src="https://microsoft.github.io/graphrag/img/GraphRag-Figure1.jpg" width="230" alt="Figure 1: LLM-generated knowledge graph built from a private dataset using GPT-4 Turbo."></a> <a href="https://microsoft.github.io/graphrag/img/viz_guide/gephi-initial-graph-example.png"><img src="https://microsoft.github.io/graphrag/img/viz_guide/gephi-initial-graph-example.png" width="230" alt="A basic graph visualization by Gephi"></a>

<sub>图：Figure 1: An LLM-generated knowledge graph built using GPT-4 Turbo.（[来源页](https://microsoft.github.io/graphrag/)）；A basic graph visualization by Gephi（[来源页](https://microsoft.github.io/graphrag/visualization_guide/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#graphrag)</sub>

#### [LightRAG](https://github.com/HKUDS/LightRAG)

<sub>文本检索与知识建模 · 一般图与网络 · 重点：连通与邻域</sub>　用图结构配合向量做检索，并用网页看板查看知识

- 展示页：没有找到在线展示页<sub>（没有找到官方托管的在线演示。README 只链接了 YouTube 视频（https://www.youtube.com/watch?v=g21royNJ4fw，标为 video demo）；视频不是可直接操作的页面…）</sub>
- 网页：[lightrag-hku · PyPI](https://pypi.org/project/lightrag-hku/)（包的 PyPI 项目页，README 嵌有 LightRAG Diagram 与一张 iShot 截图，并介绍 LightRAG WebUI（2024.11 新功能）。）

<sub>[编码与原文摘录](case-evidence.md#lightrag)</sub>

#### [Graphiti](https://help.getzep.com/graphiti/getting-started/overview)

<sub>Agent 记忆 · 一般图与网络 · 重点：时间与演化、来源与证据</sub>　让 Agent 长期记得事实，并知道哪些事实现在不再成立

- 展示页（可直接操作）：[Playground \| Zep](https://app.getzep.com/playground)（Graphiti 概述页顶部导航有 Playground 入口，链接指向该地址。页面文字为 Pick example 和 This dataset doesn't have any graph data to visualize. Pick example，即先选示例数据再看图谱。打开时无需登录）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 6451 字、canvas 1 个、svg 41 个</sub>
- 网页：[Overview \| Zep Documentation](https://help.getzep.com/graphiti/getting-started/overview)（Graphiti 官方概述页，页内嵌有两张幻灯式动图（intro 与 demo slides））
- 网页：[Adding Episodes \| Zep Documentation](https://help.getzep.com/graphiti/core-concepts/adding-episodes)（核心概念页，标题为 Adding Episodes（添加 episode））

<sub>[编码与原文摘录](case-evidence.md#graphiti)</sub>

#### [伦敦地铁图（Beck）](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)

<sub>交通 · 一般图与网络 · 重点：连通与邻域、有什么</sub>　乘客要知道在哪条线、哪站换乘、几站到达，不需要知道地面上的真实距离

- 展示页：没有找到在线展示页<sub>（官方地铁图页 https://tfl.gov.uk/maps/tube 返回 403，读不到，无法确认是否有 TfL 在线交互地图）</sub>
- 网页：[How Harry Beck revolutionised the Tube map \| London Museum](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)（伦敦博物馆专题页，讲 Harry Beck 对地铁图的改画，页内有 1933 年地图图片）
- 网页：[Railway map \| London Museum](https://www.londonmuseum.org.uk/collections/v/object-536576/railway-map/)（馆藏记录 Railway map，专题页把它链接为 1935 map，页面有该地图的大图）

<a href="https://media.londonmuseum.org.uk/images/WagtailSource-Railway-map.width-1136.format-webp.webp"><img src="https://media.londonmuseum.org.uk/images/WagtailSource-Railway-map.width-1136.format-webp.webp" width="230" alt="1933 map of the london underground, showing colored lines and stations in a stylized layout, with th"></a>

<sub>图：1933 map of the london underground, showing colored lines and stations in a stylized layout, with th（[来源页](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#tube-map)</sub>

#### [SBGN 系统生物学图形标记](https://sbgn.github.io/specifications)

<sub>分子生物学通路 · 一般图与网络 · 重点：先后与依赖方向、关系上的类型与量</sub>　用统一的图形语言表示生物网络，并按想传达的信息选择详细程度

- 展示页（样例目录）：[Examples \| Systems Biology Graphical Notation](https://sbgn.github.io/examples)（示例页列出 MAPK、Glycolysis、Insulin signalling 等示例图；每个示例可下载 PNG，并有 Newt 链接（在 Newt 编辑器中打开 SBGN-ML 文件））<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 8078 字</sub>
- 网页：[Symbols \| Systems Biology Graphical Notation](https://sbgn.github.io/symbols)（符号页，按类别列出 SBGN 的符号（如 Stimulation、Inhibition、Process、Macromolecule），并附每个符号的示例图）
- 网页：[Learning SBGN \| Systems Biology Graphical Notation](https://sbgn.github.io/learning)（学习页，用葡萄糖被己糖激酶磷酸化等例子讲解 Process 符号，并介绍 SBGN Bricks 的示例图）

<a href="https://sbgn.github.io/images/examples/Sample-mapk-pd.png"><img src="https://sbgn.github.io/images/examples/Sample-mapk-pd.png" width="230" alt="MAPK-PD"></a> <a href="https://sbgn.github.io/images/examples/WWWglycolysis.png"><img src="https://sbgn.github.io/images/examples/WWWglycolysis.png" width="230" alt="Glycolysis.png"></a> <a href="https://sbgn.github.io/images/examples/WWWinsulin.png"><img src="https://sbgn.github.io/images/examples/WWWinsulin.png" width="230" alt="Insulin_signaling"></a>

<sub>图：MAPK-PD（[来源页](https://sbgn.github.io/examples)）；Glycolysis.png（[来源页](https://sbgn.github.io/examples)）；Insulin_signaling（[来源页](https://sbgn.github.io/examples)）</sub>

<sub>[编码与原文摘录](case-evidence.md#sbgn)</sub>

#### [ICIJ Offshore Leaks 数据库](https://offshoreleaks.icij.org/pages/howtouse)

<sub>调查报道与金融 · 一般图与网络 · 重点：连通与邻域、关系上的类型与量</sub>　查出离岸公司背后是谁，以及两个人之间有什么间接联系

- 展示页（可直接操作）：[ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/)（首页搜索框（页面示例：'British Virgin Islands \| Entity Name LLC \| Lima, Peru'）；'Explore the investigations' 可按 Pandora、Paradise、Panama、Bahamas、Offshore Leaks 调查浏览；how-to 页说明点击人名会出现连接关系的可视化）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 4058 字、svg 2 个</sub><sub> 打开后所见：先弹出使用声明，勾选同意并提交后才能搜索</sub>
- 网页：[How to use the Offshore Leaks Database \| ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/pages/howtouse)（使用指南，按例子说明搜索人名或公司、按国家和司法辖区筛选，以及点击节点查看关系图）

<sub>[编码与原文摘录](case-evidence.md#icij-offshore-leaks)</sub>

#### [VOWL / WebVOWL 本体可视化](https://semantic-web-journal.net/content/visualizing-ontologies-vowl-0)

<sub>本体与语义网 · 一般图与网络 · 重点：连通与邻域、关系上的类型与量</sub>　让不懂本体语言的人也能看懂本体

- 展示页：没有找到在线展示页<sub>（未找到可打开的官方 WebVOWL 在线版。已知地址 http://vowl.visualdataweb.org/webvowl.html 域名无法解析…）</sub>
- 网页：[Visualizing Ontologies with VOWL](https://semantic-web-journal.net/content/visualizing-ontologies-vowl-0)（期刊文章页，摘要说明 VOWL 用力导向图布局表示本体，并介绍了 ProtégéVOWL 与 WebVOWL 两种实现）
- 网页：[VOWL 2: User-Oriented Visualization of Ontologies](https://semantic-web-journal.net/content/vowl-2-user-oriented-visualization-ontologies)（期刊文章页，摘要说明 VOWL 2 的图形原语与抽象配色方案，并简述两种实现）

<sub>[编码与原文摘录](case-evidence.md#vowl)</sub>

#### [Hive Plot](https://mk.bcgsc.ca/linnet/)

<sub>网络分析（生物与社会网络） · 一般图与网络 · 重点：连通与邻域、对象上的度量</sub>　在大型网络里看出趋势和异常，并能比较相关的网络

- 展示页（可直接操作）：[Hive Plots](https://bost.ocks.org/mike/hive/)（页面正文写 'This hive plot, a type of node-link diagram, shows the dependency graph of the Flare visualization toolkit'，并提示 'Mouseover for more details'）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2832 字、svg 1 个</sub><sub> 打开后所见：打开能看到 Flare 依赖图的 hive plot（三条轴之间的弧线）</sub>
- 网页：[Hive Plots - Linear Layout for Network Visualization - Visually Interpreting Network Structure and Content Made Possible](https://mk.bcgsc.ca/linnet/)（hive plot 原作者 Martin Krzywinski 的主页，页面上有多张线性布局的网络图）

<a href="https://mk.bcgsc.ca/linnet/img/hiveplot-ecoli.png"><img src="https://mk.bcgsc.ca/linnet/img/hiveplot-ecoli.png" width="230" alt="E. coli gene regulatory network visualized with the linear layout."></a> <a href="https://mk.bcgsc.ca/linnet/img/hiveplot-linux.png"><img src="https://mk.bcgsc.ca/linnet/img/hiveplot-linux.png" width="230" alt="Linux kernel function call network visualized with the linear layout."></a>

<sub>图：E. coli gene regulatory network visualized with the linear layout.（[来源页](https://mk.bcgsc.ca/linnet/)）；Linux kernel function call network visualized with the linear layout.（[来源页](https://mk.bcgsc.ca/linnet/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#hive-plot)</sub>

#### [Gephi](https://gephi.org/desktop/)

<sub>通用网络分析 · 一般图与网络 · 重点：连通与邻域、群落与相似</sub>　探索网络、检验假设、发现复杂关系数据里的模式

- 展示页（可直接操作）：[Gephi Lite](https://lite.gephi.org/)（gephi.org/lite 页面的 “Open in your browser” 按钮指向此地址，该页写着 “Import graph data, run network ranking and layout algorithms, customize the graph appearance … No installation required.”）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 352 字、canvas 7 个、svg 33 个</sub><sub> 打开后所见：弹出欢迎窗口，可选 Les Miserables 等示例图</sub>
- 网页：[Gephi Desktop: Free Network Analysis and Visualization Software](https://gephi.org/desktop/)（Gephi 桌面版的官方功能页，带界面截图，图注有 “Drag and drop nodes”、“Highlight neighbors” 等操作示意）
- 网页：[Gephi Quickstart: Visualize and Analyze Your First Network](https://gephi.org/quickstart/)（官方入门教程，用 Les misérables 图等例子配步骤截图）

<a href="https://gephi.org/_astro/Gephi%20Desktop%20Screenshot%20DtB.DzXtydP5_1uXmvG.webp"><img src="https://gephi.org/_astro/Gephi%20Desktop%20Screenshot%20DtB.DzXtydP5_1uXmvG.webp" width="230" alt="gephi"></a> <a href="https://gephi.org/_astro/graph.C6hSDaRl_oWvg9.webp"><img src="https://gephi.org/_astro/graph.C6hSDaRl_oWvg9.webp" width="230" alt="Les misérables.gexf in the graph view"></a> <a href="https://gephi.org/_astro/layout_02.DQ0xO6Xg_Z1H0oyf.webp"><img src="https://gephi.org/_astro/layout_02.DQ0xO6Xg_Z1H0oyf.webp" width="230" alt="gephi"></a>

<sub>图：Visual user interface（[来源页](https://gephi.org/desktop/)）；Les misérables.gexf in the graph view（[来源页](https://gephi.org/quickstart/)）；Separate clusters（[来源页](https://gephi.org/desktop/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#gephi)</sub>

#### [设计结构矩阵 DSM](https://dsmweb.org/reading-a-dsm/)

<sub>工程系统与产品架构 · 一般图与网络 · 重点：先后与依赖方向、环与反馈</sub>　看清一个系统里元素之间的依赖，决定怎样分组与排序（团队、模块、先后）

- 展示页：没有找到在线展示页<sub>（dsmweb.org 的 DSM 工具页（https://dsmweb.org/dsm-tools/）列出的研究工具与商业工具中未找到在线演示入口…）</sub>
- 网页：[Reading a DSM – The Dependency and Structure Modeling (DSM) Web](https://dsmweb.org/reading-a-dsm/)（讲怎样读 DSM 矩阵（行、列与标记的含义），配有六元素 DSM 示意图）
- 网页：[Different DSM Types – The Dependency and Structure Modeling (DSM) Web](https://dsmweb.org/different-dsm-types/)（讲 DSM 的几种类型与各自的元素和关系，含多张矩阵示例图）

<a href="https://dsmweb.org/wp-content/uploads/2019/04/readingadms_bild1.png"><img src="https://dsmweb.org/wp-content/uploads/2019/04/readingadms_bild1.png" width="230" alt="dsm"></a> <a href="https://dsmweb.org/wp-content/uploads/2019/02/rtemagicc_bild13.png.png"><img src="https://dsmweb.org/wp-content/uploads/2019/02/rtemagicc_bild13.png.png" width="230" alt="dsm"></a> <a href="https://dsmweb.org/wp-content/uploads/2019/02/rtemagicc_bild14.png.png"><img src="https://dsmweb.org/wp-content/uploads/2019/02/rtemagicc_bild14.png.png" width="230" alt="dsm"></a>

<sub>[编码与原文摘录](case-evidence.md#dsm)</sub>

#### [Luhmann 的卡片盒](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)

<sub>知识管理与写作 · 一般图与网络 · 重点：连通与邻域、跨视图的同一对象</sub>　让积累的笔记自己产生不显而易见的联想（“卡片盒为什么能发展出自己的创造力”）

- 展示页：没有找到在线展示页<sub>（Luhmann-Archiv 相关页面（首页、教程页 /bestand/zettelkasten/tutorial、检索页 /bestand/zettelkasten/suche、/nachlass/zettelkast…）</sub>

<sub>[编码与原文摘录](case-evidence.md#zettelkasten)</sub>

#### [Git.Top Atlas](https://git.top/atlas)

<sub>开源生态导航 · 一般图与网络 · 重点：连通与邻域、对象上的度量</sub>　从一个生态（如 Cloudflare、MCP、RAG）进入，看里面的项目、替代方案、依赖和评分，做取舍

- 展示页（可直接操作）：[Git.Top Atlas \| Open Source Ecosystem Map](https://git.top/atlas)（页面标注「Atlas Beta」「Open-source ecosystems as a map」，按生态列出地图卡片（Cloudflare、AI Agent、MCP、RAG、Browser AI、AI IDE、LLM Gateway、AI Observability、Workflow Automation 等），每张卡上有 Map、Open Projects、Graph 入口，页面显示「1216 projects loaded」。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 36091 字</sub><sub> 打开后所见：打开是 “Open-source ecosystems as a map”：一排生态标签（Cloudflare、Agents、MCP、RAG 等）和每个生态一张带小关系图的卡片</sub>
- 网页：[AI Agent Ecosystem \| Git.Top Atlas](https://git.top/atlas/agents)（一个生态地图的具体页面（AI Agent Ecosystem），列出该生态的代表项目和 Projects / Graph 等入口。）
- 网页：[Atlas Guide \| Git.Top](https://git.top/topics/atlas-guide)（Atlas 使用指南，「How Atlas Works」一节说明从生态出发、查看代表项目、再到相关项目、比较、评分与搜索路径的流程。）

<sub>[编码与原文摘录](case-evidence.md#git-top-atlas)</sub>

#### [SemRepo](https://arxiv.org/abs/2605.13310)

<sub>研究软件知识图谱 · 一般图与网络 · 重点：连通与邻域、关系上的类型与量</sub>　把研究软件和论文、作者连起来，回答哪些论文对应的仓库仍在维护、被广泛复用、背后是哪些研究者

- 展示页（可直接操作）：[OpenLink Virtuoso SPARQL Query Editor](https://semrepo.org/sparql)（页面是 SPARQL 查询编辑器：Query Text 框里预填了 select distinct ?Concept where {[] a ?Concept} LIMIT 100，下方是 Result 结果区。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 684 字</sub><sub> 打开后所见：打开是 OpenLink Virtuoso 的 SPARQL 查询编辑器，预填了一条查询，点 Execute Query 才有结果；页面本身没有图</sub>
- 网页：[Ontology – SemRepo.org](https://semrepo.org/index.php/ontology/)（页面给出知识图谱的 schema 图（可点击放大），并附 OWL 本体、VoID、DCAT 描述文件的链接。）
- 网页：[SemRepo: Knowledge Graph for Research Software - ScaDS.AI](https://scads.ai/semrepo-knowledge-graph-for-research-software/)（项目说明页，写明图谱含超过 8100 万个 RDF 三元组、描述近 20 万个研究相关 GitHub 仓库，并把仓库与论文、研究者、机构、数据集、实验相连。）

<sub>[编码与原文摘录](case-evidence.md#semrepo)</sub>

#### [MOSS（研究软件知识图谱）](https://pretalx.com/juliacon-2025/talk/3EVLR9/)

<sub>研究软件知识图谱 · 一般图与网络 · 重点：连通与邻域</sub>　把 Julia 生态里的仓库、贡献者、论文、机构连成属性图，看谁贡献了什么、哪些包被哪些论文引用

- 展示页：没有找到在线展示页<sub>（known 的 https://opensource.science/moss 与 https://www.opensource.science/moss 都返回 404…）</sub>
- 网页：[Mapping the Julia Subsystem in Open Science: Use, Impact, Growth :: JuliaCon 2025 :: pretalx](https://pretalx.com/juliacon-2025/talk/3EVLR9/)（JuliaCon 2025 演讲摘要，介绍 MOSS 的数据来源（GitHub、OpenAlex、CrossRef 等）和知识图谱的节点类型（Repository、Paper、Person、Institution、Topic）。）

<sub>[编码与原文摘录](case-evidence.md#moss)</sub>

#### [Ecosyste.ms](https://packages.ecosyste.ms/)

<sub>开源数据基础设施 · 一般图与网络 · 重点：连通与邻域</sub>　为开源项目提供跨托管平台的包、仓库、依赖、提交、Issue 数据的开放 API，支撑生态研究与维护

- 展示页（可直接操作）：[Ecosyste.ms: Packages](https://packages.ecosyste.ms/)（官方的包服务首页，显示各注册表的包、版本、维护者等统计数字）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 6538 字、svg 4 个</sub><sub> 打开后所见：打开是 Ecosyste.ms: Packages 的统计页：各注册表的包、版本、维护者数量，没有可操作的图</sub>
- 网页：[Swagger UI](https://packages.ecosyste.ms/docs/index.html)（官方 API 文档页（Swagger UI），可看到 Packages 服务提供的接口形式；页面正文由脚本渲染，文字里只读到标题。）

<sub>[编码与原文摘录](case-evidence.md#ecosystems)</sub>

#### [OpenDigger](https://open-digger.cn/en/)

<sub>开源活动指标 · 一般图与网络 · 重点：对象上的度量、时间与演化</sub>　用统一的指标（活跃度、OpenRank 等）度量开源项目和开发者的活动与影响力随时间的变化

- 展示页（可直接操作）：[Playground \| OpenDigger](https://open-digger.cn/en/docs/user-docs/metrics/playground)（页面写明：可以在 playground 页输入平台、仓库名或用户登录名，查看数据的可视化效果。页面上有三个 'Select...' 选择框、一个 'Search for a name...' 搜索框和 'Submit' 按钮。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 659 字、canvas 1 个、svg 13 个</sub><sub> 打开后所见：打开是 Playground：选平台和类型、输入名字，提交后出柱线图（示例页是 X-lab2017/open-digger 的 Issue 指标）</sub>
- 网页：[OpenRank Algorithm \| OpenDigger](https://open-digger.cn/en/docs/user-docs/metrics/openrank)（OpenRank 算法说明页（标题 'OpenRank Algorithm'），页内有一张 PageRank 示意图。）
- 网页：[OpenDigger \| OpenDigger](https://open-digger.cn/en/)（官网首页，文字介绍 OpenDigger 是开源分析平台，实现了 CHAOSS 社区的多种指标。）

<sub>[编码与原文摘录](case-evidence.md#opendigger)</sub>

#### [deps.dev（Open Source Insights）](https://docs.deps.dev/)

<sub>软件供应链 · 一般图与网络 · 重点：连通与邻域、对象上的度量</sub>　弄清一个包的完整依赖图、版本、许可证和安全公告，评估引入它会带来多大风险

- 展示页（可直接操作）：[Open Source Insights](https://deps.dev/)（页面正文由脚本渲染，读到的页面文字只有标题 'Open Source Insights'，未能从页面文字确认具体可操作的位置。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 3358 字</sub><sub> 打开后所见：打开是 Open Source Insights 首页：一个搜索框，右侧列出各包管理生态的包数量</sub>
- 网页：[Announcing the deps.dev API \| Open Source Insights](https://blog.deps.dev/api/)（deps.dev API 发布文章，配有两张依赖图：理想与实际依赖图的对比，以及 react 15.0.0 的依赖图（用 GraphViz 渲染）。）
- 网页：[Documentation \| Open Source Insights](https://docs.deps.dev/)（官方文档首页，文字说明 Open Source Insights 是 Google 开发和托管的服务，帮助开发者理解开源软件包的结构、构建和安全（页面无配图）。）

<a href="https://blog.deps.dev/img/2023-04-11-api/dependency-graph-react.png"><img src="https://blog.deps.dev/img/2023-04-11-api/dependency-graph-react.png" width="230" alt="Dependency graph for react 15.0.0, fetched from the deps.dev API and rendered using GraphViz"></a>

<sub>图：Dependency graph for react 15.0.0, fetched from the deps.dev API and rendered using GraphViz（[来源页](https://blog.deps.dev/api/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#deps-dev)</sub>

#### [CodeGraph（面向源代码的开放分类知识图谱）](https://arxiv.org/abs/2609.29474)

<sub>代码知识图谱 · 一般图与网络 · 重点：连通与邻域、包含与层次</sub>　用代码本身而不是标签，找到实现某个算法、遵循某种范式、属于某个应用领域的文件，并看同一算法跨领域的复用

- 展示页（样例目录）：[halykoss/CodeGraph · Datasets at Hugging Face](https://huggingface.co/datasets/halykoss/CodeGraph/viewer/)（数据集页上的 Data Studio 标签指向本页；页面文字列出 15 个子集（Subset (15) files · 145M rows），如 concepts_algorithm_categories (268k rows)，可逐行浏览数据）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 9407 字、svg 104 个</sub>
- 网页：[CodeGraph: Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding](https://arxiv.org/html/2609.29474v1)（论文 HTML 版，含方法流程图（图 1）和跨领域复用热图（图 10））
- 网页：[halykoss/CodeGraph · Datasets at Hugging Face](https://huggingface.co/datasets/halykoss/CodeGraph)（数据集卡片页，列出数据子集并链接到 Data Studio 浏览页）

<a href="https://arxiv.org/html/2609.29474v1/algorithm_transfer_heatmap.png"><img src="https://arxiv.org/html/2609.29474v1/algorithm_transfer_heatmap.png" width="230" alt="Refer to caption"></a>

<sub>图：Figure 10. Cross-domain reuse of computational techniques. Incidence of selected algorithms across representative application domains, illustrating the recurrence of shared techniques across substantively different domains.（[来源页](https://arxiv.org/html/2609.29474v1)）</sub>

<sub>[编码与原文摘录](case-evidence.md#codegraph)</sub>

<!-- /gen -->

## 层级与树

<!-- gen:gallery:hierarchy -->
#### [CodeBoarding](https://codeboarding.org/)

<sub>软件工程 · 层级与树 · 重点：包含与层次、连通与邻域</sub>　合并之前看清一个 PR 改了系统的哪些部分、影响哪里

- 展示页（可直接操作）：[CodeBoarding/CodeBoarding · CodeBoarding](https://app.codeboarding.org/CodeBoarding/CodeBoarding)（官方首页 “Open a live example” 指向的是一个 PR 分析页，那页写着 “PR #586 has no analysis yet”；这里改用同站的公开架构图页（页面写 “Or browse public maps, no account needed”）：5 个组件的架构图，点组件的 + 号展开，另有 Pull requests、Health、History 标签）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2217 字、svg 52 个</sub>
- 网页：[CodeBoarding](https://codeboarding.org/diagrams)（首页 'Example diagrams' 链接指向的页面，页面文字列出已分析的仓库，并有 'Architecture Summary' 与 'Select a component in the diagram to view details.' 等图示界面文字）
- 网页：[CodeBoarding, review the change, not the diff](https://codeboarding.org/)（官方首页，带有 PR 审查示意图（review-stage、review-map、action-comment 等图片））

<a href="https://codeboarding.org/images/website/review-stage-light.png"><img src="https://codeboarding.org/images/website/review-stage-light.png" width="230" alt="A pull request reviewed as a system diagram with changed components and the diff beside it"></a> <a href="https://codeboarding.org/images/website/review-map-light.png"><img src="https://codeboarding.org/images/website/review-map-light.png" width="230" alt="Detail of the CodeBoarding change diagram, with changed components and their dependencies"></a> <a href="https://codeboarding.org/_next/image?url=%2Fimages%2Fwebsite%2Faction-comment-light.svg&w=1920&q=75"><img src="https://codeboarding.org/_next/image?url=%2Fimages%2Fwebsite%2Faction-comment-light.svg&w=1920&q=75" width="230" alt="Mermaid architecture diagram with Identity and Payments modified and a new dependency between them"></a>

<sub>图：A pull request reviewed as a system diagram with changed components and the diff beside it（[来源页](https://codeboarding.org/)）；Detail of the CodeBoarding change diagram, with changed components and their dependencies（[来源页](https://codeboarding.org/)）；Mermaid architecture diagram with Identity and Payments modified and a new dependency between them（[来源页](https://codeboarding.org/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#codeboarding)</sub>

#### [LikeC4](https://likec4.dev/)

<sub>软件工程 · 层级与树 · 重点：包含与层次、连通与邻域</sub>　用同一份架构模型，向不同的人展示不同范围、不同层级的图

- 展示页（可直接操作）：[LikeC4 Playground](https://playground.likec4.dev/w/bigbank/)（在 Big Bank 示例页的 'Try it online' 一节，点击 'LikeC4 playground'（页面原文：Preview and play with this example in the LikeC4 playground）打开同一示例）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2201 字、canvas 3 个、svg 52 个</sub>
- 网页：[Big Bank Example \| LikeC4](https://likec4.dev/showcases/bigbank/)（同一个 Big Bank 示例，页面对照 LikeC4 与 Structurizr 的写法，并配有 System Landscape、System Context、Containers 的渲染图）

<sub>[编码与原文摘录](case-evidence.md#likec4)</sub>

#### [AgentPrism](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)

<sub>AI Agent 观测 · 层级与树 · 重点：包含与层次、时间与演化</sub>　调试 Agent 运行，看时间和成本浪费在哪

- 展示页（可直接操作）：[AgentPrism - AI Observability Platform](https://agent-prism.evilmartians.io/)（首页显示一条示例 trace 的 span 树（页面文字中有 ChatCompletion、AgentExecutor、anonymized_search 等条目），页面写着 'Select a span to see the details'，点选 span 即可看详情）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2604 字、svg 67 个</sub>
- 网页：[Debug AI fast with this open source library to visualize agent traces—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)（博文配有 Tree View 与 Timeline 组件、Span Details 的截图，说明 AgentPrism 的界面（图见 images））

<a href="https://evilmartians.com/static/3c7e8a7abf1e378396cba6bc7e7447da/tree-view.png"><img src="https://evilmartians.com/static/3c7e8a7abf1e378396cba6bc7e7447da/tree-view.png" width="230" alt="Tree View and Timeline View Component"></a> <a href="https://evilmartians.com/static/ab1d0e50075794e438463803b1bb3008/quotient-demo.png"><img src="https://evilmartians.com/static/ab1d0e50075794e438463803b1bb3008/quotient-demo.png" width="230" alt="A demo of AgentPrism"></a>

<sub>图：Tree View on the left, Timeline on the right（[来源页](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)）；A demo of AgentPrism（[来源页](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)）</sub>

<sub>[编码与原文摘录](case-evidence.md#agentprism)</sub>

#### [Jaeger](https://github.com/jaegertracing/jaeger)

<sub>分布式系统运维 · 层级与树 · 重点：时间与演化、包含与层次</sub>　找出一次请求流经了哪些服务，性能瓶颈和错误在哪

- 展示页（可直接操作）：[Jaeger UI](https://demo.jaegertracing.io/jaeger/)（jaegertracing.io/demo/ 的 'Live Demo' 一节写明 Jaeger Live Demo 由 HotROD 应用和 Jaeger UI 组成，Jaeger UI 的地址是 https://demo.jaegertracing.io/jaeger/，即此处的 demo 地址。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 211 字、svg 13 个</sub><sub> 打开后所见：打开是搜索页，要先在左侧选一个服务（Service）才能查 trace</sub>
- 网页：[Frontend/UI Configuration \| Jaeger](https://www.jaegertracing.io/docs/2.22/deployment/frontend-ui/)（2.22 文档说明 Jaeger UI 可配置的部分，如主题切换、Dependencies、Monitor 标签页和 critical path 可视化；页面为文字，没有截图。）
- 网页：[Live Demo \| Jaeger](https://www.jaegertracing.io/demo/)（官方 Live Demo 页，列出可直接打开的 HotROD 应用和 Jaeger UI 地址。）

<sub>[编码与原文摘录](case-evidence.md#jaeger)</sub>

#### [Grafana Tempo](https://github.com/grafana/tempo)

<sub>分布式系统运维 · 层级与树 · 重点：连通与邻域、关系上的类型与量</sub>　理解分布式系统的结构，找出瓶颈和互联问题

- 展示页：没有找到在线展示页<sub>（在线展示页：play.grafana.org 返回 200，但页面文字为 'Grafana is starting up... Error loading Grafana'，前端没有加载出来…）</sub>
- 网页：[Visualize tracing data in Grafana \| Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/visualize-traces/)（页面写明 Grafana 内置 Tempo 数据源，可以查询 Tempo 并可视化 trace。）
- 网页：[Service graphs \| Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/metrics-from-traces/service_graphs/)（页面介绍服务图（service graph），即各服务之间相互关系的可视化表示。）

<sub>[编码与原文摘录](case-evidence.md#grafana-tempo)</sub>

#### [AgentScope 2.0](https://docs.agentscope.io/)

<sub>AI Agent 开发 · 层级与树 · 重点：包含与层次、时间与演化</sub>　观察一个由领导者协调多个工作者的 Agent 团队怎么运作

- 展示页：没有找到在线展示页<sub>（未找到 AgentScope 2.0 的官方在线演示或 playground。WebSearch 也没有找到官方托管的 demo 地址。）</sub>
- 网页：[Agent Team - AgentScope](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)（页面用一张动图（alt 为 Agent team coordination demo）展示 leader agent 组队并协调 worker 的过程；图注取自页面正文：'A leader agent assembling a team and coordinating workers in the example web UI.'）
- 网页：[Console - AgentScope](https://docs.agentscope.io/en/versions/2.0.9/building-blocks/console)（页面说明可以在终端里与智能体对话并查看完整事件流（'you can chat with it and inspect its full event stream directly in the terminal'）；页面上没有截图。）

<a href="https://agentscope.io/images/agentscope2-ecosystem.svg"><img src="https://agentscope.io/images/agentscope2-ecosystem.svg" width="230" alt="AgentScope 2.0 ecosystem diagram"></a>

<sub>图：AgentScope 2.0 ecosystem diagram（[来源页](https://agentscope.io/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#agentscope)</sub>

#### [Langfuse](https://github.com/langfuse/langfuse)

<sub>AI 应用观测 · 层级与树 · 重点：时间与演化、对象上的度量</sub>　弄清应用内部发生了什么，并用评测持续改进

- 展示页（可直接操作）：[Example Project - Langfuse](https://langfuse.com/docs/demo)（页面 'Generate your first demo trace' 一节（页面文字：'Run a demo interaction below to generate real data.'）下方可直接操作，列出 Q&A Chatbot、Voice Agent、Image Generator、Sentiment Classifier、Rock Paper Scissors 等示例应用。生成 trace 后按 Step 02 'Find your trace in Langfuse' 查看。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 70 字、svg 1 个；内容很少，可能需要交互或登录</sub><sub> 打开后所见：无头浏览器里页面显示 “This page couldn’t load”，没看到内容（等 12 秒后仍如此，页面有脚本报错）</sub>
- 网页：[LLM Observability & Application Tracing (Open Source) - Langfuse](https://langfuse.com/docs/observability/overview)（页面配有 Langfuse UI 中 trace 的截图（嵌套 observation、耗时、输入输出和 metadata），能说明追踪功能的界面。）
- 网页：[Evaluation of LLM Applications - Langfuse](https://langfuse.com/docs/evaluation/overview)（页面配有 Score Analytics 仪表盘截图，展示评估分数随时间的变化。）

<a href="https://langfuse.com/_next/image?url=%2Fimages%2Fdocs%2Ftracing-overview.png&w=3840&q=85&dpl=dpl_rew97PyGrqkVtmb1L4Ag4QeXhcfN"><img src="https://langfuse.com/_next/image?url=%2Fimages%2Fdocs%2Ftracing-overview.png&w=3840&q=85&dpl=dpl_rew97PyGrqkVtmb1L4Ag4QeXhcfN" width="230" alt="Example of a trace in the Langfuse UI showing nested observations, timing, inputs, outputs, and meta"></a> <a href="https://langfuse.com/_next/image?url=%2Fimages%2Fdocs%2Fscore-analytics-full-dashboard.png&w=3840&q=85&dpl=dpl_rew97PyGrqkVtmb1L4Ag4QeXhcfN"><img src="https://langfuse.com/_next/image?url=%2Fimages%2Fdocs%2Fscore-analytics-full-dashboard.png&w=3840&q=85&dpl=dpl_rew97PyGrqkVtmb1L4Ag4QeXhcfN" width="230" alt="Score Analytics dashboard in Langfuse showing evaluation scores trended over time across multiple ev"></a>

<sub>图：Example of a trace in the Langfuse UI showing nested observations, timing, inputs, outputs, and meta（[来源页](https://langfuse.com/docs/observability/overview)）；Score Analytics dashboard in Langfuse showing evaluation scores trended over time across multiple ev（[来源页](https://langfuse.com/docs/evaluation/overview)）</sub>

<sub>[编码与原文摘录](case-evidence.md#langfuse)</sub>

#### [Arize Phoenix](https://github.com/Arize-ai/phoenix)

<sub>AI 应用观测 · 层级与树 · 重点：包含与层次、时间与演化</sub>　一步步看一次 AI 应用运行，调试行为并衡量输出质量

- 展示页（可直接操作）：[Phoenix](https://phoenix-demo.arize.com/)<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 527 字、svg 27 个</sub><sub> 打开后所见：打开是 Phoenix 的项目列表（demo_agents、demo_llama_index、default），左侧有 Tracing、Datasets & Experiments、Playground 等入口；三个项目卡片上的 Traces 都显示 0，需点进项目看</sub>
- 网页：[Overview: Tracing - Phoenix](https://arize.com/docs/phoenix/tracing/llm-traces)（追踪功能页，嵌有一张没有 alt 和说明文字的图片。）
- 网页：[Evaluation - Phoenix](https://arize.com/docs/phoenix/evaluation/llm-evals)（评估功能页，嵌有 evaluator trace 与 evaluator traces page 两张带 alt 的图片。）

<a href="https://storage.googleapis.com/arize-phoenix-assets/assets/images/phoenix-docs-images/15fe0366-image.jpeg"><img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/phoenix-docs-images/15fe0366-image.jpeg" width="230" alt="arize-phoenix"></a>

<sub>[编码与原文摘录](case-evidence.md#arize-phoenix)</sub>

#### [Comet Opik](https://www.comet.com/site/products/opik/)

<sub>AI 应用观测 · 层级与树 · 重点：包含与层次、时间与演化</sub>　弄清 Agent 为什么失败、哪个 span 引起延迟

- 展示页：没有找到在线展示页<sub>（未找到无需注册即可打开的在线展示页。产品页的 Try Opik Free 指向注册页 https://www.comet.com/signup?from=llm，Get Demo 指向联系页，都不算展示页…）</sub>
- 网页：[Open-Source AI Observability Platform \| Opik by Comet](https://www.comet.com/site/products/opik/)（产品页，页面文字列出 LLM Observability & Evaluation、Experiment Management 等模块，并嵌有多张功能图片。）
- 网页：[Debugging Agents with Ollie \| Opik Documentation](https://www.comet.com/docs/opik/tracing/debug-agents)（文档页，嵌有三张带 alt 的图片，alt 分别是 Ollie analyzing a trace and identifying the root cause、Ollie proposing a code fix with a diff view、Ollie running a test suite and showing pass/fail results。）

<a href="https://www.comet.com/site/wp-content/uploads/2026/05/opik-llm-tracing.png"><img src="https://www.comet.com/site/wp-content/uploads/2026/05/opik-llm-tracing.png" width="230" alt="comet-opik"></a> <a href="https://www.comet.com/docs/opik/_fern-img/fe85b7f2855f7e02aa74fdccae736d557b71806abc45560e8b9dcffcf9c478b7.webp"><img src="https://www.comet.com/docs/opik/_fern-img/fe85b7f2855f7e02aa74fdccae736d557b71806abc45560e8b9dcffcf9c478b7.webp" width="230" alt="comet-opik"></a>

<sub>[编码与原文摘录](case-evidence.md#comet-opik)</sub>

#### [AgentOps](https://www.agentops.ai/)

<sub>AI 应用观测 · 层级与树 · 重点：时间与演化、包含与层次</sub>　在会话的时间线上看 LLM 调用、工具调用和错误，并回放

- 展示页：没有找到在线展示页<sub>（未找到无需登录的在线展示页。主页的 Dashboard 按钮指向 https://app.agentops.ai/，这是账号控制台，未访问，不计为展示页。搜索也未找到公开演示。）</sub>
- 网页：[Introduction - AgentOps](https://docs.agentops.ai/v2/introduction)（介绍页，嵌有 overview 截图以及 session-waterfall、session-drawer 两张动图，图片没有 alt 和说明文字。）

<a href="https://mintcdn.com/agentops/lKHoIAF-8UF9BP18/images/overview.png?fit=max&auto=format&n=lKHoIAF-8UF9BP18&q=85&s=7eaf05b550f66df6c3ea493035a827b3"><img src="https://mintcdn.com/agentops/lKHoIAF-8UF9BP18/images/overview.png?fit=max&auto=format&n=lKHoIAF-8UF9BP18&q=85&s=7eaf05b550f66df6c3ea493035a827b3" width="230" alt="agentops"></a> <a href="https://mintcdn.com/agentops/lKHoIAF-8UF9BP18/images/session-waterfall.gif?s=dc65c7b9a11e84ba14105811b1eaa1e5"><img src="https://mintcdn.com/agentops/lKHoIAF-8UF9BP18/images/session-waterfall.gif?s=dc65c7b9a11e84ba14105811b1eaa1e5" width="230" alt="agentops"></a>

<sub>[编码与原文摘录](case-evidence.md#agentops)</sub>

#### [LangWatch](https://langwatch.ai/)

<sub>AI 应用观测 · 层级与树 · 重点：时间与演化、连通与邻域</sub>　找出一次运行的瓶颈，并看全局的成本、延迟与话题分布

- 展示页（需要登录）：[LangWatch](https://app.langwatch.ai/demo)<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 335 字、canvas 1 个、svg 7 个</sub><sub> 打开后所见：打开后跳转到登录页（/auth/signin?callbackUrl=/demo）</sub>
- 网页：[Observability & Tracing](https://langwatch.ai/docs/observability/overview.md)（可观测性概览页，页面文字说明接入 SDK 后可在仪表盘实时查看调用，并可点入 trace 调试；嵌有 Observability Dashboard 图。）

<sub>[编码与原文摘录](case-evidence.md#langwatch)</sub>

#### [AFFiNE](https://affine.pro/)

<sub>知识管理 · 层级与树 · 重点：跨视图的同一对象</sub>　同一批内容既要线性地写，又要空间化地摆

- 展示页（样例目录）：[Free Templates for Notes, Planning & Whiteboards \| AFFiNE](https://affine.pro/templates)（页面是模板目录，列出多个模板的链接（如 'Free Blank Checklist Template with a Filled Example'、'Case Brief Example: Facts, Issues, Holding, Reasoning'），每条指向单独的模板页；未逐个打开模板页核对。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 18918 字、svg 40 个</sub>
- 网页：[Online Whiteboard for Brainstorming and Planning \| AFFiNE](https://affine.pro/whiteboard)（页面围绕在线白板（Edgeless 画布），正文有 'Draw, Plan, and Share Ideas Seamlessly'、'Endless Possibilities with the Edgeless Canvas' 等句子，并列出 Monthly Weekly Planner、Cornell Notes Template、Habit Tracker 等白板模板。）
- 网页：[Collaborative Docs for Notes and Structured Writing \| AFFiNE](https://affine.pro/pagedoc)（页面围绕 Page Docs 文档编辑，正文标题为 'Beyond Text: Build Rich, Interactive Documents'，列出 Blocks、Table、PDF Preview、Image & Videos 等内容块。）

<sub>[编码与原文摘录](case-evidence.md#affine)</sub>

#### [Tree-sitter](https://github.com/tree-sitter/tree-sitter)

<sub>软件工程 · 层级与树 · 重点：包含与层次</sub>　把源码解析成语法树，并随编辑增量更新

- 展示页（可直接操作）：[Playground - Tree-sitter](https://tree-sitter.github.io/tree-sitter/7-playground.html)（页面 About 段写明可用预选语法试用；Code 区可选 JavaScript、Python、Rust 等语言编辑代码，Tree 面板显示语法树，代码改动时树实时更新，点击树中节点可选中对应代码；Query 面板可输入查询模式，有效时捕获结果在 Code 与 Query 中高亮。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1738 字、svg 14 个</sub>
- 网页：[Basic Parsing - Tree-sitter](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)（官方教程页，标题为 Basic Parsing，讲解解析代码的基本步骤，页面有 Providing the Code 一节。）
- 网页：[Introduction - Tree-sitter](https://tree-sitter.github.io/tree-sitter/)（官网首页，首段说明 Tree-sitter 是解析器生成工具和增量解析库。）

<sub>[编码与原文摘录](case-evidence.md#tree-sitter)</sub>

#### [Docling](https://github.com/docling-project/docling)

<sub>文档处理 · 层级与树 · 重点：包含与层次、来源与证据</sub>　把 PDF 等文档转成保留版面和阅读顺序的统一结构

- 展示页（可直接操作）：[SmolDocling - a Hugging Face Space by docling-project](https://huggingface.co/spaces/docling-project/SmolDocling-256M-Demo)<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 108 字、svg 16 个</sub><sub> 打开后所见：打开是 SmolDocling-256M 的 Hugging Face Space：一个聊天框加几个示例提示（Convert this page to docling 等），要上传图片才能转换</sub>
- 网页：[Architecture - Docling](https://docling-project.github.io/docling/concepts/architecture/)（页面标题为 Architecture，并嵌有架构图 docling_arch.png。）
- 网页：[Docling document - Docling](https://docling-project.github.io/docling/concepts/docling_document/)（概念页，标题为 Docling document，嵌有两张文档层级图。）

<sub>[编码与原文摘录](case-evidence.md#docling)</sub>

#### [Nextstrain / Auspice](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)

<sub>流行病与基因组 · 层级与树 · 重点：跨视图的同一对象、时间与演化</sub>　同时看病原体的系统发生关系、地理传播和时间

- 展示页（可直接操作）：[auspice](https://nextstrain.org/ncov/open/global/6m)（nextstrain.org 首页 Core pathogens 区（页面文字：Continually updated views of a range of pathogens maintained by the Nextstrain）下的 SARS-CoV-2 链接指向该地址，即 Auspice 实时视图）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 31191 字、canvas 1 个、svg 60 个</sub>
- 网页：[Interacting with Nextstrain’s phylogeographic visualisations — Nextstrain documentation](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)（官方文档，讲怎样与 Nextstrain 的系统发育地理可视化互动，页内有 mumps 视图截图）
- 网页：[Auspice: An Open-source Interactive Tool for Visualising Phylogenomic Data — Auspice documentation](https://docs.nextstrain.org/projects/auspice/en/stable/)（Auspice 官方文档首页，页内嵌有 Auspice v2 饼图的动图）

<a href="https://docs.nextstrain.org/en/latest/_images/mumps.png"><img src="https://docs.nextstrain.org/en/latest/_images/mumps.png" width="230" alt="mumps"></a> <a href="https://docs.nextstrain.org/projects/auspice/en/stable/_images/v2-pie-charts.gif"><img src="https://docs.nextstrain.org/projects/auspice/en/stable/_images/v2-pie-charts.gif" width="230" alt="_images/v2-pie-charts.gif"></a>

<sub>图：mumps（[来源页](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)）；_images/v2-pie-charts.gif（[来源页](https://docs.nextstrain.org/projects/auspice/en/stable/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#nextstrain)</sub>

#### [OneZoom 生命之树](https://www.onezoom.org/introduction)

<sub>生物分类 · 层级与树 · 重点：包含与层次、对象上的度量</sub>　在上百万物种的进化树里自由探索，不被规模压垮

- 展示页（可直接操作）：[OneZoom web software Tree of Life Explorer](https://www.onezoom.org/)（首页即生命树浏览器。页面导航文字有 A view of all known life（全部已知生命的视图）和 Your name on the tree）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 5940 字、canvas 1 个、svg 9 个</sub><sub> 打开后所见：先弹出 cookie 窗口，后面是生命树</sub>
- 网页：[About OneZoom web software](https://www.onezoom.org/introduction)（官方介绍页，说明 OneZoom 网页软件）
- 网页：[OneZoom web software: Full user guide](https://www.onezoom.org/full_guide)（完整用户指南，标题为 Full user guide，适合查看界面操作说明）

<a href="https://journals.plos.org/plosbiology/article/figure/image?size=inline&id=10.1371/journal.pbio.1001406.g002"><img src="https://journals.plos.org/plosbiology/article/figure/image?size=inline&id=10.1371/journal.pbio.1001406.g002" width="230" alt="Figure 2"></a> <a href="https://journals.plos.org/plosbiology/article/figure/image?size=inline&id=10.1371/journal.pbio.1001406.g003"><img src="https://journals.plos.org/plosbiology/article/figure/image?size=inline&id=10.1371/journal.pbio.1001406.g003" width="230" alt="Figure 3"></a>

<sub>图：Figure 2. An example IFIG of a 408,135-tip phylogeny of small-subunit RNAs using data from SILVA [ 9 ] .（[来源页](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)）；Figure 3. The different fractal forms available in OneZoom.（[来源页](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)）</sub>

<sub>[编码与原文摘录](case-evidence.md#onezoom)</sub>

#### [Reactome 通路浏览器](https://reactome.org/userguide/pathway-browser)

<sub>分子生物学通路 · 层级与树 · 重点：包含与层次、先后与依赖方向</sub>　浏览人类生物通路：从全部通路总览，进入某条通路的反应图

- 展示页：没有找到在线展示页<sub>（https://reactome.org/PathwayBrowser/ 返回 200，但页面显示 'Ooops! This is unexpected...' 错误提示，检查时不可用）</sub>
- 网页：[Pathway Browser - Reactome Pathway Database](https://reactome.org/userguide/pathway-browser)（用户指南，说明 Pathway Browser 的总览用同心圆层级图表示通路，并标注了界面各部分）
- 网页：[Understanding the Pathway Browser \| Reactome](https://www.ebi.ac.uk/training/online/courses/reactome-exploring-biological-pathways/understanding-the-pathway-browser/)（EMBL-EBI 培训页，标题为 Understanding the Pathway Browser，属于 Reactome 培训课程 Exploring biological pathways）

<a href="https://reactome.org/images/userguide/pathway_browser/pathway_browser_labelled.png"><img src="https://reactome.org/images/userguide/pathway_browser/pathway_browser_labelled.png" width="230" alt="pathway browser labelled"></a> <a href="https://reactome.org/images/userguide/pathway_browser/subpathway_selection.png"><img src="https://reactome.org/images/userguide/pathway_browser/subpathway_selection.png" width="230" alt="subpathway selection"></a> <a href="https://reactome.org/images/userguide/pathway_browser/EHLD.png"><img src="https://reactome.org/images/userguide/pathway_browser/EHLD.png" width="230" alt="EHLD"></a>

<sub>图：pathway browser labelled（[来源页](https://reactome.org/userguide/pathway-browser)）；subpathway selection（[来源页](https://reactome.org/userguide/pathway-browser)）；EHLD（[来源页](https://reactome.org/userguide/pathway-browser)）</sub>

<sub>[编码与原文摘录](case-evidence.md#reactome)</sub>

#### [CodeCity](https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf)

<sub>软件演化与度量 · 层级与树 · 重点：包含与层次、对象上的度量</sub>　把软件系统的整体结构一眼看清，找出设计问题的位置

- 展示页：没有找到在线展示页<sub>（未找到官方在线 demo。搜索结果提到 2021、2022 年的论文描述了一个基于 git 仓库的网页版 CodeCity，但未能在官方页面上找到可打开的地址，未收录。）</sub>
- 网页：[https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf](https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf)（论文 PDF（无页面标题），书签目录含 The City Metaphor in a Nutshell、The Tool、Configurability、Application，可看到工具与应用的说明）

<sub>[编码与原文摘录](case-evidence.md#codecity)</sub>

#### [Treemap（磁盘空间）](https://www.cs.umd.edu/hcil/treemap-history/)

<sub>文件系统与资源占用 · 层级与树 · 重点：包含与层次、总体分布</sub>　看谁占用了最多的磁盘空间，哪里有大块或重复的目录

- 展示页（样例目录）：[Treemap \| the D3 Graph Gallery](https://d3-graph-gallery.com/treemap.html)（“Interactivity” 下的 “Button and smooth transition” 一节：按钮可在 size 与 count 之间切换，用于学习平滑过渡（页面文字）。这是第三方示例库，非 D3 官方；页面示例为通用 treemap，未针对磁盘空间。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2042 字</sub>
- 网页：[Treemaps for space-constrained visualization of hierarchies](https://www.cs.umd.edu/hcil/treemap-history/)（Treemap 发展史页，配有 KDirStat、WinDirStat 等文件浏览类 treemap 截图）
- 网页：[Treemap: Home page](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)（HCIL Treemap 项目主页，给出 treemap 的定义（空间受限地显示层级结构的可视化），并列出软件下载与 applet 入口）

<a href="https://www.cs.umd.edu/hcil/treemap-history/index_files/image005.jpg"><img src="https://www.cs.umd.edu/hcil/treemap-history/index_files/image005.jpg" width="230" alt="KDirStat main window"></a> <a href="https://www.cs.umd.edu/hcil/treemap-history/windirstat-small.jpg"><img src="https://www.cs.umd.edu/hcil/treemap-history/windirstat-small.jpg" width="230" alt="WinDirStat"></a> <a href="https://www.cs.umd.edu/hcil/treemap-history/index_files/image007.gif"><img src="https://www.cs.umd.edu/hcil/treemap-history/index_files/image007.gif" width="230" alt="3D treemap for file browsing"></a>

<sub>图：KDirStat main window（[来源页](https://www.cs.umd.edu/hcil/treemap-history/)）；WinDirStat（[来源页](https://www.cs.umd.edu/hcil/treemap-history/)）；3D treemap for file browsing（[来源页](https://www.cs.umd.edu/hcil/treemap-history/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#treemap-diskspace)</sub>

#### [火焰图](https://www.brendangregg.com/flamegraphs.html)

<sub>性能剖析 · 层级与树 · 重点：包含与层次、总体分布</sub>　找出最频繁的代码路径

- 展示页（可直接操作）：[mysqld`page_align (97 samples, 0.03%)](https://www.brendangregg.com/FlameGraphs/cpu-mysql-updated.svg)（这是 SVG 文件，没有独立页面标题，上面的 title 是 SVG 内 <title> 元素的文字。SVG 内可见文字含 “Flame Graph”、“Reset Zoom”、“Search”；cpuflamegraphs 页说明 “mouse over the SVGs to reveal details, and click to zoom”。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 0 字、svg 1 个</sub>
- 网页：[Flame Graphs](https://www.brendangregg.com/flamegraphs.html)（火焰图的作者站点主页，是这个案例的官方入口页）
- 网页：[CPU Flame Graphs](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)（CPU 火焰图页，含用 perf 采样 bash 程序生成的火焰图示例，以及 MySQL 示例（“MySQL CPU Flame Graph”））

<a href="https://www.brendangregg.com/FlameGraphs/cpu-bash-flamegraph.png"><img src="https://www.brendangregg.com/FlameGraphs/cpu-bash-flamegraph.png" width="230" alt="flame-graph"></a>

<sub>[编码与原文摘录](case-evidence.md#flame-graph)</sub>

#### [Universal Dependencies 依存树](https://universaldependencies.org/introduction.html)

<sub>语言学 · 层级与树 · 重点：关系上的类型与量、包含与层次</sub>　用同一套标注描述多种语言的句子结构，方便比较和训练解析器

- 展示页（可直接操作）：[CoNLL-U Viewer](https://universaldependencies.org/conllu_viewer.html)（页面文字为 'CoNLL-U Viewer'，可用 'Load CoNLL-U File ...' 加载 CoNLL-U 文件。UD tools 页面把它列为工具，链接文字为 'Access here'）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 49 字；内容很少，可能需要交互或登录</sub><sub> 打开后所见：只有一个空的 CoNLL-U 文件加载框，要自己提供文件</sub>
- 网页：[Syntax](https://universaldependencies.org/u/overview/syntax.html)（页面说明句法标注是词与词之间带类型的依存关系，基础表示形成一棵树，句中恰有一个词是句子的中心词（head）。）
- 网页：[CoNLL-U Format](https://universaldependencies.org/format.html)（页面说明 UD 采用修订版 CoNLL-X 的 CoNLL-U 格式，用纯文本文件逐词标注词形与句法。）

<sub>[编码与原文摘录](case-evidence.md#universal-dependencies)</sub>

#### [Wikipedia 摘要式写作](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)

<sub>百科写作 · 层级与树 · 重点：包含与层次、跨视图的同一对象</sub>　一个大主题的文章太长，如何拆分又不让读者迷路

- 展示页：没有找到在线展示页<sub>（demo：这是维基百科的写作方法指南，页面上没有可操作的在线演示，记为 null）</sub>
- 网页：[Wikipedia:Summary style - Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)（页面说明 summary style 的做法：长文章把各子主题分到子文章中，母文章对应小节写摘要，并用 'Main article' 类 hatnote 链到子文章。）
- 网页：[Wikipedia:Article size - Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Article_size)（页面给出可读正文长度的经验值，并说明超长文章通常会拆分为两篇或更多较小的文章。）

<sub>[编码与原文摘录](case-evidence.md#wikipedia-summary-style)</sub>

#### [Markmap](https://markmap.js.org/docs/markmap)

<sub>知识管理与写作 · 层级与树 · 重点：包含与层次</sub>　把一篇 Markdown 文档的层级直接看成一张可折叠的思维导图

- 展示页（可直接操作）：[展示页](https://markmap.js.org/repl)（官方首页页面文字 'Visualize your Markdown with mindmaps' 下有 'Try it out →' 入口，链接指向 /repl。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1517 字、svg 1 个</sub>
- 网页：[markmap](https://markmap.js.org/)（官方首页，页面文字为 'Visualize your Markdown with mindmaps'，并有 'Try it out →' 入口。）
- 网页：[markmap - markmap docs](https://markmap.js.org/docs/markmap)（文档的 'What is markmap?' 入门页，页面说明 markmap 是 Markdown 与思维导图的结合。）

<sub>[编码与原文摘录](case-evidence.md#markmap)</sub>

#### [ATLAS：用多个 LLM Agent 自动构建软件仓库分类体系](https://arxiv.org/abs/2606.21597)

<sub>软件仓库分类 · 层级与树 · 重点：包含与层次、有什么</sub>　给五万多个 GitHub 仓库建一棵带定义和拆分理由的多层分类树，用来按任意粒度检索、找功能等价的替代项目、看生态趋势

- 展示页（可直接操作）：[ATLAS: Hierarchical Taxonomy of 54k GitHub Repositories](https://atlas-taxonomy.netlify.app/)（页面标题下是「Rank-Aligned View」视图，顶部统计 Nodes、Leaves、Inserted、Depth Changed、Repos（如「54390 Repos」）；控件包括 Rank Levels（D0–D7）、Node Markers、Inserted (Passthrough)、Sub-layer、Depth Changed、Search，以及 Expand All / Collapse All 和 Highlight Inserted / Highlight Sub-layer / Highlight Depth Changed / Clear Highlight。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 5064 字、svg 4 个</sub><sub> 打开后所见：打开是左侧控件、右侧从左到右展开的分类树（各分支按语义层级对齐成列），顶部统计 36,986 个节点、54,390 个仓库</sub>
- 网页：[ATLAS: Agentic Taxonomy of LArge-Scale Software Ecosystems](https://arxiv.org/html/2606.21597v1)（论文 HTML 版（实验性），含框架架构图 Figure 1（见 images）。）
- 网页：[ATLAS: Agentic Taxonomy of LArge-Scale Software Ecosystems \| Zenodo](https://zenodo.org/records/21160280)（配套复现包的 Zenodo 记录页，页面说明包内含 54,387 个仓库的完整分类结果（output/atlas_54k/，含每个节点的仓库归属），可不运行代码直接使用。）

<sub>[编码与原文摘录](case-evidence.md#atlas-taxonomy)</sub>

#### [Speculora](https://speculora.com/)

<sub>市场需求分析 · 层级与树 · 重点：对象上的度量、有什么</sub>　让独立开发者看到软件需求在哪里拥挤、哪里有可用的缺口

- 展示页（可直接操作）：[Speculora — real demand & saturation data for software ideas](https://speculora.com/)（首页文字写 'Explore the live, interactive map above, or jump into a domain'（交互地图在页面上方）；/info 页的 'Open the live map →' 链接也指向首页）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 3792 字、svg 5 个</sub><sub> 打开后所见：打开是深色界面的任务列表，按机会分数排序，每项标缺口等级和投诉数；顶部有 Top gaps、Full tree、Treemap、Trending 等标签</sub>
- 网页：[What is Speculora? The demand × saturation × gap map for software \| Speculora](https://speculora.com/info)（产品说明页，列出六个缺口等级（Prime Gap、Lacks Features、Poorly Executed、Too Expensive、Undersupplied、Fully Served）及各自的建议动作）
- 网页：[Shopping & Deals — software gaps & app opportunities \| Speculora](https://speculora.com/domain/shopping-deals-694)（领域页样例，按机会分数列出任务，每项标注缺口等级、应用数和用户反馈数（如 Track package deliveries：Opportunity 100/100 · 54 apps · 332 user reports））

<sub>[编码与原文摘录](case-evidence.md#speculora)</sub>

<!-- /gen -->

## 有向无环图

<!-- gen:gallery:dag -->
#### [AgentEnsemble Viz](https://docs.agentensemble.net/guides/visualization/)

<sub>AI Agent 开发 · 有向无环图 · 重点：先后与依赖方向、时间与演化</sub>　看清一次多 Agent 任务：计划里哪些任务并行、哪些串行、关键路径是哪条，实际每个任务何时运行、调了哪些工具

- 展示页：没有找到在线展示页<sub>（viewer 是本地运行的（npx @agentensemble/viz ./traces/，地址 http://localhost:7328），没有找到托管的在线 viewer 或公开样例页…）</sub>
- 网页：[Visualization Example \| AgentEnsemble](https://docs.agentensemble.net/examples/visualization/)（'What You’ll See' 一节按 Flow View 与 Timeline View 描述视图里能看到什么（如关键路径高亮））
- 网页：[Execution Graph Visualization \| AgentEnsemble](https://docs.agentensemble.net/guides/visualization/)（指南页说明 viewer 用 npx @agentensemble/viz 启动，地址为 http://localhost:7328）

<sub>[编码与原文摘录](case-evidence.md#agentensemble-viz)</sub>

#### [Marquez](https://marquezproject.ai/)

<sub>数据工程 · 有向无环图 · 重点：先后与依赖方向、时间与演化</sub>　数据模式改变时，审计并排查下游受影响的作业

- 展示页：没有找到在线展示页<sub>（在线展示页：首页有 'Interactive Demo' 标题，但抓到的页面里没有对应链接（按 demo、interactive 搜索均无结果），可能由脚本或 iframe 渲染，未能核对入口…）</sub>
- 网页：[Marquez Project \| Marquez Project](https://marquezproject.ai/)（首页的 'Unified visual graph' 一节写明：通过网页界面提供可视化的依赖关系图，可查看每个 job 的输入输出，并追踪 dataset 的血缘。）
- 网页：[Quickstart \| Marquez Project](https://marquezproject.ai/docs/quickstart/)（快速开始页写明在 http://localhost:3000 打开 UI，可通过 lineage graph 查看 job 与 dataset 的依赖，并可搜索 job 查看运行元数据。）

<a href="https://marquezproject.ai/img/marquez_caps_couple.svg"><img src="https://marquezproject.ai/img/marquez_caps_couple.svg" width="230" alt="Marquez UI Screencaps"></a> <a href="https://marquezproject.ai/assets/images/search-view-job-99ec2f2497f982774ce92482b7e18c30.png"><img src="https://marquezproject.ai/assets/images/search-view-job-99ec2f2497f982774ce92482b7e18c30.png" width="230" alt="marquez"></a>

<sub>图：Marquez UI Screencaps（[来源页](https://marquezproject.ai/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#marquez)</sub>

#### [AgentEnsemble](https://agentensemble.github.io/agentensemble/)

<sub>AI Agent 开发 · 有向无环图 · 重点：先后与依赖方向、时间与演化</sub>　编排多 Agent 任务，并在关键点让人审核、修改或叫停

- 展示页：没有找到在线展示页<sub>（官方首页 https://agentensemble.github.io/agentensemble/、guides/visualization、examples/visualization、guides/review …）</sub>
- 网页：[Visualization - AgentEnsemble](https://agentensemble.github.io/agentensemble/examples/visualization/)（官方示例页：只有代码和本地运行说明，没有可点的在线界面。这是官方 Examples 库里的 Visualization 示例页。页面 'What You'll See' 一节写明会看到 Flow View 和 Timeline View 两种视图，并有 'Running the Viewer' 一节。页面本身没有可直接点击的在线界面。）
- 网页：[Execution Graph Visualization \| AgentEnsemble](https://docs.agentensemble.net/guides/visualization/)（AgentEnsemble 文档中的可视化指南页（标题 Execution Graph Visualization）。页面上只找到 logo 图片，没有截图或示意图。）

<sub>[编码与原文摘录](case-evidence.md#agentensemble)</sub>

#### [Nx](https://nx.dev/docs/features/explore-graph)

<sub>软件工程 · 有向无环图 · 重点：先后与依赖方向、连通与邻域</sub>　知道改动会影响哪些项目，决定任务的执行顺序

- 展示页（可直接操作）：[Nx Workspace Project Graph](https://nrwl-nx-examples-dep-graph.netlify.app/?focus=cart)（链接来自 Nx 功能页 https://nx.dev/docs/features/explore-graph ，那里标注为 'fully interactive graph on a sample repo'；同页正文写道可在侧栏里用 proximity 和 group by folder 控件调整围绕某项目的图，也可以手动隐藏或显示项目。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 367 字、canvas 3 个、svg 30 个</sub><sub> 打开后所见：能看到示例工程的依赖图，左侧可勾选要显示的项目</sub>
- 网页：[Explore your Workspace \| Nx](https://nx.dev/docs/features/explore-graph)（功能页，说明可在浏览器里交互式查看工作区的项目图，并链接到一个互动样例图。）

<sub>[编码与原文摘录](case-evidence.md#nx)</sub>

#### [DataHub](https://docs.datahub.com/)

<sub>数据工程 · 有向无环图 · 重点：先后与依赖方向、关系上的类型与量</sub>　排查数据问题的上游来源，改动前评估对下游的影响

- 展示页（演示视频或导览）：[Complete Data Lineage with DataHub Cloud \| Live Demo](https://datahub.com/demos/data-lineage-with-datahub/)（页面写 'Experience DataHub Cloud with demos of' 后列出 'Visual lineage explorer with filtering by time, owner, and platform' 和列级血缘，按钮为 'Watch the Demo'）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2630 字、svg 104 个</sub><sub> 打开后所见：页面是带注册表单的宣传页，没有直接可操作的血缘界面</sub>
- 网页：[About DataHub Lineage \| DataHub](https://docs.datahub.com/docs/features/feature-guides/lineage)（官方血缘功能文档，页内嵌有血缘视图、列级血缘、字段级血缘等截图（图片地址在 raw.githubusercontent.com，未收））

<sub>[编码与原文摘录](case-evidence.md#datahub)</sub>

#### [OpenMetadata](https://docs.open-metadata.org/latest/quick-start/sandbox)

<sub>数据工程 · 有向无环图 · 重点：先后与依赖方向、关系上的类型与量</sub>　发现数据资产，并追踪数据怎么变换、在哪被使用

- 展示页（需要登录）：[OpenMetadata](https://sandbox.open-metadata.org/)（官方沙盒（项目表里已有的展示页））<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 121 字；内容很少，可能需要交互或登录</sub><sub> 打开后所见：打开是 “Welcome to OpenMetadata”，只有 Sign in with Google</sub>
- 网页：[Explore the Lineage View \| Official Documentation - OpenMetadata Documentation](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)（官方血缘视图操作页，页内有列级血缘、数据库与管道血缘、影响分析等界面截图）

<a href="https://mintcdn.com/openmetadata/ukveY9QLJfPEF8DI/public/images/how-to-guides/lineage/lineage1.png?fit=max&auto=format&n=ukveY9QLJfPEF8DI&q=85&s=7fcc8275a83d82a45203e001310d0ca9"><img src="https://mintcdn.com/openmetadata/ukveY9QLJfPEF8DI/public/images/how-to-guides/lineage/lineage1.png?fit=max&auto=format&n=ukveY9QLJfPEF8DI&q=85&s=7fcc8275a83d82a45203e001310d0ca9" width="230" alt="Column-Level Data Lineage in OpenMetadata"></a> <a href="https://mintcdn.com/openmetadata/ukveY9QLJfPEF8DI/public/images/how-to-guides/lineage/pipeline.png?fit=max&auto=format&n=ukveY9QLJfPEF8DI&q=85&s=5abc1aee0d0145744ea87894b2970473"><img src="https://mintcdn.com/openmetadata/ukveY9QLJfPEF8DI/public/images/how-to-guides/lineage/pipeline.png?fit=max&auto=format&n=ukveY9QLJfPEF8DI&q=85&s=5abc1aee0d0145744ea87894b2970473" width="230" alt="Database and Pipeline Lineage"></a>

<sub>图：Column-Level Data Lineage in OpenMetadata（[来源页](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)）；Database and Pipeline Lineage（[来源页](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)）</sub>

<sub>[编码与原文摘录](case-evidence.md#openmetadata)</sub>

#### [Git 提交历史](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

<sub>版本控制 · 有向无环图 · 重点：先后与依赖方向、时间与演化</sub>　回看发生过什么，分支怎样分叉与合并

- 展示页（可直接操作）：[Learn Git Branching](https://learngitbranching.js.org/)（第三方交互练习，非 Git 官方项目。页面可见文字为终端标题 “Terminal – Learn Git Branching”，带 “Git” 与 “Hg” 两个标签）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1738 字、svg 2 个</sub><sub> 打开后所见：弹出欢迎窗口，之后是终端加提交图的练习界面</sub>
- 网页：[Git - Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)（Pro Git 分支一节，用提交、父提交与分支指针的图示说明提交历史的结构）
- 网页：[Git - Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)（Pro Git 讲查看提交历史的一节）

<sub>[编码与原文摘录](case-evidence.md#git-history)</sub>

#### [家谱图的交互可视化](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)

<sub>谱系与家族史 · 有向无环图 · 重点：连通与邻域、包含与层次</sub>　在家谱里按自己的关系去探索，不迷路

- 展示页：没有找到在线展示页<sub>（demo：作者 DGP 页面 https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/ 返回 403，按规则记为读不到，未换路径尝试…）</sub>

<sub>[编码与原文摘录](case-evidence.md#genealogical-graphs)</sub>

#### [Software Heritage Graph Dataset](https://registry.opendata.aws/software-heritage/)

<sub>源代码历史图谱 · 有向无环图 · 重点：先后与依赖方向、来源与证据</sub>　跨项目、跨托管平台追踪同一份源码和它的开发历史，研究公开软件开发的长尾

- 展示页：没有找到在线展示页<sub>（未找到官方在线可视化演示。WebSearch 只返回 Athena 查询入口和文档中的示例页（docs.softwareheritage.org/devel/swh-graph/example-dataset.html…）</sub>
- 网页：[Software Heritage Graph Dataset - Registry of Open Data on AWS](https://registry.opendata.aws/software-heritage/)（AWS 开放数据登记页，给出数据集描述，并链接到官方的图数据集使用文档）
- 网页：[The Software Heritage Graph Dataset:Large-scale Analysis of Public Software Development History](https://arxiv.org/html/2011.07824)（论文 HTML 版，图 2 为数据模型示意（统一的 Merkle DAG），图 3 为数据集的简化 schema）

<sub>[编码与原文摘录](case-evidence.md#software-heritage-graph)</sub>

<!-- /gen -->

## 表与多维属性

<!-- gen:gallery:table -->
#### [Grafana](https://github.com/grafana/grafana)

<sub>基础设施运维 · 表与多维属性 · 重点：对象上的度量、连通与邻域</sub>　把查询结果画成面板，其中节点图用来看相互关联的元素

- 展示页（可直接操作）：[Grafana](https://play.grafana.org/)<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 4523 字、svg 80 个</sub><sub> 打开后所见：打开后跳到 “Grafana Play Home” 仪表盘（第一次渲染停在 Loading…，等更久后加载出来）</sub>
- 网页：[Node graph \| Grafana documentation](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)（页面写明节点图用于展示相互关联的元素（节点与连线），列出网络、基础设施、组织架构、思维导图等适用场景，并有 'Give it a try using Grafana Play' 一节。）

<sub>[编码与原文摘录](case-evidence.md#grafana)</sub>

#### [Build Your Own Radar](https://github.com/thoughtworks/build-your-own-radar)

<sub>技术生态 · 表与多维属性 · 重点：对象上的度量</sub>　从一张表生成自己的技术雷达

- 展示页（可直接操作）：[Build your own Radar（页面 title 标签为空，此为页面可见文字）](https://radar.thoughtworks.com/)（页面有输入框 'Enter the URL of your Google Sheet, CSV or JSON file below…'，填入表格或 CSV/JSON 地址即可生成雷达；页面文字写有 'Once you've created your Radar you can use this service to generate an interactive version of your Technology Radar'。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1135 字、svg 4 个</sub><sub> 打开后所见：只有一个输入框：要填自己的 Google Sheet、CSV 或 JSON 地址才会生成雷达，没有现成的雷达可看</sub>
- 网页：[Build your Own Radar \| Thoughtworks](https://www.thoughtworks.com/radar/byor)（官方说明页，讲如何用 Google Sheet / CSV / JSON 数据生成雷达，页内列出数据要求（例如象限名称须为四个）和 'Is my data public?' 等问答。）

<sub>[编码与原文摘录](case-evidence.md#build-your-own-radar)</sub>

#### [OSS Insight](https://ossinsight.io/)

<sub>开源生态 · 表与多维属性 · 重点：总体分布、时间与演化</sub>　了解 GitHub 上现在在发生什么，以及技术领域的排名与趋势

- 展示页（可直接操作）：[OSSInsight — AI Agent Analytics & Open Source GitHub Intelligence](https://ossinsight.io/)（首页导航有 Data Explorer、Collections、Trending、Languages；页面中部有 'What is happening on GitHub NOW' 实时区块、'Trending Repos' 区块和搜索框。Trending Repos 区块写明 'Star-based rankings are paused'（星标排名暂停），原因是 GitHub 事件流分页变化导致采集不全。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1885 字、canvas 1 个、svg 20 个</sub>
- 网页：[Open Source Collections — AI Agent Frameworks, GitHub Trending & More \| OSSInsight](https://ossinsight.io/collections)（页面文字写有 'Browse 102 + curated collections of GitHub repositories grouped by technology domain'，即按技术领域分组的合集列表，可看到站点内容的组织形式。）

<a href="https://ossinsight.io/blog-assets/why-we-choose-tidb-to-support-ossinsight/javascript-framework-rankings.png"><img src="https://ossinsight.io/blog-assets/why-we-choose-tidb-to-support-ossinsight/javascript-framework-rankings.png" width="230" alt="JavaScript frameworks with the most issue creators"></a>

<sub>图：JavaScript frameworks with the most issue creators（[来源页](https://ossinsight.io/blog/why-we-choose-tidb-to-support-ossinsight)）</sub>

<sub>[编码与原文摘录](case-evidence.md#oss-insight)</sub>

#### [OSS Compass](https://oss-compass.org/)

<sub>开源生态 · 表与多维属性 · 重点：对象上的度量</sub>　评估开源社区的健康状况

- 展示页（可直接操作）：[OSS Compass](https://oss-compass.org/os-situation)（首页上 'Open Source Situation Insight' 链接指向此页（首页链接文字））<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2571 字、svg 34 个</sub><sub> 打开后所见：打开是 “Open Source Situation Insight” 页：按洞察维度列出分析卡片（开源贡献趋势、项目发展趋势等），点 View 进入</sub>
- 网页：[Open Source Trend Insights Service \| OSS compass](https://oss-compass.org/docs/docs/service-guide/open-source-insights/)（服务指南中的开源态势洞察服务页。页面文字说明它通过分析全球开源项目，提供进出口、社区、技术领域、开发者、编程语言和许可证等方面的洞察；页内有 5 张配图。）
- 网页：[Open Source Software Selection Evaluation Service \| OSS compass](https://oss-compass.org/docs/docs/service-guide/software-selection/)（服务指南中的软件选型评估服务页。页面文字说明它提供三项功能：评估已知软件、推荐候选软件、查找相似功能的替代软件；页内有 8 张配图。）

<a href="https://oss-compass.org/assets/images/image5-eeec3a8851a9c3caf04d198db5ccbd2a.png"><img src="https://oss-compass.org/assets/images/image5-eeec3a8851a9c3caf04d198db5ccbd2a.png" width="230" alt="oss-compass"></a> <a href="https://oss-compass.org/assets/images/image3-dabc48d9448b2017cddd137359482846.png"><img src="https://oss-compass.org/assets/images/image3-dabc48d9448b2017cddd137359482846.png" width="230" alt="oss-compass"></a>

<sub>[编码与原文摘录](case-evidence.md#oss-compass)</sub>

#### [PyGraphistry](https://github.com/graphistry/pygraphistry)

<sub>数据分析 · 表与多维属性 · 重点：连通与邻域、群落与相似</sub>　把任意表当作图来做可视分析（例如攻击者 IP 到受害者 IP）

- 展示页：没有找到在线展示页<sub>（未找到无需登录即可交互的 PyGraphistry 在线演示：教程中的图形由 g2.plot() 在 Graphistry 服务端渲染，代码写明需要 graphistry.register(...) 账号…）</sub>
- 网页：[Tutorial: Data Analysis in Graphistry — PyGraphistry Documentation](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)（教程页：图在 Graphistry 服务端渲染，需要账号，页面本身只有代码与输出表格。页面是 Notebook 教程，以代码单元和输出表格展示（如 [62] 的节点表）；代码中 g2.plot(as_files=False) 生成图形，encodings 示例注明 'requires api=3' 并给出 graphistry.register(api=3, username='...', password='...')。页面本身无需登录即可打开，但图形渲染需要 Graphistry 账号。）
- 网页：[UI Guide & Advanced Links](https://hub.graphistry.com/docs/ui/index/)（Graphistry 官方 UI 指南页，列出 UI Basics、Filters & Exclusions、Histograms、Selections 等章节，页内有界面截图。）

<a href="https://hub.graphistry.com/static/legacy/images/updated_ui_callouts.png"><img src="https://hub.graphistry.com/static/legacy/images/updated_ui_callouts.png" width="230" alt="Responsive image"></a> <a href="https://hub.graphistry.com/static/legacy/images/main%20panel.png"><img src="https://hub.graphistry.com/static/legacy/images/main%20panel.png" width="230" alt="Responsive image"></a> <a href="https://hub.graphistry.com/static/legacy/images/data%20inspector.jpg"><img src="https://hub.graphistry.com/static/legacy/images/data%20inspector.jpg" width="230" alt="Responsive image"></a>

<sub>图：Responsive image（[来源页](https://hub.graphistry.com/docs/ui/index/)）；Responsive image（[来源页](https://hub.graphistry.com/docs/ui/index/)）；Responsive image（[来源页](https://hub.graphistry.com/docs/ui/index/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#pygraphistry)</sub>

#### [Wikidata Query Service 结果视图](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)

<sub>开放知识图谱 · 表与多维属性 · 重点：对象上的度量、时间与演化</sub>　把一次 SPARQL 查询的结果换成不同的图来看

- 展示页（可直接操作）：[SPARQL](https://query.wikidata.org/)（在查询界面写好 SPARQL 后运行（侧栏蓝色 Execute query 按钮，说明见 Result_Views 页），再在 'Display' 格式中切换结果视图，如 Table、Image Grid、Map、Bubble Chart 等）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 265 字</sub><sub> 打开后所见：打开是空的 SPARQL 查询框，要自己输入查询或从 Examples 里选</sub>
- 网页：[Wikidata:SPARQL query service/Wikidata Query Help/Result Views - Wikidata](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)（逐个介绍结果视图（Table、Image Grid、Map、折线/柱状/散点/面积图、Bubble Chart、Tree Map、Tree、Timeline、Dimensions、Graph），并附截图）

<a href="https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f8/WDQS_-_Bubble_Chart_Result_View.png/250px-WDQS_-_Bubble_Chart_Result_View.png?utm_source=www.wikidata.org&utm_campaign=parser&utm_content=thumbnail"><img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f8/WDQS_-_Bubble_Chart_Result_View.png/250px-WDQS_-_Bubble_Chart_Result_View.png?utm_source=www.wikidata.org&utm_campaign=parser&utm_content=thumbnail" width="230" alt="wikidata-query-views"></a>

<sub>图：Bubble Chart Try Out（[来源页](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)）</sub>

<sub>[编码与原文摘录](case-evidence.md#wikidata-query-views)</sub>

#### [Gapminder 气泡图](https://www.gapminder.org/tools/)

<sub>国际发展统计 · 表与多维属性 · 重点：对象上的度量、时间与演化</sub>　看各国在收入、寿命、人口等指标上的关系，以及这种关系怎样随时间变化

- 展示页（可直接操作）：[展示页](https://www.gapminder.org/tools/)（新闻页 'Gapminder Tools are coming' 中的链接 '⧉ Gapminder Tools' 指向该地址；新闻页正文写 'Welcome ⧉ Gapminder Tools : our new Bubble Chart and more!'）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 3451 字、canvas 4 个、svg 149 个</sub>
- 网页：[Gapminder Tools are coming \| Gapminder](https://www.gapminder.org/news/gapminder-tools-are-coming/)（官方新闻页，介绍新版 Gapminder Tools 的 Bubble Chart，页面附有使用方法的示意图）
- 网页：[Quick guide to the Motion Chart \| Gapminder](https://www.gapminder.org/upload-data/motion-chart/)（官方指南页，说明在 Google 表格里用 Motion Chart 做气泡图的步骤（这是 Google 表格的小工具，不是 Gapminder 自己的工具），页面有一张样例图）

<sub>[编码与原文摘录](case-evidence.md#gapminder)</sub>

<!-- /gen -->

## 文本与文档

<!-- gen:gallery:text -->
暂无。
<!-- /gen -->

## 序列与事件流

<!-- gen:gallery:sequence -->
#### [OpenTelemetry GenAI 语义约定](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

<sub>AI Agent 观测 · 序列与事件流 · 重点：对象上的度量</sub>　规定 AI 和 Agent 的运行记录该有哪些字段（后面所有可视化的数据来源）

- 展示页：没有找到在线展示页<sub>（规范类，没有在线展示页。）</sub>

<sub>[编码与原文摘录](case-evidence.md#otel-genai-semconv)</sub>

#### [OpenLLMetry](https://github.com/traceloop/openllmetry)

<sub>AI Agent 观测 · 序列与事件流 · 重点：包含与层次</sub>　以不改代码的方式采集 LLM 应用的运行追踪

- 展示页：没有找到在线展示页<sub>（在线展示页：traceloop.com/demo 与 www.traceloop.com/demo 均返回 404；官网页和文档介绍页上未找到 demo 或 playground 链接…）</sub>
- 网页：[What is OpenLLMetry? - traceloop](https://docs.traceloop.com/docs/openllmetry/introduction)（官方文档的介绍页，页面标题即为 What is OpenLLMetry?。）
- 网页：[Open-source Observability for LLMs with OpenTelemetry](https://www.traceloop.com/openllmetry)（官网的 OpenLLMetry 页，页面上有 'Start now with just 2 lines of code' 下的 Python 和 Typescript 示例代码。）

<a href="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=2733424bcb797188846417e2516e50fe"><img src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=2733424bcb797188846417e2516e50fe" width="230" alt="openllmetry"></a>

<sub>[编码与原文摘录](case-evidence.md#openllmetry)</sub>

#### [Up and Down the Ladder of Abstraction](https://worrydream.com/LadderOfAbstraction/)

<sub>交互式写作与抽象 · 序列与事件流 · 重点：时间与演化、对象上的度量</sub>　通过在不同抽象层之间上下移动，理解一个系统的行为

- 展示页（可直接操作）：[Up and Down the Ladder of Abstraction](https://worrydream.com/LadderOfAbstraction/)（文章本身就是交互页面。页面文字：'Click Tap to the right to find out how this algorithm behaves.'（点击或轻触右侧，查看算法的行为）；'Drag the slider at the right to control time explicitly.'（拖动右侧滑块显式控制时间）；'we can also mouse over touch the trajectory to see the car at that point.'（鼠标移到轨迹上，查看该点对应的车）。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 39031 字、canvas 44 个</sub>

<sub>[编码与原文摘录](case-evidence.md#ladder-of-abstraction)</sub>

<!-- /gen -->

## 集合与分类

<!-- gen:gallery:set -->
#### [CNCF Landscape](https://landscape.cncf.io/)

<sub>技术生态 · 集合与分类 · 重点：有什么、对象上的度量</sub>　在云原生生态里找到某类项目，并查看具体项目的信息

- 展示页（可直接操作）：[CNCF Landscape](https://landscape.cncf.io/)<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2737 字、svg 78 个</sub><sub> 打开后所见：打开是 CNCF 交互式全景图：按类别分区的项目 logo 网格，顶部有 Explore / Guide / Stats 标签，左侧有筛选与分组选项</sub>
- 网页：[Introducing the Cloud Native Landscape 2.0 - interactive edition \| CNCF](https://www.cncf.io/blog/2018/03/08/introducing-the-cloud-native-landscape-2-0-interactive-edition/)（官方博客介绍交互版：可以筛选、查看某个项目或技术的详细信息，并通过带状态的 URL 分享；页内有 landscape 网站页面的截图。）
- 网页：[The beginner's guide to the CNCF landscape \| CNCF](https://www.cncf.io/blog/2018/11/05/beginners-guide-cncf-landscape/)（官方入门指南，按类别逐个解释 landscape 中的项目（正文例如 Notary、OPA、NATS、gRPC）；页面上未见界面截图。）

<a href="https://www.cncf.io/wp-content/uploads/2020/08/CNCF-Lanscape-1.png"><img src="https://www.cncf.io/wp-content/uploads/2020/08/CNCF-Lanscape-1.png" width="230" alt="Cloud Native Interactive Landscape website page"></a>

<sub>图：Cloud Native Interactive Landscape website page（[来源页](https://www.cncf.io/blog/2018/03/08/introducing-the-cloud-native-landscape-2-0-interactive-edition/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#cncf-landscape)</sub>

#### [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar)

<sub>技术生态 · 集合与分类 · 重点：对象上的度量、时间与演化</sub>　判断每项技术或做法现在是否推荐采用

- 展示页（可直接操作）：[Technology Radar \| Guide to technology landscape \| Thoughtworks](https://www.thoughtworks.com/radar)（页面正文写有 'Explore the interactive version by quadrant, or download the PDF to read the Radar in full'（按象限查看交互版，或下载 PDF）；页面列出 Adopt、Trial、Assess、Caution 四个环的说明。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 13734 字、canvas 6 个、svg 29 个</sub><sub> 打开后所见：打开是第 34 期技术雷达的介绍页（有下载和订阅按钮），页面上没有直接显示雷达图</sub>
- 网页：[FAQ \| Thoughtworks](https://www.thoughtworks.com/radar/faq)（官方 FAQ 解释雷达的象限（quadrants）与环（rings）的含义，以及 blip 在环中位置的意义。）

<sub>[编码与原文摘录](case-evidence.md#thoughtworks-tech-radar)</sub>

#### [Zalando Tech Radar](https://github.com/zalando/tech-radar)

<sub>技术生态 · 集合与分类 · 重点：对象上的度量</sub>　帮工程团队为新项目选技术，并跟踪技术决策的演变

- 展示页（可直接操作）：[Zalando Tech Radar](https://opensource.zalando.com/tech-radar/)（页面正文是 'What is the Tech Radar?' 和四个环（ADOPT / TRIAL / ASSESS / HOLD）的说明；末尾写有 'generate this visualization'（生成这一可视化的代码已开源），说明页面上有雷达可视化，但页面文字没有描述具体交互方式。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 4367 字、svg 1 个</sub>
- 网页：[Building a Better Tech Radar](https://engineering.zalando.com/posts/2018/01/building-tech-radar.html)（官方工程博客，讲 Tech Radar 的自动布局（力导向布局加笛卡尔与极坐标包围盒），文中嵌有一张自动生成的雷达截图。）

<a href="https://img01.ztat.net/engineering-blog/posts/2018/01/images/75793f677142d5be65cd880d33eaee13ea5594c5_screen-shot-2018-01-25-at-11.16.16.png?imwidth=1320"><img src="https://img01.ztat.net/engineering-blog/posts/2018/01/images/75793f677142d5be65cd880d33eaee13ea5594c5_screen-shot-2018-01-25-at-11.16.16.png?imwidth=1320" width="230" alt="zalando-tech-radar"></a>

<sub>[编码与原文摘录](case-evidence.md#zalando-tech-radar)</sub>

#### [Open Source AI Gap Map](https://www.aipotluck.org/map)

<sub>开源生态评估 · 集合与分类 · 重点：对象上的度量、有什么</sub>　看开源 AI 生态里哪些类别已经成熟、哪里还有缺口，好决定资金和精力投向哪里

- 展示页（可直接操作）：[Explore the Gap Map – AI Potluck](https://www.aipotluck.org/map/gap-map)（页面有「Explore the Gap Map」区块，列出 Total products、Assessed products、Open(ish) products、Gaps found 等数字；下面按「Model components」与「Product / UX」两组列出各类别，每行有成熟度（如「3 /5」）、Gaps found 标记和 open(ish) 产品数；页面上有「Legend」「How to read the map」入口。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 3518 字、svg 215 个</sub><sub> 打开后所见：打开是 “Explore the Gap Map”：顶部四个数字（62,538 个产品、1,133 个已评估、879、38 个缺口），下面按 Model components 等页签列出类别，每行有成熟度徽章、缺口标记和开放产品的色块</sub>
- 网页：[Open Source AI Stack Gap Map – AI Potluck](https://www.aipotluck.org/map)（项目主页，页面上嵌有 Gap Map 图表图（alt 为「The Gap Map chart, showing overall scores across the open source AI stack」），并有对地图的简短介绍。）
- 网页：[Introducing the Gap Map v0.1](https://www.currentai.org/blogs/introducing-the-gap-map-v0-1)（v0.1 发布博文，正文介绍 Gap Map 的目的与覆盖范围，并嵌有多张图片（见 images）。）

<a href="https://content.aipotluck.org/gap-map-banner.png"><img src="https://content.aipotluck.org/gap-map-banner.png" width="230" alt="The Gap Map chart, showing overall scores across the open source AI stack"></a> <a href="https://cdn.prod.website-files.com/683836d22e82afa0e5494c4b/6a44fcbc2068be16addd28c5_gap-map-dashboard.webp"><img src="https://cdn.prod.website-files.com/683836d22e82afa0e5494c4b/6a44fcbc2068be16addd28c5_gap-map-dashboard.webp" width="230" alt="oss-ai-gap-map"></a>

<sub>图：The Gap Map chart, showing overall scores across the open source AI stack（[来源页](https://www.aipotluck.org/map)）</sub>

<sub>[编码与原文摘录](case-evidence.md#oss-ai-gap-map)</sub>

<!-- /gen -->

## 空间与几何

<!-- gen:gallery:spatial -->
#### [Embedding Projector](https://projector.tensorflow.org/)

<sub>机器学习 · 空间与几何 · 重点：群落与相似、空间位置</sub>　检查相近的点是否在语义上真的相关，并在高维空间里找有意义的方向

- 展示页（可直接操作）：[展示页](https://projector.tensorflow.org/)（页面静态 HTML 中有投影面板的文字：BOOKMARKS 抽屉说明 'Open this drawer to save a set of views of the projection, including selected points. A file containing the bookmarks can then be saved and later loaded to view them.'）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 415 字、canvas 3 个、svg 39 个</sub><sub> 打开后所见：打开是 Embedding Projector：左侧选数据（默认 Word2Vec 10K），中间是点云（PCA 视图，10000 点、200 维），可切换 UMAP、T-SNE、PCA、CUSTOM</sub>
- 网页：[Visualizing Data using the Embedding Projector in TensorBoard \| TensorFlow](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin)（TensorFlow 官方的 TensorBoard Embedding Projector 使用页，页内有 embedding_projector 系列示例图（alt 为空）。）
- 网页：[Open sourcing the Embedding Projector: a tool for visualizing high dimensional d](https://research.google/blog/open-sourcing-the-embedding-projector-a-tool-for-visualizing-high-dimensional-data/)（Google Research 官方博客，介绍 Embedding Projector 的开源；页面 og:image 文件名为 embedding-mnist.gif。）

<a href="https://www.tensorflow.org/tensorboard/images/embedding_projector.png?raw=1"><img src="https://www.tensorflow.org/tensorboard/images/embedding_projector.png?raw=1" width="230" alt="embedding-projector"></a> <a href="https://www.tensorflow.org/tensorboard/images/embedding_projector_hitchcock.png?raw=1"><img src="https://www.tensorflow.org/tensorboard/images/embedding_projector_hitchcock.png?raw=1" width="230" alt="embedding-projector"></a> <a href="https://storage.googleapis.com/gweb-research2023-media/original_images/f02c81bacca2434edcc059ef56bbd5e4-embedding-mnist.gif"><img src="https://storage.googleapis.com/gweb-research2023-media/original_images/f02c81bacca2434edcc059ef56bbd5e4-embedding-mnist.gif" width="230" alt="embedding-projector"></a>

<sub>[编码与原文摘录](case-evidence.md#embedding-projector)</sub>

#### [Circos](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)

<sub>比较基因组 · 空间与几何 · 重点：空间位置、连通与邻域</sub>　比较基因组，显示基因组位置对之间的关系

- 展示页：没有找到在线展示页<sub>（circos.ca 官网，以及 PMC 页面链接的 mkweb.bcgsc.ca/circos 与 /tableviewer，在本环境 DNS 解析失败，读不到，无法确认是否有在线演示）</sub>
- 网页：[Circos: An information aesthetic for comparative genomics - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)（Circos 原论文页，Figure 5 至 7 的图注描述了全基因组拷贝数轨道及染色体放大等图的画法）

<a href="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83a8/2752132/c478c2ce1cb2/1639fig5.jpg"><img src="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83a8/2752132/c478c2ce1cb2/1639fig5.jpg" width="230" alt="Figure 5."></a> <a href="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83a8/2752132/60841735c591/1639fig6.jpg"><img src="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83a8/2752132/60841735c591/1639fig6.jpg" width="230" alt="Figure 6."></a> <a href="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83a8/2752132/4e726d4b0642/1639fig7.jpg"><img src="https://cdn.ncbi.nlm.nih.gov/pmc/blobs/83a8/2752132/4e726d4b0642/1639fig7.jpg" width="230" alt="Figure 7."></a>

<sub>图：Copy number whole-genome profiles of five follicular lymphoma tumor samples generated from the Affymetrix Mapping 500K array. Samples are represented in each of the five histograms in tracks A–E. (后文省略)（[来源页](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)）；Copy number profiles for chromosomes 6 and 17 of five follicular lymphoma tumor samples generated from the Affymetrix Mapping 500K array. Probe values were averaged across 20 adjacent probes. (后文省略)（[来源页](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)）；Copy number profiles for chromosomes 6 and 17 of five follicular lymphoma tumor samples generated from the Affymetrix Mapping 500K array. Regions of interest A and B on chromosomes 6 and J and K on chromosomes 17 (后文省略)（[来源页](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#circos)</sub>

#### [Semantic Map of GitHub](https://stevenfazzio.com/semantic-github-map/)

<sub>开源生态地图 · 空间与几何 · 重点：空间位置、群落与相似</sub>　看高 Star 仓库按 README 语义自然聚成哪些主题，每个仓库在地图上和谁相邻

- 展示页（可直接操作）：[Semantic Map of GitHub](https://stevenfazzio.com/semantic-github-map/)（页面副标题「Top 10,000 most-starred repositories, mapped by README similarity」；顶部有 Visualization / Methodology 切换，工具栏有 Advanced Filters、Reset、Display（Labels、Edge Graph、Legend）和 Point / Label / Meta / Colormap Data 的百分比控件。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 155 字、canvas 1 个</sub><sub> 打开后所见：打开是一张彩色点云地图，带 Speech Recognition、AI Agents、Web Components 等主题标签，左侧有搜索和 Advanced Filters，底部可选 Clusters 着色</sub>
- 网页：[Methodology — Semantic Map of GitHub](https://stevenfazzio.com/semantic-github-map/methodology.html)（方法页，含「Using the Visualization」一节与字段定义（Field Definitions），说明这个可视化怎么用。）

<sub>[编码与原文摘录](case-evidence.md#semantic-map-github)</sub>

#### [Map of GitHub](https://anvaka.github.io/map-of-github/)

<sub>开源生态地图 · 空间与几何 · 重点：群落与相似、空间位置</sub>　看 GitHub 上几十万个项目在“被同一批人点 Star”的空间里怎样分布成一块块“国家”，找到相邻的项目

- 展示页（可直接操作）：[Map of GitHub](https://anvaka.github.io/map-of-github/)（页面文字只有加载提示「Website load sequence initiated...」，地图由脚本渲染，页面文字里看不到操作说明；未能从页面文字确认可交互的界面细节。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 15 字、canvas 1 个、svg 1 个</sub><sub> 打开后所见：打开是深色背景的点团地图，每个团有名字（如 Frozen Esclave），左上角有 Find Project 搜索框</sub>

<sub>[编码与原文摘录](case-evidence.md#map-of-github)</sub>

<!-- /gen -->

## 因果与反馈

<!-- gen:gallery:causal -->
#### [Insight Maker](https://www.insightmaker.com/)

<sub>系统建模 · 因果与反馈 · 重点：环与反馈、对象上的度量</sub>　搭建存量流量模型并改变参数，看系统的行为

- 展示页（样例目录）：[Explore Insights \| Insight Maker](https://www.insightmaker.com/explore)（页面有 'Find Insights' 区块，文字为 'Enter keywords or topics to find matching Insights.'，下方有 'Popular Tags'（如 ABM、Agriculture、Animals）。）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 1253 字、svg 1 个</sub>
- 网页：[Insight Maker \| Build simulations and models for free](https://www.insightmaker.com/)（官网首页，页内有 'Explore More Insights' 入口和三张模型图（alt 分别为 'A climate change model'、'A world model'、'An Agent Based disease model'）。）
- 网页：[Model Diagramming \| Insight Maker](https://www.insightmaker.com/docs/diagramming)（官方文档中的 Model Diagramming 页，页内有 toolbar_nodes、toolbar_connector、toolbar_style 等编辑器工具栏图片（alt 为空）。）

<a href="https://www.insightmaker.com/images/diagram_slide.png"><img src="https://www.insightmaker.com/images/diagram_slide.png" width="230" alt="A climate change model"></a> <a href="https://www.insightmaker.com/images/sd_slide.png"><img src="https://www.insightmaker.com/images/sd_slide.png" width="230" alt="A world model"></a> <a href="https://www.insightmaker.com/images/abm_slide.png"><img src="https://www.insightmaker.com/images/abm_slide.png" width="230" alt="An Agent Based disease model"></a>

<sub>图：A climate change model（[来源页](https://www.insightmaker.com/)）；A world model（[来源页](https://www.insightmaker.com/)）；An Agent Based disease model（[来源页](https://www.insightmaker.com/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#insightmaker)</sub>

#### [Explorable Explanations](https://worrydream.com/ExplorableExplanations/)

<sub>交互式写作 · 因果与反馈 · 重点：关系上的类型与量、对象上的度量</sub>　让读者不只读结论，还能改动前提看后果

- 展示页（可直接操作）：[Ten Brighter Ideas? An Explorable Explanation](https://worrydream.com/TenBrighterIdeas/)（页面写：'Mouse over each claim to read and play with an interactive analysis. Mouse over any statistic to see the source.'（鼠标移到每条主张上可阅读并操作交互分析，移到统计数字上可看来源））<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 2901 字</sub>
- 网页：[Explorable Explanations](https://worrydream.com/ExplorableExplanations/)（作者 Bret Victor 的总文，用 Ten Brighter Ideas、滤波器示例和上下文信息三个例子说明可交互文章的形式，正文中有可调整的示例。）
- 网页：[Tangle: a JavaScript library for reactive documents](https://worrydream.com/Tangle/)（页面说明 Tangle 是用于做可交互文档（reactive documents）的 JavaScript 库，读者可以在文档中交互式地探索可能性、调整参数。）

<a href="https://worrydream.com/ExplorableExplanations/Media/IntroTenBrighterIdeas.png"><img src="https://worrydream.com/ExplorableExplanations/Media/IntroTenBrighterIdeas.png" width="230" alt="explorable-explanations"></a> <a href="https://worrydream.com/ExplorableExplanations/Media/IntroFilter.png"><img src="https://worrydream.com/ExplorableExplanations/Media/IntroFilter.png" width="230" alt="explorable-explanations"></a>

<sub>[编码与原文摘录](case-evidence.md#explorable-explanations)</sub>

<!-- /gen -->

## 流量网络

<!-- gen:gallery:flow -->
#### [LLNL 美国能源流向图](https://flowcharts.llnl.gov/)

<sub>能源 · 流量网络 · 重点：关系上的类型与量、总体分布</sub>　看清能源从哪里来、被哪些部门使用、有多少被浪费

- 展示页（样例目录）：[Energy Flow Charts \| Flowcharts](https://flowcharts.llnl.gov/commodities/energy)（页面写明 'Search the flow chart database by year, country, and state'，可按年份、国家、州搜索流向图数据库；页内列出各州 2024 年 Sankey 图的缩略图）<sub> 渲染检查（无头 Chromium，2026-10-13）：页面文字 4901 字、svg 13 个</sub>
- 网页：[Energy Flow Charts \| Lawrence Livermore National Laboratory](https://flowcharts.llnl.gov/)（首页说明流向图（也称 Sankey 图）是单页参考图，并给出 2024 年美国能源流向图）
- 网页：[Energy Flow Charts \| STAR](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)（STAR 站的能源流向图页，说明这些图用来呈现国家尺度能源系统的结构）

<a href="https://flowcharts.llnl.gov/sites/flowcharts/files/2026-08/2024-us-energy-flowchart-homepage.jpg"><img src="https://flowcharts.llnl.gov/sites/flowcharts/files/2026-08/2024-us-energy-flowchart-homepage.jpg" width="230" alt="A sankey chart showing U.S. energy consumption in 2024."></a>

<sub>图：A sankey chart showing U.S. energy consumption in 2024.（[来源页](https://flowcharts.llnl.gov/)）</sub>

<sub>[编码与原文摘录](case-evidence.md#llnl-energy-flow)</sub>

<!-- /gen -->
