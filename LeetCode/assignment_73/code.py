def set_zeroes(matrix):
    zero_coords = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0: 
                tmp_coord = [row, col]
                zero_coords.append(tmp_coord)
    if not zero_coords: 
        return matrix
    for row, col in zero_coords: 
        for j in range(len(matrix[0])):
            matrix[row][j] = 0 
        
        for i in range(len(matrix)):
            matrix[i][col] = 0
    return matrix
