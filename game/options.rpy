init -10 python:
    gui.init(1920, 1080)

define config.name = _("TEMPLATE")

define config.version = "1.0"

# define config.main_menu_music = "main-menu-theme.ogg"

define config.enter_transition = dissolve
define config.exit_transition  = dissolve
define config.intra_transition = dissolve

define config.after_load_transition = None

define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

define config.save_directory = "TEMPLATE-1766327398"

define config.window_icon = "assets/ui/window_icon.png"

init 500 python hide:
    def add_detached_layer(layer):
        config.detached_layers.append(layer)
        config.layer_clipping[layer] = (0, 0, config.screen_width, config.screen_height)
    
    # add_detached_layer("detached_layer_1")

## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."

## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

init python:
    build.name = "TEMPLATE"

    build.archive("assets")
    build.classify("game/assets/*", "assets all")

    build.archive("scripts")
    build.classify("game/code/*", "scripts all")
    build.classify("**.rpy", None)
    build.classify("**.rpyc", "scripts all")

    build.classify("game/cache/*.*", None)
    build.classify("game/saves/**", None)
    build.classify("**.md", None)
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**.DS_Store", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.psd", None)
    build.classify("**.sublime-project", None)
    build.classify("**.sublime-workspace", None)
    build.classify("script-regex.txt", None)

    build.include_old_themes = False

    build.documentation('*.html')
    build.documentation('*.txt')

#####################
# Config variables you (probably) don't need to change

define config.narrator_menu = True
define config.linear_fades = True
define config.developer = "auto"
define config.autoreload = False
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.allow_skipping = True
define config.gl2 = True
define config.gl_test_image = "white"
define config.skip_indicator = False
define config.early_start_store = False

init 500 python hide:
    config.window_auto_hide.remove("menu")
    
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    _preferences.pad_enabled = False

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    config.adjust_view_size = force_integer_multiplier

    config.start_callbacks.append(lambda: renpy.run(Preference("auto-forward", "disable")))
    config.start_callbacks.append(lambda: renpy.run(FilePage(1)))

    if config.developer:
        config.start_callbacks.append(lambda: renpy.run(Preference("rollback side", "left")))

# for testing mobile ui
# init -500 python:
#     config.variants.extend(("small", "touch"))