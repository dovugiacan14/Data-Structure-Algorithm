from collections import deque

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
