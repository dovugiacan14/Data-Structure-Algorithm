"""Assignment 221: Maximal Square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
- Input: matrix = [
                    ["1","0","1","0","0"],
                    ["1","0","1","1","1"],
                    ["1","1","1","1","1"],
                    ["1","0","0","1","0"]
                ]
- Output: 4

"""

# Use Dynamic Programming
def maximal_square(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_size = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_size = max(max_size, dp[i][j])
    return max_size * max_size


"""Assignment 222: Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:
- Input: root = [1,2,3,4,5,6]
- Output: 6

Example 2: 
- Input: root = [1]
- Output: 1
"""
class TreeNode(object):
    def __init__(self, val= 0, left= None, right= None):
        self.val = val 
        self.left = left 
        self.right = right
    
def countNodes(root):
    if not root: 
        return 0

    def get_height(node, is_left):
        height = 0 
        while node: 
            node = node.left if is_left else node.right
            height += 1 
        return height 
        
    left_height = get_height(root, True)
    right_height = get_height(root, False)

    if left_height == right_height:
        return (1 << left_height) - 1
    else: 
        return 1 + countNodes(root.left) + countNodes(root.right)
