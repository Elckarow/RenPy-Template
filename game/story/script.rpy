define test_character = Character("Test")

label start:
    scene expression "#fdfdfd"
    test_character "test menu"

    menu:
        "test caption"

        "a":
            "a"
        
        "b":
            "b"
    
    "end"

    return
