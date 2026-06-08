from typing import Optional
from collections import defaultdict, deque



def is_happy(n):
    def calculate_sum_square(number):
        return sum(int(c) ** 2 for c in str(number))

    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = calculate_sum_square(n)
    return True
