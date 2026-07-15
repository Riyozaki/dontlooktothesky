#!/usr/bin/env python3
"""Exhaustively check the accumulated-score resolver for the Mirael route.

This does not need the Ren'Py SDK.  It models the nine choices that currently
feed the E01/E02 resolver and checks the boundary cases explicitly.
"""

from __future__ import annotations

import itertools
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "game"))

from mirael_logic import (  # noqa: E402
    ENDING_GUARDIAN,
    ENDING_HUMAN,
    MIRAEL_DECISION_SPEC,
    MIRAEL_ENDING_REQUIREMENTS,
    ending_report,
    resolve_mirael_ending,
)


# Four common-route responsibility choices, five autonomy choices, and the
# linked M05 choice.  True means the first/positive branch listed here: it is
# intentionally represented as values rather than Ren'Py menu text.  The
# labels come from the shared route specification in game/mirael_logic.py.
DECISIONS = tuple(name for name, _, _ in MIRAEL_DECISION_SPEC)


def score(bits: tuple[bool, ...]) -> tuple[int, int, int]:
    responsibility = sum(bits[:4])
    # C03-S02: deleting the photos respects Mirael's privacy; keeping one is
    # evidence gathering and gives no autonomy point.
    autonomy = bits[4] + sum(1 if bit else -1 for bit in bits[5:9])

    # M05: stopping the investigation respects Mirael and accepts Alexander's
    # responsibility; keeping the draft does the opposite and adds evidence.
    if bits[9]:
        responsibility += 1
        autonomy += 1
    else:
        autonomy -= 1

    # M03 hand-holding and M06 kiss are linear route beats.  They are a
    # completion guard, not a hidden final-choice bonus.
    closeness = 2
    return autonomy, responsibility, closeness


def validate_boundaries() -> None:
    req = MIRAEL_ENDING_REQUIREMENTS
    assert resolve_mirael_ending(req["mirael_autonomy"], req["alex_responsibility"], req["mirael_closeness"]) == ENDING_HUMAN
    assert resolve_mirael_ending(req["mirael_autonomy"] - 1, req["alex_responsibility"], req["mirael_closeness"]) == ENDING_GUARDIAN
    assert resolve_mirael_ending(req["mirael_autonomy"], req["alex_responsibility"] - 1, req["mirael_closeness"]) == ENDING_GUARDIAN
    assert resolve_mirael_ending(req["mirael_autonomy"], req["alex_responsibility"], req["mirael_closeness"] - 1) == ENDING_GUARDIAN


def validate_runtime_scoring_sources() -> None:
    """Catch a missing raw increment before the report becomes misleading."""
    files = (
        "c00.rpy",
        "c01.rpy",
        "c03.rpy",
        "c04.rpy",
        "c05.rpy",
        "m01.rpy",
        "m03.rpy",
        "m05.rpy",
        "m06.rpy",
    )
    source = "\n".join((ROOT / "game" / filename).read_text(encoding="utf-8") for filename in files)

    def count(line: str) -> int:
        return len(re.findall(r"^\s*\$ " + re.escape(line) + r"\s*$", source, re.MULTILINE))

    # C03-S02 contributes the positive branch of the autonomy axis. The other
    # five autonomy choices form four +/- pairs plus the linked M05 branch.
    assert count("alex_responsibility += 1") == 5
    assert count("mirael_autonomy += 1") == 6
    assert count("mirael_autonomy -= 1") == 5
    assert count("mirael_closeness += 1") == 2


def render_report(rows: list[tuple[tuple[int, int, int], str, int]]) -> str:
    counts = Counter(result for _, result, _ in rows)
    profiles = Counter(scores for scores, _, _ in rows)
    req = MIRAEL_ENDING_REQUIREMENTS
    total = len(rows)
    human = counts[ENDING_HUMAN]
    guardian = counts[ENDING_GUARDIAN]

    lines = [
        "# Логика концовок маршрута Мираэль — автоматический перебор",
        "",
        "Этот отчёт строится скриптом `scripts/test_mirael_endings.py` без Ren’Py SDK.",
        "В игре сами значения накапливаются в меню общей ветки и M01–M05; единый резолвер находится в `game/mirael_logic.py`.",
        "",
        "## Правило",
        "",
        f"- E01 (`human`), если `mirael_autonomy >= {req['mirael_autonomy']}`, `alex_responsibility >= {req['alex_responsibility']}` и `mirael_closeness >= {req['mirael_closeness']}`.",
        "- Во всех остальных случаях E02 (`guardian`).",
        "- `mirael_closeness` не является скрытой наградой за правильный выбор: в обычном полном прохождении это 2 линейных события — рука в M03 и поцелуй в M06. Порог защищает от неполного/неправильного входа в M07.",
        "",
        "## Что реально влияет",
        "",
        "| Блок | Выборы | Эффект |",
        "|---|---|---|",
        "| Ответственность Александра | C00-S01, C00-S04, C01-S02, C04-S03 | каждый ответственный вариант `+1`, максимум 4 |",
        "| Автономия Мираэль | C03-S02, C04-S01, C05-S03, M01-S03, M03-S03 | C03: удалить фото `+1`, сохранить `0`; остальные четыре: уважение `+1`, контроль `-1` |",
        "| Связанный выбор | M05-S04 | остановиться: `autonomy +1`, `responsibility +1`; оставить черновик: `autonomy -1` |",
        "| Близость | M03, M06 | линейно `+1` за руку и `+1` за поцелуй |",
        "",
        "`evidence_depth`, `lena_trust`, `artem_trust`, `valeria_boundaries` и `mirael_memory` сейчас не подмешиваются в E01/E02. Они не должны случайно менять эту концовку до написания соответствующих маршрутов.",
        "",
        "## Полный перебор",
        "",
        f"Проверено независимых профилей: **{total}** (2¹⁰).",
        f"- E01: **{human}** ({human / total:.1%})",
        f"- E02: **{guardian}** ({guardian / total:.1%})",
        f"- Диапазон `mirael_autonomy`: **{min(s[0] for s, _, _ in rows)}…{max(s[0] for s, _, _ in rows)}**.",
        f"- Диапазон `alex_responsibility`: **{min(s[1] for s, _, _ in rows)}…{max(s[1] for s, _, _ in rows)}**.",
        f"- `mirael_closeness`: **{min(s[2] for s, _, _ in rows)}…{max(s[2] for s, _, _ in rows)}** в полном маршруте.",
        "",
        "| `autonomy` | `responsibility` | `closeness` | Профилей | Итог |",
        "|---:|---:|---:|---:|---|",
    ]
    # Print each distinct score profile once; the exhaustive count remains in
    # the summary above.
    for (autonomy, responsibility, closeness), amount in sorted(profiles.items()):
        result = resolve_mirael_ending(autonomy, responsibility, closeness)
        lines.append(f"| {autonomy} | {responsibility} | {closeness} | {amount} | {result} |")
    lines.extend(
        [
            "",
            "## Контрольные границы",
            "",
            "- `(3, 2, 2)` → E01.",
            "- `(2, 2, 2)` → E02: не хватает одного пункта автономии.",
            "- `(3, 1, 2)` → E02: не хватает одного пункта ответственности.",
            "- `(3, 2, 1)` → E02: маршрут не завершил оба линейных романтических события.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    validate_boundaries()
    validate_runtime_scoring_sources()
    rows = []
    for bits in itertools.product((False, True), repeat=len(DECISIONS)):
        scores = score(bits)
        result = resolve_mirael_ending(*scores)
        rows.append((scores, result, 1))

    # Check every generated state also has a complete, self-consistent report.
    for scores, result, _ in rows:
        report = ending_report(*scores)
        assert report["ending"] == result
        assert all(isinstance(value, bool) for value in report["checks"].values())

    output = ROOT / "docs" / "manuscript" / "mirael-ending-logic-report.md"
    output.write_text(render_report(rows), encoding="utf-8")

    counts = Counter(result for _, result, _ in rows)
    print(
        "Mirael ending logic passed: "
        f"{len(rows)} profiles, E01={counts[ENDING_HUMAN]}, "
        f"E02={counts[ENDING_GUARDIAN]}. Wrote {output.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
