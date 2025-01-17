"""Assignment 32 
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.
Example: 
- Input:  s = ")()())"
- Output: 4 
- Explaination: The longest valid parenthesis substring is "()()"

Example: 
- Input: s = "()(()"
- Output: 2  
"""
def longest_valid_parenthesis(s): 
    stack = [-1]
    max_length = 0 

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else: 
            stack.pop()
            if not stack: 
                stack.append(i)
            else: 
                max_length = max(max_length , i - stack[-1])

    return max_length    

"""Assignment 38: Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    - countAndSay(1) = "1"
    - countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Example: 
- Input: n= 4
- Ouput: "1211"
- Explaination: 
    + countAndSay(1) = "1"
    + countAndSay(2) = RLE of "1" = "11"
    + countAndSay(3) = RLE of "11" = "21"
    + countAndSay(4) = RLE of "21" = "1211"
"""
def count_and_convert(text): 
    if not text: 
        return ""
    
    result = []
    count = 1 
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else: 
            result.append(f"{count}{text[i - 1]}")
            count = 1
    result.append(f"{count}{text[-1]}")
    return "".join(result)

def count_and_say(n): 
    if n == 1: 
        return "1"
    return count_and_convert(count_and_say(n-1))

