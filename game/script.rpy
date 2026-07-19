################################################################################
## Точка входа текущей рабочей сборки
################################################################################

label start:
    $ quick_menu = True

    call c00
    call c01
    call c02
    call c03
    call c04
    call c05
    call c06
    call c07
    call c08
    call c09

    if route_selected == "mirael":
        call m01
        call m02
        call m03
        call m04
        call m05
        call m06
        call m07

        scene black
        stop music fadeout 1.0
        with fade
        centered "Конец маршрута Мираэль"

    elif route_selected == "valeria":
        call v01
        call v02
        call v03
        call v04
        call v05

        scene black
        stop music fadeout 1.0
        with fade
        centered "Конец текущего блока маршрута Валерии (V05)"

    elif route_selected == "neutral":
        scene black
        stop music fadeout 1.0
        with fade
        centered "Нейтральный маршрут будет спроектирован после маршрута Валерии"

    elif route_selected == "true":
        scene black
        stop music fadeout 1.0
        with fade
        centered "Истинный маршрут пока не спроектирован"

    else:
        scene black
        stop music fadeout 1.0
        with fade
        centered "Маршрут не выбран"

    return
