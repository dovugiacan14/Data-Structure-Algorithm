def solve_n_queens(n): 
    def is_safe(board, row, col):
        for i in range(row): 
            if board[i] == col: 
                return False 

        for i in range(row):
            if board[i] - i == col - row: 
                return False 

        for i in range(row): 
            if board[i] + i == row + col: 
                return False 
        return True 

    def solve(board, row, coordinates_set): 
        if row == n: 
            normalized_solution = tuple(sorted((r, board[r]) for r in range(n)))
            coordinates_set.append(normalized_solution)
            return 

        # recursive 
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col 
                solve(board, row + 1, coordinates_set)
                board[row] = -1

    board = [-1] * n
    coordinates_set = list()
    solve(board, 0, coordinates_set)
    result = []
    for solution in coordinates_set:
        chess =  ["." * n for _ in range(n)]
        for coord in solution:
            chess[coord[0]] = chess[coord[0]][:coord[1]] + "Q" + chess[coord[0]][coord[1] + 1:]

        result.append(chess)
     
    return result

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
    return solutions
