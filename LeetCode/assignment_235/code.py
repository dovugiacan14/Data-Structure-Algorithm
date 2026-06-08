class TreeNode(object):
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    # nếu p và q nhỏ hơn root thì duyệt về bên trái 
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # nếu p và q lớn hơn root thì duyệt về bên phải 
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.left, p, q)
    else: 
        return root
