screen preferences():
    tag menu

    use game_menu(_("Preferences")):
        use game_menu_viewport():
            vbox:
                hbox box_wrap True style "pref_hbox":
                    if renpy.variant("pc") or renpy.variant("web"):
                        vbox style_prefix "radio":
                            label _("Display")

                            textbutton _("Window")     action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")

                    vbox style_prefix "check":
                        label _("Skip")

                        textbutton _("Unseen Text")   action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions")   action InvertSelected(Preference("transitions", "toggle"))

                null height 60

                hbox style_prefix "slider" box_wrap True:
                    vbox:
                        label _("Text Speed")
                        bar value Preference("text speed")

                        label _("Auto-Forward Time")
                        bar value Preference("auto-forward time")

                    vbox:
                        if config.has_music:
                            label _("Music Volume")
                            bar value Preference("music volume")

                        if config.has_sound:
                            label _("Sound Volume")
                            bar value Preference("sound volume")

                        if config.has_voice:
                            label _("Voice Volume")
                            bar value Preference("voice volume")

                        if config.has_music or config.has_sound or config.has_voice:
                            null height 15

                            textbutton _("Mute All") action Preference("all mute", "toggle"):
                                style "mute_all_button"

style pref_hbox is empty:
    spacing 150

style pref_hbox variant "small":
    spacing 300

style pref_vbox is empty:
    spacing 0

style pref_vbox variant "small":
    spacing 15

style pref_label is label:
    top_margin 15 bottom_margin 3

style pref_label_text is label_text:
    yalign 1.0
    color gui.text_accent_color

define gui.radio_button_borders = Borders(27, 6, 6, 6)

style radio_hbox is pref_hbox
style radio_vbox is pref_vbox
style radio_label is pref_label
style radio_label_text is pref_label_text

style radio_button is button:
    foreground "assets/ui/button/radio_[prefix_]foreground.png"
    padding gui.radio_button_borders.padding

style radio_button variant "small":
    foreground "assets/ui/phone/button/radio_[prefix_]foreground.png"

style radio_button_text is button_text

define gui.check_button_borders = gui.radio_button_borders

style check_hbox is pref_hbox
style check_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text

style check_button is button:
    foreground "assets/ui/button/check_[prefix_]foreground.png"
    padding gui.check_button_borders.padding

style check_button variant "small":
    foreground "assets/ui/phone/button/check_[prefix_]foreground.png"

style check_button_text is button_text

style slider_hbox is pref_hbox

style slider_vbox is pref_vbox:
    xsize 525
    spacing 0

style slider_vbox variant "small":
    xsize 900

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_button is button
style slider_button_text is button_text
style slider_slider is slider

style mute_all_button is check_button
style mute_all_button_text is check_button_text