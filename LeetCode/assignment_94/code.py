

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Use Recursive
def inorder_traversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    if not root:
        return []

    left_subtree = inorder_traversal(root.left)
    current_value = [root.val]
    right_subtree = inorder_traversal(root.right)

    return left_subtree + current_value + right_subtree


# Use Stack
def inorder_traversal_iter(root):
    stack = []
    result = []
    current_node = root

    while current_node or stack:
        # 1. Push all left node to stack
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        # 2. Get the node on the top of the stack
        current_node = stack.pop()
        result.append(current_node.val)

        # 3. Traversal the right branch
        current_node = current_node.right

    return result
