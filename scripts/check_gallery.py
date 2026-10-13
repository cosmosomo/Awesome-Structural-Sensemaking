#!/usr/bin/env python3
"""核对案例画廊里的地址：展示页、网页、图片。需要联网。

catalog/case-gallery.json 里每个案例有 demo（展示页）、images（官方图片地址）、pages（说明页）。
这个脚本逐个访问，写回 check 字段：
  展示页和网页：HTTP 状态、最终地址、页面标题；
  图片：HTTP 状态、Content-Type 是否 image/*、字节数、像素宽高（用 Pillow 读）。
渲染检查（JS 页面打开后有没有内容）由 scripts/render_check.js 做，结果用 --render 合并进来。

用法:
  python3 scripts/check_gallery.py                 核对全部并写回
  python3 scripts/check_gallery.py --id kiali      只核对一个案例
  python3 scripts/check_gallery.py --render r.json 把 render_check.js 的输出合并进 demo.render
只读访问；遇到 403、429、5xx 记为读不到，不换请求头去绕。
"""
from __future__ import annotations

import argparse
import html
import io
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "catalog" / "case-gallery.json"
UA = "Mozilla/5.0 (compatible; awesome-structural-sensemaking-linkcheck/1.0)"
DATE = "2026-10-13"


def fetch(url: str, limit: int = 12_000_000) -> tuple[int | None, str, str, bytes]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.geturl(), r.headers.get("Content-Type", ""), r.read(limit)
    except urllib.error.HTTPError as e:
        return e.code, url, "", b""
    except Exception as e:  # noqa: BLE001
        return None, url, f"{type(e).__name__}", b""


def page_check(url: str) -> dict:
    st, final, ctype, body = fetch(url, 400_000)
    out = {"status": st, "at": DATE}
    if final != url:
        out["final"] = final
    if body and "html" in ctype.lower():
        m = re.search(rb"<title[^>]*>(.*?)</title>", body, re.S | re.I)
        if m:
            out["title"] = re.sub(r"\s+", " ", html.unescape(m.group(1).decode("utf-8", "replace"))).strip()[:120]
    return out


def image_check(url: str) -> dict:
    st, final, ctype, body = fetch(url)
    out = {"status": st, "content_type": ctype.split(";")[0].strip(), "bytes": len(body), "at": DATE}
    if body and out["content_type"].startswith("image/") and "svg" not in out["content_type"]:
        try:
            from PIL import Image
            with Image.open(io.BytesIO(body)) as im:
                out["width"], out["height"] = im.size
        except Exception as e:  # noqa: BLE001
            out["decode_error"] = type(e).__name__
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--id")
    ap.add_argument("--render")
    args = ap.parse_args()
    data = json.loads(FILE.read_text(encoding="utf-8"))
    if args.render:
        for r in json.loads(Path(args.render).read_text(encoding="utf-8")):
            g = data.get(r["id"])
            if g and g.get("demo") and g["demo"]["url"] == r["url"]:
                g["demo"]["render"] = {k: r.get(k) for k in ("status", "final", "title", "text_len", "canvas", "svg", "img", "page_errors", "error") if r.get(k) is not None}
                g["demo"]["render"]["at"] = DATE
        FILE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print("已合并渲染结果")
        return 0
    jobs = []
    for cid, g in data.items():
        if args.id and cid != args.id:
            continue
        if g.get("demo"):
            jobs.append((g["demo"], page_check))
        for p in g.get("pages", []):
            jobs.append((p, page_check))
        for im in g.get("images", []):
            jobs.append((im, image_check))
    with ThreadPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(lambda j: j[1](j[0]["url"]), jobs))
    bad = 0
    for (item, _), res in zip(jobs, results):
        item["check"] = res
        ok = res.get("status") == 200 and (not item.get("kind") or res.get("content_type", "").startswith("image/") or "content_type" not in res)
        if not ok:
            bad += 1
            print(f"问题 {res.get('status')} {item['url']}")
    FILE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"共 {len(jobs)} 个地址，{bad} 个有问题")
    return 0


if __name__ == "__main__":
    sys.exit(main())
