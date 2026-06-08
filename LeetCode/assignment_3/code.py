from collections import defaultdict 


def longest_substring(s): 
    max_len = 0 
    count = 0 
    arr = set()

    for idx, character in enumerate(s): 
        while character in arr: 
            arr.remove(s[count])
            count += 1 
        arr.add(character)
        max_len = max(max_len, idx - count + 1)
    return max_len
