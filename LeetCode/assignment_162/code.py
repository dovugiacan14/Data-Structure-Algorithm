def maximum_gap(nums):
    if len(nums) <= 1: 
        return 0
    sorted_nums = sorted(nums)
    max_gap = 0
    for i in range(len(nums) - 1): 
        gap = sorted_nums[i + 1] - sorted_nums[i]
        max_gap = gap if gap > max_gap else max_gap
    return max_gap
