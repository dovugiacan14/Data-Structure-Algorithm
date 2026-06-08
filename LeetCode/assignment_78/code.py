def subsets(nums):
    def backtrack(pos, subset):
        result.append(subset[:])
        
        if len(subset) == len(nums):
            return 

        for i in range(pos, len(nums)):
            subset.append(nums[i]) 
            backtrack(i + 1, subset)
            subset.pop()
    result = []
    backtrack(0, [])
    return result 

print(subsets([1,2,3]))


# có thời gian hãy xem và debug lại nhé.
