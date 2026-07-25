# Don’t Look to the Sky

Некоммерческая визуальная новелла на Ren’Py. Проект в разработке.

## Текущий статус

Подключено технически (диспетчер `game/script.rpy` их вызывает), но не во всём равноценно готово:

- `C00–C03` — новая романная редакция общей недели, полностью написана и проходит стилевые проверки;
- `C04–C09` — старая реализация из `main`, ниже планового объёма и не проходит `style_guard.py`; ожидает переписывания по новым посценовым картам (`docs/story/c04-plan-earth.md`, `c05-plan-earth.md`, `c06-plan.md`); `C07–C09` признаны сюжетным утилем (следственная линия с камерами и записями отменена);
- маршрут Мираэль `M01–M07` и финалы `E01/E02` — написаны, resolver проверен на 1024 профилях, часть глав не проходит `style_guard.py`;
- маршрут Валерии `V01–V08` и финалы `E03–E05` — написаны, resolver проверен на 64 профилях, проходит `style_guard.py` полностью;
- нейтральный маршрут — перепроектирован только на уровне карты (`docs/story/routes/neutral-plan.md`), художественного текста ещё нет.

Полная целевая архитектура — 21 день, общая неделя + три версии дня 8 + переплетённые дни 9–12 со скрытым resolver + ведущие линии дней 13–21 — описана в [мастер-структуре](docs/story/master-structure.md), но диспетчер `game/script.rpy` пока собран по старой модели (один выбор маршрута после C09).

Подробности и полный список известных несоответствий: [состояние проекта](docs/state/project-state.md).

## С чего начать

### Для сюжетной работы

0. **[Мастер-структура](docs/story/master-structure.md) — главный структурный документ; при противоречиях он главный**
1. [Главная рабочая инструкция](PRIMARY-WORK-INSTRUCTION.md)
2. [Жёсткие блокеры](HARD-BLOCKERS.md)
3. [Авторский голос](SKILL.md)
4. [Библия персонажей](docs/bible/character-bible.md)
5. [Космология](docs/bible/cosmology-bible.md)
6. [Макроструктура](docs/story/story-structure.md)
7. [Карта активного канона](docs/story/story-map.md)
8. [Утверждённое ядро Валерии](docs/story/routes/valeria-brief.md)
9. [Полный план маршрута Валерии](docs/story/routes/valeria-plan.md)
10. [Утверждённое ядро нейтрального маршрута](docs/story/routes/neutral-brief.md)
11. [План мистического нейтрального маршрута](docs/story/routes/neutral-plan.md)

[Примеры авторских правок](examples.md) используются для адресной калибровки.

### Для технической работы

```bash
python3 scripts/style_guard.py game/<chapter>.rpy
python3 scripts/validate_renpy_static.py
python3 scripts/test_mirael_endings.py
python3 scripts/test_valeria_endings.py
python3 scripts/audit_text_transfer.py
python3 scripts/chapter_gate.py <chapter>
```

При установленном Ren’Py SDK:

```bash
RENPY_SDK=/path/to/renpy-sdk scripts/run_renpy_checks.sh
```

## Канонический текст

Художественный источник находится только в `game/*.rpy`.

```text
game/
├── c00.rpy–c09.rpy
├── m01.rpy–m07.rpy
├── v01.rpy–v08.rpy
├── e01.rpy–e05.rpy
├── definitions.rpy
├── script.rpy
└── UI/config files
```

`docs/manuscript/*.md` — автоматически создаваемые зеркала для чтения. Они не редактируются вручную.

## Документация

```text
docs/
├── bible/       — персонажи и краткий навигатор голосов
├── state/       — текущий этап
├── story/       — канон мира, маршруты и постановка
├── manuscript/  — зеркала активной прозы и несколько актуальных аудитов
└── licenses/    — лицензии ассетов
```

Ключевые документы завершённой линии Мираэль:

- [план маршрута](docs/story/routes/mirael-plan.md)
- [детальный итоговый проход](docs/manuscript/mirael-route-full-read.md)
- [автоматическая логика концовок](docs/manuscript/mirael-ending-logic-report.md)

## Ассеты

- `images/` — фоны, персонажи и референсы;
- `game/audio/music/`, `game/audio/sfx/` — подключённые музыка и звуки, определены в `definitions.rpy`;
- `game/ui/` — используемые интерфейсные ассеты;
- `images/ui_source/` — исходные UI-листы, сохранены для дальнейшей нарезки.

Ren’Py SDK и собранные файлы игры в репозитории не хранятся.

## Git

- Ассистент работает только в закреплённой Arena-ветке.
- Merge в `main` не выполняется ассистентом.
- Автор самостоятельно сливает ветку после завершения всей совместной работы.
