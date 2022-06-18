    m "Hey, [player]!"
    m "Do you want to speak some Greek with me?"
    m "I'm sure you already know this, but aside from Greek being the offical language for Greece..."
    m "It is also one of the twenty-four official languages in the European Union!"
    m "It might be a little complicated, since it has differences in it's alphabet, comparing to the other languages."
    m "However [player], I'm pretty sure you would be well acquainted for a majority of the letters, if you ever taken any higher level math class!"
    
    m "So? Would you like to learn with me?{nw}" 
    $ _history_list.pop()
    menu:
        m "So? Would you like to learn with me?{fast}"
        
        "Not now, [m_name].":
            m "Oh…"
            extend "It’s alright!" 
            m "Maybe some other time then."
            m "If you ever want to try it out, make sure to let me know!"
            m "Thanks for listening, [player]~"

        "Yes!":
            m "That's wonderful, [player]!"
            m "I was honestly hoping you would say that!"
            m "I'm so excited! There's so much to say about Greece."
            m "Much of the early greek culture revolved around literature, art, and music!"
            m "Greece is well known for their contributions to theatre."
            m "Early plays like those of Sophocles! He is one of three greek play writers whose works are still really well known!"
            m "Although, the plays in Greece are often filled with tragedy..."
            m "Anyway! In fact, without the knowledge brought from Ancient Greece, it is likely that the Renaissance would've never happened!"
            m "The ancient had a very well-rounded civilization, so much so, that many of their works are still idolized today!"
            m "However, these history lessons can wait for another time, hehe~"
            extend "Let’s do it together, [mas_get_player_nickname()]!"

        return
