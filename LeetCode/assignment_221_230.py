from collections import deque

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
    def __init__(self, val=0, left=None, right=None):
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


"""Assignment 223: Rectangle Area 
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:
- Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
- Output: 45

Example 2: 
- Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
- Output: 16
"""


def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
    overlap_y = max(0, min(ay2, by2) - max(ay1, by1))

    overlap_area = overlap_x * overlap_y
    total_area = area1 + area2 - overlap_area
    return total_area


"""Assignment 224: Basic Calculator
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval()

Example 1:
- Input: s = "1 + 1"
- Output: 2

Example 2: 
- Input: s = " 2-1 + 2 "
- Output: 3

Example 3: 
- Input: s = "(1+(4+5+2)-3)+(6+8)"
- Output: 23
"""


def basic_calculate(s):
    """IDEA
    - Nếu là số -> đọc hết số nguyên (có thể nhiều chữ số) -> cộng / trừ vào kết quả hiện tại.
    - Nếu là '+' hoặc '-' -> cập nhật dấu hiện tại.
    - Nếu là "(" -> đẩy kết quả hiện tại và dấu hiện tại vào stack -> reset kết quả.
    - Nếu là ")" -> kết thúc một biểu thức con -> lấy dấu và kết quả trước đó từ stack ra -> tính kết quả tổng thể.
    """
    stack = []
    num = 0
    result = 0
    sign = 1

    i = 0
    while i < len(s):
        char = s[i]
        if char.isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            result += sign * num
            continue

        elif char == "+":
            sign = 1
        elif char == "-":
            sign = -1
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ")":
            result = result * stack.pop() + stack.pop()
        i += 1
    return result


"""Assignment 225: Implement Stack using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
    - void push(int x) Pushes element x to the top of the stack.
    - int pop() Removes the element on the top of the stack and returns it.
    - int top() Returns the element on the top of the stack.
    - boolean empty() Returns true if the stack is empty, false otherwise.
"""
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return not self.q1


"""Assignment 226: Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1: 
- Input: root = [4,2,7,1,3,6,9]
- Output: [4,7,2,9,6,3,1]

Example 2: 
- Input: root = [2,1,3]
- Output: [2,3,1]
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


"""Assignment 227: Basic Calculator II
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1: 
- Input: s = "3+2*2"
- Output: 7

Example 2: 
- Input: s = " 3/2 "
- Output: 1

Example 2: 
- Input: s =" 3+5 / 2 "
- Output: 5
"""
def basic_calculate_II(s):
    s = s.replace(" ", "")
    stack= []
    num = 0
    sign = "+"

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)

            if ch in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    prev = stack.pop()
                    result = int(prev / num) if prev * num >= 0 else -(-prev // num)
                    stack.append(result)
                sign = ch 
                num = 0
    return sum(stack)

"""Assignment 228: Summary Ranges
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Example 1: 
- Input: nums = [0,1,2,4,5,7]
- Output:  ["0->2","4->5","7"]

Example 2: 
- Input:  nums = [0,2,3,4,6,8,9]
- Output: ["0","2->4","6","8->9"]
"""
def summary_range(nums):
    result = []
    if not nums:
        return result
    
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            end = nums[i - 1]
            if start == end:
                result.append(str(start))
            else: 
                result.append(f"{start}->{end}")
            start = nums[i]
    
    end = nums[-1]
    if start == end: 
        result.append(str(start))
    else:
        result.append(f"{start}->{end}")
    return result