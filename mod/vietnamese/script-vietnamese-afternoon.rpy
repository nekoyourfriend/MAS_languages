    m "Chào buổi trưa, [mas_get_player_nickname()]~"
    m "Oh, [player], I can’t believe it’s noon already!"
    m "Perhaps it’s about time you go get some lunch... But before any of that!"
    m "Do you need a full explanation of the phrase we just spoke, [player]?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you need a full explanation of the phrase we just spoke, [player]?{fast}"

            "Yes, please.":
                m "Alright! The full phrase itself means 'good noon'!"
                m "'Buổi' is a word used to indicate the time of the day or more broadly, some kind of event or session."
                m "Going over everything, 'Sáng' means 'morning', 'trưa' means 'noon', 'chiều' means 'afternoon' and 'tối' can be used for both evening and night."
                m "I hope that my explanations helped you understand the meaning of each word."
                m "Thank you for listening, [player]!"
                m "I love you so much."
            
            "Nope, I’m confident that I know what most of the words mean.":
                m "Is that so? Have you been studying?"
                m "That's great!"
                m "But anyway, it’s great to hear that you’re understanding the language better!" 
                extend " Keep it up, [player]~"
                m "I love you so much."
                
            "Not now, [m_name]":
                m "Ah... I see! But..."
                m "If you ever want to listen to the explanation, just let me know!"
                m "Thanks for listening, [player]!"
                m "I love you so much."
                
            return "love"

Chào buổi trưa, [player nickname]~

>> Chào buổi trưa, [monika nickname]!

Oh [player nickname], I can’t believe it’s noon already! 

Perhaps it’s about time you go get some lunch… But before any of that! 

Do you need a full explanation of the phrase we just spoke, player?

>> Yes, please.

Alright! The full phrase itself means “good noon”!

“Chào” is the basic go-to Vietnamese greeting for “hello”! 


As seen in the common “xin chào” for example.

However, “chào” is often used with a noun associated with the person you’re talking to casually.

If you’re saying “hi” to a friend, then it’ll be “chào bạn” or “chào cậu”.

Or if it’s someone slightly older, there could be gender-specific pronouns like “chào chị” or “chào anh”. 

Next, “buổi” is a word used to indicate the time of the day or more broadly, some kind of event or session.

“Sáng” means morning, “trưa” means noon, “chiều” means afternoon and “tối” can be used for both evening and night.

I hope that my explanations help you understand the meaning of each word. 

If necessary, be sure to write some definition notes down! Writing down notes is a good habit to learning a new language efficiently. 

Thanks for listening, [player]~


>> Nope, I’m confident that I know what most of the words mean.

Is that so? Have you been studying?

(Only show this part of the dialogue if she has explained one of the four phrases) Or I might’ve explained a variation of the phrase to you before already… my bad, [player nickname]!

But anyway, it’s great to hear that you’re understanding the language better! Keep it up, [player]~ 


>> Not now, Monika…

Ah… I see! But…

If you ever want to listen to the explanation, just let me know!

Thanks for listening, [player]!
