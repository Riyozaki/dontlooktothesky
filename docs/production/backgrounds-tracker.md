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

## Подключено и используется (C01)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | C01-S01–S06, утро и день в квартире |
| `bg alex room night` | `bg_alex_room_night.jpeg` | C01-S07–S08, вечер, приход Валерии |
| `bg garage workshop day` | `bg_garage_workshop_day.png` | C01-S06 (вставка), мастерская — ремонт велосипеда |

## Подключено и используется (C02)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | C02-S01, утро в квартире |
| `bg street day` | `bg_street_no_rain.jpeg` | C02-S02/S05, дорога к барбершопу и доставка |
| `bg barbershop day` | `bg_barbershop_day.png` (новый, сгенерирован 26.07.2026) | C02-S02–S04, барбершоп Артёма |
| `bg depot morning` | `bg_delivery_depot_morning_clean.png` | C02-S05, депо |
| `bg alex room night` | `bg_alex_room_night.jpeg` | C02-S06, вечерний разговор с Мираэль |

Новый фон `bg_barbershop_day.png` сгенерирован специально под эту главу — раньше в проекте
не было интерьера барбершопа. Стиль откалиброван по образцу `bg_town_square.png` (тёплая
иллюстрация, полутоновая штриховка, без фотореализма и без интерфейсных элементов).

## Подключено и используется (C03)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | C03-S01/S02, утро в квартире |
| `bg street day` | `bg_street_no_rain.jpeg` | C03-S03/S08, автобус к родителям, дорога домой |
| `bg apartment entrance day` | `bg_apartment_entrance_day.jpeg` | C03-S04–S07, квартира родителей |
| `bg alex room night` | `bg_alex_room_night.jpeg` | C03-S09, вечерний поиск ответов |

Ни одного нового фона под C03 не потребовалось — все локации уже существовали
(`bg apartment entrance day` ранее не использовался в написанных главах, но существовал в
`definitions.rpy` с самого начала).

## Подключено и используется (C04)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | C04-S01/S02, утро в квартире |
| `bg stairwell old evening` | `bg_stairwell_old_evening.png` (новый alias с пробелами, файл уже существовал) | C04-S03, пороговый переход на лестнице |
| `bg street day` | `bg_street_no_rain.jpeg` | C04-S04, встреча с Никой |
| `bg depot morning` | `bg_delivery_depot_morning_clean.png` | C04-S05, депо |
| `bg private sector day` | `bg_private_sector_day.png` | C04-S05, доставка в частном секторе |
| `bg alex room night` | `bg_alex_room_night.jpeg` | C04-S06/S07, вечер и ночь дома |

Новых фонов не потребовалось — `bg_stairwell_old_evening.png` уже существовал в файлах, но не
был подключён как alias с пробелами (только с подчёркиванием для старого стиля вставки).
Добавлен `bg stairwell old evening` для единообразия с остальными сценами. Идеально подошёл
для порогового перехода — обычная подъездная лестница с достаточно тревожной атмосферой.

## Подключено и используется (C05)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | C05-S01/S03/S05, утро и день дома |
| `bg barbershop day` | `bg_barbershop_day.png` | C05-S02, Александр забирает компьютер у Артёма |
| `bg city park autumn day` | `bg_city_park_autumn_day.png` (существовал, не был подключён в написанных главах) | C05-S04, случайная встреча с Валерией на скамейке в парке |
| `bg alex room night` | `bg_alex_room_night.jpeg` | C05-S06/S07, аниме-вечер, визит Лены, ночь |

Ни одного нового фона генерировать не пришлось — парк уже существовал в `images/backgrounds/`
(`bg_city_park_autumn_day.png`), просто не был использован ни в одной написанной главе до сих
пор. Компьютерный уголок и квартира Артёма показаны тем же фоном барбершопа (интерьер квартиры
отдельно не выведен на экран — сцена подана через диалог и предметы, без смены фона).

**По прямому указанию автора (27.07.2026): не нужно подгонять текст под наличие/отсутствие
фонов.** Автор планирует отдельно провести масштабную работу по генерации новых и замене старых
фонов (по аналогии с CG-листом) — писать сцены свободно, ориентируясь на сюжет, а нужные фоны
просто накапливать отдельным списком для будущей пакетной генерации.

## Подключено и используется (C06)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | C06-S01, утро дома |
| `bg depot morning` | `bg_delivery_depot_morning_clean.png` | C06-S02, обычная рабочая смена |
| `bg alex room night` | `bg_alex_room_night.jpeg` | C06-S03/S04/S05, вечер и ночь дома |

Ни одного нового фона не потребовалось — все три уже были подключены в предыдущих главах.
Уличная сцена с мимолётной встречей Валерии (C06-S02) не выводит отдельный фон и происходит
внутри той же сцены депо — по сюжету это короткое наблюдение на ходу, без остановки, поэтому
смена задника не понадобилась содержательно.

## Подключено и используется (D08_N)

| Alias в `definitions.rpy` | Файл | Где используется |
|---|---|---|
| `bg alex room dawn` | `bg_alex_room_evening_or_dawn.jpeg` | D08_N-S01, утро дома |
| `bg city library` | `city_library.png` (существовал, не был подключён с алиасом через пробелы) | D08_N-S02, поиск в библиотеке |
| `bg street day` | `bg_street_no_rain.jpeg` | D08_N-S03, ступени библиотеки, разговор с Валерией |
| `bg city square day` | `bg_city_square_day_market.png` | D08_N-S04, обед с Леной у фонтана |
| `bg alex room night` | `bg_alex_room_night.jpeg` | D08_N-S05/S06, вечер и ночь дома |

Один новый alias подключён (`bg city library`) — файл `city_library.png` уже существовал в
репозитории, но не имел alias с пробелами для прямой вставки в `scene`. Заодно добавлены
алиасы `bg city internet cafe` и `bg city occult shop` (пока не использованы ни в одной сцене —
задел на следующие главы нейтральной линии, где Александр, вероятно, продолжит поиск).

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
- `city_internet_cafe.png`, `city_occult_shop.png` — нейтральная линия, места поиска источников
  (см. `routes/neutral-plan.md`); `city_library.png` уже подключена и используется в D08_N
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

## Нужно, но пока нет ни файла, ни alias (список для будущей пакетной генерации)

По прямому решению автора (27.07.2026) этот раздел — просто рабочий список пожеланий, не
блокер для письма: сцены пишутся свободно по сюжету, а подбор/генерация фонов откладывается
на отдельную большую сессию, аналогично будущему CG-листу.

- **Кафе/бар для вечерних сцен** — пока не понадобился напрямую (C05 использовала парк вместо
  кафе для сцены с Валерией), но пригодится в будущих главах, особенно в день 8 (М) — «кафе с
  мороженым».
- **Депо вечером** (сейчас есть только «depot morning») — если появится вечерняя сцена в
  депо, нужен отдельный вариант освещения.
- **Интерьер квартиры Артёма** — использовался только на словах в C05 (компьютер забирают из
  его квартиры), отдельного фона не потребовалось, сцена подана без смены задника.

Закрыто в этой сессии: «ванная в квартире Александра» — решили обойтись интерьером комнаты
за кадром, отдельного фона не понадобилось. «Мастерская велосипедов» — `bg_garage_workshop_day.png`
подошёл по духу, подключён как `bg garage workshop day` в C01. «Барбершоп Артёма» — новый фон
`bg_barbershop_day.png` сгенерирован и подключён в C02. «Городской парк» — существовавший
`bg_city_park_autumn_day.png` наконец использован в C05.

## Правило ведения

Обновлять эту таблицу сразу после того, как глава с новыми фонами попадает в `game/*.rpy` и
проходит `validate_renpy_static.py`. Если автор заменяет фон — просто менять путь в
`definitions.rpy`, не трогая `game/*.rpy` (alias остаётся прежним) там, где это возможно.
