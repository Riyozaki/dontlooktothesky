#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -z "${RENPY_SDK:-}" ]]; then
    echo "RENPY_SDK is not set (example: /opt/renpy-8.5.3-sdk)." >&2
    exit 2
fi

RENPY="$RENPY_SDK/renpy.sh"
if [[ ! -f "$RENPY" ]]; then
    echo "Ren'Py launcher not found: $RENPY" >&2
    exit 2
fi

python3 "$ROOT/scripts/validate_renpy_static.py"
python3 "$ROOT/scripts/test_mirael_endings.py"
python3 "$ROOT/scripts/test_valeria_endings.py"
python3 "$ROOT/scripts/audit_text_transfer.py"

sh "$RENPY" "$ROOT" lint
sh "$RENPY" "$ROOT" compile
