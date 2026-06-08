# Assignment 38: Count and Say

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
