# You can place the script of your game in this file.
python:
    import random
    def get_random():
        return random.choice(['head','leg','hand','gun'])
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg start_img = "first_img.jpg"
image enemy john = "enemy.png"
# Declare characters used by this game.
define me = Character('Munis', color="#c8ffc8")
define me_health = 100
define enemy = Character('Enemy', color="#ff0000")


init python:

    tutorials = [
        ("tutorial_playing", _("User Experience"), "6.10.0"),
        ("tutorial_dialogue", _("Writing Dialogue"), "6.10.0"),
        ("tutorial_images", _("Adding Images"), "6.10.0"),
        ("tutorial_transitions", _("Transitions"), "6.99.8"),
        ("tutorial_music", _("Music and Sound Effects"), "6.10.0"),
        ("tutorial_menus", _("In-Game Menus and Python"), "6.10.0"),
        ("tutorial_positions", _("Screen Positions"), "6.10.0"),
        ("tutorial_atl", _("Animation and Transformation"), "6.10.0"),
        ("tutorial_video", _("Video Playback"), "6.10.0"),
        ("demo_transitions", _("Transition Gallery"), "6.11.1"),
        ("demo_imageops", _("Image Operations"), "6.5.0"),
        ("demo_ui", _("User Interaction"), "6.15.0"),
        ("demo_text", _("Fonts and Text Tags"), "6.13.0"),
        ("demo_character", _("Character Objects"), "6.2.0"),
        ("demo_layers", _("Layers & Advanced Show"), "6.17.0"),
        ("demo_nvlmode", _("NVL Mode"), "6.4.0"),
        ("demo_dynamic", _("Dynamic Displayables"), "5.6.3"),
        ("demo_minigame", _("Minigames"), "6.3.2"),
        ("demo_persistent", _("Persistent Data"), "6.7.0"),
        ("demo_transform", _("Transform"), "6.9.0"),
        ("tutorial_sprite", _("Sprites"), "6.12.0"),
        ]

screen tutorials:

    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for label, name, ver in tutorials:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True

                        hbox:
                            text name style "button_text" min_width 420
                            text ver style "button_text"

                null height 20

                textbutton _("That's enough for now."):
                    xfill True
                    action Return(False)

        bar adjustment adj style "vscrollbar"


# The game starts here.
#begin start


# The game starts here.
label start:
    
    play music "mortalkombat.mp3"
    
    scene bg start_img
    with fade
    me "Hello welcome to Dervish game"
    me "Are you ready for game ?"
    menu:
        "yes":
            jump beginning
        "no":
            jump exit

    return

label beginning:
    $ enemy_health = 100
    $ player_health = 100
    $ looping = True
    $ randfruit = renpy.random.choice(['apple', 'orange', 'plum'])
    scene bg start_img
    with fade
    show enemy john
    me "This is enemy"
    enemy "I wanna fight you !"
    me "Starting the fight"
    while looping:
        me "Select Your Attack Type"
        $ player_attach_damage = renpy.random.choice([5,10,20,30,40])
        $ player_defeat = renpy.random.choice([5,10,20,30,40])
        $ enemy_attack_damage = renpy.random.choice([5,10,20,30,40])
        $ enemy_defeat = renpy.random.choice([5,10,20,30,40])
        menu:
            "Blow to the head":
                pass
            "Blow to the chest":
                pass
            "Blow to the stomach":
                pass
            "Blow to the bels":
                pass
            "Kich in the legs":
                pass
        me "Defeat Yourself"
        menu:
            "Block of head and chest":
                pass
            "Block the chest and stomachs":
                pass
            "Block belly and waist":
                pass
            "Block legs and bels":
                pass
            "Block of legs and head":
                pass
        
        if enemy_defeat > player_attach_damage or enemy_defeat == player_attach_damage:
            me "Enemy was defeated !"
        else:
            $ player_hit = player_attach_damage - enemy_defeat
            $ enemy_health  -= player_hit
            me "You hit the enemy. enemy health: [enemy_health]"
        
        $ enemy_choice = renpy.random.choice(['Blow to the head', 'Blow to the chest', 'Blow to the stomach', 'Blow to the bels','Kich in the legs'])
        if enemy_choice == 'Blow to the head':
            pass
        elif enemy_choice == 'Blow to the chest':
            pass
        elif enemy_choice == 'Blow to the stomach':
            pass
        elif enemy_choice == 'Blow to the bels':
            pass
        elif enemy_choice == 'Kich in the legs':
            pass    
        
        if player_defeat > enemy_attack_damage or player_defeat == enemy_attack_damage:
            enemy "You defeated !"
        else:
            $ enemy_hit = enemy_attack_damage - player_defeat 
            $ player_health -= enemy_hit
            enemy "You was hit by enemy. Your heart: [player_health]"
        
        if enemy_health > 0 and player_health > 0:
            pass
        elif enemy_health < 0 and player_health > 0:
            me "Congratulation You Win !"
            $ looping = False
            pass
        elif enemy_health > 0 and player_health < 0:
            enemy "Game over enemy win !"
            $ looping = False
            pass
        elif enemy_health <= 0 and player_health <= 0:
            if enemy_health == player_health:
                me "Equality !"
                $ looping = False
                pass
            elif  enemy_health > player_health:
                enemy "Game over enemy win !"
                $ looping = False
                pass
            else:
                me "Congratulation You Win !"
                $ looping = False
                
                
        
    


label exit:
    
    me "Thank you for gaming"
    
    return