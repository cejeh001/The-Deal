# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define L = Character("Licc", color="#b24a4a",)
define N = Character("Note", color="#4a7eb2")

# Define a transform for subtle bounce when speaking
transform speaking_bounce:
    easein 0.1 yoffset -15  # Quick rise up
    easeout 0.2 yoffset 0   # Gentle fall down with bounce effect

# images
image Licc 1 = "images/Licc 1.png"
image Licc 2 = "images/Licc 2.png"
image Licc 3 = "images/Licc 3.png"
image Licc 4 = "images/Licc 4.png"
image Licc 5 = "images/Licc 5.png"
image Licc 6 = "images/Licc 6.png"
image Licc 7 = "images/Licc 7.png"
image Licc 8 = "images/Licc 8.png"
image Licc 9 = "images/Licc 9.png"
image Licc 10 = "images/Licc 10.png"
image Licc 11 = "images/Licc 11.png"
image Licc 12 = "images/Licc 12.png"
image Licc 13 = "images/Licc 13.png"
image Licc 14 = "images/Licc 14.png"
image Licc 15 = "images/Licc 15.png"
image Licc 16= "images/Licc 16.png"
image Licc 17= "images/Licc 17.png"
image Licc 18= "images/Licc 18.png"

image bg room = "images/background.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    "A minimalistic glass meeting room, high above the city."
    "The artist, Note, sits across from a man in a crisp, too-perfect suit: Licc, a representative from the AI company SynMind."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Licc 1 at center
    play music "audio/fluffing a duck 1 hour loop.mp3" loop fadein 2.0

    # These display lines of dialogue.

    L "Nice to see you arrive to arrange this deal, Mister Note."

    N "Nice to meet you too."

    # show Licc 2 at center 
    show Licc 2 at speaking_bounce

    L "Just so you know what we’re about, I’m Licc, and I proudly represent SynMind, an organiation using AI to innovate art."

    show Licc 3 at speaking_bounce

    L "We have... collaborated with many creators and are happy to add you to the team."

    show Licc 4 at speaking_bounce

    L "Your illustrations are very and I mean VERY good."

    N "Thank you."

    L "You’re very skilled~"

    show Licc 5 at speaking_bounce
    L "It is a shame they don’t pay your rent, and you’re on the final pieces of your savings."

    N "Yeah..."

    show Licc 2 at speaking_bounce

    L "And so I’m elated to offer you a deal."
    L "SynMind, our organisation, wants you to promote our franchise! And in exchange..."
    show Licc 6 at speaking_bounce
    L "we’ll give you up from 5 million dollars!"

    menu:
        L "What do you think?"

        "Accept Deal":
            jump accept


        "Refuse":
            stop music
            play sound "audio/Epic Shock (Doom).mp3" noloop

            N "I'm sorry, but I can't accept this deal."

            show Licc 9 at speaking_bounce

            play music "audio/sneaky snitch.mp3" loop

            L "Hmm? Why not?"

            show Licc 5 at speaking_bounce

            L " Oooohh, I get it, you think it’s inauthentic or we’ll have you under our thumb or something?"

            show Licc 10 at speaking_bounce

            L "I can assure you, Note, we’re not asking you to sell your soul or anything of the sort..."

            show Licc 3 at speaking_bounce

            L "all we’re asking of you to do for millions of dollars is to tell the world that we aren’t trying to replace creativity – we're just amplifying it~"


            show Licc 2 at speaking_bounce
            menu:

                L "Isn't it a good idea for you to help us?"

                "Accept Deal":
                    jump accept
                
                "Refuse":

                    stop music

                    N "Amplifying it with what, exactly?"

                    N " A database of every artist’s work you scraped without permission?"
                    
                    show Licc 10 at speaking_bounce

                    play music "audio/NXT elevator.mp3" loop

                    L "Woah woah woah, who said we did all that?"
                    L "And even if we have, we’re long past that... we’ve learned from those mistakes."

                    show Licc 1

                    L "What we do now is reach out a hand to artists from our side."

                    show Licc 4 at speaking_bounce

                    L "Artists like you, Note."

                    menu:
                        "Accept Deal":
                            jump accept
                        
                        "Refuse":

                            stop music

                            N "Sorry, but I can't force myself to smile, take your money, and tell my audience it’s okay to use a machine to finish their painting for them."

                            show Licc 3 at speaking_bounce

                            play music "audio/tense gameshow music.mp3" loop

                            L "No. You say that with SynMind, anyone can create."
                            L "You don’t have to say you use it. You don’t even have to like it."

                            #new one here
                            show Licc 8 at speaking_bounce

                            L "Just accept it."

                            menu:
                                "Accept Deal":
                                    jump accept
                                
                                "Refuse":
                                    N " You’re asking me to stand next to this wreckage and smile like it’s progress."

                                    #new one here: smiling with shadows n stuff
                                    show Licc 11 at speaking_bounce

                                    L "It IS progress. Evolution, even. All you’re doing right now is slowing it down, and why do that when you can help people feel less afraid?"
                                    L "With all due respect, I feel you’re letting all your power go to waste here."
                                    L "Imagine how much better your life will be with that money, too. Any artist would kill for a stable career doing what they love most."

                                    N " You really think selling out the people who can’t afford to compete with you is me using my power for good?"
                                    #new one here: mouth closed
                                    show Licc 12 at center
                                    L ""
                                    # show Licc new one here
                                    show Licc 13 at speaking_bounce

                                    stop music

                                    L "Fair enough."

                                    # new one here: arms crossed

                                    show Licc 14 at speaking_bounce

                                    play music "audio/Elevator Music.mp3" loop

                                    L "You know, most people don’t even hesitate. They just see the number and nod."

                                    show Licc 15 at speaking_bounce

                                    L "But you… you’re still thinking about the people who listen to you."

                                    show Licc 16 at speaking_bounce

                                    L "That’s rare. And I respect it."

                                    N "Respect doesn't usually come with a non-disclosure agreement."

                                    show Licc 17 at speaking_bounce

                                    L "Touché."

                                    
                                    show Licc 3 at speaking_bounce

                                    L "Well with that settled, we won’t bother you again."
                                    L "This kind of offer only works if it feels right. And that’s clearly not the case for you."
                                    show Licc 13 at speaking_bounce
                                    L "I wish you the best in whatever you plan to do with all those paintings."
                                    L "Just know that when the world changes, this door will be open."

                                    show Licc 18 at speaking_bounce
                                    stop music fadeout 2.0

                                    L "The best legacy is the one you can live with after all ~~"

    # This ends the game.
    hide Licc 18 with dissolve
    "she closes the door behind her, leaving Note alone in the room."
    scene black with Dissolve(2.0)
    pause(10.0)
    return


#acceptance scene
label accept:

    show Licc 8 at speaking_bounce
    play music "audio/Mario Party 2 - Let the Game Begin.mp3" loop
    L "Nice! Good to have you on the team, Note!"
    N "Yeah, thanks..."

    #fade to black
    scene black with Dissolve(2.0)
    stop music fadeout 2.0
    pause(10.0)
    return