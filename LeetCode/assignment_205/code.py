from typing import Optional
from collections import defaultdict, deque



def isormophic_string(s, t):
    if len(s) != len(t):
        return False
    data_dict = {}
    list_val = []
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        if s_char in data_dict:
            if data_dict[s_char] != t_char:
                return False
        else:
            if t[i] in list_val:
                return False
            data_dict[s_char] = t[i]
            list_val.append(t_char)
    return True


s = "paper"
t = "title"
print(isormophic_string(s, t))
