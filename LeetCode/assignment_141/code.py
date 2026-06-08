from collections import OrderedDict, defaultdict

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
