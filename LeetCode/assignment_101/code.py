
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
