define gui.game_menu_background = "assets/ui/game_menu.png"

screen game_menu(title):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        transclude

    use navigation(True)

    label title style "game_menu_title"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen game_menu_viewport(**properties):
    viewport style "empty" properties properties:
        mousewheel True draggable True
        scrollbars "vertical" side_yfill True

        transclude

style game_menu_frame is empty:
    padding (60 + gui.navigation_width, 180 + 15 + 10, 0 + 30, 45)
    background "assets/ui/overlay/game_menu.png"

style game_menu_frame variant "small":
    background "assets/ui/phone/overlay/game_menu.png"

style game_menu_title is label:
    xpos 79 ypos 48

style game_menu_title_text is label_text:
    size 75
    color "#0099cc"
    yalign 0.5