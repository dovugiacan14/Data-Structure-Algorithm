from collections import defaultdict 

def reverse(x): 
    MIN_VALUE = -2**31 
    MAX_VALUE = 2**31
    result = ""
    x_str = str(x)
    for char in x_str[::-1]: 
        if char.isdigit():
            result += char 
    if x < 0: 
        res = -int(result)
    else: 
        res = int(result)
    if res <= MIN_VALUE or res >= MAX_VALUE: 
        return 0
    else: 
        return res 
