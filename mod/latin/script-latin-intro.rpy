    m "{i}~Arma uirumque cano, Troiae qui primus ab oris,~{/i}"
    m "{i}~Italiam, fato profugus, Lauiniaque uenit,~{/i}"
    m "{i}~Litora, multum ille et terris iactatus et alto,~{/i}"
    m "{i}~Ui superum saeuae memorem Iunonis ob iram...~{/i}"
    m "Oh? You didn't understand? " 
    extend "Hehehe, or maybe you did... I was reciting the first verses of Virgilio's Aeneid!"
    m "Latin is truly a wonderful language, isnt it?"
    m "Born from ancient culture and mother of roman languages..."
    
    m "Would you like to hear a little more about it?{nw}"
    $ _history_list.pop()
    menu:
        m "Would you like to hear a little more about it?{fast}"
        
        "Not now, [m_name]."
            m "Oh…"
            extend "It’s alright!" 
            m "If you ever want to try it out, make sure to let me know!"
            m "Thanks for listening, [player]~"

        "Yes!"
            m "Great! I'm delighted to know you're willing to learn something new apud amica tua, ehehe~"
            m "Let’s do it together, [mas_get_player_nickname()]!"
            #write more here

        return
