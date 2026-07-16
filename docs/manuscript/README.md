# docs/manuscript/

Зеркала художественного текста и обзоры. **Эти файлы генерируются автоматически и не редактируются вручную.**

## Что здесь лежит

- **Канонические рукописи** — `c00.md`–`c09.md`, `m01.md`–`m07.md`, `e01.md`, `e02.md`. Это зеркала соответствующих `game/*.rpy`. Скрипт: `scripts/extract_rpy_manuscript.py`.
- **Сводные обзоры и аудиты** — `c00-c09-*.md`, `mirael-route-*.md`, `full-route-review.md`, `p0-closure-audit.md`, `p1-editorial-master-plan.md`.
- **Рекурсивные ревью отдельных глав** — `m02-recursive-review.md`, `m03-recursive-review.md`, `m05-recursive-review.md`, `m06-recursive-review.md`, `m07-recursive-review.md`.
- **Аудиты переноса текста в Ren’Py** — `renpy-text-audit.md`, `renpy-full-transfer-audit.md`, `renpy-transfer-classification.md`.
- **Аудиты концовок** — `mirael-endings-review.md`, `mirael-ending-logic-report.md`.
- **Закрытые служебные документы** — `m07-recursive-review.md` есть отдельный `m07-recursive-review.md` для M07 (см. список в `README.md` корня).

## Что читать, а что нет

- **Читать как канон:** только `c0*.md`, `m0*.md`, `e0*.md`. Если они расходятся с `game/*.rpy` — баг в зеркале, чинится пересборкой.
- **Читать при конкретной задаче:** сводные обзоры и рекурсивные ревью, когда нужно сверить голос, причинность или фильтры по конкретной главе.
- **Не читать как источник правды для нового текста:** обзоры и ревью. Они фиксируют, **что было решено раньше**, но приоритет имеют последние прямые решения автора и текущая версия в `game/*.rpy`.

## Как обновляется

```text
game/*.rpy  →  scripts/extract_rpy_manuscript.py  →  docs/manuscript/*.md
```

После правки `.rpy` пересобрать зеркало, прогнать `scripts/audit_text_transfer.py` и `scripts/validate_renpy_static.py`.
