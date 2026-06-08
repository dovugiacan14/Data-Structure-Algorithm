import heapq
from sortedcontainers import SortedList



def find_kth_largest(nums, k):
    max_k = 0
    for i in range(k):
        max_k = max(nums)
        nums.remove(max_k)
    return max_k


def find_kth_largest(nums, k):
    """Ý tưởng:
    - Sử dụng min-heap kích thước k để giữ k phần tử lớn nhất.
    - Phần tử nhỏ nhất trong heap này chính là k-th largest.
    """
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    return min_heap[0]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_largest(nums, k))
