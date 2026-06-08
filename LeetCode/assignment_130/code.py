def solve(board): 
    n_rows = len(board)
    n_cols = len(board[0])

    def dfs(row,col): 
        if row < 0 or col < 0 or row >= n_rows or col >= n_cols or board[row][col] != "O": 
            return 
        
        board[row][col] = "#"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    # Step 1: Mark all 'O' connect to the bounder. 
    for i in range(n_rows):
        dfs(i, 0)
        dfs(i, n_cols -1)
    
    for j in range(n_cols): 
        dfs(0, j)
        dfs(n_rows - 1, j)
    
    # Step 2: Update table 
    for i in range(n_rows): 
        for j in range(n_cols): 
            if board[i][j] == "O":
                board[i][j] = 'X' 
            elif board[i][j] == '#':
                board[i][j] = "O"
