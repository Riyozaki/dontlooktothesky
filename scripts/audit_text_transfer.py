#!/usr/bin/env python3
"""Compare visible Markdown manuscript units with Ren'Py text units.

This is intentionally a report generator, not a pass/fail compiler. Markdown and
Ren'Py may differ in dialogue attribution, menus, and conditional branches. The
report identifies where a human transfer audit is needed.
"""
from __future__ import annotations

import ast
import difflib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "docs" / "manuscript"
GAME = ROOT / "game"

SCENE_RE = re.compile(r"^##\s+((?:C|M|E|V|N|T)\d+-S\d+)[^\n]*$", re.MULTILINE)
LABEL_RE = re.compile(r"^label\s+((?:c|m|e|v|n|t)\d+_s\d+):", re.MULTILINE)
TEXT_RE = re.compile(r'^\s*(?:(?:[A-Za-z_][A-Za-z0-9_]*)\s+)?(".*")\s*$')

ATTRIBUTION_RE = re.compile(
    r"(?:сказал|сказала|сказали|спросил|спросила|ответил|ответила|"
    r"добавил|добавила|продолжил|продолжила|произнёс|произнесла|удивился)"
    r"\s+[^.!?]+[.!?]"
)


def normalize_markdown_dialogue(value: str) -> str:
    """Remove prose-only speaker attributions from a Markdown dialogue unit.

    Ren'Py stores the speaker in the Character object, so phrases such as
    ``— спросил Александр`` must not be treated as missing visible dialogue.
    Clause boundaries are retained to avoid turning two spoken sentences into
    one run-on string.
    """
    value = re.sub(r"\s*,\s*—\s*" + ATTRIBUTION_RE.pattern + r"\s*—\s*", ". ", value)
    value = re.sub(r"\s*,\s*" + ATTRIBUTION_RE.pattern, "", value)
    value = re.sub(r"\s*—\s*" + ATTRIBUTION_RE.pattern, "", value)
    value = re.sub(r",\s*$", ".", value)
    return value.strip()


def markdown_scenes(path: Path) -> dict[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    matches = list(SCENE_RE.finditer(text))
    result: dict[str, list[str]] = {}
    for index, match in enumerate(matches):
        scene_id = match.group(1).lower().replace("-", "_")
        body = text[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        units: list[str] = []
        menu_description = False
        for raw in body.splitlines():
            line = raw.strip()
            if not line or line == "---":
                continue
            if scene_id == "c09_s04" and line.startswith("После этого на экране появилось меню"):
                menu_description = True
                continue
            if menu_description:
                # The four descriptions are visible narrator strings in the
                # Ren'Py menu branches; choice labels and route assignments are
                # technical syntax and are intentionally omitted.
                if line in {
                    "Найти способ стабилизировать её тело и восстановить память, не превращая её в доказательство.",
                    "Увидеть систему изнутри и разобрать предложение о жизни и везении.",
                    "Собрать земные факты и не принимать версию ни одной заинтересованной стороны.",
                    "Не позволить каждому участнику закрыть дело отдельно.",
                }:
                    units.append(line)
                    continue
                if line.startswith("Он должен был выбрать"):
                    units.append(line)
                    menu_description = False
                continue
            if line.startswith(("#", "**", "###", "```")):
                continue
            if line.startswith("route_selected") or line.startswith("Если пять базовых"):
                continue
            if line.startswith("> "):
                units.append(line[2:])
            elif line.startswith("— "):
                units.append(normalize_markdown_dialogue(line[2:]))
            else:
                units.append(line)
        result[scene_id.lower()] = units
    return result


def renpy_scenes(path: Path) -> dict[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    matches = list(LABEL_RE.finditer(text))
    result: dict[str, list[str]] = {}
    for index, match in enumerate(matches):
        scene_id = match.group(1)
        body = text[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        units: list[str] = []
        for raw in body.splitlines():
            match_text = TEXT_RE.match(raw)
            if not match_text:
                continue
            try:
                units.append(ast.literal_eval(match_text.group(1)))
            except (SyntaxError, ValueError):
                continue
        result[scene_id] = units
    return result


def first_difference(expected: list[str], actual: list[str]) -> str:
    matcher = difflib.SequenceMatcher(a=expected, b=actual, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != "equal":
            left = expected[i1] if i1 < len(expected) else "<конец Markdown>"
            right = actual[j1] if j1 < len(actual) else "<конец Ren'Py>"
            return f"{tag}: MD={left[:100]!r}; RPY={right[:100]!r}"
    return "—"


def main() -> None:
    md: dict[str, list[str]] = {}
    for path in (
        sorted(MANUSCRIPT.glob("c0[0-9].md"))
        + sorted(MANUSCRIPT.glob("m0[1-7].md"))
        + sorted(MANUSCRIPT.glob("v0[1-8].md"))
        + sorted(MANUSCRIPT.glob("e0[1-2].md"))
    ):
        md.update(markdown_scenes(path))

    rpy: dict[str, list[str]] = {}
    for path in (
        sorted(GAME.glob("c0[0-9].rpy"))
        + sorted(GAME.glob("m0[1-7].rpy"))
        + sorted(GAME.glob("v0[1-8].rpy"))
        + sorted(GAME.glob("e0[1-2].rpy"))
    ):
        rpy.update(renpy_scenes(path))

    rows: list[str] = []
    mismatched: list[str] = []
    rows.append("# Соответствие активных Markdown-зеркал исходникам Ren’Py")
    rows.append("")
    rows.append("Автоматический отчёт по активным C-, M-, V-главам и E01/E02. Канонический источник — Ren’Py; расхождение означает, что зеркало нужно пересоздать или проверить вручную.")
    rows.append("")
    rows.append("| Сцена | Markdown | Ren’Py | Сходство | Первый участок расхождения |")
    rows.append("|---|---:|---:|---:|---|")

    for scene_id in sorted(md):
        expected = md[scene_id]
        actual = rpy.get(scene_id, [])
        ratio = difflib.SequenceMatcher(a=expected, b=actual, autojunk=False).ratio() if expected or actual else 1.0
        difference = first_difference(expected, actual)
        if expected != actual:
            mismatched.append(scene_id)
        rows.append(f"| `{scene_id.upper()}` | {len(expected)} | {len(actual)} | {ratio:.3f} | {difference} |")

    missing = sorted(set(md) - set(rpy))
    extra = sorted(set(rpy) - set(md))
    rows.append("")
    rows.append(f"Сцен Markdown: {len(md)}. Сцен Ren’Py: {len(rpy)}.")
    if missing:
        rows.append("\nОтсутствуют в Ren’Py: " + ", ".join(f"`{x.upper()}`" for x in missing) + ".")
    if extra:
        rows.append("\nЕсть только в Ren’Py: " + ", ".join(f"`{x.upper()}`" for x in extra) + ".")

    output = ROOT / "docs" / "manuscript" / "renpy-full-transfer-audit.md"
    output.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)} with {len(md)} scene rows")
    if missing or extra or mismatched:
        problems = missing + extra + mismatched
        print("Transfer audit failed: " + ", ".join(sorted(set(problems))))
        raise SystemExit(1)
    print("Transfer audit passed: all active scene mirrors match Ren'Py.")


if __name__ == "__main__":
    main()
