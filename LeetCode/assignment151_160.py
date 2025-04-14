"""Assignment 151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Example 1:
    - Input: s = "the sky is blue"
    - Output: "blue is sky the"

Example 2:
    - Input: s = "a good   example"
    - Output: "example good a"
"""
def reverse_words(s): 
    s_split_space = s.split(" ")
    new_s = []
    for word in s_split_space: 
        if word != "": 
            new_s.insert(0, word)
    return " ".join(new_s)