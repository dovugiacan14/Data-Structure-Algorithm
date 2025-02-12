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

heights = [2,1,5,6,2,3]
print(largest_rectangle(heights))