# Awesome Structural Sensemaking

系统研究复杂信息、知识与系统的结构表示、分层抽象、可视化表达和交互探索方法，并对底层技术、专项可视化项目、成熟应用及其认知效果建立可持续扩展的分类、索引与评价体系。

> 状态：起步阶段。条目来自一份 2026-10 的调研报告，除标 ✓ 的展示页外尚未逐项核验，见 [证据与核验](#证据与核验)。

## 每个条目收两样东西

- **开源项目**（`repo`）：源码仓库。
- **展示页**（`demo`）：能直接看到效果的演示、示例库或在线站点。

缺哪样，索引里就写“待补”或“待收集”，方便接着补。完整清单见 [`catalog/INDEX.md`](catalog/INDEX.md)。

## 四个板块

| 板块 | 目录 | 研究什么 |
| --- | --- | --- |
| 1 结构表示与可视化理论 | [`01-theory`](01-theory/) | 结构类型、图形流派、视觉编码、布局范式、交互原理，以及各种表示方式的适用边界。 |
| 2 可视化技术与应用生态 | [`02-visualization-ecosystem`](02-visualization-ecosystem/) | 按技术抽象程度分三层：L1 底层可视化技术；L2 针对特定结构与数据的专项可视化项目；L3 成熟应用与综合交互系统。 |
| 3 综合项目索引与横向评测 | [`03-project-reviews`](03-project-reviews/) | 真实项目的可视化覆盖范围、交互能力、优势、局限和使用场景，做可比较的评测。 |
| 4 结构提炼与认知建模 | [`04-structure-and-cognition`](04-structure-and-cognition/) | 如何从信息和认知中识别结构、建立抽象层级、控制颗粒度；不同信息结构的理论讨论也在这里。 |

四个板块是四种不同的研究对象，不是从低到高的步骤，可以从任何一个进入。第二板块是最大的实证主体，但不替代其余三个：第一板块建立分类标准，第三板块做横向比较，第四板块研究信息如何变成可表达的认知结构。

数据放在 [`catalog/`](catalog/)，文档里的项目表格由脚本从数据生成。

## 想找什么，去哪里

| 想知道 | 去 |
| --- | --- |
| 某种结构该用什么图，图的适用边界 | [`01-theory/taxonomy.md`](01-theory/taxonomy.md) |
| 折叠、钻取、多视角这些交互怎么分类 | [`01-theory/interaction-patterns.md`](01-theory/interaction-patterns.md) |
| 某个研究方向在三个层级上各有什么代表 | [`02-visualization-ecosystem`](02-visualization-ecosystem/) 里的跨层索引 |
| 全部项目的仓库和展示页 | [`catalog/INDEX.md`](catalog/INDEX.md) |
| 项目之间怎么比较、怎么测试 | [`03-project-reviews`](03-project-reviews/) |
| 怎么从信息里提炼结构、怎么分层 | [`04-structure-and-cognition`](04-structure-and-cognition/) |
| 怎么加一个条目 | [`CONTRIBUTING.md`](CONTRIBUTING.md) |

## 证据与核验

调研报告做的是基于公开源码和官方文档的广覆盖调研，没有逐项安装、交互测试、性能压测和源码依赖审计。因此：

- 项目的定位和能力描述是报告的归纳，不是实测排名。
- 仓库地址来自报告原文，没有逐个访问。
- 展示页来自报告原文（`demo_source: report`）或事后的搜索结果（`search`）。收集时所在环境不能访问这些站点，所以地址取自搜索结果里出现的页面，没有打开过；访问并确认内容相符的才标 ✓。
- 报告没给出、由整理者补充的地址，在数据里用 `added_by_maintainer` 标出。
- 官方文档声称支持、源码能验证、公开 Demo 可体验、亲自实测，是四种不同的证据，评测记录里分开写。

## 维护

```bash
python3 -m pip install pyyaml
python3 scripts/build.py            # 校验数据并重新生成表格
python3 scripts/build.py --check    # 只检查，数据或表格过期则失败
python3 scripts/check_links.py      # 访问所有地址，输出状态码（需要联网）
```

推送和 PR 时，`.github/workflows/check.yml` 会运行 `build.py --check`。

## 待定

- License 未定。
- 第一板块里的数据结构、语义结构讨论，和第四板块的“信息结构理论”如何分工，见 [`04-structure-and-cognition/information-structure-theory.md`](04-structure-and-cognition/information-structure-theory.md)。
- 条目要不要增加“输入的结构”“采用的图形”“支持的交互”等字段，见 [`catalog/README.md`](catalog/README.md)。
