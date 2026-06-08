
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next  

def partition(head, x): 
    # convert to list 
    tmp_arr = []
    if not head: 
        return None 
    while head: 
        tmp_arr.append(head.val)
        head = head.next

    # process 
    shorter_x, larger_x = [], []
    for item in tmp_arr: 
        if item < x: 
            shorter_x.append(item)
        else:
            larger_x.append(item)
    result_arr = shorter_x + larger_x

    # convert to ListNode 
    new_head = ListNode(result_arr[0])
    cur = new_head 
    for val in result_arr[1:]: 
        cur.next = ListNode(val)
        cur = cur.next 
    return new_head
