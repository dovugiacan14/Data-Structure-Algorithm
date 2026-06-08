class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next 
    
def merge_k_lists(lists):
    result_arr = list()
    for arr in lists: 
        while arr: 
            result_arr.append(arr.val)
            arr = arr.next
    result_arr.sort()
    if not result_arr: 
        return None 
    result_node = ListNode(result_arr[0])
    cur = result_node
    for val in result_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next 
    return result_node
