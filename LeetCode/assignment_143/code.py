from collections import OrderedDict, defaultdict

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
