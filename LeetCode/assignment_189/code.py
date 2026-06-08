import pandas as pd
from collections import Counter



def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
