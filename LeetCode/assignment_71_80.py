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

"""Assignment 74: Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

- Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 
- Output: True 
"""
def search_matrix(matrix, target):
    n_row = len(matrix)
    i = 0 
    while i < n_row: 
        if target > matrix[i][-1]: 
            i += 1 
        else: 
            if target in matrix[i]: 
                return True 
            else: 
                break 
    return False 

"""Assignment 76: Minimum Window Substring 

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

- Input: s = "ADOBECODEBANC", t = "ABC"
- Output: "BANC"
- Explaination: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""
from collections import Counter
def minWindow(s, t): 
    if not s or not t: 
        return ""
    t_count = Counter(t)
    window_count = {}

    left = 0 
    min_len = float("inf")
    min_substr = ""
    required_chars = len(t_count)
    formed_chars = 0 

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1 
        if char in t_count and window_count[char] == t_count[char]:
            formed_chars += 1 
        
        while left <= right and formed_chars == required_chars: 
            if right - left + 1 < min_len:
                min_len = right - left + 1 
                min_substr = s[left : right + 1]
            
            left_char = s[left]
            window_count[left_char] -= 1 
            if left_char in t_count and window_count[left_char] <  t_count[left_char]: 
                formed_chars -= 1 
            left += 1 
    return min_substr


"""Assignment 77: Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1: 
Input: Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
def combinations(n, k):
    pass