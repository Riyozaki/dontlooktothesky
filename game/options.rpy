# Базовая конфигурация проекта. Значения UI временные.

define config.name = _("Don't Look to the Sky")
define config.version = "0.1.0-dev"

define build.name = "dontlooktothesky"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve

define config.main_menu_music = None

define config.save_directory = "dontlooktothesky-dev"

define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

default preferences.text_cps = 35
default preferences.afm_time = 15

define config.developer = True

define build.classify("**~", None)
define build.classify("**.bak", None)
define build.classify("**/.**", None)
define build.classify("game/**.rpy", "archive")
define build.classify("game/**.rpyc", "archive")
