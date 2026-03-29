# CHARACTERS
define pom_idk = Character("Forlorn Gardener")
define pom = Character("Pom", color="#0e5d34")

define wiz_idk = Character("Rancid Small Man")
define wiz = Character("Magmodeus the Staunch, Greatest Wizard of All the Realms",color="#13489c")

define sam_idk = Character("Bug Man???")
define sam = Character("Gregor Samsa", color="#305f54")

## VARIABLES
define grandScore = 0 
#   Pom
define pomBad = False
#   Wiz
define knowApprentice = False
define wizBad = False
define wizBadPre = False
#   Samsa
define samBad = False
define samPreBad = False

label start:    #paper intro!
    # pause 1.0
    play sound "audio/sfx_paper.mp3" volume 0.5
    show bg letter1 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 0.5
    show bg letter2 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 0.5
    show bg letter3 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 0.5
    show bg letter4 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 1
    
    play sound "audio/sfx_trainwhistle.mp3" fadein 0.5 volume 0.5
    play music "audio/bgm_train.mp3" fadein 1 volume 0.1
    scene bg titlecard 
    with slideleft
    $ renpy.pause()

##  POM CHARACTER ARC
label Pom:
    scene bg compartment
    with fade
    play sound "audio/sfx_doorslide.mp3" volume 1
    ## SCENE INTRO/DESCRIPTION
    "You open the door to the compartment. As you enter, the train's gentle smell of worn leather and walnut wood fades,
    and you pick up a new scent–freshly cut flowers and…wet dirt?"

    show pom neutral
    with moveinright
    
    "As you observe the passenger, you begin to understand."

    "Before you on the plush, blue velvet seats, a young man with wild hair stares out of the window. 
    As he turns and notices you, you hear a soft, kind voice escape his lips."

    ## BEGIN POM DIALOGUE
    show pom talking
    
    pom_idk "Good morning! How can I help you?"

    show pom neutral
    "His dress sense confounds you. A brown, patched up apron rests gently over a muddied collared shirt, which once upon a time must have been quite elegant.
    On his face sit large,  gold-trimmed glasses, giving his eyes a kind air."
    
    "He sits surrounded by a variety of pots, holding them like a proud father holds his children. And yet, he doesn’t smile."
    "Stunning bouquets sit in glass vases, swaying gently with the train's movements. Some of his pots have spilt over, leaving small patches of dirt on the upholstery. "

    ## === MAJOR CHOICE 1 ===
    menu:
        "Tickets, please!":                                  #1A
            show pom happy
            #jump 1A
            pom_idk "Here you are, sir."
            "As the man hands you his ticket, you notice his hand shaking. Despite his sunny demeanor, he is clearly plagued by something."
            show pom neutral
            menu: 
                "By Jove, your hands are shaking! Are you alright, lad?":
                    pom_idk "Frankly? Not really, no. See all these plants? I was taking them into town to compete at the New Key Gardener’s Fair." 
                    pom_idk "But as they are now, they nothing but a leafy green pile of rubbish. No way I’ll win anything with those."
                    menu: 
                        "How so?":
                            jump pom_JOIN1

                "These flowers are absolutely delightful, what are you going to get up to in New Key?":
                    jump pom_1B

        "Lovely little green-house you’ve built in here!":  #1B
            label pom_1B:
                show pom happy
                pom "You really think so?"
                show pom talking
                pom" I was going to take them to the Gardener’s Fair in the city to compete, but look at them. They’re in a right state."
                menu:
                    "What do you mean?":
                        "He pauses for a moment, then bursts out." #TODO: Replace
                        #jump pom_JOIN1:
            
        "OH MY GOD THERE IS FILTH EVERYWHERE":              #1C
            show pom sad
            "The man looks around and back at you. He starts to tear up."
            pom_idk "I’m sorry, I’m such a bloody mess I shouldn’t even have boarded this train..."

            menu:
                "Sorry--I, er, flew a bit off the handle there. Are you doing alright son?":
                    show pom worried
                    pom_idk "Honestly, not at all. See all these flowers? I was going to take them to a competition in New Key but I’ll never win with these..."
                    menu:
                        "How come?":
                            jump pom_JOIN1


                "Damn right about that! Get the hell off of my train!":
                    $ pomBad = True
                    jump pom_BADEND

    label pom_JOIN1:
        show pom worried
        pom_idk "I mean, look at them! I forgot the daisies at home, nobody’s going to think forgetmenots are interesting, and worst of all, my roses aren’t even red!"
        show pom sad
        pom_idk "A right mess I am, I should have never even boarded this train..."

        "The young man tears up. His face turns red as he turns away from you in shame."
        show pom sad
        ## === MAJOR CHOICE 1 ===
        menu:
            "Alright lad, settle down, settle down. Why don’t you tell me your name and what this is all about?":
                show pom talking
                pom "I’m Pom. I've been preparing to compete at the Gardener's Fair for months, but now I’ve made a right mess of things."
                pom "Red roses, lively lilies, that’s the kind of bouquet you need to win a competition! Not my pale roses and little specks of blue."
                jump pom_JOIN2

            "{i}Lay your arm around his shoulder {/i} I’m sure we can figure something out, no?":
                show pom talking
                pom_idk "Trust me, sir, I’ve tried. A bike almost hit me on my way to the station and I was only able to grab these before hurrying to the train; and now I’ve lost my prize-winning blooms..."
                pom "{i}mumbling {/i} Pom, you’re a right dolt."
                jump pom_JOIN2

            "You’re not wrong lad, those flowers look worse than the bramble on my grandmother’s house...":
                show pom sad
                "The young man tears up. His face turns red as he turns away from you and starts to cry quietly."
                pom_idk "God, I’m such a bloody dimwit. I shouldn’t’ve  gotten on this train..."
                $ pomBad = True
                jump pom_BADEND

    label pom_JOIN2:
        show pom neutral
        "Pom gestures towards the pots and bouquets. Lively little forgetmenots bloom in them, so small and numerous you cannot help but smile."
        "Besides them stand peach roses, white yarrow flowers and some other pale yellow blossoms you don’t recognise. Each flower seems more beautiful than the last."
        
        menu:
            "{i}Put some flowers together into a bouquet {/i} I’m no florist, but these look rather nice together, don’t they?":
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
                show pom talking
                pom "You’re right, I know I am. Maybe you are right and I just need to show them what they’re missing out on..."
                    #jump pom_JOIN5

            "If I were you, I’d much rather compete and lose with flowers I love rather than suck up to some old geezer with bad taste.":
                jump pom_JOIN5
    
    label pom_JOIN5: #POM GOOD ENDING
        show pom happy
        "Light seems to come back into the young gardener's eyes as inspiration takes hold."
        pom "I’ll compete. Even if I lose, I’ll have my flowers."
        pom "And they’ll still be quite nice for the city people to look at. It’s not everyday you get to show off your hard work to an entire city after all!"

        play sound "audio/sfx_doorslide.mp3" volume 1
        scene bg hallway
        "The smell of sweet peach roses and hopeful hyacinths follows you into the hallway as you close the sliding door behind you."
        "A smile hushes across your lips as you imagine Pom's beautiful flowers stunning all of New Key."
        $ grandScore += 1

    label pom_BADEND:
        if pomBad:
            scene bg hallway
            # play sound "audio/sfx_talking.mp3" volume 0.2
            "The train comes to a slow stop at Rosegarden Station."
            "With his head hung low, the young man exits the train. The smell of roses fades, returning you to your world of leather and wood."

##  WIZARD CHARACTER ARC
label Wizard:
    label WizardIntro:
        scene bg compartment
        with fade

        ## SCENE INTRO/DESCRIPTION
        "As you approach the door of the next passenger’s, a loud rumble, then a loud curse, then...silence."
        "Disquieted by the sudden absence, you carefully approach the door."

        "Unknown" "{b}EUREKA!{/b}"
        play sound "audio/sfx_explosion.mp3" volume 0.5
        "You flinch. Not at the sudden yell, but the explosion that follows immediately after."

        "Before you know what’s going on, the door comes to greet before you get a chance to, smashing both into you and the wall behind you."
        "With a slight cough, you throw the door aside and get back on your feet."
        show wizard shadowed
        with dissolve
        "Through the mist, you begin to recognise a shape: a tall, imposing figure walks towards you as you adjust your hat. For a moment, a cold shiver runs down your spine."

        "Unknown" "{b}WHO ARE YOU TO DISTURB MY MACHINATIONS?!{/b}"

        "As the dust settles, you realise that your fear might have been in vain."
        show wizard neutral
        with dissolve
        "The figure standing before you is a small, bearded man cloaked in a dark blue cape."
        "The imposing height you feared but a second ago seems to come entirely from his star-spangled hat."

    menu:       #MAJOR CHOICE 1
        "{i}Intense coughing {/i} Tickets please!":
            show wizard thinking
            wiz_idk "Ticket, yeeees, tickets. That is all they ask for, all they care for, but me, I have greater plans...machinations, even!"
            wiz_idk "Machinations a simple mind like yours could never comprehend!"
            menu: #Sub-choice 1a
                "Ahem. Tickets. Please.":
                    show wizard neutral
                    "The man looks at you with eyes filled to the brim with insanity."
                    "Without breaking eye-contact, he slowly reaches into his sleeve and pulls out a ticket."
                    "As you grab it, you realise how wet it is. The name, clearly written with a quill or some other old-fashioned implement, has become illegible."

                    menu:
                        "Thank you. Do you mind telling me your name, sir?":
                            jump wiz_JOIN2
                "...What?":
                    jump wiz_JOIN1

        "By Jove! What on earth is happening in there? What happened to the window?":
            jump wiz_JOIN1

        "{b}MY DOOR! MY WINDOW! YOU WILL PAY FOR THIS YOU TRAFFIC-CONE SHAPED DIMWIT!{/b}":
            show wizard mad
            wiz_idk "OH, YELLING, ARE WE?"
            wiz "I, MAGMODEUS THE STAUNCH, GREATEST WIZARD IN ALL THE REALMS AND OF ALL TIME, WILL NOT SUFFER SUCH DISRESPECT AT THE HANDS OF A SIMPLETON!"
            menu:   #Sub-choice 1c
                "Good Heavens, calm yourself! Just...explain to me what happened and we can keep yelling after!":
                    jump wiz_JOIN1
                "AND I WILL NOT HAVE A CRUSTY, HOMICIDAL FINGER WIGGLER ON MY TRAIN! OUT!":
                    $ wizBad = True
                    jump wiz_BADEND
            
    label wiz_JOIN1:
        show wizard neutral
        wiz "Experiments, my dear boy! I, Magmodeus the Staunch, Greatest Wizard of all the Realms, and of all time am conducting experiments of utmost importance! "
        wiz "I am to present my findings to the Wizarding Council of New Key this week, and I have yet to complete my writings!"
        show wizard thinking
        wiz "Alack, my newest apprentice and keeper of the minutes has, mysteriously, gone missing! I could swear he was here a moment ago..."
    
        "The Wizard turns around, observing the window with an almost bemused expression."
        
        wiz "Ah...that explains it. Not the first time it has happened I suppose."
        
        show wizard neutral
        "He turns back to you, staring into what you feel must be either the deepest corners of your soul, or absolutely nothing at all."
        "Finally, he extends his hand to you. His bony, pale, ice-cold hand."
        jump wiz_JOIN2

    label wiz_JOIN2:
        show wizard happy
        wiz "Magmodeus the Staunch, Greatest Wizard of all the Realms, and of all time, if I may say so myself!"
        wiz "You are? Well, it hardly matters."
        
        wiz "Say, dear boy, are you in search of work? I need a young, virile fellow like yourself to aid me in my research!"

    menu:   #MAJOR CHOICE 2
        "{i}Shake his hand {/i} A...pleasure. I’d be honoured to work with a true professional such as yourself.":
            "Grasping his hand makes your stomach turn."
            "You feel cold and hot simultaneously, as if you’re suddenly struck with the heaviest of fevers."
            "Not a good look for a job interview."
            show wizard neutral
            wiz "Likewise, dear boy! I have been in need of one ever since my dear...what was it? Daniel? Dan? D-Dog?"
            show wizard thinking
            wiz "Can’t have been a very good one since he flew out the window like a half-empty bag of potatoes!"
            show wizard happy
            wiz "Here, sign this and we’ll get to work, dear boy!"

            "A crusty, brown piece of parchment reading {i}“CONTRACT FOR {s}SHERLOCK{/s} {s}BRAM{/s} {s}AMOS{/s} NEW APPRENTICE” appears in his hand."
            "Before you know it, a pen appears in your hand, moving so independently you can barely stop yourself from signing the contract."
            "...Maybe this was a bad idea."
            show wizard thinking
            wiz "Spectacular! Now, I will need some time to set up the experiment again; hopefully you perform better than whatever-his-name was."
            show wizard neutral
            wiz "But for now, go! Tend to your obligations and I...shall call upon you when I most need you."
            show wizard happy
            "The most bizarre grin you’ve ever had the displeasure of witnessing spreads across your new boss’s face as you shake his hand again."
            "As soon as he lets go, Magmodeus wiggles his fingers and you are pushed violently back out into the hall."
            
            scene bg hallway
            with hpunch
            play sound "audio/sfx_doorslide.mp3" volume 1
            "When you turn around, the door is back where it was, and muffled voice bids you adieu."

            wiz "Ta, dear boy! I shall see you soon!"
            "As you face the hall, your new employer's cackle fills your ears, and your stomach turns again."
            "You dread your stay in New Key City."
            $ grandScore += 1
            
        "“Not the first time”?":
            wiz "Yes, yes, I think I might have lost three this week!"
            wiz "None of them will see the big city now, but such is the price of progress!"
            menu:   #sub-choice 2B
                "Have you ever considered that your work might be more successful if you didn’t need to...find new apprentices each day?":
                    show wizard thinking
                    "A glimmer of something you can only describe as “morbid inspiration” filles Magmodeus’s eyes."
                    show wizard happy
                    "You see decrepit yellow teeth, standing in line like rotting ancient tomb stones, as a smile creeps across the Wizard’s face and widens into a disgusting cackle."
                    
                    wiz "Absolutely magnificent! If I simply stockpile apprentices I won’t have to take in all these simple men!"
                    wiz "Simply spectacular, dear boy. I am {i}simply{/i} spectacular."
                    wiz "And as it just so happens, I am {i}surrounded{/i} by potent individuals to bag!"
                    menu:
                        "Oh no.":
                            "Magmodeus does not hear you. He pushes past you, leaving a dark, green stain on your trousers with his hand."
                            "A vile smell rises into your nose, making you wonder if its the odour or your conscience making your stomach turn as you watch the Wizard walk towards the next cart..."
                            $ grandScore += 1

                "Am I going to die?":
                    show wizard thinking
                    wiz "What are you, a coward? Or worse...a rat?"
                    show wizard mad
                    wiz "{b}A FILTHY RAT SENT BY THE COUNCIL TO SPY ON MY MACHINATIONS?{/b}"
                    $ wizBadPre = True;
                    jump wiz_pre_BADEND
                "You’re insane! I won’t let you keep killing people for your pointless experiments!":
                    $ wizBadPre = True;
                    jump wiz_pre_BADEND

        "You’re insane! Get the hell off of my train before I call the mage-catcher!":
            $ wizBadPre = True;
            jump wiz_pre_BADEND

    label wiz_pre_BADEND:
        if wizBadPre:
            show wizard mad
            "Magmodeus stares at you with white-hot rage glazing over his eyes."
            "Suddenly, he raises his arms as if to claw at you and hisses loudly."
            wiz "Go ahead and try it, cretin! Nothing and no-one catches Magmodeus the Staunch, Greatest Wizad of All the Realms! I shall find more apprentices elsewhere and you shan’t stop me!"
            $ wizBad = True
            jump wiz_BADEND
    label wiz_BADEND:
            if wizBad:
                
                scene bg compartment
                with hpunch
                play sound "audio/sfx_explosion.mp3" volume 1
                "Magmodeus turns towards the window. Before you realise what is happening, another explosion catapults you into the hall. There is no trace of the Wizard."
                
                "There are, however, traces of his having been here. Glass lies upon the wooden floor and black soot stains cover every surface of the compartment."
                "Through the shattered window, somehow an even sadder sight than before, you hear a faint, yet mad cackle."
                if knowApprentice:
                    "You shiver when you think of how many apprentices you sacrificed with your decisions here today."

## SAMSA CHARACTER ARC
label Samsa:
    label SamIntro:
        scene bg hallway
        with fade

        ## SCENE INTRO/DESCRIPTION
        "The compartment before you unnerves you..."
        "Not a single movement, not a single sound comes from within."
        "Peering through the tinted windows, however, you can clearly see the silhouette of a passenger within."

        menu:
            "{i}Knock politely {/i} May I come in?":
                "Unknown" "Hm? What? Oh yeah, come in."
                play sound "audio/sfx_doorslide.mp3" volume 1
                scene bg compartment with fade
            "Open the door":
                play sound "audio/sfx_doorslide.mp3" volume 1
                scene bg compartment with fade
        
        "As you open the door, a cold, primal fear grips your entire body."
        show samsa neutral
        with moveinright
        "Sitting in front of you on the plush upholstery sits a grotesque, human-sized bug."
        "A tie hangs loosely around his neck, emphasising his long, creaky carapace covered by a sports coat with only two sleeves."
        "Were he human, you’d call him dapper. But he’s not. He’s a bug."

        menu:   #   MAJOR CHOICE 1
            "I- er- wha- ...Tickets please!":
                sam_idk "Hm? Oh yeah, tickets. You need those. Here you go."
                "You hear hard chitin plates rub against one another as he clumsily pulls a small piece of paper from his jacket pocket"
                "As he passes you the slip, you realise that his sharp claws have mangled it entirely."

                menu:
                    "Thanks, but...this is completely illegible.":
                        sam_idk "Right...the claws. Those’ll be fun to work spreadsheets with..."
                        menu:
                            "I feel like you should take a day off to work out this whole...bug situation.":
                                jump sam_JOIN2
                    "You, er, have claws. That’s not normal.":
                        jump sam_JOIN1
            "Great Scott, what the hell are you?!":
                sam_idk "An accountant. Kind of a weird question to ask a stranger."
                "The bug’s mandibles click so slowly it feels like a sigh."
                menu:
                    "That’s not what I mean! Do you not know that you’re a giant bug?":
                        jump sam_JOIN1
            "{i}SCREAM{/i}":
                show samsa dejected
                sam_idk "Oh no...I’m sorry for startling you...you probably thought that there wasn’t anyone in here..."
                menu:
                    "No, no, don’t apologise. It’s just...you’re a giant bug.":
                        jump sam_JOIN1
                    "Giant b-bug!! Pest control in here now!!":
                        $samBad = True;
                        "Before the beast can respond, you slam the door shut. No vile beasts will prey on your valued passengers!"
                        "Pest control arrives shortly after, and as you walk away, you smell the sickly stench of insecticides filling the compartment before you."
                        "Your passengers are safe; another job well done!"
                        jump sam_BADEND

    label sam_JOIN1:
        show samsa dejected
        sam_idk "Oh right...I forgot. Sorry about that."
        sam_idk "I woke up like this today but...boss would kill me if I didn’t come in today, so..."

        menu: 
            "I feel like you should take a day off to work out this whole...bug situation.":
                jump sam_JOIN2
            "So you’re just...content with this?":
                sam_idk "I guess so...Everyone has a job, right? Aren’t you doing yours right now?"
                menu:
                    "But you’re a bug! Bugs don’t work in accounting!":
                        show samsa hopeful
                        "A brief look of recognition hushes across Gregor’s face, or so you think."
                        jump sam_JOIN3
                    "I guess so":
                        $ samPreBad = True
                        jump sam_pre_BADEND
            "Tell me about it. My boss has been busting my balls for years now...":
                $ samPreBad = True;
                jump sam_pre_BADEND
    
    label sam_JOIN2:
        "Gregor turns his head to look at you, making every plate in his neck creak. Each one of his thousands of eyes is filled with nothing but raw apathy."
        
        sam "I’ve already taken three days off this year, I would get fired if I took any more."
        show samsa dejected
        sam "I haven’t even had time to visit family this year..."
        menu:
            "That’s horrible! How are you even alive?":
                sam "Well, you know how it is...Boss makes a dollar, I make a dime, that’s why I’m a bug on company time..."
                "You expect to detect some hint of cynicism on Gregor’s face, but even through the mandibles and thousands of eyes, you can tell that he isn’t smiling."
                menu:
                    "Come on, you deserve better than this. If turning into a half-tonne chitinous beast doesn’t merit some rest, then what does?":
                        sam "That’s...fair I suppose."
                        show samsa hopeful
                        sam "Maybe I’ll go visit my aunt in the city. I haven’t seen her in months, and she was always fond of insects..."
                        "Excited clicking fills the room as Gregor tells you about things he and his aunt used to get up to when he was younger."
                        
                        play sound "audio/sfx_doorslide.mp3" volume 1
                        "When you leave the compartment, your exoskeletal friend is positively buzzing. You smile as you think of a middle aged woman and her gigantic bug nephew conquering New Key City."
                        jump sam_GOODEND

                    "Gregor, you’re a bug! Bugs don’t work in accounting!":
                        jump sam_JOIN3

            "But you’re a bug! Bugs don’t work in accounting!":
                "A brief look of recognition hushes across Gregor’s face, or so you think."
                jump sam_JOIN3

    label sam_JOIN3:
        sam "...It’s true, and I would know. I’ve never even seen a bug in my office before..."
        menu:
            "See! Maybe just take one day to sort out the fact that you have more eyes than this train has wheels.":
                show samsa hopeful
                "Gregor nods. A slightly more lively clicking escapes his jaws as he begins to discuss things to do in New Key City, even agreeing to meet for dinner tonight."
                play sound "audio/sfx_doorslide.mp3" volume 1
                "When you leave the compartment, your exoskeletal friend is positively buzzing. You smile as you think of all the fun things Gregor will be getting up to today."
                jump sam_GOODEND
    label sam_GOODEND:
        $grandScore += 1
    label sam_pre_BADEND:
        if samPreBad:
            show samsa dejected
            sam_idk "See? We’re all just doing our jobs."
            sam_idk "You talk to giant bug accountants, and I work spreadsheets for a living. Nothing that interesting about it..."
    label sam_BADEND:
        # if samBad:
        #     $grandScore -
        

return
