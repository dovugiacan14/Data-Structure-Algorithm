from typing import Optional
from collections import defaultdict, deque



class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    if not head:
        return None

    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    new_arr = arr[::-1]

    new_head = ListNode(new_arr[0])
    cur = new_head
    for val in new_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head
