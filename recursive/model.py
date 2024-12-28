def factorial(n): 
    if n == 0:
        return 1 
    return factorial(n - 1) * n 

def fibonacci(n):
    if n == 0: 
        return 1 
    if n== 1:
        return 2 
    return fibonacci(n - 2) + fibonacci(n -1)

def UCLN(a, b):
    if b == 0: 
        return a 
    return UCLN(b, a % b)

if __name__=="__main__":
    # print(factorial(20))
    print(fibonacci(20))
    print(UCLN(25, 15))