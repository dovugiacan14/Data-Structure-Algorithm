from collections import deque

def get_row(rowIndex): 
    num_row = rowIndex + 1
    res = [[1]]
    for _ in range(1, num_row): 
        prev_row = res[-1]
        new_row = [1]

        for j in range(1, len(prev_row)): 
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        res.append(new_row)
    return res[-1]
