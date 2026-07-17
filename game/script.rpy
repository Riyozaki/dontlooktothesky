################################################################################
## Точка входа вертикального среза
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
    elif route_selected == "valeria":
        call v01
        call v02
        call v03
        call v04
        call v05
        call v06
        call v07
        call v08

        if valeria_trust >= 3 and alex_responsibility >= 3:
            call e03
        else:
            call e04
    elif route_selected == "neutral":
        call n01
        call n02
        call n03
    else:
        scene black
        with fade
        centered "Выбранный маршрут пока находится в разработке"

    scene black
    stop music fadeout 1.0
    with fade
    if route_selected == "mirael":
        centered "Конец маршрута Мираэль"
    elif route_selected == "valeria":
        centered "Конец маршрута Валерии"
    elif route_selected == "neutral":
        centered "Конец текущего блока Нейтрального маршрута (N03)"
    else:
        centered "Конец текущего вертикального среза"
    return
