from collections import defaultdict 

def zigzag_conversion(s, numRows):
    result = ""
    arrays = defaultdict(list)
    if numRows == 1: 
        return s 
    
    idx_char = 1 
    n_char = 0 
    reset_flag = 1 
    
    while n_char < len(s): 
        arrays[f"arr{idx_char}"].append(s[n_char])
        if reset_flag: 
            idx_char += 1 
        else: 
            idx_char -= 1 

        if idx_char == numRows: 
            reset_flag = 0 
        if idx_char == 1: 
            reset_flag = 1 
        
        n_char += 1
    
    dict_arr = dict(arrays)
    for _, values in dict_arr.items(): 
        for char in values: 
            result += char 
    return result

result = zigzag_conversion("PAYPALISHIRING", 4)
