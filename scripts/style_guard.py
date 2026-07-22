#!/usr/bin/env python3
"""Conservative mechanical guard for project prose.

The guard catches explicit markers only. A clean result never replaces a manual
read of HARD-BLOCKERS.md.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

BANNED_PHRASES = (
    "нечто иное",
    "нечто",
    "что-то внутри",
    "лёгкий холодок",
    "тяжёлые слова",
    "по-настоящему",
    "наконец-то",
    "в этот момент",
    "в тот момент",
    "каким-то образом",
    "казалось бы",
    "словно бы",
    "уголки губ",
    "краешки губ",
    "глубокий вздох",
    "сердце сжалось",
    "сердце ёкнуло",
    "осознал, что",
    "почувствовал, что",
)
PHRASE_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(item) for item in BANNED_PHRASES) + r")\b",
    re.IGNORECASE,
)
HANGING_RE = re.compile(
    r"\b(?:повисло|повисла|повисли|разлилось|разлилась|разлились)\b",
    re.IGNORECASE,
)
KNUCKLES_RE = re.compile(r"\bкостяшк\w*\b", re.IGNORECASE)
CONTRAST_RE = re.compile(
    r"\bне\s+[^.!?\n]{1,120}?(?:,\s*|\s+[—-]\s+)(?:а|просто|только|зато|скорее)\b",
    re.IGNORECASE,
)
THIS_NOT_RE = re.compile(
    r"\bэто\s+не\s+[^.!?\n]{1,100}[.!?]\s+это\b",
    re.IGNORECASE,
)
META_RE = re.compile(
    r"(?:\bпосле\s+[CMVNET]\d{2}\b|\bдо\s+того,?\s+как\s+меню\b|"
    r"character-bible|\.md\b|\bИИ(?:[- ]|$)|\bпротагонист\w*\b|"
    r"показател\w*\s+(?:доверия|ответственности))",
    re.IGNORECASE,
)
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
            # Syntax errors belong to validate_renpy_static.py / Ren'Py lint.
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

    paragraphs: list[list[tuple[int, str]]] = [[]]
    seen: dict[str, int] = {}

    for number, text in lines:
        if not is_renpy and not text.strip():
            paragraphs.append([])
            continue
        if not is_renpy:
            paragraphs[-1].append((number, text))

        for regex, label in (
            (PHRASE_RE, "banned phrase"),
            (HANGING_RE, "hanging/spreading cliché"),
            (KNUCKLES_RE, "knuckles cliché"),
            (CONTRAST_RE, "negative contrast"),
            (THIS_NOT_RE, "'this is not X, this is Y' formula"),
            (META_RE, "production meta-text"),
        ):
            for match in regex.finditer(text):
                blockers.append(f"{number}: {label}: {match.group(0)!r}")

        if text.count("—") >= 4:
            warnings.append(f"{number}: four or more em dashes")

        normalized = re.sub(r"\s+", " ", text.strip().lower())
        if len(normalized) >= 30:
            if normalized in seen:
                warnings.append(f"{number}: duplicate of line {seen[normalized]}")
            else:
                seen[normalized] = number

    for paragraph in paragraphs:
        if not paragraph:
            continue
        joined = " ".join(text for _, text in paragraph).lower()
        for word in ("словно", "будто"):
            if len(re.findall(rf"\b{word}\b", joined)) > 1:
                warnings.append(
                    f"{paragraph[0][0]}: more than one {word!r} in paragraph"
                )

    for item in blockers:
        print(f"BLOCKER {args.file}: {item}")
    for item in warnings:
        print(f"WARNING {args.file}: {item}")

    if not blockers and not warnings:
        print(
            f"OK {args.file}: no mechanical blockers or warnings "
            f"in {len(lines)} visible lines"
        )
    elif not blockers:
        print(
            f"OK {args.file}: no mechanical blockers; "
            f"review {len(warnings)} warning(s) manually"
        )

    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
