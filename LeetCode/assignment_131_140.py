
"""Assignment 131. Palindrome Partitioning 

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
    - Input: s = "aab"
    - Output: [["a","a","b"],["aa","b"]]
    - Explaination: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    - Input: s = "a"
    - Output: [["a"]]
"""
def partition(s): 
    def is_palindrome(text): 
        return text == text[::-1]
    
    def generate_partition(start, path): 
        if start == len(s):
            subsets.append(path[:])
            return 
        
        for i in range(start + 1, len(s) + 1): 
            substring = s[start:i]
            if is_palindrome(substring): 
                path.append(s[start:i])
                generate_partition(i, path)
                path.pop()
        
    subsets = []
    generate_partition(0, [])
    
    return subsets


"""Assignment 132. Palindrome Partitioning II.

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
    - Input: s = "aab"
    - Output: 1
    - Explaination: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
    - Input: s = "ab"
    - Output: 1
"""
# ĐPT: O(2^n)
def min_cut(s): 
    def is_palindrome(text): 
        return text == text[::-1]
    
    def partition(str):
        def generate_partition(start, path): 
            if start == len(str):
                subsets.append(path[:])
                return 

            for i in range(start + 1, len(s) + 1): 
                substring = str[start:i]
                if is_palindrome(substring): 
                    path.append(substring)
                    generate_partition(i, path)
                    path.pop()

        subsets = [] 
        generate_partition(0, [])
        return subsets

    subsets = partition(s)
    min_len = min(len(arr) for arr in subsets)
    return min_len - 1 


# ĐPT: O(n^2)
def min_cut_palindrome(s): 
    n = len(s)
    # palindrome checking. 
    is_palindrome = [[False] * n for _ in range(n)]

    for right in range(n): 
        for left in range(right + 1): 
            if s[left] == s[right] and (right - left <= 2 or is_palindrome[left + 1][right - 1]):
                is_palindrome[left][right] = True 
    
    # DP to calculate the miminum cut times. 
    dp = [float("inf")] * n
    for i in range(n): 
        if is_palindrome[0][i]: 
            dp[i] = 0 
        else: 
            for j in range(i): 
                if is_palindrome[j + 1][i]: 
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]

s = "aab"
print(min_cut_palindrome(s))

"""Assignment 133: Cloned Graph. 

Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 
Test case format:

- For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
- An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
- The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example: 
    - Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    - Output: [[2,4],[1,3],[2,4],[1,3]]
"""
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
        



