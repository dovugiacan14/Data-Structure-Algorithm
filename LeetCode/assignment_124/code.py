class TreeNode: 
    def __init__(self, val= 0, left= None, right= None): 
        self.val  = val 
        self.left = left
        self.right = right 

def max_path_sum(root):
    global max_sum
    max_sum = float('-inf') 

    def dfs(node): 
        if not node: 
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        global max_sum 
        max_sum = max(max_sum, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)
    
    dfs(root)
    return max_sum

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(max_path_sum(root))
