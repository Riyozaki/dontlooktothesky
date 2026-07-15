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
    else:
        scene black
        with fade
        centered "Выбранный маршрут пока находится в разработке"

    scene black
    stop music fadeout 1.0
    with fade
    centered "Конец текущего вертикального среза"
    return
