from collections import deque

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    head = root 
    while head and head.left: 
        curr = head  
        while curr: 
            curr.left.next = curr.right   # link left child -> right child 
            if curr.next: 
                curr.right.next = curr.next.left 
            curr = curr.next   # move to next node in the current level 
        head = head.left
    return root 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connect(root)
