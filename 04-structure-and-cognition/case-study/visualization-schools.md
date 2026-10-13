# 可视化流派

回答的问题：同一份结构，大家实际用哪几种画法；每种画法押注什么、放弃什么；哪些画法常常搭配；画法和数据结构、重点部分、结构来源之间是什么关系。

## 这份文档怎么来的

和 [信息结构理论](information-structure-theory.md) 一样，从案例归纳，不从图表手册演绎。2026-10-13 对当时的全部 84 个案例做了第二轮编码，之后新增的 13 个案例按同一词表编码，现在共 97 个（见 [案例分析的方法](method.md)）：在原来的“数据结构”“重点部分”之外，给每个案例加了两项——

- **画法流派**（`schools`）：案例的视图主要用哪种方式把重点画出来，可以同时用几种，主要的放第一位；
- **结构来源**（`source`）：这份结构是怎么进到系统里的。

“流派”在这里的意思是：**在不同领域里反复出现的一种画法，它把结构的重点部分映射到同一类视觉构件上，并且有明说的取舍（保留什么、放弃什么）。** 八个流派的名字和边界是我从案例里归纳的，不是文献里现成的分类；文献里相近的说法只作旁证（例如 Schulz 等区分用连线表达层级的“显式”画法和用包含、重叠表达的“隐式”画法，大致对应下面的连线图和包含与面积图）。

结论后面的证据标记：〔案〕来自案例表，能点回具体案例和官方原文；〔文〕来自我读过的文献；〔推〕整理者的推断。

**编码的可靠性。** 这一轮编码仍是我一个人做的。为了看词表是否只有我自己读得懂，我另让 Haiku 子智能体**只看官方原文摘录和词表**、不看我的编码，对当时的 84 个案例独立编了一遍（Madge 的原文摘录是空的，不计，所以是 83 个）。下面是改正我自己的错**之前**的一致率：

| 编码项 | 首位标签一致率 | Cohen’s κ | 我的首位标签出现在对方的标签里 |
| --- | --- | --- | --- |
| 主类结构 | 80% | 0.74 | 93% |
| 首位重点部分 | 67% | 0.61 | 89% |
| 主流派 | 83% | 0.78 | 88% |
| 首位来源 | 84% | 0.79 | 90% |

读法：一致率中等偏高，不一致多半是**主次顺序**不同（右列比左列高得多），其次是摘录没写画法时对方只能推断（对方在 `unsure` 里最常写的一句）。**重点部分的 κ 最低**，说明这个词表是四项里最不稳的，凡是依赖它的结论都要打折扣。需要提醒：盲编者看得到词表里的定义，而定义里写了我的几条规则（例如“页面没写是否有环的流程画布，按一般图编码”），一致率因此偏高；而且摘录是我在第一轮编码时一起读过的，不是完全独立的材料。

后补的 13 个案例也做了一次盲编（盲编者仍只看摘录，看不到我打开页面时的所见）：主类结构 85%（κ = 0.77），首位重点部分 77%（κ = 0.69），**主流派只有 54%（κ = 0.41）**，首位来源 77%（κ = 0.32，边缘分布偏斜，κ 偏低）。主流派一致率低，主要因为这批案例的官方文字很少写画法，我是打开页面、看了截图才编的，盲编者只能推断；所以这 13 个案例的流派编码比前 84 个更依赖我的判断，也更可能被别人编成别的样子。

盲编也帮我找到了 5 处自己的错（前 84 个案例里）：DataHub、OpenMetadata、Nextstrain 的原文明写了解析、摄取、推断（“SQL query parsing that automatically extracts transformation logic and column-level dependencies”），我先前保守地把来源编成了现成数据，已改为“算出来的”；Graphiti 的原文没有任何视图，不该编流派，已清空；通用依存（UD）的查看器画出了依存关系，已把画法改为列表与文字 + 连线图。没有改的分歧：矩形树图的来源（我编现成数据，对方编算出来的，因为面积是向上累加的）等，边界本来就模糊。

语料的偏向要先说在前面：97 个案例里，69 个来自软件、AI、数据平台和开源生态（其中 56 个是本库收的项目，13 个是最后补入的开源生态地图、分类与知识图谱），28 个来自其他领域（交通、生物、能源、金融、语言学、论证、写作等）。下面凡是只出现在软件或 AI 运维案例里的画法，都会注明。

## 三个独立的问题

一份结构被画出来之前，要回答三个问题，它们的答案之间只有弱关联：

| 问题 | 选项 | 在哪里讲 |
| --- | --- | --- |
| 材料被当成什么结构？ | 集合、表、层级、有向无环图、一般图、命题与论证、序列、流量、空间、因果（10 类） | [信息结构理论](information-structure-theory.md) |
| 这份结构从哪来？ | 手工建构、运行记录、算出来的、现成数据（4 种） | 本文“结构来源” |
| 用什么画法画？ | 连线图、包含与面积图、时间轴条图、规则布局、通道分配图、示意与隐喻图、列表与文字、记法图（8 个流派） | 本文 |

“弱关联”是量出来的：用留一法，拿一个案例的主结构（或首位重点、首位议题）去预测它的主流派，只用其余案例做统计。结果见下表。随便猜“连线图”也能猜对 42%。

| 用什么预测主流派 | 留一法预测正确率 |
| --- | --- |
| 不用任何信息，总猜连线图 | 0.42 |
| 首位议题 | 0.26 |
| 结构来源（首位） | 0.40 |
| 主类结构 | 0.44 |
| 首位重点部分 | 0.48 |
| 重点 + 议题 | 0.51 |
| 结构 + 来源 | 0.57 |
| 结构 + 议题 | 0.61 |

〔案〕90 个有视图、有重点和议题编码的案例；样本小，几个百分点的差别不能当真。读法：**数据结构、重点部分都只能解释画法的一小部分**，最好的组合（结构 + 议题）也有四成说不准。上一版文档里写的“重点部分比结构类别更决定画法”，这个数据撑不起来：重点部分略好于主类结构，但差距在误差范围内。补入 13 个开源生态地图、分类与知识图谱案例前，主类结构的预测正确率是 0.54，补入后降到 0.44，几乎回到瞎猜的水平：这批案例里同样是“图”“层级”或“空间”的结构，被画成了地图、列表、分类树、查询界面等五花八门的样子。

这说明画法在相当程度上是**设计者面对同一份结构时的选择**，而不是结构逼出来的。下面各节要回答的就是：有哪些选择，各自押注什么。

## 八个流派

| 流派 | 押注什么 | 放弃什么 | 用到的案例数（其中主流派） |
| --- | --- | --- | --- |
| 连线图 | 关系就是线，读者能顺着线走 | 规模：稠密时成“毛球”，位置本身没有含义 | 54（38） |
| 包含与面积图 | 屏幕空间：包含表达“属于”，面积表达量 | 跨分支的关系；面积不易精确比较 | 5（4） |
| 时间轴条图 | 耗时看得见：条的长度是时间，缩进是父子 | 父子以外的依赖关系 | 10（7） |
| 规则布局 | 位置由数据的规则决定，布局可复现、可比较 | 位置的含义要向读者解释；关系类型单一 | 6（6） |
| 通道分配图 | 一张表的列分到位置、大小、颜色、时间等通道 | 对象之间的关系 | 18（13） |
| 示意与隐喻图 | 保留一种性质，舍掉另一种；或借熟悉的东西作隐喻 | 被舍掉的性质（几何距离、精确尺度） | 6（3） |
| 列表与文字 | 结构留在文字里，能读、能搜、能排序 | 结构的整体形状 | 18（11） |
| 记法图 | 意义放在符号里，布局可以自由 | 读者要先学记法；细节被隐藏 | 9（8） |

每个流派的案例清单列了全部用到它的案例（加粗的是主流派）。下表是**主流派**与**主类结构**的交叉计数：同一种结构被画成什么，哪种画法只服务一种结构（时间轴条图的 7 个主流派案例全是层级），哪种画法跨得最广（连线图跨了表、层级、有向无环图、一般图四类）。

<!-- gen:schoolcount:structure -->
| 主流派 \ 主类结构 | 集合与分类 | 表与多维属性 | 层级与树 | 有向无环图 | 一般图与网络 | 命题与论证 | 序列与事件流 | 流量网络 | 空间与几何 | 因果与反馈 | 合计 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 连线图 | · | 1 | 6 | 7 | 24 | · | · | · | · | · | 38 |
| 包含与面积图 | 1 | · | 3 | · | · | · | · | · | · | · | 4 |
| 时间轴条图 | · | · | 7 | · | · | · | · | · | · | · | 7 |
| 规则布局 | 2 | 1 | · | · | 2 | · | · | · | 1 | · | 6 |
| 通道分配图 | 1 | 5 | · | · | 3 | · | 1 | 1 | 2 | · | 13 |
| 示意与隐喻图 | · | · | 1 | · | 1 | · | · | · | 1 | · | 3 |
| 列表与文字 | · | · | 7 | 1 | 1 | 1 | · | · | · | 1 | 11 |
| 记法图 | · | · | 1 | · | 3 | 3 | · | · | · | 1 | 8 |
<!-- /gen -->

### 连线图

对象画成点，关系画成线。**这是默认选择**：54 个案例用到，占 56%；软件、AI 运维和开源生态类案例里有 41/69，其他领域有 13/28，所以这个比例有一部分是语料偏向造成的。〔案〕

**什么时候出现。** 首位重点是关系类（连通与邻域、先后与依赖方向、环、群落）的 45 个案例里，32 个主流派是连线图。〔案〕

**两种布局逻辑。** 同是连线图，布局的含义不同：*流向布局*里方向就是先后或依赖（血缘、工作流、依赖图：Marquez、DataHub、OpenMetadata、bpmn-js、Dify、Flowise），*聚类布局*里靠近表示相关（共现网络、关系网络：InfraNodus、Gephi、VOWL，以及 GraphRAG 在 Gephi 里的图）。我没有给每个案例编码布局逻辑，这个区分来自读案例和看画廊里的截图，不能给出比例。〔案，未量化〕

**代价，设计者自己写的。** 稠密、规模大时失效：“In a hairball, data is subordinate to layout”（Hive Plot）；“graph visualizations are only viable up to a certain size”（VOWL）；“Viewing the entire graph can be unmanageable even for smaller repositories”（Nx）；DataHub 写“the table-level view is getting too busy”；家谱图的作者说传统的大家族图“inevitably contain at least some long edges or nodes displaced far away from their close relatives”。〔案〕

**应对的三条路。** 案例里看到：（一）离开连线图，换成另一个流派（下面的包含与面积图、规则布局）；（二）留在连线图里，但**不一次画全**：聚合再原地展开（Nx 的组合节点：“Composite nodes are essential to navigate a graph of even a moderate size”）、一次只看一个子集（家谱图的双树）、聚焦与淡化（Kumu：“Cut through the clutter using filter, focus and showcase”）；（三）另配一个列表视图（OpenMetadata 把同一批上下游资产列成表，“easier to scan, search, and sort when an asset has a large number of dependencies”）。〔案〕

<details><summary>用到连线图的案例（加粗的是主流派）</summary>

<!-- gen:schoolcases:link -->
- **[dependency-cruiser](data/case-evidence.md#dependency-cruiser)**　软件工程 · 一般图与网络
- **[Madge](data/case-evidence.md#madge)**　软件工程 · 一般图与网络
- **[pydeps](data/case-evidence.md#pydeps)**　软件工程 · 一般图与网络
- **[CodeBoarding](data/case-evidence.md#codeboarding)**　软件工程 · 层级与树+一般图与网络
- **[Understand Anything](data/case-evidence.md#understand-anything)**　软件工程 · 一般图与网络+层级与树
- [LikeC4](data/case-evidence.md#likec4)　软件工程 · 层级与树+一般图与网络 · 同时用：记法图
- **[Nx](data/case-evidence.md#nx)**　软件工程 · 有向无环图+层级与树
- **[Backstage](data/case-evidence.md#backstage)**　软件工程 · 一般图与网络 · 同时用：列表与文字
- [Git 提交历史](data/case-evidence.md#git-history)　版本控制 · 有向无环图 · 同时用：列表与文字
- [Jaeger](data/case-evidence.md#jaeger)　分布式系统运维 · 层级与树+一般图与网络 · 同时用：时间轴条图
- **[Grafana Tempo](data/case-evidence.md#grafana-tempo)**　分布式系统运维 · 层级与树+一般图与网络 · 同时用：时间轴条图
- **[Apache SkyWalking](data/case-evidence.md#skywalking)**　分布式系统运维 · 一般图与网络+层级与树+空间与几何 · 同时用：示意与隐喻图
- **[Kiali](data/case-evidence.md#kiali)**　服务网格运维 · 一般图与网络
- [Grafana](data/case-evidence.md#grafana)　基础设施运维 · 表与多维属性+一般图与网络 · 同时用：通道分配图
- [Comet Opik](data/case-evidence.md#comet-opik)　AI 应用观测 · 层级与树+一般图与网络 · 同时用：时间轴条图
- [LangWatch](data/case-evidence.md#langwatch)　AI 应用观测 · 层级与树+一般图与网络 · 同时用：时间轴条图、通道分配图
- **[Dify](data/case-evidence.md#dify)**　AI Agent 开发 · 一般图与网络
- **[Langflow](data/case-evidence.md#langflow)**　AI Agent 开发 · 一般图与网络
- **[Flowise](data/case-evidence.md#flowise)**　AI Agent 开发 · 一般图与网络
- **[n8n](data/case-evidence.md#n8n)**　业务自动化 · 一般图与网络+序列与事件流 · 同时用：列表与文字
- **[Node-RED](data/case-evidence.md#node-red)**　物联网与事件流 · 一般图与网络
- [bpmn-js](data/case-evidence.md#bpmn-js)　业务流程 · 一般图与网络 · 同时用：记法图
- **[LangGraph / Studio](data/case-evidence.md#langgraph)**　AI Agent 开发 · 一般图与网络+序列与事件流
- **[AgentEnsemble](data/case-evidence.md#agentensemble)**　AI Agent 开发 · 有向无环图+序列与事件流 · 同时用：时间轴条图
- **[AgentEnsemble Viz](data/case-evidence.md#agentensemble-viz)**　AI Agent 开发 · 有向无环图+序列与事件流 · 同时用：时间轴条图
- **[AutoGen / AutoGen Studio](data/case-evidence.md#autogen)**　AI Agent 开发 · 一般图与网络+序列与事件流
- **[diagrams.net / draw.io](data/case-evidence.md#drawio)**　通用绘图 · 一般图与网络 · 同时用：记法图
- **[Kumu](data/case-evidence.md#kumu)**　系统与关系分析 · 一般图与网络
- [Insight Maker](data/case-evidence.md#insightmaker)　系统建模 · 因果与反馈+流量网络 · 同时用：记法图
- **[Marquez](data/case-evidence.md#marquez)**　数据工程 · 有向无环图
- **[DataHub](data/case-evidence.md#datahub)**　数据工程 · 有向无环图
- **[OpenMetadata](data/case-evidence.md#openmetadata)**　数据工程 · 有向无环图 · 同时用：列表与文字
- [NeoDash](data/case-evidence.md#neodash)　图数据库应用 · 一般图与网络 · 同时用：通道分配图
- **[PyGraphistry](data/case-evidence.md#pygraphistry)**　数据分析 · 表与多维属性+一般图与网络
- **[Gephi](data/case-evidence.md#gephi)**　通用网络分析 · 一般图与网络
- **[InfraNodus](data/case-evidence.md#infranodus)**　文本分析与知识发现 · 一般图与网络
- **[Docling Graph](data/case-evidence.md#docling-graph)**　文档处理 · 一般图与网络
- **[Microsoft GraphRAG](data/case-evidence.md#graphrag)**　文本检索与知识建模 · 一般图与网络+层级与树
- **[LightRAG](data/case-evidence.md#lightrag)**　文本检索与知识建模 · 一般图与网络
- [VOWL / WebVOWL 本体可视化](data/case-evidence.md#vowl)　本体与语义网 · 一般图与网络 · 同时用：记法图
- [Universal Dependencies 依存树](data/case-evidence.md#universal-dependencies)　语言学 · 层级与树 · 同时用：列表与文字
- **[Markmap](data/case-evidence.md#markmap)**　知识管理与写作 · 层级与树
- [CmapTools 概念图](data/case-evidence.md#cmaptools)　教育与知识建模 · 命题与论证+层级与树 · 同时用：记法图
- [Argdown](data/case-evidence.md#argdown)　论证与讨论 · 命题与论证 · 同时用：记法图
- **[deps.dev（Open Source Insights）](data/case-evidence.md#deps-dev)**　软件供应链 · 一般图与网络
- **[ATLAS：用多个 LLM Agent 自动构建软件仓库分类体系](data/case-evidence.md#atlas-taxonomy)**　软件仓库分类 · 层级与树
- **[Git.Top Atlas](data/case-evidence.md#git-top-atlas)**　开源生态导航 · 一般图与网络+集合与分类 · 同时用：列表与文字
- **[Nextstrain / Auspice](data/case-evidence.md#nextstrain)**　流行病与基因组 · 层级与树+空间与几何+序列与事件流 · 同时用：通道分配图
- [OneZoom 生命之树](data/case-evidence.md#onezoom)　生物分类 · 层级与树 · 同时用：示意与隐喻图
- **[Reactome 通路浏览器](data/case-evidence.md#reactome)**　分子生物学通路 · 层级与树+一般图与网络 · 同时用：列表与文字
- [SBGN 系统生物学图形标记](data/case-evidence.md#sbgn)　分子生物学通路 · 一般图与网络 · 同时用：记法图
- [伦敦地铁图（Beck）](data/case-evidence.md#tube-map)　交通 · 一般图与网络 · 同时用：示意与隐喻图
- **[ICIJ Offshore Leaks 数据库](data/case-evidence.md#icij-offshore-leaks)**　调查报道与金融 · 一般图与网络 · 同时用：列表与文字
- **[家谱图的交互可视化](data/case-evidence.md#genealogical-graphs)**　谱系与家族史 · 有向无环图
<!-- /gen -->

</details>

**亲眼看：** [Nx 示例项目图](https://nrwl-nx-examples-dep-graph.netlify.app/?focus=cart)、[Kumu 地图](https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative)、[Jaeger 在线演示](https://demo.jaegertracing.io/jaeger/)（单次请求用时间轴条，服务依赖用连线图）。更多见 [案例画廊](data/case-gallery.md)。

### 包含与面积图

用嵌套或相邻的块表达“属于”，用面积或宽度表达量：矩形树图（磁盘占用）、火焰图、分组块（CNCF Landscape）、城市隐喻里的街区（CodeCity）。5 个案例用到，4 个是主流派（3 个层级、1 个集合）；Speculora 另有一个 Treemap 标签（整理者打开所见，官方文字没有说明）。〔案〕

**押注的是屏幕空间。** 矩形树图的设计史：“Tree structured node-link diagrams grew too large to be useful”，换成包含之后能“see tens of thousands of nodes in a fixed space”。火焰图作者的出发点是“The regular profilers/tracers had produced walls of text”。〔案〕

**放弃的东西，设计者都写了。**

- 时间顺序：火焰图“I ditched time on the x-axis”，横轴“sorted alphabetically (it is not the passage of time)”，为的是让相同的调用路径合并后宽度可比。〔案〕
- 精确的面积比较：矩形树图作者承认“encoding a linear variable such as file size as an area was breaking a graphic design guideline”。〔案〕
- 关系：CodeCity 默认不画调用与继承，并写“We currently do not display the class internals”。〔案〕

〔文〕Schulz 等把层级的表示分为显式（连线）和隐式（包含、重叠、相邻），指出“any hierarchy can be represented by nested sets”；这个流派就是隐式画法在案例里的样子。

<details><summary>用到包含与面积图的案例</summary>

<!-- gen:schoolcases:enclosure -->
- **[CodeCity](data/case-evidence.md#codecity)**　软件演化与度量 · 层级与树+表与多维属性 · 同时用：示意与隐喻图
- **[火焰图](data/case-evidence.md#flame-graph)**　性能剖析 · 层级与树
- **[Treemap（磁盘空间）](data/case-evidence.md#treemap-diskspace)**　文件系统与资源占用 · 层级与树
- **[CNCF Landscape](data/case-evidence.md#cncf-landscape)**　技术生态 · 集合与分类
- [Speculora](data/case-evidence.md#speculora)　市场需求分析 · 层级与树+表与多维属性 · 同时用：列表与文字
<!-- /gen -->

</details>

### 时间轴条图

横轴是时间，条的长度是耗时，缩进表达父子：trace 的瀑布图、时间线。10 个案例用到，7 个是主流派；**主流派的 7 个全部是“层级 + 时间”的运行追踪，首位议题全是定位异常。**〔案〕

**为什么。** AgentPrism 的作者的说法：问题是“The answer is buried within a terrible wall of JSON logs”，而且“loops invisible in JSON become glaringly clear when made visual”；选树视图的理由是渐进披露让深层结构“navigable”。LangWatch 干脆把同一次运行画成四种：“Waterfall, flame graph, topology, and sequence diagram, whichever way you need to read a run.”〔案〕

**放弃的东西。** 父子以外的依赖。所以追踪类产品几乎都另配一个连线图：Jaeger 和 Tempo 配服务依赖图，AgentEnsemble 配任务依赖图（Flow 视图不画时间，Timeline 视图不画依赖箭头）。〔案〕

**要注意的偏向。** 这 10 个案例**全部**来自软件、AI 开发与运维；本库没有非软件领域的时间轴条案例（甘特图、历史时间线之类），所以这个流派能不能推到别的领域，案例里没有答案。〔案〕

<details><summary>用到时间轴条图的案例</summary>

<!-- gen:schoolcases:timebar -->
- **[Jaeger](data/case-evidence.md#jaeger)**　分布式系统运维 · 层级与树+一般图与网络 · 同时用：连线图
- [Grafana Tempo](data/case-evidence.md#grafana-tempo)　分布式系统运维 · 层级与树+一般图与网络 · 同时用：连线图
- **[AgentPrism](data/case-evidence.md#agentprism)**　AI Agent 观测 · 层级与树+序列与事件流
- **[Langfuse](data/case-evidence.md#langfuse)**　AI 应用观测 · 层级与树+表与多维属性 · 同时用：通道分配图
- **[Arize Phoenix](data/case-evidence.md#arize-phoenix)**　AI 应用观测 · 层级与树+序列与事件流
- **[Comet Opik](data/case-evidence.md#comet-opik)**　AI 应用观测 · 层级与树+一般图与网络 · 同时用：连线图
- **[AgentOps](data/case-evidence.md#agentops)**　AI 应用观测 · 层级与树+序列与事件流
- **[LangWatch](data/case-evidence.md#langwatch)**　AI 应用观测 · 层级与树+一般图与网络 · 同时用：连线图、通道分配图
- [AgentEnsemble](data/case-evidence.md#agentensemble)　AI Agent 开发 · 有向无环图+序列与事件流 · 同时用：连线图
- [AgentEnsemble Viz](data/case-evidence.md#agentensemble-viz)　AI Agent 开发 · 有向无环图+序列与事件流 · 同时用：连线图
<!-- /gen -->

</details>

**亲眼看：** [Jaeger 在线演示](https://demo.jaegertracing.io/jaeger/)、[AgentPrism](https://agent-prism.evilmartians.io/)。

### 规则布局

位置由数据的规则决定，而不是物理模拟的结果：设计结构矩阵（行列排序）、Hive Plot（辐射状轴）、Circos（环形坐标）、技术雷达（环与象限）。6 个案例，都是主流派。〔案〕

**押注的是可复现、可比较。** Hive Plot：“Hive plots make it possible to assess network structure because they are founded on network properties, not on aesthetic layout.” 设计结构矩阵：“highly compact, easily scalable, and intuitively readable”，而且重排行列就能暴露环和模块。Circos 的出发点是“multitudes of lines transgress unrelated ideograms and make patterns very difficult to discern”，所以把线性坐标首尾相接成环。〔案〕

**放弃的东西。** 位置的含义要向读者解释：Hive Plot 自己写“The axis and node mapping is arbitrary”；设计结构矩阵一张图只能放一种关系、一个领域（“A DSM always only contains elements from one domain”）；Circos 的全基因组视图“precludes the display of individual small-scale events at their native scale”。技术雷达放弃的是技术之间的全部关系。〔案〕

**两类东西挤在这个流派里。** 一类是把**一般图**从毛球里救出来的（矩阵、Hive Plot、Circos），一类是把**集合**按类别放进固定的环和象限的（三个技术雷达）。它们共有的动作是“用规则槽位代替自由布局”，但处理的结构不同；是否该拆成两个流派，我拿不准。〔推〕

<details><summary>用到规则布局的案例</summary>

<!-- gen:schoolcases:rulepos -->
- **[设计结构矩阵 DSM](data/case-evidence.md#dsm)**　工程系统与产品架构 · 一般图与网络
- **[Hive Plot](data/case-evidence.md#hive-plot)**　网络分析（生物与社会网络） · 一般图与网络
- **[Thoughtworks Technology Radar](data/case-evidence.md#thoughtworks-tech-radar)**　技术生态 · 集合与分类
- **[Zalando Tech Radar](data/case-evidence.md#zalando-tech-radar)**　技术生态 · 集合与分类
- **[Build Your Own Radar](data/case-evidence.md#build-your-own-radar)**　技术生态 · 表与多维属性+集合与分类
- **[Circos](data/case-evidence.md#circos)**　比较基因组 · 空间与几何+一般图与网络
<!-- /gen -->

</details>

**亲眼看：** [Hive Plot（Bostock 的实现）](https://bost.ocks.org/mike/hive/)、[Zalando 技术雷达](https://opensource.zalando.com/tech-radar/)。设计结构矩阵的示例图见 [案例画廊](data/case-gallery.md) 里的 DSM 条目。

### 通道分配图

把一张表的列分配给位置、大小、颜色、时间、宽度等视觉通道：气泡图、柱线图、桑基图、仪表盘面板、投影散点。18 个案例用到，13 个是主流派；其中 5 个的主结构是表；首位重点多数是对象上的度量（7 个）。新补入的有 Open Source AI Gap Map（类别列表里的成熟度徽章、缺口标记和产品色块）、OpenDigger（Playground 里的指标柱线图）。〔案〕

**做法的核心是“角色槽”。** Wikidata 的每种视图都规定它要的列：第一列是 X 轴、第二列是 Y 轴，气泡图另有大小和颜色列；Gapminder 把五个变量分到位置（两个）、大小、颜色、时间五个通道，一张图同时回答“关系”和“变化”。Grafana 的面板是“查询 + 一种可视化”。〔案〕

**放弃的东西。** 对象之间的关系，以及通道的数量上限。Embedding Projector 的作者认为光有投影不够：“these static views are generally inadequate for exploring high-dimensional data”，所以加了最近邻列表等面板；Ladder of Abstraction 指出汇总有代价：“We can no longer see the car!”〔案〕

<details><summary>用到通道分配图的案例</summary>

<!-- gen:schoolcases:channels -->
- **[Grafana](data/case-evidence.md#grafana)**　基础设施运维 · 表与多维属性+一般图与网络 · 同时用：连线图
- [Langfuse](data/case-evidence.md#langfuse)　AI 应用观测 · 层级与树+表与多维属性 · 同时用：时间轴条图
- [LangWatch](data/case-evidence.md#langwatch)　AI 应用观测 · 层级与树+一般图与网络 · 同时用：时间轴条图、连线图
- **[NeoDash](data/case-evidence.md#neodash)**　图数据库应用 · 一般图与网络 · 同时用：连线图
- **[Embedding Projector](data/case-evidence.md#embedding-projector)**　机器学习 · 空间与几何
- **[Wikidata Query Service 结果视图](data/case-evidence.md#wikidata-query-views)**　开放知识图谱 · 表与多维属性
- [Explorable Explanations](data/case-evidence.md#explorable-explanations)　交互式写作 · 因果与反馈 · 同时用：列表与文字
- **[Up and Down the Ladder of Abstraction](data/case-evidence.md#ladder-of-abstraction)**　交互式写作与抽象 · 序列与事件流+因果与反馈
- **[Open Source AI Gap Map](data/case-evidence.md#oss-ai-gap-map)**　开源生态评估 · 集合与分类+表与多维属性 · 同时用：列表与文字
- **[OSS Insight](data/case-evidence.md#oss-insight)**　开源生态 · 表与多维属性+序列与事件流
- **[OSS Compass](data/case-evidence.md#oss-compass)**　开源生态 · 表与多维属性
- **[OpenDigger](data/case-evidence.md#opendigger)**　开源活动指标 · 一般图与网络+序列与事件流
- **[Semantic Map of GitHub](data/case-evidence.md#semantic-map-github)**　开源生态地图 · 空间与几何 · 同时用：示意与隐喻图
- [Map of GitHub](data/case-evidence.md#map-of-github)　开源生态地图 · 空间与几何 · 同时用：示意与隐喻图
- **[CodeGraph（面向源代码的开放分类知识图谱）](data/case-evidence.md#codegraph)**　代码知识图谱 · 一般图与网络+层级与树
- [Nextstrain / Auspice](data/case-evidence.md#nextstrain)　流行病与基因组 · 层级与树+空间与几何+序列与事件流 · 同时用：连线图
- **[LLNL 美国能源流向图](data/case-evidence.md#llnl-energy-flow)**　能源 · 流量网络
- **[Gapminder 气泡图](data/case-evidence.md#gapminder)**　国际发展统计 · 表与多维属性+序列与事件流
<!-- /gen -->

</details>

**亲眼看：** [Gapminder Tools](https://www.gapminder.org/tools/)、[Wikidata 查询服务](https://query.wikidata.org/)、[Embedding Projector](https://projector.tensorflow.org/)。

### 示意与隐喻图

有意保留一种性质、舍掉另一种，或借熟悉的东西作隐喻：伦敦地铁图（保留连通与换乘，舍掉地理距离）、CodeCity（城市里的街区和楼）、OneZoom（整棵树放在一页，用缩放看细节）、SkyWalking 的三维基础设施地图。另有两张 GitHub 地图（Semantic Map of GitHub、Map of GitHub）。6 个案例用到，3 个是主流派（地铁图、OneZoom、Map of GitHub）；**案例仍然偏少，不足以当作稳定的流派**，放在这里是因为它们的取舍都写得很清楚。〔案〕

- 地铁图：视图完全服务于“连通与换乘”，代价是不能用它估距离。〔案〕
- CodeCity：“A city, with its downtown area and its suburbs is a familiar notion with a clear concept of orientation.” 借的是读者已有的空间认知。〔案〕
- 两张 GitHub 地图：位置不是地理，而是算出来的“相近”，而且**算法不同，分出来的组不同**。Semantic Map of GitHub 按 README 内容算（“positioned by the semantic similarity of their README files”），方法页明说它和按关注关系算的做法“The two approaches produce meaningfully different groupings”，并提醒“inter-cluster distances should not be read as precise measurements of dissimilarity”；Map of GitHub 按共同 Star 的用户算（“Two dots within the same cluster are usually close to each other if multiple users frequently gave stars to both projects”），并把聚类叫“countries”，“国家”“地图”的叫法是页面自己的隐喻。〔案〕
- OneZoom：作者的出发点是批评“paper paradigm”，核心概念是“all the data is on one page so that all the user has to do is zoom to reveal it”；局限是“The natural view emphasizes tree balance over rates of diversification.”〔案〕

### 列表与文字

结构留在文字里：缩进列表、分栏、日志、正文里的链接、卡片。18 个案例用到，11 个是主流派。〔案〕

**它常常不是主角，而是补充视图。** 和连线图搭配出现 8 次：OpenMetadata 的影响分析表、Backstage 的目录表、ICIJ 的结果列表、Reactome 的事件层级列表、n8n 的执行列表、通用依存的查看器、Git.Top Atlas 的生态卡片列表、Git 的 `log`（加 `--graph` 才画出分叉）。补上的是“便于扫描、搜索、排序”和“精确的文字”。〔案〕

**作为主角的时候**，它们的共同点是读者要**读内容**而不是**看形状**：Kialo 把论点按赞成、反对分栏；Wikipedia 的摘要式写作用正文里的“主条目”链接连接上下两层，理由是“Summary style keeps the reader from being overwhelmed by too much information up front”；Tree-sitter 的游乐场把树和代码互相定位；Speculora 的领域页把任务按机会分数排序成列表。〔案〕

**放弃的东西。** 结构的整体形状。Git 的提交历史是有分叉有合并的 DAG，默认视图却是按时间倒序的一维列表，要加 `--graph` 才露出结构。〔案〕

<details><summary>用到列表与文字的案例</summary>

<!-- gen:schoolcases:textlist -->
- **[Tree-sitter](data/case-evidence.md#tree-sitter)**　软件工程 · 层级与树
- [Backstage](data/case-evidence.md#backstage)　软件工程 · 一般图与网络 · 同时用：连线图
- **[Git 提交历史](data/case-evidence.md#git-history)**　版本控制 · 有向无环图 · 同时用：连线图
- [n8n](data/case-evidence.md#n8n)　业务自动化 · 一般图与网络+序列与事件流 · 同时用：连线图
- **[AgentScope 2.0](data/case-evidence.md#agentscope)**　AI Agent 开发 · 层级与树+序列与事件流
- [OpenMetadata](data/case-evidence.md#openmetadata)　数据工程 · 有向无环图 · 同时用：连线图
- **[Docling](data/case-evidence.md#docling)**　文档处理 · 层级与树
- **[Universal Dependencies 依存树](data/case-evidence.md#universal-dependencies)**　语言学 · 层级与树 · 同时用：连线图
- **[AFFiNE](data/case-evidence.md#affine)**　知识管理 · 层级与树+空间与几何
- **[Luhmann 的卡片盒](data/case-evidence.md#zettelkasten)**　知识管理与写作 · 一般图与网络+层级与树
- **[Kialo 论证树](data/case-evidence.md#kialo)**　论证与讨论 · 命题与论证+层级与树
- **[Wikipedia 摘要式写作](data/case-evidence.md#wikipedia-summary-style)**　百科写作 · 层级与树
- **[Explorable Explanations](data/case-evidence.md#explorable-explanations)**　交互式写作 · 因果与反馈 · 同时用：通道分配图
- [Open Source AI Gap Map](data/case-evidence.md#oss-ai-gap-map)　开源生态评估 · 集合与分类+表与多维属性 · 同时用：通道分配图
- [Git.Top Atlas](data/case-evidence.md#git-top-atlas)　开源生态导航 · 一般图与网络+集合与分类 · 同时用：连线图
- **[Speculora](data/case-evidence.md#speculora)**　市场需求分析 · 层级与树+表与多维属性 · 同时用：包含与面积图
- [Reactome 通路浏览器](data/case-evidence.md#reactome)　分子生物学通路 · 层级与树+一般图与网络 · 同时用：连线图
- [ICIJ Offshore Leaks 数据库](data/case-evidence.md#icij-offshore-leaks)　调查报道与金融 · 一般图与网络 · 同时用：连线图
<!-- /gen -->

</details>

### 记法图

先规定一套形状、线型、颜色的含义，再按它画：BPMN、SBGN、VOWL、C4（LikeC4）、图尔敏模型、Argdown 的论证图、概念图、系统动力学的存量流量图，另有通用绘图工具 draw.io。9 个案例用到，8 个是主流派。〔案〕

**押注的是“意义放在符号里”。** 因此布局可以自由，同一份模型可以画出几张图：SBGN 明说三种语言是“three alternative projections of the underlying, more complex biological information”；LikeC4 让多个视图从同一份模型继承范围；bpmn-js 把图形层和 BPMN 元模型分成两层来设计。〔案〕

**这个流派的案例几乎都是“人来建或来讲”，不是“人来查”。** 9 个案例里，议题（含次要议题）是构建编辑、讲解传达、论证推理、推演仿真、建立全貌，**没有一个涉及定位异常或影响范围**；8 个的结构来源是手工建构，另 1 个（VOWL）是把现成的 OWL 本体画出来。〔案〕

**放弃的东西。** 读者要先学记法：VOWL 的出发点是已有的尝试“require knowledge about UML”，所以另造一套不需要 UML 知识的画法；细节被隐藏：Argdown 写“This map hides a lot of the logical details”，要点 “Source” 才回到原文；SBGN 的活动流语言“omits information about the state transitions”。〔案〕

<details><summary>用到记法图的案例</summary>

<!-- gen:schoolcases:notation -->
- **[LikeC4](data/case-evidence.md#likec4)**　软件工程 · 层级与树+一般图与网络 · 同时用：连线图
- **[bpmn-js](data/case-evidence.md#bpmn-js)**　业务流程 · 一般图与网络 · 同时用：连线图
- [diagrams.net / draw.io](data/case-evidence.md#drawio)　通用绘图 · 一般图与网络 · 同时用：连线图
- **[Insight Maker](data/case-evidence.md#insightmaker)**　系统建模 · 因果与反馈+流量网络 · 同时用：连线图
- **[VOWL / WebVOWL 本体可视化](data/case-evidence.md#vowl)**　本体与语义网 · 一般图与网络 · 同时用：连线图
- **[CmapTools 概念图](data/case-evidence.md#cmaptools)**　教育与知识建模 · 命题与论证+层级与树 · 同时用：连线图
- **[Argdown](data/case-evidence.md#argdown)**　论证与讨论 · 命题与论证 · 同时用：连线图
- **[图尔敏论证模型](data/case-evidence.md#toulmin)**　论证与写作 · 命题与论证
- **[SBGN 系统生物学图形标记](data/case-evidence.md#sbgn)**　分子生物学通路 · 一般图与网络 · 同时用：连线图
<!-- /gen -->

</details>

**亲眼看：** [bpmn-js 在线编辑器](https://demo.bpmn.io/)、[Argdown 沙盒](https://argdown.org/sandbox/)、[SBGN 示例](https://sbgn.github.io/examples)。

## 流派和重点部分、议题的对应

<!-- gen:schoolcount:focus -->
| 主流派 \ 首位重点 | 有什么 | 包含与层次 | 连通与邻域 | 先后与依赖方向 | 环与反馈 | 对象上的度量 | 关系上的类型与量 | 时间与演化 | 跨视图的同一对象 | 群落与相似 | 空间位置 | 总体分布 | 合计 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 连线图 | · | 4 | 17 | 11 | 2 | · | · | · | 2 | 2 | · | · | 38 |
| 包含与面积图 | 1 | 3 | · | · | · | · | · | · | · | · | · | · | 4 |
| 时间轴条图 | · | 3 | · | · | · | · | · | 4 | · | · | · | · | 7 |
| 规则布局 | · | · | 1 | 1 | · | 3 | · | · | · | · | 1 | · | 6 |
| 通道分配图 | · | · | 1 | · | · | 7 | 1 | 1 | · | 1 | 1 | 1 | 13 |
| 示意与隐喻图 | · | 1 | 1 | · | · | · | · | · | · | 1 | · | · | 3 |
| 列表与文字 | · | 5 | 1 | 1 | · | 1 | 2 | · | 1 | · | · | · | 11 |
| 记法图 | · | 2 | 2 | 2 | 1 | · | 1 | · | · | · | · | · | 8 |
<!-- /gen -->

从上表和案例里能读出的规律（〔案〕；样本小，只作线索）：

- **重点是对象上的度量：** 首位重点是它的 11 个案例里，7 个画成通道分配图，3 个画成规则布局（技术雷达），1 个画成列表与文字（Speculora 的排序列表）。重点在度量上时，案例里没有连线图。
- **重点是关系（连通、先后、环、群落）：** 连线图占 45 个案例里的 32 个。
- **重点是时间：** 首位重点是时间的 5 个案例里 4 个画成时间轴条图，另 1 个是通道分配图（Ladder of Abstraction 的小多图）。
- **重点是包含与层次：** 18 个案例分散在六种画法里（列表与文字 5，连线图 4，时间轴条图 3，包含与面积图 3，记法图 2，示意与隐喻图 1）——**层级是画法最不唯一的一类结构。**这不是我预期的结果：我原先以为层级会集中在矩形树图一族。

<!-- gen:schoolcount:issue -->
| 主流派 \ 首位议题 | 定位异常 | 影响范围 | 建立全貌 | 追踪流向 | 比较 | 决策与状态 | 探索发现 | 论证推理 | 推演仿真 | 构建编辑 | 讲解传达 | 检索召回 | 合计 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 连线图 | 7 | 5 | 7 | 1 | · | · | 8 | · | · | 8 | · | 2 | 38 |
| 包含与面积图 | 2 | · | 1 | · | · | · | 1 | · | · | · | · | · | 4 |
| 时间轴条图 | 7 | · | · | · | · | · | · | · | · | · | · | · | 7 |
| 规则布局 | · | · | 1 | · | 1 | 3 | 1 | · | · | · | · | · | 6 |
| 通道分配图 | · | · | · | 1 | · | 3 | 7 | · | · | 1 | · | 1 | 13 |
| 示意与隐喻图 | · | · | 1 | · | · | · | 2 | · | · | · | · | · | 3 |
| 列表与文字 | · | · | 1 | 1 | · | 1 | 1 | 1 | · | 3 | 3 | · | 11 |
| 记法图 | · | · | 1 | · | · | · | · | 2 | 1 | 2 | 2 | · | 8 |
<!-- /gen -->

- 时间轴条图的 7 个主流派案例首位议题全是定位异常；记法图里没有任何一个涉及定位异常或影响范围；通道分配图的 13 个里 7 个是探索发现。〔案〕

## 流派怎么搭配

一个案例用到不止一个流派的有 35 个。常见的搭配，每一对都可以读成“一个视图丢了什么，另一个视图补上”：

<!-- gen:schoolpairs: -->
| 搭配 | 案例数 | 案例 |
| --- | --- | --- |
| 连线图 + 记法图 | 8 | LikeC4、bpmn-js、diagrams.net / draw.io、Insight Maker、VOWL / WebVOWL 本体可视化、CmapTools 概念图、Argdown、SBGN 系统生物学图形标记 |
| 连线图 + 列表与文字 | 8 | Backstage、Git 提交历史、n8n、OpenMetadata、Universal Dependencies 依存树、Git.Top Atlas、Reactome 通路浏览器、ICIJ Offshore Leaks 数据库 |
| 连线图 + 时间轴条图 | 6 | Jaeger、Grafana Tempo、Comet Opik、LangWatch、AgentEnsemble、AgentEnsemble Viz |
| 连线图 + 通道分配图 | 4 | Grafana、LangWatch、NeoDash、Nextstrain / Auspice |
| 连线图 + 示意与隐喻图 | 3 | Apache SkyWalking、OneZoom 生命之树、伦敦地铁图（Beck） |
| 时间轴条图 + 通道分配图 | 2 | Langfuse、LangWatch |
| 通道分配图 + 列表与文字 | 2 | Explorable Explanations、Open Source AI Gap Map |
| 通道分配图 + 示意与隐喻图 | 2 | Semantic Map of GitHub、Map of GitHub |
| 包含与面积图 + 示意与隐喻图 | 1 | CodeCity |
| 包含与面积图 + 列表与文字 | 1 | Speculora |
<!-- /gen -->

- 连线图 + 记法图：记法规定符号，连线图规定位置；这一对出现最多（与“连线图 + 列表与文字”并列），因为大多数记法（BPMN、SBGN、VOWL、概念图）本来就是画在节点连线上的。
- 连线图 + 时间轴条图：一个管关系，一个管时间。追踪类产品的标准配置。
- 连线图 + 列表与文字：图用来看形状，表用来扫描和排序。
- 同一个对象要在几个视图里保持可对应：Nextstrain 用一致的颜色把树、地图、时间连起来，“Multiple views into different facets of the data are presented and remain in sync as one interacts with the data.”〔案〕

## 结构来源和画法

<!-- gen:schoolcount:source -->
| 主流派 \ 首位来源 | 手工建构 | 运行记录 | 算出来的 | 现成数据 | 合计 |
| --- | --- | --- | --- | --- | --- |
| 连线图 | 11 | 5 | 18 | 4 | 38 |
| 包含与面积图 | · | · | 2 | 2 | 4 |
| 时间轴条图 | · | 7 | · | · | 7 |
| 规则布局 | 3 | · | · | 3 | 6 |
| 通道分配图 | 2 | 2 | 5 | 4 | 13 |
| 示意与隐喻图 | 1 | · | 1 | 1 | 3 |
| 列表与文字 | 6 | 2 | 3 | · | 11 |
| 记法图 | 7 | · | · | 1 | 8 |
<!-- /gen -->

- **算出来的结构，大多画成连线图：** 首位来源是“算出来的”的 33 个案例里，18 个画成连线图（代码依赖图、文本抽取出的知识图、从表构造的图、仓库分类树），5 个画成通道分配图，3 个画成列表与文字。〔案〕〔推〕一种解释：抽取、解析、聚合的产出本来就是实体和关系，最直接的呈现是连线；这时视觉通道承载的是算法的输出（中心性、社区、度数），而不是原始数据。InfraNodus 的作者特意说：“The result is not a word cloud: it is a map of relations”。
- **运行记录，画成时间轴条图或连线图：** 19 个里 7 个是时间轴条图，5 个是连线图，列表与文字、通道分配图各 2 个。
- **手工建构的，画成连线图（11）、记法图（7）、列表与文字（6）：** 共 30 个。人建的结构需要被读者理解和修改，所以记法和文字多。〔推〕
- **现成数据**（15 个）里，通道分配图 4、连线图 4、规则布局 3（Build Your Own Radar、Hive Plot、Circos）、包含与面积图 2。

## 每个流派都是对默认画法某个失效点的回应吗

设计者在官方页面或论文里写了自己理由的有 41 个案例，其中 29 个还写了“原来的做法有什么问题”（`alternative`）。把这些话摆在一起：

| 原来的做法 | 失效在哪里（设计者原话） | 他们换成了 |
| --- | --- | --- |
| 节点连线图 | “Tree structured node-link diagrams grew too large to be useful”（矩形树图）；“In a hairball, data is subordinate to layout”（Hive Plot）；“multitudes of lines transgress unrelated ideograms”（Circos） | 包含与面积图；规则布局 |
| 原始日志与文字 | “The answer is buried within a terrible wall of JSON logs”（AgentPrism）；“The regular profilers/tracers had produced walls of text”（火焰图） | 时间轴条图；包含与面积图 |
| 需要先学的记法 | “they require knowledge about UML”（VOWL） | 自带说明的记法（仍是记法图） |
| 静态视图 | “these static views are generally inadequate for exploring high-dimensional data”（Embedding Projector） | 带最近邻等面板的通道图 |
| 扁平的标签 | “GitHub Topics, the dominant organizational mechanism, is flat, inconsistent, and covers only 67% of projects.”（ATLAS） | 多层、带定义和拆分理由的分类树（连线图里的树） |
| 只看关注量（Star）判断相近 | “Repository stars can provide a useful signal when better data is unavailable, but they are not treated as equivalent to real usage.”（Open Source AI Gap Map）；“This project instead uses a content-based signal.”（Semantic Map of GitHub） | 按直接使用信号评估；按 README 内容算距离 |
| 为纸设计的版面 | “the “paper paradigm””（OneZoom） | 整棵树一页加缩放 |
| 只读的文章 | “displays the author's argument, and nothing else”（可探索的解释） | 能改参数的文字 |

〔案〕〔推〕这张表读起来像“每个流派是对一个具体失效的回应”，但要小心：**这 29 个案例本来就是挑出来的、设计者写了理由的案例**，写“原来的问题”的人当然在讲失效；没写理由的案例（多数是产品）是否同样如此，案例里没有证据。

## 局限，以及没有案例支撑的

- **一个人编码，外加一次盲编。** 一致率见开头；重点部分最不稳。
- **语料偏向。** 时间轴条图只出现在软件、AI 运维案例里；连线图占比在这类案例里更高。非软件领域的案例只有 28 个，各流派在其中分布更均匀：连线图 13，列表与文字 8，通道分配图 6，记法图 4，示意与隐喻图 3，规则布局 3，包含与面积图 3，时间轴条图 0。
- **小流派不稳。** 示意与隐喻图只有 6 个案例（主流派 3 个），包含与面积图只有 5 个（主流派 4 个）。
- **后补的 13 个案例没有参与第一次画法归纳。** 它们是用户发来的一份调研里提到的项目，按同一词表编码、另做了一次盲编；它们让“结构预测画法”的正确率明显下降（见上文）。一种可能是：前 84 个案例里看到的规律有一部分是那批案例的特点，不是普遍的。〔推〕
- **边界有争议的：** 规则布局与通道分配图（技术雷达、散点算哪边）；记法图与连线图（记法画在连线上）；示意与隐喻图与包含与面积图（CodeCity 两边都占）。
- **文献里常见、本库没有案例支撑的画法**，这里不下结论：地理地图、小多图、弧线图、弦图作为独立的案例、层次化的 UML 类图。需要的话要先收案例。
- **“设计者为什么这样画”不是“这样画更好”的证据。** 画法效果的受控比较，本库只用到了节点连线图与矩阵那一组，而且读到的是转述（见 [怎么选画法](../../01-theory/choosing-views.md)）。
