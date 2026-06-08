from collections import Counter
def minWindow(s, t): 
    if not s or not t: 
        return ""
    t_count = Counter(t)
    window_count = {}

    left = 0 
    min_len = float("inf")
    min_substr = ""
    required_chars = len(t_count)
    formed_chars = 0 

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1 
        if char in t_count and window_count[char] == t_count[char]:
            formed_chars += 1 
        
        while left <= right and formed_chars == required_chars: 
            if right - left + 1 < min_len:
                min_len = right - left + 1 
                min_substr = s[left : right + 1]
            
            left_char = s[left]
            window_count[left_char] -= 1 
            if left_char in t_count and window_count[left_char] <  t_count[left_char]: 
                formed_chars -= 1 
            left += 1 
    return min_substr
