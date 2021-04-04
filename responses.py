import moviedatabase as m


def sample_responses(input_text):
    user_message = str(input_text).lower()   # making the input into lower case

    if user_message in ("hey", "hello", "hi"):
        return "Hey! My name is MovBot! How are you?"

    if user_message in ("I am fine,thank you!", "great", "good", "fine"):
        return "great to hear that, how can i help you?"

    if user_message in ("thank you", "thanks"):
        return "Your Welcome! Happy to help :)"

    if user_message in ("bye", "good bye"):
        return "Bye! Happy to help :)"

    if user_message in ("movie", "i need a movie", "give me a movie", "suggest me a movie"):
        return "Choose a language:TELUGU/HINDI/ENGLISH"

    if user_message in ("telugu", "t"):
        return "Choose a genre:Comedy-c1/Action-a1/Romance-r1/Thriller-t1(Please type the code beside the genre!)"

    if user_message in ("hindi", "h"):
        return "Choose a genre:Comedy-c2/Action-a2/Romance-r2/Thriller-t2(Please type the code beside the genre!)"

    if user_message in ("english", "e"):
        return "Choose a genre:Comedy-c3/Action-a3/Romance-r3/Thriller-t3/Animated-k"

    if user_message in "c1":
        return m.t_c
    if user_message in "c2":
        return m.h_c
    if user_message in "c3":
        return m.e_c
    if user_message in "a1":
        return m.t_a
    if user_message in "a2":
        return m.h_a
    if user_message in "a3":
        return m.h_a
    if user_message in "r1":
        return m.t_r
    if user_message in "r2":
        return m.h_r
    if user_message in "r3":
        return m.e_r
    if user_message in "t1":
        return m.t_h
    if user_message in "t2":
        return m.h_h
    if user_message in "t3":
        return m.e_h
    if user_message in "k":
        return m.e_k

    return "I am sorry, I don't understand, Please type the correct command"
