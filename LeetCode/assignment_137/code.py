def single_number_v2(nums): 
    counter = Counter(nums)
    for key, val in counter.items(): 
        if val == 1: 
            return key
