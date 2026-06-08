import heapq
from sortedcontainers import SortedList



def combination_sum_III(k, n):
    def backtrack(start, target, path):
        if len(path) == k:
            if target == 0:
                results.append(path[:])
            return

        for i in range(start, 10):
            if i > target:
                break
            path.append(i)
            backtrack(i + 1, target - i, path)
            path.pop()

    results = []
    backtrack(1, n, [])
    return results


k = 3
n = 9
print(combination_sum_III(k, n))
