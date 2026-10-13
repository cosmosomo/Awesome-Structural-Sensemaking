# 怎么选画法：按结构和重点部分

回答的问题：面对一种结构、一个要回答的问题，用什么画法展示认知最合适，以及每种画法的代价是什么。

这份文档从 [全部案例](../04-structure-and-cognition/case-study/data/case-analysis.md) 里归纳，不是从图表选型手册里抄来的。“最好”是有条件的：案例里设计者写下的是**他们为什么这样画**，不是**这样画比别的画法更好**。真正比较画法效果的受控实验在案例里很少，所以每条建议后面标了证据等级：

- **实验**：有受控实验（我读到的是转述，会注明）。
- **设计者**：设计者在官方页面或论文里明说的理由。
- **做法**：多个案例都这样做，但没有谁专门论证。
- **推断**：整理者的推断。

## 先问四件事

1. **底座是什么结构、叠了什么。** 见 [信息结构理论](../04-structure-and-cognition/case-study/information-structure-theory.md)。98 个案例里 43 个不止一种结构，所以常常需要不止一个视图。
2. **视图要回答结构的哪一部分。** 连通、先后、环、包含、量、时间、来源……重点不同，画法常常不同。例如同一批调用栈样本，要看“哪些路径出现得最多”就画火焰图（丢掉时间顺序）；要看“什么时候发生”就画火焰图表（flame chart，时间在 x 轴）。不过第二轮的统计显示，结构类别和重点部分都只能解释画法的一部分（见 [可视化流派](../04-structure-and-cognition/case-study/visualization-schools.md)），所以下表是“案例里常见的选择和理由”，不是唯一解。
3. **使用者的任务。** 〔文〕Brehmer 和 Munzner 的任务分类把“找”分成四种：目标和位置都已知（lookup）、目标已知位置未知（locate）、目标未知但位置已知（browse）、两者都未知（explore）；找到之后再 identify（识别）、compare（比较）或 summarize（概括）。同一种结构，任务不同，合适的画法也不同（见下面节点连线图与矩阵）。
4. **规模，以及要丢掉什么。** 先想清楚这个视图会丢掉结构的哪一部分，再决定另配哪个视图补上。

## 选择表

链接指向案例的官方原文摘录。“代价”一栏尽量引设计者自己写的局限。

| 结构与重点 | 画法 | 依据 | 代价与替代 | 证据 |
| --- | --- | --- | --- | --- |
| **层级，叶子带数量**，要看量在层级里怎么分布 | 矩形树图、冰柱图、火焰图：包含表达层级，面积或宽度表达数量 | [Treemap](../04-structure-and-cognition/case-study/data/case-evidence.md#treemap-diskspace) 的设计史：“Tree structured node-link diagrams grew too large to be useful”，能在固定空间里看数万节点。[火焰图](../04-structure-and-cognition/case-study/data/case-evidence.md#flame-graph)作者比较了几种画法，指出旭日图要比较角度，是“a more difficult perceptive task” | 面积编码线性变量本身违反图形设计准则，窄长矩形难比较（Treemap 作者自己写的）；小矩形标不了名 | 设计者 |
| **层级，节点带时间**（运行追踪） | 缩进的树加横向时间条（瀑布图），旁边放详情面板 | 追踪类案例里多数这样画（瀑布图，或树加时间线）：[Jaeger](../04-structure-and-cognition/case-study/data/case-evidence.md#jaeger)、[AgentOps](../04-structure-and-cognition/case-study/data/case-evidence.md#agentops)、[Arize Phoenix](../04-structure-and-cognition/case-study/data/case-evidence.md#arize-phoenix)、[Comet Opik](../04-structure-and-cognition/case-study/data/case-evidence.md#comet-opik)、[LangWatch](../04-structure-and-cognition/case-study/data/case-evidence.md#langwatch)、[AgentPrism](../04-structure-and-cognition/case-study/data/case-evidence.md#agentprism) 等。AgentPrism 的设计者：“Tree View was the most effective since progressive disclosure keeps deep structures navigable and minimizes on-screen noise and navigation cost” | 看不出静态的服务关系，所以 [Jaeger](../04-structure-and-cognition/case-study/data/case-evidence.md#jaeger) 和 [Tempo](../04-structure-and-cognition/case-study/data/case-evidence.md#grafana-tempo) 另配服务依赖图 | 做法 + 设计者 |
| **层级，只需要导航** | 折叠展开的列表加详情；规模到百万级时用连续缩放 | [Reactome](../04-structure-and-cognition/case-study/data/case-evidence.md#reactome) 的三面板（层级列表、通路图、详情）；[OneZoom](../04-structure-and-cognition/case-study/data/case-evidence.md#onezoom)：“all the data is on one page so that all the user has to do is zoom to reveal it” | 缩放时丢失全局上下文；OneZoom 用分支粗细辅助尺度感 | 设计者 |
| **层级加横向联系** | 概念图（层级加跨联）或嵌套复合图；不要只画树 | [CmapTools](../04-structure-and-cognition/case-study/data/case-evidence.md#cmaptools) 的作者把跨联看作创造性的来源；[Markmap](../04-structure-and-cognition/case-study/data/case-evidence.md#markmap) 只用层级，横向联系整个丢了 | 跨联多了画面会乱；谁来决定哪些跨联值得画是另一个问题 | 设计者 + 推断 |
| **一般图，小到中等规模，任务是邻域或路径** | 节点连线图（或拓扑示意图） | 〔实验，转述〕Ghoniem 等的受控实验：节点连线图在小而稀疏的图上更好，路径查找一直是节点连线图占优的任务。案例：[Kiali](../04-structure-and-cognition/case-study/data/case-evidence.md#kiali)、[Backstage](../04-structure-and-cognition/case-study/data/case-evidence.md#backstage)、[ICIJ](../04-structure-and-cognition/case-study/data/case-evidence.md#icij-offshore-leaks) | 位置本身没有含义；稠密时成“毛球” | 实验（转述）+ 做法 |
| **一般图，稠密或较大，任务不是找路径** | 邻接矩阵加排序；工程系统用设计结构矩阵 | 〔实验，转述〕同一实验里，图大而稠密时矩阵更好。[DSM](../04-structure-and-cognition/case-study/data/case-evidence.md#dsm) 的设计者：“highly compact, easily scalable, and intuitively readable”，并配套排序（sequencing）、聚类（clustering）、分带（banding） | 没有合适的排序读不出模式；路径难跟；复杂系统“highly unlikely”排成上三角；一个 DSM 只含一种关系 | 实验（转述）+ 设计者 |
| **一般图，大规模，要看出结构而不是毛球** | 位置由结构性质决定（[Hive Plot](../04-structure-and-cognition/case-study/data/case-evidence.md#hive-plot)）；或聚合并支持原地展开（[Nx](../04-structure-and-cognition/case-study/data/case-evidence.md#nx) 的组合节点，[Kiali](../04-structure-and-cognition/case-study/data/case-evidence.md#kiali) 的多粒度图） | Hive Plot：“In a hairball, data is subordinate to layout”；Nx：“Composite nodes are essential to navigate a graph of even a moderate size” | Hive Plot 自己写“The axis and node mapping is arbitrary”，需要向读者解释；聚合需要先定义聚合口径 | 设计者 |
| **有向无环图，依赖、血缘、流水线** | 方向固定的分层图；边可展开到子任务或字段；另配运行视图 | 血缘类：[Marquez](../04-structure-and-cognition/case-study/data/case-evidence.md#marquez)、[DataHub](../04-structure-and-cognition/case-study/data/case-evidence.md#datahub)、[OpenMetadata](../04-structure-and-cognition/case-study/data/case-evidence.md#openmetadata)；计划与执行成对：[AgentEnsemble](../04-structure-and-cognition/case-study/data/case-evidence.md#agentensemble-viz)、[n8n](../04-structure-and-cognition/case-study/data/case-evidence.md#n8n) | DataHub：一次只能展开一个任务的上下游“to keep the visualization simple”；时间窗只过滤最新版本的血缘，不显示历史血缘 | 做法 + 设计者 |
| **图，重点是环** | 把环单独标出或只显示环；或用矩阵排序让反馈标记集中 | [pydeps](../04-structure-and-cognition/case-study/data/case-evidence.md#pydeps)：“--show-cycles show only import cycles”，环用蓝色框；DSM 的 sequencing 以消除反馈标记为目标 | 大型系统的反馈环无法这样完全分析（DSM 文档） | 设计者 |
| **流量网络** | 桑基图：宽度正比于量，颜色表示形式，方向表示流向 | [LLNL 能源流向图](../04-structure-and-cognition/case-study/data/case-evidence.md#llnl-energy-flow)：“Every line's width is proportional to the quantity” | 静态汇总；看不出单个设备或随时间的变化（整理者推断） | 设计者 + 推断 |
| **表，每项只有状态，关系不重要** | 雷达（环加象限），明确放弃关系 | [Thoughtworks](../04-structure-and-cognition/case-study/data/case-evidence.md#thoughtworks-tech-radar)、[Zalando](../04-structure-and-cognition/case-study/data/case-evidence.md#zalando-tech-radar)；景观图（[CNCF](../04-structure-and-cognition/case-study/data/case-evidence.md#cncf-landscape)）同理 | 完全看不出项目之间的依赖 | 做法 |
| **表，多个变量加时间** | 位置、大小、颜色、时间各占一个通道（动画气泡图） | [Gapminder](../04-structure-and-cognition/case-study/data/case-evidence.md#gapminder)：x、y、面积、颜色、时间五个变量 | 通道有限，变量多了要取舍 | 做法 |
| **表，要换不同的图看** | 先看每种视图需要哪些“角色槽”（位置、大小、颜色、层级、时间），再看数据的列能不能填进去 | [Wikidata 查询服务](../04-structure-and-cognition/case-study/data/case-evidence.md#wikidata-query-views)的每种视图都列出了它要的列角色 | — | 做法 + 推断 |
| **文本派生出的图** | 大小表示中心性，颜色表示话题群，关注“没连上”的结构空白；不要用词云代替 | [InfraNodus](../04-structure-and-cognition/case-study/data/case-evidence.md#infranodus)：“The result is not a word cloud: it is a map of relations” | 结构由算法派生，语义是否成立要人来判断 | 设计者 + 推断 |
| **高维向量** | 二维或三维投影，加最近邻列表和标签着色 | [Embedding Projector](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-projector)：静态视图不够，需要检查 “nearby points are semantically related” | 投影会扭曲距离；比较两个嵌入需要额外设计 | 设计者 |
| **同一批对象的多种结构**（树、地图、时间） | 并排的联动视图，用一致的颜色保持对象身份 | [Nextstrain](../04-structure-and-cognition/case-study/data/case-evidence.md#nextstrain)：“Multiple views into different facets of the data are presented and remain in sync” | 推断出的状态在证据不足时可能要隐藏 | 设计者 |
| **论证** | 论证地图，默认隐藏逻辑细节，能回到源文本 | [Argdown](../04-structure-and-cognition/case-study/data/case-evidence.md#argdown)、[图尔敏模型](../04-structure-and-cognition/case-study/data/case-evidence.md#toulmin)、[Kialo](../04-structure-and-cognition/case-study/data/case-evidence.md#kialo) | Argdown：“This map hides a lot of the logical details” | 设计者 |
| **长篇材料** | 摘要加链接向下，子层自己完整可读 | [Wikipedia 摘要式写作](../04-structure-and-cognition/case-study/data/case-evidence.md#wikipedia-summary-style)；见 [分层写作](../04-structure-and-cognition/extraction/layered-writing.md) | 摘要和子层要同步维护 | 设计者 |

## 几个常见的坏选择

- **把有分叉的结构只画成一维列表。** Git 提交历史是 DAG，默认视图却是按时间倒序的列表，要加 `--graph` 才画出分叉和合并。〔[案](../04-structure-and-cognition/case-study/data/case-evidence.md#git-history)〕
- **用旭日图做比较。** 火焰图作者的理由是：它要比较角度，而不是长度或面积。〔[案](../04-structure-and-cognition/case-study/data/case-evidence.md#flame-graph)〕
- **用词云代替关系。** 见上表。
- **用只表达层级的视图承载带跨联的知识。** Markmap 把文章变成导图时，横向联系全部消失。〔案+推〕
- **在稠密大图上用力导向图。** Hive Plot、VOWL、Nx 的设计者都写了类似的话。

## 给同一份结构配几个视图

案例里常见的搭配，每一对都是“一个视图丢了什么，另一个视图补上”：

| 搭配 | 补上的是 |
| --- | --- |
| 追踪树的瀑布图 + 服务依赖图（Jaeger、Tempo） | 单次请求的时间 / 跨请求的静态关系 |
| 计划 DAG + 执行时间线（AgentEnsemble、n8n、LangGraph） | 依赖 / 实际发生的时间 |
| 火焰图 + 火焰图表（Gregg） | 路径占比 / 时间顺序 |
| SBGN 的过程描述、实体关系、活动流 | 时间进程 / 所有可能关系 / 活动之间的影响 |
| 树 + 地图 + 时间（Nextstrain） | 系统发生 / 地理 / 时间，靠颜色保持同一个对象 |
| 血缘图 + 表（OpenMetadata） | 拓扑 / 便于扫描、搜索、排序的列表 |
| 文章页面 + 白板（AFFiNE） | 线性论述 / 空间摆放，靠同一批块保持对象 |

## 按流派看

下表按结构和重点列画法；换一个角度——**八个画法流派各自押注什么、放弃什么、什么时候出现、常和谁搭配**——见 [可视化流派](../04-structure-and-cognition/case-study/visualization-schools.md)。

## 与旧分类表的关系

[结构与图形范式的分类](taxonomy.md) 的“容易出问题的地方”一列是整理者的初稿，没有核验。本文是它的案例版：前者按结构家族列图形，这里按“结构加重点加任务”选图，并给出能追溯到原文的理由和代价。

## 还没有解决的

- 缺少非软件领域里“设计者写了理由”的案例（见 [案例分析的方法](../04-structure-and-cognition/case-study/method.md)）。
- 受控实验只用到节点连线图与矩阵这一组，而且读到的是转述；其他对比（树图与旭日图、瀑布图与火焰图）没有实验证据，只有设计者的论证。
