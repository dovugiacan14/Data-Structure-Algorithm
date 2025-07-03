"""Assignment 241: Search a 2D Matrix II
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Example 1: 
- Input: expression = "2-1-1"
- Output: [0,2]
- Explaination: ((2-1)-1) = 0 and (2-(1-1)) = 2

Example 2: 
- Input: expression = "2*3-4*5"
- Output: [-34,-14,-10,-10,10]
- Explaination: 
    (2*(3-(4*5))) = -34 
    ((2*3)-(4*5)) = -14 
    ((2*(3-4))*5) = -10 
    (2*((3-4)*5)) = -10 
    (((2*3)-4)*5) = 10
"""
def diffways_to_compute(expression):
    memo = {}

    def compute(expr):
        if expr in memo:
            return memo[expr]
        
        results = []
        for i, char in enumerate(expr):
            if char in '+-*':
                left = compute(expr[:i])
                right = compute(expr[i+1:])

                for l in left:
                    for r in right:
                        if char == "+": 
                            results.append(l + r)
                        elif char == "-":
                            results.append(l - r)
                        elif char == "*":
                            results.append(l * r)
        if not results:
            results = [int(expr)]
        memo[expr] = results
    return compute(expression)