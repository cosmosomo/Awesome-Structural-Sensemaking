# 贡献指南

## 加一个条目

1. 在 `catalog/projects/` 下选对应层级的文件（`L1.yaml`、`L2.yaml`、`L3.yaml`，第四板块用 `cognition.yaml`），照已有条目的格式加一项。字段说明见 [`catalog/README.md`](catalog/README.md)。
2. 运行 `python3 scripts/build.py`，它会校验数据并更新 `catalog/INDEX.md` 和文档里的表格。
3. 提交 YAML 和被更新的 Markdown。

不要直接改 `<!-- gen:... -->` 与 `<!-- /gen -->` 之间的内容，下次生成会覆盖。

## 开源项目与展示页

每个条目尽量同时给出：

- `repo`：源码仓库。
- `demo`：展示页，即能直接打开看到图形或交互效果的页面，比如在线演示、示例库、公开 Demo。只有文档文字的页面放进 `docs`，不要当展示页。

商业产品没有仓库就不填 `repo`，并把 `access` 标为 `commercial`。

填了 `demo` 就要同时写 `demo_source`：`report`（报告原文给出）、`search`（搜索结果里找到）或 `maintainer`（整理者补充）。展示页访问并确认内容相符后，加 `demo_checked: 日期`；`python3 scripts/check_links.py` 可以批量访问并显示状态码和页面标题，用来辅助核对。

## 记录的原则

- **一个项目只定义一次**。主要定位写在 `level` 和 `category`，其他定位用 `also` 列出，避免同一份资料复制多处。
- **区分证据**。官方文档声称、源码能验证、公开 Demo 可体验、亲自实测，是四种不同的证据，不要统称“已验证”。
- **关系要有证据**。`uses` 只在源码或官方文档确认时记录。“技术上可以配合使用”是研究判断，不是真实依赖，可以写进说明，不要写进 `relationships.yaml`。
- **标明使用边界**。许可证有限制、仍是 Alpha、已归档或维护状态不明的，用 `access`、`status`、`notes` 记录。
- **不确定就留空**。留空会在索引里显示“待补”或“待收集”，比填一个猜的地址好。
- **仓库地址优先用包元数据核对**。项目发布在 npm 或 PyPI 上的，在条目里写 `package`，运行 `python3 scripts/check_registries.py`，仓库一致再加 `repo_checked`。不要凭记忆写仓库地址；凭记忆补的要用 `added_by_maintainer` 标出，并尽快核对。
