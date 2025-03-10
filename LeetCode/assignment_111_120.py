from collections import deque

"""Assignment 111: 

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Example 1: 
    - Input: root = [3,9,20,null,null,15,7]
    - Output: 2

Example 2: 
    - Input: root = [2,null,3,null,4,null,5,null,6]
    - Output:5 

"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    if not root:
        return 0

    queue = deque([root, 1])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # if leaf node, return depth immediately
        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


"""Assignment 112: Path Sum 
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1: 
    - Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    - Output: True

Example 2: 
    - Input: root = [1, 2, 3]], targetSum = 5
    - Output: False 

"""


def has_path_sum(root, targetSum):
    if not root:
        return False

    targetSum -= root.val
    if not root.left and not root.right:
        return targetSum == 0

    return has_path_sum(root.left, targetSum) or has_path_sum(root.right, targetSum)
