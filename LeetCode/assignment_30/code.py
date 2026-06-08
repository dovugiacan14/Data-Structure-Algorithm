from itertools import permutations
from collections import Counter
def find_substring(s, words):
    permutate_lst = ["".join(word) for word in permutations(words)]
    len_words = len(permutate_lst[0])
    result = []
    idx = 0 
    while True: 
        if idx >= len(s):
            break 
        if s[idx:idx+len_words] in permutate_lst: 
            result.append(idx)
        idx += 1
    return result 

def find_substring(s, words): 
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words) # count the frequency of each word in list 

    result = []
    for i in range(word_len):
        left = i 
        right = i 
        current_freq = Counter()
        while right + word_len <= len(s):
            word = s[right : right + word_len]
            right += word_len   # update right index 
            if word in word_freq:
                current_freq[word] += 1 

                while current_freq[word] > word_freq[word]:
                    current_freq[s[left:left + word_len]] -= 1
                    left += word_len
                
                if right - left == total_len:
                    result.append(left)
            else: 
                current_freq.clear()
                left = right 
    return result
