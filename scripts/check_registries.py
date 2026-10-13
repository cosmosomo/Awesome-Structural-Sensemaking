#!/usr/bin/env python3
"""用 npm / PyPI 上的包元数据核对条目的 repo、许可证和维护情况。需要联网。

条目里写了 `package: npm:名称` 或 `package: pypi:名称` 的才会检查。包元数据里的仓库地址是包作者
自己声明的，拿它和条目里的 `repo` 对比，不需要访问 GitHub 页面。

用法:
  python3 scripts/check_registries.py                  检查全部带 package 的条目
  python3 scripts/check_registries.py --id d3          只检查一个条目
  python3 scripts/check_registries.py --json out.json  同时写出 JSON

输出每个条目的：声明的仓库是否与 repo 一致、许可证（SPDX 或原文）、是否被标记弃用、最近一次发布时间。
只读，不修改任何文件。一致才可以给条目加 `repo_checked`；不一致时要人工看是包和仓库不是一回事
（例如平台的客户端 SDK），还是 repo 写错了。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = "awesome-structural-sensemaking-registry-check/1.0"


def get_json(url: str, headers: dict | None = None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def norm_repo(url: str | None) -> str:
    """把各种仓库地址写法归一成 host/owner/repo（小写）。"""
    if not url:
        return ""
    u = url.strip()
    u = re.sub(r"^git\+", "", u)
    u = re.sub(r"^git://", "https://", u)
    u = re.sub(r"^ssh://git@", "https://", u)
    u = re.sub(r"^git@([^:]+):", r"https://\1/", u)
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"\.git$", "", u.rstrip("/"))
    p = urllib.parse.urlparse(u)
    parts = [x for x in p.path.split("/") if x]
    return f"{p.netloc.lower()}/{'/'.join(parts[:2]).lower()}"


def npm(name: str) -> dict:
    enc = urllib.parse.quote(name, safe="@")
    latest = get_json(f"https://registry.npmjs.org/{enc}/latest")
    meta = get_json(f"https://registry.npmjs.org/{enc}", {"Accept": "application/vnd.npm.install-v1+json"})
    repo = latest.get("repository")
    repo = repo.get("url") if isinstance(repo, dict) else repo
    lic = latest.get("license")
    lic = lic.get("type") if isinstance(lic, dict) else lic
    return {"declared_repo": repo or "", "license": lic or "", "deprecated": latest.get("deprecated") or "",
            "version": latest.get("version", ""), "modified": (meta.get("modified") or "")[:10]}


def pypi(name: str) -> dict:
    d = get_json(f"https://pypi.org/pypi/{urllib.parse.quote(name)}/json")
    info = d["info"]
    urls = info.get("project_urls") or {}
    repo = ""
    for k, v in urls.items():
        if re.search(r"github\.com|gitlab\.com", v or "") and k.lower() in ("source", "repository", "source code", "code", "github", "homepage", "home"):
            repo = v
            break
    if not repo:
        repo = next((v for v in urls.values() if re.search(r"github\.com|gitlab\.com", v or "")), "") or info.get("home_page") or ""
    lic = info.get("license_expression") or ""
    if not lic:
        lic = next((c.split("::")[-1].strip() for c in info.get("classifiers", []) if c.startswith("License ::")), "") or (info.get("license") or "")[:60]
    files = [f for fs in d["releases"].values() for f in fs]
    last = max((f["upload_time"] for f in files), default="")[:10]
    return {"declared_repo": repo, "license": lic, "deprecated": "yanked" if info.get("yanked") else "",
            "version": info.get("version", ""), "modified": last}


def check(entry: dict) -> dict:
    reg, name = entry["package"].split(":", 1)
    res = {"id": entry["id"], "package": entry["package"], "repo": entry.get("repo", ""), "ok": False}
    try:
        res.update(npm(name) if reg == "npm" else pypi(name))
        res["match"] = bool(res["declared_repo"]) and norm_repo(res["declared_repo"]) == norm_repo(entry.get("repo"))
        res["ok"] = True
    except urllib.error.HTTPError as e:
        res["error"] = f"HTTP {e.code}"
    except Exception as e:
        res["error"] = f"{type(e).__name__}: {e}"[:100]
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--id")
    ap.add_argument("--json")
    args = ap.parse_args()
    entries = []
    for p in sorted((ROOT / "catalog" / "projects").glob("*.yaml")):
        for e in yaml.safe_load(p.read_text(encoding="utf-8")) or []:
            if e.get("package") and (not args.id or e["id"] == args.id):
                entries.append(e)
    if not entries:
        print("没有带 package 的条目")
        return 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(check, entries))
    bad = 0
    for r in results:
        if not r["ok"]:
            bad += 1
            print(f"ERR   {r['id']:<30} {r['package']:<36} {r['error']}")
            continue
        flag = "match" if r["match"] else "DIFF "
        bad += 0 if r["match"] else 1
        dep = f" DEPRECATED[{r['deprecated'][:50]}]" if r["deprecated"] else ""
        print(f"{flag} {r['id']:<30} {r['package']:<36} lic={r['license'] or '?':<22} last={r['modified']} v{r['version']}{dep}")
        if not r["match"]:
            print(f"        条目: {r['repo']}\n        包声明: {r['declared_repo']}")
    print(f"\n共 {len(results)} 个包，{len(results) - bad} 个仓库地址一致")
    if args.json:
        Path(args.json).write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
