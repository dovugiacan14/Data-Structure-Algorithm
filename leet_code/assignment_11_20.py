"""Assignment 11: Container with Most Water 

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Example: 
    - Input: height = [1,8,6,2,5,4,8,3,7]
    - Output: 49
    - Explanation:  
    The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
    In this case, the max area of water (blue section) the container can contain is 49.
"""


def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < height:
        cur_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, cur_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


"""Assignment 12: Integer to Roman 

Seven different symbols represent Roman numerals with the following values:
Symbols: 
I -> 1 
V -> 5 
X -> 10
L -> 50 
C -> 100 
D -> 500 
M -> 100 

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

Example 1: 
- Input: 3749 
- Ouput: "MMMDCCXLIX" 
- Exaplaination: 
    3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
    700 = DCC as 500 (D) + 100 (C) + 100 (C)
    40 = XL as 10 (X) less of 50 (L)
    9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
"""


def intToRoman(num):
    num_str = str(num)
    n = len(num_str)
    arr_roman_part = []
    for idx, digit in enumerate(num_str, start=1):
        digit = int(digit)
        section_unit = n - idx
        if digit == 0:
            continue
        # thousand unit
        if section_unit == 3:
            text = "M" * digit
            arr_roman_part.append(text)
        # hundreds unit
        if section_unit == 2:
            if digit == 9:
                text = "CM"
            elif digit == 4:
                text = "CD"
            elif digit == 5:
                text = "D"
            elif digit == 1:
                text = "C"
            elif digit > 5 and digit < 9:
                offset = digit - 5
                text = "D" + "C" * offset
            else:
                text = "C" * digit
            arr_roman_part.append(text)
        # tenths unit
        if section_unit == 1:
            if digit == 1:
                text = "X"
            elif digit == 4:
                text = "XL"
            elif digit == 5:
                text = "L"
            elif digit == 9:
                text = "XC"
            elif digit > 5 and digit < 9:
                offset = digit - 5
                text = "L" + "X" * offset
            else:
                text = "X" * digit
            arr_roman_part.append(text)
        # unit
        if section_unit == 0:
            if digit == 1:
                text = "I"
            elif digit == 4:
                text = "IV"
            elif digit == 5:
                text = "V"
            elif digit == 9:
                text = "IX"
            elif digit > 5 and digit < 9:
                offset = digit - 5
                text = "V" + "I" * offset
            else:
                text = "I" * digit
            arr_roman_part.append(text)
    return "".join(arr_roman_part)


"""Assignment 13: Roman to Integer

Seven different symbols represent Roman numerals with the following values:
Symbols: 
I -> 1 
V -> 5 
X -> 10
L -> 50 
C -> 100 
D -> 500 
M -> 100 

Example 1: 
- Input: "LVIII"
- Ouput: 58
- Exaplaination: 
    L = 50, V= 5, III = 3.
"""


def roman_to_int(s):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = (
        s.replace("IV", "IIII")
        .replace("IX", "VIIII")
        .replace("XL", "XXXX")
        .replace("XC", "LXXXX")
        .replace("CD", "CCCC")
        .replace("CM", "DCCCC")
    )
    arr = []
    for i in s:
        arr.append(i)
    for idx in range(len(arr)):
        arr[idx] = int(dic[arr[idx]])
    return sum(arr)


"""Assignment 14: Longest Common Prefix 

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1: 
- Input: strs = ["flower","flow","flight"]
- Ouput: "fl"

"""


def longestCommonPrefix(strs):
    strs = sorted(strs)
    head = strs[0]
    tail = strs[-1]
    min_word = min(len(head), len(tail))
    res = ""
    for i in range(min_word):
        if head[i] != tail[i]:
            return res
        else:
            res += head[i]
    return res


res = longestCommonPrefix(["flower", "flow", "flight"])


"""Assignment 15: 3Sum 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0

- Input: nums = [-1, 0, 1, 2, -1, -4]
- Output:  [[-1,-1,2],[-1,0,1]] 
- Explaination: 
"""
def three_sum(nums):
    results_set = set()
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum3 = nums[left] + nums[i] + nums[right]
            if sum3 == 0:
                results_set.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum3 > 0:
                right -= 1
            else:
                left += 1
    results = []
    for elm in results_set:
        results.append(list(elm))
    return results


"""Assignment 16: 3Sum Closet 
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

- Input:  nums = [-1,2,1,-4], target = 1
- Output: 2
- Explaination: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
def threeSumCloset(nums, target):
    nums.sort()
    n = len(nums)
    result = nums[0] + nums[1] + nums[2]
    if result > target: 
        return result 
    for i in range(n - 2):
        left = i + 1 
        right = n - 2 
        while left < right: 
            sum3 = nums[i] + nums[left] + nums[right]  
            if sum3 < target: 
                left += 1 
            elif sum3 > target: 
                right -= 1 
            else: 
                return target
            if abs(sum3 - target) < abs(result - target):
                result = sum3
    return result  

"""Assignment 17: Letter Combination of a Phone Number 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

- Input: "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
- Explaination: 

"""
def letterCombination(digits): 
    encode_number_phone = {
        '2': 'abc', 
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []
    if not digits: 
        return result 
    
    def backtrack(combination, netx_digits):
        if not netx_digits:
            result.append(combination)
            return 
        
        for letter in encode_number_phone[netx_digits[0]]:
            backtrack(combination + letter, netx_digits[1:])
    backtrack("", digits)
    return result

"""Assignment 18: 4Sum
Given an array nums of n integers, 
Return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n 
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

- Input: nums = [1,0,-1,0,-2,2], target = 0
- Ouput: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
def four_sum(nums, target):
    results_set = set()
    n = len(nums)
    nums.sort()
    for i in range(n-3):
        for j in range(i+1, n-2):
            left = j + 1 
            right = n - 1 
            while left < right: 
                sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                if sum4 == target:
                    results_set.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1 
                    right -= 1 
                elif sum4 > target: 
                    right -= 1 
                else: 
                    left += 1
    result = []
    for elem in results_set:
        result.append(list(elem))
    return result

