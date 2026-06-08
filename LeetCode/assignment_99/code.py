class TreeNode(object): 
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val
        self.left = left 
        self.right = right 

def recover_tree(root): 
    """
    :type root: Optional[TreeNode]
    :rtype: None Do not return anything, modify root in-place instead.
    """
    first = None 
    second = None 
    prev = None 

    def inoder_traversal(node):
        nonlocal first, second, prev
        if not node: 
            return 
        
        inoder_traversal(node.left) # visit left subtree

        if prev and prev.val > node.val: 
            if not first: 
                first = prev # mark the first error 
            second = node  # mark the second error 
        prev = node 

        inorder_traversal(node.right)

    inoder_traversal(root)
    
    # swap two errors node 
    if first and second: 
        first.val, second.val = second.val, first.val  
