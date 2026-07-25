# Трекер фонов — что используется, что доступно, чего не хватает

**Статус:** рабочий журнал ассетов, ведётся по ходу написания глав. Автор предупредил, что
многие текущие фоны — черновые заглушки и, скорее всего, будут заменены позже. Цель этого
документа — не потерять, что уже подключено, и заранее видеть, чего физически не хватает,
когда дело дойдёт до конкретной сцены.

**Как читать:** «Подключено в C00» — уже используется в написанном тексте. «Доступно, не
использовано» — файл существует в `images/backgrounds/`, но ни в одной сцене пока не
задействован. «Нужно, но нет» — сцена по плану требует места, для которого ассета ещё не
существует ни в файлах, ни в `definitions.rpy`.

## Подключено и используется (C00)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | C00-S01, утро в квартире |
| `bg depot morning` | `bg_delivery_depot_morning_clean.png` | C00-S02, депо |
| `bg street day` | `bg_street_no_rain.jpeg` | C00-S02/03/06, обычные уличные сцены |
| `bg client corridor` | `bg_client_building_corridor.png` | C00-S03/05, бизнес-центр |
| `bg private sector day` | `bg_private_sector_day.png` | C00-S03/05, частный сектор |
| `bg town square` | `bg_town_square.png` | C00-S04, обед с Леной |
| `bg city square day` | `bg_city_square_day_market.png` | C00-S05, дневная суета |
| `bg rain street` | `bg_rain_street.png` | C00-S06–S10, дождь, авария, дорога домой |
| `bg alex room night` | `bg_alex_room_night.jpeg` | C00-S11, финальная ночная сцена |

Итого 9 уникальных фонов реально задействованы в C00 из 9 использованных alias'ов —
дублирования нет, экономно.

## Доступно в `images/backgrounds/`, но пока не использовано ни в одной написанной главе

Эти файлы физически лежат в репозитории, но либо не имеют alias в `definitions.rpy`, либо
имеют alias, который ни разу не вызван в `game/*.rpy` из глав, признанных «в силе»:

- `bg_apartment_entrance_day.jpeg` / `bg_apartment_entrance_evening.png` — вход в подъезд
- `bg_bus_stop_rain_evening.png` — автобусная остановка под дождём
- `bg_pharmacy_day_clean.jpeg` / `bg_small_pharmacy_exterior_rain.png` — аптека (сухая/дождь)
- `bg_bridge.png`, `bg_embankment_evening.png`, `bg_rooftop_night_city_clean.png` — открытые
  городские пространства (мост, набережная, крыша) — зарезервированы под сцены дней 13–20,
  см. `full-story-plan.md`
- `bg_city_square_market_night.jpeg` — ночной рынок/площадь
- `bg_city_park_autumn_day.png`, `city_park_night.png` — парк (день/ночь)
- `bg_stairwell_old_evening.png` — лестничная клетка
- `bg_garage_workshop_day.png` — мастерская/гараж
- `city_internet_cafe.png`, `city_library.png`, `city_occult_shop.png` — нейтральная линия,
  места поиска источников (см. `routes/neutral-plan.md`)
- Верх (8 фонов): `verkh_edge.png`, `verkh_fields.png`, `verkh_gardens.png`, `verkh_grove.png`,
  `verkh_library.png`, `verkh_river.png`, `verkh_village.png`, `verkh_workshop.png` — для дней
  13–21, локации Верха как реального места (`master-structure.md` §5)
- Пекло (7 фонов): `peklo_flow.png`, `peklo_pain_bank.png`, `peklo_pain_bank_classic.png`,
  `peklo_reception.png`, `peklo_tunnel.png`, `peklo_tunnel_gates.png`, `peklo_village_gates.png`
  — то же самое для дней 13–21
- Административные/промежуточные (вероятно устареют под новую логику «иные измерения вместо
  инстанций», см. `master-structure.md` §5): `bg_admin_core_terminal.png`,
  `bg_admin_council_amphitheater.png`, `bg_admin_tunnel_lock.png`, `bg_grey_zone_terminal.png`,
  `bg_inferno_reception_dark.png`
- Валерия (её земные и рабочие интерьеры — актуальность под новую логику уточнить):
  `bg_valeria_apartment_night.png`, `bg_valeria_office_corridor.png`,
  `bg_valeria_office_day_clean.png`, `bg_valeria_office_night_clean.png`,
  `bg_valeria_rest_room_night.png`
- `bg_abandoned_boiler_room.png`, `bg_memory_space_mirael_soft.png`, `bg_upper_observatory.png`
  — назначение не уточнено, вероятно старые заготовки
- `bg_private_sector_night.jpeg` — ночная версия частного сектора (дневная уже используется)
- `alex_room_rainy.png`, `bg_alex_room_rainy.jpeg`, `room_alex.png` — дублирующие/альтернативные
  версии комнаты Александра, не расчищены

## Нужно, но пока нет ни файла, ни alias

По `full-story-plan.md`, ближайшие главы (C01–C06) потребуют:

- **Ванная в квартире Александра** — крупный план для сцен телесных границ (C01) — нет
  отдельного фона, вероятно можно обойтись интерьером комнаты за кадром.
- **Мастерская велосипедов/веломастерская** — упоминается в плане (велосипед в ремонте) —
  нет подходящего фона (гараж/мастерская есть, но не проверено, подходит ли по духу).
- **Кафе/бар для вечерних сцен** — понадобится в C05 (программирование/аниме/юмор дома —
  не требует нового фона) и потенциально в день 8 (М) — «кафе с мороженым».
- **Депо вечером** (сейчас есть только «depot morning») — если появится вечерняя сцена в
  депо, нужен отдельный вариант освещения.

## Правило ведения

Обновлять эту таблицу сразу после того, как глава с новыми фонами попадает в `game/*.rpy` и
проходит `validate_renpy_static.py`. Если автор заменяет фон — просто менять путь в
`definitions.rpy`, не трогая `game/*.rpy` (alias остаётся прежним) там, где это возможно.
