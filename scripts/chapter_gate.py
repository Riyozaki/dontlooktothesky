#!/usr/bin/env python3
"""Block chapter completion reports until the full production cycle is done."""
from __future__ import annotations

import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "docs" / "state" / "active-chapter.md"
TEXT_RE = re.compile(r'^\s*(?:(?:[A-Za-zА-Яа-я_][\w]*)\s+)?(".*")\s*$')
WORD_RE = re.compile(r"[А-Яа-яЁёA-Za-z0-9]+(?:[-’'][А-Яа-яЁёA-Za-z0-9]+)*")


def active_fields() -> dict[str, str]:
    if not ACTIVE.is_file():
        return {}
    fields: dict[str, str] = {}
    for raw in ACTIVE.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^([a-z_]+):\s*(.+?)\s*$", raw)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


def visible_word_count(path: Path) -> int:
    values: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TEXT_RE.match(line)
        if not match:
            continue
        try:
            values.append(ast.literal_eval(match.group(1)))
        except (SyntaxError, ValueError):
            continue
    return len(WORD_RE.findall(" ".join(values)))


def run(command: list[str]) -> bool:
    print("$ " + " ".join(command))
    result = subprocess.run(command, cwd=ROOT, text=True)
    return result.returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", nargs="?", help="chapter stem, for example c03")
    parser.add_argument("--skip-checks", action="store_true", help="only inspect completion artifacts")
    args = parser.parse_args()

    fields = active_fields()
    chapter = (args.chapter or fields.get("chapter", "")).lower()
    failures: list[str] = []
    if not chapter:
        failures.append("active chapter is not specified")
        chapter = "<unknown>"

    if fields.get("chapter", "").lower() != chapter:
        failures.append(f"active-chapter.md does not name {chapter}")
    if fields.get("state") != "ready":
        failures.append(f"active chapter state is {fields.get('state', 'missing')!r}, expected 'ready'")

    source = ROOT / "game" / f"{chapter}.rpy"
    mirror = ROOT / "docs" / "manuscript" / f"{chapter}.md"
    review = ROOT / "temp" / f"{chapter}-full-review.md"
    drafts = ROOT / "drafts" / chapter
    minimum = int(fields.get("minimum_visible_words", "7000"))
    maximum = int(fields.get("maximum_visible_words", "10000"))

    if not source.is_file():
        failures.append(f"missing {source.relative_to(ROOT)}")
    else:
        words = visible_word_count(source)
        print(f"Visible word count (all source branches): {words}")
        if words < minimum:
            failures.append(f"visible word count {words} is below {minimum}")
        if words > maximum:
            failures.append(f"visible word count {words} is above {maximum}")
    if not mirror.is_file():
        failures.append(f"missing {mirror.relative_to(ROOT)}")
    if not review.is_file():
        failures.append(f"missing {review.relative_to(ROOT)}")
    if drafts.exists() and any(drafts.iterdir()):
        failures.append(f"temporary drafts remain in {drafts.relative_to(ROOT)}")

    if not args.skip_checks and source.is_file():
        commands = [
            [sys.executable, "scripts/style_guard.py", f"game/{chapter}.rpy"],
            [sys.executable, "scripts/validate_renpy_static.py"],
            [sys.executable, "scripts/test_mirael_endings.py"],
            [sys.executable, "scripts/test_valeria_endings.py"],
            [sys.executable, "scripts/audit_text_transfer.py"],
        ]
        for command in commands:
            if not run(command):
                failures.append("failed: " + " ".join(command))

    if failures:
        print("\nCHAPTER GATE FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("\nCHAPTER GATE PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
