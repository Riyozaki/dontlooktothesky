#!/usr/bin/env python3
"""Static checks available without the Ren'Py SDK."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
ERRORS: list[str] = []

rpy_files = sorted(GAME.glob("*.rpy"))
combined = "\n".join(path.read_text(encoding="utf-8") for path in rpy_files)

labels = re.findall(r"^label\s+([A-Za-z0-9_]+):", combined, re.MULTILINE)
calls = re.findall(r"^\s*call\s+([A-Za-z0-9_]+)", combined, re.MULTILINE)

for label in sorted(set(labels)):
    if labels.count(label) > 1:
        ERRORS.append(f"duplicate label: {label}")

for target in sorted(set(calls) - set(labels)):
    ERRORS.append(f"unresolved call: {target}")

asset_pattern = re.compile(
    r'"(\.\./[^"\n]+\.(?:png|jpe?g|mp3|wav|ogg|opus))"', re.IGNORECASE
)

for path in rpy_files:
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        location = f"{path.relative_to(ROOT)}:{number}"

        if "\t" in line:
            ERRORS.append(f"{location}: tab character")
        if line.count('"') % 2:
            ERRORS.append(f"{location}: odd number of double quotes")
        if re.search(r'"\}\}?\s*$', line):
            ERRORS.append(f"{location}: stray closing brace after string")

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
    f"{len(labels)} labels, {len(set(asset_pattern.findall(combined)))} assets."
)
