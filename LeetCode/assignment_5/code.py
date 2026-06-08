from collections import defaultdict 


def process(s, first, end): 
    while first >= 0 and end < len(s) and s[first] == s[end]: 
        first -= 1 
        end += 1 
    return s[first + 1 : end]

def longestPalindrome(s): 
    result = ""
    for idx in range(len(s)): 
        tmp = process(s, idx, idx)
        if len(tmp) > len(result):
            result = tmp 
        
        tmp = process(s, idx, idx+1)
        if len(tmp) > len(result): 
            result = tmp 
    return result
