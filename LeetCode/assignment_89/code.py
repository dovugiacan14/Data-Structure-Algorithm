def gray_code(n): 
    result = 0 
    for i in range(n): 
        result += [x | (1 << i) for x in reversed(result)]
    return result 

def gray_code(n): 
    return [i ^ (i >> 1) for i in range(1 << n)]
