"""Assignment 121. Best Time to Buy and Sell Stock 

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
    - Input: prices = [7,1,5,3,6,4]
    - Output: 5
    - Explaination:  Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

def max_profit(prices):
    res = 0 
    buy_value = prices[0]

    for price in prices[1:]:
        res = max(res, price - buy_value)
        buy_value = min(buy_value, price)
        
    return res 

"""Assignment 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
    - Input: prices = [7,1,5,3,6,4]
    - Output: 7
    - Explaination:  
        + Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        + Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        + Total profit is 4 + 3 = 7.
"""
def max_profit_v2(prices): 
    profit = 0 
    for i in range(1, len(prices)): 
        if prices[i] > prices[i-1]: 
            profit += prices[i] - prices[i-1]
    return profit

print(max_profit_v2([1,2,3,4,5]))

"""Assignment 123. Best Time to Buy and Sell Stock III.

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
    - Input: prices = [3,3,5,0,0,3,1,4]
    - Output: 6
    - Explaination:  
        + Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
        + Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""
def max_profit_v3(prices):
    trans1, trans2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0 

    for i in prices: 
        trans1 = min(trans1, i)
        profit1 = max(profit1, i - trans1)

        trans2 = min(trans2, i - profit1)
        profit2 = max(profit2, i - trans2)

    return profit2


"""Assignment 124. Binary Tree Maximum Path Sum. 

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
Example 1:
    - Input: root = [1,2,3]
    - Output: 6
    - Explaination: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
    - Input: root = [-10,9,20,null,null,15,7]
    - Output: 42
    - Explaination:  The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42."
"""
class TreeNode: 
    def __init__(self, val= 0, left= None, right= None): 
        self.val  = val 
        self.left = left
        self.right = right 

def max_path_sum(root):
    global max_sum
    max_sum = float('-inf') 

    def dfs(node): 
        if not node: 
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        global max_sum 
        max_sum = max(max_sum, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)
    
    dfs(root)
    return max_sum

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(max_path_sum(root))


"""Assignment 125. Valid Palindorme 

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
    - Input: s = "A man, a plan, a canal: Panama"
    - Output: true
    - Explaination: "amanaplanacanalpanama" is a palindrome.

Example 2:
    - Input: s = "race a car"
    - Output: false
    - Explanation: "raceacar" is not a palindrome.
"""
def is_palindorme(s):
    if not s: 
        return True 
    s = s.replace(',',"").replace(" ", "").replace(":", "").replace('.', "").replace("@", "").replace("#", "").replace("_", "")
    s = s.lower()
    reversed_text = s[::-1]
    if s == reversed_text:
        return True 
    return False

import re
def is_palindorme(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

"""Assignment 128. Longest Consecutive Sequence.

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
    - Input: nums = [100,4,200,1,3,2]
    - Output: 4
    - Explaination: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    - Input: nums = [0,3,7,2,5,8,4,6,0,1]
    - Output: 9
"""
def longest_consecutive_sequence(nums): 
    if not nums: 
        return 0 
    
    num_set = set(nums)
    longest = 0 
    for num in num_set: 
        if num -1 not in num_set: 
            cur_num = num 
            cur_streak = 1 
            
            while cur_num + 1 in num_set: 
                cur_num += 1 
                cur_streak += 1 
            
            longest = max(longest, cur_streak)
    return longest 
    

"""Assignment 129. Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
    - Input: root = [1,2,3]
    - Output: 25
    - Explaination: 
        + The root-to-leaf path 1->2 represents the number 12.
        + The root-to-leaf path 1->3 represents the number 13.
        + Therefore, sum = 12 + 13 = 25.

Example 2:
    - Input: root = [4,9,0,5,1]
    - Output: 1026
    - Explanation: 
        + The root-to-leaf path 4->9->5 represents the number 495.
        + The root-to-leaf path 4->9->1 represents the number 491.
        + The root-to-leaf path 4->0 represents the number 40.
        + Therefore, sum = 495 + 491 + 40 = 1026.
"""
class TreeNode: 
    def __init__(self, val=0, left= None, right= None): 
        self.val = val 
        self.left = left 
        self.right = right
    
def sum_numbers(root):
    if not root: 
        return []
    total_traversal = []

    def dfs(node, tmp_lst): 
        if not node: 
            return  
        
        tmp_lst.append(node.val)
        if not node.left and not node.right:
            total_traversal.append(tmp_lst[:])
        
        dfs(node.left, tmp_lst)
        dfs(node.right, tmp_lst)
        tmp_lst.pop()     # backtrack 

    dfs(root, [])
    res = []
    for elem in total_traversal: 
        if elem not in res: 
            res.append(elem )
    res = [["".join(map(str, sub_lst)) for sub_lst in res]]
    
    res_int = [int(elem) for elem in res[0]]

    return sum(res_int)

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print(sum_numbers(root))

"""Assignment 129. Surrounded Region.

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:
    - Input: board= [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    - Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    
Example 2:
    - Input: board = [["X"]]
    - Output: [["X"]]
"""
def solve(board): 
    n_rows = len(board)
    n_cols = len(board[0])

    def dfs(row,col): 
        if row < 0 or col < 0 or row >= n_rows or col >= n_cols or board[row][col] != "O": 
            return 
        
        board[row][col] = "#"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    # Step 1: Mark all 'O' connect to the bounder. 
    for i in range(n_rows):
        dfs(i, 0)
        dfs(i, n_cols -1)
    
    for j in range(n_cols): 
        dfs(0, j)
        dfs(n_rows - 1, j)
    
    # Step 2: Update table 
    for i in range(n_rows): 
        for j in range(n_cols): 
            if board[i][j] == "O":
                board[i][j] = 'X' 
            elif board[i][j] == '#':
                board[i][j] = "O"