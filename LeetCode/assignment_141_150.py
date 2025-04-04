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
