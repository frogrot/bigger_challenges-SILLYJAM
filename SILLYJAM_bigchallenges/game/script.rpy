# CHARACTERS
define pom = Character("Pom")
define wiz = Character("Wizard")

#VARIABLES
define grandScore = 0 
define pomBad = False

label start:
    window hide dissolve
    pause 1.0
    scene bg with dissolve
    pause 1.0
    window show dissolve
    "Bigger Challenges' SILLY JAM Entry"

## POM CHARACTER ARC
label Pom:
    scene bg compartment
    with fade
    show pom neutral

    ## SCENE INTRO/DESCRIPTION
    "You open the door to the compartment. As you enter, the train's gentle smell of worn leather and walnut wood fades,
    and you pick up a new scent–freshly cut flowers and…wet dirt?"

    "As you observe the passenger, you begin to understand."

    "Before you on the plush, blue velvet seats, a young man with wild hair stares out of the window. 
    As he turns and notices you, you hear a soft, kind voice escape his lips."

    ## BEGIN POM DIALOGUE
    show pom talking
    
    pom "Good morning! How can I help you?"

    show pom neutral
    "His dress sense confounds you. A brown, patched up apron rests gently over a muddied collared shirt, which once upon a time must have been quite elegant.
    On his face sit large,  gold-trimmed glasses, giving his eyes a kind air."
    
    "He sits surrounded by a variety of pots, holding them like a proud father holds his children. And yet, he doesn’t smile."
    "Stunning bouquets sit in glass vases, swaying gently with the train's movements. Some of his pots have spilt over, leaving small patches of dirt on the upholstery. "

    ## === MAJOR CHOICE 1 ===
    menu:
        "Tickets please!":                                  #1A
            show pom happy
            #jump 1A
            pom "Here you are, sir."
            "As the man hands you his ticket, you notice his hand shaking. Despite his sunny demeanor, he is clearly plagued by something."
            show pom neutral
            menu: 
                "By Jove, your hands are shaking! Are you alright, lad?":
                    pom "Frankly? Not really, no. See all these plants? I was taking them into town to compete at the New Key Gardener’s Fair." 
                    pom "But as they are now, they nothing but a leafy green pile of rubbish. No way I’ll win anything with those."
                    menu: 
                        "How so?":
                            jump pom_JOIN1

                "These flowers are absolutely delightful, what are you going to get up to in New Key?":
                    jump pom_1B

        "Lovely little green-house you’ve built in here!":  #1B
            label pom_1B:
                show pom happy
                pom "You really think so? I was going to take them to the Gardener’s Fair in the city to compete, but look at them. They’re in a right state."
                menu:
                    "What do you mean?":
                        "He pauses for a moment, then bursts out." #TODO: Replace
                        #jump pom_JOIN1:
            
        "OH MY GOD THERE IS FILTH EVERYWHERE":              #1C
            show pom sad
            "The man looks around and back at you. He starts to tear up."
            pom "I’m sorry, I’m such a bloody mess I shouldn’t even have boarded this train..."

            menu:
                "Sorry--I, er, flew a bit off the handle there. Are you doing alright son?":
                    show pom worried
                    pom "Honestly, not at all. See all these flowers? I was going to take them to a competition in New Key but I’ll never win with these..."
                    menu:
                        "How come?":
                            jump pom_JOIN1


                "Damn right about that! Get the hell off of my train!":
                    $ pomBad = True
                    jump pom_BADEND

    label pom_JOIN1:
        show pom worried
        pom "I mean, look at them! I forgot the daisies at home, nobody’s going to think forgetmenots are interesting, and worst of all, my roses aren’t even red!"
        show pom sad
        pom "A right mess I am, I should have never even boarded this train..."

        "The young man tears up. His face turns red as he turns away from you in shame."
        show pom sad
        ## === MAJOR CHOICE 1 ===
        menu:
            "Alright lad, settle down, settle down. Why don’t you tell me your name and what this is all about?":
                show pom talking
                pom "I’m Pom. I've been preparing to compete at the Gardener's Fair for months, but now I’ve made a right mess of things."
                pom "Red roses, lively lilies, that’s the kind of bouquet you need to win a competition! Not my pale roses and little specks of blue."
                jump pom_JOIN2

            "*Lay your arm around his shoulder* I’m sure we can figure something out, no?":
                show pom talking
                pom "Trust me, sir, I’ve tried. A bike almost hit me on my way to the station and I was only able to grab these before hurrying to the train; and now I’ve lost my prize-winning blooms..."
                pom "*mumbling* Pom, you’re a right dolt."
                jump pom_JOIN2

            "You’re not wrong lad, those flowers look worse than the bramble on my grandmother’s house...":
                show pom sad
                "The young man tears up. His face turns red as he turns away from you and starts to cry quietly."
                pom "God, I’m such a bloody dimwit. I shouldn’t’ve  gotten on this train..."
                $ pomBad = True
                jump pom_BADEND

    label pom_JOIN2:
        show pom neutral
        "Pom gestures towards the pots and bouquets. Lively little forgetmenots bloom in them, so small and numerous you cannot help but smile."
        "Besides them stand peach roses, white yarrow flowers and some other pale yellow blossoms you don’t recognise. Each flower seems more beautiful than the last."
        
        menu:
            "*Put some flowers together into a bouquet* I’m no florist, but these look rather nice together, don’t they?":
                show pom worried
                pom "I mean, they are my favourites. But nobody’s ever won with colours like these, I don’t even know if anyone’s tried! You’d have to be mad to."
                jump pom_JOIN4

            "Why are you so sure you’re not going to win?":
                jump pom_JOIN3

            "Oh dear, that is rather tricky, isn’t it?":
                jump pom_JOIN3

    label pom_JOIN3:
        pom "Nobody’s ever won with such a bold selection of colours! Red and gold is all the judges seem to ever pick."
        pom "Though, I can’t remember ever seeing anyone else compete with colours like these..."
        jump pom_JOIN4
    label pom_JOIN4:
        show pom neutral
        menu:
            "This could be your chance! If I were a judge, I’d be bored to death of seeing the same old things over and over again.":
                "Pom looks up, his eyes no longer wet with tears."
                show pom hopeful
                pom "You’re right, I know I am. Maybe you are right and I just need to show them what they’re missing out on!"
                    #jump pom_JOIN5

            "If I were you, I’d much rather compete and lose with flowers I love rather than suck up to some old geezer with bad taste.":
                jump pom_JOIN5
    label pom_JOIN5: #POM GOOD ENDING
        show pom happy
        "Light seems to come back into the young gardener's eyes as inspiration takes hold."
        pom "I’ll compete. Even if I lose, I’ll have my flowers."
        pom "And they’ll still be quite nice for the city people to look at. It’s not everyday you get to show off your hard work to an entire city after all!"

        "The smell of sweet peach roses and hopeful hyacinths follows you into the hallway as you close the sliding door behind you."
        "A smile hushes across your lips as you imagine Pom's beautiful flowers stunning all of New Key."
        "POM GOOD ENDING YIPPEE!!"

    label pom_BADEND:
        if pomBad:
            scene bg boarding
            "The train comes to a slow stop at Rosegarden Station."
            "With his head hung low, the young man exits the train. The smell of roses fades, returning you to your world of leather and wood."
            "POM BAD ENDING :("

    
return
