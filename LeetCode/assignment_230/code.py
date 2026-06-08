from collections import deque, Counter

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val 
        self.left = left
        self.right = right
    
def kth_smallest(root, k):
    count = 0 
    result = None 

    def in_order(node):
        nonlocal count, result 
        if not node or result is not None: 
            return 
        
        in_order(node.left)

        count += 1 
        if count == k:
            result = node.val 
            return 
        
        in_order(node.right)
    in_order(root)
    return result
