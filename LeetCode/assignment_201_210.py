from typing import Optional

"""Assignment 201: Binary Tree Right Side View
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:
- Input: left = 5, right = 7
- Output: 4

Example 2:
- Input: left= 0 , right= 0
- Output: 0

Example 3:
- Input: left = 1, right = 2147483647
- Output: 0
"""


def range_bitwise_and(left: int, right: int):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift


left = 5
right = 7
print(range_bitwise_and(left, right))

"""Assignment 202: Happy Number
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in are happy
Return true if n is a happy number, and false if not.

Example 1: 
- Input: n = 19
- Output: True
- Explaination: 
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68 
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

Example 2: 
- Input: n = 2 
- Output: False

"""
def is_happy(n):
    def calculate_sum_square(number): 
       return sum(int(c) ** 2 for c in str(number))
    
    seen = set()
    while n != 1: 
        if n in seen:
            return False 
        seen.add(n)
        n = calculate_sum_square(n)
    return True


"""Assignment 203: Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1: 
- Input head = [1,2,6,3,4,5,6], val = 6
- Output: [1,2,3,4,5]

Example 2: 
- Input: head = [7,7,7,7], val = 7
- Output: 7

"""
class ListNode: 
    def __init__(self, val, next= None):
        self.val = val 
        self.next = next 
    
def remove_elements(head: Optional[ListNode], val: int):
    if not head:
        return None 
    
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    # delete 
    new_list = [x for x in arr if x != val]
    if not new_list:
        return None 
    
    new_head = ListNode(new_list[0])
    cur = new_head
    for val in new_list[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head


"""Assignment 204: Count Primes
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1: 
- Input: n = 10
- Output: 4 
- Explaination: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2: 
- Input: n = 0
- Output: 0

Example 3: 
- Input: n = 1 
- Output: 0 

"""
# O(N^2)
def count_primes(n):
    if n < 2: 
        return 0 
    count = 0
    for i in range(2, n):
        check = 0  
        for j in range(2, i):
            if i % j == 0:
                check += 1 
        if check == 0: 
            count += 1
    return count 

# O(N.log(N))
def count_primes(n):
    if n < 2: 
        return 0 
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False 
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)

n= 10
print(count_primes(n))