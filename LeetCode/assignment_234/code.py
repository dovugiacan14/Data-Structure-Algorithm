
class ListNode(object):
    def __init__(self, val= 0, next= None):
        self.val = val 
        self.next = next 
    
def isPalindorme(head):
    if not head: 
        return False 
    
    arr = []
    while head: 
        arr.append(head.val)
        head = head.next 
    
    reversed_arr = arr[::-1]
    if arr == reversed_arr:
        return True 
    return False 
