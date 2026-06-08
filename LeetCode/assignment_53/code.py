# ĐPT: (O(n^3))
def max_subarray(nums):
    result = max(nums)
    if len(nums) == 1: 
        return result
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)+1):
            if result < sum(nums[i:j]): 
                result = sum(nums[i:j]) 
    return result

# ĐPT: (O(N))
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = 0 

    for num in nums: 
        current_sum += num 
        max_sum = max(max_sum, current_sum)
        if current_sum < 0: 
            current_sum = 0 
    return max_sum 
