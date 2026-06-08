def search_matrix(matrix, target):
    for i in range(len(matrix)):
        if target in matrix[i]:
            return True
    return False
