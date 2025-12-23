define gui.navigation_width = (510 if renpy.variant("small") else 420)

screen navigation(return_button=False):
    style_prefix "navigation"

    frame style "empty":
        left_padding 65 xsize gui.navigation_width ysize 1.0

        vbox:
            if main_menu:
                textbutton _("Start") action Start()

            else:
                textbutton _("History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:
                textbutton _("Main Menu") action MainMenu()

            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=not main_menu)
        
        if return_button:
            textbutton _("Return") action Return() yalign 1.0 offset (5, -50)

style navigation_button is button
style navigation_button_text is button_text

style navigation_vbox is empty:
    yalign 0.5 spacing 18

style navigation_vbox variant "small":
    spacing 50