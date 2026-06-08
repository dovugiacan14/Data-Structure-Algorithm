

class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def generate_trees(n):
    def generate_subtrees(start, end):
        if start > end:
            return [None]

        all_trees = []
        for i in range(start, end + 1):
            left_trees = generate_subtrees(start, i - 1)  # left node
            right_trees = generate_subtrees(i + 1, end)  # right node

            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i, left, right)
                    all_trees.append(root)
        return all_trees

    if n == 0:
        return []
    return generate_subtrees(1, n)


# # Helper function to print the tree in preorder traversal
# def preorder_traversal(root):
#     if not root:
#         return "None"
#     return f"{root.val}, {preorder_traversal(root.left)}, {preorder_traversal(root.right)}"

# # Test with n = 3
# trees = generate_trees(3)

# # Print all generated trees
# for i, tree in enumerate(trees, 1):
#     print(f"Tree {i}: {preorder_traversal(tree)}")
