def isAdditiveNumber(num):
    n = len(num)

    def valid(a, b , start): 
        while start < n: 
            c = str(int(a) + int(b))
        
            if not num.startswith(c, start):
                return False
        
            start += len(c)
            a, b = b, c
        return True

    for i in range(1, n): 
        if num[0] == '0' and i > 1: 
            break

        a = int(num[:i])
        for j in range(i + 1, n): 
            if num[i] == '0' and j - i > 1: 
                break

            b = int(num[i:j])
            if valid(a, b, j):
                return True

    return False

if __name__ == "__main__":
    print(isAdditiveNumber("112358"))  # True
    print(isAdditiveNumber("199100199"))  # True
    print(isAdditiveNumber("123"))  # True
    print(isAdditiveNumber("1023"))  # False