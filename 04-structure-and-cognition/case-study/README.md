# 案例研究：从案例归纳结构类别与可视化流派

用户 2026-10-13 定的方法：理论不是想写就写，而是分析不同领域的案例——哪些被归为哪类数据结构、结构的哪一部分是重点、最后怎样可视化。这个目录是这条研究线的全部材料，按**从结论到依据**分三层。

| 层 | 文件 | 回答什么 |
| --- | --- | --- |
| 结论 | [`information-structure-theory.md`](information-structure-theory.md) | 信息的数据结构有哪些类别，每类回答什么议题、重点是哪一部分、画不出什么；结构从哪来。 |
| 结论 | [`visualization-schools.md`](visualization-schools.md) | 可视化有哪几个流派，各自押注什么、放弃什么，常见搭配，和结构、重点、议题的关系。 |
| 方法 | [`method.md`](method.md) | 怎么收案例、编码、核对原文、做盲编；词表；限制。 |
| 依据（生成） | [`data/case-analysis.md`](data/case-analysis.md) | 全部案例的编码表。 |
| 依据（生成） | [`data/case-evidence.md`](data/case-evidence.md) | 每个案例编码所依据的官方原文摘录。 |
| 依据（生成） | [`data/case-gallery.md`](data/case-gallery.md) | 案例画廊：展示页、官方图片、说明网页，可以一个个点开看。 |

## 怎么读

- 想知道结论：读两篇“结论”。每条结论后面标〔案〕〔文〕〔推〕，〔案〕能点回具体案例。
- 想质疑某条结论：点到 `data/case-analysis.md` 看编码，再点到 `data/case-evidence.md` 看官方原文。
- 想亲眼看某个案例：`data/case-gallery.md`。
- 想加案例或改编码：先看 [`method.md`](method.md) 末尾，改数据在 [`catalog/`](../../catalog/README.md)，`data/` 里的页面是脚本生成的，不要直接改。

## 数据在哪

`catalog/cases.yaml`（编码）、`catalog/case-vocab.yaml`（词表）、`catalog/case-evidence.json`（官方原文）、`catalog/case-gallery.json`（展示页与图片）。字段说明见 [`catalog/README.md`](../../catalog/README.md)。

## 和别的板块的关系

按结构和任务选画法的实用指南在 [`01-theory/choosing-views.md`](../../01-theory/choosing-views.md)，它的每条建议都回到这里的案例。
