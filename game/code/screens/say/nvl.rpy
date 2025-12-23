define config.nvl_list_length = (4 if renpy.variant("small") else 6)

screen nvl(dialogue, items=None):
    window style "nvl_window":
        vbox style "nvl_vbox":
            use nvl_what(dialogue)

            if items is not None:
                use nvl_items(items)

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_what(dialogue):
    for d in dialogue:
        window id d.window_id:
            hbox style "nvl_hbox":
                if d.who is not None:
                    frame style "nvl_label_frame":
                        text d.who id d.who_id

                text d.what id d.what_id

screen nvl_items(items):
    for i in items:
        hbox style "nvl_hbox":
            frame style "nvl_label_frame":
                text "" style "nvl_label"

            textbutton i.caption style "nvl_button":
                action i.action

style nvl_vbox is empty:
    spacing 120

style nvl_vbox variant "small":
    spacing 200

style nvl_hbox is empty:
    spacing 30

style nvl_window:
    xysize (1.0, 1.0)
    background "assets/ui/nvl.png"
    padding (420, 15, 420, 30)

style nvl_window variant "small":
    background "assets/ui/phone/nvl.png"
    xpadding 200

style nvl_entry is empty

style nvl_label_frame is empty:
    xsize 225

style nvl_label is say_label:
    textalign 1.0 xalign 1.0

style nvl_label variant "small":
    xsize 458

style nvl_dialogue is say_dialogue:
    yoffset 10

style nvl_thought is nvl_dialogue

style nvl_button is button
style nvl_button_text is button_text