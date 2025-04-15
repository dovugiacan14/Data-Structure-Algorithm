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