# Документация

## Структура

| Папка | Содержание |
|---|---|
| [`bible/`](bible/) | подробная библия персонажей и краткий навигатор голосов |
| [`state/`](state/) | текущий этап и границы разрешённой работы |
| [`story/`](story/) | мир, активная сюжетная карта, маршруты, UI и звук |
| [`manuscript/`](manuscript/) | зеркала канонических `.rpy` и актуальные контрольные отчёты |
| [`licenses/`](licenses/) | лицензии шрифтов и звуков |

## Иерархия

1. Прямое решение автора.
2. [`../PRIMARY-WORK-INSTRUCTION.md`](../PRIMARY-WORK-INSTRUCTION.md).
3. [`state/project-state.md`](state/project-state.md).
4. [`story/story-structure.md`](story/story-structure.md) и активный маршрут.
5. [`bible/character-bible.md`](bible/character-bible.md).
6. [`../SKILL.md`](../SKILL.md) и [`../HARD-BLOCKERS.md`](../HARD-BLOCKERS.md).
7. Канонический художественный текст в `../game/`.

## Правило зеркал

```text
game/*.rpy → scripts/extract_rpy_manuscript.py → docs/manuscript/*.md
```

Художественные правки вносятся только в `.rpy`. Зеркала пересоздаются после стабилизации текста.

## Удалённые документы

Старые V/N-карты, произведённые по ним рукописи, дублирующие инструкции и архивные копии удалены. История Git остаётся единственным архивом устаревших версий.
