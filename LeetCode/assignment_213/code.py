import heapq
from sortedcontainers import SortedList



# Use Dynamic Programming
def rob(nums):
    """Phân tích
    Vì không thể cướp cả nhà đầu tiên và nhà cuối cùng cùng lúc, ta chia bài toán thành hai trường hợp:
    1. Không cướp nhà đầu tiên -> Xét dãy nums[1:]
    2. Không cướp nhà cuối cùng -> Xét dãy nums[:-1]
    Sau đó, với mỗi trường hợp, ta dùng thuật toán House Robber I để tìm ta số tiền tối đa,
    và cuối cùng lấy giá trị lớn nhất giữa hai trường hợp đó.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses):
        prev1, prev2 = 0, 0
        for amount in houses:
            curr = max(prev1, prev2 + amount)
            prev2 = prev1
            prev1 = curr
        return prev1

    case1 = rob_linear(nums[:-1])
    case2 = rob_linear(nums[1:])

    return max(case1, case2)
