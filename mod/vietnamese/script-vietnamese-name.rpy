    m "Hey, [player]...!"
    m "I'm going to demonstrate how to introduce your name and ask for others' names in Vietnamese."
    m "Let’s start..."
    m "Xin chào! Tên cậu là gì?{nw}"
    $ _history_list.pop()
    menu:
        m "Xin chào! Tên cậu là gì?{fast}"
        
        "Tên tớ là [player].":
        m "Rất vui được gặp cậu, [player]!{nw}"
        $ _history_list.pop()
        menu:
            m "Rất vui được gặp cậu, [player]!{fast}"
            
            "Tên của cậu là gì?":
            m "Tớ tên là Monika!"
            m "..."
            m "Great job, [mas_get_player_nickname()]!"
            m "If you can tell by the cues, the first question I asked was for your name, same for the second question you asked. "
            m "Your answer to my first question was the introduction of your name. It’s quite simple!"
            m "Thanks for listening to my demonstration, [player]~"
