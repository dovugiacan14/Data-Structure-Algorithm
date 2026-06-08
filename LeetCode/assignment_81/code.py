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
