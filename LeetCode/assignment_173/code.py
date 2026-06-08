

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self._push_left_nodes(root)

    def _push_left_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        top_node = self.stack.pop()
        if top_node.right:
            self._push_left_nodes(top_node.right)
        return top_node.val

    def hasNext(self):
        return len(self.stack) > 0
