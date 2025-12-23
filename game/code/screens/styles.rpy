init offset = -9

define config.check_conflicting_properties = True

init python:
    def hyperlink_functions_style(name):
        """
        Hyperlink functions but the style `name` is used.
        """
        style_object = getattr(style, name)
        return (lambda target: style_object,) + style.default.hyperlink_functions[1:]

style text is empty:
    hyperlink_functions hyperlink_functions_style("hyperlink_text")
    color "#fff"
    language "unicode"
    font "DejaVuSans.ttf"
    size 33

style text variant "small":
    size 45

style hyperlink_text is text:
    hover_underline True

style input is text:
    adjust_spacing False
    color "#0099cc"

style button is empty:
    hover_sound    None
    activate_sound None

style button_text is text:
    yalign 0.5

    idle_color "#888888"
    hover_color "#66c1e0"
    selected_idle_color "#ffffff"
    selected_hover_color "#66c1e0"
    insensitive_color "#8888887f"

style button_text variant "small":
    size 45

define gui.frame_borders = Borders(6, 6, 6, 6)

style frame is empty:
    padding gui.frame_borders.padding
    background Frame("assets/ui/frame.png", gui.frame_borders)

style window is empty
    
style label is empty
style label_text is text:
    yalign 0.5
    size 36
    color "#0099cc"

style label_text variant "small":
    size 51

define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = gui.bar_borders
define gui.scrollbar_borders = gui.bar_borders
define gui.vscrollbar_borders = gui.bar_borders
define gui.slider_borders = gui.bar_borders
define gui.vslider_borders = gui.bar_borders

style bar is empty:
    ysize 38
    left_bar Frame("assets/ui/bar/left.png", gui.bar_borders)
    right_bar Frame("assets/ui/bar/right.png", gui.bar_borders)
    unscrollable "hide"

style bar variant "small":
    left_bar Frame("assets/ui/phone/bar/left.png", gui.bar_borders)
    right_bar Frame("assets/ui/phone/bar/right.png", gui.bar_borders)

style vbar is empty:
    xsize 38
    top_bar Frame("assets/ui/bar/top.png", gui.vbar_borders)
    bottom_bar Frame("assets/ui/bar/bottom.png", gui.vbar_borders)
    unscrollable "hide"

style vbar variant "small":
    top_bar Frame("assets/ui/phone/bar/top.png", gui.bar_borders)
    bottom_bar Frame("assets/ui/phone/bar/bottom.png", gui.bar_borders)

style scrollbar is empty:
    ysize 18
    base_bar Frame("assets/ui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders)
    thumb Frame("assets/ui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders)
    unscrollable "hide"

style scrollbar variant "small":
    base_bar Frame("assets/ui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders)
    thumb Frame("assets/ui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders)

style vscrollbar is empty:
    xsize 18
    base_bar Frame("assets/ui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders)
    thumb Frame("assets/ui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders)
    unscrollable "hide"

style vscrollbar variant "small":
    base_bar Frame("assets/ui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders)
    thumb Frame("assets/ui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders)

style slider is empty:
    ysize 38
    base_bar Frame("assets/ui/slider/horizontal_[prefix_]bar.png", gui.slider_borders)
    thumb "assets/ui/slider/horizontal_[prefix_]thumb.png"
    unscrollable "hide"

style slider variant "small":
    ysize 54
    base_bar Frame("assets/ui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders)
    thumb "assets/ui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider is empty:
    xsize 38
    base_bar Frame("assets/ui/slider/vertical_[prefix_]bar.png", gui.vslider_borders)
    thumb "assets/ui/slider/vertical_[prefix_]thumb.png"
    unscrollable "hide"

style vslider variant "small":
    xsize 54
    base_bar Frame("assets/ui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders)
    thumb "assets/ui/phone/slider/vertical_[prefix_]thumb.png"

style fixed is empty
style vbox  is empty
style hbox  is empty
style grid  is empty
style side  is empty

style vpgrid   is empty
style viewport is empty