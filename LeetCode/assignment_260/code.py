from collections import Counter 

def singleNumber(nums): 
    count = Counter(nums) 
    results = []
    for num, freq in count.items(): 
        if freq == 1: 
            results.append(num)
    return results

nums = [1, 2, 1, 3, 2, 5]
result = singleNumber(nums)
print(result)    
