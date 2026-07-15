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
image bg town square = "../images/backgrounds/bg_town_square.png"
image bg client corridor = "../images/backgrounds/bg_client_building_corridor.png"
image bg private sector day = "../images/backgrounds/bg_private_sector_day.png"
image bg rain street = "../images/backgrounds/bg_rain_street.png"
image bg bus stop rain = "../images/backgrounds/bg_bus_stop_rain_evening.png"
image bg pharmacy rain = "../images/backgrounds/bg_small_pharmacy_exterior_rain.png"
image bg valeria office = "../images/backgrounds/bg_valeria_office_night_clean.png"

# Спрайты первой главы
image alex neutral = "../images/characters/aleksandr/alexandr_neutral.png"
image alex shocked = "../images/characters/aleksandr/alexandr_shocked.png"
image lena neutral = "../images/characters/lena/lena_neutral.png"
image lena snide = "../images/characters/lena/lena_snide.png"
image dmitry neutral = "../images/characters/dmitry/dmitry_neutral.png"
image dmitry serious = "../images/characters/dmitry/dmitry_serious.png"
image mirael neutral = "../images/characters/mirael/mirael_neutral.png"
image mirael shocked = "../images/characters/mirael/mirael_shocked_terrified.png"
image mirael sad = "../images/characters/mirael/mirael_sad.png"
image artem happy = "../images/characters/artem/artem_shank_happy.png"
image artem empty = "../images/characters/artem/artem_shank_empty.png"
image valeria serious = "../images/characters/valeria/valeria_serious.png"
image valeria neutral = "../images/characters/valeria/valeria_neutral.png"
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

    persistent.ending_mirael_human = getattr(persistent, "ending_mirael_human", False)
    persistent.ending_mirael_guardian = getattr(persistent, "ending_mirael_guardian", False)
    persistent.ending_valeria_contract = getattr(persistent, "ending_valeria_contract", False)
    persistent.ending_valeria_free = getattr(persistent, "ending_valeria_free", False)
    persistent.ending_neutral_truth = getattr(persistent, "ending_neutral_truth", False)
    persistent.true_ending_complete = getattr(persistent, "true_ending_complete", False)

    def observer_memory_count():
        endings = (
            persistent.ending_mirael_human,
            persistent.ending_mirael_guardian,
            persistent.ending_valeria_contract,
            persistent.ending_valeria_free,
            persistent.ending_neutral_truth,
        )
        return sum(bool(value) for value in endings)

    def true_route_is_unlocked():
        return observer_memory_count() == 5

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
