from collections import defaultdict 

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + i, len(nums)):
            if nums[i] + nums[j] == target: 
                return i, j 
    return -1, -1  
