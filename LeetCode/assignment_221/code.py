from collections import deque, Counter



# Use Dynamic Programming
def maximal_square(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_size = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_size = max(max_size, dp[i][j])
    return max_size * max_size
