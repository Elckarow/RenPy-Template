screen skip_indicator():
    zorder 100
    style_prefix "notify"

    frame yoffset -50:
        hbox spacing 9:
            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0)
            text "▸" at delayed_blink(0.2, 1.0)
            text "▸" at delayed_blink(0.4, 1.0)

transform delayed_blink(delay, cycle):
    alpha 0.5

    pause delay

    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.4)
        repeat