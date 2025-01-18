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


"""Assignment 39: Combination Sum 

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example: 
- Input: candidates = [2,3,6,7], target = 7
- Ouput: [[2,2,3],[7]]
- Explaination: 
    + 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    + 7 is a candidate, and 7 = 7. These are the only two combinations.
"""
def combination_sum(candidates, target):
    def get_candidates(candidates, target, index, cur_total, result):
        if sum(cur_total) == target:
            result.append(list(cur_total))
            return 
        
        if sum(cur_total) > target: 
            return 
        
        for i in range(index, len(candidates)):
            cur_total.append(candidates[i])
            get_candidates(candidates, target, i, cur_total, result)
            cur_total.pop()
        return result 
    res = get_candidates(candidates, target, 0, [], [])
    return res

"""Assignment 40: Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example: 
- Input: candidates = [10,1,2,7,6,1,5], target = 8
- Ouput:[
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6]
        ]
"""
def combination_sum_2(candidates, target):
    def get_candidates(start, target, cur_total):
        if target == 0: 
            result.append(cur_total[:])
            return 

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]: 
                continue 
            if candidates[i] > target:
                break 
            cur_total.append(candidates[i])
            get_candidates(i + 1, target - candidates[i], cur_total)
            cur_total.pop()
    
    candidates.sort()
    result = []
    get_candidates(0, target, [])
    return result


combination_sum_2([10,1,2,7,6,1,5], 8)