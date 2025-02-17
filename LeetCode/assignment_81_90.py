"""Assignment 81: Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1: 
- Input: head = [1,2,3,3,4,4,5]
- Output: [1,2,5]

Example 2: 
- Input: head = [1,1,1,2,3]
- Output: [1,2,3]
"""
from collections import Counter
class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val 
        self.next= next

def delete_duplicates(head): 
    # convert list node to array 
    tmp_arr = list()
    result_arr = list()
    if not head: 
        return None 
    while head: 
        tmp_arr.append(head.val)
        head = head.next 
    
    count_dict = Counter(tmp_arr)
    for key, val in count_dict.items():
        if val == 1: 
            result_arr.append(key)
    if not result_arr: 
        return None 
    result_arr.sort()
    # convert result to node 
    new_head = ListNode(result_arr[0])
    cur = new_head
    for val in result_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head

"""Assignment 82: Remove Duplicates from Sorted List 

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1: 
- Input: head = [1,1,2]
- Output: [1,2]

Example 2: 
- Input: head = [1,1,2,3,3]
- Output: [1,2,3]
"""

class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val 
        self.next= next

def delete_duplicates(head): 
    # convert list node to array 
    tmp_arr = list()
    result_arr = list()
    if not head: 
        return None 
    while head: 
        tmp_arr.append(head.val)
        head = head.next 
    
    result_arr = list(set(tmp_arr))
    if not result_arr: 
        return None 
    result_arr.sort()
    # convert result to node 
    new_head = ListNode(result_arr[0])
    cur = new_head
    for val in result_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head


"""Assignment 84: Largest Rectangle in Histogram 

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1: 
- Input: heights = [2,1,5,6,2,3]
- Output: 10
- Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2: 
- Input: heights = [2,4]
- Output: 4
"""
# ĐPT: O(n^2)
def largest_rectangle(heights): 
    area_arr = []
    len_heights = len(heights)
    for i in range(len_heights): 
        j = i + 1 
        nums_left = 1
        nums_right = 1  
        while j < len_heights:
            if  heights[j] >= heights[i]: 
                nums_right += 1 
            else: 
                break  
            j += 1
        
        k = i - 1 
        while k >= 0: 
            if heights[k] >= heights[i]: 
                nums_left += 1 
            else: 
                break 
            k -= 1
        
        total_nums = nums_left + nums_right - 1
        cur_area = heights[i] * total_nums
        area_arr.append(cur_area)
    return max(area_arr)

# ĐPT: O(n)
def largest_rectangle(heights):
    stack = []
    max_area = 0 
    heights.append(0)  # padding zero
    for i in range(len(heights)): 
        while stack and heights[i] < heights[stack[-1]]: 
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1 
            max_area = max(max_area , height * width)
        stack.append(i)
    return max_area

# heights = [2,1,5,6,2,3]
# print(largest_rectangle(heights))

"""Assignment 85: Maximal Rectangle 

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Example 1: 
- Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
- Output: 6
- Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2: 
- Input: matrix = [["0"]]
- Output: 0

Idea: 
    1. Iterate through each row of the matrix and construct a "heights array" representing a histogram. 
    2. Treat each row as a histogram and use "Largest Rectangle in Histogram" (as 84) to find the largest rectangle.
    3. Repeat for all rows while keeping track of the maximun area. 
Approach: 
    matrix = [                             
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],     
        ["1","0","0","1","0"]
    ]
 ==>     
    heights = [                             
        ["1","0","1","0","0"],
        ["2","0","2","1","1"],
        ["3","1","3","2","2"],     
        ["4","0","0","3","0"]
    ]
"""
def maximal_rectangle(matrix): 
    if not matrix or not matrix[0]:
        return 0 
    
    n_cols = len(matrix[0])
    heights = [0] * n_cols  # initialize zero-matrix 
    result = 0 

    def largest_rectangle(heights):
        stack = []
        max_area = 0 
        heights.append(0)  # padding zero
        for i in range(len(heights)): 
            while stack and heights[i] < heights[stack[-1]]: 
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1 
                max_area = max(max_area , height * width)
            stack.append(i)
        return max_area
    for row in matrix: 
        for col in range(n_cols): 
            heights[col] = heights[col] + 1 if row[col] == "1" else 0 
        result = max(result, largest_rectangle(heights))

    return result 

"""Assignment 86: Partition List 

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1: 
- Input: head = [1,4,3,2,5,2], x = 3
- Output: [1,2,2,4,3,5]

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next  

def partition(head, x): 
    # convert to list 
    tmp_arr = []
    if not head: 
        return None 
    while head: 
        tmp_arr.append(head.val)
        head = head.next

    # process 
    shorter_x, larger_x = [], []
    for item in tmp_arr: 
        if item < x: 
            shorter_x.append(item)
        else:
            larger_x.append(item)
    result_arr = shorter_x + larger_x

    # convert to ListNode 
    new_head = ListNode(result_arr[0])
    cur = new_head 
    for val in result_arr[1:]: 
        cur.next = ListNode(val)
        cur = cur.next 
    return new_head

"""Assignment 88: Partition List 

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

- Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
- Output: nums1= [1,2,2,3,5,6]

"""
def merge(nums1, m, nums2, n): 
    del nums1[m:]
    nums1.extend(nums2)
    return nums1.sort()

"""Assignment 89: Gray Code 

An n-bit gray code sequence is a sequence of 2n integers where:
    + Every integer is in the inclusive range [0, 2n - 1],
    + The first integer is 0,
    + An integer appears no more than once in the sequence,
    + The binary representation of every pair of adjacent integers differs by exactly one bit, and
    + The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

- Input: n = 2 
- Output: [0,1,3,2]
- Explaination: 
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit

"""
def gray_code(n): 
    result = 0 
    for i in range(n): 
        result += [x | (1 << i) for x in reversed(result)]
    return result 

def gray_code(n): 
    return [i ^ (i >> 1) for i in range(1 << n)]


"""Assignment 90: Subsets II  

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

- Input: nums = [1,2,2]
- Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""
def subset_version2(nums): 
    def backtrack(pos, subset): 
        result.append(subset[:])
        
        if len(subset) == len(nums): 
            return 
        
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]: 
                continue 
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

    nums.sort()
    result = []
    backtrack(0, [])
    return result     

nums = [4,4,4,1,4]
print(subset_version2(nums))
