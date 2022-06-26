    m "Hallo [player]!"
    m "Willst du ein bisschen deutsch mit mir sprechen?"
    m "Ahahaha~"
    m "I was just speaking some german right now."
    m "It's quite a complicated language..." 
    m "But it's still one of the most beautiful and lyrical languages in the world!"
    m "Would you like to learn some more about german with me, [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Would you like to learn some more about german with me, [player]?{fast}"
        
        "Of course!":
            m "That's amazing!"
            m "Well, did you know that german is an official language in six countries?"
            m "It counts as one of the major languages of the world and it's even the second most spoken native language within the European Union!"
            m "And the possibilities in phrasing and lyrical performance seem endless!"
            m "I am so excited!"
            m "Ehehehe~"
            m "I can´t wait to tell you more about german in the future!"
            m "Thanks for listening, [mas_get_player_nickname()]~!"
        
        "Not really, [m_name].":
            m "Oh, okay [player]! "
            extend "No problem!"
            m "Just let me know if you change your mind!"

        return
