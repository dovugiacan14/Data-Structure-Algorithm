"""Assignment 161. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:
    - Input: nums = [1,2,3,1]
    - Output: 2
    - Explaination: 3 is a peak element and your function should return the index number 2.

Example 2:
    - Input: nums = [1,2,1,3,5,6,4]
    - Output: 5
    - Explaination: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""
def find_peak_elem(nums): 
    max_par = max(nums)
    return nums.index(max_par)

"""Assignment 162. Maximum Gap

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
    - Input: nums = [3,6,9,1]
    - Output: 2
    - Explaination: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
    - Input: nums = [10]
    - Output: 0
    - Explaination: The array contains less than 2 elements, therefore return 0.
"""
def maximum_gap(nums):
    if len(nums) <= 1: 
        return 0
    sorted_nums = sorted(nums)
    max_gap = 0
    for i in range(len(nums) - 1): 
        gap = sorted_nums[i + 1] - sorted_nums[i]
        max_gap = gap if gap > max_gap else max_gap
    return max_gap

"""Assignment 165. Compare Version Numbers

Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. 
The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. 
If one of the version strings has fewer revisions, treat the missing revision values as 0.
Return the following:
    - If version1 < version2, return -1.
    - If version1 > version2, return 1.
    - Otherwise, Return 0 

Example 1:
    - Input: version1 = "1.2", version2 = "1.10"
    - Output: -1
    - Explaination: version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
    - Input: version1 = "1.01", version2 = "1.001"
    - Output: 0
"""
def compare_version(version1, version2): 
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    # make both versions the same length by padding with 0 
    max_len = max(len(v1), len(v2))
    v1 += [0] * (max_len - len(v1))
    v2 += [0] * (max_len - len(v2))

    for a, b in zip(v1, v2): 
        if a > b: 
            return 1 
        elif a < b: 
            return -1
    return 0

"""Assignment 166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.

Example 1:
    - Input: numerator = 1, denominator = 2
    - Output: "0.5"

Example 2:
    - Input: numerator = 2, denominator = 1
    - Output: "2"
"""

def fraction_to_decimal(numerator, denominator):
    if numerator == 0: 
        return "0"

    res = []
    
    # handle sign 
    if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
        res.append("-") 
    numerator = abs(numerator)
    denominator = abs(denominator)

    # whole part 
    res.append(str(numerator // denominator))
    remainder = numerator % denominator 

    if remainder == 0: 
        return "".join(res)
    
    # map remainder to its index in the result.
    remainder_map = {}
    while remainder_map != 0: 
        if remainder in remainder_map: 
            index = remainder_map[remainder]
            res.insert(index, "(")
            res.append(")")
            break 
            
        remainder_map[remainder] = len(res)
        remainder *= 10 
        res.append(str(remainder // denominator))
        remainder %= denominator 
    return "".join(res)


"""Assignment 167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
    - Input: numbers = [2,7,11,15], target = 9
    - Output: [1,2]

Example 2:
    - Input: numbers = [2,3,4], target = 6
    - Output: [1, 3]
"""
def two_sum(numbers, target): 
    for i in range(len(numbers) - 1): 
        for j in range(i + 1, len(numbers)): 
            if numbers[i] + numbers[j] == target: 
                return i+1, j+1
            elif numbers[i] + numbers[j] > target: 
                break 
        continue

    return -1, -1

def two_sum(numbers, target): 
    num_map = {}
    for i, num in enumerate(numbers): 
        complement = target - num
        if complement in num_map: 
            return num_map[complement] + 1, i + 1 
        num_map[num] = i
    return -1, -1 


"""Assignment 168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
    - Input: columnNumber = 28
    - Output:  "AB"

Example 2:
    - Input: columnNumber = 701
    - Output: "ZY"
"""
def convert_to_title(columnNumber):
    result = []
    while columnNumber > 0: 
        columnNumber -= 1 
        remainder = columnNumber % 26 
        result.append(chr(remainder + ord("A")))
        columnNumber //=26
    return ''.join(reversed(result))

print(convert_to_title(701))