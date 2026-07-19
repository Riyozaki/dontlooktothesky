#!/usr/bin/env python3
"""Exhaustively check the Valeria route ending resolver."""

from __future__ import annotations

import itertools
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "game"))

from valeria_logic import (  # noqa: E402
    ENDING_EQUAL,
    ENDING_FAILURE,
    ENDING_STANDARD,
    equal_contract_is_admissible,
    resolve_valeria_ending,
)


def score(bits: tuple[bool, ...]) -> tuple[int, int, int]:
    # V01 exact testimony, V01 disclosure, V02 shared reference,
    # V03 full/corrected testimony.
    transparency = sum(bits[:4])
    # Closing the accidental origin line respects reciprocity; reading it does not.
    reciprocity = 1 if bits[4] else -1
    # Mirael's confidence is always preserved by the route text. The second point
    # comes from respecting Artem's requested scope in V05.
    third_party_autonomy = 1 + (1 if bits[5] else 0)
    return transparency, reciprocity, third_party_autonomy


def main() -> None:
    rows = []
    for bits in itertools.product((False, True), repeat=6):
        scores = score(bits)
        result = resolve_valeria_ending(*scores)
        rows.append((bits, scores, result))

        if result == ENDING_EQUAL:
            assert equal_contract_is_admissible(*scores)
        if result == ENDING_STANDARD:
            assert scores[0] < 3
        if result == ENDING_FAILURE:
            assert scores[0] >= 3
            assert not equal_contract_is_admissible(*scores)

    assert resolve_valeria_ending(3, 1, 2) == ENDING_EQUAL
    assert resolve_valeria_ending(2, 1, 2) == ENDING_STANDARD
    assert resolve_valeria_ending(3, -1, 2) == ENDING_FAILURE
    assert resolve_valeria_ending(3, 1, 1) == ENDING_FAILURE

    counts = Counter(result for _, _, result in rows)
    print(
        "Valeria ending logic passed: "
        f"{len(rows)} profiles, E03={counts[ENDING_EQUAL]}, "
        f"E04={counts[ENDING_STANDARD]}, E05={counts[ENDING_FAILURE]}."
    )


if __name__ == "__main__":
    main()
