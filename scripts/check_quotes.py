#!/usr/bin/env python3
"""核对案例证据里的原文摘录：逐条访问 url，检查 quote 是否真的出现在页面文字里。需要联网。

案例证据（catalog/case-evidence.json）里每条摘录都是子智能体从官方页面逐字抄下来的。这个脚本不靠模型，
直接取页面文字做子串比对（忽略空白、大小写、HTML 实体和弯引号），找出抄错或改写过的摘录。

用法:
  python3 scripts/check_quotes.py                       检查 catalog/case-evidence.json 里全部摘录
  python3 scripts/check_quotes.py --id kiali            只检查一个案例
  python3 scripts/check_quotes.py --file x.json         检查另一个同格式的文件（子智能体原始输出，数组形式）
  python3 scripts/check_quotes.py --json out.json       同时写出逐条结果

结果分三种: ok（找到）、MISSING（页面读到了但没有这段文字）、UNREADABLE（页面读不到：403、429、5xx、超时）。
UNREADABLE 不代表摘录有误；MISSING 要人工看是抄错、改写，还是页面由 JS 渲染、静态文字里没有。
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; awesome-structural-sensemaking-linkcheck/1.0)"
CATEGORIES = ("input_material", "entities", "relations", "attributes", "views", "encodings",
              "interactions", "questions", "abstraction", "why", "alternative", "limit")


def norm(s: str) -> str:
    s = html.unescape(s)
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = s.replace(" ", " ").replace("​", "")
    s = re.sub(r"\s+", " ", s)
    # 行内标签（<a>、<em> 等）被去掉后，标点前会多出空格：统一去掉
    s = re.sub(r"\s+([.,;:!?)\]”’'\"])", r"\1", s)
    s = re.sub(r"([(\[“‘])\s+", r"\1", s)
    return s.strip().lower()


def page_text(url: str) -> tuple[str, str]:
    """返回 (状态, 文字)。状态是 'ok' 或错误说明。"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if data[:5] == b"%PDF-":  # PDF：用 pdftotext 取文字
            with tempfile.TemporaryDirectory() as d:
                f = Path(d) / "x.pdf"
                f.write_bytes(data)
                out = subprocess.run(["pdftotext", str(f), "-"], capture_output=True, timeout=120)
            return "ok", norm(out.stdout.decode("utf-8", "replace"))
        raw = data.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}", ""
    except Exception as e:
        return f"{type(e).__name__}", ""
    if re.search(r"\.(js|mjs|json|css|txt|md)(\?|$)", url):
        # 脚本和纯文本不是标签文档：去标签会让 `i < n` 吞掉后面的内容；但脚本里的字符串又可能夹着 <p> 之类的标签。两种文字都留着，哪边找到都算
        stripped = re.sub(r"<[^>]+>", " ", raw)
        return "ok", norm(raw) + " \n " + norm(stripped)
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return "ok", norm(raw)


def quotes_of(case: dict) -> list[tuple[str, int, str, str]]:
    out = []
    for cat in CATEGORIES:
        for i, item in enumerate(case.get(cat) or []):
            if item.get("quote") and item.get("url"):
                out.append((cat, i, item["quote"], item["url"]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=str(ROOT / "catalog" / "case-evidence.json"))
    ap.add_argument("--id")
    ap.add_argument("--json")
    ap.add_argument("--write", action="store_true", help="把核对结果写回证据文件里每条摘录的 check 字段")
    args = ap.parse_args()
    data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    cases = list(data.values()) if isinstance(data, dict) else data
    if isinstance(data, dict):
        for k, v in data.items():
            v.setdefault("id", k)
    if args.id:
        cases = [c for c in cases if c["id"] == args.id]
    jobs = [(c["id"], *q) for c in cases for q in quotes_of(c)]
    urls = sorted({j[4] for j in jobs})
    with ThreadPoolExecutor(max_workers=3) as ex:
        texts = dict(zip(urls, ex.map(page_text, urls)))
    res = []
    for cid, cat, i, quote, url in jobs:
        status, text = texts[url]
        if status != "ok":
            kind = "UNREADABLE"
        else:
            kind = "ok" if norm(quote) in text else "MISSING"
        res.append({"id": cid, "category": cat, "index": i, "status": kind, "page": status, "url": url, "quote": quote})
    tot = len(res)
    cnt = {k: sum(1 for r in res if r["status"] == k) for k in ("ok", "MISSING", "UNREADABLE")}
    for r in res:
        if r["status"] != "ok":
            print(f"{r['status']:<10} {r['id']:<26} {r['category']}#{r['index']}  {r['quote'][:70]!r}  <{r['page']}> {r['url']}")
    print(f"\n共 {tot} 条摘录: ok {cnt['ok']}，MISSING {cnt['MISSING']}，UNREADABLE {cnt['UNREADABLE']}")
    if args.json:
        Path(args.json).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    if args.write:
        if not isinstance(data, dict):
            print("--write 只能用于 case-evidence.json 这种以案例 id 为键的文件")
            return 1
        mapping = {"ok": "ok", "MISSING": "missing", "UNREADABLE": "unreadable"}
        for r in res:
            data[r["id"]][r["category"]][r["index"]]["check"] = mapping[r["status"]]
        Path(args.file).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"已写回 {args.file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
