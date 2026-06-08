from collections import defaultdict 

def isPalindrome(x): 
    if x < 0: 
        return False 
    else: 
        arr= []
        while x > 0: 
            arr.append(x%10)
            x = int(x/10)
        _arr = list(reversed(arr))
        if arr == _arr:
            return True 
        else: 
            return False

def isPalindrome(x):
    str_x = str(x)
    n = str_x[::-1]
    if str_x == n: 
        return True 
    else: 
        return False 
