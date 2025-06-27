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