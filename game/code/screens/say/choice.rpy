screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is empty:
    xalign 0.5
    ypos 405 yanchor 0.5
    spacing 33

define gui.choice_button_borders = Borders(150, 8, 150, 8)

style choice_button is button:
    xsize 1185
    background Frame("assets/ui/button/choice_[prefix_]background.png", gui.choice_button_borders)
    padding gui.choice_button_borders.padding

style choice_button variant "small":
    xsize 1860

style choice_button_text is button_text:
    xalign 0.5
    hover_color "#fff"

style choice_button_text variant "small":
    size 45