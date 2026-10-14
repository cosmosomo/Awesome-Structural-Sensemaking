# 高维可视化：超越二维与三维

问题：数据的维度比屏幕的位置轴多的时候，怎样把它变成人能看、能推理的东西；以及“再加一个空间维度（三维、分层、VR）”在什么条件下有帮助。

> 这篇是从案例归纳的，不是从文献演绎的。证据分三种，在句末标出：〔案〕来自本库案例（编码是整理者的判断，原文摘录在[案例证据](../04-structure-and-cognition/case-study/data/case-evidence.md)里）；〔文〕来自整理者读过的文献，只用来校准词表和旁证；〔算〕是整理者自己用脚本算的数，不是文献也不是案例，脚本在 `scripts/` 里；〔推〕是整理者的推测，没有直接的证据。哪些文献读到了什么程度，见[经典研究](references.md)里每条的备注。

## 这里说的“高维”是什么

“超越二维、三维”至少是三件不同的事。这个议题是用户 2026-10-14 提的，下面按我读到的意思分开，不确定对不对：

| | 含义 | 本库的案例 |
| --- | --- | --- |
| 数据维度多 | 每个对象有几十、几百、几千个属性（特征），位置轴不够分 | 大多数案例：投影、平行坐标、特征总览、集合交集…… |
| 几何维度多 | 对象真的生活在四维或更高维的空间里 | [Miegakure](../04-structure-and-cognition/case-study/data/case-evidence.md#miegakure) |
| 载体多一维 | 数据维度不变（或本来只有二三维），位置轴放进三维、分层或立体空间 | 见下文[再加一个空间维度](#再加一个空间维度三维分层立体)：[pca3d](../04-structure-and-cognition/case-study/data/case-evidence.md#pca3d)、[Embedding Projector](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-projector)、[SkyWalking](../04-structure-and-cognition/case-study/data/case-evidence.md#skywalking)、[iCAVE](../04-structure-and-cognition/case-study/data/case-evidence.md#icave)、[VRNetzer](../04-structure-and-cognition/case-study/data/case-evidence.md#vrnetzer)、[GeoGraphViz](../04-structure-and-cognition/case-study/data/case-evidence.md#geographviz)、[ImAxes](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes)；[双曲浏览器](../04-structure-and-cognition/case-study/data/case-evidence.md#hyperbolic-browser)算边界案例（换的是几何，不是维数） |

文献对这件事的说法是一致的：显示设备和人的视觉系统“prevent the direct display and instantaneous recognition of structures with higher dimensions than two or three”（Liu 等 2015）〔文〕。Lee 等 2021 补了一句：这里的“高维”指欧氏空间，用 1 维到 5 维的立方体线框来说明每加一维，立方体就翻倍〔文〕。

## 十种办法

下表是从案例里归纳的“维度处理”（词表 `dim_modes`），不是文献里现成的分类；名字调整时对照了 Keim 2002 把技术分成“标准二三维、几何变换、图符、密集像素、堆叠”五类、再加“交互与扭曲”一个维度的做法，和 Liu 等 2015 按“数据变换、视觉映射、视图变换”三个流水线步骤分类的做法〔文〕。本库的案例里没有图符（Chernoff 脸、星形图）和密集像素两类，因为本库没收到把它们做成产品并写了设计理由的案例，不代表它们没用。〔推〕

<!-- gen:dimsmodes: -->
| 维度处理 | 做法 | 案例（加粗的是主要做法） | 数量 |
| --- | --- | --- | --- |
| 降维投影 | 把多维压成二到三个位置轴：PCA、t-SNE、UMAP 等；线性投影的轴有含义，非线性投影的邻域较可信但距离和大小没有含义 | **[Embedding Projector](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-projector)**、**[pca3d](../04-structure-and-cognition/case-study/data/case-evidence.md#pca3d)**、**[How to Use t-SNE Effectively（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#tsne-misread)**、[Visualizing Neural Networks with the Grand Tour（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#grand-tour)、**[Embedding Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-atlas)**、**[Nomic Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#nomic-atlas)**、[Orange](../04-structure-and-cognition/case-study/data/case-evidence.md#orange)、[KeplerMapper](../04-structure-and-cognition/case-study/data/case-evidence.md#kepler-mapper)、**[Semantic Map of GitHub](../04-structure-and-cognition/case-study/data/case-evidence.md#semantic-map-github)**、**[The State of Open Source Agentic AI](../04-structure-and-cognition/case-study/data/case-evidence.md#state-of-agentic-ai)**、**[单细胞数据的二维嵌入：失真之争（Chari 与 Pachter 2023；Lause 等 2024）](../04-structure-and-cognition/case-study/data/case-evidence.md#single-cell-embeddings)**、**[VRNetzer](../04-structure-and-cognition/case-study/data/case-evidence.md#vrnetzer)** | 12 |
| 复用轴 | 不降维，每个维度一根轴，并排（平行坐标）或围成圆（Radviz）；所有维度同时可见，代价是线的交叉和轴的顺序 | **[HiPlot](../04-structure-and-cognition/case-study/data/case-evidence.md#hiplot)**、**[Orange](../04-structure-and-cognition/case-study/data/case-evidence.md#orange)**、[ImAxes（VR 里的沉浸式坐标轴）](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes) | 3 |
| 多通道编码 | 把维度分到位置之外的通道：颜色、大小、形状、分面、动画时间；一张图能容纳的维度数受通道数限制 | [Facets](../04-structure-and-cognition/case-study/data/case-evidence.md#facets)、[Voyager](../04-structure-and-cognition/case-study/data/case-evidence.md#voyager)、**[Gapminder 气泡图](../04-structure-and-cognition/case-study/data/case-evidence.md#gapminder)** | 3 |
| 并置多视图 | 一次画很多低维视图：小多图、散点矩阵、逐特征总览；联动刷选把它们连起来 | [How to Use t-SNE Effectively（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#tsne-misread)、[dtour](../04-structure-and-cognition/case-study/data/case-evidence.md#dtour)、[Embedding Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-atlas)、[HiPlot](../04-structure-and-cognition/case-study/data/case-evidence.md#hiplot)、**[Facets](../04-structure-and-cognition/case-study/data/case-evidence.md#facets)**、[Voyager](../04-structure-and-cognition/case-study/data/case-evidence.md#voyager)、[Rank-by-Feature 框架与 Hierarchical Clustering Explorer（Seo 与 Shneiderman）](../04-structure-and-cognition/case-study/data/case-evidence.md#rank-by-feature)、[UpSet](../04-structure-and-cognition/case-study/data/case-evidence.md#upset)、[ImAxes（VR 里的沉浸式坐标轴）](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes) | 9 |
| 切片与截面 | 固定其余维度，只看一个低维子空间，并提供换子空间的操作：四维世界的三维截面、轴范围筛选 | **[Miegakure（四维解谜游戏）](../04-structure-and-cognition/case-study/data/case-evidence.md#miegakure)** | 1 |
| 巡游 | 沿一串连续变化的投影或截面做动画，让人从运动里推断高维形状；点的身份要在帧之间保持 | **[Visualizing Neural Networks with the Grand Tour（Distill）](../04-structure-and-cognition/case-study/data/case-evidence.md#grand-tour)**、**[dtour](../04-structure-and-cognition/case-study/data/case-evidence.md#dtour)** | 2 |
| 排序与推荐 | 可能的视图太多（组合爆炸）时，由系统打分、排序、推荐，人只看靠前的 | **[Voyager](../04-structure-and-cognition/case-study/data/case-evidence.md#voyager)**、**[Rank-by-Feature 框架与 Hierarchical Clustering Explorer（Seo 与 Shneiderman）](../04-structure-and-cognition/case-study/data/case-evidence.md#rank-by-feature)**、[Orange](../04-structure-and-cognition/case-study/data/case-evidence.md#orange) | 3 |
| 先摘要再画 | 先把高维数据变成更小的结构（聚类、集合交集、拓扑图），再画这个结构；高维本身不再出现在画面里 | [Embedding Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-atlas)、[Nomic Atlas](../04-structure-and-cognition/case-study/data/case-evidence.md#nomic-atlas)、**[UpSet](../04-structure-and-cognition/case-study/data/case-evidence.md#upset)**、**[KeplerMapper](../04-structure-and-cognition/case-study/data/case-evidence.md#kepler-mapper)**、[Semantic Map of GitHub](../04-structure-and-cognition/case-study/data/case-evidence.md#semantic-map-github)、[The State of Open Source Agentic AI](../04-structure-and-cognition/case-study/data/case-evidence.md#state-of-agentic-ai)、[单细胞数据的二维嵌入：失真之争（Chari 与 Pachter 2023；Lause 等 2024）](../04-structure-and-cognition/case-study/data/case-evidence.md#single-cell-embeddings) | 7 |
| 换载体 | 借 VR、AR 或身体操作多给人一个空间维度和一组手势；不改变数据维度，改变人接触它的方式 | **[ImAxes（VR 里的沉浸式坐标轴）](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes)** | 1 |
| 换空间 | 不加维度，改用非欧几何（双曲平面）给指数增长的结构更多空间；放在这里是边界案例 | **[双曲浏览器（Lamping、Rao、Pirolli，CHI 1995）](../04-structure-and-cognition/case-study/data/case-evidence.md#hyperbolic-browser)** | 1 |

22 个案例标了维度处理；其余案例没有“维度比位置轴多”的问题，或页面没写。
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

**这些投影最后画成二维还是三维，是另一个问题**，见下文[再加一个空间维度](#再加一个空间维度三维分层立体)。先说一句：关于降维点云加一根轴有没有用，已有的实验互相不一致，不能合成一句话。

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

### 换空间：不加维度，换几何

双曲浏览器（1995）说大树在欧氏平面上没有令人满意的布局，“because of its exponential growth”，改用双曲平面；实验没有发现显著的性能差异，但参与者明显偏爱它。〔案〕“换载体”（VR、立体）和“加一根轴”（三维、分层）见下一节。

## 再加一个空间维度：三维、分层、立体

> **这一节在 2026-10-14 按用户的反馈重写。** 原来这里只有一句“加一个空间维度不一定更好”，证据是 Sedlmair 等 2013 一篇（研究的是降维后的点云，量的是“类别看起来分不分得开”），加上 ImAxes 一个案例；没有查三维图谱，也漏看了库里已有的三维案例。用户的说法是：加一个维度的图谱，帮助不小。用户后来举了“pca-3d”作例子，我读成降到三维的 PCA 点云（R 的 pca3d 包，或 Embedding Projector 里的 PCA 三维视图），不确定对不对。节点连线的三维图谱、分层的 2.5D 图谱也一并查了。下面按对象和任务分开读，不合成一句“三维好”或“三维差”。

### 三种“多一维”

案例里三种混着出现。词表 `spaces` 把它们分开；它和上面的 `dim_modes` 是两个独立的字段：`dim_modes` 回答“数据维度比位置轴多时怎么办”，`spaces` 回答“位置轴本身放在平面、分层还是立体空间里”。

<!-- gen:spacemodes: -->
| 展示空间 | 做法 | 案例（加粗的是主要的） | 数量 |
| --- | --- | --- | --- |
| 分层平面（2.5D） | 第三根轴只放层或类别，每一层内部仍是平面布局；层与层之间的连线穿过第三根轴 | **[Apache SkyWalking](../04-structure-and-cognition/case-study/data/case-evidence.md#skywalking)**、[GeoGraphViz](../04-structure-and-cognition/case-study/data/case-evidence.md#geographviz)、[iCAVE](../04-structure-and-cognition/case-study/data/case-evidence.md#icave) | 3 |
| 三维场景（普通屏幕） | 在平面屏幕上画三维位置，靠透视、旋转、遮挡和深度线索（点随距离变大小、雾、阴影）读深度 | [Apache SkyWalking](../04-structure-and-cognition/case-study/data/case-evidence.md#skywalking)、**[Embedding Projector](../04-structure-and-cognition/case-study/data/case-evidence.md#embedding-projector)**、**[pca3d](../04-structure-and-cognition/case-study/data/case-evidence.md#pca3d)**、**[Miegakure（四维解谜游戏）](../04-structure-and-cognition/case-study/data/case-evidence.md#miegakure)**、**[GeoGraphViz](../04-structure-and-cognition/case-study/data/case-evidence.md#geographviz)**、[VRNetzer](../04-structure-and-cognition/case-study/data/case-evidence.md#vrnetzer)、**[iCAVE](../04-structure-and-cognition/case-study/data/case-evidence.md#icave)** | 7 |
| 立体与沉浸 | 双目立体、头部追踪或 VR、CAVE；多给人立体深度线索和手势，需要专门设备或头显 | **[ImAxes（VR 里的沉浸式坐标轴）](../04-structure-and-cognition/case-study/data/case-evidence.md#imaxes)**、**[VRNetzer](../04-structure-and-cognition/case-study/data/case-evidence.md#vrnetzer)**、[iCAVE](../04-structure-and-cognition/case-study/data/case-evidence.md#icave) | 3 |

8 个案例标了展示空间；其余案例的位置轴放在普通二维平面里（含平面上的双曲几何）。
<!-- /gen -->

**第三根轴放的东西各不相同。**〔案〕

- **一个连续的量**：第三个主成分（pca3d、Embedding Projector），或把功能注释嵌入三维后的第三个分量（VRNetzer）。
- **离散的层**：SkyWalking 的 3D 基础设施地图把 Apps、Middleware、Service Mesh、Infra 四层竖直堆起来，层内是平面，层间画跨层连线（摘录只写了 cross-layer view，层的样子是我打开演示页看到的）；iCAVE 的“语义层布局”默认分 7 层；GeoGraphViz 把二维地图放在底层、图悬在它上方。3d-force-graph 的有向无环图模式也有把层次放在深度轴上的选项（`zout`、`zin`，npm 说明）。
- **深度本身，只用来多摆些点和边**：3d-force-graph 的力模拟默认三维（`numDimensions` 默认 3，可设 1、2、3）；VRNetzer 里的弹簧布局。
- **第四维的截面**：Miegakure。

**读深度靠什么线索，各案例不同。**〔案〕Embedding Projector 的论文写“To help interpretation of the 3D mode, the Projector uses multiple redundant depth cues”：按距离改变点的大小、加雾、开场的“lazy susan”旋转；pca3d 画点到 xy 平面的细线和一块灰色平面；iCAVE 可以开关立体、旋转到没有遮挡的角度；VRNetzer 用头显的六自由度走动和旋转。这些线索恰好是下面文献里决定三维有没有帮助的条件。〔推〕

### 文献里的实验：按对象和任务读

**节点连线图（图谱）**〔文〕

| 研究 | 比较了什么 | 三维（或立体）更好 | 二维更好，或没有差别 | 作者写的条件和代价 |
| --- | --- | --- | --- | --- |
| Ware 与 Franck 1996 | 判断两个高亮节点之间有没有长度为二的路径；二维、静态三维、立体、头部耦合、旋转 | “head-coupled stereo viewing can increase the size of an abstract graph that can be understood by a factor of three”；运动和立体都有帮助，运动的方式不重要 | 单张静态透视图：“A static perspective image may add little in comparison with a 2D diagram” | 头部耦合让一些被试“somewhat stressful”；运动要持续重绘 |
| Ware 与 Mitchell 2008（只读到摘要） | 用高分辨率立体显示重做路径追踪 | 运动加立体时，未经训练的观察者在 333 个节点的图里错误率低于 10%，熟练观察者到 1000 个节点；作者写这是“a much greater benefit for 3D viewing than previous studies” | 摘要里没有 | 摘要里没有写代价 |
| Alper 等 2011 | 二维、2.5D、三维布局，静态高亮与立体高亮；16 人 | 较复杂的任务：三维加静态高亮优于只用一种高亮的二维 | 另外几个任务（T1、T2、T4）里 2.5D 更快 | “The 3D graph layouts were at a disadvantage without rotation since certain nodes could be occluded from a static viewpoint” |
| Kotlarek 等 2020 | 头显里的沉浸式三维对桌面二维；20 人；读结构、记住节点、找出变化 | 读网络结构和找最短路径：沉浸式更准更容易 | 桌面更快；记忆任务和回忆变化，桌面更好 | 两种环境整体算一个条件，不能拆到单个因素 |
| Greffard 等 2011（原文被人机验证挡住，没读） | 社区发现：二维、三维透视、立体三维 | Marriott 的综述转述：“benefits for binocular 3D over 2D for community detection in social networks” | | 转述，不当一手证据 |
| Marriott 等 2018（综述） | 综述二维与三维的实证研究 | 三维节点连线图对路径追踪有实证收益 | 三维锥形树“a poor representation for hierarchical data”（遮挡，旋转慢） | “3D representations are not generally better than 2D representations, but nor are 2D representations always better than 3D: which is better depends upon the kind of task” |

**降维后的点云（散点图）**〔文〕

| 研究 | 比较了什么 | 三维（或立体）更好 | 二维更好，或没有差别 | 作者写的条件和代价 |
| --- | --- | --- | --- | --- |
| Sedlmair 等 2013 | 816 张图（75 个数据集、4 种降维、3 种散点图），两名编码者给“类别可分性”打分；静态二维、交互三维、散点图矩阵 | 只在人为设计的 entangled 和 grid 数据集上有优势 | “interactive 3D rarely helps but often hurts in terms of poorer class separation and usability”；建议“avoiding interactive 3D scatterplots for DR data, especially for cluster verification tasks” | 要花时间旋转；是数据研究，不是用户实验；比较的是**静态**二维 |
| Poco 等 2011 | 12 人；681 个对象、2993 维的文档集；数簇、按密度排序、列出重叠 | 有两道题三维的正确率显著更高 | 三维更慢：平均 59.3 秒对 40.7 秒 | “the lack of a more compact geometry tends to impair user orientation and interaction in 3D” |
| Tian 等 2021 | 29 种投影技术、质量指标，加 4 位数据科学家的评估 | “scored almost always better but only marginally”；个别技术（H-LLE）第三维有明显增益 | t-SNE 在二维里的解释更清楚；二维不需要交互 | 遮挡和额外的交互负担；只有 4 位专家、简单任务 |
| Wagner Filho 等（2017 研讨会版） | 桌面二维、桌面三维、头显三维；20 人；450 到 620 维 | 沉浸式在点分类、距离感知和离群点任务上有精度优势 | 二维始终最快；主观评分二维 83.1、沉浸式 68.3、桌面三维 61.3；桌面三维与沉浸式多数任务无显著差异 | 作者把部分结果归因于二维的熟悉度和被试没有头显经验 |
| Raja 等 2004 | CAVE 四面墙加头部追踪的三维散点图；4 人 | 沉浸加头部追踪最快 | | “no statistical analysis was performed on the data”，只能算趋势 |

另有 Tory 等 2006（三维几何对象，不是抽象数据）：“3D displays can be very effective for approximate navigation and relative positioning when appropriate cues, such as shadows, are present”，精确任务二维或组合显示更好〔文〕。

### 怎么读这些结果

1. **图谱这一侧，实验证据偏向三维，条件很具体。**〔文〕收益出现在两个条件同时成立时：有运动（旋转）或立体，任务是读连通结构（路径、最短路径、社区）。没有这两个条件，收益消失：Ware 与 Franck 写“A static perspective image may add little”，Alper 等写没有旋转的三维吃亏。这与用户的感觉一致：在这个范围里“帮助不小”，同样错误率下能读的图大约大三倍（1996），到几百上千个节点（2008）。**但三点要一起读**〔推〕：这些实验用的是普通的节点连线图，规模从几十到一千个节点，没有语义类型；用的多是立体加头部耦合或头显；我没有找到带语义类型的知识图谱的三维对照实验。
2. **“记住位置”“精确比较”，三维不占便宜。**〔文〕Kotlarek 等：记忆任务桌面二维更快更准；Marriott 综述：二维更适合精确操作和数值比较；Tory 等：精确任务二维或组合更好。
3. **点云这一侧，几个实验互相不一致，因为量的东西不一样。**〔推〕Sedlmair 等量的是“人看出类别分开了没有”，对手是静态二维，三维差。Poco、Wagner Filho 量的是回答对不对（数簇、点分类、距离），三维更准，但更慢；Tian 等用质量指标和专家评估，三维只有边际改进。第三根轴确实多带了信息（见下表），所以“忠于原数据”的任务三维可以占优；“一眼看出分开”要靠旋转，不占优。两类测量并不矛盾。
4. **层（2.5D）是三维图谱里风险最小的一种。**〔推〕第三根轴是离散的层，每层内读平面，层间连线穿过去；Alper 等的 2.5D 在几个任务里最快，案例里 SkyWalking 和 iCAVE 都这么用。这是对文献和案例的对照，没有哪项实验专门比较过分层与连续三维。
5. **一致的代价是时间、定向、遮挡和设备。**〔文〕几乎每篇都写了其中至少一项；没有读到哪个实验里三维又快又准又不需要设备。

### PCA 的第三根轴：多保留多少〔算〕

用户举的 pca-3d 是线性投影，第三根轴有明确含义（第三个主成分）。下面是整理者自己算的：对四个自带数据集标准化后做 PCA，比较取两根轴和三根轴；脚本是 `scripts/pca_axes.py`。这只回答“数据里多带了多少东西”，不回答“人读不读得懂”。

| 数据集 | 前两个成分累计方差 | 前三个成分累计方差 | 第三根轴多保留 | 邻域保持（k=10）二维 → 三维 |
| --- | --- | --- | --- | --- |
| iris（4 维，150 点） | 0.958 | 0.995 | +0.037 | 0.978 → 0.999 |
| wine（13 维，178 点） | 0.554 | 0.665 | +0.111 | 0.888 → 0.935 |
| breast_cancer（30 维，569 点） | 0.632 | 0.726 | +0.094 | 0.871 → 0.929 |
| digits（64 维，1797 点） | 0.216 | 0.300 | +0.084 | 0.816 → 0.903 |

另一个数来自 Embedding Projector 的演示页自己：200 维的 Word2Vec 10K，PCA 取三根轴，页面写“Total variance described: 8.5%”；取消勾选 Z 轴只取两根，是 6.3%（2026-10-14 在页面里读出）。〔算〕

读法：**第三根轴多带信息是真的**，在这四个数据集上多保留 4 到 11 个百分点的方差，邻域保持涨 0.02 到 0.09；累计方差相对多了 4% 到 39%，数据维度越高相对增益越大（digits 是 39%，Projector 里的词向量是 35%）；**但在高维嵌入上绝对量仍然很小**（8.5%），三根轴不足以把高维结构看清，Embedding Projector 同时提供 t-SNE、UMAP 和最近邻面板，大概就是这个原因（〔推〕，作者没有这样写）。〔算〕〔推〕

### 本库案例里的设计理由和代价

- pca3d 的作者在文档里写“fiddle around with the 3D version to explore your graphics and / or choose the components, and then use pca2d to create a figure for a publication”：**三维用来探索和选成分，二维用来出图**；三维版不能用带透明度的颜色（“colors and palette should not contain an alpha channel”）。〔案〕
- VRNetzer 写“The immersive nature of VR provides a sense of depth that cannot be achieved by other means, such as 2D or non-immersive 3D representations”，理由是立体深度让被遮挡的节点和边的连接不再歧义；它的对照表比较的是工具的功能和大图上的流畅度，**摘录里没有 VR 对二维的用户实验**；它也写 VR 专用的交互隐喻还很少。〔案〕
- iCAVE 引用别人的用户研究作理由，自己写“More user and case studies are needed to understand how best we can make use of immersion, stereoscopy, and 3D”，并写明大网络的显示可能出现“perceptual tension, leading the user to misinterpret closely positioned molecules as related”，即靠得近被误读成有关系；作者没有说这是三维特有的，三维里沿视线方向的靠近更容易这样，是我的推测。〔案〕〔推〕
- GeoGraphViz 的理由是二维图“constraints the dimensions of information that can be presented”，第三维用来放地图层；代价是地理力占主导时“the local cluster … almost completely gone”。〔案〕
- ImAxes 写需要经验验证；Embedding Projector 的论文和博客没有写三维模式的局限（摘录里没有）。〔案〕

**案例里没有一个拿出自己的实验，证明三维优于二维。**设计者的理由都是“二维放不下、看不清”，设计者写明的代价集中在设备、交互隐喻少、近邻误读和没有用户研究。〔案〕

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
| 降维投影 | · | · | · | 1 | 8 | 9 |
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
| 降维投影 | 1 | · | 8 | · | 9 |
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
| 要读图谱的连通结构（路径、社区），图较大，能旋转或有立体 | 三维可以试，**必须带旋转或立体**；静态截图和打印里三维基本没有收益 | Ware 与 Franck 1996、Ware 与 Mitchell 2008、Kotlarek 等 2020、Alper 等 2011〔文〕；iCAVE、VRNetzer〔案〕 |
| 图本来分层（跨层依赖、类型层） | 分层平面（2.5D）：每层是平面，层间连线穿过去 | SkyWalking、iCAVE 的语义层、GeoGraphViz〔案〕；Alper 等 2011 的 2.5D〔文〕；没有专门比较分层与连续三维的实验〔推〕 |
| 看降维后的点云 | 三维用来探索、挑选成分，需要“看出分开”或出图时回到二维，并配深度线索；t-SNE 的结果优先二维 | pca3d、Embedding Projector〔案〕；Sedlmair 等 2013、Tian 等 2021〔文〕；Poco 等 2011 和 Wagner Filho 等说明“忠于原数据”的任务三维可以更准〔文〕 |
| 要记住位置、精确比较数值 | 二维，或二维加三维的组合 | Kotlarek 等 2020、Tory 等 2006、Marriott 等 2018〔文〕 |
| 用动画展示时间或投影的变化 | 演示可以；要做分析，同时给并排的静态视图 | Robertson 等 2008〔文〕 |

## 还没有解决的

- **没有案例带用户研究。** dtour 的作者没有评估用户受益；ImAxes 只有用例演示；VRNetzer、iCAVE 的三维理由是设计者的主张或引用别人的研究。文献里的实证研究（Sedlmair、Robertson、Ware 等）比较的是更窄的任务。这篇文档的“怎么选”多数只有案例证据。
- **三维图谱的实验证据有三个缺口。** 一是实验用的是普通的节点连线图，没有带语义类型的知识图谱；二是 Greffard 等 2011、Gracia 等 2016、St. John 等 2001 的原文页面被人机验证或 403 挡住，没读到，只能通过 Marriott 的综述转述；三是 Ware 与 Mitchell 2008 只读到摘要。
- **笔记软件里的三维图谱没收案例。** Obsidian 等有一批三维图谱插件，建在 3d-force-graph 一类组件上；它们的页面写的是“沉浸、空间记忆”这类宣传，没有比较证据，我没有把它们当案例收。如果用户说的“图谱”是这类，那么上面的实验只能当旁证。〔推〕
- **展示页和图片。** VRNetzer、iCAVE、GeoGraphViz、pca3d 都没有在线展示页（头显、CAVE、R 窗口、仅论文），只能看论文里的图。
- **失真的度量没有读。** Nonato 与 Aupetit 2018 综述了投影的失真类型和量化方法，整理者只读到摘要；Lause 等用邻域和类别保持的度量反驳 Chari 与 Pachter，这个争论怎么判断，本库没有立场。
- **语料偏。** 案例多来自机器学习和生物；金融、物理、社会科学里的高维可视化没有收。图符（Chernoff 脸、星形图）和密集像素两类办法本库没有案例。
- **“维度数”与结构复杂度的关系没有讨论。** [评价理论](evaluation-theory.md)把结构复杂度和理解难度分开；维度数算哪一边，案例里没有证据。
- **边界案例。** Miegakure 是游戏，双曲浏览器不是加维度；它们帮助划边界，但让“十种办法”里的两种只有一个案例。

## 修订记录

- **2026-10-14（用户反馈）**：原来写“加一个空间维度不一定更好”，并说“本库案例里主张用三维或沉浸式载体的只有 ImAxes”，“想上三维或 VR：先证明它比二维加联动更好”。三处都有问题：(1) 证据只有 Sedlmair 等 2013 一篇，它研究的是降维点云，量的是类别可分性，比较的是静态二维对交互三维，不能推到三维图谱；(2) 库里已有的 Embedding Projector（三维模式和深度线索）、SkyWalking（分层的 3D 地图）漏看了；(3) 把举证责任单方面放在三维上。这次补了 11 篇文献的原文摘录（`catalog/literature-evidence.json`，187 条，逐条与页面比对）、4 个案例（pca3d、VRNetzer、iCAVE、GeoGraphViz）、5 个项目条目、一个新字段 `spaces`，并自己算了 PCA 第三根轴的数。结论从“三维不一定更好”改成“按对象和任务读”：图谱的实验证据偏向三维（带旋转或立体时），点云的实验互相不一致。
- **检索的缺陷**：这个议题上我原来的检索是核验我已经知道的工具和论文，没有开放式地找反方证据；用户指出后才补。已写进 `CLAUDE.md`：下一个带方向的结论，先做开放式检索，找支持和反对的证据，再下结论。
