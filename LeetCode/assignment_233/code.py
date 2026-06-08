def count_digit_one(n): 
    count = 0 
    for i in range(n+1):
        count += str(i).count("1")
    return count 

def count_digit_one(n):
    count = 0 
    factor = 1
    while n // factor > 0: 
        high = n // (factor * 10)
        cur = (n // factor) % 10 
        low = n // factor  

        if cur == 0: 
            count += high * factor 
        elif cur == 1: 
            count += high * factor + (low + 1)
        else: 
            count += (high + 1) * factor 
        
        factor *= 10
    return count 
