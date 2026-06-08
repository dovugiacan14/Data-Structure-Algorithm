def longest_consecutive_sequence(nums): 
    if not nums: 
        return 0 
    
    num_set = set(nums)
    longest = 0 
    for num in num_set: 
        if num -1 not in num_set: 
            cur_num = num 
            cur_streak = 1 
            
            while cur_num + 1 in num_set: 
                cur_num += 1 
                cur_streak += 1 
            
            longest = max(longest, cur_streak)
    return longest 
