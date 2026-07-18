#!/usr/bin/env python3
"""Conservative mechanical guard for the project's Russian prose filter.

It intentionally catches only unambiguous blockers. Warnings are prompts for a
human reading, not automatic rewriting instructions. The input may be a Ren'Py
source file or a readable Markdown/text draft.
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

BLOCKERS = (
    "нечто иное", "нечто", "что-то внутри", "лёгкий холодок", "тяжёлые слова",
    "по-настоящему", "наконец-то", "в этот момент", "в тот момент",
    "каким-то образом", "казалось бы", "словно бы",
)
BLOCKER_RE = re.compile(r"\b(?:" + "|".join(re.escape(item) for item in BLOCKERS) + r")\b", re.IGNORECASE)
HANGING_RE = re.compile(r"\b(?:повисло|повисла|повисли|разлилось|разлилась|разлились)\b", re.IGNORECASE)
TEXT_RE = re.compile(r'^\s*(?:(?:[A-Za-zА-Яа-я_][\w]*)\s+)?(".*")\s*$')


def visible_lines(path: Path) -> list[tuple[int, str]]:
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    if path.suffix.lower() != ".rpy":
        return [(number, line) for number, line in enumerate(raw_lines, 1)]

    result: list[tuple[int, str]] = []
    for number, line in enumerate(raw_lines, 1):
        match = TEXT_RE.match(line)
        if not match:
            continue
        try:
            value = ast.literal_eval(match.group(1))
        except (SyntaxError, ValueError):
            continue
        result.append((number, value))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    if not args.file.is_file():
        parser.error(f"file not found: {args.file}")

    lines = visible_lines(args.file)
    is_renpy = args.file.suffix.lower() == ".rpy"
    blockers: list[str] = []
    warnings: list[str] = []
    # Ren'Py stores every visible line separately, so it does not preserve
    # paragraph boundaries. Paragraph-level heuristics are only meaningful for
    # Markdown and plain-text drafts.
    paragraphs: list[list[tuple[int, str]]] = [[]]
    for number, text in lines:
        if not is_renpy and not text.strip():
            paragraphs.append([])
            continue
        if not is_renpy:
            paragraphs[-1].append((number, text))
        for match in BLOCKER_RE.finditer(text):
            blockers.append(f"{number}: {match.group(0)!r}")
        for match in HANGING_RE.finditer(text):
            blockers.append(f"{number}: {match.group(0)!r}")
        if text.count("—") >= 4:
            warnings.append(f"{number}: four or more em dashes")
        if not is_renpy and re.fullmatch(r"\s*[А-ЯЁа-яё-]{1,20}[.!?]\s*", text):
            warnings.append(f"{number}: possible one-word paragraph")

    seen: dict[str, int] = {}
    for number, text in lines:
        normalized = re.sub(r"\s+", " ", text.strip().lower())
        if len(normalized) < 30:
            continue
        if normalized in seen:
            warnings.append(f"{number}: duplicate of line {seen[normalized]}")
        else:
            seen[normalized] = number

    for paragraph in paragraphs:
        joined = " ".join(text for _, text in paragraph).lower()
        for word in ("словно", "будто"):
            if len(re.findall(rf"\b{word}\b", joined)) > 1:
                warnings.append(f"{paragraph[0][0]}: more than one {word!r} in paragraph")

    for item in blockers:
        print(f"BLOCKER {args.file}: {item}")
    for item in warnings:
        print(f"WARNING {args.file}: {item}")
    if not blockers and not warnings:
        print(f"OK {args.file}: no mechanical blockers or warnings in {len(lines)} visible lines")
    elif not blockers:
        print(f"OK {args.file}: no mechanical blockers; review {len(warnings)} warning(s) manually")
    return 1 if blockers else 0


if __name__ == "__main__":
    sys.exit(main())
