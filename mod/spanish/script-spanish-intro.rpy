    m "¡Hola, [player]! ¿Cómo estás el día de hoy?" 
    m "Ehehe, sorry, I was only speaking a bit of spanish!"
    
    m "Would you like to learn some spanish with me?{nw}"
    $ _history_list.pop()
    menu:
        m "Would you like to learn some spanish with me?{fast}"
        
        "Yes!":
            m "Wonderful!"
            m "I'm so glad you're willing to learn about languages with your charming girlfriend~"
            m "Ahahaha~!"   
            m "Before we dive into Spanish's vocabulary and syntax, we should make a first contact with this language."
            m "So, as you probably know, Spanish is a language known by foreign speakers because of its complexity and its huge load of verb tenses."
            m "And… this is actually true."
            m "While in English language there are only three basic tenses, Spanish counts with approximately 20."
            m "This, of course, is a challenge for those who are not familiarized with these types of languages."
            m "I won´t dive into all of these tenses because it would be something so tedious... that would require tons of practice and memorisation."
            m "But! We will be able to introduce the basics of this language: basic forms, vocabulary, a bit of history…"
            m "Hmmmm..."
            m "So, Spanish, apart from its complexity, is known for being the fourth most-spoken language globally!" 
            m "Around 534 millons of people speak it nowadays!"
            m "It is also the native language of books such as Don Quixote, the best-selling book of all time - coming only after The Bible!"
            m "Spanish is a roman language which derivates from Latin, which, at the same time, derivates from Indo-European, a tremendously ancient language."
            m "Indo-European remains as a mystery nowadays for languages scholars."
            m "But! Spanish has also been influenced by Ancient Greek and Arab, this due to the huge number of conquers which have taken place in the Iberian Peninsule."
            m "In addition, Christopher Colombus arrived, in the XV century, to southern America, conquered it, and expanded Spanish by consequence."
            m "Of course, all these conquers I´m talking about are all misfortunate events which ended up in millions of deaths."
            m "It is truly tragic, but we need to accept that after all, history is history, and there is no way to change that."
            m "What we know for sure is that, thanks to this, now Spanish is such a cultivated and developed language!"
            m "Oops, sorry for rambling, [player]! I hope that wasn´t too dense."
            m "Anyway, I think we'll leave the subject here. Wait for Monika's next Spanish tip of the day!"
            m "Ehehehe~"
            m "Thanks for listening, [mas_get_player_nickname()]~!”

        "Not really, [m_name].":
            m "Oh, okay [player]! 
            extend "No problem!"
            m "Just let me know if you change your mind!"

        return
