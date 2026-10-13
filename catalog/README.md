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
| `repo_checked` | 否 | 包作者声明的仓库与 `repo` 一致的日期，索引里标 ✓。没有它就表示没核对。 |
| `demo_none` | 否 | 这个条目本身不存在展示页的原因（规范、采集库、命令行工具等）。有它就不会列入“待收集”。 |
| `demo_checked` | 否 | 展示页访问并确认内容相符的日期，索引里标 ✓。没有它就表示没打开过。 |
| `access` | 否 | `open-source` / `custom-license` / `source-available` / `commercial` / `research-prototype` / `archived` / `unchecked`。默认按 `unchecked` 处理，不表示闭源。 |
| `status` | 否 | `alpha` / `maintenance-mode` / `deprecated` / `needs-check`。 |
| `notes` | 否 | 使用边界、维护状态等需要提醒的事实。 |
| `added_by_maintainer` | 否 | 列出由整理者补充、报告原文没有给出的地址字段。 |

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
- 2026-10-13：`scripts/check_registries.py` 查了 55 个带 package 的条目，51 个仓库地址与包声明一致。另外 4 个不一致：Flowise、AutoGen、LangWatch 的包元数据没有声明仓库；Argdown 是凭记忆写错了地址，按包声明改正后一致。现在共 52 个条目标 ✓。
