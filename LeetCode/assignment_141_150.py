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
