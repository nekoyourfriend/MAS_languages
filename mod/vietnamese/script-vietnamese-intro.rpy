    m "Hey, [player]?"
    m "I was thinking of maybe teaching you some Vietnamese..."
    m "It has a Latin-based alphabet but it's actually quite difficult to speak..."
    m "Due to its expressive six tones which makes it a very tonal and melodic language!" 
    
    m "So, do you wanna try it out?{nw}"
    $ _history_list.pop()
    menu:
        m "So, do you wanna try it out?{fast}"
        
        "Of course, [m_name]!":
        m "That's the spirit, [mas_get_player_nickname()]!"
        m "So, starting the first lesson with a fun fact..."
        m "Did you know that the Vietnamese language is heavily influenced by some other languages like French and Chinese?"
        m "It's actually stemmed from history! That's why there's so many different cultural similarities too."
        m "The Vietnamese alphabet is very similar to English too, but there's 29 characters which may include special tonal letters, "
        extend "but it also removed letters like F, J, W, and Z!"
        m "Plus, the tones of a letter can also change a word's meaning completely!"        
        m "Take the word 'ma' for example, which means 'ghost'."
        m "If the tone of 'a' is changed to 'á', a sharp tone, then it becomes 'má', which means 'cheek' or 'mother'."
        m "But if 'a' is changed to a deep tone, then the word becomes 'mà', which means 'but'."
        m "There’s also the questioning and tumbling tones which often gets mistaken with each other, take 'mả' and 'mã' for example."
        m "They sound very similar to each other, but the first one means 'grave' and the latter means 'horse'!"
        m "And then there’s the heavy tone, which makes the word 'mạ', which means 'rice seedling'!" 
        m "It sure is a complicated but fun language detail to learn!"
        m "Oh!" 
        extend "[player], I’m sorry if I spilled too much information for you to digest for now." 
        m "It’s just that I can’t contain the excitement of teaching you a new language!"
        m "Ehehehe~"
        m "Welp... Be sure to stay tuned for Monika’s next Vietnamese tip of the day!"
        m "I can’t wait to discuss more about this beautiful language with you, [mas_get_player_nickname()]~"

        "Not now.":
        m "Ah... I see!"
        m "But... "
        m "If you ever happen to change your mind, just let me know!"
        m "Thanks for listening, [player]~"
        
        return
