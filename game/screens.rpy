################################################################################
## Initialization
################################################################################

init offset = -1

init:
    image pluto_title_40:
        "gui/pluto.png"
        zoom 0.40
    image pluto_title_58:
        "gui/pluto.png"
        zoom 0.58

    image button_play:
        "gui/button_play.png"
        zoom 0.5
    image button_license:
        "gui/button_license.png"
        zoom 0.5
    image button_setting:
        "gui/button_setting.png"
        zoom 0.5
    image button_exit:
        "gui/button_exit.png"
        zoom 0.5

    image button_play_hover:
        "gui/button_play_hover.png"
        zoom 0.5
    image button_license_hover:
        "gui/button_license_hover.png"
        zoom 0.5
    image button_setting_hover:
        "gui/button_setting_hover.png"
        zoom 0.5
    image button_exit_hover:
        "gui/button_exit_hover.png"
        zoom 0.5

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=False)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" antialias True

        text what id "what" layout "greedy"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    # if not renpy.variant("small"):
    #     add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')
    _game_menu_screen = "preferences"


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action top_padding 7

screen choice(items):
    style_prefix "choice"
    variant "touch"

    vbox:
        for i in items:
            textbutton i.caption action i.action top_padding 22


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 623
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("뒤로") action Rollback()
            textbutton _("대화기록") action ShowMenu('history')
            # textbutton _("스킵") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("자동저장") action Preference("auto-forward", "toggle")
            # textbutton _("저장하기") action ShowMenu('save')
            # textbutton _("퀵세이브") action QuickSave()
            # textbutton _("퀵로드") action QuickLoad()
            textbutton _("설정") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    #import urllib, json
    config.overlay_screens.append("quick_menu")
    # def getLastCommit():
    #     url = "https://api.github.com/repos/Neibce/Pluto-Update/commits"
    #     response = urllib.urlopen(url)
    #     data = json.loads(response.read())
    #     return data[0]["sha"][0:7]
    # def checkUpdate():
    #     ver = updater.UpdateVersion("https://cdn.rawgit.com/Neibce/Pluto-Update/"+getLastCommit()+"/updates.json", check_interval=21600)
    #     if ver == None:
    #         return None
    #     else:
    #         return ver
    def show_achevement():
        renpy.vibrate(1101)

    def show_leaderboard():
        renpy.vibrate(1102)

    ee_click_num = 0
    ns_click_num = 1

    def easter_egg():
        global ee_click_num, ns_click_num
        ee_click_num = ee_click_num + 1
        if ee_click_num >= 5:
            ee_click_num = 0
            renpy.transition(dissolve)
            ns_click_num = 1
            renpy.music.set_pause(True);
            renpy.show_screen("easter_egg_screen")

    def next_slide_image():
        global ns_click_num
        if ns_click_num >= 9:
            renpy.transition(dissolve)
            renpy.hide_screen("easter_egg_screen")
            renpy.music.set_pause(False);
            return
        ns_click_num = ns_click_num + 1

    def get_slide_image(st, at):
        global ns_click_num
        return "gui/s/s"+str(ns_click_num)+".png", None

image easter_slide = DynamicDisplayable(get_slide_image)

screen easter_egg_screen():
    imagebutton idle "easter_slide" xalign 0.5 action Function(next_slide_image)

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen change_language():
    modal True
    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("change_language", Dissolve(.3))
    frame:
        xpadding 20
        ypadding 15
        xalign 0.5
        yalign 0.5
        style_prefix "pref"
        has vbox

        label ("Language") text_size 35
        null height 15

        style_prefix "radio"
        textbutton "English":
            action Notify("  Will be updated soon !!  ")
            #[Language("english"), Hide("change_language", Dissolve(.3))]
        textbutton "Korean":
            action [Language(None), Hide("change_language", Dissolve(.3))]
        textbutton "Japanese":
            action Notify("  Will be updated soon !!  ")
            #[Language("japanese"), Hide("change_language", Dissolve(.3))]

        textbutton ("Close") xalign 1.0 action Hide("change_language", Dissolve(.3))


screen esc_menu():
    modal True
    zorder 50

    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("esc_menu", Dissolve(.3))
    frame:
        xpadding 25
        ypadding 20
        xalign 0.5
        yalign 0.5
        style_prefix "pref"
        has vbox

        null height 17

        add Image("gui/pluto.png") zoom 0.33 xalign 0.55

        vbox:
            xpos 0.5
            xalign 0.5
            yalign 0.55

            null height 40

            textbutton _("대화기록") xalign 0.5 text_size 22 action [Hide("esc_menu"), Show("history", Dissolve(.3))]
            null height 7
            textbutton _("환경설정") xalign 0.5 text_size 22 action [Hide("esc_menu"), Show("preferences", Dissolve(.3))]
            null height 7
            textbutton _("메인메뉴") xalign 0.5 text_size 22 action MainMenu()
            null height 7
            #if renpy.variant("pc"):
                ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("끝내기") xalign 0.5 text_size 22 action Quit(confirm=not main_menu)

screen esc_menu():
    variant "touch"

    modal True
    zorder 50

    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("esc_menu", Dissolve(.3))
    frame:
        xpadding 35
        ypadding 20
        xalign 0.5
        yalign 0.5
        style_prefix "pref"
        has vbox

        null height 17

        add Image("gui/pluto.png") zoom 0.4 xalign 0.55

        vbox:
            xpos 0.5
            xalign 0.5
            yalign 0.55

            null height 40

            textbutton _("대화기록") xalign 0.5 text_size 30 action Show("history", Dissolve(.3))
            null height 7
            textbutton _("환경설정") xalign 0.5 text_size 30 action Show("preferences", Dissolve(.3))
            null height 7
            textbutton _("메인메뉴") xalign 0.5 text_size 30 action MainMenu()
            null height 7
            #if renpy.variant("pc"):
                ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("끝내기") xalign 0.5 text_size 30 action Quit(confirm=not main_menu)


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background
    add Color((0, 0, 0, 100))

    imagebutton idle "pluto_title_58" xalign 0.5 yalign 0.13 action Function(easter_egg)

    ## This empty frame darkens the main menu.
    frame:
        pass

    hbox:
        xpos 0.012
        ypos 0.855

        imagebutton idle "gui/achievement.png" action Function(show_achevement)
        imagebutton idle "gui/leaderboard.png" xpos -0.1 action Function(show_leaderboard)

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    vbox:
        xpos 0.517
        xalign 0.5
        yalign 1.068

        imagebutton idle "button_play" hover "button_play_hover" action Start()
        imagebutton idle "button_setting" hover "button_setting_hover" ypos -0.3 action ShowMenu("preferences")
        imagebutton idle "button_license" hover "button_license_hover" ypos -0.6 action ShowMenu("about")
        imagebutton idle "button_exit" hover "button_exit_hover" ypos -0.9 action Quit(confirm=not main_menu)

    if gui.show_name:
        vbox xalign 1.0 yalign 1.0:
            text "ver [config.version]" color '#ffffff' size 17
            text "Team Coding Dongcheon 2018." color '#ffffff' size 17
        
screen main_menu():
    variant "touch"

    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background
    add Color((0, 0, 0, 100))
    imagebutton idle "pluto_title_58" xalign 0.5 yalign 0.13 action Function(easter_egg)

    ## This empty frame darkens the main menu.
    frame:
        pass

    hbox:
        xpos 0.012
        ypos 0.855

        imagebutton idle "gui/achievement.png" action Function(show_achevement)
        imagebutton idle "gui/leaderboard.png" xpos -0.1 action Function(show_leaderboard)

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    vbox:
        xpos 0.517
        xalign 0.5
        yalign 1.068

        imagebutton idle "button_play" hover "button_play_hover" action Start()
        imagebutton idle "button_setting" hover "button_setting_hover" ypos -0.3 action ShowMenu("preferences")
        imagebutton idle "button_license" hover "button_license_hover" ypos -0.6 action ShowMenu("about")
        imagebutton idle "button_exit" hover "button_exit_hover" ypos -0.9 action Quit(confirm=not main_menu)

    if gui.show_name:
        vbox xalign 1.0 yalign 1.0:
            text "ver [config.version]" color '#ffffff' size 23
            text "Team Coding Dongcheon 2018." color '#ffffff' size 23

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_button is gui_medium_button

style main_menu_frame:
    xsize 280
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    textbutton _("돌아가기"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    zorder 100
    modal True

    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("about", Dissolve(.3))


    frame:
        xpadding 25
        ypadding 18
        xalign 0.5
        yalign 0.5
        style_prefix "pref"
        has vbox

        hbox:
            box_wrap True
            

            vbox:
                xsize 450

                label _("라이센스") text_size 40
                null height 10

                label "[config.name!t]"
                text ("Version [config.version!t]\nTeam Coding Dongcheon 2018.\n")

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n" 

                label "Ren'Py"
                text ("{a=https://www.renpy.org}https://www.renpy.org{/a}\n\n[renpy.license!t]")

        null height 10
        textbutton _("닫기") xalign 1.0 action Hide("about", Dissolve(.3))

screen about():
    variant "touch"
    zorder 100
    modal True

    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("about", Dissolve(.3))


    frame:
        xpadding 25
        ypadding 18
        xalign 0.5
        yalign 0.5
        style_prefix "pref"
        has vbox

        hbox:
            box_wrap True
            

            vbox:
                xsize 500

                label _("라이센스") text_size 40
                null height 10

                label "[config.name!t]" text_size 35
                text ("Version [config.version!t]\nTeam Coding Dongcheon 2018.\n") size 25

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n" 

                label "Ren'Py" text_size 35
                text ("{a=https://www.renpy.org}https://www.renpy.org{/a}\n\n[renpy.license!t]") size 25

        null height 10
        textbutton _("닫기") xalign 1.0 action Hide("about", Dissolve(.3))


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

# screen save():

#     tag menu

#     use file_slots(_("저장하기"))


# screen load():

#     tag menu

#     use file_slots(_("불러오기"))


# screen file_slots(title):

#     default page_name_value = FilePageNameInputValue(pattern=_("{} 페이지"), auto=_("자동저장"), quick=_("퀵세이브"))

#     use game_menu(title):

#         fixed:

#             ## This ensures the input will get the enter event before any of the
#             ## buttons do.
#             order_reverse True

#             ## The page name, which can be edited by clicking on a button.
#             button:
#                 style "page_label"

#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()

#                 input:
#                     style "page_label_text"
#                     value page_name_value

#             ## The grid of file slots.
#             grid gui.file_slot_cols gui.file_slot_rows:
#                 style_prefix "slot"

#                 xalign 0.5
#                 yalign 0.5

#                 spacing gui.slot_spacing

#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):

#                     $ slot = i + 1

#                     button:
#                         action FileAction(slot)

#                         has vbox

#                         add FileScreenshot(slot) xalign 0.5

#                         text FileTime(slot, format=_("{#file_time}%Y년 %B %d일, %H:%M"), empty=_("빈 슬롯")):
#                             style "slot_time_text"
#                             color "#666"

#                         text FileSaveName(slot):
#                             style "slot_name_text"

#                         key "save_delete" action FileDelete(slot)

#             ## Buttons to access other pages.
#             hbox:
#                 style_prefix "page"

#                 xalign 0.5
#                 yalign 1.0

#                 spacing gui.page_spacing

#                 textbutton ("<") action FilePagePrevious()

#                 if config.has_autosave:
#                     textbutton ("{#auto_page}A") action FilePage("auto")

#                 if config.has_quicksave:
#                     textbutton ("{#quick_page}Q") action FilePage("quick")

#                 ## range(1, 10) gives the numbers from 1 to 9.
#                 for page in range(1, 4):
#                     textbutton "[page]" action FilePage(page)

#                 textbutton (">") action FilePageNext(max=3)


# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text

# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text

# style page_label:
#     xpadding 50
#     ypadding 3

# style page_label_text:
#     text_align 0.5
#     layout "subtitle"
#     hover_color gui.hover_color

# style page_button:
#     properties gui.button_properties("page_button")

# style page_button_text:
#     properties gui.button_text_properties("page_button")

# style slot_button:
#     properties gui.button_properties("slot_button")

# style slot_button_text:
#     size 15
#     properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    zorder 100
    modal True

    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("preferences", Dissolve(.3))

    #use game_menu(_("환경설정"), scroll="viewport"):

    frame:
        xpadding 25
        ypadding 18
        xalign 0.5
        yalign 0.5
        style_prefix "pref"
        has vbox

        label _("환경설정") text_size 40
        null height 10

        hbox:
            box_wrap True

            if renpy.variant("pc"):
                vbox:
                    style_prefix "radio"
                    label _("화면모드") xalign 0.1
                    textbutton _("창 모드") xalign 0.1 action Preference("display", "window")
                    textbutton _("전체화면 모드") xalign 0.1 action Preference("display", "fullscreen")

                    # vbox:
                    #     style_prefix "check"
                    #     label _("스킵")
                    #     textbutton _("빈 대화창 스킵") action Preference("skip", "toggle")
                    #     textbutton _("선택지 이후 스킵유지") action Preference("after choices", "toggle")
                    #     textbutton _("화면전환 효과 스킵") action InvertSelected(Preference("transitions", "toggle"))

                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                    ## added here, to add additional creator-defined preferences.

                    null height (gui.pref_spacing)

            vbox:
                xpos 0.05

                label ("Language")
                null height 5

                style_prefix "radio"
                textbutton "English":
                    action Notify("  업데이트 예정입니다.  ")
                    #[Language("english"), Hide("change_language", Dissolve(.3))]
                textbutton "Korean":
                    action Language(None)
                textbutton "Japanese":
                    action Notify("  업데이트 예정입니다.  ")
                    #[Language("japanese"), Hide("change_language", Dissolve(.3))]
                null height 5

            vbox:
                style_prefix "slider"

                label _("텍스트 속도")
                bar value Preference("text speed")

                if config.has_music:
                    label _("배경음 크기")

                    bar value Preference("music volume")

                if config.has_sound:

                    label _("효과음 크기")

                    bar value Preference("sound volume")

                if config.has_voice:
                    label _("음성 크기")

                    bar value Preference("voice volume")

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("음소거"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"

        textbutton _("닫기") xalign 1.0 action Hide("preferences", Dissolve(.3))


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    xalign 0.05

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350
    xalign 0.4

style slider_label:
    xalign 0.05

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 380


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    zorder 100
    modal True

    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("history", Dissolve(.3))


    frame:
        xsize 600
        ysize 600
        xpadding 35
        ypadding 22
        xalign 0.5
        yalign 0.5

        has vbox

        label _("대화기록") text_size 40
        null height 17

        vpgrid:
            ysize 448
            yfill True 
            xfill True
            cols 1
            spacing 5
            draggable True
            mousewheel True

            if _history_list.__len__() > 12:
                scrollbars "vertical"
                yinitial 1.0

            vbox:
                spacing 10
                for h in _history_list[_history_list.__len__()-30:_history_list.__len__()]:
                    hbox:
                        if h.who:
                            label h.who+": ":
                                ## Take the color of the who text from the Character, if
                                ## set.
                                if "color" in h.who_args:
                                    text_color "#000" #h.who_args["color"]
                                text_size gui.text_size

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what

                if not _history_list:
                    label _("대화 내용이 없습니다.")
        null height 17
        textbutton _("닫기") xalign 1.0 action Hide("history", Dissolve(.3))
       


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.0

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

# screen help():

#     tag menu

#     default device = "keyboard"

#     use game_menu(_("도움말"), scroll="viewport"):

#         style_prefix "help"

#         vbox:
#             spacing 15

#             hbox:

#                 textbutton _("키보드") action SetScreenVariable("device", "keyboard")
#                 textbutton _("마우스") action SetScreenVariable("device", "mouse")

#             if device == "keyboard":
#                 use keyboard_help
#             elif device == "mouse":
#                 use mouse_help


# screen keyboard_help():

#     hbox:
#         label ("Enter Space")
#         text _("대화 넘기기")

#     hbox:
#         label ("↑ ↓ ← →")
#         text _("인터페이스 탐색")

#     hbox:
#         label ("Esc")
#         text _("메뉴 열기")

#     hbox:
#         label ("Ctrl")
#         text _("누르고 있는 동안 대화 스킵하기")

#     hbox:
#         label ("Tab")
#         text _("대화 스킵 켜기/끄기")

#     hbox:
#         label ("Page Up")
#         text _("이전 대화로")

#     hbox:
#         label ("Page Down")
#         text _("다음 대화로")

#     hbox:
#         label "H"
#         text _("UI 숨기기/보이기")

#     hbox:
#         label "S"
#         text _("스크린샷 찍기")

# screen mouse_help():

#     hbox:
#         label _("좌 클릭")
#         text _("대화 넘기기")

#     hbox:
#         label _("우 클릭")
#         text _("메뉴 열기")

#     hbox:
#         label _("휠 클릭")
#         text _("UI 숨기기/보이기")

#     hbox:
#         label _("휠 올림/내림")
#         text _("이전/다음 대화로")


# style help_button is gui_button
# style help_button_text is gui_button_text
# style help_label is gui_label
# style help_label_text is gui_label_text
# style help_text is gui_text

# style help_button:
#     properties gui.button_properties("help_button")
#     xmargin 8

# style help_button_text:
#     properties gui.button_text_properties("help_button")

# style help_label:
#     xsize 250
#     right_padding 20

# style help_label_text:
#     size gui.text_size
#     xalign 1.0
#     text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    imagebutton:
        idle Color((0, 0, 0, 140))
        clicked Hide("confirm", Dissolve(.3))

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 1.0
                spacing 30

                textbutton _("확인") text_color "#59F" action yes_action
                textbutton _("취소") text_color "#F95" action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_prompt_text:
    variant "touch"
    text_align 0.5
    size 30
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

style confirm_button_text:
    variant "touch"
    properties gui.button_text_properties("confirm_button")
    size 25


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

# screen skip_indicator():

#     zorder 100
#     style_prefix "skip"

#     frame:

#         hbox:
#             spacing 6

#             text _("스킵 중")

#             text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
#             text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
#             text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


# ## This transform is used to blink the arrows one after another.
# transform delayed_blink(delay, cycle):
#     alpha .5

#     pause delay

#     block:
#         linear .2 alpha 1.0
#         pause .2
#         linear .2 alpha 0.5
#         pause (cycle - .4)
#         repeat


# style skip_frame is empty
# style skip_text is gui_text
# style skip_triangle is skip_text

# style skip_frame:
#     ypos gui.skip_ypos
#     background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
#     padding gui.skip_frame_borders.padding

# style skip_text:
#     size gui.notify_text_size

# style skip_triangle:
#     ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
#     ## glyph in it.
#     font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 0.8
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    xalign 0.5
    xpos 0.5
    ypos gui.notify_ypos

    background Frame("gui/frame.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

# style pref_vbox:
#     variant "medium"
#     xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        #textbutton _("뒤로") action Rollback()
        # textbutton _("스킵") action Skip() alternate Skip(fast=True, confirm=True)
        # textbutton _("자동저장") action Preference("auto-forward", "toggle")
        #textbutton _("메뉴") action Show("esc_menu")


style window:
    variant "touch"
    background "gui/textbox_small.png"

# style radio_button:
#     variant "small"
#     foreground "gui/phone/button/check_[prefix_]foreground.png"

# style check_button:
#     variant "small"
#     foreground "gui/phone/button/check_[prefix_]foreground.png"

# style nvl_window:
#     variant "small"
#     background "gui/phone/nvl.png"

# style main_menu_frame:
#     variant "small"

# style game_menu_outer_frame:
#     variant "small"
#     background "gui/phone/overlay/game_menu.png"

# style game_menu_navigation_frame:
#     variant "small"
#     xsize 340

# style game_menu_content_frame:
#     variant "small"
#     top_margin 0

# style pref_vbox:
#     variant "small"
#     xsize 400

# style bar:
#     variant "small"
#     ysize gui.bar_size
#     left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

# style vbar:
#     variant "small"
#     xsize gui.bar_size
#     top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

# style scrollbar:
#     variant "small"
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

# style vscrollbar:
#     variant "small"
#     xsize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "touch"
    ysize gui.slider_size
    base_bar Frame("gui/slider_phone/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider_phone/horizontal_[prefix_]thumb.png"

# style vslider:
#     variant "small"
#     xsize gui.slider_size
#     base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

# style slider_pref_vbox:
#     variant "small"
#     xsize None

# style slider_pref_slider:
#     variant "small"
#     xsize 600





