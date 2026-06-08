from typing import Optional
from collections import defaultdict, deque


def min_subarray_len(target, nums): 
    left = 0 
    total = 0 
    min_len = float("inf")

    for right in range(len(nums)):
        total += nums[right]

        while total >= target: 
            min_len = min(min_len, right - left + 1) 
            total -= nums[left]
            left += 1 
    return 0 if min_len == float("inf") else min_len

target = 11
nums  = [1,1,1,1,1,1,1,1]
print(min_subarray_len(target, nums))
