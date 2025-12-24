define gui.main_menu_background = "assets/ui/main_menu.png"

screen main_menu():
    tag menu

    add gui.main_menu_background

    if renpy.variant("small"):
        add "assets/ui/phone/overlay/main_menu.png"
    else:
        add "assets/ui/overlay/main_menu.png"

    use navigation()

    vbox:
        xalign 1.0 yalign 1.0
        xoffset -30 yoffset -30
        xmaximum 1200

        text "[config.name!t]":
            style "main_menu_title"

        text "[config.version]":
            style "main_menu_version"

style main_menu_version is text:
    xalign 1.0
    color gui.text_accent_color

style main_menu_title is main_menu_version:
    size 75