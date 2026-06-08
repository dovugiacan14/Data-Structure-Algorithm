from collections import deque, Counter



def majority_element(nums):
    n = len(nums)
    thres = n // 3
    freq = Counter(nums)
    return [num for num, count in freq.items() if count > thres]
