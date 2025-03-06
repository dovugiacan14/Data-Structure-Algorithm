"""Note

- Inorder: Left -> Node -> Right (LNR)
- Preorder: Left -> Right -> Node (LRN) 
- Postorder: Node -> Left -> Right (NLR)

"""

"""Assignment 101: Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1: 
    - Input: root = [1,2,2,3,4,4,3]
    - Output: True

Example 2: 
    - Input: root = [1,2,2,null,3,null,3]
    - Output: False

"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object): 
    def is_mirror(self, left, right): 
        if not left and not right: 
            return True 
        
        if not left or not right: 
            return False 
        
        return left.val == right.val and self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root: 
            return True 
        
        return self.is_mirror(root.left, root.right)
    
"""Assignment 102: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1: 
    - Input: root = [3,9,20,null,null,15,7]
    - Output:  [[3],[9,20],[15,7]]

Example 2: 
    - Input: root =[1]
    - Output: [[1]]

"""
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root): 
    if not root: 
        return []
    
    result = []
    queue = deque([root])
    while queue: 
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size): 
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        result.append(level_nodes)
    return result 

    
"""Assignment 103: Binary Tree Level Zigzag Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1: 
    - Input: root = [3,9,20,null,null,15,7]
    - Output: [[3],[20,9],[15,7]]

Example 2: 
    - Input: root =[1]
    - Output: [[1]]

"""
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_zigzag_traversal(root): 
    if not root: 
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True 
    while queue: 
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size): 
            node = queue.popleft()

            if left_to_right: 
                level_nodes.append(node.val)
            else: 
                level_nodes.insert(0, node.val)

            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        result.append(level_nodes)
        left_to_right = not left_to_right
    return result 


"""Assignment 104: Maximum Depth of Binary Tree

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1: 
    - root = [3,9,20,null,null,15,7]
    - Output: 3

Example 2: 
    - Input: root = [1,null,2]
    - Output: 2

"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    depth = 0 
    if root: 
        queue = deque([root])
        while queue: 
            level_size = len(queue)
            for _ in range(level_size): 
                node = queue.popleft()
                
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            depth += 1 
    return depth 

"""Assignment 105: Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1: 
    - Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    - Output:  [3,9,20,null,null,15,7]

Example 2: 
    - Input: preorder = [-1], inorder = [-1]
    - Output: [-1]

"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)} 
        pre_idx = 0  

        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return None  

            root_val = preorder[pre_idx]  
            pre_idx += 1 
            root = TreeNode(root_val)

            root.left = helper(left, inorder_map[root_val] - 1)
            root.right = helper(inorder_map[root_val] + 1, right)

            return root

        return helper(0, len(inorder) - 1)
    
"""Assignment 106: Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and 
postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1: 
    - Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    - Output:  [3,9,20,null,null,15,7]

Example 2: 
    - Input: inorder = [-1], postorder = [-1]
    - Output: [-1]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)} 
        pre_idx = 0  

        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return None  

            root_val = preorder[pre_idx]  
            pre_idx += 1 
            root = TreeNode(root_val)

            root.left = helper(left, inorder_map[root_val] - 1)
            root.right = helper(inorder_map[root_val] + 1, right)

            return root

        return helper(0, len(inorder) - 1)

"""Assignment 107: Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1: 
    - Input: root = [3,9,20,null,null,15,7]
    - Output: [[15,7],[9,20],[3]]

"""
class TreeNode(object):
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val 
        self.left = left 
        self.right = right 

def level_order_traversal(root):
    if not root: 
        return []
    
    queue = deque([root])
    result = []
    while queue: 
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size): 
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        result.insert(0, level_nodes)

    return result 


"""Assignment 108: Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1: 
    - Input: nums = [-10,-3,0,5,9]
    - Output: [0,-3,9,-10,null,5]
    - Explaination: [0,-10,5,null,-3,null,9] is also accepted
"""

class TreeNode(object): 
    def __init__(self, val, left, right): 
        self.val = val 
        self.left = left 
        self.right = right 

def sorted_array_to_bst(nums):
    if not nums: 
        return None 
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums[:mid]) # build left subtree
    root.right = sorted_array_to_bst(nums[mid+1:]) # build right subtree

    return root 