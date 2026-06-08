from collections import OrderedDict, defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def preorder_traversal(root):
    if not root: 
        return []
    
    stack, output = [root], []
    while stack: 
        node = stack.pop()
        if node: 
            output.append(node.val)

            if node.right: 
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)
    return output

def preorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return 
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result
