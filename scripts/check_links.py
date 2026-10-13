#!/usr/bin/env python3
"""访问 catalog/ 里的地址，输出每个地址的状态码和页面标题。需要联网。

用法:
  python3 scripts/check_links.py                 检查全部地址字段
  python3 scripts/check_links.py --fields demo   只检查展示页
  python3 scripts/check_links.py --id likec4     只检查某个条目

只读取并打印结果，不修改任何文件。确认展示页内容与项目相符后，手动在对应条目加
`demo_checked: 日期`。
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; awesome-structural-sensemaking-linkcheck/1.0)"


def collect(fields: list[str], only_id: str | None) -> list[tuple[str, str, str]]:
    out = []
    for p in sorted((ROOT / "catalog" / "projects").glob("*.yaml")):
        for e in yaml.safe_load(p.read_text(encoding="utf-8")) or []:
            if only_id and e["id"] != only_id:
                continue
            for f in fields:
                if e.get(f):
                    out.append((e["id"], f, e[f]))
    return out


def probe(item: tuple[str, str, str]) -> tuple[str, str, str, str, str]:
    ident, field, url = item
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(200_000).decode("utf-8", errors="replace")
            m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
            title = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
            return ident, field, url, str(r.status), title[:80]
    except urllib.error.HTTPError as e:
        return ident, field, url, str(e.code), ""
    except Exception as e:  # 网络错误、超时、证书问题
        return ident, field, url, "ERR", type(e).__name__


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fields", nargs="+", default=["repo", "demo", "docs", "site"])
    ap.add_argument("--id")
    args = ap.parse_args()
    items = collect(args.fields, args.id)
    if not items:
        print("没有可检查的地址")
        return 0
    bad = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        for ident, field, url, status, title in ex.map(probe, items):
            ok = status.startswith(("2", "3"))
            bad += 0 if ok else 1
            print(f"{'ok ' if ok else 'BAD'} {status:>3} {ident:<28} {field:<5} {url}  {title}")
    print(f"\n共 {len(items)} 个地址，异常 {bad} 个")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
