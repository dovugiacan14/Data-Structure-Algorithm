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
