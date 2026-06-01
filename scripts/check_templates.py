#!/usr/bin/env python3
"""Lightweight repository checks for Markdown-based Stata templates."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_NON_STATA_FENCES = {"bash", "markdown", "shell", "text", "plain text", ""}


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def check_title(path: Path, text: str, errors: list[str]) -> None:
    if not text.lstrip().startswith("#"):
        errors.append(f"{path.relative_to(ROOT)}: missing top-level Markdown heading")


def check_local_links(path: Path, text: str, errors: list[str]) -> None:
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        link = match.group(1).strip()
        if (
            not link
            or link.startswith(("http://", "https://", "mailto:", "#"))
            or "://" in link
        ):
            continue

        target_text = link.split("#", 1)[0]
        if not target_text:
            continue

        target = (path.parent / target_text).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: local link escapes repository: {link}")
            continue

        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link: {link}")


def check_fences(path: Path, text: str, warnings: list[str]) -> None:
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if (
            not stripped.startswith("```")
            or stripped.startswith("````")
            or stripped == "```"
        ):
            continue

        language = stripped[3:].strip()
        if language and language not in {"stata", *ALLOWED_NON_STATA_FENCES}:
            warnings.append(
                f"{path.relative_to(ROOT)}:{lineno}: non-Stata fence language `{language}`"
            )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    markdown_files = iter_markdown_files()
    if not markdown_files:
        errors.append("No Markdown files found.")

    for path in markdown_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        check_title(path, text, errors)
        check_local_links(path, text, errors)
        check_fences(path, text, warnings)

    for warning in warnings:
        print(f"warning: {warning}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Checked {len(markdown_files)} Markdown files.")
    if warnings:
        print(f"{len(warnings)} warning(s): existing code fence tags can be normalized later.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
