class TreeNode(object):
    def __init__(self, val=0, left=None, right= None):
        self.val = val 
        self.left = left 
        self.right = right 

def binary_tree_paths(root):
    result = []

    def dfs(node, path):
        if not node: 
            return 
        
        path += str(node.val)
        if not node.left and not node.right:
            result.append(path)
        else: 
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
    dfs(root, "")
    return result
