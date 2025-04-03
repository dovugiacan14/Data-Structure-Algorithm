# Assigment 36: Valid Sodoku 
def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def has_duplicate(arr):
            new_arr = list()
            for text in arr:
                if text != '.': new_arr.append(text)
            if len(new_arr) == 0: return False
            if len(set(new_arr)) != len(new_arr):
                return True 
            return False
        
        # horizontal check 
        for line in board: 
            if has_duplicate(line): 
                return False 
            
        # vertical check 
        for col in range(9):
            check_col_arr = list()
            for row in range(9):
                check_col_arr.append(board[row][col])
            if has_duplicate(check_col_arr):
                return False 
        
        # 3x3 square check 
        i, j = 0, 0 
        while i < 10:
            while j < 9: 
                check_col_arr = list()
                for col in range(i, i+3):
                    for row in range(j, j+3):
                        check_col_arr.append(board[col][row])
                if has_duplicate(check_col_arr): return False 
                j += 3
            j = 0 
            i += 3 
        return True

# Assignment 37: Solver Sodoku 
def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    def is_valid_move(board, row, col, num):
        # check row 
        for i in range(9):
            if board[row][i] == num: return False 
        # check col 
        for i in range(9):
            if board[i][col] == num: return False 
        # check 3x3 square 
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num: return False 
        return True 
    
    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if is_valid_move(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if solve(board): return True 
                            board[i][j] = '.'
                    return False 
        return True 
    
    solve(board)

# Assignment 45: Jump Game II 
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

