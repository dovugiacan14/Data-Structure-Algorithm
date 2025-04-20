"""Assignment 151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Example 1:
    - Input: s = "the sky is blue"
    - Output: "blue is sky the"

Example 2:
    - Input: s = "a good   example"
    - Output: "example good a"
"""
def reverse_words(s): 
    s_split_space = s.split(" ")
    new_s = []
    for word in s_split_space: 
        if word != "": 
            new_s.insert(0, word)
    return " ".join(new_s)

"""Assignment 152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
    - Input: nums = [2,0,3,-2,4]
    - Output: 6
    - Explaination: [2,3] has the largest product 6.

Example 2:
    - Input: nums = [-2,0,-1]
    - Output: 0
"""
def max_product_subarray(nums): 
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_product * curr, min_product * curr)
        min_product = min(curr, max_product * curr, min_product * curr)
        max_product = temp_max 
        result = max(result, max_product)
    return result

def max_product_subarray(nums):
    reversed = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        reversed[i] *= reversed[i-1] or 1
    return max(nums + reversed)
nums = [2,0,3,-2,4]
print(max_product_subarray(nums))


"""Assignment 153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
    - [4,5,6,7,0,1,2] if it was rotated 4 times.
    - [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
    - Input: nums = [3,4,5,1,2]
    - Output: 1
    - Explaination: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
    - Input: nums = [4,5,6,7,0,1,2]
    - Output: 0
    - Explaination: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""
def findMin(nums): 
    return min(nums)

"""Assignment 155. Min Stack 

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
    - Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
             [[],[-2],[0],[-3],[],[],[],[]]
    - Output: [null,null,null,null,-3,null,0,-2]
"""
class MinStack(object): 
    def __init__(self): 
        self.arr = []
        self.minStack = []

    def push(self, val: int): 
        self.arr.append(val)
        if not self.minStack or val <= self.minStack[-1]: 
            self.minStack.append(val)
    
    def pop(self): 
        if self.arr[-1] == self.minStack[-1]: 
            self.minStack.pop()
        self.arr.pop()
    
    def top(self):
        return self.arr[-1]
    
    def getMin(self): 
        return self.minStack[-1]
    
class MinStack(object): 
    def __init__(self): 
        self.stack = []
    
    def push(self, val): 
        return self.stack.append(val)

    def pop(self): 
        return self.stack.pop()

    def top(self): 
        return self.stack[-1]

    def getMin(self): 
        return min(self.stack)
    
"""Assignment 160. Intersection of Two Linked Lists

iven the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
Example 1:
    - Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    - Output: Intersected at '8'

Example 2:
    - Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    - Output: Intersected at '2'
"""
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