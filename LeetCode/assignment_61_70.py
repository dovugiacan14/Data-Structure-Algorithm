"""Assignment 61: Rotate List

Given the head of a linked list, rotate the list to the right by k places.
Example 1: 
- Input:  head = [1,2,3,4,5], k = 2
- Ouput: [4,5,1,2,3]

Example 2: 
- Input: head = [0,1,2], k = 4
- Output: [2,0,1]
"""
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

"""Assignment 65: Valid Number 

Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", 
while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

Example 1: 
- Input:  s = "0"
- Ouput: True 

Example 2: 
- Input:  s = "e" 
- Ouput: False 
"""
import re 
def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    return re.match(pattern, s.strip()) is not None

"""Assignment 66: Plus One 

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
Example 1: 
- Input: digits = [1,2,3]
- Ouput: [1,2,4]

Example 2: 
- Input: digits = [9]
- Output: [1,0]
"""
        
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    number_str = "".join(map(str, digits))
    number = int(number_str)
    number += 1
    res = [] 
    for c in str(number): 
        res.append(int(c))
    return res

"""Assignment 67: Add Binary 
Given two binary strings a and b, return their sum as a binary string.

Example 1: 
- Input: a = "11", b = "1"
- Ouput: "100"

Example 2: 
- Input: a = "1010", b = "1011"
- Output: "10101"

Hint: bin -> convert integer to binary bit 
"""
def add_binary(a, b): 
    int_a = int(a, 2)
    int_b = int(b, 2)
    total = int_a + int_b
    binary_total = bin(total)[2:]
    return binary_total


"""Assignment 68: Text Justification
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
    + A word is defined as a character sequence consisting of non-space characters only.
    + Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    + The input array words contains at least one word.

Example 1: 
- Input: words = ["This", "is", "an", "example", "of", "text", "justification."],  maxWidth = 16
- Ouput: 
        [
        "This    is    an",
        "example  of text",
        "justification.  "
        ]

Example 2: 
- Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
- Output: 
        [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
        ]
"""
def full_jusify(words, maxWidth): 
    result = []
    line_words = []
    line_len = 0
    for word in words: 
        if line_len + len(word) + len(line_words) > maxWidth: 
            total_spaces = maxWidth - line_len
            gaps= len(line_words) - 1 
            if gaps == 0: 
                result.append(line_words[0] + " "*total_spaces)
            else: 
                space_per_gap = total_spaces // gaps 
                extra_spaces = total_spaces % gaps 
                line = ""
                for i, w in enumerate(line_words): 
                    line += w 
                    if i < gaps: 
                        line += " "*space_per_gap
                        if i < extra_spaces:
                            line += " "
                result.append(line)
            line_words, line_len = [], 0 
        line_words.append(word)
        line_len += len(word)
    last_line = " ".join(line_words)
    remaining_spaces = maxWidth - len(last_line)
    result.append(last_line + " "*remaining_spaces)
    return result

"""Assignment 69: Sqrt(x)
Given two binary strings a and b, return their sum as a binary string.

Example 1: 
- Input: x = 4 
- Ouput: 2

Example 2: 
- Input: 8
- Output: 2

"""
import math 
def my_sqrt(x):
    return int(math.sqrt(x))


"""Assignment 70: Climbing Stairs  

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1: 
- Input: n = 3
- Ouput: 3
- Explaination: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
"""
def climbing_stairs(n):
    if n == 1: 
        return 1 
    if n == 2: 
        return 2 
    return climbing_stairs(n-1) + climbing_stairs(n-2)

print(climbing_stairs(5))