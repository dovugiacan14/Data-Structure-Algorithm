from collections import defaultdict 

"""Assigment 1: Two Sum

        Given an array of integers nums and an integer target
        Return indices of the two numbers such that they add up to target.

        Example: 
        - Input: nums = [2, 7, 12, 15], target= 14
        - Output: [0, 2]
"""
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + i, len(nums)):
            if nums[i] + nums[j] == target: 
                return i, j 
    return -1, -1  

"""Assigment 2: Two Sum

        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.

        Example: 
        - Input: l1= [2, 4, 3], l2= [5, 6, 4]
        - Output: [7, 0, 8]
        - Explanation: 342 + 465 = 807 
"""
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

"""Assignment 3: Longest Substring without Repeating Characters 

Given a string s, find the length of the longest substring without repeating characters.

Example: 
    - Input: "abcabcbb"
    - Output: 3
    - Explanation: The answer is "abc", with the length of 3.
"""

def longest_substring(s): 
    max_len = 0 
    count = 0 
    arr = set()

    for idx, character in enumerate(s): 
        while character in arr: 
            arr.remove(s[count])
            count += 1 
        arr.add(character)
        max_len = max(max_len, idx - count + 1)
    return max_len


"""Assignment 4: Longest Substring without Repeating Characters 

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
Return the median of the two sorted arrays.

Example: 
    - Input: nums1 = [1,2], nums2 = [3,4]
    - Output: 2.50000
    - Explanation: merged array = [1,2,3,4] and median is (2 + 3) /2 = 2.5
"""
def find_median_two_array(arr1, arr2):
    merged_lst = sorted(arr1 + arr2)
    n_len = len(merged_lst)

    if n_len % 2 == 0: 
        mid = int(n_len / 2)
        return float((merged_lst[mid] + merged_lst[mid - 1]) / 2.0)
    else: 
        mid = int((n_len - 1) / 2)
        return merged_lst[mid]

"""Assignment 5: Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example: 
    - Input: s = "babad"
    - Output: "bab"
    - Explanation: "aba" is also a valid answer.
"""

def process(s, first, end): 
    while first >= 0 and end < len(s) and s[first] == s[end]: 
        first -= 1 
        end += 1 
    return s[first + 1 : end]

def longestPalindrome(s): 
    result = ""
    for idx in range(len(s)): 
        tmp = process(s, idx, idx)
        if len(tmp) > len(result):
            result = tmp 
        
        tmp = process(s, idx, idx+1)
        if len(tmp) > len(result): 
            result = tmp 
    return result



"""Assignment 6: ZigZag Conversion 

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example: 
    - Input: s = "PAYPALISHIRING" , numRows= 4
    - Output: "PINALSIGYAHRPI"
    - Explanation: 
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
"""
def zigzag_conversion(s, numRows):
    result = ""
    arrays = defaultdict(list)
    if numRows == 1: 
        return s 
    
    idx_char = 1 
    n_char = 0 
    reset_flag = 1 
    
    while n_char < len(s): 
        arrays[f"arr{idx_char}"].append(s[n_char])
        if reset_flag: 
            idx_char += 1 
        else: 
            idx_char -= 1 

        if idx_char == numRows: 
            reset_flag = 0 
        if idx_char == 1: 
            reset_flag = 1 
        
        n_char += 1
    
    dict_arr = dict(arrays)
    for _, values in dict_arr.items(): 
        for char in values: 
            result += char 
    return result

result = zigzag_conversion("PAYPALISHIRING", 4)
print(0)
