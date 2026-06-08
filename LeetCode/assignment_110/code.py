class TreeNode(object): 
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val 
        self.left = left 
        self.right = right

def is_balance(root): 
    def height(node): 
        if not node: 
            return 0 
        
        left_subtree = height(node.left)
        right_subtree = height(node.right)

        if left_subtree == -1 or right_subtree == -1 or abs(left_subtree - right_subtree) > 1: 
            return -1 
        
        return max(left_subtree, right_subtree) + 1
    return height(root) != -1
