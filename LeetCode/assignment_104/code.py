class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    depth = 0 
    if root: 
        queue = deque([root])
        while queue: 
            level_size = len(queue)
            for _ in range(level_size): 
                node = queue.popleft()
                
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            depth += 1 
    return depth 
