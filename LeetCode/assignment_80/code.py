def remove_duplicates(nums):
    if len(nums) <= 2: 
        return len(nums) 
    k = 2 
    for i in range(2, len(nums)):
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1
    return k 

def remove_duplicates(nums):
    j = 1 
    for i in range(1, len(nums)):
        if j == 1 or nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1 
    return j
