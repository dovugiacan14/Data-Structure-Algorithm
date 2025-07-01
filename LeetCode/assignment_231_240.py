"""Assignment 231: Power of Two 
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1: 
- Input: n = 1
- Output: True

Example 2: 
- Input: n = 16  
- Output: True 
"""
def is_power_true(n):
    i = 0 
    while True: 
        if 2**i < n: 
            i += 1 
        elif 2**i == n:
            return True 
        else: 
            return False 
        
"""Assignment 232: Implement Queue using Stacks 
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty)
Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.
"""
class MyQueue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.move()
        return self.out_stack.pop()
    
    def peek(self):
        self.move()
        return self.out_stack[-1]
    
    def empty(self):
        return not self.in_stack and not self.out_stack

    def move(self):
        if not self.out_stack:
            while self.in_stack: 
               self.out_stack.append(self.in_stack.pop()) 


"""Assignment 233: Count Number Digit One 
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1: 
- Input: 13
- Output: 6

Example 2: 
- Input: 0 
- Output: 0 
"""
def count_digit_one(n): 
    count = 0 
    for i in range(n+1):
        count += str(i).count("1")
    return count 

def count_digit_one(n):
    count = 0 
    factor = 1
    while n // factor > 0: 
        high = n // (factor * 10)
        cur = (n // factor) % 10 
        low = n // factor  

        if cur == 0: 
            count += high * factor 
        elif cur == 1: 
            count += high * factor + (low + 1)
        else: 
            count += (high + 1) * factor 
        
        factor *= 10
    return count 

"""Assignment 234: Palindrome Linked List 
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1: 
- Input: head = [1,2,2,1]
- Output: true

Example 2: 
- Input: head = [1,2]
- Output: false
"""

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

"""Assignment 235: Lowest Common Ancestor of a Binary Search Tree 
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1: 
- Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
- Output: 6

Example 2: 
- Input:root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
- Output: 2
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    # nếu p và q nhỏ hơn root thì duyệt về bên trái 
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # nếu p và q lớn hơn root thì duyệt về bên phải 
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.left, p, q)
    else: 
        return root
    
"""Assignment 236: Lowest Common Ancestor of a Binary Tree 
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1: 
- Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
- Output: 3

Example 2: 
- Input:root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
- Output: 5
"""
def lowest_common_ancestor_II(root, p, q):
    if root is None or root == p or root == q: 
        return root 

    left = lowest_common_ancestor_II(root.left, p, q)
    right = lowest_common_ancestor_II(root.right, p, q)

    # Nếu cả left và right đều khác None -> Node hiện tại là LCA 
    if left and right:
        return root 
    return left if left else right


"""Assignment 238: Product of Array Except Self 
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1: 
- Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
- Output: 3

Example 2: 
- Input:root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
- Output: 5
"""
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # calculate prefix 
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    
    # calculate suffix 
    r = 1 
    for i in range(n-1, -1, -1):
        answer[i] *= r
        r *= nums[i]
    return answer

nums = [1,2,3,4]
print(product_except_self(nums))

