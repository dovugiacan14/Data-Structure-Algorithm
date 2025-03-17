from collections import deque

"""Assignment 111: 

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Example 1: 
    - Input: root = [3,9,20,null,null,15,7]
    - Output: 2

Example 2: 
    - Input: root = [2,null,3,null,4,null,5,null,6]
    - Output:5 

"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    if not root:
        return 0

    queue = deque([root, 1])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # if leaf node, return depth immediately
        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


"""Assignment 112: Path Sum 
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1: 
    - Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    - Output: True

Example 2: 
    - Input: root = [1, 2, 3]], targetSum = 5
    - Output: False 

"""
def has_path_sum(root, targetSum):
    if not root:
        return False

    targetSum -= root.val
    if not root.left and not root.right:
        return targetSum == 0

    return has_path_sum(root.left, targetSum) or has_path_sum(root.right, targetSum)

"""Assignment 113: Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1: 
    - Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    - Output: [[5,4,11,2],[5,8,4,5]]
    - Explaination: There are two paths whose sum equals targetSum:
    5 + 4 + 11 + 2 = 22
    5 + 8 + 4 + 5 = 22

Example 2: 
    - Input: root = [1,2], targetSum = 0
    - Output: []

"""
def pathSum(root, targetSum):
    if not root: 
        return []
    result = []

    def process(node, target, tmp_val_lst, curr_sum):
        tmp_val_lst.append(node.val)
        curr_sum += node.val 

        if not node.left and not node.right and curr_sum == target: 
            result.append(list(tmp_val_lst))

        process(node.left, target, tmp_val_lst, curr_sum)
        process(node.right, target, tmp_val_lst, curr_sum)

        tmp_val_lst.pop()
    
    process(root, targetSum, [], 0)
    return result


"""Assignment 114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":
    - The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    - The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1: 
    - Input: root = [1,2,5,3,4,null,6]
    - Output: [1,null,2,null,3,null,4,null,5,null,6]

"""
def flatten(root): 
    if not root: 
        return []
    
    # traversal pre-orrder
    stack = [root]
    prev = None 

    while stack: 
        node = stack.pop()

        if prev: 
            prev.right = node 
            prev.left = None  # set left to None 

        if node.right: 
            stack.append(node.right)
        if node.left: 
            stack.append(node.left)
        
        prev= node 
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
flatten(root)

"""Assignment 116. Populating Next Right Pointers in Each Node 

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1: 
    - Input: root = [1,2,3,4,5,6,7]
    - Output: [1,#,2,3,#,4,5,6,7,#]
    - Explaination: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. 
    The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

"""
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    head = root 
    while head and head.left: 
        curr = head  
        while curr: 
            curr.left.next = curr.right   # link left child -> right child 
            if curr.next: 
                curr.right.next = curr.next.left 
            curr = curr.next   # move to next node in the current level 
        head = head.left
    return root 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connect(root)

"""Assignment 117. Populating Next Right Pointers in Each Node II.

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1: 
    - Input: root = [1,2,3,4,5,null,7]
    - Output: [1,#,2,3,#,4,5,7,#] 
    - Explaination: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
      The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
"""
def connect2(root):
    if not root: 
        return None 
    
    queue = deque([root])
    while queue: 
        prev = None 
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if prev: 
                prev.next = node    # connect previous node to current node 
            
            prev = node 
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        node.next = None 
    return root

"""Assignment 118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
    - Input: numRows = 5
    - Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

def generate(numRows):
    res = [[1]] 

    for _ in range(1, numRows):
        prev_row = res[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j-1], prev_row[j])
        
        new_row.append(1)   # last partition
        res.append(new_row)
   
    return res

"""Assignment 119. Pascal's Triangle
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
    - Input: rowIndex = 3
    - Output: [1,3,3,1]
"""
def get_row(rowIndex): 
    num_row = rowIndex + 1
    res = [[1]]
    for _ in range(1, num_row): 
        prev_row = res[-1]
        new_row = [1]

        for j in range(1, len(prev_row)): 
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        res.append(new_row)
    return res[-1]


"""Assignment 120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
    - Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    - Output: 11
"""
def minimum_total(triangle): 
    total = triangle[0][0]
    cur_index = 0 
    for i in range(1, len(triangle)): 
        if triangle[i][cur_index] < triangle[i][cur_index + 1]:  
            min_par = triangle[i][cur_index]
        else:
            min_par = triangle[i][cur_index + 1]
            cur_index += 1 

        total += min_par 

    return total 

# use dynamic programming 
def minimum_total(triangle): 
    n = len(triangle)
    dp = triangle[-1][:]

    for i in range(n - 2, -1, -1): 
        for j in range(len(triangle[i])): 
            # choose the minimum path 
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

    return dp[0]

triangle =  [[2],[3,4],[6,5,7],[4,1,8,3]] 
print(minimum_total(triangle))