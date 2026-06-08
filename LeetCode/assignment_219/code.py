import heapq
from sortedcontainers import SortedList



def contain_duplicate_II(nums, k):
    def contain_duplicates(nums):
        format_nums = list(set(nums))
        return True if len(format_nums) != len(nums) else False

    for i in range(len(nums) - k):
        consider_nums = nums[i : i + k + 1]
        if contain_duplicates(consider_nums):
            return True
    return False


def contain_duplicate_II(nums, k):
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
        if len(seen) > k:
            seen.remove(nums[i - k])
    return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
print(contain_duplicate_II(nums, k))
