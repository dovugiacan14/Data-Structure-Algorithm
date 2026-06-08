from collections import deque

def connect2(root):
    if not root: 
        return None 
    
    queue = deque([root])
    while queue: 
        prev = None 
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if prev: 
                prev.next = node    # connect previous node to current node 
            
            prev = node 
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        node.next = None 
    return root
