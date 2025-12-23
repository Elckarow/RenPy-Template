define config.history_length = 250

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

screen history():
    tag menu

    predict False

    use game_menu(_("History")):
        style_prefix "history"

        if not _history_list:
            label _("The dialogue history is empty.")
        
        else:
            use game_menu_viewport(yinitial=1.0):
                vbox:
                    for h in _history_list:
                        hbox spacing 22:
                            label h.who or "":
                                style "history_name"
                                substitute False

                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                            text renpy.filter_text_tags(h.what, allow=gui.history_allow_tags):
                                substitute False
                                yoffset 3

style history_vbox is empty:
    spacing 50

style history_vbox variant "small":
    spacing 160

style history_name is label:
    xsize 233

style history_name_text is label_text:
    xalign 1.0 textalign 1.0

style history_text is text

style history_label is label:
    xalign 0.5

style history_label_text is label_text