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


"""Assignment 134. Gas Station.

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique.

Example 1:
    - Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    - Output: 3

Example 2:
    - Input: gas = [2,3,4], cost = [3,4,3]
    - Output: -1
"""
def gas_station(gas, cost):
    total_energy = 0 
    cur_energy = 0
    start = 0
    for i in range(len(gas)):
        total_energy += gas[i] - cost[i]
        cur_energy += gas[i] - cost[i]
        if cur_energy < 0: 
            start = i + 1
            cur_energy = 0
    return start if total_energy >= 0 else -1

def gas_station(gas, cost): 
    if sum(cost) > sum(gas): 
        return -1 
    
    tank = start = 0 
    for i in range(len(gas)): 
        tank += gas[i] - cost[i]
        if tank < 0: 
            tank = 0 
            start = i + 1
    return start 

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(gas_station(gas, cost))


"""Assignment 136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    - Input: nums = [2,2,1]
    - Output: 1

Example 2:
    - nums = [4,1,2,1,2]
    - Output: 4
"""
from collections import Counter 

def single_numbers(nums):
    counter = Counter(nums)
    for key, val in counter.items(): 
        if val == 1: 
            return key        


"""Assignment 137. Single Number II.

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    - Input: nums = [2,2,3,2]
    - Output: 3

Example 2:
    - Input: nums = [0,1,0,1,0,1,99]
    - Output: 99
"""
def single_number_v2(nums): 
    counter = Counter(nums)
    for key, val in counter.items(): 
        if val == 1: 
            return key
    

"""Assignment 138. Copy List with Random Pointer. 

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    - val: an integer representing Node.val
    - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
    - Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    - Output:  [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
    - Input: head = [[1,1],[2,1]]
    - Output: [[3,null],[3,0],[3,null]]
"""
class Node(object): 
    def __init__(self, x, next= None, random= None): 
        self.val = int(x)
        self.next = next 
        self.random = random  

def copy_random_lst(head): 
    if not head: 
        return None 
    
    # step1: create a mapping from original nodes to new nodes
    old_to_new = {}
    current = head 
    while current: 
        old_to_new[current] = Node(current.val)
        current = current.next
    
    # step 2: update the next and random pointers for the new nodes 
    current = head 
    while current: 
        if current.next: 
            old_to_new[current].next = old_to_new[current.next]
        if current.random: 
            old_to_new[current].random = old_to_new[current.random]
        current = current.next
    
    # step 3: return the head of the copied list 
    return old_to_new[head]


"""Assignment 139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    - Input: s = "leetcode", wordDict = ["leet","code"]
    - Output: true 

Example 2:
    - Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    - Output: false 
"""

# using dynamic programming 
def word_break(s, wordDict): 
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i): 
            if dp[j] and s[j:i] in word_set: 
                dp[i] = True 
                break
    return dp[len(s)]


"""Assignment 140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    - Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    - Output: ["cats and dog","cat sand dog"]

Example 2:
    - Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
    - Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
"""
def word_break_v2(s, wordDict):
    word_set = set(wordDict)
    memo = {}
    def backtrack(index):
        if index in memo:
            return memo[index]
        if index == len(s): 
            return [""]

        sentences = []
        for end in range(index + 1, len(s) + 1): 
            word = s[index:end]
            if word in word_set: 
                rest_sentences = backtrack(end)
                for sentence in rest_sentences: 
                    sentences.append(word + (" " + sentence if sentence else ""))
        memo[index] = sentences
        return sentences
        
    return backtrack(0)

s = "catsanddog"
word_dict =  ["cat","cats","and","sand","dog"]
print(word_break_v2(s, word_dict))