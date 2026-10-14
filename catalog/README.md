# catalog

整个库的数据层。文档里的项目表格都从这里生成。

| 文件 | 内容 |
| --- | --- |
| `taxonomy.yaml` | 层级与分类的词表。 |
| `projects/*.yaml` | 项目条目，按层级分文件。 |
| `references.yaml` | 理论资料和上游 Awesome 清单。 |
| `diagram-types.yaml` | 结构家族、图形，以及每种图形的展示页。 |
| `directions.yaml` | 研究方向 × 三个层级的跨层索引。 |
| `relationships.yaml` | 项目之间有类型、有证据的关系。 |
| `evaluation-records.yaml` | 评测记录，每条标明证据级别。 |
| `INDEX.md` | 生成的完整索引。 |

## 项目条目的字段

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `id` | 是 | 全库唯一，小写加连字符。 |
| `name` | 是 | 显示名称。 |
| `level` | 是（第四板块除外） | `L1` / `L2` / `L3`。 |
| `section` | 否 | 默认 `ecosystem`；第四板块的工具写 `cognition`，此时不写 `level`。 |
| `category` | 是 | 必须在 `taxonomy.yaml` 里。 |
| `also` | 否 | 其他定位，写成 `L2/data-lineage` 的形式。 |
| `kind` | 是 | `library` / `tool` / `platform` / `spec` / `web-app` / `publication`。 |
| `summary` | 是 | 它是什么。 |
| `focus` | 是 | 值得研究什么。 |
| `repo` | 否 | 开源项目地址。 |
| `demo` | 否 | 展示页地址。 |
| `docs` / `site` | 否 | 文档、官方站点。 |
| `demo_source` | 有 `demo` 时必填 | 展示页从哪里来：`report` / `search` / `maintainer`。 |
| `package` | 否 | `npm:名称` 或 `pypi:名称`。写了它，`scripts/check_registries.py` 就能用包元数据核对仓库、许可证和最近一次发布。 |
| `repo_checked` | 否 | 官方来源指向的仓库与 `repo` 一致的日期，索引里标 ✓。没有它就表示没核对。 |
| `repo_check_via` | 有 `repo_checked` 且没有 `package` 时必填 | 核对依据，写成一句话（例如“项目官网的 GitHub 链接”“Go 模块代理返回的模块来源”）。鼠标悬停在 ✓ 上能看到。依据是官方站点、官方文档或软件包与发行渠道的元数据，不用第三方评测和聚合站。 |
| `facts_checked` | 否 | `summary` 和 `focus` 对照官方页面核对过的日期。索引里“定位与值得研究”一列末尾标 ✓（主要点都有官方依据）或 △（有 `facts_gaps`）。没有它就表示没核对。 |
| `facts_gaps` | 否 | 字符串列表：核对时在官方页面里没找到依据的点，会写进备注。官方页面由 JS 渲染读不到的也记在这里，并注明原因；只是整理者评价性判断的话（“更适合研究……”“不等于……”）不记。找不到依据不等于说法有误。 |
| `demo_none` | 否 | 这个条目本身不存在展示页的原因（规范、采集库、命令行工具等）。有它就不会列入“待收集”。 |
| `demo_checked` | 否 | 展示页访问并确认内容相符的日期，索引里标 ✓。没有它就表示没打开过。 |
| `access` | 否 | `open-source` / `custom-license` / `source-available` / `commercial` / `research-prototype` / `archived` / `unchecked`。默认按 `unchecked` 处理，不表示闭源。 |
| `status` | 否 | `alpha` / `maintenance-mode` / `deprecated` / `needs-check`。 |
| `notes` | 否 | 使用边界、维护状态等需要提醒的事实。 |
| `added_by_maintainer` | 否 | 列出由整理者补充、报告原文没有给出的地址字段。 |

## 案例分析的数据

| 文件 | 内容 |
| --- | --- |
| `cases.yaml` | 案例编码：领域（`field` 领域大类，文件按它分段；`domain` 细标签）、议题、数据结构类别、重点部分、弱化了什么、图形、层级处理。编码是整理者的判断；`ev` 指向依据的官方原文，`thinking` 指向设计者自己写的思路（why / alternative / limit）。 |
| `case-vocab.yaml` | 编码用的词表：议题、结构类别、结构修饰、重点部分、层级处理方式、画法流派（`schools`，带 `bet` / `cost`）、结构来源（`sources`）、领域大类（`fields`）、维度处理（`dim_modes`，案例里写 `dims` 和 `dims_note`，只给“维度比位置轴多”的案例标）。 |
| `case-evidence.json` | 官方页面的原文摘录，按案例 id 和类目存放，每条有 `check`：`ok`（页面文字里找到了）、`missing`、`unreadable`、`unchecked`。 |
| `case-gallery.json` | 每个案例的展示页（`demo`，带 `mode`：`live` 可操作 / `samples` 样例目录 / `video` 视频或导览）、官方图片（`images`，只存地址）、说明网页（`pages`），以及没找到什么（`not_found`）。每个地址有 `check`；展示页另有 `render`（无头 Chromium 打开后的情况）。 |

`python3 scripts/check_gallery.py [--id 案例id]` 逐个访问画廊里的地址，写回状态、标题、图片的类型和像素尺寸；`NODE_PATH=$(npm root -g) node scripts/render_check.js urls.json out.json 截图目录` 用无头 Chromium 打开展示页，再用 `check_gallery.py --render out.json` 合并进来。图片不转存，不收 GitHub 域名上的图（按会话的访问范围）。生成的页面是 `04-structure-and-cognition/case-study/data/case-gallery.md`。 `python3 scripts/case_numbers.py` 重算案例编码的统计（理论文档里手写的数字从这里对）。

`python3 scripts/check_quotes.py [--id 案例id] [--write]` 核对摘录：不靠模型，直接在页面文字里做子串比对。`MISSING` 不一定是抄错，也可能是页面排版或由 JS 渲染。生成的表格在 `04-structure-and-cognition/case-study/data/case-analysis.md` 和 `case-evidence.md`。

## 关于 `access`

标为 `open-source` 的，依据是 npm / PyPI 上该包的许可证属于常见的 OSI 许可（MIT、Apache-2.0、BSD、ISC 等）。这说明的是这个包的许可，整个项目可能还有别的部分采用别的许可（例如平台的商业版）。包的许可证不是常见 OSI 许可的（Elastic-2.0、自定义许可），按实际情况标，并在备注里写明依据。

## 与统一索引问题的对应

每个收录对象尽量回答九个问题。目前的字段只覆盖其中一部分：

| 问题 | 现有字段 |
| --- | --- |
| 对象：它用于理解什么？ | `category`，以及 `directions.yaml` |
| 原始信息：输入是什么？ | 暂无，计划增加 |
| 结构：描述哪类关系与组织？ | 暂无，计划增加 |
| 层级：覆盖什么抽象层级？ | `level` |
| 表达：用什么图形或文字？ | 暂无，计划增加 |
| 交互：支持哪些操作和跨视角切换？ | 暂无，计划增加；目前写在 `focus` 里 |
| 分析：能帮助发现什么？ | 暂无，计划增加 |
| 实现：用了哪些技术？ | `kind`、`relationships.yaml` |
| 评价：优势、局限、边界？ | `notes`、`evaluation-records.yaml` |

计划增加的字段先不要求填，等收集到一批条目、看清哪些信息真有区分度之后再定。

## 核对记录

- 2026-10-13：`scripts/check_links.py --fields demo docs site` 访问了 161 个地址（项目的展示页、文档、站点，加图形范式的展示页和理论资料；不含 GitHub 仓库页）。143 个返回 2xx 或 3xx，18 个没有：observablehq.com 返回 429（15 个）或超时（1 个），ELK Live 返回 502，doi.org 在该环境里解析不了。
- 这一轮之后，项目展示页标 ✓ 的有 53 个，图形范式展示页标 ✓ 的有 28 个。
- 2026-10-13：说明和仓库地址交给 Haiku 子智能体对照官方页面核对（12 批，每批只读、逐字引用原文、不访问 GitHub 页面），之后由主会话复核：说明核对 87 条，其中 45 条标 ✓、37 条标 △（Haiku 判为 partly 的条目里，只有整理者评价性判断没找到依据的，按 ✓ 处理），5 条没读到有效内容（dagre、aerograph、LightRAG、CNCF Landscape2、OpenTelemetry GenAI 约定页），保持无标记；复核时抽查了 10 条引用，对照原页面都能找到；对 Haiku 判为 contradicted 或与现有数据不一致的点，主会话自己重新读了页面（NeoDash 的状态、Flowise 的停运、D2 和 Structurizr 的仓库地址）。仓库地址新增 25 个标 ✓（官网或官方文档里的源码链接、Go 模块代理、Homebrew 记录的下载来源）。仓库没有核对出结果的（CNCF Landscape2、CNCF Landscape、infranodus、oss-compass、embedding-projector、D2、Structurizr DSL）不标 ✓。
- 复核中改正了一处我之前写错的内容：NeoDash 的备注原写“Labs 页面写明已毕业为 Neo4j Dashboards”，页面上并没有这句，实际写的是该文档对应 Labs 里不受官方支持的版本、受支持的版本见 NeoDash commercial。
- 2026-10-13：`scripts/check_registries.py` 查了 55 个带 package 的条目，51 个仓库地址与包声明一致。另外 4 个不一致：Flowise、AutoGen、LangWatch 的包元数据没有声明仓库；Argdown 是凭记忆写错了地址，按包声明改正后一致。现在共 52 个条目标 ✓。
