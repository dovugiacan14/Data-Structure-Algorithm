import heapq
from sortedcontainers import SortedList



def contain_duplicates(nums):
    format_nums = list(set(nums))
    return True if len(format_nums) != len(nums) else False
