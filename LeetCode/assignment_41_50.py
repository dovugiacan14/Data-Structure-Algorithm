"""Assignment 46
Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.

Example: 
- Input: nums = [1,2,3]
- Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""
from itertools import permutations 
def permute(nums):
    res = []
    for word in permutations(nums):
        res.append(list(word))
    return res

def permute2(nums):
    res= []
    def backtrack(start): 
        if start == len(nums):
            res.append(nums[:])
            return 
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return res 



"""Assignment 47
Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.

Example: 
- Input: nums = nums = [1,1,2]
- Output: [[1,1,2], [1,2,1], [2,1,1]]
 
"""
from itertools import permutations 
def permute(nums):
    res = []
    for word in permutations(nums):
        word_lst = list(word)
        if word_lst in res: 
            continue
        res.append(word_lst)
    return res

def permute(nums):
    res = set()
    for word in permutations(nums):
        if word not in res: 
            res.add(word)
    return list(res)

res = permute([1,1,2]) 
print(res)
