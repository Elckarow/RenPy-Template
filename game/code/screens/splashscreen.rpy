label splashscreen():
    scene expression "#000"

    scene expression "#fdfdfd" with Dissolve(1.0)
    pause 1.0
    scene expression "#000" with Dissolve(0.5)

    return