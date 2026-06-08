def search_matrix(matrix, target):
    n_row = len(matrix)
    i = 0 
    while i < n_row: 
        if target > matrix[i][-1]: 
            i += 1 
        else: 
            if target in matrix[i]: 
                return True 
            else: 
                break 
    return False 
