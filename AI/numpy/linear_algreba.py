import numpy as np 

# 1. Compute the length of a vector 
def compute_vector_lenght(vector):
    return np.linalg.norm(vector)

# 2. Dot product of two vectors 
def dot_product(vector1, vector2):
    return np.dot(vector1, vector2)

# 3. Multiply a vector by a matrix 
def multiply_vector_matrix(vector, matrix):
    return np.dot(vector, matrix)

# 4. Multiply a matrix by a matrix 
def multiply_matrix_matrix(matrix1, matrix2):
    return np.dot(matrix1, matrix2) 

# 5. Matrix Inverse
def inverse_matrix(matrix):
    return np.linalg.inv(matrix) 

# 6. Eigenvalues and eigenvectors of a matrix
def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# 7. Cosine Similarity 
def cosine_similarity(vector1, vector2): 
    len_vector = len(vector1)
    dot_product_two_vectors = 0 
    for i in range(len_vector):
        dot_product_two_vectors += vector1[i] * vector2[i] 
    
    len_vector1 = 0 
    len_vector2 = 0 
    for i in range(len_vector):
        len_vector1 += vector1[i] ** 2 
        len_vector2 += vector2[i] ** 2 
    
    cos_sim = dot_product_two_vectors / (np.sqrt(len_vector1) * np.sqrt(len_vector2))
    return cos_sim
        
if __name__ == "__main__":
    print(compute_vector_lenght([1,2,7,2,4,2])) 
    print(dot_product([1,2,7],[2,4,2]))
    print(multiply_vector_matrix([1,2,7],[[2,4,2],[1,2,3],[4,5,6]]))
    print(multiply_matrix_matrix([[1,2,3],[4,5,6]],[[2,4,2],[1,2,3],[4,5,6]]))
    print(inverse_matrix([[1,2,7], [2,4,2], [4,14,24]]))
    print(compute_eigenvalues_eigenvectors([[0.9,0.2], [0.1,0.8]]))
    print(cosine_similarity([1,2,3,4],[1,0,3,0]))
