class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next 
    
def merge_two_lists(list1, list2):
    if not list1 and not list2:
        return None 
    
    # convert linked list to array 
    list1_arr = []
    list2_arr = []
    while list1: 
        list1_arr.append(list1.val)
        list1 = list1.next 
    while list2:
        list2_arr.append(list2.val)
        list2 = list2.next
    
    # process 
    new_list = list1_arr + list2_arr
    new_list.sort()

    # convert list to Node 
    if not new_list: 
        return None 
    res_node = ListNode(new_list[0])
    cur = res_node
    for val in new_list[1:]:
        cur.next = ListNode(val)
        cur = cur.next 
    return res_node
