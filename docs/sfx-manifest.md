# SFX manifest

**Статус:** подготовка к подбору файлов

| ID | Назначение | Сцены | Файл | Источник | Лицензия | Статус |
|---|---|---|---|---|---|---|
| phone_vibrate | вибрация телефона | C00, C01, C02, C03 | — | — | — | нужен |
| phone_notification | уведомление | C00, C01 | — | — | — | нужен |
| door_apartment | дверь подъезда | C00, C03 | — | — | — | нужен |
| bicycle_lock | замок велосипеда | C00 | — | — | — | нужен |
| bicycle_brake | торможение | C00, C02 | — | — | — | нужен |
| plaster_fall | падение штукатурки | C00 | — | — | — | нужен |
| depot_scanner | сканер депо | C00 | — | — | — | нужен |
| package_handling | коробка, лента, упаковка | C00, C01 | — | — | — | нужен |
| bank_terminal | терминал банка | C01 | — | — | — | нужен |
| intercom | домофон | C01 | — | — | — | нужен |
| rain_light | лёгкий дождь | C01, C02 | — | — | — | нужен |
| rain_heavy | сильный дождь | C02 | — | — | — | нужен |
| car_pass_wet | машина на мокрой дороге | C02 | — | — | — | нужен |
| tire_skid | торможение автомобиля | C02 | — | — | — | нужен |
| car_impact | столкновение | C02 | — | — | — | нужен |
| bicycle_crash | падение велосипеда | C02 | — | — | — | нужен |
| phone_cracked | повреждение телефона | C02 | — | — | — | нужен |
| emergency_fail | неудачное соединение | C02 | — | — | — | нужен |
| dead_interval_drop | обрыв звукового слоя | C02 | — | — | — | реализовать тишиной |
| city_return | возвращение городского шума | C02 | — | — | — | нужен |
| wing_shift | движение крыльев | C02 | — | — | — | нужен |
| key_lock | ключ в замке | C03 | — | — | — | нужен |
| kettle | чайник | C03 | — | — | — | нужен |
| sofa_open | раскладывание дивана | C03 | — | — | — | нужен |
| door_knock | стук в дверь | C03 | — | — | — | нужен |

## Предпочтительная компактная альтернатива

Большой Sonniss-пак пока откладываем. Для небольшого вертикального среза достаточно двух компактных пакетов Kenney:

1. [Interface Sounds](https://kenney.nl/assets/interface-sounds) — 100 UI-звуков, лицензия CC0.
2. [Impact Sounds](https://kenney.nl/assets/impact-sounds) — 130 эффектов ударов и столкновений, лицензия CC0.

Они закроют:

- кнопки и подтверждения;
- навигацию;
- ошибки и отмену;
- часть ударов и падений;
- базовые звуки аварии.

Для дождя, двери, телефона и велосипеда позже можно добавить отдельные короткие CC0-записи, выбирая лицензию на уровне конкретного файла. Не нужно скачивать целую библиотеку ради одного эффекта.

Если эти два пакета будут загружаться в GitHub вручную, временно положить ZIP-файлы в:

```text
_incoming/sfx/kenney/
```

После отбора в игру попадут только нужные обработанные файлы из `game/audio/sfx/`, а ZIP-архивы будут удалены из рабочей версии.

## Выбранные файлы из Kenney

В рабочую ветку добавлен небольшой отбор. ZIP-архивы и неиспользованные варианты в репозиторий не попадают.

| Файл | Исходник | Назначение |
|---|---|---|
| `ui_back.ogg` | Interface Sounds / `back_001.ogg` | возврат |
| `ui_select.ogg` | Interface Sounds / `select_001.ogg` | выбор |
| `ui_confirm.ogg` | Interface Sounds / `confirmation_001.ogg` | подтверждение |
| `ui_error.ogg` | Interface Sounds / `error_001.ogg` | ошибка |
| `ui_toggle.ogg` | Interface Sounds / `toggle_001.ogg` | переключатель |
| `ui_click.ogg` | Interface Sounds / `click_001.ogg` | общий клик |
| `ui_open.ogg` | Interface Sounds / `open_001.ogg` | открытие |
| `ui_close.ogg` | Interface Sounds / `close_001.ogg` | закрытие |
| `ui_question.ogg` | Interface Sounds / `question_001.ogg` | вопросительный акцент |
| `footstep_concrete.ogg` | Impact Sounds / `footstep_concrete_000.ogg` | подъезд и город |
| `impact_metal_heavy.ogg` | Impact Sounds / `impactMetal_heavy_001.ogg` | тяжёлый металлический удар |
| `impact_metal_light.ogg` | Impact Sounds / `impactMetal_light_001.ogg` | велосипед и мелкий металл |
| `impact_glass_light.ogg` | Impact Sounds / `impactGlass_light_000.ogg` | трещина телефона или стекло |
| `impact_generic_light.ogg` | Impact Sounds / `impactGeneric_light_001.ogg` | общий небольшой удар |
| `impact_wood_medium.ogg` | Impact Sounds / `impactWood_medium_001.ogg` | дверь, коробка, бытовой удар |

Лицензии сохранены в `docs/licenses/Kenney-Interface-Sounds-License.txt` и `docs/licenses/Kenney-Impact-Sounds-License.txt`.

UI-файлы подключены к стилям кнопок Ren’Py: hover использует `ui_select.ogg`, нажатие — `ui_click.ogg`, выборы — `ui_confirm.ogg`.

Базовые игровые эффекты уже расставлены в вертикальном срезе: удар штукатурки, автомобильное столкновение, металл велосипеда, разбитый телефон и стук в дверь. Громкость и характер нужно проверить после фактического запуска Ren’Py.

Дождь, телефонную вибрацию, торможение автомобиля и звук крыльев подберём отдельными небольшими файлами позже.

## Правило отбора

Не скачивать весь архив в репозиторий. Сначала выбрать короткие исходники, затем обработать громкость, обрезать тишину, переименовать по ID и сохранить сведения о лицензии.
