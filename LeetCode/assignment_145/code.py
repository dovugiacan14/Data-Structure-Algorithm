from collections import OrderedDict, defaultdict

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def post_order_traversal(root):
    result = []
    def dfs(node):
        if not node: 
            return 
        
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
print(post_order_traversal(root))
