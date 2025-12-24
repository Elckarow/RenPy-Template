## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."

## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

init python:
    build.name = "TEMPLATE"

    build.archive("assets")
    build.classify("game/assets/*", "assets all")

    build.archive("scripts")
    build.classify("game/code/*", "scripts all")
    build.classify("**.rpy", None)
    build.classify("**.rpyc", "scripts all")

    build.classify("game/cache/*.*", None)
    build.classify("game/saves/**", None)
    build.classify("**.md", None)
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**.DS_Store", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.psd", None)
    build.classify("**.sublime-project", None)
    build.classify("**.sublime-workspace", None)
    build.classify("script-regex.txt", None)

    build.include_old_themes = False

    build.documentation('*.html')
    build.documentation('*.txt')