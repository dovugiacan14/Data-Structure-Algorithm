class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next 
    
def remove_nth_from_end(head, n):
    if not head: 
        return None 
    head_lst = []
    while head: 
        head_lst.append(head.val)
        head = head.next 
    
    head_lst.pop(-n)
    if not head_lst:
        return None 
    new_head = ListNode(head_lst[0])
    cur = new_head
    for val in head_lst[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head
