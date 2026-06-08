def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # calculate prefix 
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    
    # calculate suffix 
    r = 1 
    for i in range(n-1, -1, -1):
        answer[i] *= r
        r *= nums[i]
    return answer

nums = [1,2,3,4]
print(product_except_self(nums))
