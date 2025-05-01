"""Assignment 171. Excel Sheet Column Number.

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
    - Input: columnTitle = "A"
    - Output: 1

Example 2:
    - Input: columnTitle = "AB"
    - Output: 28
"""


def title_to_number(columnTitle):
    result = 0
    for char in columnTitle:
        result = result * 26 + (ord(char) - ord("A") + 1)
    return result


column_title = "ZY"
print(title_to_number(column_title))


"""Assignment 172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1: 
    - Input: n = 3
    - Output: 0
    - Explanation: 3! = 6, no trailing zero.

Example 2: 
    - Input: n = 5 
    - Output: 1
    - Explaination: 5! = 120 trailing zero 
"""


def trailing_zeroes(n):
    if n == 0:
        return 0

    def factorial(x):
        if x == 1:
            return 1
        return x * factorial(x - 1)

    output = factorial(n)
    res = 0
    while output > 10:
        if output % 10 != 0:
            break
        res += 1
        output = output // 10

    return res


def trailing_zeroes(n):
    res = 0
    while n > 0:
        n = n // 5
        res += n
    return res


print(trailing_zeroes(10))


"""Assignment 173. Binary Search Tree Iterator 
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
    - BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. 
    The pointer should be initialized to a non-existent number smaller than any element in the BST.
    - boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    - int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1: 
    - Input: ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
             [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    - Output: [null, 3, 7, true, 9, true, 15, true, 20, false]
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self._push_left_nodes(root)

    def _push_left_nodes(self, node):
        while node: 
            self.stack.append(node)
            node = node.left

    def next(self):
        top_node = self.stack.pop()
        if top_node.right: 
            self._push_left_nodes(top_node.right)
        return top_node.val 

    def hasNext(self):
        return len(self.stack) > 0 

"""Assignment 174. Dungeon Game
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. 
Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; 
other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers
To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
Return the knight's minimum initial health so that he can rescue the princess.

Example 1: 
    - Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    - Output: 7
    - Explaination: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
"""

# Using Dynamic Programming
def calculate_minimum(dungeon): 
    m, n = len(dungeon), len(dungeon[0])
    dp = [[float('inf')] * (n + 1) for _ in range(m+1)]
    dp[m][n-1] = dp[m-1][n] = 1 # base case: princess cell 

    for i in range(m-1, -1, -1): 
        for j in range(n-1, -1, -1):
            need =  min(dp[i+1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = max(1, need)
    return dp[0][0]
        
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]] 
print(calculate_minimum(dungeon))

"""Assignment 176: Combine Two Tables."""
import pandas as pd 

def combine_two_tables(person_tab: pd.DataFrame, address_tab: pd.DataFrame):
    result = pd.merge(person_tab, address_tab, on= "personId", how= "left")
    result = result[["firstName", "lastName", "city", "state"]]
    return result