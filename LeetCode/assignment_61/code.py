class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next 

def rotate_right(head, k):
    if not head: 
        return None 

    head_lst = []
    while head: 
        head_lst.append(head.val)
        head = head.next 
    
    tmp_arr= []
    k = k % len(head_lst)
    tmp_arr.extend(head_lst[-k:] + head_lst[:-k])
    
    if not tmp_arr: 
        return None 
    new_head = ListNode(tmp_arr[0])
    cur = new_head
    for val in tmp_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head

head_lst = [1,2]
k = 0
tmp_arr= []
k = k % len(head_lst)
tmp_arr.extend(head_lst[-k:] + head_lst[:-k])
print(tmp_arr)
