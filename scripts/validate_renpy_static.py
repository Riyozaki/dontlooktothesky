#!/usr/bin/env python3
"""Static project checks available without importing the Ren'Py engine.

This intentionally checks project wiring, not full Ren'Py grammar. A real lint
and compile remain mandatory before release.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
ERRORS: list[str] = []

rpy_files = sorted(GAME.glob("*.rpy"))
sources: dict[Path, str] = {}
for path in rpy_files:
    try:
        sources[path] = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid UTF-8: {error}")
        sources[path] = ""

combined = "\n".join(sources.values())

# Labels and control flow.
labels = re.findall(r"^label\s+([A-Za-z0-9_]+):", combined, re.MULTILINE)
for label in sorted(set(labels)):
    if labels.count(label) > 1:
        ERRORS.append(f"duplicate label: {label}")

control_targets = re.findall(
    r"^\s*(?:call|jump)\s+([A-Za-z_][A-Za-z0-9_]*)\s*$",
    combined,
    re.MULTILINE,
)
for target in sorted(set(control_targets) - set(labels)):
    ERRORS.append(f"unresolved call/jump: {target}")

# Declared project objects.
characters = set(
    re.findall(
        r"^define\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*Character\(",
        combined,
        re.MULTILINE,
    )
)
characters.update({"narrator", "centered"})

def normalize_name(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()

images = {
    normalize_name(value)
    for value in re.findall(r"^image\s+([^=]+?)\s*=", combined, re.MULTILINE)
}
audio = set(
    re.findall(
        r"^define\s+audio\.([A-Za-z_][A-Za-z0-9_]*)\s*=",
        combined,
        re.MULTILINE,
    )
)
defaults = set(
    re.findall(
        r"^default\s+([A-Za-z_][A-Za-z0-9_]*)\s*=",
        combined,
        re.MULTILINE,
    )
)

quoted = r'"(?:\\.|[^"\\])*"'
say_re = re.compile(
    rf"^\s*(?:(?P<speaker>[A-Za-z_][A-Za-z0-9_]*)\s+)?(?P<text>{quoted})\s*$"
)
dynamic_say_re = re.compile(rf"^\s*{quoted}\s+{quoted}\s*$")
menu_re = re.compile(rf"^\s*{quoted}(?:\s+if\s+.+)?\s*:\s*$")
looks_like_say_re = re.compile(r'^\s*(?:(?:[A-Za-z_][A-Za-z0-9_]*)\s+)?"')

asset_pattern = re.compile(
    r'"(\.\./[^"\n]+\.(?:png|jpe?g|mp3|wav|ogg|opus|ttf))"',
    re.IGNORECASE,
)
image_ref_re = re.compile(
    r"^\s*(?:scene|show)\s+(.+?)(?:\s+at\s+|\s+with\s+|\s*$)"
)
audio_ref_re = re.compile(
    r"^\s*play\s+(?:music|sound)\s+([A-Za-z_][A-Za-z0-9_]*)\b"
)
augmented_re = re.compile(
    r"^\s*\$\s+([A-Za-z_][A-Za-z0-9_]*)\s*[+\-*/%]="
)

for path, source in sources.items():
    narrative_file = bool(
        re.fullmatch(r"(?:[cmevnt]\d+|script)\.rpy", path.name)
    )
    for number, line in enumerate(source.splitlines(), 1):
        location = f"{path.relative_to(ROOT)}:{number}"

        if "\t" in line:
            ERRORS.append(f"{location}: tab character")

        if narrative_file:
            say = say_re.match(line)
            if say:
                try:
                    ast.literal_eval(say.group("text"))
                except (SyntaxError, ValueError):
                    ERRORS.append(f"{location}: invalid quoted Ren'Py text")
                speaker = say.group("speaker")
                if speaker and speaker not in characters:
                    ERRORS.append(f"{location}: undefined speaking character {speaker!r}")
            elif dynamic_say_re.match(line) or menu_re.match(line):
                pass
            elif looks_like_say_re.match(line):
                ERRORS.append(f"{location}: malformed say/menu statement")

        if re.search(r'"\s*[.]}]+\s*$', line):
            ERRORS.append(f"{location}: stray punctuation after quoted text")

        image_ref = image_ref_re.match(line)
        if image_ref:
            name = normalize_name(image_ref.group(1))
            if name != "black" and name not in images:
                ERRORS.append(f"{location}: undefined image {name!r}")

        audio_ref = audio_ref_re.match(line)
        if audio_ref and audio_ref.group(1) not in audio:
            ERRORS.append(f"{location}: undefined audio {audio_ref.group(1)!r}")

        augmented = augmented_re.match(line)
        if augmented and augmented.group(1) not in defaults:
            ERRORS.append(
                f"{location}: augmented assignment to undeclared variable "
                f"{augmented.group(1)!r}"
            )

        for reference in asset_pattern.findall(line):
            resolved = (path.parent / reference).resolve()
            if not resolved.exists():
                ERRORS.append(f"{location}: missing asset {reference}")

if ERRORS:
    print("Static Ren'Py validation failed:")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print(
    f"Static Ren'Py validation passed: {len(rpy_files)} files, "
    f"{len(labels)} labels, {len(images)} images, {len(audio)} audio ids."
)
