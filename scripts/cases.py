"""案例分析：加载、校验和生成表格。由 build.py 调用。

数据文件（都在 catalog/ 下）:
  cases.yaml          案例编码（整理者的判断）
  case-vocab.yaml     编码用的词表
  case-evidence.json  官方页面里的原文摘录（子智能体抄的，scripts/check_quotes.py 核对过）
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import yaml

CONFIDENCE = {"high": "官方页面直接写了", "medium": "页面信息支持，归类靠推断", "low": "证据很少"}
ORIGINS = ("project", "external")
EV_CATEGORIES = ("input_material", "entities", "relations", "attributes", "views", "encodings",
                 "interactions", "questions", "abstraction", "why", "alternative", "limit")
EV_TITLES = {"input_material": "处理的材料", "entities": "对象", "relations": "关系", "attributes": "属性与度量",
             "views": "视图", "encodings": "编码", "interactions": "交互", "questions": "回答的问题", "abstraction": "抽象与层级",
             "why": "为什么这样画", "alternative": "原来的问题", "limit": "局限与代价"}
CHECK_MARK = {"ok": "✓", "missing": "？", "unreadable": "？", "unchecked": "？"}


def load_cases(cat: Path) -> dict:
    return {
        "cases": yaml.safe_load((cat / "cases.yaml").read_text(encoding="utf-8")) or [],
        "vocab": yaml.safe_load((cat / "case-vocab.yaml").read_text(encoding="utf-8")),
        "evidence": json.loads((cat / "case-evidence.json").read_text(encoding="utf-8")),
    }


def esc(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def resolve_ev(evidence: dict, cid: str, ref: str) -> list[dict]:
    cat, _, sub = ref.partition(":")
    items = evidence.get(cid, {}).get(cat, [])
    return [x for x in items if sub.lower() in x["quote"].lower()]


def validate_cases(c: dict, project_ids: set[str], form_ids: set[str]) -> list[str]:
    errs: list[str] = []
    v = c["vocab"]
    seen: set[str] = set()
    for case in c["cases"]:
        i = case.get("id")
        if not i:
            errs.append(f"案例缺少 id: {case}")
            continue
        if i in seen:
            errs.append(f"案例 {i}: id 重复")
        seen.add(i)
        for k in ("domain", "issue", "structure", "confidence", "origin"):
            if not case.get(k):
                errs.append(f"案例 {i}: 缺少 {k}")
        if case.get("origin") not in ORIGINS:
            errs.append(f"案例 {i}: origin 必须是 project 或 external")
        elif case["origin"] == "project" and i not in project_ids:
            errs.append(f"案例 {i}: origin 是 project，但 projects/ 里没有这个 id")
        elif case["origin"] == "external":
            if not case.get("name"):
                errs.append(f"案例 {i}: external 案例要写 name")
            if not case.get("urls") or not all(str(u).startswith("https://") for u in case["urls"]):
                errs.append(f"案例 {i}: external 案例要写 https:// 开头的 urls")
        if case.get("confidence") and case["confidence"] not in CONFIDENCE:
            errs.append(f"案例 {i}: confidence 不在 {list(CONFIDENCE)} 里")
        for key, vocab_key in (("issue_types", "issue_types"), ("structure", "structures"), ("modifiers", "modifiers"),
                               ("focus", "focus_parts"), ("abstraction", "abstraction_modes")):
            for x in case.get(key, []):
                if x not in v[vocab_key]:
                    errs.append(f"案例 {i}: {key} 里的 {x} 不在词表 {vocab_key} 里")
        for x in case.get("forms", []):
            if x not in form_ids:
                errs.append(f"案例 {i}: forms 里的 {x} 不在 diagram-types.yaml 里")
        for key in ("ev", "thinking"):
            for ref in case.get(key, []):
                hits = resolve_ev(c["evidence"], i, ref)
                if len(hits) != 1:
                    errs.append(f"案例 {i}: {key}「{ref}」匹配到 {len(hits)} 条摘录（要恰好 1 条）")
        for ref in case.get("thinking", []):
            if ref.partition(":")[0] not in ("why", "alternative", "limit"):
                errs.append(f"案例 {i}: thinking 里的「{ref}」要以 why: / alternative: / limit: 开头")
        if case.get("confidence") == "high" and not case.get("ev"):
            errs.append(f"案例 {i}: confidence 为 high 但没有 ev")
        if case.get("structure") and case.get("focus") is None:
            errs.append(f"案例 {i}: 缺少 focus（没有重点部分的案例写 focus: []）")
    for i in c["evidence"]:
        pass
    return errs


# ---------------------------------------------------------------- 渲染


def case_name(case: dict, projects: dict[str, dict]) -> str:
    return case["name"] if case["origin"] == "external" else projects[case["id"]]["name"]


def case_url(case: dict, projects: dict[str, dict]) -> str | None:
    if case["origin"] == "external":
        return case["urls"][0]
    p = projects[case["id"]]
    return p.get("site") or p.get("docs") or p.get("repo") or p.get("demo")


def name_link(case: dict, projects: dict[str, dict]) -> str:
    n, u = esc(case_name(case, projects)), case_url(case, projects)
    return f"[{n}]({u})" if u else n


def titles(case: dict, key: str, table: dict) -> str:
    out = []
    for x in case.get(key, []):
        t = table[x]
        out.append(t["title"] if isinstance(t, dict) else t)
    return "、".join(out)


def form_names(forms_data: dict) -> dict[str, str]:
    return {f["id"]: f["name"] for fam in forms_data["families"] for f in fam["forms"]}


def structure_cell(case: dict, v: dict) -> str:
    main = v["structures"][case["structure"][0]]["title"]
    rest = "、".join(v["structures"][x]["title"] for x in case["structure"][1:])
    mods = "、".join(v["modifiers"][x] for x in case.get("modifiers", []))
    out = main + (f" + {rest}" if rest else "")
    if mods:
        out += f"<br><sub>{esc(mods)}</sub>"
    if case.get("structure_note"):
        out += f"<br>{esc(case['structure_note'])}"
    return out


def focus_cell(case: dict, v: dict) -> str:
    out = "、".join(v["focus_parts"][x]["title"] for x in case.get("focus", [])) or "—"
    if case.get("dropped"):
        out += f"<br>弱化：{esc(case['dropped'])}"
    return out


def vis_cell(case: dict, forms: dict[str, str], v: dict) -> str:
    bits = []
    if case.get("forms"):
        bits.append("、".join(forms[x] for x in case["forms"]))
    if case.get("views_note"):
        bits.append(esc(case["views_note"]))
    out = "<br>".join(bits) or "—"
    if case.get("abstraction_note"):
        out += f"<br><sub>层级处理：</sub>{esc(case['abstraction_note'])}"
    elif case.get("abstraction") and case["abstraction"] != ["none-stated"]:
        out += "<br><sub>层级处理：</sub>" + "、".join(v["abstraction_modes"][x] for x in case["abstraction"])
    if case.get("fit_note"):
        out += f"<br><sub>匹配与盲区：</sub>{esc(case['fit_note'])}"
    return out


def thinking_cell(case: dict, evidence: dict) -> str:
    lab = {"why": "为什么", "alternative": "原来的问题", "limit": "局限"}
    bits = []
    for ref in case.get("thinking", []):
        hits = resolve_ev(evidence, case["id"], ref)
        if hits:
            h = hits[0]
            bits.append(f"<sub>{lab[ref.partition(':')[0]]}</sub> “{esc(h['quote'])}”")
    return "<br>".join(bits) or "—"


def render_by_structure(d: dict, arg: str) -> str:
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    forms = form_names(d["forms"])
    rows = [x for x in c["cases"] if x["structure"][0] == arg]
    if not rows:
        return "暂无案例。\n"
    out = ["| 案例 | 领域与议题 | 数据结构 | 重点部分 | 可视化与交互 | 设计者的思路（原话） | 依据 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for x in rows:
        issue = esc(x["issue"])
        types = titles(x, "issue_types", v["issue_types"])
        dom = f"{esc(x['domain'])}<br>{issue}" + (f"<br><sub>{esc(types)}</sub>" if types else "")
        conf = {"high": "高", "medium": "中", "low": "低"}[x["confidence"]]
        ev = f"[摘录](case-evidence.md#{x['id']})<br><sub>把握：{conf}</sub>"
        out.append(f"| {name_link(x, projects)} | {dom} | {structure_cell(x, v)} | {focus_cell(x, v)} | {vis_cell(x, forms, v)} | {thinking_cell(x, c['evidence'])} | {ev} |")
    return "\n".join(out) + "\n"


def render_focus_matrix(d: dict, _arg: str) -> str:
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    structs = [s for s in v["structures"] if any(x["structure"][0] == s for x in c["cases"])]
    out = ["| 主要重点 \\ 主类结构 | " + " | ".join(v["structures"][s]["title"] for s in structs) + " |",
           "| --- |" + " --- |" * len(structs)]
    for fk, fv in v["focus_parts"].items():
        cells = []
        for s in structs:
            names = [case_name(x, projects) for x in c["cases"] if x["structure"][0] == s and x.get("focus") and x["focus"][0] == fk]
            cells.append("、".join(esc(n) for n in names) or "·")
        if any(cell != "·" for cell in cells):
            out.append(f"| {fv['title']} | " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


def render_issue_matrix(d: dict, _arg: str) -> str:
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    structs = [s for s in v["structures"] if any(x["structure"][0] == s for x in c["cases"])]
    out = ["| 议题（首位） \\ 主类结构 | " + " | ".join(v["structures"][s]["title"] for s in structs) + " |",
           "| --- |" + " --- |" * len(structs)]
    for ik, iv in v["issue_types"].items():
        cells = []
        for s in structs:
            names = [case_name(x, projects) for x in c["cases"] if x["structure"][0] == s and x.get("issue_types") and x["issue_types"][0] == ik]
            cells.append("、".join(esc(n) for n in names) or "·")
        if any(cell != "·" for cell in cells):
            out.append(f"| {iv['title']} | " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


def render_forms_by_structure(d: dict, _arg: str) -> str:
    c, v = d["cases"], d["cases"]["vocab"]
    forms = form_names(d["forms"])
    out = ["| 主类结构 | 案例数 | 用到的图形（图形×案例数） | 没有对应图形库条目的视图 |", "| --- | --- | --- | --- |"]
    for s, sv in v["structures"].items():
        rows = [x for x in c["cases"] if x["structure"][0] == s]
        if not rows:
            continue
        cnt: dict[str, int] = defaultdict(int)
        for x in rows:
            for f in x.get("forms", []):
                cnt[f] += 1
        used = "、".join(f"{forms[f]}×{n}" for f, n in sorted(cnt.items(), key=lambda t: -t[1])) or "—"
        other = sum(1 for x in rows if x.get("views_note") and not x.get("forms"))
        out.append(f"| {sv['title']} | {len(rows)} | {used} | {other} 个案例只有文字描述的视图 |")
    return "\n".join(out) + "\n"


def render_stats(d: dict, _arg: str) -> str:
    cs = d["cases"]["cases"]
    by_origin = defaultdict(int)
    by_conf = defaultdict(int)
    for x in cs:
        by_origin[x["origin"]] += 1
        by_conf[x["confidence"]] += 1
    domains = sorted({x["domain"] for x in cs})
    return (f"共 {len(cs)} 个案例：目录内项目 {by_origin['project']} 个，其他领域 {by_origin['external']} 个；"
            f"覆盖 {len(domains)} 个领域标签。编码把握：高 {by_conf['high']}、中 {by_conf['medium']}、低 {by_conf['low']}。\n")


def render_evidence(d: dict, _arg: str) -> str:
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    ev = c["evidence"]
    out: list[str] = []
    for x in c["cases"]:
        i = x["id"]
        out.append(f'<a id="{i}"></a>\n\n### {esc(case_name(x, projects))}\n')
        out.append(f"- 领域：{esc(x['domain'])}；议题：{esc(x['issue'])}")
        out.append(f"- 编码：{structure_cell(x, v).split('<br>')[0]}；重点：{focus_cell(x, v).split('<br>')[0]}；把握：{CONFIDENCE[x['confidence']]}")
        if x.get("note"):
            out.append(f"- 说明：{esc(x['note'])}")
        cited = []
        for ref in x.get("ev", []):
            hits = resolve_ev(ev, i, ref)
            if hits:
                cited.append((ref.partition(':')[0], hits[0]))
        if cited:
            out.append("- 编码所依据的原文：")
            for cat, h in cited:
                out.append(f"  - {EV_TITLES[cat]}：“{h['quote']}” [{CHECK_MARK[h['check']]}]({h['url']})")
        e = ev.get(i, {})
        rest = [(cat, it) for cat in EV_CATEGORIES for it in e.get(cat, []) if (cat, it) not in cited]
        if rest:
            out.append("<details><summary>本案例读到的其他原文摘录</summary>\n")
            for cat, it in rest:
                out.append(f"- {EV_TITLES[cat]}：“{it['quote']}” [{CHECK_MARK[it['check']]}]({it['url']})")
            out.append("\n</details>")
        if e.get("not_stated"):
            out.append("- 没读到：" + "；".join(esc(s) for s in e["not_stated"]))
        out.append("")
    return "\n".join(out)


CASE_RENDERERS = {
    "cases": render_by_structure,
    "casefocus": render_focus_matrix,
    "caseissue": render_issue_matrix,
    "caseforms": render_forms_by_structure,
    "casestats": render_stats,
    "caseevidence": render_evidence,
}
