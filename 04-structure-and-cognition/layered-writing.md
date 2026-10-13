# 分层写作：案例里的做法

回答的问题：一篇文章怎样才能承载有层次的认知——高层的概括不吞掉低层的细节，读者能上下走，也能横向走。

> 这一篇记的是**别人**怎么处理分层文本，以及从中能归纳出什么。用户自己写“立体认知”文章的做法，需要用户给材料（文章、规则、自己的话）之后才能写，这里没有替他填。对话里转述过一条原则——“文章不能因为产生了更高层级的抽象，就把原来的概念、细节和判断删除”——那是对话里别的 AI 对用户立场的转述，不是用户原话，下面当作一条可检验的假设来对照案例。

## 案例

| 案例 | 它怎么分层 |
| --- | --- |
| [Wikipedia 摘要式写作](case-evidence.md#wikipedia-summary-style) | 主文章 + 子文章：主文章里留摘要并链接下去，子文章有自己的导语并链回上级 |
| [Explorable Explanations](case-evidence.md#explorable-explanations) | 文字里嵌可调的模型，读者改前提看后果；“可以按兴趣在多个层次上读” |
| [Up and Down the Ladder of Abstraction](case-evidence.md#ladder-of-abstraction) | 从一次具体运行，到一组参数，到全局度量；每一步都能下去、上来 |
| [CmapTools 概念图](case-evidence.md#cmaptools) | 围绕焦点问题把概念按一般到具体排，另标跨联 |
| [Luhmann 的卡片盒](case-evidence.md#zettelkasten) | 一张卡一个单元，排序结构 + 引用 + 关键词索引 |
| [Markmap](case-evidence.md#markmap) | 直接把 Markdown 的标题层级画成可折叠的导图 |
| [图尔敏论证模型](case-evidence.md#toulmin) | 把一个论证拆成主张、依据、保证、支撑、限定词、反驳 |
| [Argdown](case-evidence.md#argdown) | 用文本写论证，生成论证地图；地图隐藏逻辑细节，点“Source”看原文 |
| [GraphRAG](case-evidence.md#graphrag) | 从文本抽图，层级聚类，各层社区摘要，自底向上 |

〔文〕另有 Segel 和 Heer 对叙事性可视化的设计空间分析（《Narrative Visualization: Telling Stories with Data》，IEEE TVCG 2010，读的是作者主页上的 PDF）。它把作者主导和读者主导看成一条光谱，并总结了三种常见的混合结构：马提尼杯（先走一条作者设计好的窄路径，再打开成读者自由探索）、交互式幻灯片（沿叙事一页页走，每页内允许交互）、下钻故事（先给总主题，读者选具体实例看细节）。

## 从案例归纳出的做法

以下每条标了证据类型：〔案〕案例里有设计者原话；〔文〕来自上面那篇文献；〔推〕我的推断。

**1. 每一层都是独立可读的完整单位。〔案〕** Wikipedia 的规则是：子主题文章 “is a complete encyclopedic article in its own right”，并且 “contains its own lead section that is quite similar to the summary in its parent article”。所以向下走不是“展开被省略的半句话”，而是进入另一篇完整的文章。

**2. 上有摘要，下有链接，下也链回上。〔案〕** 父文章的摘要段下面放指向详细文章的链接（Main 模板），子文章“also contains a link back to the parent article”。读者“it only takes a click”就能换层。Ladder of Abstraction 的版本是：图上任意位置可以“step down”到具体的一次运行，也可以往上回到汇总。Argdown 的版本是：地图隐藏逻辑细节，但随时可以点“Source”回到原文。

**3. 摘要是语义概括，要维护，会过时。〔案〕** Wikipedia 明说要避免摘要与子文章不同步：“If the child article changes considerably without updating the parent article, the summary of the child article in the parent article will need to be rewritten to do it justice”，并提供模板标记同步问题。建议的写法顺序是先在子文章里开发新内容，再概括回父文章。这对应本库在 [抽象层级与颗粒度](abstraction-and-granularity.md) 里区分的“表达压缩”和“语义概括”：摘要要自己负责准确，不是机械地删。

**4. 层要对着读者的问题分，而不是对着对象自身分。〔案〕** CmapTools 的作者说层级“depends on the context in which that knowledge is being applied”，所以每张图都要围着一个焦点问题画；Wikipedia 的前提是“different readers have different needs”。

**5. 往上走与往下走同样重要。〔案〕** Victor：“when creating abstractions, stepping down is as important as stepping up”；抽象的目的是“to bring out high-level patterns”，但“this benefit comes at a cost. We can no longer see the car”，也就是失去了对具体对象的直观。分层写作里相应的做法是：每个概括旁边留一个能让人“看到车”的具体例子或链接。〔推〕

**6. 横向联系也要有位置。〔案〕** 概念图作者把跨联看作创造性的来源（“cross-links often represent creative leaps”）；卡片盒用引用和多入口来做横向联系；Markmap 因为只用层级一种关系，就把这些全部丢了。所以“分层文章 + 导图”如果只做树，就会损失横向联系；需要另外的表达（链接、跨联、关系图）。

**7. 论证要把“凭什么”写出来。〔案〕** 图尔敏模型的核心是把“依据为什么能推出主张”（warrant）变成必须写明的角色，并说“the weakest part of any argument is its weakest warrant”。分层文章里，每一级概括的“凭什么”要能在下一级找到。〔推〕

**8. 文字和模型可以对着改。〔案〕** Explorable Explanations：“The goal is to change people's relationship with text... I want text to be used as an environment to think in.” 但它也自己提醒：“the interactivity itself is not really the point”，重点是交互与解释被细腻地整合在一起。

**9. 来源与修订的痕迹要留。〔案〕** Docling 和 Graphiti 都把来源作为数据模型的一部分；卡片盒的先前内容是“被修订而没有消除”（二手分析的德语原文：“durch spätere Eintragungen revidiert, nicht aber eliminiert wurden”）。这与前面那条转述的原则方向一致，但上面三个案例都不是写文章的案例，不能直接当作证据。

## 对应到图

〔案〕文章和结构图之间已有的衔接方式：

- 文章的标题层级直接成为图（Markmap）：简单，但只剩层级。
- 同一批内容块既能排成文档也能摆在画布上（[AFFiNE](case-evidence.md#affine)）：靠“同一对象”衔接。
- 论证从文本生成论证地图，地图再链回文本（Argdown）。
- 图里的节点链到各自的详细页面（Wikipedia 的 Main 链接，Reactome 的子通路方框点进去是自己的图）。

## 一份可对照的清单〔推〕

按上面的案例，检查一篇分层文章时可以问：

1. 每一层单独读，是否说得通？
2. 每个概括能不能点到下一层对应的位置？下一层能不能回到上一层？
3. 概括是否写明了自己省略了什么、适用范围是什么？
4. 概括和下层是否同步？最近一次改下层时有没有改上层？
5. 有没有层级以外的联系（引用、对照、反例），它们放在哪里？
6. 每层的划分对着什么问题？

## 还没有的

- 用户自己的写作规则和样稿。
- 非英语、非技术类的分层写作案例（例如书籍的目录结构、法律条文的层级、教材的螺旋式编排）。
