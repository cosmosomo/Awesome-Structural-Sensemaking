#!/usr/bin/env python3
"""访问 catalog/ 里的地址，输出每个地址的状态码和页面标题。需要联网。

检查范围：项目条目的 repo / demo / docs / site，图形范式的展示页（form:*），理论资料（ref:*）。

用法:
  python3 scripts/check_links.py                       检查全部地址
  python3 scripts/check_links.py --fields demo docs    只检查项目的展示页和文档，图形范式的展示页也会一并检查
  python3 scripts/check_links.py --id likec4           只检查某个项目条目
  python3 scripts/check_links.py --json out.json       同时把结果写成 JSON
  python3 scripts/check_links.py --retry 429           对返回 429 的地址间隔 20 秒后再试一次

只读取并打印结果，不修改任何文件。状态码 200 只说明页面存在；要不要标 `demo_checked`
（项目）或 `checked`（图形范式展示页），还要看标题和正文是否与对象相符，由人确认后手动添加。
被限流（429）、被拦（403）的站点不要换请求头去绕，如实留作未核对。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; awesome-structural-sensemaking-linkcheck/1.0)"


def load(path: str):
    return yaml.safe_load((ROOT / "catalog" / path).read_text(encoding="utf-8"))


def collect(fields: list[str], only_id: str | None) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for p in sorted((ROOT / "catalog" / "projects").glob("*.yaml")):
        for e in yaml.safe_load(p.read_text(encoding="utf-8")) or []:
            if only_id and e["id"] != only_id:
                continue
            for f in fields:
                if e.get(f):
                    out.append((e["id"], f, e[f]))
    if only_id:
        return out
    if "demo" in fields:
        for fam in load("diagram-types.yaml")["families"]:
            for form in fam["forms"]:
                for d in form.get("demos", []):
                    out.append((f"form:{form['id']}", "demo", d["url"]))
    for t in load("references.yaml")["theory"]:
        out.append((f"ref:{t['id']}", "url", t["url"]))
    return out


def probe(item: tuple[str, str, str]) -> dict:
    ident, field, url = item
    res = {"id": ident, "field": field, "url": url, "status": "ERR", "title": "", "final": url}
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read(300_000).decode("utf-8", errors="replace")
            m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
            res.update(status=str(r.status), final=r.geturl(),
                       title=re.sub(r"\s+", " ", m.group(1)).strip()[:100] if m else "")
    except urllib.error.HTTPError as e:
        res["status"] = str(e.code)
    except Exception as e:  # 网络错误、超时、证书问题
        res["title"] = type(e).__name__
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fields", nargs="+", default=["repo", "demo", "docs", "site"])
    ap.add_argument("--id")
    ap.add_argument("--json")
    ap.add_argument("--retry", type=int, help="对返回这个状态码的地址，间隔 20 秒后再试一次")
    args = ap.parse_args()
    items = collect(args.fields, args.id)
    if not items:
        print("没有可检查的地址")
        return 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(probe, items))
    if args.retry:
        again = [i for i, r in enumerate(results) if r["status"] == str(args.retry)]
        if again:
            time.sleep(20)
            for i in again:
                results[i] = probe(items[i])
    bad = 0
    for r in results:
        ok = r["status"].startswith(("2", "3"))
        bad += 0 if ok else 1
        moved = f"  -> {r['final']}" if r["final"] != r["url"] else ""
        print(f"{'ok ' if ok else 'BAD'} {r['status']:>3} {r['id']:<28} {r['field']:<5} {r['url']}{moved}  {r['title']}")
    print(f"\n共 {len(results)} 个地址，异常 {bad} 个")
    if args.json:
        Path(args.json).write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
