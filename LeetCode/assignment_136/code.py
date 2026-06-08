from collections import Counter 

def single_numbers(nums):
    counter = Counter(nums)
    for key, val in counter.items(): 
        if val == 1: 
            return key        
