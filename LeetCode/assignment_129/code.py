class TreeNode: 
    def __init__(self, val=0, left= None, right= None): 
        self.val = val 
        self.left = left 
        self.right = right
    
def sum_numbers(root):
    if not root: 
        return []
    total_traversal = []

    def dfs(node, tmp_lst): 
        if not node: 
            return  
        
        tmp_lst.append(node.val)
        if not node.left and not node.right:
            total_traversal.append(tmp_lst[:])
        
        dfs(node.left, tmp_lst)
        dfs(node.right, tmp_lst)
        tmp_lst.pop()     # backtrack 

    dfs(root, [])
    res = []
    for elem in total_traversal: 
        if elem not in res: 
            res.append(elem )
    res = [["".join(map(str, sub_lst)) for sub_lst in res]]
    
    res_int = [int(elem) for elem in res[0]]

    return sum(res_int)

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print(sum_numbers(root))
