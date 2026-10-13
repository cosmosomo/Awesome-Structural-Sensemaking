# 板块 4 结构提炼与认知建模

一个复杂结构在被画出来之前，究竟如何从原始信息中被发现、定义、组织和验证。这部分与“画图”距离最远，但与最终研究目标联系最紧密。

两个方向都收：从信息里提炼结构，以及这些结构本身是什么。

| 文件 | 内容 |
| --- | --- |
| [`extraction-layers.md`](extraction-layers.md) | 结构提炼的七个研究层次。 |
| [`abstraction-and-granularity.md`](abstraction-and-granularity.md) | 五种不同的“分层”，两类抽象操作，以及抽象时要保留什么。 |
| [`information-structure-theory.md`](information-structure-theory.md) | 信息结构有哪些类别，每类回答什么议题、重点是哪一部分、怎么画、画不出什么。从案例归纳。 |
| [`case-analysis-method.md`](case-analysis-method.md) | 案例分析的方法：怎么收案例、编码、核对摘录，以及限制。 |
| [`visualization-schools.md`](visualization-schools.md) | 可视化流派：从案例归纳的八种画法，各自押注什么、放弃什么，和结构、重点、议题、结构来源的关系，常见搭配。 |
| [`case-analysis.md`](case-analysis.md) | 84 个案例的编码表：领域、议题、数据结构、结构来源、重点部分、可视化与交互、画法流派、设计者的思路。 |
| [`case-evidence.md`](case-evidence.md) | 每个案例编码所依据的官方原文摘录。 |
| [`case-gallery.md`](case-gallery.md) | 案例画廊：每个案例的展示页、官方图片、说明网页，可以一个个点开看是什么样子。 |
| [`layered-writing.md`](layered-writing.md) | 分层写作：别人怎么处理分层文本，以及能归纳出的做法。 |

## 三类输入不能用同一套方法

| 原始材料 | 结构提炼特点 | 主要困难 |
| --- | --- | --- |
| 代码、配置、日志、数据库 | 已有相对明确的技术语法或字段结构 | 如何从技术结构理解业务及系统意义 |
| 文档、论文、网站、市场资料 | 部分结构显式存在，部分需要语义提取 | 概念消歧、关系准确性、来源一致性 |
| 思想、讨论、经验、认知框架 | 结构边界往往尚未确定 | 抽象层次、粒度选择、思想保全与持续重构 |

程序的导入依赖可以通过代码解析得到；而“某个技术为什么具有长期价值”需要论证和判断，无法像解析代码一样直接得到唯一正确的结构。

## 工具与项目

> 项目事实来自 2026-10 调研报告，未逐项核验。

### 结构提取

<!-- gen:catalog:cognition/information-extraction -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Tree-sitter](https://github.com/tree-sitter/tree-sitter) | 程序源代码的语法树与增量解析。<br>输入是源码。语法事实不直接等于架构语义。 ✓ | [仓库](https://github.com/tree-sitter/tree-sitter "核对依据：npm 包元数据") ✓ | [展示页](https://tree-sitter.github.io/tree-sitter/7-playground.html) ✓ | — | 开源 |
| [Docling](https://github.com/docling-project/docling) | PDF、文档等的版面、标题、表格及文档结构提取。<br>输入是文档。文档结构不等于知识结构。 ✓ | [仓库](https://github.com/docling-project/docling "核对依据：PyPI 包元数据") ✓ | [展示页](https://huggingface.co/spaces/docling-project/SmolDocling-256M-Demo) | — | 开源；展示页是 SmolDocling 视觉语言模型的演示，不是 Docling 库本身。 |
| [Docling Graph](https://github.com/docling-project/docling-graph) | 从结构化文档内容进一步提取结构化实体与关系。<br>需要约束关系类型和语义准确性。 ✓ | [仓库](https://github.com/docling-project/docling-graph "核对依据：PyPI 包元数据") ✓ | 待收集 | [文档](https://docling-project.github.io/docling-graph/) | 开源 |
| [Understand Anything](https://understand-anything.com/)<br>（主分类 L2/software-architecture） | 文件、函数、类、调用关系与知识文档的交互知识图。<br>架构分层视图、业务领域视图、语义搜索、引导式理解、变更影响分析。对 Markdown 知识库先解析显式链接和类别，再借助模型发现隐式关系，生成带类型的知识网络。与“复杂认知地图”相关度高。 △ | [仓库](https://github.com/Egonex-AI/Understand-Anything "核对依据：项目官网 understand-anything.com 的 GitHub 链接") ✓ | [展示页](https://understand-anything.com/) ✓ | — | 以上能力来自项目文档的功能说明，未逐项做交互和输出准确率评测；据文档，结构事实部分采用 Tree-sitter 等确定性解析；官方页面没找到依据的说明：变更影响分析、先解析显式链接再用模型发现隐式关系、带类型的知识网络 |
<!-- /gen -->

### 多层知识建模

GraphRAG 的路径是：文本片段，实体、关系与声明提取，图社区发现与层级聚类，各层级社区摘要，全局与局部检索。但图社区层级不等于认知的逻辑抽象层级：算法可以发现一群连接紧密的概念，却未必能证明其中存在“系统—子系统”“原理—机制”“类别—实例”这样的关系。它可以作为认知建模的辅助工具，不应直接替代语义分层。

<!-- gen:catalog:cognition/multilevel-knowledge-modeling -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) | 对非结构化文本做实体关系抽取、社区分层、社区摘要。<br>路径：文本片段、实体关系与声明提取、图社区发现与层级聚类、各层级社区摘要、全局与局部检索。图社区层级不等于认知的逻辑抽象层级，只能作为辅助，不能替代语义分层。 ✓ | [仓库](https://github.com/microsoft/graphrag "核对依据：PyPI 包元数据") ✓ | 无：命令行流水线，官方建议导出后用 Gephi 查看 | [站点](https://microsoft.github.io/graphrag/) · [文档](https://microsoft.github.io/graphrag/visualization_guide/) | 开源；维护状态待核查；报告称官方文档显示仓库主要处于维护模式；microsoft.github.io/graphrag 的首页、get_started、overview 页里没有找到这样的表述，GitHub README 未核实（2026-10-13）。官方可视化指南建议把图导出为 GraphML 后用 Gephi 查看，没有专门的可视化器。 |
| [LightRAG](https://github.com/HKUDS/LightRAG) | 图结构检索与知识网络可视化。<br>检索结构与认知模型并不完全相同。 | [仓库](https://github.com/HKUDS/LightRAG "核对依据：PyPI 包元数据") ✓ | 无：WebUI 需自行部署，没有公开在线演示 | — | 开源 |
<!-- /gen -->

### 动态与演化的知识结构

Graphiti 把时间与原始来源纳入结构模型。例如某份资料曾说技术 A 依赖项目 B，后来版本更新不再采用 B：只保存当前状态的静态图会直接删除旧依赖，而时间化的知识模型可以保留关系有效期及其来源，区分“过去成立”“现在成立”和“存在冲突”。

<!-- gen:catalog:cognition/evolving-knowledge-structures -->
| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |
| --- | --- | --- | --- | --- | --- |
| [Graphiti](https://github.com/getzep/graphiti) | 带时间属性的实体和关系，保留来源。<br>时间化事实、原始 Episode、增量知识更新、显式或学习得到的关系类型；能区分“过去成立”“现在成立”和“存在冲突”。 △ | [仓库](https://github.com/getzep/graphiti "核对依据：PyPI 包元数据") ✓ | 无：开源库本身没有可视化界面，图浏览器在需账号的 Zep 控制台里 | [文档](https://help.getzep.com/graphiti/getting-started/overview) | 开源；官方页面没找到依据的说明：学习得到的关系类型 |
<!-- /gen -->

## 待展开的主题

- 用户自己写“立体认知”文章的做法：需要用户的材料，见 [分层写作](layered-writing.md) 末尾。
- 概念与关系建模：如何提炼概念、类别、实体、属性与关系。目前只有 [CmapTools 的构建流程](case-evidence.md#cmaptools)（焦点问题、15 到 25 个概念、停车场、初稿、找跨联、反复修订）可以参照。
- 来源追溯与保真：从高层结构回到原始判断、细节和证据。案例里有 Docling、Graphiti、Wikipedia 摘要式写作的做法，还没有归纳成一套。
- 更多“复杂信息与认知结构”类的案例，尤其是设计者写了理由的。
