def nthSuperUglyNumber(n, primes): 
    k = len(primes)
    ugly = [1] * n 
    ptr = [0] * k 

    for i in range(1, n): 
        next_ugly = min(
            primes[j] * ugly[ptr[j]] for j in range(k)
        )

        ugly[i] = next_ugly 
        for z in range(k): 
            if primes[z] * ugly[ptr[z]] == next_ugly: 
                ptr[z] += 1
    return ugly[-1]
