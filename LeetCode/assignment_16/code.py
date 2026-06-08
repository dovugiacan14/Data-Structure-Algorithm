def threeSumCloset(nums, target):
    nums.sort()
    n = len(nums)
    result = nums[0] + nums[1] + nums[2]
    if result > target: 
        return result 
    for i in range(n - 2):
        left = i + 1 
        right = n - 2 
        while left < right: 
            sum3 = nums[i] + nums[left] + nums[right]  
            if sum3 < target: 
                left += 1 
            elif sum3 > target: 
                right -= 1 
            else: 
                return target
            if abs(sum3 - target) < abs(result - target):
                result = sum3
    return result  
