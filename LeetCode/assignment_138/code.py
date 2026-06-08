class Node(object): 
    def __init__(self, x, next= None, random= None): 
        self.val = int(x)
        self.next = next 
        self.random = random  

def copy_random_lst(head): 
    if not head: 
        return None 
    
    # step1: create a mapping from original nodes to new nodes
    old_to_new = {}
    current = head 
    while current: 
        old_to_new[current] = Node(current.val)
        current = current.next
    
    # step 2: update the next and random pointers for the new nodes 
    current = head 
    while current: 
        if current.next: 
            old_to_new[current].next = old_to_new[current.next]
        if current.random: 
            old_to_new[current].random = old_to_new[current.random]
        current = current.next
    
    # step 3: return the head of the copied list 
    return old_to_new[head]
