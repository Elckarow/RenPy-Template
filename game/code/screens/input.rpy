screen input(prompt):
    window style "say_window":
        vbox ypos gui.dialogue_ypos:
            text prompt style "input_prompt"
            input id "input"

style input_prompt is say_dialogue