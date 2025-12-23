screen confirm(message, yes_action, no_action=None):
    modal True zorder 200
    style_prefix "confirm"

    add "assets/ui/overlay/confirm.png"

    frame:
        vbox spacing 50:
            label message

            hbox xalign 0.5 spacing 160:
                if no_action is not None:
                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action
                
                else:
                    textbutton _("Ok") action yes_action

    key "game_menu" action no_action

define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

style confirm_frame is empty:
    background Frame(["assets/ui/confirm_frame.png", "assets/ui/frame.png"], gui.confirm_frame_borders)
    padding gui.confirm_frame_borders.padding
    align (0.5, 0.5)

style confirm_label is label:
    xalign 0.5

style confirm_label_text is label_text:
    textalign 0.5
    layout "subtitle"
    color "#fff"
    size 33

style confirm_button is button
style confirm_button_text is button_text