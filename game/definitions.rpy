################################################################################
## Персонажи, изображения, музыка и переменные
################################################################################

# Персонажи

define a = Character("Александр", color="#d7e5ff")
define m = Character("Мираэль", color="#fff2c7")
define v = Character("Валерия", color="#e6c8ff")
define l = Character("Лена", color="#ffd1dc")
define n = Character("Ника", color="#ffc7ef")
define ar = Character("Артём", color="#d5e8d4")
define d = Character("Дмитрий", color="#d9d9d9")
define r = Character("Ревизор", color="#c8ced8")
define driver = Character("Водитель", color="#b8b8b8")
define mechanic = Character("Механик", color="#a9a9a9")
define mother = Character("Мать", color="#e5d4c7")

# Фоны. Во время разработки файлы остаются в корневом каталоге assets.
# Перед релизной сборкой будет создан оптимизированный game/assets.
image bg alex room dawn = "../images/backgrounds/bg_alex_room_evening_or_dawn.jpeg"
image bg alex room night = "../images/backgrounds/bg_alex_room_night.jpeg"
image bg apartment entrance day = "../images/backgrounds/bg_apartment_entrance_day.jpeg"
image bg apartment entrance evening = "../images/backgrounds/bg_apartment_entrance_evening.png"
image bg street day = "../images/backgrounds/bg_street_no_rain.jpeg"
image bg depot morning = "../images/backgrounds/bg_delivery_depot_morning_clean.png"
image bg city square day = "../images/backgrounds/bg_city_square_day_market.png"
image bg city square night = "../images/backgrounds/bg_city_square_market_night.jpeg"
image bg town square = "../images/backgrounds/bg_town_square.png"
image bg client corridor = "../images/backgrounds/bg_client_building_corridor.png"
image bg private sector day = "../images/backgrounds/bg_private_sector_day.png"
image bg rain street = "../images/backgrounds/bg_rain_street.png"
image bg bus stop rain = "../images/backgrounds/bg_bus_stop_rain_evening.png"
image bg pharmacy rain = "../images/backgrounds/bg_small_pharmacy_exterior_rain.png"
image bg valeria office = "../images/backgrounds/bg_valeria_office_night_clean.png"
image bg bridge = "../images/backgrounds/bg_bridge.png"
image bg embankment evening = "../images/backgrounds/bg_embankment_evening.png"
image bg rooftop night city clean = "../images/backgrounds/bg_rooftop_night_city_clean.png"

# Новые фоны и алиасы с подчеркиваниями для прямой вставки в scene
image bg_alex_room_evening_or_dawn = "../images/backgrounds/bg_alex_room_evening_or_dawn.jpeg"
image bg_alex_room_night = "../images/backgrounds/bg_alex_room_night.jpeg"
image bg_apartment_entrance_day = "../images/backgrounds/bg_apartment_entrance_day.jpeg"
image bg_apartment_entrance_evening = "../images/backgrounds/bg_apartment_entrance_evening.png"
image bg_street_no_rain = "../images/backgrounds/bg_street_no_rain.jpeg"
image bg_delivery_depot_morning_clean = "../images/backgrounds/bg_delivery_depot_morning_clean.png"
image bg_city_square_day_market = "../images/backgrounds/bg_city_square_day_market.png"
image bg_town_square = "../images/backgrounds/bg_town_square.png"
image bg_client_building_corridor = "../images/backgrounds/bg_client_building_corridor.png"
image bg_private_sector_day = "../images/backgrounds/bg_private_sector_day.png"
image bg_private_sector_night = "../images/backgrounds/bg_private_sector_night.jpeg"
image bg_rain_street = "../images/backgrounds/bg_rain_street.png"
image bg_bus_stop_rain_evening = "../images/backgrounds/bg_bus_stop_rain_evening.png"
image bg_small_pharmacy_exterior_rain = "../images/backgrounds/bg_small_pharmacy_exterior_rain.png"
image bg_valeria_office_corridor = "../images/backgrounds/bg_valeria_office_corridor.png"
image bg_valeria_office_night_clean = "../images/backgrounds/bg_valeria_office_night_clean.png"
image bg_bridge = "../images/backgrounds/bg_bridge.png"
image bg_embankment_evening = "../images/backgrounds/bg_embankment_evening.png"
image bg_rooftop_night_city_clean = "../images/backgrounds/bg_rooftop_night_city_clean.png"
image bg_memory_space_mirael_soft = "../images/backgrounds/bg_memory_space_mirael_soft.png"
image bg_stairwell_old_evening = "../images/backgrounds/bg_stairwell_old_evening.png"

# 12 новых сгенерированных фонов
image bg_admin_council_amphitheater = "../images/backgrounds/bg_admin_council_amphitheater.png"
image bg_admin_core_terminal = "../images/backgrounds/bg_admin_core_terminal.png"
image bg_valeria_apartment_night = "../images/backgrounds/bg_valeria_apartment_night.png"
image bg_valeria_office_day_clean = "../images/backgrounds/bg_valeria_office_day_clean.png"
image bg_admin_tunnel_lock = "../images/backgrounds/bg_admin_tunnel_lock.png"
image bg_abandoned_boiler_room = "../images/backgrounds/bg_abandoned_boiler_room.png"
image bg_valeria_rest_room_night = "../images/backgrounds/bg_valeria_rest_room_night.png"
image bg_grey_zone_terminal = "../images/backgrounds/bg_grey_zone_terminal.png"
image bg_garage_workshop_day = "../images/backgrounds/bg_garage_workshop_day.png"
image bg_inferno_reception_dark = "../images/backgrounds/bg_inferno_reception_dark.png"
image bg_upper_observatory = "../images/backgrounds/bg_upper_observatory.png"
image bg_city_park_autumn_day = "../images/backgrounds/bg_city_park_autumn_day.png"

# Спрайты первой главы
image alex neutral = "../images/characters/aleksandr/alexandr_neutral.png"
image alex shocked = "../images/characters/aleksandr/alexandr_shocked.png"
image alex happy = "../images/characters/aleksandr/alexandr_happy.png"
image alex sad = "../images/characters/aleksandr/alexandr_sad.png"
image alex determined_anger = "../images/characters/aleksandr/alexandr_determined_anger.png"
image alex shocked_terrified = "../images/characters/aleksandr/alexandr_shocked_terrified.png"
image alex shy = "../images/characters/aleksandr/alexandr_shy.png"

# Пак Александра в серой рубашке (для ветки Валерии)
image alex_grey neutral = "../images/characters/aleksandr/alexandr_neutral_grey_shirt.png"
image alex_grey happy = "../images/characters/aleksandr/alexandr_happy_grey_shirt.png"
image alex_grey determined_anger = "../images/characters/aleksandr/alexandr_determined_anger_grey_shirt.png"
image alex_grey sad = "../images/characters/aleksandr/alexandr_sad_grey_shirt.png"
image alex_grey shocked = "../images/characters/aleksandr/alexandr_shocked_grey_shirt.png"
image alex_grey shocked_terrified = "../images/characters/aleksandr/alexandr_shocked_terrified_grey_shirt.png"
image alex_grey shy = "../images/characters/aleksandr/alexandr_shy_grey_shirt.png"

image lena neutral = "../images/characters/lena/lena_neutral.png"
image lena snide = "../images/characters/lena/lena_snide.png"
image lena happy = "../images/characters/lena/lena_happy.png"
image lena sad = "../images/characters/lena/lena_sad.png"
image lena tired = "../images/characters/lena/lena_tired.png"
image dmitry neutral = "../images/characters/dmitry/dmitry_neutral.png"
image dmitry serious = "../images/characters/dmitry/dmitry_serious.png"
# Спрайты первой главы и канонический сет Мираэль (v3 — 24 года, серебристые волосы, ушки, небольшие крылья, раздельный белый комплект)
image mirael neutral = "../images/characters/mirael/mirael_v3_neutral.png"
image mirael happy = "../images/characters/mirael/mirael_v3_happy.png"
image mirael shy = "../images/characters/mirael/mirael_v3_shy.png"
image mirael sad = "../images/characters/mirael/mirael_v3_sad.png"
image mirael crying = "../images/characters/mirael/mirael_v3_crying.png"
image mirael determined_anger = "../images/characters/mirael/mirael_v3_determined_anger.png"
image mirael shocked = "../images/characters/mirael/mirael_v3_shocked_terrified.png"
image mirael shocked_terrified = "../images/characters/mirael/mirael_v3_shocked_terrified.png"
image mirael surprised = "../images/characters/mirael/mirael_v3_surprised.png"
image artem happy = "../images/characters/artem/artem_shank_happy.png"
image artem empty = "../images/characters/artem/artem_shank_empty.png"
# Пак Валерии (v3 — канон: аристократичный корсет с баской, брюки, сапоги, бант с рубином)
image valeria neutral = "../images/characters/valeria/valeria_neutral_v3.png"
image valeria serious = "../images/characters/valeria/valeria_v3_serious.png"
image valeria happy = "../images/characters/valeria/valeria_v3_happy.png"
image valeria sad = "../images/characters/valeria/valeria_v3_sad.png"
image valeria seductive_excited = "../images/characters/valeria/valeria_v3_seductive_excited.png"
image valeria shy = "../images/characters/valeria/valeria_v3_shy.png"
image valeria surprised = "../images/characters/valeria/valeria_v3_surprised.png"
image nika neutral = "../images/characters/nika/nika_neutral.png"

# Рабочие трансформы приводят исходники разного размера примерно к одной высоте.
# После визуального теста значения будут откалиброваны для каждого персонажа.
transform alex_left:
    zoom 0.84
    xalign 0.18
    yalign 1.0

transform alex_center:
    zoom 0.84
    xalign 0.5
    yalign 1.0

transform alex_right:
    zoom 0.84
    xalign 0.82
    yalign 1.0

transform small_sprite_right:
    zoom 0.84
    xalign 0.82
    yalign 1.0

transform sprite_left:
    zoom 0.42
    xalign 0.18
    yalign 1.0

transform sprite_center:
    zoom 0.42
    xalign 0.5
    yalign 1.0

transform sprite_right:
    zoom 0.42
    xalign 0.82
    yalign 1.0

# Музыкальные идентификаторы. Пути снаружи game — временное решение для разработки.
define audio.city_day = "../Sunny Afternoon.mp3"
define audio.delivery_day = "../Golden Afternoon Light.mp3"
define audio.mirael_mystery = "../River Fog.mp3"
define audio.mirael_awake = "../Glass Cathedral.mp3"
define audio.suspense = "../The Hollow Stare.mp3"
define audio.night_solitude = "../Late Night Solitude.mp3"
define audio.quiet_after = "../The Quiet After.mp3"
define audio.valeria_office = "../The Great Office Meeting.mp3"
define audio.valeria_intimate = "../Midnight Boardroom.mp3"
define audio.nika_office = "../The Meeting That Never.mp3"
define audio.observer = "../The Watcher’s Lullaby.mp3"

# Новая адресная музыкальная библиотека. Исходные MP3 загружены автором,
# игровые копии переносятся в game/audio/music по мере работы над сценами.
define audio.work_motion = "audio/music/workflow.mp3"
define audio.neutral_paper_trace = "audio/music/paper_trace.mp3"
define audio.dead_minute = "audio/music/dead_minute.mp3"
define audio.evidence_anxiety = "audio/music/evidence_anxiety.mp3"
define audio.midnight_apartment = "audio/music/midnight_apartment.mp3"
define audio.neutral_quarantine = "audio/music/paper_trace_memory.mp3"

# Компактный набор SFX. Исходники Kenney, лицензии сохранены в docs/licenses.
define audio.sfx_ui_click = "audio/sfx/ui_click.ogg"
define audio.sfx_ui_select = "audio/sfx/ui_select.ogg"
define audio.sfx_ui_confirm = "audio/sfx/ui_confirm.ogg"
define audio.sfx_ui_error = "audio/sfx/ui_error.ogg"
define audio.sfx_ui_open = "audio/sfx/ui_open.ogg"
define audio.sfx_ui_close = "audio/sfx/ui_close.ogg"
define audio.sfx_footstep = "audio/sfx/footstep_concrete.ogg"
define audio.sfx_impact_generic = "audio/sfx/impact_generic_light.ogg"
define audio.sfx_impact_metal = "audio/sfx/impact_metal_heavy.ogg"
define audio.sfx_impact_metal_light = "audio/sfx/impact_metal_light.ogg"
define audio.sfx_impact_glass = "audio/sfx/impact_glass_light.ogg"
define audio.sfx_impact_wood = "audio/sfx/impact_wood_medium.ogg"

# Переменные текущего прохождения
default alex_responsibility = 0
default mirael_autonomy = 0
default mirael_closeness = 0
default mirael_memory = 0
default mirael_ending = None
default valeria_boundaries = 0
default evidence_depth = 0
default lena_trust = 0
default artem_trust = 0
default nika_trust = 0

# Маршрут Валерии: прозрачность и будущие оси встречного договора.
default valeria_transparency = 0
default valeria_reciprocity = 0
default third_party_autonomy = 0
default v01_exact_testimony = False
default v01_mutual_disclosure = False
default v02_shared_reference = False
default v03_full_testimony = False
default v03_corrected_testimony = False
default v04_qte_result = None
default v04_qte_success = False
default v04_route_delay = 0
default v04_read_origin = False
default v05_used_internal_assessment = False
default v08_equal_failures = ()
default valeria_ending = None

# Нейтральный маршрут: доказательная целостность, совместное авторство
# и автономия владельцев сведений.
default neutral_evidence_integrity = 0
default neutral_shared_authorship = 0
default neutral_witness_autonomy = 0
default n01_told_full_reason = False
default n01_operator_absence_confirmed = False
default n01_time_failure_witnessed = False
default n01_outer_sleeve_chain = False
default n01_shared_evidence_rule = False
default lena_supernatural_acknowledged = False

default n02_pharmacy_archive_preserved = False
default n02_service_archive_preserved = False
default n02_actions_inside_gap = False
default n02_used_unapproved_copy = False
default n02_upper_quarantine_read = False
default n02_lower_quarantine_read = False
default n02_quarantine_refused = False
default n02_named_desire_without_pressure = False

# Активный выбор после общей ветки. Будущие маршруты пока ведут на
# информационные заглушки в script.rpy.
default route_selected = None

# Прямые флаги последствий C00
default c00_replied_to_dmitry = False
default c00_reported_manifest_error = False
default c00_helped_lena = False

# Постоянный прогресс. Инициализация безопасна для старых сохранений.
init python:
    from mirael_logic import (
        ENDING_HUMAN,
        ending_report,
        resolve_mirael_ending,
    )
    from valeria_logic import (
        ENDING_EQUAL,
        ENDING_FAILURE,
        ENDING_STANDARD,
        equal_contract_failures,
        equal_contract_is_admissible,
        resolve_valeria_ending,
        valeria_ending_report,
    )

    persistent.ending_mirael_human = getattr(persistent, "ending_mirael_human", False)
    persistent.ending_mirael_guardian = getattr(persistent, "ending_mirael_guardian", False)
    persistent.ending_valeria_equal = getattr(persistent, "ending_valeria_equal", False)
    persistent.ending_valeria_standard = getattr(persistent, "ending_valeria_standard", False)
    persistent.ending_valeria_failure = getattr(persistent, "ending_valeria_failure", False)

    def true_route_is_unlocked():
        """Keep T-route unavailable until all base routes are redesigned."""
        return False

    def mirael_ending_state():
        """Resolve E01/E02 from accumulated values, never from a final menu."""
        return resolve_mirael_ending(
            autonomy=mirael_autonomy,
            responsibility=alex_responsibility,
            closeness=mirael_closeness,
        )

    def mirael_ending_explanation():
        """Give development tools a readable explanation of the endpoint."""
        return ending_report(
            autonomy=mirael_autonomy,
            responsibility=alex_responsibility,
            closeness=mirael_closeness,
        )

    def mirael_human_ending_is_unlocked():
        """Compatibility wrapper used by older labels and tools."""
        return mirael_ending_state() == ENDING_HUMAN
