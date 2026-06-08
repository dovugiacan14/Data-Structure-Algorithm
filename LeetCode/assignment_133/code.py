class Node(object): 
    def __init__(self, val= 0, neighbors= None):
        self.val = val 
        self.neighbors = neighbors if neighbors is not None else []

# DFS Approach 
def clone_graph(node: Node): 
    if not node: 
        return None 
    
    old_to_new = {}

    def dfs(node):
        if node in old_to_new: 
            return old_to_new[node]

        # clone the node 
        clone = Node(node.val)
        old_to_new[node] = clone

        # clone all neighbors 
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone 
    return dfs(node)

# BFS Approach 
from collections import deque
def clone_graph(node: Node): 
    if not node: 
        return None 
    
    old_to_new = {}
    queue = deque([node])
    old_to_new[node] = Node(node.val)

    while queue:
        curr = queue.popleft()
        for neighor in curr.neighbors: 
            if neighor not in old_to_new: 
                old_to_new[neighor] = Node(neighor.val)
                queue.append(neighor)
            old_to_new[curr].neighbors.append(old_to_new[neighor])
    return old_to_new[node]
