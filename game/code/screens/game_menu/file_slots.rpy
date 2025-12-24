screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

define gui.file_slot_cols = (2 if renpy.variant("small") else 3)
define gui.file_slot_rows = 2

define config.thumbnail_width = 384
define config.thumbnail_height = 216

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            vbox align (0.5, 1.0):
                style_prefix "page"

                hbox xalign 0.5:
                    textbutton _("<") action FilePagePrevious() keysym "save_page_prev"

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton str(page) action FilePage(page)

                    textbutton _(">") action FilePageNext() keysym "save_page_next"

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        vbox:
                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)
            
            button style "page_label":
                action page_name_value.Toggle() selected False

                input style "page_label_text":
                    value page_name_value

style page_button is button:
    padding (15, 6, 15, 6)

style page_button_text is button_text

style slot_button is button:
    xsize 414 ysize 309
    padding (15, 15, 15, 15)
    background "assets/ui/button/slot_[prefix_]background.png"

style slot_button_text is button_text:
    size 21 xalign 0.5

style slot_grid is empty:
    align (0.5, 0.5)
    spacing 15

style slot_time_text is button_text:
    xalign 0.5 textalign 0.5
    size 21
style slot_name_text is slot_time_text

style page_label is button:
    xpadding 75 ypadding 5
    xalign 0.5

style page_label_text is button_text:
    textalign 0.5 layout "subtitle"
    size 40
    idle_color gui.text_accent_color
    insensitive_color gui.text_accent_color