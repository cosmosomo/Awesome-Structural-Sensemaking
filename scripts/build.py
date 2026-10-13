#!/usr/bin/env python3
"""校验 catalog/ 下的数据，并重新生成由数据派生的 Markdown。

用法:
  python3 scripts/build.py          校验，并写出派生内容
  python3 scripts/build.py --check  只校验；派生内容过期则退出码为 1（适合 CI）

派生内容有两处:
  1. catalog/INDEX.md 整个文件。
  2. 其他 Markdown 里夹在 <!-- gen:种类:参数 --> 和 <!-- /gen --> 之间的块。
     种类: catalog / eval / forms / matrix / refs
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cases import CASE_RENDERERS, load_cases, validate_cases  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / "catalog"

ACCESS = {
    "open-source": "开源",
    "custom-license": "含附加条件的许可证",
    "source-available": "源码可见但有使用限制",
    "commercial": "商业产品",
    "research-prototype": "研究原型",
    "archived": "已归档",
    "unchecked": "未核验",
}
STATUS = {
    "alpha": "Alpha",
    "maintenance-mode": "维护模式",
    "deprecated": "已停止维护",
    "needs-check": "维护状态待核查",
}
KINDS = {
    "library", "tool", "platform", "spec", "web-app", "publication",
}
EVIDENCE = {
    "report": "调研报告（未复核）",
    "docs": "官方文档",
    "code": "源码",
    "demo": "公开 Demo",
    "hands-on": "实测",
}
URL_FIELDS = ("repo", "demo", "docs", "site")
ALLOWED_KEYS = {
    "id", "name", "section", "level", "category", "also", "kind", "summary",
    "focus", "notes", "access", "status", "added_by_maintainer", "demo_checked",
    "demo_source", "demo_none", "package", "repo_checked", "repo_check_via",
    "facts_checked", "facts_gaps", *URL_FIELDS,
}
DEMO_SOURCES = {"report", "search", "maintainer"}
BLOCK = re.compile(r"(<!-- gen:(\w+):([^ ]*) -->\n)(.*?)(<!-- /gen -->)", re.S)


def read(path: Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load() -> dict:
    projects: list[dict] = []
    for p in sorted((CAT / "projects").glob("*.yaml")):
        projects += read(p) or []
    return {
        "tax": read(CAT / "taxonomy.yaml"),
        "projects": projects,
        "refs": read(CAT / "references.yaml"),
        "directions": read(CAT / "directions.yaml"),
        "rels": read(CAT / "relationships.yaml"),
        "evals": read(CAT / "evaluation-records.yaml"),
        "forms": read(CAT / "diagram-types.yaml"),
        "cases": load_cases(CAT),
    }


def primary_key(e: dict) -> str:
    if e.get("section") == "cognition":
        return f"cognition/{e['category']}"
    return f"{e['level']}/{e['category']}"


def valid_scopes(tax: dict) -> set[str]:
    out = {f"{lv}/{c}" for lv, v in tax["levels"].items() for c in v["categories"]}
    out |= {f"cognition/{c}" for c in tax["cognition"]["categories"]}
    return out


def is_url(s) -> bool:
    return isinstance(s, str) and s.startswith("https://") and " " not in s


# ---------------------------------------------------------------- 校验


def validate(d: dict) -> list[str]:
    errs: list[str] = []
    scopes = valid_scopes(d["tax"])
    ids: set[str] = set()
    for e in d["projects"]:
        i = e.get("id")
        if not i:
            errs.append(f"缺少 id: {e}")
            continue
        if i in ids:
            errs.append(f"{i}: id 重复")
        ids.add(i)
        for k in ("name", "summary", "focus", "kind"):
            if not e.get(k):
                errs.append(f"{i}: 缺少 {k}")
        for k in e:
            if k not in ALLOWED_KEYS:
                errs.append(f"{i}: 未知字段 {k}")
        if e.get("kind") and e["kind"] not in KINDS:
            errs.append(f"{i}: kind 不在词表里: {e['kind']}")
        section = e.get("section", "ecosystem")
        if section not in ("ecosystem", "cognition"):
            errs.append(f"{i}: section 必须是 ecosystem 或 cognition")
        elif section == "ecosystem" and e.get("level") not in d["tax"]["levels"]:
            errs.append(f"{i}: level 必须是 L1/L2/L3")
        if e.get("category") is None or primary_key(e) not in scopes:
            errs.append(f"{i}: 分类不在 taxonomy 里: {e.get('level')}/{e.get('category')}")
        for s in e.get("also", []):
            if s not in scopes:
                errs.append(f"{i}: also 里的分类不存在: {s}")
        if e.get("access") and e["access"] not in ACCESS:
            errs.append(f"{i}: access 不在词表里: {e['access']}")
        if e.get("status") and e["status"] not in STATUS:
            errs.append(f"{i}: status 不在词表里: {e['status']}")
        for k in URL_FIELDS:
            if k in e and not is_url(e[k]):
                errs.append(f"{i}: {k} 必须是 https:// 开头的地址")
        for k in e.get("added_by_maintainer", []):
            if k not in URL_FIELDS or k not in e:
                errs.append(f"{i}: added_by_maintainer 里的 {k} 不是已填的地址字段")
        if e.get("demo_checked") and not e.get("demo"):
            errs.append(f"{i}: 有 demo_checked 但没有 demo")
        if e.get("demo") and e.get("demo_source") not in DEMO_SOURCES:
            errs.append(f"{i}: 有 demo 就要标 demo_source（report / search / maintainer）")
        if e.get("demo_source") and not e.get("demo"):
            errs.append(f"{i}: 有 demo_source 但没有 demo")
        if e.get("demo_none") and e.get("demo"):
            errs.append(f"{i}: demo 和 demo_none 不能同时存在")
        if e.get("package") and not re.fullmatch(r"(npm|pypi):[A-Za-z0-9@._/-]+", str(e["package"])):
            errs.append(f"{i}: package 要写成 npm:名称 或 pypi:名称")
        if e.get("repo_checked") and not e.get("repo"):
            errs.append(f"{i}: 有 repo_checked 但没有 repo")
        if e.get("repo_checked") and not (e.get("package") or e.get("repo_check_via")):
            errs.append(f"{i}: 有 repo_checked 就要写明依据：package，或 repo_check_via（官方来源的说明）")
        if e.get("repo_check_via") and not e.get("repo_checked"):
            errs.append(f"{i}: 有 repo_check_via 但没有 repo_checked")
        if e.get("facts_gaps") and not e.get("facts_checked"):
            errs.append(f"{i}: 有 facts_gaps 但没有 facts_checked")
        if "facts_gaps" in e and not (isinstance(e["facts_gaps"], list) and all(isinstance(x, str) and x for x in e["facts_gaps"])):
            errs.append(f"{i}: facts_gaps 必须是非空字符串的列表")

    for r in d["rels"]["relations"]:
        for end in ("from", "to"):
            if r[end] not in ids:
                errs.append(f"关系 {r}: {end} 不是已知项目")
        if r["type"] not in d["rels"]["types"]:
            errs.append(f"关系 {r}: 类型不在 types 里")

    for row in d["directions"]:
        for lv in ("L1", "L2", "L3"):
            for cell in row[lv]:
                if "ref" in cell and cell["ref"] not in ids:
                    errs.append(f"方向 {row['id']}: 引用了不存在的项目 {cell['ref']}")
                if ("ref" in cell) == ("text" in cell):
                    errs.append(f"方向 {row['id']}: 单元格要么 ref 要么 text: {cell}")

    for r in d["evals"]["records"]:
        if r["project"] not in ids:
            errs.append(f"评测记录引用了不存在的项目 {r['project']}")
        if r["evidence"] not in EVIDENCE:
            errs.append(f"评测记录 {r['project']}: evidence 不在词表里")

    form_ids: set[str] = set()
    for fam in d["forms"]["families"]:
        for f in fam["forms"]:
            if f["id"] in form_ids:
                errs.append(f"图形 id 重复: {f['id']}")
            form_ids.add(f["id"])
            for demo in f.get("demos", []):
                if not demo.get("title") or not is_url(demo.get("url")):
                    errs.append(f"图形 {f['id']}: demos 需要 title 和 https 地址")

    for t in d["refs"]["theory"]:
        if not is_url(t["url"]):
            errs.append(f"理论资料 {t['id']}: url 不合法")
    for a in d["refs"]["awesome_lists"]:
        if not is_url(a["repo"]):
            errs.append(f"上游清单 {a['id']}: repo 不合法")
    form_ids = {f["id"] for fam in d["forms"]["families"] for f in fam["forms"]}
    errs += validate_cases(d["cases"], {p["id"] for p in d["projects"]}, form_ids)
    return errs


# ---------------------------------------------------------------- 渲染


def esc(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def a(label: str, url: str, tip: str = "") -> str:
    return f"[{esc(label)}]({url}{' ' + chr(34) + tip + chr(34) if tip else ''})"


def title_link(e: dict) -> str:
    url = e.get("site") or e.get("repo") or e.get("docs") or e.get("demo")
    return a(e["name"], url) if url else esc(e["name"])


def cell_repo(e: dict) -> str:
    if e.get("repo"):
        via = e.get("repo_check_via") or ("%s 包元数据" % e["package"].split(":")[0].replace("pypi", "PyPI") if e.get("package") else "")
        return a("仓库", e["repo"], f"核对依据：{via}" if e.get("repo_checked") else "") + (" ✓" if e.get("repo_checked") else "")
    return "—" if e.get("access") == "commercial" or e.get("kind") in ("spec", "publication") else "待补"


def cell_demo(e: dict) -> str:
    if e.get("demo"):
        return a("展示页", e["demo"]) + (" ✓" if e.get("demo_checked") else "")
    if e.get("demo_none"):
        return "无：" + esc(e["demo_none"])
    return "待收集"


def cell_links(e: dict) -> str:
    parts = []
    if e.get("site") and e["site"] != e.get("demo"):
        parts.append(a("站点", e["site"]))
    if e.get("docs") and e["docs"] != e.get("demo"):
        parts.append(a("文档", e["docs"]))
    return " · ".join(parts) or "—"


def cell_notes(e: dict) -> str:
    bits = []
    if e.get("access") and e["access"] != "unchecked":
        bits.append(ACCESS[e["access"]])
    if e.get("status"):
        bits.append(STATUS[e["status"]])
    if e.get("notes"):
        bits.append(e["notes"])
    if e.get("facts_gaps"):
        bits.append("官方页面没找到依据的说明：" + "、".join(e["facts_gaps"]))
    bits = [x.rstrip("。") if i < len(bits) - 1 else x for i, x in enumerate(bits)]
    return esc("；".join(bits)) if bits else "—"


def mark_facts(e: dict) -> str:
    if not e.get("facts_checked"):
        return ""
    return " △" if e.get("facts_gaps") else " ✓"


def project_table(entries: list[dict], scope: str) -> str:
    if not entries:
        return "暂无条目。\n"
    out = ["| 项目 | 定位与值得研究 | 开源项目 | 展示页 | 站点 / 文档 | 备注 |",
           "| --- | --- | --- | --- | --- | --- |"]
    for e in entries:
        name = title_link(e)
        if primary_key(e) != scope:
            name += f"<br>（主分类 {primary_key(e)}）"
        text = esc(e["summary"]) + "<br>" + esc(e["focus"]) + mark_facts(e)
        out.append(f"| {name} | {text} | {cell_repo(e)} | {cell_demo(e)} | {cell_links(e)} | {cell_notes(e)} |")
    return "\n".join(out) + "\n"


def entries_for(d: dict, scope: str) -> list[dict]:
    primary = [e for e in d["projects"] if primary_key(e) == scope]
    others = [e for e in d["projects"] if primary_key(e) != scope and scope in e.get("also", [])]
    return primary + others


def render_catalog(d: dict, arg: str) -> str:
    return project_table(entries_for(d, arg), arg)


def render_eval(d: dict, arg: str) -> str:
    byid = {e["id"]: e for e in d["projects"]}
    rows = [r for r in d["evals"]["records"] if r["round"] == arg]
    out = ["| 项目 | 最值得借鉴 | 主要适用范围 | 需要进一步验证 | 依据 |", "| --- | --- | --- | --- | --- |"]
    for r in rows:
        out.append(f"| {title_link(byid[r['project']])} | {esc(r['strengths'])} | {esc(r['scope'])} | "
                   f"{esc(r['to_verify'])} | {EVIDENCE[r['evidence']]} |")
    return "\n".join(out) + "\n"


def render_forms(d: dict, _arg: str) -> str:
    out = ["| 结构家族 | 图形 | 展示页 |", "| --- | --- | --- |"]
    for fam in d["forms"]["families"]:
        for f in fam["forms"]:
            demos = f.get("demos", [])
            cell = "、".join(a(x["title"], x["url"]) + (" ✓" if x.get("checked") else "") for x in demos) or "待收集"
            out.append(f"| {esc(fam['title'])} | {esc(f['name'])} | {cell} |")
    return "\n".join(out) + "\n"


def render_matrix(d: dict, _arg: str) -> str:
    byid = {e["id"]: e for e in d["projects"]}

    def cell(items: list[dict]) -> str:
        parts = []
        for it in items:
            if "ref" in it:
                parts.append(title_link(byid[it["ref"]]))
            else:
                parts.append(esc(it["text"]))
        return "、".join(parts)

    out = ["| 研究方向 | L1 通用技术能力 | L2 专项项目或可视化 | L3 综合应用 |", "| --- | --- | --- | --- |"]
    for row in d["directions"]:
        out.append(f"| {esc(row['title'])} | {cell(row['L1'])} | {cell(row['L2'])} | {cell(row['L3'])} |")
    return "\n".join(out) + "\n"


def render_refs(d: dict, arg: str) -> str:
    if arg == "theory":
        out = ["| 资料 | 核心价值 | 对本库的用途 |", "| --- | --- | --- |"]
        for t in d["refs"]["theory"]:
            use = t["use"] + (f"（{t['notes']}）" if t.get("notes") else "")
            out.append(f"| {a(t['title'], t['url'])} | {esc(t['summary'])} | {esc(use)} |")
    else:
        out = ["| 上游清单 | 优先用于 |", "| --- | --- |"]
        for x in d["refs"]["awesome_lists"]:
            out.append(f"| {a(x['title'], x['repo'])} | {esc(x['use'])} |")
    return "\n".join(out) + "\n"


RENDERERS = {
    **CASE_RENDERERS,
    "catalog": render_catalog,
    "eval": render_eval,
    "forms": render_forms,
    "matrix": render_matrix,
    "refs": render_refs,
}


def stats(d: dict) -> dict:
    ps = d["projects"]
    return {
        "total": len(ps),
        "repo": sum(1 for e in ps if e.get("repo")),
        "demo": sum(1 for e in ps if e.get("demo")),
        "demo_none": sum(1 for e in ps if e.get("demo_none")),
        "repo_checked": sum(1 for e in ps if e.get("repo_checked")),
        "facts_ok": sum(1 for e in ps if e.get("facts_checked") and not e.get("facts_gaps")),
        "facts_gaps": sum(1 for e in ps if e.get("facts_checked") and e.get("facts_gaps")),
        "demo_checked": sum(1 for e in ps if e.get("demo_checked")),
    }


def render_index(d: dict) -> str:
    s = stats(d)
    out = [
        "# 项目索引",
        "",
        "> 本文件由 `scripts/build.py` 根据 `catalog/` 生成，请改 YAML，不要直接改这里。",
        "> 条目信息来自 2026-10 调研报告。展示页来自报告原文或事后的搜索结果，除标 ✓ 的外都没有实际访问过。",
        "",
        f"共 {s['total']} 个条目；有开源项目地址 {s['repo']} 个，有展示页 {s['demo']} 个"
        f"（其中 {s['demo_checked']} 个已访问核对，标 ✓）；另有 {s['demo_none']} 个本身没有展示页。",
        f"有 {s['repo_checked']} 个开源项目地址已核对（标 ✓，鼠标悬停可看依据）：npm / PyPI 的包元数据、项目官网或官方文档里的源码链接，或 Go 模块代理指向的仓库与这里一致。其余没有核对，GitHub 页面本身没有访问。",
        f"“定位与值得研究”一列末尾的标记：✓ 表示这段说明的主要点在官方页面里都找到了依据（{s['facts_ok']} 个）；△ 表示有些点没找到依据，写在备注里（{s['facts_gaps']} 个）；没有标记的没核对过。找不到依据不等于说法有误，官方页面由 JS 渲染读不到的、或者只是整理者的评价性判断，也会落在这一类。",
        "",
        "“待补”表示开源项目地址缺失，“待收集”表示展示页缺失或还没找到；“无：…”表示这个条目本身不存在展示页（如规范、采集库、命令行工具）；商业产品、规范和刊物没有仓库，用“—”表示。",
        "",
    ]
    for lv, v in d["tax"]["levels"].items():
        out += [f"## {lv} {v['title']}", ""]
        for c, title in v["categories"].items():
            scope = f"{lv}/{c}"
            out += [f"### {title}", "", f"<sub>{scope}</sub>", "", project_table(entries_for(d, scope), scope)]
    out += [f"## 第四板块 {d['tax']['cognition']['title']}", ""]
    for c, title in d["tax"]["cognition"]["categories"].items():
        scope = f"cognition/{c}"
        out += [f"### {title}", "", f"<sub>{scope}</sub>", "", project_table(entries_for(d, scope), scope)]
    out += ["## 项目之间的关系", "", "只记录报告或官方文档明确说明的关系。", "",
            "| 项目 | 关系 | 对象 | 依据 |", "| --- | --- | --- | --- |"]
    byid = {e["id"]: e["name"] for e in d["projects"]}
    for r in d["rels"]["relations"]:
        out.append(f"| {esc(byid[r['from']])} | {r['type']} | {esc(byid[r['to']])} | {esc(r['evidence'])} |")
    out += ["", "## 上游 Awesome 清单", "", render_refs(d, "awesome")]
    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------- 生成与检查


def markdown_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]


def generate(d: dict) -> dict[Path, str]:
    outputs: dict[Path, str] = {CAT / "INDEX.md": render_index(d)}
    for p in markdown_files():
        if p == CAT / "INDEX.md":
            continue
        text = p.read_text(encoding="utf-8")

        def sub(m: re.Match) -> str:
            kind, arg = m.group(2), m.group(3)
            if kind not in RENDERERS:
                raise SystemExit(f"{p.relative_to(ROOT)}: 未知的生成块种类 {kind}")
            return m.group(1) + RENDERERS[kind](d, arg) + m.group(5)

        new = BLOCK.sub(sub, text)
        if new != text:
            outputs[p] = new
    return outputs


def relative_link_errors(outputs: dict[Path, str]) -> list[str]:
    errs = []
    link = re.compile(r"\]\(([^)\s]+)\)")
    for p in markdown_files():
        text = outputs.get(p) or p.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for m in link.finditer(text):
            t = m.group(1)
            if re.match(r"^(https?:|mailto:|#)", t):
                continue
            target = (p.parent / t.split("#")[0]).resolve()
            if not target.exists() and target not in outputs:
                errs.append(f"{p.relative_to(ROOT)}: 相对链接不存在 {t}")
    return errs


def main() -> int:
    check = "--check" in sys.argv
    d = load()
    errs = validate(d)
    if errs:
        print("数据校验失败:")
        for e in errs:
            print("  -", e)
        return 1
    outputs = generate(d)
    link_errs = relative_link_errors(outputs)
    if link_errs:
        print("链接检查失败:")
        for e in link_errs:
            print("  -", e)
        return 1
    changed = []
    for path, text in outputs.items():
        cur = path.read_text(encoding="utf-8") if path.exists() else None
        if cur != text:
            changed.append(path.relative_to(ROOT))
            if not check:
                path.write_text(text, encoding="utf-8")
    s = stats(d)
    print(f"校验通过: {s['total']} 个条目，开源项目 {s['repo']}（已核对 {s['repo_checked']}），展示页 {s['demo']}（已核对 {s['demo_checked']}）")
    if changed:
        verb = "已过期（请运行 python3 scripts/build.py）" if check else "已更新"
        for c in changed:
            print(f"  {verb}: {c}")
        return 1 if check else 0
    print("派生内容均为最新")
    return 0


if __name__ == "__main__":
    sys.exit(main())
