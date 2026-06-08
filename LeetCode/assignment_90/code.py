def subset_version2(nums): 
    def backtrack(pos, subset): 
        result.append(subset[:])
        
        if len(subset) == len(nums): 
            return 
        
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]: 
                continue 
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

    nums.sort()
    result = []
    backtrack(0, [])
    return result     

nums = [4,4,4,1,4]
print(subset_version2(nums))
