class ListNode(object): 
    def __init__(self, x): 
        self.val = x 
        self.next = None 
    
def get_intersection_node(headA, headB):
    pointA = headA 
    pointB = headB 
    while pointA != pointB: 
        pointA = pointA.next if pointA else headB 
        pointB = pointB.next if pointB else headA 
    return pointA 
