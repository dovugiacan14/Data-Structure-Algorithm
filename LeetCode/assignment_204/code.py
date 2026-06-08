from typing import Optional
from collections import defaultdict, deque



# O(N^2)
def count_primes(n):
    if n < 2:
        return 0
    count = 0
    for i in range(2, n):
        check = 0
        for j in range(2, i):
            if i % j == 0:
                check += 1
        if check == 0:
            count += 1
    return count


# O(N.log(N))
def count_primes(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)


n = 10
print(count_primes(n))
