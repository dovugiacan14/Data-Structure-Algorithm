"""Assignment 241: Search a 2D Matrix II
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Example 1: 
- Input: expression = "2-1-1"
- Output: [0,2]
- Explaination: ((2-1)-1) = 0 and (2-(1-1)) = 2

Example 2: 
- Input: expression = "2*3-4*5"
- Output: [-34,-14,-10,-10,10]
- Explaination: 
    (2*(3-(4*5))) = -34 
    ((2*3)-(4*5)) = -14 
    ((2*(3-4))*5) = -10 
    (2*((3-4)*5)) = -10 
    (((2*3)-4)*5) = 10
"""
def diffways_to_compute(expression):
    memo = {}

    def compute(expr):
        if expr in memo:
            return memo[expr]
        
        results = []
        for i, char in enumerate(expr):
            if char in '+-*':
                left = compute(expr[:i])
                right = compute(expr[i+1:])

                for l in left:
                    for r in right:
                        if char == "+": 
                            results.append(l + r)
                        elif char == "-":
                            results.append(l - r)
                        elif char == "*":
                            results.append(l * r)
        if not results:
            results = [int(expr)]
        memo[expr] = results
    return compute(expression)

"""Assignment 242: Valid Anagram 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1: 
- Input: s = "anagram", t = "nagaram"
- Output: True

Example 2: 
- Input: s = "rat", t = "car"
- Output: False
"""

def is_anagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t

"""Assignment 257: Binary Tree Paths 
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1: 
- Input: root = [1,2,3,null,5]
- Output: ["1->2->5","1->3"]

Example 2: 
- Input: root = 1 
- Output: ["1"]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right= None):
        self.val = val 
        self.left = left 
        self.right = right 

def binary_tree_paths(root):
    result = []

    def dfs(node, path):
        if not node: 
            return 
        
        path += str(node.val)
        if not node.left and not node.right:
            result.append(path)
        else: 
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
    dfs(root, "")
    return result