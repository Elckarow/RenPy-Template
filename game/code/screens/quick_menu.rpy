init -500 python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

screen quick_menu():
    zorder 100
    style_prefix "quick_menu"

    if quick_menu:
        hbox:
        if config.rollback_enabled:
                textbutton _("Back") action Rollback()

            if not renpy.variant("touch"):
                textbutton _("History") action ShowMenu("history")

            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")

            if not renpy.variant("touch"):
                textbutton _("Save") action ShowMenu("save")
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
                textbutton _("Prefs") action ShowMenu("preferences")
            
            if renpy.variant("touch"):
                 textbutton _("Menu") action ShowMenu("history")

style quick_menu_hbox is empty:
    align (0.5, 1.0)

define gui.quick_button_borders = (
    Borders(60, 21, 60, 0)
    if renpy.variant("touch")
    else Borders(15, 6, 15, 0)
)

style quick_menu_button is button:
    padding gui.quick_button_borders.padding

style quick_menu_button_text is button_text:
    size 21
    idle_color "#aaaaaa"
    selected_color gui.text_accent_color

style quick_menu_button_text variant "small":
    size 30