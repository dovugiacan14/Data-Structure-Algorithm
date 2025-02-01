
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


"""Assignment 54: Spiral Matrix 

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1: 
- Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
- Ouput: [1,2,3,6,9,8,7,4,5]

Example 2: 
- Input: [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 
- Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
def spiral_order(matrix):
    if not matrix:
        return []
        
    res = []
    start_row, end_row = 0, len(matrix) - 1
    start_col, end_col = 0, len(matrix[0]) - 1
    
    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            res.append(matrix[start_row][i])
        start_row += 1
        
        for i in range(start_row, end_row + 1):
            res.append(matrix[i][end_col])
        end_col -= 1
        
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                res.append(matrix[end_row][i])
            end_row -= 1
        
        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                res.append(matrix[i][start_col])
            start_col += 1
            
    return res

"""Assignment 55: Jump Game 

You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise. 

Example 1: 
- Input: nums = [2,3,1,1,4]
- Ouput: true 
- Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index. 

Example 2: 
- Input: nums = [3,2,1,0,4]
- Output: False 
- Explaination: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Idea: 
B1: Use "farthest" to save the longest jump you can jump 
B2: For elem in array: 
    cur_index > farthest -> you can't jump 
    else: update farthest 
B3: if farthest >= len(nums) -> True 
"""
def can_jump(nums):
    farthest = 0 
    for idx, elm in enumerate(nums):
        if idx > farthest: 
            return False 
        farthest = max(farthest, idx + elm)

        if farthest >= len(nums) - 1: 
            return True 


"""Assignment 56: Merge Intervals  

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1: 
- Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
- Ouput: [[1,6],[8,10],[15,18]]
- Explaination: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]

Example 2: 
- Input: intervals = [[1,4],[4,5]]
- Output: [[1,5]]
"""
def merge(intervals):
    idx = 1
    intervals= sorted(intervals, key=lambda x: x[0])
    while True:
        n_interval = len(intervals)
        if idx >= n_interval:
            break 
        if intervals[idx][0] >= intervals[idx-1][0] and intervals[idx][0] <= intervals[idx-1][1]:
            if intervals[idx][1] >= intervals[idx-1][1]:
                intervals[idx-1][1] = intervals[idx][1]
            del intervals[idx]
        else: 
            idx += 1  
    return intervals


"""Assignment 57: Insert Intervals  

You are given an array of non-overlapping intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
Example 1: 
- Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
- Ouput: [[1,5],[6,9]]
- Explaination: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]

Example 2: 
- Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
- Output: [[1,2],[3,10],[12,16]]
- Explaination: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
def insert(intervals, newInterval):
    intervals.append(newInterval)
    def merge(intervals):
        idx = 1
        intervals= sorted(intervals, key=lambda x: x[0])
        while True:
            n_interval = len(intervals)
            if idx >= n_interval:
                break 
            if intervals[idx][0] >= intervals[idx-1][0] and intervals[idx][0] <= intervals[idx-1][1]:
                if intervals[idx][1] >= intervals[idx-1][1]:
                    intervals[idx-1][1] = intervals[idx][1]
                del intervals[idx]
            else: 
                idx += 1  
        return intervals
    result = merge(intervals)
    return result 


"""Assignment 58:  Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1: 
- Input: s = "   fly me   to   the moon  "
- Ouput: 4
"""
def lengthOfLastWord(s):
    word_split = s.split(" ")   # split by space 
    word_lst = [x for x in word_split if x!= ""]
    return len(word_lst[-1])

"""Assignment 59: Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1: 
- Input: n = 3
- Ouput: [[1,2,3],[8,9,4],[7,6,5]]
"""
def generate_matrix(n): 
    matrix = [[0] * n for _ in range(n)] 
    par = 1
    start_row, end_row = 0, n-1
    start_col, end_col = 0, n-1
    while start_row <= end_row and start_col <= end_col: 
        for i in range(start_col, end_col+1):
            matrix[start_row][i] = par 
            par += 1 
        start_row += 1 

        for i in range(start_row, end_row + 1): 
            matrix[i][end_col] = par 
            par += 1 
        end_col -=1 

        if start_row <= end_row: 
            for i in range(end_col, start_col - 1, -1): 
                matrix[end_row][i] = par 
                par += 1 
            end_row -= 1 

        if start_col <= end_col: 
            for i in range(end_row, start_row - 1, -1): 
                matrix[i][start_col] = par 
                par += 1 
            start_col += 1 
        
    return matrix 


"""Assignment 60: Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
Given n and k, return the kth permutation sequence.

Example 1: 
- Input: n = 3, k = 3
- Ouput: "213"
"""
from itertools import permutations

def get_permutate(n, k): 
    arr = [str(i) for i in range(1, n + 1)]
    permute = [] 
    for word in permutations(arr):
        word_str = ''.join(word)
        permute.append(word_str)
    return permute[k-1]

res= get_permutate(4,9)
print(res)