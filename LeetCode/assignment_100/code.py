class TreeNode(object): 
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val
        self.left = left 
        self.right = right 
    
def is_sametree(p, q):
    def inorder_traversal(root): 
        stack = []
        result = []
        current_node = root

        while current_node or stack:
            while current_node: 
                stack.append(current_node)
                current_node = current_node.left 
        
            current_node = stack.pop()
            result.append(current_node.val)

            current_node = current_node.right

        return result 
    
    p_traversaled = inorder_traversal(p)
    q_traversaled = inorder_traversal(q)
    return p_traversaled == q_traversaled

def isSameTree(p, q): 
    if not p and not q: 
        return True 
    
    if not p or not q or p.val != q.val: 
        return False 
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
