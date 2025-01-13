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
        cur_area = min(height[left], height[right]) * (right-left)
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
    for idx, digit in enumerate(num_str, start= 1):
        digit = int(digit)
        section_unit = n - idx 
        if digit == 0:
            continue
        # thousand unit
        if section_unit == 3: 
            text = 'M'*digit
            arr_roman_part.append(text)
        # hundreds unit 
        if section_unit == 2:
            if digit == 9: 
                text = 'CM'
            elif digit == 4: 
                text = 'CD'
            elif digit == 5: 
                text = 'D'
            elif digit == 1:
                text = 'C'
            elif digit > 5 and digit < 9 : 
                offset = digit - 5 
                text = 'D' + 'C'*offset
            else: 
                text = 'C'*digit
            arr_roman_part.append(text)
        # tenths unit 
        if section_unit == 1: 
            if digit == 1:
                text = 'X'
            elif digit == 4:
                text = 'XL'
            elif digit == 5:
                text = 'L'
            elif digit == 9:
                text = 'XC'
            elif digit > 5 and digit < 9: 
                offset = digit - 5  
                text = 'L' + 'X'*offset 
            else: 
                text = 'X' * digit 
            arr_roman_part.append(text)
        # unit 
        if section_unit == 0: 
            if digit == 1: 
                text = 'I'
            elif digit == 4: 
                text = 'IV'
            elif digit == 5: 
                text = 'V'
            elif digit == 9:
                text = 'IX'
            elif digit > 5 and digit < 9:
                offset = digit - 5  
                text = 'V' + 'I'*offset
            else: 
                text = 'I' * digit 
            arr_roman_part.append(text)
    return  ''.join(arr_roman_part)   

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
    dic = {
        'I': 1, 
        'V':5, 
        'X':10,
        'L': 50, 
        'C': 100, 
        'D':500, 
        'M': 1000
    }
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
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
        else: res += head[i]
    return res

res = longestCommonPrefix(["flower","flow","flight"])