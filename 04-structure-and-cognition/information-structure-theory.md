# 信息结构理论

回答的问题：复杂信息背后的数据结构有哪些类别；每一类在实际案例里回答什么议题、结构的哪一部分是重点、怎么画、画不出什么。

## 这份文档怎么来的

不是先从文献里列一套分类，再找例子，而是反过来：先收不同领域的案例，给每个案例标出“它被当成哪类数据结构、结构的哪一部分是重点、最后怎么可视化”，再看规律。做法见 [案例分析的方法](case-analysis-method.md)，全部案例和编码见 [案例表](case-analysis.md)，每条编码依据的官方原文见 [案例证据](case-evidence.md)。文献（Munzner、Hogan 等、McGee 等、Schulz 等）只用来校准词表和解释规律。

下文每条结论后面标了证据类型：

- 〔案〕来自案例表，能点回具体案例和官方原文。
- 〔文〕来自我读过的文献，标了出处。
- 〔推〕整理者的推断，没有直接证据，需要再找案例验证。

语料的偏向要先说在前面：84 个案例里，56 个来自本库收的软件、AI、数据平台项目，28 个来自其他领域（交通、生物、能源、金融、语言学、论证、写作等）。工程工具偏多，所以关于“软件和运行观测”的结论比关于其他领域的结论更扎实。

## 三个总的发现

**一、单一结构不够用〔案〕。** 84 个案例里有 44 个要用两种以上的结构才描述得准。最常见的叠加：

| 叠加 | 案例数 | 例子 |
| --- | --- | --- |
| 层级 + 图 | 11 | [CodeBoarding](case-evidence.md#codeboarding)（组件层级 + 组件关系）、[Jaeger](case-evidence.md#jaeger)（span 树 + 服务依赖图）、[Reactome](case-evidence.md#reactome)（通路层级 + 反应图） |
| 层级 + 时间 | 4 | [AgentPrism](case-evidence.md#agentprism)、[AgentOps](case-evidence.md#agentops)、[Arize Phoenix](case-evidence.md#arize-phoenix)、[AgentScope](case-evidence.md#agentscope) |
| 文本 → 图 | 4 | [InfraNodus](case-evidence.md#infranodus)、[GraphRAG](case-evidence.md#graphrag)、[Docling Graph](case-evidence.md#docling-graph)、[LightRAG](case-evidence.md#lightrag) |
| 有向无环图 + 时间 | 3 | [AgentEnsemble Viz](case-evidence.md#agentensemble-viz)（计划 DAG 与执行 Trace）、[n8n](case-evidence.md#n8n)（工作流与执行记录） |
| 图 + 时间 | 3 | [LangGraph](case-evidence.md#langgraph)、[AutoGen Studio](case-evidence.md#autogen)、[Graphiti](case-evidence.md#graphiti) |
| 表 → 图 | 2 | [PyGraphistry](case-evidence.md#pygraphistry)、[Grafana](case-evidence.md#grafana) |

这意味着给一份材料归类时，问的不该是“它是树还是图”，而是“它的底座是哪种结构、叠了什么”。〔案〕

**二、重点部分比结构类别更决定画法〔案〕。** 同样归为“一般图与网络”的 27 个案例，第一重点分成四群，画法随之不同：

- 重点是连通与邻域（15 个）：[Kiali](case-evidence.md#kiali)、[Backstage](case-evidence.md#backstage)、[ICIJ Offshore Leaks](case-evidence.md#icij-offshore-leaks)、[Kumu](case-evidence.md#kumu)、[伦敦地铁图](case-evidence.md#tube-map)、[Hive Plot](case-evidence.md#hive-plot) 等。画成节点连线图或示意图，布局只要让邻接读得出来。
- 重点是先后与依赖方向（6 个）：[bpmn-js](case-evidence.md#bpmn-js)、[Flowise](case-evidence.md#flowise)、[LangGraph](case-evidence.md#langgraph)、[SBGN](case-evidence.md#sbgn)、[设计结构矩阵](case-evidence.md#dsm) 等。画成有方向的流程图，或者画成矩阵再排序。
- 重点是环与反馈（2 个）：[Madge](case-evidence.md#madge)、[pydeps](case-evidence.md#pydeps)。pydeps 单独提供“只显示导入环”的选项，并把环用蓝色框标出。
- 重点是对象上的度量或关系上的类型和量（4 个）：颜色、大小、线型承担这些。

同样，“层级与树”里叶子带数量的，画成矩形树图、冰柱图、火焰图；节点带时间的，画成缩进加时间条的瀑布图；只关心导航的，画成可折叠的列表或连续缩放。〔案〕

**三、一个视图是对结构的有损投影；丢掉的那一部分，常由同一系统里的另一个视图补上〔案〕。** 84 个案例里有 26 个提供了多个视图。设计者常常明说自己丢了什么：

- 地铁图丢掉真实的地理形状和距离。〔案：[伦敦地铁图](case-evidence.md#tube-map)〕
- 火焰图丢掉时间顺序：“The x-axis shows the stack profile population, sorted alphabetically (it is not the passage of time)”。同一页还讲了把时间放回 x 轴的火焰图表（flame chart）。〔案：[火焰图](case-evidence.md#flame-graph)〕
- 技术雷达丢掉技术之间的关系，只留每一项的状态。〔案：[Thoughtworks 雷达](case-evidence.md#thoughtworks-tech-radar)〕
- SBGN 的实体关系语言丢掉时间，活动流语言丢掉机制细节，它们被明说是“同一份生物学信息的三种可替代的投影”（“three alternative projections of the underlying, more complex biological information”）。〔案：[SBGN](case-evidence.md#sbgn)〕
- AgentEnsemble 的 Flow 视图看依赖不看时间，Timeline 视图看时间不看依赖；两张图靠点击任务保持同一个对象。〔案：[AgentEnsemble Viz](case-evidence.md#agentensemble-viz)〕

补上丢失部分的办法，是让同一个对象在各个视图之间保持可对应：Nextstrain 用颜色把树、地图、时间连起来（“Color is used consistently throughout the app in order to link different panels”）；LikeC4 让视图从同一份模型继承范围；AFFiNE 让同样的块既能排成文档也能摆在画布上。〔案〕

## 各类结构

下面每一类先说本库里的用法，再说案例里它回答什么议题、常见的重点部分、常见画法和画不出的东西。数字是该类作为“主类”的案例数。

### 层级与树（21）

**用法。** 每个对象至多有一个上级，关系是包含或父子。〔文〕任何层级都可以表示成嵌套集合：“since any hierarchy can be represented by nested sets”（Schulz 等，《The Design Space of Implicit Hierarchy Visualization》引言）。所以层级既可以用连线表达（显式），也可以用包含和重叠表达（隐式）。

**回答什么议题。** 最多的是定位异常（9 个，几乎都是运行追踪和资源占用）、建立全貌（4 个）、探索发现（3 个）。〔案〕

**重点部分。** 首位重点是包含与层次（14 个）和时间（4 个）。〔案〕

**三种常见变体。**

1. 叶子带数量：用包含表达层级，用面积或宽度表达数量。[Treemap](case-evidence.md#treemap-diskspace)、[火焰图](case-evidence.md#flame-graph)、[CodeCity](case-evidence.md#codecity)（三维版，高度编码方法数）。设计者提到的理由是屏幕空间：“Tree structured node-link diagrams grew too large to be useful”，而 treemap 能“see tens of thousands of nodes in a fixed space”。〔案〕
2. 节点带时间：缩进表达嵌套，横条表达起止时间。[Jaeger](case-evidence.md#jaeger)、[AgentPrism](case-evidence.md#agentprism)、[AgentOps](case-evidence.md#agentops)、[LangWatch](case-evidence.md#langwatch)、[Comet Opik](case-evidence.md#comet-opik)。这是运行观测里最常见的一种。〔案〕
3. 只关心导航：目录列表、折叠展开、连续缩放。[Kialo](case-evidence.md#kialo)（按支持和反对分栏）、[Reactome](case-evidence.md#reactome)（层级列表加总览加详图）、[OneZoom](case-evidence.md#onezoom)（把整棵树放在一页，用地图式缩放）。〔案〕

**画不出的东西。** 横向联系。[Markmap](case-evidence.md#markmap) 把 Markdown 的标题层级变成导图，只用了层级这一种关系，文章里的论证和跨节联系不会出现。〔案+推〕CmapTools 的作者把跨联（cross-link）看得很重：“In the creation of new knowledge, cross-links often represent creative leaps”。纯树状的视图都丢了它。〔案：[CmapTools](case-evidence.md#cmaptools)〕

### 有向无环图（11）

**用法。** 一个对象可以有多个上游或下游，方向表示先后、依赖或来源，没有环。

**回答什么议题。** 影响范围（3）、构建编辑（3）、追踪流向（2）。〔案〕

**重点部分。** 先后与依赖方向（9 个）；时间在 7 个 DAG 案例里也是重点之一。〔案〕

**常见画法。** 从左到右或从上到下的分层有向图，边带方向；规模一大就聚合并支持“原地展开”：Nx 的组合节点（“Composite nodes are essential to navigate a graph of even a moderate size”）、DataHub 把数据管道画成装着任务的盒子、表级血缘里展开字段级血缘。〔案：[Nx](case-evidence.md#nx)、[DataHub](case-evidence.md#datahub)、[OpenMetadata](case-evidence.md#openmetadata)〕

**一个模式：计划与执行成对。** [AgentEnsemble](case-evidence.md#agentensemble-viz)（任务依赖图与执行 Trace）、[n8n](case-evidence.md#n8n)（工作流与执行记录，可把一次执行的数据带回编辑器）、[LangGraph](case-evidence.md#langgraph)（图与检查点历史，可从检查点分叉）。设计时的结构和运行时的记录是两份数据，靠对象身份连起来。〔案〕

**一个反例：默认视图不是图。** [Git 提交历史](case-evidence.md#git-history)的数据结构是 DAG（合并提交有多个父提交），但默认视图是按时间倒序的一维列表，要加 `--graph` 才画出分叉和合并。〔案〕

**家谱也是 DAG。** [McGuffin 等](case-evidence.md#genealogical-graphs)的做法是不画整张图，而是每次只看以当前人为中心的“祖先树 + 后代树”两棵树，并用折叠展开做拓扑导航：“convinced us to focus on visualizing only a subset of the graph at a time”。〔案〕

### 一般图与网络（27）

**用法。** 对象和关系；可以有环、可以无向；对象和关系可分类型，点和边可带属性。〔文〕Hogan 等对知识图谱的综述把常见的图数据模型分为有向边标签图、异质图、属性图、图数据集，并指出：当需要给边加上时间、来源等上下文时，可以把边变成节点，或使用“reification”（对边再做陈述）。

**回答什么议题。** 构建编辑（7）、定位异常（6）、建立全貌（5）、探索发现（4）。〔案〕

**重点部分。** 见上面的第二个发现：连通、先后、环三群。

**规模问题的三种回应。** 设计者对节点连线图在大规模时的失败说得很直白：“In a hairball, data is subordinate to layout”（Hive Plot）、“graph visualizations are only viable up to a certain size”（VOWL）、“Viewing the entire graph can be unmanageable even for smaller repositories”（Nx）。案例里看到三种不同的回应：〔案〕

- 换编码：用包含代替连线（上面的 treemap 一族）。
- 聚合再展开：Nx 的组合节点、Kiali 的四种图（服务图聚合所有流量，带版本的应用图把版本拆开）。
- 换坐标：位置不由物理模拟决定，而由结构性质决定。[Hive Plot](case-evidence.md#hive-plot)：“Node-to-axis assignment and node-on-axis position are determined solely by network structure”；[Circos](case-evidence.md#circos) 把基因组首尾相接成环，位置对之间的关系画成环内的彩带，避免线性排列时连线横穿无关区域（论文原话：“multitudes of lines transgress unrelated ideograms”）；[设计结构矩阵](case-evidence.md#dsm)把依赖变成矩阵，靠重排行列（sequencing）减少反馈标记、靠聚类（clustering）找出模块。

〔文〕节点连线图和矩阵的对比有受控实验：Ghoniem、Fekete、Castagliola（《Information Visualization》4(2)，2005）的结论经 Munzner 和 Fekete 的课程材料转述为：小而稀疏的图用节点连线图更好，大而稠密的图用矩阵更好，路径查找是节点连线图一直占优的任务。（我读到的是转述，没读到论文原文。）

**画不出的东西。** 取决于所选的画法：节点连线图的位置没有含义，矩阵没有合适的排序就读不出模式（Munzner 的课程幻灯片专门强调节点顺序）。

### 多层与复合

**用法。** 层、视角或嵌套本身是模型里的对象；同一对象可出现在多层。〔文〕McGee 等对多层网络可视化的综述指出，二分图、多变量图、动态图都可以看作多层网络的特例：动态图的时间片可以当作层，多变量图里区分类型的属性可以用来划层。它还强调，层“既不是一个子网络，也不只是点或边的属性”，而是进入分析过程的概念对象。

**案例里主要出现在两种形态。**

- 嵌套复合：[CodeBoarding](case-evidence.md#codeboarding)（组件和子组件）、[Reactome](case-evidence.md#reactome)（子通路在上层图里用彩色方框标出）、[Nx](case-evidence.md#nx)（组合节点）。
- 多投影：[SBGN](case-evidence.md#sbgn) 的三种语言、[AFFiNE](case-evidence.md#affine) 的页面与白板、[Nextstrain](case-evidence.md#nextstrain) 的树地图时间三视图。〔案〕

### 序列与事件流（3 个主类，但作为叠加出现很多）

序列几乎总是叠加在别的结构上：运行追踪是“树加时间”，计划与执行是“DAG 加时间”。[Graphiti](case-evidence.md#graphiti) 是一个只有数据模型、没有图形界面的案例：它的边带双时间元数据，可以失效，保留来源。它说明时间有效期和来源要先进数据模型，否则图只能画出“现在”。〔案〕

### 表与多维属性（7）

**回答什么议题。** 探索发现（5）和决策与状态（2）。〔案〕

**重点部分。** 对象上的度量（5）。关系完全不表达或靠属性值相似产生。〔案〕

**两个值得记的做法。**

- 技术雷达只留每项技术的“环”（采用建议）和“象限”（种类），把技术之间的关系整个丢掉。[Thoughtworks 技术雷达](case-evidence.md#thoughtworks-tech-radar)、[Build Your Own Radar](case-evidence.md#build-your-own-radar)（输入就是一张表，列名 name、ring、quadrant、isNew、description 承担角色）。
- [Wikidata 查询服务](case-evidence.md#wikidata-query-views)的结果是一张表，每种视图要求特定的列扮演特定角色：“First will be X-axis, second Y-axis”、气泡图的大小和颜色列、树图的“1st label in a row will be 1st level in tree map”。〔案〕

〔推〕这提示一种选图的办法：先看每个视图需要哪些“角色槽”（位置、大小、颜色、层级、时间），再看数据的列能不能填进去。[Gapminder](case-evidence.md#gapminder) 把五个变量分到位置（两个）、大小、颜色、时间五个通道，一张图同时回答“关系”和“变化”。

### 集合与分类（3）

只有成员和类别，没有成员之间的关系：[CNCF Landscape](case-evidence.md#cncf-landscape)、两个技术雷达。回答“哪类里有谁”，盲区正好是项目之间的依赖。〔案〕

### 流量网络（1）

[LLNL 能源流向图](case-evidence.md#llnl-energy-flow)：边上的量守恒，从资源分到四类终端用途和“被拒绝的能量”（废热）。线宽正比于能量，颜色表示能量形式。设计者说选桑基图是“for its versatility in displaying quantitative information visually”。适合看总体分配，不适合看单个设备或随时间的变化。〔案〕

### 空间与几何（2）

[Embedding Projector](case-evidence.md#embedding-projector)：高维向量投影到二维或三维，重点是群落和位置；设计者承认静态视图不够，要加最近邻列表来检查“nearby points are semantically related”。[Circos](case-evidence.md#circos)：位置本身是含义（基因组坐标）。〔案〕

### 文本与文档

文本不是一种可以直接画的结构，需要先被提取成结构。案例里有三种提取的结果：

- 提取出层级：[Docling](case-evidence.md#docling)（版面、阅读顺序、章节），[Tree-sitter](case-evidence.md#tree-sitter)（语法树）。调研报告提醒这两种“结构”都不等于更高一层的知识结构或架构语义，这是报告的判断，官方页面没有这样写。
- 提取出图：[InfraNodus](case-evidence.md#infranodus) 把词当节点、共现当边，节点大小是介数中心性，颜色是话题群，最后找“结构空白”；[Docling Graph](case-evidence.md#docling-graph) 约束关系类型并保留来源；[GraphRAG](case-evidence.md#graphrag) 提取实体、关系、主张，再做层级聚类并生成各层摘要。
- 提取出论证：[Argdown](case-evidence.md#argdown)（用文本写论证，地图由文本生成）。〔案〕

**一个规律。** 结构是派生出来的时候，视觉通道承载的是算法的输出（中心性、社区、度数），而不是原始数据。InfraNodus 的作者特意说：“The result is not a word cloud: it is a map of relations”。〔案〕GraphRAG 的社区层级是算法聚类，我读到的官方页面没有说它对应认知上的逻辑层级。〔案〕

### 因果与反馈（2）

[Insight Maker](case-evidence.md#insightmaker)：存量、流量、变量、链接，重点是环与度量，用来改变参数看系统行为。[Explorable Explanations](case-evidence.md#explorable-explanations)：把模型嵌进文章，让读者改前提看后果。〔案〕

## 认知结构本身

我另外收了几个“认知结构本身就是研究对象”的案例：[CmapTools 概念图](case-evidence.md#cmaptools)、[图尔敏论证模型](case-evidence.md#toulmin)、[Kialo](case-evidence.md#kialo)、[Argdown](case-evidence.md#argdown)、[Luhmann 的卡片盒](case-evidence.md#zettelkasten)、[Markmap](case-evidence.md#markmap)。它们有几个共同点：

1. **基本单位是命题，不只是节点。** 概念图里“Propositions contain two or more concepts connected using linking words or phrases”；图尔敏模型把论证拆成主张、依据、保证、支撑、限定词、反驳几个角色。〔案〕
2. **边的类型就是内容。** 概念图的连接词、论证里的支持与攻击、图尔敏模型里的“保证”（warrant：依据为什么能推出主张）。图尔敏模型的说法是：“the weakest part of any argument is its weakest warrant”。〔案〕
3. **层级取决于所问的问题。** CmapTools 的作者写道：“it is best to construct concept maps with reference to some particular question we seek to answer, which we have called a focus question”。同一个领域，换一个焦点问题，层级就会变。〔案〕这是对“抽象层级不是对象自带的性质”最直接的案例证据。
4. **跨联被当作创造性的来源。** 层级负责组织，跨联负责连接不同分支。〔案：[CmapTools](case-evidence.md#cmaptools)〕卡片盒有类似提纲或书籍目录的排序结构，有卡片之间的引用，还有关键词索引，同一个主题可以从不同入口进入（“Multiple-Storage-Prinzip”）；编号对应层级位置是我的读法。〔案+推：[卡片盒](case-evidence.md#zettelkasten)，来源是一篇德语的二手分析〕
5. **向下可追溯。** Docling 和 Graphiti 保留来源；卡片盒里先前的内容被后来的条目“修订而没有消除”（德语原文：“durch spätere Eintragungen revidiert, nicht aber eliminiert wurden”，同样是二手分析）；Wikipedia 的摘要式写作要求每个子文章“is a complete encyclopedic article in its own right”。〔案〕分层写作的部分见 [分层写作](layered-writing.md)。

## 还没有解决的

- 语料偏工程工具。想检验结论是否站得住，需要更多“复杂信息和认知结构”类的案例，尤其是非软件领域里设计者写下了理由的案例。
- “重点部分”的词表（13 项）是我按案例归纳出来的，没有被别人用过；换一个人来编码，同一个案例可能落在不同的重点上。方法文档里列了这个限制。
- 没有读到论文原文的：Ghoniem 等的受控实验、McGuffin 的家谱图论文（读到的是作者主页的 PDF，课程材料只用作旁证）。
