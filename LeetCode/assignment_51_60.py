
"""Assignment 51: N-Queens

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


"""Assignment 52: N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1: 
- Input:  n = 4 
- Ouput: 2
- Explaination: 
    There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
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


"""Assignment 53: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1: 
- Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
- Ouput: 6
- Explaination: 
    The subarray [4,-1,2,1] has the largest sum 6.
"""
# ĐPT: (O(n^3))
def max_subarray(nums):
    result = max(nums)
    if len(nums) == 1: 
        return result
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)+1):
            if result < sum(nums[i:j]): 
                result = sum(nums[i:j]) 
    return result

# ĐPT: (O(N))
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = 0 

    for num in nums: 
        current_sum += num 
        max_sum = max(max_sum, current_sum)
        if current_sum < 0: 
            current_sum = 0 
    return max_sum 

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))