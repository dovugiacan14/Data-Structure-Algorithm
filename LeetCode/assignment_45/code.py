def jump(nums):
    n = len(nums)
    if n == 1: return 0 
    if n == 2: return 1
    dp = [float('inf')] * n 
    dp[0] = 0
    for i in range(n):
        for j in range(1, nums[i]+1):
            if i+j < n:
                dp[i+j] = min(dp[i+j], dp[i]+1)
    return dp[-1]
