    m "Salut, [player]!"
    m "Comment ça va?"
    m "Ahahaha~ "
    extend "I was just speaking some french, [mas_get_player_nickname()]."
    m "Isn't it such a beautiful language? Ehehehe~"
    m "What do you think, [player]?"
    m "Would you like to learn some french with me?{nw}"
    $ _history_list.pop()
    menu:
        m "Would you like to learn some french with me?{fast}"
        
        "Yes!":
            m "Yay! That's wonderful!"
            m "Did you know French is a Romance language of the Indo-European family?"
            m "It descended from the Vulgar Latin of the Roman Empire, as did all Romance languages!"
            m "French evolved from Gallo-Romance, the Latin spoken in Gaul, and more specifically in Northern Gaul."
            m "Many people consider it the most romantic of languages, and seek to learn how to speak it because of that."
            #write more here
            m ""
            m "Wait for Monika's next French tip of the day!"
            m "Ehehehe~"
            m "Thanks for listening, [mas_get_player_nickname()]~!”
            
        "Not now, [m_name].":
            m "Oh, okay [player]! "
            extend "No problem!"
            m "Just let me know if you change your mind!"
