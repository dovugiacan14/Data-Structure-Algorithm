from collections import deque

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
