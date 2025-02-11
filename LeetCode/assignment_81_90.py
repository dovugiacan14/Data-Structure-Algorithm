"""Assignment 81: Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1: 
- Input: head = [1,2,3,3,4,4,5]
- Output: [1,2,5]

Example 2: 
- Input: head = [1,1,1,2,3]
- Output: [1,2,3]
"""
from collections import Counter
class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val 
        self.next= next

def delete_duplicates(head): 
    # convert list node to array 
    tmp_arr = list()
    result_arr = list()
    if not head: 
        return None 
    while head: 
        tmp_arr.append(head.val)
        head = head.next 
    
    count_dict = Counter(tmp_arr)
    for key, val in count_dict.items():
        if val == 1: 
            result_arr.append(key)
    if not result_arr: 
        return None 
    result_arr.sort()
    # convert result to node 
    new_head = ListNode(result_arr[0])
    cur = new_head
    for val in result_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head

"""Assignment 82: Remove Duplicates from Sorted List 

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1: 
- Input: head = [1,1,2]
- Output: [1,2]

Example 2: 
- Input: head = [1,1,2,3,3]
- Output: [1,2,3]
"""

class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val 
        self.next= next

def delete_duplicates(head): 
    # convert list node to array 
    tmp_arr = list()
    result_arr = list()
    if not head: 
        return None 
    while head: 
        tmp_arr.append(head.val)
        head = head.next 
    
    result_arr = list(set(tmp_arr))
    if not result_arr: 
        return None 
    result_arr.sort()
    # convert result to node 
    new_head = ListNode(result_arr[0])
    cur = new_head
    for val in result_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head