def is_power_true(n):
    i = 0 
    while True: 
        if 2**i < n: 
            i += 1 
        elif 2**i == n:
            return True 
        else: 
            return False 
