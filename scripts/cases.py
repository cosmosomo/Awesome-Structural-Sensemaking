"""案例分析：加载、校验和生成表格。由 build.py 调用。

数据文件（都在 catalog/ 下）:
  cases.yaml          案例编码（整理者的判断）
  case-vocab.yaml     编码用的词表
  case-evidence.json  官方页面里的原文摘录（子智能体抄的，scripts/check_quotes.py 核对过）
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
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


# 生成块写进哪个文件，指向案例证据页的相对路径就不同；build.py 在渲染每个文件前设置它（"" 表示就在 data/ 里）
LINK_BASE = ""


def ev_link(case_id: str) -> str:
    return f"{LINK_BASE}case-evidence.md#{case_id}"


def load_cases(cat: Path) -> dict:
    gpath = cat / "case-gallery.json"
    return {
        "gallery": json.loads(gpath.read_text(encoding="utf-8")) if gpath.exists() else {},
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
    field_order = list(v["fields"])
    last_field = -1
    for case in c["cases"]:
        i = case.get("id")
        if not i:
            errs.append(f"案例缺少 id: {case}")
            continue
        if i in seen:
            errs.append(f"案例 {i}: id 重复")
        seen.add(i)
        for k in ("domain", "field", "issue", "structure", "confidence", "origin"):
            if not case.get(k):
                errs.append(f"案例 {i}: 缺少 {k}")
        if case.get("dims") and not case.get("dims_note"):
            errs.append(f"案例 {i}: 写了 dims 就要写 dims_note（数据有几维、每一维在画面上变成什么）")
        if case.get("field") and case["field"] not in v["fields"]:
            errs.append(f"案例 {i}: field {case['field']!r} 不在词表 fields 里")
        elif case.get("field"):
            pos = field_order.index(case["field"])
            if pos < last_field:
                errs.append(f"案例 {i}: 放错了位置，cases.yaml 里案例要按词表 fields 的顺序分段，它属于“{v['fields'][case['field']]['title']}”那一段")
            last_field = max(last_field, pos)
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
                               ("focus", "focus_parts"), ("abstraction", "abstraction_modes"), ("dims", "dim_modes")):
            for x in case.get(key, []):
                if x not in v[vocab_key]:
                    errs.append(f"案例 {i}: {key} 里的 {x} 不在词表 {vocab_key} 里")
        for key, vocab_key in (("schools", "schools"), ("source", "sources")):
            if key not in case:
                errs.append(f"案例 {i}: 缺少 {key}（没有视图的案例 schools 写 []）")
            for x in case.get(key, []):
                if x not in v[vocab_key]:
                    errs.append(f"案例 {i}: {key} 里的 {x} 不在词表 {vocab_key} 里")
        if ("derived" in case.get("modifiers", [])) != ("derived" in case.get("source", [])):
            errs.append(f"案例 {i}: modifiers 里有没有 derived，要和 source 里有没有 derived 一致")
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
    case_ids = {x["id"] for x in c["cases"]}
    for gid, g in c.get("gallery", {}).items():
        if gid not in case_ids:
            errs.append(f"画廊: {gid} 不是案例 id")
            continue
        urls = []
        if g.get("demo"):
            urls.append(g["demo"].get("url"))
            if g["demo"].get("mode") not in ("live", "samples", "video", "login"):
                errs.append(f"画廊 {gid}: 展示页 mode 要是 live / samples / video / login: {g['demo'].get('mode')}")
        urls += [p.get("url") for p in g.get("pages", [])]
        for im in g.get("images", []):
            urls.append(im.get("url"))
            if im.get("kind") not in ("screenshot", "diagram", "figure", "banner"):
                errs.append(f"画廊 {gid}: 图片 kind 不合法: {im.get('kind')}")
            if im.get("shows") not in ("view", "ui", "method", "schema", "concept", "other"):
                errs.append(f"画廊 {gid}: 图片要标 shows（view / ui / method / schema / concept / other）: {im.get('url')}")
        for u in urls:
            if not (isinstance(u, str) and u.startswith("https://") and " " not in u):
                errs.append(f"画廊 {gid}: 地址不合法: {u}")
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
    bits = []
    if case.get("source"):
        bits.append("来源：" + "、".join(v["sources"][x]["title"] for x in case["source"]))
    if case.get("schools"):
        bits.append("画法：" + "、".join(v["schools"][x]["title"] for x in case["schools"]))
    if bits:
        out += f"<br><sub>{esc('；'.join(bits))}</sub>"
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
        ev = f"[摘录]({ev_link(x['id'])})<br><sub>把握：{conf}</sub>"
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


def _count_matrix(rows, rowkey, colkey, row_vocab, col_vocab, corner):
    """行是流派（取案例的主流派），列是另一个维度的取值；格里是案例数。"""
    cols = [k for k in col_vocab if any(colkey(x) == k for x in rows)]
    out = [f"| {corner} | " + " | ".join(col_vocab[k]["title"] for k in cols) + " | 合计 |", "| --- |" + " --- |" * (len(cols) + 1)]
    for rk, rv in row_vocab.items():
        sub = [x for x in rows if rowkey(x) == rk]
        if not sub:
            continue
        cells = [str(sum(1 for x in sub if colkey(x) == k) or "·") for k in cols]
        out.append(f"| {rv['title']} | " + " | ".join(cells) + f" | {len(sub)} |")
    return "\n".join(out) + "\n"


def render_school_count(d: dict, arg: str) -> str:
    """流派（主流派）与结构、重点、议题、来源的交叉计数。arg: structure / focus / issue / source"""
    v = d["cases"]["vocab"]
    rows = [x for x in d["cases"]["cases"] if x.get("schools")]
    spec = {
        "structure": (lambda x: x["structure"][0], v["structures"], "主流派 \\ 主类结构"),
        "focus": (lambda x: (x.get("focus") or [None])[0], v["focus_parts"], "主流派 \\ 首位重点"),
        "issue": (lambda x: (x.get("issue_types") or [None])[0], v["issue_types"], "主流派 \\ 首位议题"),
        "source": (lambda x: x["source"][0], v["sources"], "主流派 \\ 首位来源"),
    }[arg]
    return _count_matrix(rows, lambda x: x["schools"][0], spec[0], v["schools"], spec[1], spec[2])


def render_dims_modes(d: dict, _arg: str) -> str:
    """维度处理方式总表：定义、用到它的案例（主要的加粗）。"""
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    out = ["| 维度处理 | 做法 | 案例（加粗的是主要做法） | 数量 |", "| --- | --- | --- | --- |"]
    for k, m in v["dim_modes"].items():
        rows = [x for x in c["cases"] if k in x.get("dims", [])]
        names = "、".join((lambda s, x=x: f"**{s}**" if x["dims"][0] == k else s)(f"[{esc(case_name(x, projects))}]({ev_link(x['id'])})") for x in rows)
        out.append(f"| {m['title']} | {esc(m['desc'])} | {names or '—'} | {len(rows)} |")
    n = sum(1 for x in c["cases"] if x.get("dims"))
    out.append("")
    out.append(f"{n} 个案例标了维度处理；其余案例没有“维度比位置轴多”的问题，或页面没写。")
    return "\n".join(out) + "\n"


def render_dims_cross(d: dict, arg: str) -> str:
    """主要维度处理与主流派、主类结构的交叉计数。arg: school / structure"""
    c, v = d["cases"], d["cases"]["vocab"]
    rows = [x for x in c["cases"] if x.get("dims") and x.get("schools")] if arg == "school" else [x for x in c["cases"] if x.get("dims")]
    if arg == "school":
        return _count_matrix(rows, lambda x: x["dims"][0], lambda x: x["schools"][0], v["dim_modes"], v["schools"], "主要维度处理 \\ 主流派")
    return _count_matrix(rows, lambda x: x["dims"][0], lambda x: x["structure"][0], v["dim_modes"], v["structures"], "主要维度处理 \\ 主类结构")


def render_school_summary(d: dict, _arg: str) -> str:
    """八个流派的总表：押注什么、放弃什么、用到的案例数（其中主流派）。"""
    c, v = d["cases"], d["cases"]["vocab"]
    out = ["| 流派 | 押注什么 | 放弃什么 | 用到的案例数（其中主流派） |", "| --- | --- | --- | --- |"]
    for k, s in v["schools"].items():
        anyn = sum(1 for x in c["cases"] if k in x.get("schools", []))
        prim = sum(1 for x in c["cases"] if x.get("schools") and x["schools"][0] == k)
        out.append(f"| {s['title']} | {esc(s['bet'])} | {esc(s['cost'])} | {anyn}（{prim}） |")
    return "\n".join(out) + "\n"


def render_school_loo(d: dict, _arg: str) -> str:
    """留一法：拿一个案例的某些编码去预测它的主流派，只用其余案例统计。平局取其余案例里整体更常见的流派，结果与案例顺序无关。"""
    rows = [x for x in d["cases"]["cases"] if x.get("schools") and x.get("focus") and x.get("issue_types")]
    predictors = [
        ("不用任何信息，总猜最常见的流派", lambda c: 0),
        ("首位议题", lambda c: c["issue_types"][0]),
        ("结构来源（首位）", lambda c: c["source"][0]),
        ("主类结构", lambda c: c["structure"][0]),
        ("首位重点部分", lambda c: c["focus"][0]),
        ("重点 + 议题", lambda c: (c["focus"][0], c["issue_types"][0])),
        ("结构 + 来源", lambda c: (c["structure"][0], c["source"][0])),
        ("结构 + 议题", lambda c: (c["structure"][0], c["issue_types"][0])),
    ]
    prime = [r["schools"][0] for r in rows]
    out = ["| 用什么预测主流派 | 留一法预测正确率 |", "| --- | --- |"]
    for label, key in predictors:
        groups: dict = defaultdict(list)
        for i, r in enumerate(rows):
            groups[key(r)].append(i)
        hit = 0
        for i, r in enumerate(rows):
            others = [prime[j] for j in groups[key(r)] if j != i] or [prime[j] for j in range(len(rows)) if j != i]
            cnt = Counter(others)
            base = Counter(prime[j] for j in range(len(rows)) if j != i)
            hit += max(cnt, key=lambda s: (cnt[s], base[s])) == prime[i]
        out.append(f"| {label} | {hit / len(rows):.2f} |")
    out.append("")
    out.append(f"n = {len(rows)}（有视图、有重点和议题编码的案例）。")
    return "\n".join(out) + "\n"


def render_school_cases(d: dict, arg: str) -> str:
    """用到某个流派的案例（主流派是它的加粗）。"""
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    rows = [x for x in c["cases"] if arg in x.get("schools", [])]
    out = []
    for x in rows:
        mark = "**" if x["schools"][0] == arg else ""
        others = "、".join(v["schools"][s]["title"] for s in x["schools"] if s != arg)
        out.append(f"- {mark}[{esc(case_name(x, projects))}]({ev_link(x['id'])}){mark}　{esc(x['domain'])} · "
                   f"{'+'.join(v['structures'][s]['title'] for s in x['structure'])}"
                   + (f" · 同时用：{others}" if others else ""))
    return "\n".join(out) + "\n"


def render_school_pairs(d: dict, _arg: str) -> str:
    """同一个案例里一起出现的流派对（说明哪些画法常常搭配）。"""
    from itertools import combinations
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    pairs: dict[tuple[str, str], list[str]] = defaultdict(list)
    order = list(v["schools"])
    for x in c["cases"]:
        for a, b in combinations(sorted(set(x.get("schools", [])), key=order.index), 2):
            pairs[(a, b)].append(case_name(x, projects))
    out = ["| 搭配 | 案例数 | 案例 |", "| --- | --- | --- |"]
    for (a, b), names in sorted(pairs.items(), key=lambda t: -len(t[1])):
        out.append(f"| {v['schools'][a]['title']} + {v['schools'][b]['title']} | {len(names)} | " + "、".join(esc(n) for n in names) + " |")
    return "\n".join(out) + "\n"


def render_stats(d: dict, _arg: str) -> str:
    cs = d["cases"]["cases"]
    by_origin = defaultdict(int)
    by_conf = defaultdict(int)
    for x in cs:
        by_origin[x["origin"]] += 1
        by_conf[x["confidence"]] += 1
    domains = sorted({x["domain"] for x in cs})
    nfields = len({x["field"] for x in cs})
    return (f"共 {len(cs)} 个案例，归在 {nfields} 个领域大类里（细标签 {len(domains)} 个）；"
            f"来源：目录内项目 {by_origin['project']} 个，补收的 {by_origin['external']} 个。"
            f"编码把握：高 {by_conf['high']}、中 {by_conf['medium']}、低 {by_conf['low']}。\n")


def render_by_field(d: dict, _arg: str) -> str:
    """按领域大类列出案例（括号里是主类结构），并给出大类的定义。"""
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    out = ["| 领域大类 | 数量 | 案例（主类结构） |", "| --- | --- | --- |"]
    for fid, f in v["fields"].items():
        rows = [x for x in c["cases"] if x["field"] == fid]
        names = "、".join(f"{name_link(x, projects)}（{v['structures'][x['structure'][0]]['title']}）" for x in rows)
        out.append(f"| **{esc(f['title'])}**<br><sub>{esc(f['desc'])}</sub> | {len(rows)} | {names} |")
    return "\n".join(out) + "\n"


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


def gallery_images(g: dict) -> list[dict]:
    """能展示的图片：展示的是这个案例画出来的视图（shows 为 view）；核对过是图片；位图宽不小于 180、高不小于 100（更小的看不清），单张不超过 8 MB。
    界面设置面板、架构与方法图、数据模型图、概念示意、模板和宣传页（shows 为别的值）留在数据里，不显示。"""
    out = []
    for im in g.get("images", []):
        if im.get("shows") != "view":
            continue
        ck = im.get("check") or {}
        if ck.get("status") != 200 or not str(ck.get("content_type", "")).startswith("image/"):
            continue
        if (ck.get("width") and ck["width"] < 180) or (ck.get("height") and ck["height"] < 100):
            continue
        if ck.get("bytes") and ck["bytes"] > 8_000_000:  # 单张超过 8 MB 的不显示：读者打开页面会很慢
            continue
        out.append(im)
    return out


def gallery_pages(g: dict) -> list[dict]:
    """说明页：去掉和展示页同一地址的，以及核对时打不开的。"""
    demo = (g.get("demo") or {}).get("url")
    return [p for p in g.get("pages", []) if p["url"] != demo and (p.get("check") or {}).get("status") in (None, 200)]


def render_demo_line(g: dict) -> str:
    demo = g.get("demo")
    if not demo:
        why = (g.get("not_found") or [""])[0]
        if len(why) > 110:
            cut = max(why.rfind(x, 0, 110) for x in ("；", "。", "，", "，"))
            why = why[: cut if cut > 40 else 110] + "…"
        return "- 展示页：没有找到在线展示页" + (f"<sub>（{esc(why)}）</sub>" if why else "")
    ck = demo.get("check") or {}
    rd = demo.get("render") or {}
    title = demo.get("title") or ck.get("title") or "展示页"
    label = {"live": "展示页（可直接操作）", "samples": "展示页（样例目录）", "video": "展示页（演示视频或导览）", "login": "展示页（需要登录）"}[demo.get("mode", "live")]
    bits = [f"- {label}：[{esc(title)}]({demo['url']})"]
    if demo.get("how"):
        bits.append(f"（{esc(demo['how'])}）")
    if rd:
        if rd.get("error"):
            bits.append("<sub> 渲染检查：没打开</sub>")
        else:
            parts = [f"页面文字 {rd.get('text_len', 0)} 字"]
            if rd.get("canvas"):
                parts.append(f"canvas {rd['canvas']} 个")
            if rd.get("svg"):
                parts.append(f"svg {rd['svg']} 个")
            thin = rd.get("text_len", 0) < 200 and not rd.get("canvas") and rd.get("svg", 0) < 3 and not demo["url"].endswith(".svg")
            bits.append(f"<sub> 渲染检查（无头 Chromium，{rd.get('at', '')}）：{'、'.join(parts)}{'；内容很少，可能需要交互或登录' if thin else ''}</sub>")
    elif ck.get("status") == 200:
        bits.append("<sub> 链接可访问，未做渲染检查</sub>")
    elif ck:
        bits.append(f"<sub> 链接检查：{ck.get('status')}</sub>")
    if demo.get("seen"):
        bits.append(f"<sub> 打开后所见：{esc(demo['seen'])}</sub>")
    return "".join(bits)


def render_gallery(d: dict, arg: str) -> str:
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    gal = c.get("gallery", {})
    rows = [x for x in c["cases"] if x["structure"][0] == arg and x["id"] in gal]
    if not rows:
        return "暂无。\n"
    out: list[str] = []
    for x in rows:
        g = gal[x["id"]]
        meta = f"{esc(x['domain'])} · {v['structures'][x['structure'][0]]['title']}"
        if x.get("focus"):
            meta += " · 重点：" + "、".join(v["focus_parts"][f]["title"] for f in x["focus"][:2])
        out.append(f"#### {name_link(x, projects)}\n")
        out.append(f"<sub>{meta}</sub>　{esc(x['issue'])}\n")
        out.append(render_demo_line(g))
        for p in gallery_pages(g):
            why = f"（{esc(p['why'])}）" if p.get("why") else ""
            out.append(f"- 网页：[{esc(p.get('title') or p['url'])}]({p['url']}){why}")
        imgs = gallery_images(g)
        if imgs:
            out.append("")
            out.append(" ".join(f'<a href="{im["url"]}"><img src="{im["url"]}" width="230" alt="{esc(im.get("alt") or x["id"])}"></a>' for im in imgs))
            caps = [f"{esc(im['caption'] or im['alt'])}（[来源页]({im['page']})）" for im in imgs if (im.get("caption") or im.get("alt"))]
            if caps:
                out.append("")
                out.append("<sub>图：" + "；".join(caps) + "</sub>")
        out.append(f"\n<sub>[编码与原文摘录]({ev_link(x['id'])})</sub>\n")
    return "\n".join(out) + "\n"


def render_gallery_index(d: dict, _arg: str) -> str:
    """一张总表：每个案例的展示页、图片数、网页数，方便一个个点开。"""
    c, v = d["cases"], d["cases"]["vocab"]
    projects = {p["id"]: p for p in d["projects"]}
    gal = c.get("gallery", {})
    order = list(v["structures"])
    rows = sorted(c["cases"], key=lambda x: order.index(x["structure"][0]))
    out = ["| 案例 | 领域 | 主结构 | 展示页 | 图 | 网页 |", "|---|---|---|---|---|---|"]
    mode = {"live": "可操作", "samples": "样例目录", "video": "视频/导览", "login": "需登录"}
    for x in rows:
        g = gal.get(x["id"], {})
        demo = g.get("demo")
        dcell = f"[{mode[demo.get('mode', 'live')]}]({demo['url']})" if demo else "—"
        out.append(f"| {name_link(x, projects)} | {esc(x['domain'])} | {v['structures'][x['structure'][0]]['title']} | {dcell} | "
                   f"{len(gallery_images(g)) or '—'} | {len(gallery_pages(g)) or '—'} |")
    return "\n".join(out) + "\n"


def render_gallery_stats(d: dict, _arg: str) -> str:
    c = d["cases"]
    gal = c.get("gallery", {})
    cases = len(c["cases"])
    demos = [g["demo"] for g in gal.values() if g.get("demo")]
    modes = {m: sum(1 for x in demos if x.get("mode") == m) for m in ("live", "samples", "video", "login")}
    rendered = sum(1 for x in demos if x.get("render") and not x["render"].get("error"))
    with_img = sum(1 for g in gal.values() if gallery_images(g))
    n_img = sum(len(gallery_images(g)) for g in gal.values())
    return (f"{cases} 个案例里，{len(demos)} 个有在线展示页（可操作 {modes['live']}、样例目录 {modes['samples']}、视频或导览 {modes['video']}、需要登录 {modes['login']}），"
            f"其中 {rendered} 个用无头 Chromium 实际打开过；{with_img} 个有官方图片，共 {n_img} 张。"
            f"其余 {cases - len(demos)} 个没找到在线展示页（命令行工具、规范、方法类，或官方页面读不到），原因写在各案例下。图片只存地址，不转存。\n")


CASE_RENDERERS = {
    "schoolcount": render_school_count,
    "schoolcases": render_school_cases,
    "schoolpairs": render_school_pairs,
    "schoolloo": render_school_loo,
    "schoolsummary": render_school_summary,
    "dimsmodes": render_dims_modes,
    "dimscross": render_dims_cross,
    "gallery": render_gallery,
    "gallerystats": render_gallery_stats,
    "galleryindex": render_gallery_index,
    "cases": render_by_structure,
    "casefocus": render_focus_matrix,
    "caseissue": render_issue_matrix,
    "caseforms": render_forms_by_structure,
    "casestats": render_stats,
    "casefields": render_by_field,
    "caseevidence": render_evidence,
}
