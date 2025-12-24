init -500 python:
    config.character_id_prefixes.append("namebox")

define gui.dialogue_ypos = 75

screen say(who, what):
    window id "window":
        fixed:
            if who is not None:
                window id "namebox" style "say_namebox":
                    text who id "who"

            text what id "what" ypos gui.dialogue_ypos

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style say_window is empty:
    background Transform("assets/ui/textbox.png", xysize=(1.0, 1.0), subpixel=True)
    xsize 1.0 ysize 278
    xpadding 402
    yanchor 1.0 ypos 1.0

style say_window variant "small":
    left_padding 135
    ysize 360
    background Transform("assets/ui/phone/textbox.png", xysize=(1.0, 1.0), subpixel=True)

style say_namebox is empty:
    xoffset -35 yoffset 5

style say_namebox variant "small":
    xoffset -10

style say_label is text:
    size 45
    color gui.text_accent_color

style say_label variant "small":
    size 54

style say_dialogue is text:
    adjust_spacing False

style say_thought is say_dialogue