from collections import deque

def minimum_total(triangle): 
    total = triangle[0][0]
    cur_index = 0 
    for i in range(1, len(triangle)): 
        if triangle[i][cur_index] < triangle[i][cur_index + 1]:  
            min_par = triangle[i][cur_index]
        else:
            min_par = triangle[i][cur_index + 1]
            cur_index += 1 

        total += min_par 

    return total 

# use dynamic programming 
def minimum_total(triangle): 
    n = len(triangle)
    dp = triangle[-1][:]

    for i in range(n - 2, -1, -1): 
        for j in range(len(triangle[i])): 
            # choose the minimum path 
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

    return dp[0]

triangle =  [[2],[3,4],[6,5,7],[4,1,8,3]] 
print(minimum_total(triangle))
