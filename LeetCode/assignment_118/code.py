from collections import deque


def generate(numRows):
    res = [[1]] 

    for _ in range(1, numRows):
        prev_row = res[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j-1], prev_row[j])
        
        new_row.append(1)   # last partition
        res.append(new_row)
   
    return res
