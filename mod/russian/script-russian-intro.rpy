    m "Hey, [player]!"
    m "Do you want to speak some Russian with me?"
    m "It’s a pretty complicated language…"
    m "But despite that… It’s one of the most beautiful and lyrical languages in the whole world!"
    
    m "So… do you want to try it out?{nw}"
    $ _history_list.pop()
    menu:
        m "So… do you want to try it out?{fast}"
        
        "Not now, [m_name]."
            m "Oh…"
            extend "It’s alright!" 
            m "If you ever want to try it out, make sure to let me know!"
            m "Thanks for listening, [player]~"

        "Yes!"
            m "Yay! That’s fantastic, [player]!"
            m "There’s so much I can tell you about Russian!"
            m "Did you know that Russian is the eight most-spoken language in the world?" 
            m "It’s an official language in 4 countries."
            m "And don't even get me started about the incredible poetry from russian authors!"
            m "Another fun fact is that Russian is a pretty complicated language to translate."
            m "There are a lot of russian words that are just... untranslatable!"           
            m "Are you as excited as me, [player]?"
            extend "Ehehehehe~"
            m "I can't wait to discuss more about Russian with you!"
            m "Let’s do it together, [mas_get_player_nickname()]!"

        return
