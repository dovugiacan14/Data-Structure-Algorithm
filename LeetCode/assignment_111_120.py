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
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val 
        self.left = left 
        self.right = right 
    
def min_depth(root): 
    result = 0 
    if root: 
        queue = deque([root]) 
        while queue: 
            level_size = len(queue) 
            for _ in range(level_size): 
                nodes = queue.popleft()

                if nodes.left: 
                    queue.append(nodes.left) 
                if nodes.right: 
                    queue.append(nodes.right) 
            result += 1 
            
    return result 