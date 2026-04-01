# CHARACTERS
define pom_idk = Character("Forlorn Gardener")
define pom = Character("Pom", color="#0e5d34")

define wiz_idk = Character("Rancid Small Man")
define wiz = Character("Magmodeus the Staunch, Greatest Wizard of All the Realms",color="#13489c")

define sam_idk = Character("Looming Insect")
define sam = Character("Gregor Samsa", color="#305f54")

define jones_idk = Character("Violent Man")
define jones = Character("Icicle Jones", color = "#86634d")

## VARIABLES
define grandScore = 0 
#   Pom
define pomBad = False
#   WizR
define knowApprentice = False
define wizBad = False
define wizBadPre = False
#   Samsa
define samBad = False
# Jones
define jonesBad = False

label start:    #paper intro!
    
    pause 1.2
    play sound "audio/sfx_paper.mp3" volume 0.5
    scene bg letter1 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 0.5
    scene bg letter2 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 0.5
    scene bg letter3 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 0.5
    scene bg letter4 with dissolve
    $ renpy.pause()
    play sound "audio/sfx_paper.mp3" volume 1
    
    play music "audio/bgm_train.mp3" fadein 1 volume 0.1
    scene bg titlecard 
    with slideleft
    $ renpy.pause()

label preSamsa:
    "It’s your first day on the job!"
    play sound "<from 3 to 10>audio/sfx_footsteps.mp3" volume .8
    "Who knows what exciting things might happen; the people you’ll meet, the landscapes you’ll travel through, all of it is very intriguing."
    play sound "audio/sfx_trainwhistle.mp3" fadein 0.5 volume 0.5
    "You hop onto the first cart with zest, looking forward to your day. The train whistles sounds, and off you go!" 
    play sound "audio/bgm_train.mp3" fadein 1 volume 0.2

## SAMSA CHARACTER ARC
label Samsa:
    label SamIntro:
        scene bg hallway with fade
        play sound "<from 0 to 10>audio/sfx_footsteps.mp3" volume .8
        
        ## SCENE INTRO/DESCRIPTION
        "The compartment before you unnerves you..."
        "Not a single movement, not a single sound comes from within."
        "Peering through the tinted windows, however, you can clearly see the silhouette of a passenger within."

        menu:
            "{i}Knock politely {/i} May I come in?":
                play sound "<from 0 to 3>audio/sfx_footsteps.mp3" volume .8
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
                        show samsa dejected
                        sam "Right...the claws. Gregor with the bug claws. That’s me."
                        sam "Those’ll be fun to work spreadsheets with..."
                        menu:
                            "I feel like you should take a day off to work out this whole...bug situation.":
                                jump sam_JOIN2
                    "You, er, have claws. That’s not normal.":
                        jump sam_JOIN1
            "Great Scott, what the hell are you?!":
                sam_idk "An accountant. Kind of a weird question to ask a stranger."
                show samsa dejected
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
                        $grandScore -= 1
                        play sound "audio/sfx_doorslide.mp3" volume 1
                        scene bg hallway with hpunch
                        "Before the beast can respond, you slam the door shut. No vile beasts will prey on your valued passengers!"
                        play sound "<from 2>audio/sfx_footsteps.mp3" volume .8
                        "Pest control arrives shortly after, and as you walk away, you smell the sickly stench of insecticides filling the compartment before you."
                        "Your passengers are safe; another job well done!"

                        "Composing yourself that moment of heroism, you perk up as you notice something perculiar."
                        "You take a deep breath in...Flowers? Not a common scent on a train!"
                        "You approach the next compartment, looking for the source."
                        jump Pom

    label sam_JOIN1:
        show samsa dejected
        sam_idk "Oh right...I forgot. Sorry about that."
        
        sam_idk " I woke up like this today but...boss would kill me if I didn’t come in today."
        sam "“Gregor, you’re a good-for-nothing idler and a fool”, he’ll say..."

        menu: 
            "I feel like you should take a day off to work out this whole...bug situation.":
                jump sam_JOIN2
            "So you’re just...content with this?":
                sam "I guess so...Everyone has a job, right? Aren’t you doing yours right now?"
                menu:
                    "But you’re a bug! Bugs don’t work in accounting!":
                        show samsa hopeful
                        "A brief look of recognition hushes across Gregor’s face, or so you think."
                        jump sam_JOIN3
                    "I guess so":
                        $ samBad = True
                        jump sam_BADEND
            "Tell me about it. My boss has been busting my balls for years now...":
                $ samBad = True;
                jump sam_BADEND
    
    label sam_JOIN2:
        "Gregor turns his head to look at you, making every plate in his neck creak. Each one of his thousands of eyes is filled with nothing but raw apathy."
        show samsa neutral
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
                        scene bg hallway with fade
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
                scene bg hallway with fade
                "When you leave the compartment, your exoskeletal friend is positively buzzing. You smile as you think of all the fun things Gregor will be getting up to today."
                jump sam_GOODEND
    label sam_GOODEND:
        play sound "<from 2 to 9>audio/sfx_footsteps.mp3" volume 1
        "As you walk from Gregor’s compartment to the next, uncomfortable thoughts creep into your brain."
        "Could you be a bug one random Monday morning?"
        "You shiver at the thought. What do bugs even think about all day?"
        "Flying from flower to flower…"
        "You take a deep breath in...Flowers?"
        "You approach the next compartment, looking for the scent’s source."
        jump Pom

    label sam_BADEND:
        if samBad:
            $grandScore -= 1
            show samsa dejected
            sam "See? We’re all just doing our jobs."
            sam "You talk to giant bug accountants, and I work spreadsheets for a living. Nothing that interesting about it..."
            
            "You both silently stare into nothing as you half-heartedly glance over the bug-man's ticket."
            "With everything in order, you quietly step out of the compartment."
            play sound "audio/sfx_doorslide.mp3" volume 1
            scene bg hallway with fade

   
##  POM CHARACTER ARC
label Pom:
    ## SCENE INTRO/DESCRIPTION
    play sound "<from 0 to 3>audio/sfx_footsteps.mp3" volume 1
    "Following the pleasant scent, you rap your knuckles against the next door and slide it open."
    play sound "audio/sfx_doorslide.mp3" volume 1
    scene bg compartment
    with fade
    "As you enter, the train's gentle smell of worn leather and walnut wood fades, replaced by freshly cut flowers and…wet dirt?"

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
        scene bg hallway with fade
        "The smell of sweet peach roses and hopeful hyacinths follows you into the hallway as you close the sliding door behind you."
        "A smile hushes across your lips as you imagine Pom's beautiful flowers stunning all of New Key."

    label pom_BADEND:
        if pomBad:
            $grandScore -= 1
            scene bg hallway with fade
            play sound "audio/sfx_doorslide.mp3" volume 1
            "The train comes to a slow stop at Rosegarden Station."
            "With his head hung low, the young man exits the train. The smell of roses fades, returning you to your world of leather and wood."

label Pom2Wiz:
    play sound "<from 5 to 10>audio/sfx_footsteps.mp3" volume .8
    "The scent of lilies and roses follows you as you walk through the hall towards your next compartment."
    "Though he was messy, Pom was not very difficult to handle."
    "With confidence, you step towards the next compartment, excited to see who sits inside."

##  WIZARD CHARACTER ARC
label Wizard:
    label WizardIntro:
        scene bg hallway
        ## SCENE INTRO/DESCRIPTION
        play sound "<from 5 to 10>audio/sfx_footsteps.mp3" volume .8
        "As you approach the door of the next passenger’s, a loud rumble, then a loud curse, then...silence."
        "Disquieted by the sudden absence, you carefully approach the door."

        "Unknown" "{b}EUREKA!{/b}"
        play sound "audio/sfx_explosion.mp3" volume 0.5
        show bg hallway with vpunch
        "You flinch. Not at the sudden yell, but the explosion that follows immediately after."
        play sound "<from 0 to 1.5>sfx_glassbreaking.mp3" volume 1
        "Before you get the chance to open it, the door flies off its hinges, smashing both into you and the wall behind you."
        "With a slight cough, you throw the door aside and get back on your feet."

        show bg compartment with hpunch
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
                    $ grandScore -= 1
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
            
        "“Not the first time”?":
            
            wiz "Yes, yes, I think I might have lost three this week!"
            show wizard thinking
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
                            play sound "audio/sfx_doorslide.mp3" volume 1
                            scene bg hallway
                            with fade
                            "A vile smell rises into your nose, making you wonder if its the odour or your conscience making your stomach turn as you watch the Wizard walk towards the next cart..."

                "Am I going to die?":
                    show wizard thinking
                    wiz "What are you, a coward? Or worse...a rat?"
                    show wizard mad with vpunch
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
            show wizard mad with hpunch
            wiz "Go ahead and try it, cretin! Nothing and no-one catches Magmodeus the Staunch, Greatest Wizad of All the Realms!"
            wiz "I shall find more apprentices elsewhere and you shan’t stop me!"
            $ wizBad = True
            jump wiz_BADEND
    label wiz_BADEND:
            if wizBad:
                play sound "audio/sfx_explosion.mp3" volume 1
                play sound "<from 1.8 to 3.8>sfx_glassbreaking.mp3" volume 1
                scene bg hallway
                with hpunch
                
                "Magmodeus turns towards the window. Before you realise what is happening, another explosion catapults you into the hall. There is no trace of the Wizard."
                "There are, however, traces of his having been here. Glass lies upon the wooden floor and black soot stains cover every surface of the compartment."
                "Through the shattered window, somehow an even sadder sight than before, you hear a faint, yet mad cackle."
                if knowApprentice:
                    "You shiver when you think of how many apprentices you sacrificed with your decisions here today."

label Wiz2Jones:
    play sound "<from 9>audio/sfx_footsteps.mp3" volume .8
    "You quake at the thought of what you just experienced."
    "Who the hell was that man?"
    "What was his deal?"
    "Are Wizards real?!"

    "You shake off the existential dread the rancid little man caused you and move on to the next compartment"
    "Hopefully your next passenger is a little less…eccentric."
#   ICICYLE JONES ARC
label Jones:

    scene bg hallway
    play sound "<from 0 to 5>audio/sfx_footsteps.mp3" volume .8
    ## SCENE INTRO/DESCRIPTION
    "An icy breeze rushes over you as you approach this compartment’s door."
    "Stepping closer, you see that the windows have been poorly covered by animal furs. Peeking through them, you see random assortment of pelts fill each corner of the room." 
    "A passenger, however, is nowhere to be seen."
    
    "Cautiously, you slide the door open and step into the compartment."
    play sound "<from 0 to 1>audio/sfx_footsteps.mp3" volume .8
    play sound "sfx_doorslide.mp3" volume 1
    scene bg compartment with fade
    show bg compartment with hpunch
    "Suddenly, your life flashes before your eyes as you hear the cocking of a gun from a dark corner of the room before you."

    show jones shadowed
    "You see the silhouette of a man, a lion skin cape that looks more like roadkill than a trophy wrapped around his shoulders."
    
    jones_idk"Are you with the yeti?"
    menu:
        "There’s a yeti?!":
            show jones wideeyed
            jones_idk "Darn right!"
            jones_idk "Same one drove me outta my home in the mountains, same one been chasin’ me fer nigh on four weeks now, that darn monster!"
            jones "But if ye ain’t seen no yeti, clever ol’ Icicle Jones must’ve lost him..."

            "The man, whom you assume to be Icicle Jones, lowers his gun."
            show jones neutral
            "His remaining eye beholds you with suspicion, but he seems to have calmed down for now."

            menu:
                "I, er, like your cloak.":
                    show jones happy
                    jones "Ah well thank you kindly!"
                    jones "‘Tis the only thang Icicle Jones was able to bring from my mountain, my pelts and my trusty Jezabelle..."

                    "Icicle Jones gentle strokes his gun before giving it a kiss and a rather violent sniff. He sighs."
                    show jones neutral
                    jones "But now that I ain’t got no mountain no more...I don’t really know what to do with any of ‘em no longer..."
                    jump jones_JOIN3
                "Is that why you’re on this train? Running from this...yeti?":
                    jones "Darn right. Icicle Jones ain’t ever been one fer all these modern thangs, but I remembered that them long metal snakes were awful quick."
                    show jones wideeyed
                    jones"Too quick for a yeti!"
                    jump jones_JOIN1
        "{i}Years of training are about to pay off. Disarm the aggressor with your jiujitsu skills.{/i}":
            "You’ve been waiting for this day."
            "With a quick and elegant twist you spring into action, disarming your opponent and punting him across the room like a football."
            show jones happy with vpunch
            "He crashes into the far side wall of the room, coughing and cackling as he gets back up"

            jones "Great mammoth’s balls! I ain’t been tossed around like that since that there yeti drove me from my cave!"
            menu:
                "Is that why you’re on this train? Running from this...yeti?":
                    show jones neutral
                    jones "Darn right. Icicle Jones ain’t ever been one fer all these modern thangs, but I remembered that them long metal snakes were awful quick."
                    show jones happy
                    jones "Too quick for a yeti"
                    jump jones_JOIN1
        "T-t-tickets please?":
            show jones wideeyed
            jones "Even if I knew what that was, Icicle Jones wouldn’t’ve given ye any “tick-its”. Now tell me, where’s that gosh darn yeti?"
            menu:
                "Talisman Railroad Co. has a strict anti-monster code! There are no yetis anywhere near this train!":
                    show jones happy
                    jones "You don’t say...well, then this seems like just the place fer me!"
                    jump jones_JOIN1
                "Are you crazy? What yeti? Put that gun away before I call security!":
                    jones "Don’t you threaten me, boah! I know that them yetis ain’t dumb!"
                    jones "They's proberbly out there right now, huntin’ me..."
                    menu:
                        "I swear to you, there are no yetis aboard this train. As the conductor, I would know!":
                            show jones neutral
                            jones "Hmm...well if you ain’t heard of no yetis then maybe there ain’t no yetis on this here ve-hickle."
                            jump jones_JOIN2
                        "Alright, that’s it. Security!":
                            jones "Oh, you think Icicle Jones is crazy?"
                            jones "Them yetis are a plague upon this here earth, ya hear me! And I am gettin’ away from them and you ain’t stoppin’ m-"
                            scene bg compartment_yeti with hpunch
                            jump jones_BADEND

    label jones_JOIN1:
        "Icicle Jones stalks towards the window like a drunk mountain lion."
        "He observes it for a few seconds, then smashes it with his raw fist before leaning out and yelling."

        jones "There ain’t no catchin’ up with ol’ Icicle Jones now, you foul beast of the night!"
        jones "You hear me! Icicle Jones is free!!"

    label jones_JOIN2:
        "He turns around and stares you down. You don’t know how much time passes as he simply...stands there."
        "Then, without breaking eye contact, Icicle Jones awkwardly spins his gun in his now bloodied hand, getting tiny specks of blood and gun powder over the upholstery."
        "Finally, he jams it into a ragged holster, made from an indiscernible number of rabbit furs."
        #jump jones_JOIN3

    label jones_JOIN3:
        "Looking at his pelts you realise how fine they are."
        "Were he not so...eccentric, he surely could make good money in New Key City."
        "You wonder why he chooses to wear these horrid scraps instead."

        jones "I ain’t never been to no city before, but I heard them city folk live comfy-like."
        show jones happy
        jones "Maybe them got warmer caves there!"
        menu:   #MAJOR CHOICE 2
            "You know, you could try to sell your pelts in town, that way you can get yourself a little money to start over!":
                show jones wideeyed
                "Icicle Jones locks eyes with you."
                "Slowly, his faces inches closer to yours until his big bushy beard is brushing against your chest."
                "You try your best to ignore the...earthy scent that now invades your personal space."
                show jones neutral
                jones "Yer sayin’ Icicle Jones could be...a businessman? Like them fancy types with a suit?"
                menu:
                    "Absolutely! You’ve got the charm, wit, and stunning good looks!":
                        show jones happy
                        jones "Icicle Jones is a mighty fine specimen, it’s true!"
                        show jones wideeyed
                        jones "That’s why Icicle Jones had ta flee, y’know? Darn yeti’s wife couldn’t keep her mitts off me!"
                        show jones happy
                        "Icicle Jones grins, then pulls your forehead against his."
                        "You feel his greasy hair pressed between your faces as he whispers."
                        show jones wideeyed with vpunch
                        jones "But let me tell you, don’t you ever go fraternisin’ with no yeti-wives, no matter how charmin’ they may be!"
                        jones "For I tell you, Icicle Jones is a peace-lovin’ man, but them yeti-husbands ain’t quite so!"

                        "As he lets go of your head, you take a deep breath. You will take this advice to heart."

                        show jones happy
                        jones "Hoo-wee! This is gon’ be excitin’! Icicle Jones’s Pelt Emporium!"
                        jones "Thank ye fer all yer thinkin’! Icicle Jones thinks the city’ll be fine!"

                        "Icicle Jones excitedly starts talking to...probably himself about his business plans."
                        "You’re sure he’ll make it big one day, he has the charm and the good looks after all."
                        
                        scene bg hallway with fade
                        play sound "audio/sfx_doorslide.mp3" volume 1
                        play sound "<from 2 to 10>audio/sfx_footsteps.mp3" volume .8
                        "You leave the compartment and go on your way, a small rabbit’s foot now tied to your keychain."
                        jump conclusion

            "How does one even begin to get chased by a yeti?":
                show jones neutral
                jones "Well...y’know. Icicle Jones is a handsome feller, and them yetis got pretty wives..."
                show jones happy
                "He grins through his thick beard. Then, he pulls you in close."
                show jones wideeyed with vpunch
                "You can feel your forehead rubbing against his, as he continues to speak."
                jones "But let me tell you, don’t you ever go fraternisin’ with them yeti-wives, them yeti-husbands ain’t got no skill fer diplomacy."
                jones "Icicle Jones is a peace lovin’ man, but them yetis ain’t quite so reasonable. Heed my words!!"
                menu:
                    "What’s your plan then?":
                        show jones neutral
                        jones "Icicle Jones hears that them city folks got bigger guns than me...and if’n I want my mountain back...well."
                        show jones wideeyed
                        jones "Icicle Jones shan’t say...that is Icicle Jones’s business, and Icicle Jones’s business alone! Now scram!"

                        "Finally, the Mountain Man lets go of your head and violently pushes you out the door."
                        scene bg hallway with vpunch
                        play sound "audio/sfx_doorslide.mp3" volume 1
                        play sound "<from 10 to 15>audio/sfx_footsteps.mp3" volume .8
                        "As you begin your walk to the next compartment, you realise that the yeti might be in more danger than Icicle Jones ever was."

            "{i}Chuckle {/i} You’re not wrong, I’ve never had to worry about yetis chasing after me in my life.":
                jones "Hoo-wee, that does sound quite nice. Icicle Jones is excited!"
                show bg compartment_yeti with dissolve
                $ jonesBad = True
                jump jones_BADEND

    label jones_BADEND:
        if jonesBad:
            $grandScore -= 1
            "The train rumbles."
            
            play sound "<from 0 to 1.5>sfx_glassbreaking.mp3" volume 1
            "Suddenly, a gigantic, white-furred hand bursts through the window, grabbing Icicle Jones. You lock eyes with him as he's suddenly pulled back."
            show jones wideeyed with vpunch
            jones "NO!!! THIS AIN’T THE LAST YOU SEEN OF ICICLE JONES, I SWEAR IT!! I SWEAR BY-"
            scene bg compartment_yeti with moveoutbottom
            "With one, swift motion, Icicle Jones disappears from sight."
            "Were it not for the copious amounts of pelts, shards of glass, and odd, earthy smell, you’d never think he’d been here in the first place."
            
            scene bg hallway with fade
            play sound "audio/sfx_doorslide.mp3" volume 1
            play sound "<from 6 to 13>audio/sfx_footsteps.mp3" volume .8
            "As you step back into the hallway, you nervously glance toward the windows. Maybe you aren’t safe from the yeti either..."
            

label conclusion:
    if grandScore == -4:
        scene bg bad with fade
        $ renpy.pause()
        scene bg bad2 with fade
        $ renpy.pause()

    elif grandScore == 0:
        scene bg good with fade
        $ renpy.pause()
        scene bg good2 with fade
        $ renpy.pause()

    else:
        scene bg mid with fade
        $ renpy.pause()
        scene bg mid2 with fade
        $ renpy.pause()

return
