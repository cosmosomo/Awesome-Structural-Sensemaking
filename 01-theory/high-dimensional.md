# 高维可视化：超越二维与三维

问题：数据的维度比屏幕的位置轴多的时候，怎样把它变成人能看、能推理的东西；以及“再加一个空间维度（三维、VR）”到底有没有帮助。

> 这篇是从案例归纳的，不是从文献演绎的。证据分三种，在句末标出：〔案〕来自本库案例（编码是整理者的判断，原文摘录在[案例证据](../04-structure-and-cognition/case-study/data/case-evidence.md)里）；〔文〕来自整理者读过的文献，只用来校准词表和旁证；〔推〕是整理者的推测，没有直接的证据。哪些文献读到了什么程度，见[经典研究](references.md)里每条的备注。

## 这里说的“高维”是什么

“超越二维、三维”至少是三件不同的事。这个议题是用户 2026-10-14 提的，下面按我读到的意思分开，不确定对不对：

| | 含义 | 本库的案例 |
| --- | --- | --- |
| 数据维度多 | 每个对象有几十、几百、几千个属性（特征），位置轴不够分 | 大多数案例：投影、平行坐标、特征总览、集合交集…… |
| 几何维度多 | 对象真的生活在四维或更高维的空间里 | [Miegakure](../04-structure-and-cognition/case-study/data/case-evidence.md#miegakure) |
| 载体多一维 | 数据维度不变，改用三维、VR 给人更多的摆放自由 | [ImAxes](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes)；[双曲浏览器](../04-structure-and-cognition/case-study/data/case-evidence.md#hyperbolic-browser)算边界案例（换的是几何，不是维数） |

文献对这件事的说法是一致的：显示设备和人的视觉系统“prevent the direct display and instantaneous recognition of structures with higher dimensions than two or three”（Liu 等 2015）〔文〕。Lee 等 2021 补了一句：这里的“高维”指欧氏空间，用 1 维到 5 维的立方体线框来说明每加一维，立方体就翻倍〔文〕。

## 十种办法

下表是从案例里归纳的“维度处理”（词表 `dim_modes`），不是文献里现成的分类；名字调整时对照了 Keim 2002 把技术分成“标准二三维、几何变换、图符、密集像素、堆叠”五类、再加“交互与扭曲”一个维度的做法，和 Liu 等 2015 按“数据变换、视觉映射、视图变换”三个流水线步骤分类的做法〔文〕。本库的案例里没有图符（Chernoff 脸、星形图）和密集像素两类，因为本库没收到把它们做成产品并写了设计理由的案例，不代表它们没用。〔推〕

<!-- gen:dimsmodes: -->
| 维度处理 | 做法 | 案例（加粗的是主要做法） | 数量 |
| --- | --- | --- | --- |
| 降维投影 | 把多维压成二到三个位置轴：PCA、t-SNE、UMAP 等；线性投影的轴有含义，非线性投影的邻域较可信但距离和大小没有含义 | **[Embedding Projector](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-projector)**、**[How to Use t-SNE Effectively（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#tsne-misread)**、[Visualizing Neural Networks with the Grand Tour（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#grand-tour)、**[Embedding Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-atlas)**、**[Nomic Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#nomic-atlas)**、[Orange](../04-structure-and-cognition/case-study/data/case-evidence.md#orange)、[KeplerMapper](../04-structure-and-cognition/case-study/data/case-evidence.md#kepler-mapper)、**[Semantic Map of GitHub](../04-structure-and-cognition/case-study/data/case-evidence.md#semantic-map-github)**、**[The State of Open Source Agentic AI](../04-structure-and-cognition/case-study/data/case-evidence.md#state-of-agentic-ai)**、**[单细胞数据的二维嵌入：失真之争（Chari 与 Pachter 2023；Lause 等 2024）](../04-structure-and-cognition/case-study/data/case-evidence.md#single-cell-embeddings)** | 10 |
| 复用轴 | 不降维，每个维度一根轴，并排（平行坐标）或围成圆（Radviz）；所有维度同时可见，代价是线的交叉和轴的顺序 | **[HiPlot](../04-structure-and-cognition/case-study/data/case-evidence.md#hiplot)**、**[Orange](../04-structure-and-cognition/case-study/data/case-evidence.md#orange)**、[ImAxes（VR 里的沉浸式坐标轴）](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes) | 3 |
| 多通道编码 | 把维度分到位置之外的通道：颜色、大小、形状、分面、动画时间；一张图能容纳的维度数受通道数限制 | [Facets](../04-structure-and-cognition/case-study/data/case-evidence.md#facets)、[Voyager](../04-structure-and-cognition/case-study/data/case-evidence.md#voyager)、**[Gapminder 气泡图](../04-structure-and-cognition/case-study/data/case-evidence.md#gapminder)** | 3 |
| 并置多视图 | 一次画很多低维视图：小多图、散点矩阵、逐特征总览；联动刷选把它们连起来 | [How to Use t-SNE Effectively（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#tsne-misread)、[dtour](../04-structure-and-cognition/case-study/data/case-evidence.md#dtour)、[Embedding Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-atlas)、[HiPlot](../04-structure-and-cognition/case-study/data/case-evidence.md#hiplot)、**[Facets](../04-structure-and-cognition/case-study/data/case-evidence.md#facets)**、[Voyager](../04-structure-and-cognition/case-study/data/case-evidence.md#voyager)、[Rank-by-Feature 框架与 Hierarchical Clustering Explorer（Seo 与 Shneiderman）](../04-structure-and-cognition/case-study/data/case-evidence.md#rank-by-feature)、[UpSet](../04-structure-and-cognition/case-study/data/case-evidence.md#upset)、[ImAxes（VR 里的沉浸式坐标轴）](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes) | 9 |
| 切片与截面 | 固定其余维度，只看一个低维子空间，并提供换子空间的操作：四维世界的三维截面、轴范围筛选 | **[Miegakure（四维解谜游戏）](../04-structure-and-cognition/case-study/data/case-evidence.md#miegakure)** | 1 |
| 巡游 | 沿一串连续变化的投影或截面做动画，让人从运动里推断高维形状；点的身份要在帧之间保持 | **[Visualizing Neural Networks with the Grand Tour（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#grand-tour)**、**[dtour](../04-structure-and-cognition/case-study/data/case-evidence.md#dtour)** | 2 |
| 排序与推荐 | 可能的视图太多（组合爆炸）时，由系统打分、排序、推荐，人只看靠前的 | **[Voyager](../04-structure-and-cognition/case-study/data/case-evidence.md#voyager)**、**[Rank-by-Feature 框架与 Hierarchical Clustering Explorer（Seo 与 Shneiderman）](../04-structure-and-cognition/case-study/data/case-evidence.md#rank-by-feature)**、[Orange](../04-structure-and-cognition/case-study/data/case-evidence.md#orange) | 3 |
| 先摘要再画 | 先把高维数据变成更小的结构（聚类、集合交集、拓扑图），再画这个结构；高维本身不再出现在画面里 | [Embedding Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-atlas)、[Nomic Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#nomic-atlas)、**[UpSet](../04-structure-and-cognition/case-study/data/case-evidence.md#upset)**、**[KeplerMapper](../04-structure-and-cognition/case-study/data/case-evidence.md#kepler-mapper)**、[Semantic Map of GitHub](../04-structure-and-cognition/case-study/data/case-evidence.md#semantic-map-github)、[The State of Open Source Agentic AI](../04-structure-and-cognition/case-study/data/case-evidence.md#state-of-agentic-ai)、[单细胞数据的二维嵌入：失真之争（Chari 与 Pachter 2023；Lause 等 2024）](../04-structure-and-cognition/case-study/data/case-evidence.md#single-cell-embeddings) | 7 |
| 换载体 | 借 VR、AR 或身体操作多给人一个空间维度和一组手势；不改变数据维度，改变人接触它的方式 | **[ImAxes（VR 里的沉浸式坐标轴）](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes)** | 1 |
| 换空间 | 不加维度，改用非欧几何（双曲平面）给指数增长的结构更多空间；放在这里是边界案例 | **[双曲浏览器（Lamping、Rao、Pirolli，CHI 1995）](../04-structure-and-cognition/case-study/data/case-evidence.md#hyperbolic-browser)** | 1 |

20 个案例标了维度处理；其余案例没有“维度比位置轴多”的问题，或页面没写。
<!-- /gen -->

几乎没有案例只用一种办法：多数案例同时用两种以上（最常见的搭配是“降维投影 + 先摘要再画”，其次是“并置多视图”和各种办法的组合）。〔案〕

## 逐类看：每一类放弃了什么

### 降维投影：位置能读，距离和大小不能

把几百上千维压成二维，是案例里用得最多的办法。设计者几乎都在同一句话里写明它丢了什么〔案〕：

- t-SNE：“you cannot see relative sizes of clusters in a t-SNE plot”；“distances between well-separated clusters in a t-SNE plot may mean nothing”（[How to Use t-SNE Effectively](../04-structure-and-cognition/case-study/data/case-evidence.md#tsne-misread)）。
- Nomic Atlas：“Numerical distances between 2D point positions do not have concrete meaning”；文档还提醒“2D projections can distort high-dimensional distances. Validate with metadata or alternative projections.”（[Nomic Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#nomic-atlas)）。
- 单细胞领域的争论：一方认为“extreme dimension reduction, from hundreds or thousands of dimensions to 2, inevitably induces significant distortion”，二维图只能当事后展示的“cartoon diagrams”；反驳的一方认为 t-SNE 和 UMAP 保留了有意义的局部邻域和簇，但同意“2D visualisations distort distances and should not be blindly trusted”（[单细胞嵌入之争](../04-structure-and-cognition/case-study/data/case-evidence.md#single-cell-embeddings)）。**两边都同意距离会失真，分歧是失真多大、保留的邻域够不够用。**

**线性投影与非线性投影，各自批评对方。** 这是案例里最清楚的一条对照〔案〕：

| | 线性（PCA、Grand Tour、FreeViz） | 非线性（t-SNE、UMAP） |
| --- | --- | --- |
| 设计者说它的好处 | “Linear methods are attractive because they are particularly easy to reason about”；轴有含义，可以拖手柄手动设定投影（[Grand Tour](../04-structure-and-cognition/case-study/data/case-evidence.md#grand-tour)） | “the t-SNE plot is more accurate than any linear projection could be”（对弯曲的结构）（[t-SNE 一文](../04-structure-and-cognition/case-study/data/case-evidence.md#tsne-misread)） |
| 对方说它的代价 | “Some dimensionality reduction methods find interesting angles but hide everything orthogonal to them”（[dtour](../04-structure-and-cognition/case-study/data/case-evidence.md#dtour)） | “the position of each single point depends non-trivially on the whole data distribution”；数据只变了一小部分，图上所有点却大幅移动（Grand Tour 一文）；“can muddle genuine structure with layout artifacts”（dtour） |

Grand Tour 的作者因此不用 t-SNE 和 UMAP，dtour 的作者两边都不满意，选了“沿一串线性投影巡游”。〔案〕

**加一个空间维度不一定更好。** Sedlmair、Munzner 与 Tory 2013 人工检查了 816 张由 75 个数据集、4 种降维方法和 3 种散点图形式生成的图，结论是二维散点图常常“good enough”，“interactive 3D rarely helps but often hurts in terms of poorer class separation and usability”〔文〕。本库案例里主张用三维或沉浸式载体的只有 ImAxes，而它的论文自己写明需要经验验证（见下文）。〔案〕

### 复用轴：不降维，所有维度同时可见

HiPlot 的平行坐标图是每个维度一根轴、每条记录一条线，Orange 的 Radviz 是把每个属性放成圆周上的锚点、让弹簧把点拉到平衡位置；ImAxes 把这些轴放进 VR 让人抓在手里。〔案〕

- 代价写在页面里：HiPlot 默认不显示取值太多的分类列和只有一个取值的列；Orange 文档承认不同优化方法“may be quite different”；ImAxes 的作者写“Unlike SPLOMs, in PCPs only the relations between adjacent axes are easily visible”，并承认能同时处理的轴数有限。〔案〕
- 文献里同样的说法：Lee 等写到平行坐标里“the ordering of variables along the axis changes what can be learned”，散点矩阵“does not scale to large numbers of variables”〔文〕。

### 并置多视图：一次画很多低维视图，靠联动把它们连起来

Facets Overview 逐特征一行、把训练集与测试集叠在同一行里比；HiPlot 的多个并列显示；Embedding Atlas 的嵌入图加上每个元数据列的分布图并交叉过滤；dtour 的投影预览画廊。〔案〕dtour 的作者把代价说得很清楚：并排的静态投影网格“are directly comparable at a glance but require constant shifts of focus to integrate information”。〔案〕

### 排序与推荐：视图太多的时候，由系统挑

n 个维度有 n(n−1)/2 个二维投影。Rank-by-Feature 的作者写：“An exhaustive visual search is out of the question as the number of dimensions grows”，所以对所有一维、二维投影按相关系数等特征打分，用颜色编码的网格总览，先看分高的；它自己写明总览在维度超过约 130 时就太挤了，并且只看轴平行的投影，“features can be detected in only the two selected dimensions”。Voyager 面对同一问题说变量、变换和编码的组合是“a combinatorial explosion”，所以枚举并排序图，并且“Show data variation, not design variation”：相近的编码只留一个代表。Orange 的 VizRank 做同样的事。〔案〕

### 巡游与切片：用运动或截面代替“一次全看”

- **巡游**：Grand Tour 与 dtour 沿一串连续变化的线性投影做动画，让人从运动里推断高维形状；关键在**点的身份要在帧之间保持**（dtour：“letting viewers track points across views rather than re-identifying them after each transition”），而且只有关键帧可以解释，“the smooth interpolation is an object-constancy aid”。〔案〕
- **动画的证据不乐观**：Robertson 等 2008 比较动画、叠加轨迹和小多图三种趋势可视化，动画在演示时最快、最让人愉快，但出错多；分析时“Animation is the least effective form for analysis”，小多图更准〔文〕。dtour 把预览画廊和动画放进同一个界面，可能就是在对冲这个问题（〔推〕，作者没有这样写）。
- **切片**：Miegakure 是四维解谜游戏。开发者说为什么切片而不投影：“4D to 2D is two dimensions down: a lot of objects are going to overlap on the screen”；所以玩家看到的是四维世界的三维截面，按键换看哪三个维度，代价是“When you translate the slice you cannot see where you are going”。〔案〕**当几何本身是四维，投影会让物体大量重叠，截面更可读**，这是案例里唯一的“几何维度多”的例子，所以不能推到数据维度多的情形。〔推〕

### 先摘要再画：高维不再出现在画面里

UpSet 的出发点是 Venn 图“are not suitable to visualize intersections of more than three or four sets”，改画成“交集当作行”的矩阵；KeplerMapper 先把点云变成由聚类节点组成的小图，依据是“connectivity is more important than distance”，并自己写明这是“a lossy compressed mathematical representation”；Embedding Atlas 和 Nomic Atlas 用密度等高线和自动标签把几百万个点概括成区域；单细胞一文也建议不画每个点的高层图。〔案〕**摘要把“看不清的维度”换成“看得清的结构”，代价是你只能看到摘要算法决定保留的那一部分。**〔推〕

### 换载体与换空间

ImAxes 的作者说在二维屏幕上看三维图有遮挡、透视变形和输入设备问题，所以要在 VR 里做；同时承认能同时处理的轴数有限，并且“empirical validation of ImAxes is needed”，没有用户研究。双曲浏览器（1995）说大树在欧氏平面上没有令人满意的布局，“because of its exponential growth”，改用双曲平面；实验没有发现显著的性能差异，但参与者明显偏爱它。〔案〕**这两个案例都没有给出“比二维加联动更好”的实证，而 Sedlmair 等的研究方向相反。**〔案〕〔文〕

## 反复出现的几个模式

1. **每种办法的设计者都写了别的办法的失败**（`alternative`）。Grand Tour 批评 t-SNE 的点位置依赖整体；dtour 批评两类降维；Voyager 批评手工逐张指定；UpSet 批评 Venn 图；Rank-by-Feature 批评穷举；Miegakure 批评投影；ImAxes 批评二维屏幕上的三维；KeplerMapper 批评在投影上直接聚类；Embedding Atlas 批评只管渲染的工具。这和[可视化流派](../04-structure-and-cognition/case-study/visualization-schools.md)里“流派是对默认做法失效点的回应”的发现一致，高维的版本是：**每一种办法都是对另一种办法的“失真”的回应。**〔案〕
2. **失真不被隐藏。** 标了维度处理的案例里，绝大多数在设计者自己的文字里写了失真或局限，常见的说法是“距离没有含义”“只有关键帧可解释”“有损压缩”“还没有用户研究”。〔案〕
3. **没有一种办法能同时保留距离、保留身份、保留全部维度。** 投影保留身份但丢距离和正交方向；复用轴保留全部维度但丢高阶关系；摘要保留结构但丢个体。案例里的做法都是组合：先投影，再用联动的元数据视图和近邻检查来验证。〔案〕
4. **验证是流程的一部分。** Nomic 的文档建议“Validate with metadata or alternative projections”，单细胞的反驳一方写“any generated insight should then be validated in the high-dimensional data by other means”，dtour 的论文把“validating whether structure in an embedding is genuine or a projection artifact”当作目标之一。〔案〕

## 与本库其他分类的关系

下面两张表是标了维度处理的案例与结构类别、画法流派的交叉计数。〔案〕

<!-- gen:dimscross:structure -->
| 主要维度处理 \ 主类结构 | 集合与分类 | 表与多维属性 | 层级与树 | 一般图与网络 | 空间与几何 | 合计 |
| --- | --- | --- | --- | --- | --- | --- |
| 降维投影 | · | · | · | · | 7 | 7 |
| 复用轴 | · | 2 | · | · | · | 2 |
| 多通道编码 | · | 1 | · | · | · | 1 |
| 并置多视图 | · | 1 | · | · | · | 1 |
| 切片与截面 | · | · | · | · | 1 | 1 |
| 巡游 | · | · | · | · | 2 | 2 |
| 排序与推荐 | · | 2 | · | · | · | 2 |
| 先摘要再画 | 1 | · | · | 1 | · | 2 |
| 换载体 | · | 1 | · | · | · | 1 |
| 换空间 | · | · | 1 | · | · | 1 |
<!-- /gen -->

<!-- gen:dimscross:school -->
| 主要维度处理 \ 主流派 | 连线图 | 规则布局 | 通道分配图 | 示意与隐喻图 | 合计 |
| --- | --- | --- | --- | --- | --- |
| 降维投影 | · | · | 7 | · | 7 |
| 复用轴 | · | 2 | · | · | 2 |
| 多通道编码 | · | · | 1 | · | 1 |
| 并置多视图 | · | · | 1 | · | 1 |
| 切片与截面 | · | · | · | 1 | 1 |
| 巡游 | · | · | 2 | · | 2 |
| 排序与推荐 | · | 1 | 1 | · | 2 |
| 先摘要再画 | 1 | 1 | · | · | 2 |
| 换载体 | · | 1 | · | · | 1 |
| 换空间 | 1 | · | · | · | 1 |
<!-- /gen -->

读法：高维案例的结构大多落在**空间与几何**（位置是算出来的，不是给定的）和**表与多维属性**；画法大多是通道分配图（投影散点）和规则布局（平行坐标、Radviz、矩阵）。这批案例是为这个议题专门收的，所以抬高了这些类的比重，不能当作整个语料的分布。〔案〕“位置是算出来的”这一点在[信息结构理论](../04-structure-and-cognition/case-study/information-structure-theory.md)的“空间与几何”一节里已经出现，这里是它最集中的一批证据。

## 怎么选（初步）

每一行都标了证据来自哪里；没有标〔文〕的，只是本库案例里设计者的做法，不是经过实验比较的结论。

| 你的情况 | 先试 | 依据 |
| --- | --- | --- |
| 想看簇和近邻，维度几百以上 | 二维投影，同一份数据多换几次参数，用联动的元数据视图和近邻检查来验证；不要读簇的大小和簇间距离 | t-SNE 一文、Embedding Atlas、Nomic 〔案〕 |
| 想知道哪些特征在起作用 | 轴有含义的做法：线性投影、平行坐标、Radviz | Grand Tour、HiPlot、Orange 〔案〕 |
| 变量很多，还没想好问什么 | 让系统给视图排序或推荐，人只看靠前的 | Voyager、Rank-by-Feature、VizRank 〔案〕 |
| 集合很多，要看组合 | 交集矩阵，不用 Venn 图 | UpSet 〔案〕 |
| 要看连通结构（分支、环） | 先摘要成图再画 | KeplerMapper 〔案〕 |
| 几何本身是四维以上 | 截面，并提供换截面的操作 | Miegakure 〔案〕；是否适用于数据维度多的情形没有证据〔推〕 |
| 想上三维或 VR | 先证明它比“二维加联动”更好 | Sedlmair 等 2013〔文〕；ImAxes 自己写明需要验证〔案〕 |
| 用动画展示时间或投影的变化 | 演示可以；要做分析，同时给并排的静态视图 | Robertson 等 2008〔文〕 |

## 还没有解决的

- **没有案例带用户研究。** dtour 的作者没有评估用户受益；ImAxes 只有用例演示；文献里的实证研究（Sedlmair、Robertson）比较的是更窄的任务。这篇文档的“怎么选”多数只有案例证据。
- **失真的度量没有读。** Nonato 与 Aupetit 2018 综述了投影的失真类型和量化方法，整理者只读到摘要；Lause 等用邻域和类别保持的度量反驳 Chari 与 Pachter，这个争论怎么判断，本库没有立场。
- **语料偏。** 案例多来自机器学习和生物；金融、物理、社会科学里的高维可视化没有收。图符（Chernoff 脸、星形图）和密集像素两类办法本库没有案例。
- **“维度数”与结构复杂度的关系没有讨论。** [评价理论](evaluation-theory.md)把结构复杂度和理解难度分开；维度数算哪一边，案例里没有证据。
- **边界案例。** Miegakure 是游戏，双曲浏览器不是加维度；它们帮助划边界，但让“十种办法”里的两种只有一个案例。
