from collections import deque, Counter



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root):
    if not root:
        return 0

    def get_height(node, is_left):
        height = 0
        while node:
            node = node.left if is_left else node.right
            height += 1
        return height

    left_height = get_height(root, True)
    right_height = get_height(root, False)

    if left_height == right_height:
        return (1 << left_height) - 1
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)
