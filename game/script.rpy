define slowfade = Fade(1.0, 0, 1.0)
define slowerfade = Fade(3.0, 0, 3.0)
define slowdissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)
init:
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)

define m = Character ("Me")
define l = Character ("Lars")
define s = Character ("Shira")
define g = Character ("Guy at the bar")
define ho = Character ("Hong")
define h = Character ("H")
define d = Character ("Director Shinya")
define gu = Character ("Guy with camera")
define gi = Character ("Girl on the bus")
define e = Character ("Emma")

label start:
    $ save_name = "Introduction"
    $ sad_points = 0
    $ ing_points = 0
    $ irr_points = 0
    $ aro_points = 0
    $ gen_points = 0
    $ drink = 0
    $ drunk_yes = False
    $ drunk_no = False
    $ guy = 0
    $ guy_aro = False
    $ guy_ind = False
    $ guy_dis = False
    $ guy_hap = False
    $ guy_sad = False
    $ guy_help = False
    $ guy_nhelp = False
    stop music fadeout (1.0)

    scene shira0_0
    with slowfade
    play music "bar_bgm.ogg" fadein (2.0)
    "Shira is waiting for me at the table, looking distractedly through the crowd of costumers."
    s "It took you so much for just smoking a cigarette! You know, it's not so gentle to keep a friend waiting for so long."
    scene shira0_1
    with slowdissolve
    m "I'm sorry, I just didn't notice."
    s "You don't say...Well, we were talking about him, right?"
    m "Yes..."
    s "So, how are things going between you two?"
    m "Hmm, fine."
    s "Fine? Are you sure?"
    m "Yes, why shouldn't I?"
    scene shira0_02
    with dissolve
    s "You always say he does nothing more than just care about his work, about his writings, but where does he ends up? Does he accomplish something with those?"
    m "What?"
    s "Just answer me, has he accomplished something, yet?"
    menu:
        "He's still at the beginning...":
            $ ing_points += 1
            jump beginning

        "Are you saying he's only a wannabe?":
            $  irr_points += 2
            jump wannabe

## Ingenuous
label beginning:
    scene shiraa_1
    with dissolve
    s """
    Still at the beginning? Listen, I understand you are in love with him, but don't you think that's a bit overstated?

    We both know how he treats you, and his manners aren't good. At all.
    """
    m "I know, but you make it sound as if he doesn't do anything and that's not true. I would understand if he'd just lay in the house all day, but-"
    s "Then look at me in the eyes and tell me, is it worth it? To wait for his brilliant moment of success and continue suffering?"
    menu:
        "I don't know...maybe...maybe not.":
            $ sad_points += 2
            jump opinion

        "That's enough. You're missing the point!":
            $ irr_points += 3
            jump opinion

## Irritated
label wannabe:
    scene shiraa_2
    with dissolve
    s """
    And what is him, then? A pro? An artist?

    To me, it seems that he's only joking with you, living the easy life he wants, while you're here, in this depressed state...

    Don't you understand how unfair that is?
    """
    m "But what do you know about him? You've barely talked to him a couple times. He's not even a lazy guy as you describe it, he's trying his best."
    s "Well, if he's trying his best why are you here with me every week, sighing and sobbing all evening? And tell me, are you two even having some physical contact, lately?"
    menu:
        "That...that's none of your business...":
            $ sad_points += 2
            jump opinion

        "About that, I'm afraid we're pretty...distant.":
            $ aro_points += 3
            jump opinion

label opinion:
    if ing_points >= 1 and sad_points >= 2:
        scene shirab_2
        with dissolve
        "She looks at me with worried eyes. Eyes in which an entire ocean seems to flow, projecting its water towards me."
        s "I know, it's difficult, yet you have to go on, to get through this."
        m "But how? I don't even know what I'm feeling, now."
        "She holds my hand, which has started to tremble."
        s "Don't worry, you're not alone. I'm right here, with you."
        jump proposal

    elif ing_points >= 1 and irr_points >= 3:
        scene shirab_1
        with dissolve
        s "Missing the point? And what should it be then, this so called 'missing point'?"
        m """
        Do you think you can understand me completely? That you're so intelligent and sensible to understand the whole problem and solve it?

        Well, if you think that, then you're completely failing.
        """
        s "To think I wanted to help you...How can you do it? How can you still defend him like that? After all this..."
        m "All this? What are you even talking about?"
        s """
        You even ask what I'm talking about?

        I'm talking about the way you continue to escape from the problem.
        """
        scene shiragoes
        with dissolve
        s "You know what? I'm tired. I'm going home."
        m "What? Hey, wait...!"
        "Without listening to me, she goes away, leaving mealone."
        jump goes_away

    elif irr_points >= 2 and aro_points >= 3:
        scene shirab_3
        with dissolve
        s "Distant? How much?"
        m "Pretty...pretty much distant."
        s "I can't understand how you're able to endure such torture."
        m "I don't know either. It's just like that."
        jump proposal

    ## Angry and disappointed from her passage -- Derives from 'not your business'
    elif irr_points >= 2 and sad_points >= 2:
        scene shirab_2
        with dissolve
        s "If you want my help then it's my business too."
        m """
        Your help...? And when did I asked for that? You always ask me about him and start saying what you think I should do, only because we are friends.

        I never asked for your help.
        """
        s "You never...?"
        m "No, I didn't. I don't want your help, if it's only talking about what I should do and how I should feel."
        "A pause of silence between us, strong as a thunder striking the earth."
        scene sofiagoes
        with dissolve
        m "I...I'm going home, bye."
        s "Wait, can't we talk about this? Come on, we're both exaggerating!"
        "I don't answer. I just take my coat and get up."
        s "I'm sorry, Sofia, don't go..."
        $ irr_points += 3
        stop music fadeout (2.0)
        jump street

label proposal:
    show prop0_1:
        xalign 0.0
    with dissolve

    if ing_points >= 1 and sad_points >= 2:
        s "Listen, I may have a proposal for you."
        m "Of what kind?"
        s "Why don't you just relax, for tonight? You know, detach yourself from him and from all your problems and have some fun."
        m "Ok, but...how?"
        s "Oh, you really never understand! Look, do you see that guy? The one near the counter, alone."
        show prop0_1:
            subpixel True
            xalign 0.0
            linear 3.0 xalign 1.0
        $ renpy.pause(3.5)
        "She points a man, older than me and lonely."
        m "Uhm, yes."
        s "He's been watching you since we arrived, why don't you go there and talk with him?"
        m "But...what about..."
        show prop0_1:
            subpixel True
            xalign 1.0
            linear 3.5 xalign 0.0
        $ renpy.pause(3.5)
        s "Oh, come on! You're not married, aren't you? And it wouldn't surprise me if your dear boy has already had different relationships with other people."
        m "Don't you think you could've spare this one?"
        s "Oh, I'm sorry, but you have to wake up from your dream of perfection and tenderness a little. And you could start doing so by talking with that guy."
        menu:
            ##Ingenuous don't feel like it passage
            "I don't really feel like it, sorry.":
                $ irr_points += 3
                jump go_away

            ## Ingenuous worth a try passage
            "Well...it's worth a try, I guess.":
                $ aro_points += 4
                jump guy_conversation

    elif irr_points >= 2 and aro_points >= 3:
        s "Well, that surely isn't a good thing and I'm sure you know that."
        m """
        Of course I do. And I'm tired of it. You know, you may pass even years waiting for someone to love you and be with you.

        And then, when you finally find that someone, he doesn't even stays with you at night one time in months...
        """
        s "Hmm, I can only imagine how difficult that is."
        "She seems to think for some seconds, looking around her in search of something."
        s "Hey, look!"
        m "Where?"
        s "Over there, by the counter. Do you see him? He's been watching you all the time, you know?"
        show prop0_1:
            subpixel True
            xalign 0.0
            linear 3.0 xalign 1.0
        $ renpy.pause(3.5)
        m "And then?"
        s "What do you mean by 'and then'? Isn't it obvious what I mean?"
        m "Are you saying I should go with that guy?"
        s "Why not?"
        show prop0_1:
            subpixel True
            xalign 1.0
            linear 3.5 xalign 0.0
        $ renpy.pause(3.5)
        m "I'm engaged, you know?"
        s "Engaged, not married. Come on, what's the matter? If your lover-boy doesn't even watch you anymore..."
        menu:
            ## Angry not a good idea passage
            "No, it absolutely isn't a good idea.":
                $ irr_points += 2
                jump go_away

            ## Angry deserve distraction passage
            "You know what? I think I deserve some distraction.":
                $ aro_points += 5
                $ irr_points += 3
                jump guy_conversation

label goes_away:
    scene prop0_2:
        xalign 0.0
    with dissolve
    """
    I stay still for some seconds, before realizing she really has gone away.

    A wind of sadness suddenly catch me.

    Watching all the couples and groups of friends that surround me, I feel a deep loneliness.

    Why am I not like them? Why am I so alone?
    """
    show prop0_2:
        subpixel True
        xalign .0
        linear 3.5 xalign 1.0
    $ renpy.pause(3.5)
    "As my mind struggles to free itself from all these thoughts, my eyes catch, in the distance, a lonely man."
    menu:
        ## Sad approach him passage
        "Maybe I could approach him...":
            $ aro_points += 2
            $ sad_points += 2
            jump guy_conversation

        ## Left alone and go away passage
        "It's time I go away too. That's better.":
            $ sad_points += 4
            $ ing_points += 2
            stop music fadeout (2.0)
            jump street

label go_away:
    ## From Angry not a good idea passage - Proposal label
    if irr_points >= 4 and aro_points >= 3:
        s "Well, do what you want, then. Mine was only a suggestion."
        m "Don't tell me you got offended."
        s "No, I just don't care. It's your own business. All I know is that you, after all, don't want to find a solution to your problem or even feel better."
        m "How am I supposed to feel better by just sleeping with some stranger?"
        s "It was just an idea. After all, you just said that you two are distant, so-"
        m "And does it means that I should sleep with someone else to solve my problems?"
        "She watches me, shocked and speechless. You don't pay too much attention at the tears hung at her eyes."
        m "Only because I told you we're distant, it doesn't mean I'd go with the first man I see. Is that what sex is for you? Just a way to kill time?"
        s "I'm sorry, I didn't thought-"
        scene sofiagoes
        with dissolve
        m "Well, I don't care. I'm going now, bye."
        "I leave the bar, finding myself in the lonely street."
        $ irr_points += 1
        stop music fadeout (2.0)
        jump street

    ## From Ingenuous don't feel like it passage - Proposal label
    elif ing_points >= 1 and sad_points >= 2 and irr_points >= 3:
        s "You 'don't feel like it'. Fine, do what you want. Continue being a coward, then."
        m "A coward?"
        s "Yes, that's what you are. You keep loving and suffering for a man who doesn't give a shit about you."
        m "What are you-"
        s "You see? You continue playing dumb. Just stop it already, it's unnerving."
        m "But I'm not! I just don't understand you."
        s """
        What is it that you don't understand? You don't want to solve your problem as well as you don't have the courage to detach yourself from it.

        You prefer to be stuck in a limbo, without doing anything. That's what a coward is.
        """
        scene sofiagoes
        with dissolve
        m "Ok, I understand...well, I think it's time to go. Sorry. I'll call you."
        "While leaving the bar, I don't realise that tears are slowly falling along my cheeks."
        $ sad_points += 1
        stop music fadeout (2.0)
        jump street

label guy_conversation:
    ## From Angry deserve distraction passage - Proposal label
    if irr_points >= 5 and aro_points >= 8:
        """
        Before getting up I empty my glass in one sip, closing my eyes for how strong the alcohol is.

        I then get up, smiling back at Shira and turning myself toward the guy, determined to approach him.
        """
        scene hong0_3:
            xalign 1.0
        with slowdissolve
        m "Hey there."
        "He turns at me, shily smiling."
        g "Uhm...hi. Do we know each other?"
        m "Only by sight, I suppose. Can I sit here?"
        g "Of course, go on. By sight, you say?"
        m "Well, my friend over there said you've been watching me since we arrived. Is it true, or...?"
        "His face is embarassed."
        g "Let's say it...it might be true. I just didn't expect for you to come here and talk to me."
        m "I can be surprising. "
        g "You sure can be. So, are you here for a particular reason or just to spend time?"
        menu:
            ## Sad - certain situation
            "To forget a certain situation.":
                $ sad_points += 2
                jump conversation_why

            ## Aroused - have fun
            "I came with my friend to have some...fun.":
                $ drunk_yes = True
                $ aro_points += 2
                jump conversation_why

            ## Gentle - just to drink
            "Just to drink something, you know.":
                $ drunk_yes = True
                $ gen_points += 2
                jump conversation_why

    ## From Ingenuous worth a try passage - Proposal label
    elif ing_points >= 1 and sad_points >= 2 and aro_points >= 4:
        s "Come on, then, just go and talk to him!"
        m "Yes, just...just one moment."
        "I slowly empty the glass, with little sips, before getting up and reach him."
        scene hong0_3:
            xalign 1.0
        with slowdissolve
        m "Hi there..."
        "I try to show myself convincing and happy, but I end up losing myself to embarassment."
        g "Hi!"
        m "Is there someone sit here?"
        g "Oh no, not at all. But...I guess we don't actually know each other, don't we?"
        menu:
            "Lie.":
                m "Well, I guess we do! But truth is, I just remember your face and nothing more..."
                g "Damn, I just can't remember...and that's strange."
                m "It's strange?"
                g "Yes, it would be very difficult to forget someone...like you."
            "Say the truth.":
                m "To be completely sincere, a friend of mine convinced me to come speak to you, saying that you've been watching me for the whole evening..."
                g "Well, I can't say your friend isn't correct about that. I'm sorry if I've been staring so much."
                m "No, don't worry. It's just that it doesn't happen so much, you know."
                g "Really?"
                m "Yes, really."
                g "That's something truly surprising, you seem a very...interesting person."
        g "Anyway, is this the first time you come here?"
        menu:
            ## Sad - don't like to drink
            "I'm not really the person who likes to drink, but...":
                $ drunk_no = True
                $ sad_points += 2
                jump conversation_why

            ## Aroused - distract myself
            "First time, it's just to find someone to talk to.":
                $ aro_points += 2
                $ ing_points += 2
                jump conversation_why

            ## Ingenuous - came with friend
            "Sometimes I come here to drink with a friend.":
                $ drunk_yes = True
                $ ing_points += 3
                jump conversation_why

    ## From Sad approach him passage - Goes away label
    elif ing_points >= 1 and irr_points >= 3 and aro_points >= 2 and sad_points >= 2:
        show prop0_2:
            subpixel True
            xalign 1.0
            linear 3.5 xalign 0.0
        $ renpy.pause(3.5)
        "I slowly empty my glass, before getting up and sit next to him, trying to figure out what to say."
        scene hong0_3:
            xalign 1.0
        with slowdissolve
        $ renpy.pause(1.2)
        m "Uhm...hi."
        g "Oh, hi."
        "I soon realize I don't know what to say and look at him embarassed as he doesn't understand why I'm talking to him"
        g "Are you alone too?"
        m "I was here with a friend, but she has left."
        g "Oh, I'm sorry...well, I guess that makes two of us who's been left here alone."
        m "Someone left you too?"
        g "Let's say so."
        "He empties his glass."
        g "Why did you come here, before being left alone?"
        menu:
            ## Sad - talk with friend
            "I often come here with this friend, but...":
                $ sad_points += 2
                jump conversation_why

            ## Aroused - meet people
            "I just wanted to meet new people, i guess.":
                $ aro_points += 2
                $ ing_points += 2
                jump conversation_why

            ## Ingenuous - get drunk
            "Let's say I only want to get drunk.":
                $ drunk_yes = True
                $ ing_points += 3
                jump conversation_why

label conversation_why:
    ## GUY CONVERSATION - AROUSED ROUTE (SOFIA IS EXCITED)
    if irr_points >= 5 and aro_points >= 8 and sad_points >= 2:
        g "A certain situation? Do you want to talk about it?"
        menu:
            "It's just a difficult period.":
                g "Oh, I understand. Well, I can only imagine how difficult it can be."
            "I prefer not, sorry.":
                g "Don't worry, it's ok."
        g "Well, I'm very sorry..."
        m "Sorry? About what?"
        g "About your situation. I hope it's not...uhmm...something sombre?"
        m "To be sincere I don't really know. Sometimes it is, sometimes it's not."
    elif irr_points >= 5 and aro_points >= 10:
        g "I guess this makes us similar. I came hoping to have fun too."
        m "And are you?"
        g "Before you came not really, now...maybe."
    elif irr_points >= 5 and aro_points >= 8 and gen_points >= 2:
        g "So you came here to get drunk?"
        m "Well, who knows. I think that everything can happen, tonight! Don't you think so too?"
        g "Guess you're right. Besides, it's a bar, so we might as well drink."

    ## GUY CONVERSATION - INGENUOUS ROUTE (SOFIA IS EMBARASSED)
    if ing_points >= 1 and sad_points >= 4 and aro_points >= 4:
        g """
        Well, I don't think that's a problem.

        if you don't feel like drinking too much we can avoid drinking at all.
        """
        m "Yeah, thanks."
    elif ing_points >= 3 and sad_points >= 2 and aro_points >= 6:
        g "And...have you found that someone you are looking for?"
        m "Who knows, maybe I did. There's an entire night to discover it."
        g "Guess you're right. Nights are pretty long in here, too."
    elif ing_points >= 4 and sad_points >= 2 and aro_points >= 4:
        g "That makes two of us, although I ended up completely alone."
        m "Completely alone? Why?"
        g "My friend never showed up, and I've been waiting for two hours."
        m "That really isn't nice. But you're not so alone, now."
        g "Yeah, you're right."

    ## GUY CONVERSATION - SAD ROUTE (SOFIA IS ALONE)
    elif ing_points >= 1 and irr_points >= 3 and aro_points >= 2 and sad_points >=4:
        g "But?"
        m "Well, today the conversation wasn't nice at all and...she left me here."
        g "Yeah, I can totally understand. I've been waiting for two hours for my friend but, as you can se, I'm alone here."
        m "Let's forget them, then!"
        g "Absolutely, let's drink instead!"
    elif ing_points >= 3 and irr_points >= 3 and aro_points >= 4 and sad_points >= 2:
        g "And that's why you approached me?"
        m "I guess you could say that."
        "He seems to notice immediately my ambarassment and he smiles."
        g "Let's drink something together, then, as we're both alone tonight!"
    elif ing_points >= 3 and irr_points >= 3 and aro_points >= 2 and sad_points >= 2:
        g "You know what? I've been waiting for a friend for two hours. Fuck friends, let's just drink for the entire night."
        m "I totally agree, I'm happy to have met someone like you."
        g "I'm happy too!"

    "We both order something to drink, before going on with the conversation."
    stop music fadeout (2)
    show black
    with fadehold
    return

label street:
    scene backg_3:
        xalign 0
    with slowfade
    play music "rain_bgm.ogg" fadein (2.0)
    ## From Angry and disappointed from her passage - Opinion label
    if irr_points >= 5 and sad_points >= 2:
        """
        I watch the buildings surrounding me, trying to figure out what to do with the few hours that separate me from the first lights of the morning.

        The neon lights of the bars are still on, filling the streets with strong colours but no one's around. Not even a single person, only rain.

        As I imagine my left hand drawing all these empty spaces I walk, without even thinking where I'm going as the rage seems to fly away.
        """

    ## From Left alone and go away passage - Goes away label
    elif ing_points >= 3 and irr_points >= 3 and sad_points >= 4:
        """
        I'm not in the mood to stay in the bar anymore.

        The air and soft sound of rain falling on the street seems to gently calm me, blowing away at least some of the pain and sadness I'm feeling.

        But not everything. Some traces remains, stuck in my heart.
        """

    ## From Ingenuous don't feel like it passage - Proposal label
    elif ing_points >= 1 and sad_points >= 3 and irr_points >= 3:
        """
        The more I try to sweep away all the tears, the more convinced they seem to line my face.

        In the distance, high in the sky, the moon is coldly observing me and all the streets seem empty, although every bar is still open.

        I start to walk, holding myself in the coat and sobbing.
        """

    ## From Angry not a good idea passage - proposal/go away passage
    elif irr_points >= 5 and aro_points >= 3:
        """
        Thinking about it, a part of me feels a little guilty.

        Was it alright to talk to her like that? Did I lost myself to anger?

        But as soon as I think about it, that anger returns, convincing me she's just a selfish person.

        Through the streets there's nobody, only the silent rain.
        """

    ## Cinema addicted passage in Guy conversation - Conversation_name passage
    elif me = "cinema addicted":
        """
        So it goes again, my usual addiction to cinema made me alone.

        Nothing new, after all.

        Every time, though, I find it difficult to understand what my problem is.

        Why am I incapable of act normally with someone?

        Maybe...just maybe, it's the fact that I care too much about what I love.

        And that ruins everything, always.

        I watch the street in front of me. The rain strongly falls and, strangely, there are few people around.
        """

    scene backg_3:
        subpixel True
        xalign .0
        linear 3.5 xalign 1.0
    $ renpy.pause(3.5)

    """
    I should head back home, I know that very well.

    Yet, doubt tempts me.

    Go away would be the most simple solution, to just distance myself from him.

    Maybe I could just wander through the streets until the sun sets and watch the dawn's colours conquering the sky.

    Or, maybe, I could find a new place to live in. Abandon everything and start a different life, even for a few time.

    But if I go back, would it be so bad? Perhaps he'll notice me, this time.

    Or I could just talk to him, to make things clear.
    """
    menu:
        "Just go home.":
            $ irr_points += 2
            $ sad_points += 2
            """
            Hmm, maybe it's time to face these problems we have.

            What could I lose, after all?

            It's worth at least trying. And besides...I must admit I miss him a little, even if I still am pissed off.
            """
            jump home
        "Going back to him would be a mistake.":
            $ sad_points += 3
            """
            It definately would be an error.

            After all, I know how poisonous he's for me. It doesn't matter how much I try, there's no use in faking it.

            It's way better to stay alone, at least for a while, in these rainy streets than go home.
            """
            jump street2

label home:
    scene black
    with slowfade
    if irr_points >= 6:
        """
        As I reach home, I feel I'm getting more and more angry at each step.

        What am I gonna say to him?

        What is he gonna do?

        I reach the door and stop in front of it.

        A deep breath, and then I decide to open it.
        """
    elif sad_points >= 5:
        """
        I feel bad. Truly bad.

        The more I reach the place we live in, the more I feel as if I'm suffocating.

        The door now is only few steps ahead.

        I open it and enter.
        """
    scene black
    with slowfade
    return

label street2:
    """
    I keep on walking, then, with no clue on my direction.

    Walk, until few people start appearing around me on the street.

    I take a detour, finding myself in loneliness once again. The rain on my head feels light. It's pleasant.

    At some point, I see a train station in the distance.

    A train that will take them away from the city. A line directed towards the sea, maybe...

    It wouldn't be that bad to disappear for some time...
    """
    menu:
        "Maybe I could take it...":
            """
            Why not, after all?

            If I'm here it's because I want to escape from this life, so I should at least try to.

            Even if it's not for the whole rest of my life, even if it's for some hours, weeks or years, it would be worth it.

            """
            jump train
            stop music fadeout (2.0)
        "No, it definately is a bad idea.":
            """
            I go on through the street, ignoring the station.

            Rain seems to grow a little stronger, as I turn in a little alley.
            """
            jump director

label director:
    show backg_4
    with dissolve
    """
    As I enter the alley, I instantly feel observed by someone.

    In front of me there is only a faint darkness, so I turn back, facing a man who holds a camera.
    """
    gu "No, please, go on! Continue to walk, that was perfect! You are the perfect actress!"
    menu:
        "Oh...thanks, I guess.":
            $ gen_points += 2
            gu "It's only the truth! But now go on, continue!"
            stop music fadeout (2)
            show black
            with fadehold
            return
        "What the...hell are you doing?":
            $ irr_points += 2
            gu "Uhm, making a movie...and as soon as I saw you, I was sure you were the perfect actress for it!"
            if irr_points == 7:
                m "I don't care about that crap. You should ask before doing that, you know?"
                "He looks at me surprised. A thin disappointment is mixed with sadness on his face, now."
            elif sad_points >= 6:
                m "Sorry but...I really am not in the mood, right now."
                "He seems embarassed as he bows to me, trying to excuse himself."
            else:
                m "Well, don't you think it would be better to ask for my authorisation, first?"
                gu "That's true. I'm sorry, but...I was so caught! It was as if I found the perfect shot, do you understand?"
                "I can't say I can understand completely, but I get what he means..."
            stop music fadeout (2)
            show black
            with fadehold
            return

label train:
    stop music
    show backg_22
    with slowfade
    play music "station_bgm.ogg" fadein (2.0)
    """
    On the departures board there's one train directed to Tottori.

    The image of it's dunes and the vast ocean fixes in my mind.

    I've never been in Tottori. I've only seen it in photos.

    One in particular: an old photo of the comic artist I work for, posted near his desk.

    I rapidly buy the ticket and head to the track #3.
    """
    show backg_21
    with slowfade
    play music "train_bgm.ogg" fadein (2.0)
    """
    I feel like I could fall asleep.

    The train's sounds hold me gently, as I watch outside the window.

    Landscapes passing by, rushing before me.

    A soft cry, right next to me, starts to draw my attention.

    A cute girl is crying. She tries to be as silent as pissible.

    The result, though, is a long sequence of sighs impossible to not being listened.
    """
    menu:
        "Hey, are you ok?":
            "She turns to me, watching me in the eyes."
            gi "I guess I'm not, but...I don't really wanna talk about it, sorry."
            m "Oh don't worry, I understand."
            gi "Sorry, Im so pathetic..."
            """
            Her eyes are red and full of tears.

            A thin rivulet slips above her cheek, as her thoughts seem to go give up again to sadness.
            """
            if sad_points >= 6:
                """
                That sadness resonates within me, as if it's my own.

                Or as if we are sharing it, our precious and beautiful treasure.
                """
                stop music fadeout (2)
                show black
                with fadehold
                return
            elif ing_points >= 3:
                """
                I feel sorry to not completely understand her.

                I would like to say something, to cheer her up, but what can I say?

                Maybe...
                """
                stop music fadeout (2)
                show black
                with fadehold
                return
            else:
                """
                It's so sad to see such a beautiful girl in this condition.

                What could have ever happened to her?

                What is it that makes her suffer like that?

                Yet, somehow, I feel very close to her.
                """
                stop music fadeout (2)
                show black
                with fadehold
                return
        "Uhm...do you want a...candy?":
            "She looks at me, surprised but smiling."
            gi "Oh, thanks. You're the first gentle person I've met tonight."
            m "Don't worry, it's just a pleasure."
            gi "I'm sorry. I bet it's not so enjoyable to travel alongside someone so sad."
            if sad_points >= 6:
                """
                Someone so sad, she says. Yet, I'm as sad as her, probably.

                The only difference is that I'm not as capable of crying out my feelings as she is.

                But I feel a...connection, between us. And that surprises me.
                """
                stop music fadeout (2)
                show black
                with fadehold
                return
            else:
                """
                She doesn't even look at me.

                She just stares at her feet, unwrapping the candy before eating it.

                It's so obvious that she feels totally useless, maybe even pathetic.

                What could make someone feel like that, I wonder...
                """
                stop music fadeout (2)
                show black
                with fadehold
                return
        "It's better to mind my own business.":
            """
            For now, all I need is to be calm, nothing more and nothing less.

            To peek into someone else's problems would be only a mistake.

            After all, I already have my share of thoughts and problems.
            """
            stop music fadeout (2)
            show black
            with fadehold
            return

## return
