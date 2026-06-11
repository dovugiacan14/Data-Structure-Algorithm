import math 

def numSquares(n): 
    def is_perfect_square(num):
        for a in range(int(math.sqrt(num)) + 1):
            for b in range(a, int(math.sqrt(num)) + 1):
                for c in range(b, int(math.sqrt(num)) + 1):
                    if a*a + b*b + c*c == num:
                        return True 
        return False 
    
    squares = set()
    for i in range(1, 101): 
        squares.add(i*i) 

    x = int(math.sqrt(n))
    if x*x == n: 
        return 1 

    for i in range(1, int(math.sqrt(n)) + 1): 
        if (n - i*i) in squares: 
            return 2
    if is_perfect_square(n):
        return 3
    return 4
