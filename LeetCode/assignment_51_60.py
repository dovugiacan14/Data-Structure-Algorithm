
"""Assignment 30: N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1: 
- Input:  n = 4 
- Ouput: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
- Explaination: 
    There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
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
    def solve(row, cols, diag1, diag2, current_solution):
        if row == n: 
            return 
    pass

coordinates_set = solve_n_queens(4)
print(coordinates_set)