# Assignment 85: Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Example 1: 
- Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
- Output: 6
- Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2: 
- Input: matrix = [["0"]]
- Output: 0

Idea: 
    1. Iterate through each row of the matrix and construct a "heights array" representing a histogram. 
    2. Treat each row as a histogram and use "Largest Rectangle in Histogram" (as 84) to find the largest rectangle.
    3. Repeat for all rows while keeping track of the maximun area. 
Approach: 
    matrix = [                             
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],     
        ["1","0","0","1","0"]
    ]
 ==>     
    heights = [                             
        ["1","0","1","0","0"],
        ["2","0","2","1","1"],
        ["3","1","3","2","2"],     
        ["4","0","0","3","0"]
    ]
