

def trailing_zeroes(n):
    if n == 0:
        return 0

    def factorial(x):
        if x == 1:
            return 1
        return x * factorial(x - 1)

    output = factorial(n)
    res = 0
    while output > 10:
        if output % 10 != 0:
            break
        res += 1
        output = output // 10

    return res


def trailing_zeroes(n):
    res = 0
    while n > 0:
        n = n // 5
        res += n
    return res


print(trailing_zeroes(10))
