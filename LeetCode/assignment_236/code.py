def lowest_common_ancestor_II(root, p, q):
    if root is None or root == p or root == q: 
        return root 

    left = lowest_common_ancestor_II(root.left, p, q)
    right = lowest_common_ancestor_II(root.right, p, q)

    # Nếu cả left và right đều khác None -> Node hiện tại là LCA 
    if left and right:
        return root 
    return left if left else right
