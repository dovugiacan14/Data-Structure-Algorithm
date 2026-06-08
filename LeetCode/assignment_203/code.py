from typing import Optional
from collections import defaultdict, deque



class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int):
    if not head:
        return None

    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    # delete
    new_list = [x for x in arr if x != val]
    if not new_list:
        return None

    new_head = ListNode(new_list[0])
    cur = new_head
    for val in new_list[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head
