from collections import OrderedDict

"""Assignment 141. Linked List Cycle 

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Example 1:
    - Input: head = [3,2,0,-4], pos = 1
    - Output: True

Example 2:
    - Input: head = [1,2], pos = 0
    - Output: True 
"""
class Node(object):
    def __init__(self, val):
        self.val = val 
        self.next = None  

def has_cycle(head):
    fast = head 
    slow = head 
    while fast and fast.next: 
        fast = fast.next.next
        slow = slow.next 

        if fast == slow: 
            return True 
    return False 

"""Assignment 142. Linked List Cycle 

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
    - Input: head = [3,2,0,-4], pos = 1
    - Output: tail connects to node index 1

Example 2:
    - Input: head = [1,2], pos = 0
    - Output: tail connects to node index 0
"""
def detect_cycle(head):
    if not head or not head.next: 
        return None 
    
    slow = head
    fast = head 

    # step 1: detect if a cycle exists 
    while fast and fast.next: 
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast: 
            # step 2: find entry point of the cycle 
            slow = head 
            while slow != fast: 
                slow = slow.next 
                fast = fast.next 
            return slow 
    return None  # no cycle 

"""Assignment 143. Reorder List 

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    - Input: head = [1,2,3,4]
    - Output: [1,4,2,3]

Example 2:
    - Input: head = [1,2,3,4,5]
    - Output: [1,5,2,4,3]
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head): 
    if not head: 
        return None 
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, curr = None, slow.next
    slow.next = None  # Split the list into two halves
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Step 3: Merge the two halves alternately
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2  

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
reorder_list(head)

"""Assignment 144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
    - Input: root = [1,null,2,3]
    - Output: [1, 2, 3]

Example 2:
    - Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    - Output: [1,2,4,5,6,7,3,8,9]
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def preorder_traversal(root):
    if not root: 
        return []
    
    stack, output = [root], []
    while stack: 
        node = stack.pop()
        if node: 
            output.append(node.val)

            if node.right: 
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)
    return output

def preorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return 
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result

"""Assignment 145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
    - Input: root = [1,null,2,3]
    - Output: [3,2,1]

Example 2:
    - Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    - Output: [4,6,7,5,2,9,8,3,1]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def post_order_traversal(root):
    result = []
    def dfs(node):
        if not node: 
            return 
        
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
print(post_order_traversal(root))


"""Assignment 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
    - Input: 
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    - Output: 
            [null, null, null, 1, null, -1, null, -1, 3, 4]
"""
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache: 
            return  -1 
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache: 
            self.cache.move_to_end(key)
        self.cache[key] = value 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last= False)

commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

res= []
obj = None 
for cmd, arg in zip(commands, args): 
    if cmd == "LRUCache": 
        obj = LRUCache(*arg)
        res.append(None)
    elif cmd == "put":
        obj.put(*arg)
        res.append(None)
    elif cmd == "get": 
        res.append(obj.get(*arg))
print(res)


"""Assignment 147. Insertion Sort List 

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The steps of the insertion sort algorithm:
    1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list. 
    2. at each iteration, insertion sort removes one element from the input data, finds the location it 
belongs within the sorted list and inserts it there.
    3. It repeats until no input elements remain. 

Example 1:
    - Input: head = [4, 2, 1, 3]
    - Output: [1, 2, 3, 4] 

Example 2:
    - Input: head = [-1,5,3,4,0]
    - Output: [-1, 0, 3, 4, 5]
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def insertion_sort_lst(head): 
    if not head: 
        return []
    
    head_lst = []
    while head: 
        head_lst.append(head.val)
        head = head.next
    
    sorted_head_lst = head_lst.sort()
    res_node = ListNode(sorted_head_lst[0])
    cur = res_node
    for val in sorted_head_lst[1:]: 
        cur.next = ListNode(val)
        cur = cur.next
    return res_node
    pass 