from collections import OrderedDict, defaultdict

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def insertion_sort_lst(head): 
    if not head: 
        return []
    
    head_lst = []
    while head: 
        head_lst.append(head.val)
        head = head.next
    
    sorted_head_lst = head_lst.sort()
    res_node = ListNode(sorted_head_lst[0])
    cur = res_node
    for val in sorted_head_lst[1:]: 
        cur.next = ListNode(val)
        cur = cur.next
    return res_node
