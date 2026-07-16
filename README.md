# Don’t Look to the Sky

Некоммерческая визуальная новелла на Ren’Py. В разработке.

## С чего начать

Если ты здесь впервые:

1. [Состояние проекта](docs/state/project-state.md) — где мы сейчас.
2. [Библия персонажей](docs/bible/character-bible.md) — кто здесь живёт.
3. [Сюжетная структура](docs/story/story-structure.md) и [сюжетная карта](docs/story/story-map.md) — что вообще происходит.
4. [Голос автора](SKILL.md) и [фильтр ИИ-клише](anti-cliche-filter.md) — как это написано.

Если ты возвращаешься к работе:

1. [Протокол написания](docs/production/writing-protocol.md) — обязательные шаги перед текстом.
2. [Фильтры и рекурсивная проверка](docs/filters/recursive-check.md) — R0–R6.
3. [Концепция активного маршрута](docs/story/routes/) — то, что сейчас пишется.

## Корень

- [SKILL.md](SKILL.md) — канон авторского голоса (`author-voice-v2`).
- [anti-cliche-filter.md](anti-cliche-filter.md) — жёсткие запреты и список маркеров.
- [examples.md](examples.md) — реальные правки «было → стало», калибровка по приёмам.

## Документация

### Сюжет и маршруты

- [Макроструктура сюжета](docs/story/story-structure.md)
- [Сюжетная карта активного канона](docs/story/story-map.md)
- [Посценовый план общей ветки](docs/story/common-route-outline.md)
- [Бит-карты C00](docs/story/beat-sheets/c00-beat-sheet.md)
- [Бит-карты C01–C03](docs/story/beat-sheets/c01-c03-beat-sheet.md)
- [Список необходимых ресурсов](docs/story/beat-sheets/asset-list.md)
- [Маршрут Мираэль — полный план](docs/story/routes/mirael-plan.md)
- [Дополнения к маршруту Мираэль](docs/story/routes/mirael-additions.md)
- [Концепция маршрута Валерии](docs/story/routes/valeria-brief.md)
- [V01 — рабочая карта перед написанием](docs/story/routes/v01-beat-map.md)

### Голос, персонажи, производство

- [Библия персонажей](docs/bible/character-bible.md)
- [Голос автора и речевые профили](docs/bible/voice-and-characters.md)
- [Методика производства текста](docs/production/production-method.md)
- [Протокол написания](docs/production/writing-protocol.md)
- [Фильтры и рекурсивная проверка](docs/filters/recursive-check.md)

### Техническое

- [Технический каркас Ren’Py](docs/story/renpy-vertical-slice.md)
- [UI — направление](docs/story/ui-direction.md)
- [UI — спецификация ассетов](docs/story/ui-asset-spec.md)
- [SFX manifest](docs/story/sfx-manifest.md)
- [Музыкальная драматургия](docs/story/music-direction.md)
- [Объём и время прохождения](docs/story/volume-and-playtime.md)

## Канонические рукописи

Художественный текст пишется в `game/*.rpy`. Зеркала в `docs/manuscript/*.md` генерируются автоматически и **не редактируются вручную**.

### Общая ветка

- [C00](docs/manuscript/c00.md), [C01](docs/manuscript/c01.md), [C02](docs/manuscript/c02.md), [C03](docs/manuscript/c03.md), [C04](docs/manuscript/c04.md), [C05](docs/manuscript/c05.md), [C06](docs/manuscript/c06.md), [C07](docs/manuscript/c07.md), [C08](docs/manuscript/c08.md), [C09](docs/manuscript/c09.md)

### Маршрут Мираэль

- [M01](docs/manuscript/m01.md), [M02](docs/manuscript/m02.md), [M03](docs/manuscript/m03.md), [M04](docs/manuscript/m04.md), [M05](docs/manuscript/m05.md), [M06](docs/manuscript/m06.md), [M07](docs/manuscript/m07.md)
- [E01 — «Остаться»](docs/manuscript/e01.md), [E02 — «Хранитель»](docs/manuscript/e02.md)

### Сводные обзоры и аудиты

- [Аудит C00–C09](docs/manuscript/c00-c09-audit.md)
- [Рекурсивный проход C00–C09](docs/manuscript/c00-c09-recursive-review.md)
- [Полный аудит общей ветки и Мираэль](docs/manuscript/full-route-review.md)
- [Интегрированный проход Мираэль](docs/manuscript/mirael-route-integrated-review.md)
- [Полный детальный проход Мираэль](docs/manuscript/mirael-route-full-read.md)
- [Контрольный аудит E01/E02](docs/manuscript/mirael-endings-review.md)
- [Логика концовок Мираэль](docs/manuscript/mirael-ending-logic-report.md)
- [Рекурсивные ревью отдельных глав Мираэль](docs/manuscript/m02-recursive-review.md) — [M03](docs/manuscript/m03-recursive-review.md) — [M05](docs/manuscript/m05-recursive-review.md) — [M06](docs/manuscript/m06-recursive-review.md) — [M07](docs/manuscript/m07-recursive-review.md)
- [Аудит переноса текста в Ren’Py](docs/manuscript/renpy-text-audit.md)
- [Полный аудит переноса C00–C09 и M01–M07](docs/manuscript/renpy-full-transfer-audit.md)
- [Классификация переноса](docs/manuscript/renpy-transfer-classification.md)
- [P0 — контрольный аудит после восстановления](docs/manuscript/p0-closure-audit.md)
- [P1 — редакторский мастер-план](docs/manuscript/p1-editorial-master-plan.md)
- [C00–C03 — ранний аудит](docs/manuscript/c00-c03-audit.md)

## Структура репозитория

```text
корень/
├── SKILL.md, anti-cliche-filter.md, examples.md, README.md
├── game/        — исходники Ren’Py, единственный источник художественного текста
├── renpy/, scripts/ — служебные скрипты
├── docs/
│   ├── bible/         — голос и персонажи
│   ├── filters/       — фильтры и рекурсивные проверки
│   ├── production/    — методика и протокол производства
│   ├── state/         — текущее состояние проекта
│   ├── story/         — сюжет: структура, маршруты, beat-sheets
│   ├── manuscript/    — автогенерируемые зеркала .rpy-файлов
│   ├── reference/     — внешние референсы
│   ├── licenses/      — лицензии ассетов
│   └── archive/       — устаревшие и дублирующие документы
├── images/, audio/    — исходники ассетов
└── *.png, *.mp3, *.zip — готовые ассеты
```

## Рабочее правило

- Художественный текст пишется только в `game/*.rpy`.
- Все ссылки на организационные документы — относительные, от корня.
- merge в `main` не выполняется без явной команды автора.
- Push только в рабочую ветку `arena/019f682c-dontlooktothesky`.

Текущий производственный этап — **проектирование и написание маршрута Валерии с нуля**. UI и SFX поддерживаются вторично.
