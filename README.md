# Awesome Structural Sensemaking

系统研究复杂信息、知识与系统的结构表示、分层抽象、可视化表达和交互探索方法，并对底层技术、专项可视化项目、成熟应用及其认知效果建立可持续扩展的分类、索引与评价体系。

> 状态：起步阶段。条目来自一份 2026-10 的调研报告；展示页已用脚本核对一轮，标 ✓ 的页面能打开且标题相符，其余尚未核验，见 [证据与核验](#证据与核验)。

## 每个条目收两样东西

- **开源项目**（`repo`）：源码仓库。
- **展示页**（`demo`）：能直接看到效果的演示、示例库或在线站点。

缺哪样，索引里就写“待补”或“待收集”，方便接着补。完整清单见 [`catalog/INDEX.md`](catalog/INDEX.md)。

## 四个板块

| 板块 | 目录 | 研究什么 |
| --- | --- | --- |
| 1 结构表示与可视化理论 | [`01-theory`](01-theory) | 结构类型、图形流派、视觉编码、布局范式、交互原理，以及各种表示方式的适用边界。 |
| 2 可视化技术与应用生态 | [`02-visualization-ecosystem`](02-visualization-ecosystem) | 按技术抽象程度分三层：L1 底层可视化技术；L2 针对特定结构与数据的专项可视化项目；L3 成熟应用与综合交互系统。 |
| 3 综合项目索引与横向评测 | [`03-project-reviews`](03-project-reviews) | 真实项目的可视化覆盖范围、交互能力、优势、局限和使用场景，做可比较的评测。 |
| 4 结构提炼与认知建模 | [`04-structure-and-cognition`](04-structure-and-cognition) | 如何从信息和认知中识别结构、建立抽象层级、控制颗粒度；不同信息结构的理论讨论也在这里。 |

四个板块是四种不同的研究对象，不是从低到高的步骤，可以从任何一个进入。第一板块讲**怎么画**（图形、编码、布局、交互、怎么选）；信息结构有哪些类别、可视化有哪几个流派，是从案例归纳出来的，放在第四板块的 [`case-study`](04-structure-and-cognition/case-study)，第一板块的选图指南引用它。第二板块是最大的实证主体，但不替代其余三个：第一板块建立分类标准，第三板块做横向比较，第四板块研究信息如何变成可表达的认知结构。

数据放在 [`catalog/`](catalog)，文档里的项目表格由脚本从数据生成。

## 目录地图

文档分三层：**入口**（本页）→ **板块**（每个板块一个目录，自带 README 作索引）→ **专题**（板块下的子目录或文档）。生成的页面（表格、画廊）放在 `data/` 或 `catalog/INDEX.md`，不手改。

```text
README.md                              入口
01-theory/                             板块 1：表示与可视化的理论（概念、分类、编码、布局、交互、评价、怎么选画法）
02-visualization-ecosystem/            板块 2：L1 底层技术 / L2 专项项目 / L3 成熟应用
03-project-reviews/                    板块 3：横向评测
04-structure-and-cognition/            板块 4：结构提炼与认知建模
  extraction/                            结构怎么提炼、怎么分层、怎么写成文章（讨论）
  case-study/                            从案例归纳：信息结构类别、可视化流派（实证）
    data/                                  生成的案例表、原文摘录、展示页画廊
catalog/                               数据（YAML/JSON）与生成的总索引 INDEX.md
scripts/                               校验、生成、核对脚本
```

## 想找什么，去哪里

| 想知道 | 去 |
| --- | --- |
| 某种结构该用什么图，图的适用边界 | [`01-theory/taxonomy.md`](01-theory/taxonomy.md)；按重点部分和任务选画法：[`01-theory/choosing-views.md`](01-theory/choosing-views.md) |
| 折叠、钻取、多视角这些交互怎么分类 | [`01-theory/interaction-patterns.md`](01-theory/interaction-patterns.md) |
| 某个研究方向在三个层级上各有什么代表 | [`02-visualization-ecosystem`](02-visualization-ecosystem) 里的跨层索引 |
| 全部项目的仓库和展示页 | [`catalog/INDEX.md`](catalog/INDEX.md) |
| 项目之间怎么比较、怎么测试 | [`03-project-reviews`](03-project-reviews) |
| 怎么从信息里提炼结构、怎么分层 | [`04-structure-and-cognition`](04-structure-and-cognition) |
| 信息结构有哪些类别、可视化有哪几个流派（从案例归纳），以及一个个打开案例看是什么样子 | [`04-structure-and-cognition/case-study`](04-structure-and-cognition/case-study) |
| 怎么加一个条目 | [`CONTRIBUTING.md`](CONTRIBUTING.md) |

## 证据与核验

调研报告做的是基于公开源码和官方文档的广覆盖调研，没有逐项安装、交互测试、性能压测和源码依赖审计。因此：

- 项目的定位和能力描述是报告的归纳，不是实测排名。
- 仓库地址来自报告原文或由整理者补充。会话对 GitHub 仓库页面有访问范围限制，没有去打开，所以改用官方来源核对：npm 和 PyPI 上包的元数据、项目官网或官方文档里的源码链接、Go 模块代理等。这些来源指向的仓库与条目里的 `repo` 一致的，标 ✓（`repo_checked`，鼠标悬停可看依据）。包元数据同时给出了许可证、是否弃用和最近一次发布时间，已写进条目备注。没找到官方来源的，或来源与条目不一致又没法判定哪个对的（例如 D2 的 `terrastruct/d2` 与 `d2lang/d2`），不标 ✓，并在备注里写明。
- 条目的“定位与值得研究”两句话也对照了官方页面（`facts_checked`）：末尾 ✓ 表示主要点都在官方页面里找到了依据，△ 表示有些点没找到，写在备注里；没有标记的没核对。核对由 Haiku 子智能体逐字引用原文完成，再由主会话复核和抽查。找不到依据不等于说法有误：官方页面由 JS 渲染读不到的，也在其中。
- 展示页来自报告原文（`demo_source: report`）或搜索结果（`search`）。2026-10-13 起能联网后，用 `scripts/check_links.py` 逐个访问，状态 200 且页面标题与条目相符的标 ✓。没有标 ✓ 的有几类：observablehq.com 对这次访问返回 429（限流），其下的展示页没有核对，也没有换请求头去绕；ELK Live 返回 502；标题为空或由前端渲染、无法确认内容的页面；doi.org 在这个环境里解析不了。
- 报告里关于许可证、维护状态的说法，凡能用非 GitHub 的官方页面核对的，已核对，结果和日期写在条目备注里。核对后与报告不一致或找不到依据的（AgentScope Studio、GraphRAG、AgentPrism 的 Alpha 标注）已改为“待核查”；需要 GitHub 才能核实的没有核实。核对中发现 Flowise 官网已宣布停止运营，OpenTelemetry 的 GenAI 语义约定已迁到新仓库，G6 示例页的地址需要加 `/en/`，这些都已更新。
- 报告没给出、由整理者补充的地址，在数据里用 `added_by_maintainer` 标出。
- 官方文档声称支持、源码能验证、公开 Demo 可体验、亲自实测，是四种不同的证据，评测记录里分开写。

## 许可

本仓库的内容（说明文字、数据）和脚本都以 [CC0 1.0](LICENSE) 发布，即放弃版权，可以自由复用。这也是 Awesome 清单的惯例。条目里引用的第三方项目、页面和商标仍归各自所有，项目自己的许可证不受影响。

## 维护

```bash
python3 -m pip install pyyaml
python3 scripts/build.py            # 校验数据并重新生成表格
python3 scripts/build.py --check    # 只检查，数据或表格过期则失败
python3 scripts/check_links.py      # 访问展示页、文档、站点，输出状态码和标题（需要联网）
python3 scripts/check_registries.py # 用 npm / PyPI 的包元数据核对仓库、许可证、最近发布（需要联网）
```

推送和 PR 时，`.github/workflows/check.yml` 会运行 `build.py --check`。

## 待定

- 条目要不要增加“输入的结构”“采用的图形”“支持的交互”等字段，见 [`catalog/README.md`](catalog/README.md)。
