
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_binary_search_tree(root):
    if not root:
        return True

    def check(node, min_val, max_val):
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        return check(node.left, min_val, node.val) and check(
            node.right, node.val, max_val
        )

    return check(root, float("-inf"), float("inf"))
