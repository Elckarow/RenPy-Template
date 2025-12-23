screen notify(message):
    zorder 100 style_prefix "notify"

    frame:
        at transform:
            on show:
                alpha 0.0
                linear 0.25 alpha 1.0
            on hide:
                linear 0.5 alpha 0.0

        text "[message!tq]"

    timer 3.25 action Hide("notify")

define gui.notify_frame_borders = Borders(24, 8, 80, 8)

style notify_frame is empty:
    ypos 68
    background Frame("assets/ui/notify.png", gui.notify_frame_borders)
    padding gui.notify_frame_borders.padding

style notify_text is text:
    size 24

style notify_text variant "small":
    size 38