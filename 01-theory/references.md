# 经典研究

这方面有成熟的学术基础，可以直接借鉴。

<!-- gen:refs:theory -->
| 资料 | 核心价值 | 对本库的用途 |
| --- | --- | --- |
| [Visualization Analysis and Design](https://www.routledge.com/Visualization-Analysis-and-Design/Munzner/p/book/9781466508910) | 从数据、任务、视觉表达和算法等层次设计可视化。 | 建立统一分类和评价框架。方法：先明确领域问题和用户任务，再做数据抽象、视觉设计与算法实现，而不是直接选图形库。 |
| [The Eyes Have It](https://drum.lib.umd.edu/items/155a868e-fb83-4115-9899-9187ea8c0498) | 按数据类型与交互任务分类，提出“先看全貌，再筛选缩放，按需查看细节”。 | 研究层级探索、导航与信息获取。 |
| [Why Visualization? (task abstraction for analysis and design)](https://www.microsoft.com/en-us/research/publication/why-visualization-task-abstraction-for-analysis-and-design-3/) | 将不同领域的可视化任务抽象成可比较的问题。 | 让跨领域案例共用一套分类。 |
| [Node-Link vs. Matrix Comparison](https://doi.org/10.1109/INFVIS.2004.1) | 比较节点连线图和矩阵在不同网络分析任务中的表现。 | 研究图形选择，而不是只评价视觉效果。（DOI 按报告原样记录，待核对。这一条很可能就是下面 Ghoniem 等人的那篇（InfoVis 2004 会议版，期刊版 2005），标题是整理者按主题对应的，没核对。） |
| [A comparison of the readability of graphs using node-link and matrix-based representations（Ghoniem, Fekete, Castagliola）](https://doi.org/10.1057/palgrave.ivs.9500092) | 受控实验：七类任务、三种规模与密度的随机图，比较节点连线图与矩阵。 | 选图时按规模、密度和任务取舍：小而稀疏的图和路径查找偏向节点连线图，大而稠密的图偏向矩阵。（只读到 Munzner 和 Fekete 的课程材料对它的转述，没读到论文原文；期刊版 Information Visualization 4(2)，2005，114–135，DOI 取自检索结果，未核对。） |
| [A Multi-Level Typology of Abstract Visualization Tasks（Brehmer, Munzner）](https://www.cs.ubc.ca/labs/imager/tr/2013/MultiLevelTaskTypology/) | 用 why / how / what 三个问题描述任务；“找”按目标和位置是否已知分为 lookup、locate、browse、explore，“查询”分为 identify、compare、summarize。 | 给案例里的“议题”提供任务层面的对照词表。（读了 TVCG 版 PDF 的任务部分。） |
| [Narrative Visualization: Telling Stories with Data（Segel, Heer）](https://homes.cs.washington.edu/~jheer/files/narrative.pdf) | 58 个叙事性可视化的设计空间分析；作者主导与读者主导的光谱；马提尼杯、交互式幻灯片、下钻故事三种混合结构。 | 分层写作与交互图结合时，怎样安排作者的路径与读者的探索。（读了作者主页上的 PDF。） |
| [Knowledge Graphs（Hogan 等）](https://arxiv.org/abs/2003.02320) | 知识图谱综述：图数据模型（有向边标签图、异质图、属性图、图数据集）、模式、标识、上下文、推理、归纳。 | 信息结构理论里“一般图”一节的校准：边的上下文（时间、来源）怎样进入模型。（读了数据模型和上下文两节，其余没读。） |
| [The State of the Art in Multilayer Network Visualization（McGee 等）](https://arxiv.org/abs/1902.06815) | 多层网络的定义与相关图模型（二分图、多变量图、动态图）以及可视化手法与任务分类。 | 信息结构理论里“多层与复合”一节的校准：层不是子网络，也不只是属性。（读了前四节的定义、相关模型和任务分类。） |
| [The Design Space of Implicit Hierarchy Visualization: A Survey（Schulz, Hadlak, Schumann）](https://tildeweb.au.dk/au597509/pdfs/tvsurvey.pdf) | 隐式层级可视化（treemap、冰柱图等）的设计空间；任何层级都可表示成嵌套集合。 | 解释层级为什么既可以用连线也可以用包含表达。（读了摘要和引言，其余没读。） |
| [The Theory Underlying Concept Maps and How to Construct and Use Them（Novak, Cañas）](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf) | 概念图的定义与构建流程：焦点问题、命题、层级、跨联。 | 第四板块里提炼层级的一个现成流程；层级取决于所问的问题。（读了定义和构建部分。） |
| [Visualizing High-Dimensional Data: Advances in the Past Decade（Liu, Maljovec, Wang, Bremer, Pascucci）](https://sci.utah.edu/~beiwang/publications/Vis_HD_STAR_BeiWang_2015.pdf) | 200 多篇论文的综述：按信息可视化流水线（数据变换、视觉映射、视图变换）分类，并按交互程度分成计算为主、交互探索、模型操作三类。 | 高维可视化文档里“办法在流水线的哪一步起作用”的校准；引用它对三维散点图与散点矩阵的评估。（读了引言、分类方法，以及感知评估和交互两节；其余没读。） |
| [Information Visualization and Visual Data Mining（Keim）](https://kops.uni-konstanz.de/entities/publication/79d60036-d223-41a5-836f-1c2ab19cfd2a/full) | 按数据类型、可视化技术（标准二三维、几何变换、图符、密集像素、堆叠）、交互与扭曲技术三个维度给可视化与可视数据挖掘分类。 | 校准“维度处理”词表的名字，也说明本库案例里没有图符和密集像素两类。（读了分类一节，其余没读。） |
| [A Review of the State-of-the-Art on Tours for Dynamic Visualization of High-dimensional Data（Lee 等）](https://arxiv.org/abs/2104.08016) | 综述“巡游”：用一串线性投影的动画看四维以上的数据；顺带回顾散点矩阵、平行坐标、热力图和刷选。 | 高维可视化文档里“高维”的定义，以及巡游与其他办法的关系。（读了摘要和引言，其余没读。） |
| [Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices（Sedlmair, Munzner, Tory）](https://eprints.cs.univie.ac.at/3992/) | 两位编码员检查了 75 个数据集、4 种降维方法、3 种散点图形式生成的 816 张图：二维散点图常常“够用”，交互式三维散点图很少有帮助、常常更差。 | “再加一个空间维度有没有用”的实证旁证。（读了摘要和引言，其余没读。） |
| [Effectiveness of Animation in Trend Visualization（Robertson, Fernandez, Fisher, Lee, Stasko）](https://faculty.cc.gatech.edu/~stasko/papers/infovis08-anim.pdf) | 比较动画、叠加轨迹和小多图三种趋势可视化：动画在演示时最快、最让人愉快但出错多，分析时最差，小多图最准。 | 时间或投影序列当作一个“维度”用动画展示时的取舍（Gapminder 气泡图、巡游）。（读了摘要和引言，其余没读。） |
| [Multidimensional Projection for Visual Analytics: Linking Techniques with Distortions, Tasks, and Layout Enrichment（Nonato, Aupetit）](https://qcai.qcri.org/publications/multidimensional-projection-for-visual-analytics-linking-techniques-with-distortions-tasks-and-layout-enrichment) | 多维投影的综述：投影会产生哪些失真、怎样量化评估、怎样用布局增强来识别失真。 | 高维可视化文档里“失真的度量”一项还没解决的说明。（只读到出版页的摘要，没读到全文。） |
<!-- /gen -->

尤其值得借鉴的是 Tamara Munzner 的分析方法：先明确领域问题和用户任务，再做数据抽象、视觉设计与算法实现，而不是直接选一个图形库开始画图。这可以作为后面所有项目研究的共同方法。

前四条的地址来自调研报告，未逐个访问；后面几条是整理者读过的，备注里写了读了哪些部分。
