from typing import Optional
from collections import defaultdict, deque



def range_bitwise_and(left: int, right: int):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift


left = 5
right = 7
print(range_bitwise_and(left, right))
