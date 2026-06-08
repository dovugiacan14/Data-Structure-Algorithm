def lengthOfLastWord(s):
    word_split = s.split(" ")   # split by space 
    word_lst = [x for x in word_split if x!= ""]
    return len(word_lst[-1])
