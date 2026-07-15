#!/usr/bin/env python3
"""Generate a readable Markdown mirror from a Ren'Py chapter.

P1 uses Ren'Py as the single working source. This script deliberately extracts
visible prose only; scene setup, transforms, calls and other technical lines are
not duplicated into the manuscript mirror.
"""
from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
MANUSCRIPT = ROOT / "docs" / "manuscript"
LABEL_RE = re.compile(r"^label\s+((?:c|m|e)\d+_s\d+):", re.MULTILINE)
TEXT_RE = re.compile(r'^\s*(?:(\w+)\s+)?(".*")\s*$')
SCENE_TITLE_RE = re.compile(
    r"^##\s+((?:C|M|E)\d+-S\d+)\s+(.+?)\s*$", re.MULTILINE
)


def scene_titles(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    return {
        match.group(1).lower().replace("-", "_"): match.group(2)
        for match in SCENE_TITLE_RE.finditer(text)
    }


def extract(path: Path) -> dict[str, list[tuple[str, str]]]:
    text = path.read_text(encoding="utf-8")
    labels = list(LABEL_RE.finditer(text))
    result: dict[str, list[tuple[str, str]]] = {}
    for index, label in enumerate(labels):
        scene_id = label.group(1)
        body = text[
            label.end() : labels[index + 1].start() if index + 1 < len(labels) else len(text)
        ]
        units: list[tuple[str, str]] = []
        for raw in body.splitlines():
            match = TEXT_RE.match(raw)
            if not match:
                continue
            speaker = match.group(1) or "narrator"
            try:
                value = ast.literal_eval(match.group(2))
            except (SyntaxError, ValueError):
                continue
            units.append((speaker, value))
        result[scene_id] = units
    return result


def render(chapter: str) -> str:
    rpy = GAME / f"{chapter}.rpy"
    md = MANUSCRIPT / f"{chapter}.md"
    if not rpy.exists() or not md.exists():
        raise SystemExit(f"Missing chapter pair: {rpy} / {md}")

    old = md.read_text(encoding="utf-8")
    preamble = old[: old.find("## ")].rstrip()
    titles = scene_titles(md)
    scenes = extract(rpy)
    chunks = [preamble]

    for scene_id, units in scenes.items():
        title = titles.get(scene_id, f'«{scene_id.upper()}»')
        pretty_id = scene_id.upper().replace("_", "-")
        chunks.extend(["", f"## {pretty_id} {title}", ""])
        for speaker, value in units:
            if speaker == "narrator":
                chunks.extend([value, ""])
            else:
                chunks.extend([f"— {value}", ""])
        while chunks and chunks[-1] == "":
            chunks.pop()
        chunks.extend(["", "---", ""])

    while chunks and chunks[-1] == "":
        chunks.pop()
    return re.sub(r"[ \t]+\n", "\n", "\n".join(chunks)) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter", help="chapter stem, for example m02")
    args = parser.parse_args()
    output = MANUSCRIPT / f"{args.chapter}.md"
    output.write_text(render(args.chapter), encoding="utf-8")
    print(f"Generated {output.relative_to(ROOT)} from game/{args.chapter}.rpy")


if __name__ == "__main__":
    main()
