"""Assignment 171. Excel Sheet Column Number. 

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
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
    - Input: columnTitle = "A"
    - Output: 1

Example 2:
    - Input: columnTitle = "AB"
    - Output: 28
"""
def title_to_number(columnTitle):
    result = 0 
    for char in columnTitle:
        result = result * 26 + (ord(char) - ord("A") + 1)
    return result 

column_title = "ZY"
print(title_to_number(column_title))


"""Assignment 172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1: 
    - Input: n = 3
    - Output: 0
    - Explanation: 3! = 6, no trailing zero.

Example 2: 
    - Input: n = 5 
    - Output: 1
    - Explaination: 5! = 120 trailing zero 
"""
def trailing_zeroes(n):
    if n == 0: 
        return 0 
    
    def factorial(x): 
        if x == 1: 
            return 1 
        return x * factorial(x - 1)
    
    output = factorial(n)
    res = 0 
    while output > 10: 
        if output % 10 != 0: 
            break 
        res += 1
        output = output // 10 

    return res 

def trailing_zeroes(n):
    res = 0 
    while n > 0: 
        n = n // 5 
        res += n
    return res

print(trailing_zeroes(10))