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