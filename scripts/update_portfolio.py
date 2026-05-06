#!/usr/bin/env python3
"""Sync the portfolio section of README.md from service-architecture-lab.

Reads the project list table from the source repo's README and rewrites the
content between `<!-- portfolio:start -->` and `<!-- portfolio:end -->` markers
in this repo's README, with relative links rewritten to absolute GitHub URLs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_URL = "https://github.com/t-hirata74/service-architecture-lab"
START = "<!-- portfolio:start -->"
END = "<!-- portfolio:end -->"
SOURCE_HEADING = "プロジェクト一覧"
INTRO = (
    "有名 SaaS のアーキテクチャを **ローカル完結のミニマム実装** で再現し、"
    "設計判断を ADR として残す検証用プロジェクト群。各サービスは "
    "**backend + frontend (Next.js 16) + ai-worker (Python / FastAPI) + MySQL** "
    "の同形構成で、API スタイル / キュー / 認可モデル / 整合性パターンの違いを"
    "横断比較できるように整理している。"
)
OUTRO = (
    "設計判断はすべて **ADR (Architecture Decision Record)** として記録し、"
    "E2E テストは Playwright で gif 化して各 README に埋め込んでいる。"
    "プロジェクト一覧は GitHub Actions で "
    "`service-architecture-lab` の README から日次自動同期。"
)


def absolutize(md: str, base: str) -> str:
    def repl(m: re.Match[str]) -> str:
        text, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        url = url.lstrip("./")
        kind = "tree" if url.endswith("/") else "blob"
        return f"[{text}]({base}/{kind}/main/{url.rstrip('/')})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, md)


def extract_table(text: str, heading: str) -> str:
    pattern = rf"##\s+{re.escape(heading)}.*?\n\n(\|.+?)(?=\n\n|\n##|\Z)"
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        sys.exit(f"error: table after heading '{heading}' not found in source README")
    return m.group(1).strip()


def main() -> int:
    source = Path(sys.argv[1] if len(sys.argv) > 1 else "service-architecture-lab/README.md")
    target = Path(sys.argv[2] if len(sys.argv) > 2 else "README.md")

    src_text = source.read_text(encoding="utf-8")
    table = absolutize(extract_table(src_text, SOURCE_HEADING), REPO_URL)

    block = (
        f"{START}\n"
        f"### [service-architecture-lab]({REPO_URL})\n\n"
        f"{INTRO}\n\n"
        f"{table}\n\n"
        f"{OUTRO}\n"
        f"{END}"
    )

    target_text = target.read_text(encoding="utf-8")
    new_text, n = re.subn(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        lambda _m: block,
        target_text,
        count=1,
        flags=re.DOTALL,
    )
    if n == 0:
        sys.exit(f"error: markers {START}/{END} not found in {target}")

    if new_text == target_text:
        print("portfolio: no changes")
        return 0

    target.write_text(new_text, encoding="utf-8")
    print("portfolio: updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
