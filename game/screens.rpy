################################################################################
## Экраны вертикального среза
################################################################################

# Базовые звуки интерфейса используются на кнопках выбора и навигации.
style button:
    hover_sound "audio/sfx/ui_select.ogg"
    activate_sound "audio/sfx/ui_click.ogg"

style choice_button:
    hover_sound "audio/sfx/ui_select.ogg"
    activate_sound "audio/sfx/ui_confirm.ogg"

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Solid("#10131cdd")
        xfill True
        yalign 1.0
        ysize 300
        padding (170, 48, 170, 42)

        if who is not None:
            text who id "who" xpos 0 ypos -40 color "#ffffff" size 38

        text what id "what" xsize 1580 color "#f2f2f2" size 34

    use quick_menu


screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.55
        spacing 18

        for i in items:
            textbutton i.caption:
                action i.action
                xsize 1320
                padding (38, 22)
                background Solid("#141925ee")
                hover_background Solid("#263149f5")
                text_color "#eeeeee"
                text_hover_color "#ffffff"
                text_size 30


screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            xalign 0.98
            yalign 0.985
            spacing 16

            textbutton _("Назад") action Rollback() text_size 20
            textbutton _("История") action ShowMenu("history") text_size 20
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True) text_size 20
            textbutton _("Авто") action Preference("auto-forward", "toggle") text_size 20
            textbutton _("Сохранить") action ShowMenu("save") text_size 20
            textbutton _("Настройки") action ShowMenu("preferences") text_size 20


define quick_menu = True


screen navigation():
    vbox:
        xpos 120
        yalign 0.55
        spacing 20

        if main_menu:
            textbutton _("Начать") action Start()
        else:
            textbutton _("История") action ShowMenu("history")
            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("Главное меню") action MainMenu()

        textbutton _("Выход") action Quit(confirm=not main_menu)


screen main_menu():
    tag menu

    add Solid("#0b0e15")

    vbox:
        xpos 120
        ypos 120
        spacing 12
        text "DON'T LOOK TO THE SKY" size 62 color "#ffffff"
        text "Рабочий вертикальный срез" size 26 color "#9aa3b5"

    use navigation


screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu

    add Solid("#0b0e15f5")
    text title xpos 120 ypos 80 size 48 color "#ffffff"
    use navigation

    frame:
        xpos 500
        ypos 170
        xsize 1320
        ysize 800
        background Solid("#141925")
        padding (40, 40)
        transclude


screen history():
    tag menu
    predict False

    use game_menu(_("История")):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:
                spacing 24
                for h in _history_list:
                    vbox:
                        spacing 6
                        if h.who:
                            text h.who color "#ffffff" size 28
                        text h.what color "#d8d8d8" size 27


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Страница {}"), auto=_("Авто"), quick=_("Быстрые"))

    use game_menu(title):
        vbox:
            spacing 20

            hbox:
                spacing 18
                textbutton _("Назад") action FilePagePrevious()
                textbutton _("Авто") action FilePage("auto")
                textbutton _("Быстрые") action FilePage("quick")
                textbutton _("Вперёд") action FilePageNext()

            grid 3 2:
                spacing 18

                for i in range(6):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        xsize 380
                        ysize 250
                        background Solid("#20283a")
                        has vbox
                        spacing 8
                        add FileScreenshot(slot) xsize 340 ysize 160
                        text FileTime(slot, format=_("%d.%m.%Y %H:%M"), empty=_("Пусто")) size 22


screen save():
    tag menu
    use file_slots(_("Сохранить"))


screen load():
    tag menu
    use file_slots(_("Загрузить"))


screen preferences():
    tag menu

    use game_menu(_("Настройки")):
        vbox:
            spacing 28

            text _("Скорость текста") size 30
            bar value Preference("text speed") xsize 800

            text _("Автопереход") size 30
            bar value Preference("auto-forward time") xsize 800

            text _("Громкость музыки") size 30
            bar value Preference("music volume") xsize 800

            text _("Громкость звуков") size 30
            bar value Preference("sound volume") xsize 800

            textbutton _("Полный экран") action Preference("display", "toggle")


screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add Solid("#000000aa")

    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#171d2a")
        padding (50, 40)

        vbox:
            spacing 28
            text message xalign 0.5 color "#ffffff" size 30
            hbox:
                xalign 0.5
                spacing 50
                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action


screen route_qte(prompt, first_caption, first_value, second_caption, second_value, timeout=7.0):
    modal True
    zorder 250

    timer timeout action Return("timeout")
    key "K_1" action Return(first_value)
    key "K_2" action Return(second_value)

    add Solid("#070a10dd")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1420
        background Solid("#151b28f5")
        padding (55, 45)

        vbox:
            spacing 24
            text prompt xalign 0.5 text_align 0.5 color "#ffffff" size 34
            text _("Решение нужно принять быстро") xalign 0.5 color "#aeb8ca" size 23

            textbutton first_caption:
                action Return(first_value)
                xfill True
                padding (32, 20)
                background Solid("#202a3cee")
                hover_background Solid("#334564f5")
                text_color "#ffffff"
                text_size 29

            textbutton second_caption:
                action Return(second_value)
                xfill True
                padding (32, 20)
                background Solid("#202a3cee")
                hover_background Solid("#334564f5")
                text_color "#ffffff"
                text_size 29

            text _("1 / 2") xalign 0.5 color "#7f8aa0" size 20
