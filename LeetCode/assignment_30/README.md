# Assignment 30: Substring with Concatenation of All Words

You are given a string s and an array of strings words. 
All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

Example 1: 
- Input:  s = "barfoothefoobarman", words = ["foo","bar"]
- Ouput: [0, 9]
- Explaination: 
    + The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
    + The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
