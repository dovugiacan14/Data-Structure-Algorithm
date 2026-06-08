def solve_n_queens(n):
    def solve(row, columns, diagionals1, diagionals2, board, solutions):
        if row == n: 
            solutions.append(["".join(row) for row in board])
            return 
        
        for col in range(n):
            diag1 = row - col 
            diag2 = row + col 
            if col in columns or diag1 in diagionals1 or diag2 in diagionals2: 
                continue 

            # place the queen 
            board[row][col] = "Q"
            columns.add(col)
            diagionals1.add(diag1)
            diagionals2.add(diag2)

            # recursive to the next row 
            solve(row + 1, columns, diagionals1, diagionals2, board, solutions)

            # backtrack 
            board[row][col] = "."
            columns.remove(col)
            diagionals1.remove(diag1)
            diagionals2.remove(diag2)
        
    solutions = []
    board = [["."]*n for _ in range(n)]
    solve(0, set(), set(), set(), board, solutions)
    return len(solutions)
