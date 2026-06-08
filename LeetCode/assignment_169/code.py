from collections import Counter 

def majority_element(nums):
    freq_dict = Counter(nums)
    freq_dict = dict(freq_dict)
    res= 0 
    max_freq = 0
    for key, val in freq_dict.items(): 
        if val > max_freq: 
            max_freq = val
            res = key 
    return res
