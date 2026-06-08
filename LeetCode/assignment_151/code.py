def reverse_words(s): 
    s_split_space = s.split(" ")
    new_s = []
    for word in s_split_space: 
        if word != "": 
            new_s.insert(0, word)
    return " ".join(new_s)
