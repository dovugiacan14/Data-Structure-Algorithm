from collections import defaultdict 

def myAtoi(s): 
    MIN_VALUE = -2**31 
    MAX_VALUE = 2**31
    n = 0 
    sign = 1 
    empty= True 
    for char in s: 
        if empty: 
            if char == " ": 
                continue 
            elif char == "-": 
                sign = -1 
            elif char.isdigit():
                n = int(char)
            elif char != "+": 
                return 0 
            empty = False 
        else: 
            if char.isdigit():
                n = n*10 + int(char)
                if sign * n > MAX_VALUE: 
                    return MAX_VALUE
                if sign * n < MIN_VALUE:
                    return MIN_VALUE
            else: 
                break 
    return sign * n 
