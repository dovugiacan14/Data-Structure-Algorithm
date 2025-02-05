"""Assignment 71: Simplify Path 

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1: 
- Input: path = "/home/"
- Ouput: "/home"

Example 2: 
- Input: path = "/home/user/Documents/../Pictures"
- Output: "/home/user/Pictures"
"""
def simplify_path(path):
    stack = []
    directories = path.split("/")
    for dir in directories: 
        if dir == "." or not dir: 
            continue 
        elif dir == "..": 
            if stack: 
                stack.pop()
        else: 
            stack.append(dir)
    return "/" + "/".join(stack)


# Nghiên cứu lại - Dùng Quy Hoạch Động 
"""Assignment 72: Edit Distance 

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1: 
- Input: word1 = "horse", word2 = "ros"
- Ouput: 3
- Explaination: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
"""
def min_distance(word1, word2):
    len_w1 = len(word1)
    len_w2 = len(word2)
    prev = list(range(len_w2 + 1))
    curr = [0] * (len_w2 + 1)
    for i in range(1, len_w1 + 1):
        curr[0] = i
        for j in range(1, len_w2 + 1): 
            if word1[i - 1] == word2[j -1]:
                curr[j] = prev[j -1]
            else: 
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev 
    return prev[len_w2]

"""Assignment 73: Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1: 
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""
def set_zeroes(matrix):
    zero_coords = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0: 
                tmp_coord = [row, col]
                zero_coords.append(tmp_coord)
    if not zero_coords: 
        return matrix
    for row, col in zero_coords: 
        for j in range(len(matrix[0])):
            matrix[row][j] = 0 
        
        for i in range(len(matrix)):
            matrix[i][col] = 0
    return matrix


"""Assignment 77: Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1: 
Input: Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
def combinations(n, k):
    
    pass