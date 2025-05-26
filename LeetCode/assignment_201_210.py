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
