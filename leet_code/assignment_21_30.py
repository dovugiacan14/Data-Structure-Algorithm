"""Assignment 22: Generate Parentheses 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1: 
- Input: n = 3 
- Ouput: ["((()))","(()())","(())()","()(())","()()()"]
"""
def generate_parenthesis(n):
    result = []
    def back_track(s, open, close): 
        if len(s) == 2*n:
            result.append(s)
            return 

        if open < n: 
            back_track(s + "(", open + 1, close)
        if close < open: 
            back_track(s + ")", open, close + 1)
    back_track("", 0, 0)
    return result 

test = generate_parenthesis(3)
print(0)