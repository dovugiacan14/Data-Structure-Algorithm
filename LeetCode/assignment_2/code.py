from collections import defaultdict 

class ListNode(object): 
    def __init__(self, val= 0, next= None): 
        self.val = val 
        self.next= next 
    
def addTwoNumbers(l1, l2): 
    resultNode = ListNode()
    temp = resultNode

    while l1 or l2: 
        total, carrier = 0, 0 
        if l1: 
            total = l1.val 
            l1 = l1.next
        if l2: 
            total += l2.val 
            l2 = l2.next 
        
        total += temp.val 
        if total > 9: 
            carrier = int(total / 10)
            total %= 10 
        temp.val = total 
        if not carrier and not l1 and not l2: 
            return resultNode

        temp.next = ListNode()
        temp = temp.next
        temp.val = carrier
    return resultNode
