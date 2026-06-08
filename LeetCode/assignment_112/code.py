from collections import deque

def has_path_sum(root, targetSum):
    if not root:
        return False

    targetSum -= root.val
    if not root.left and not root.right:
        return targetSum == 0

    return has_path_sum(root.left, targetSum) or has_path_sum(root.right, targetSum)
