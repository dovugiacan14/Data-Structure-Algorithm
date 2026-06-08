from collections import OrderedDict, defaultdict

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
