import numpy as np 

# 1. Create a 1D array of numbers from 4 to 9 
def create_array():
    return np.arange(4, 10)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
def create_matrix():
    return np.arange(9).reshape(3, 3)

# 3. Create a 3x3 boolean matrix 
def create_boolean_matrix():
    return np.ones((3, 3), dtype=bool)

# 4 Replace all odd numbers in the array with -1 
def replace_odd_numbers(use_case):
    data = np.arange(10)
    if use_case == 1: 
        data[data % 2 != 0] = -1 
        return data 
    else: 
        out = np.where(data % 2 == 1, -1, data)
        return out

# 5. Stack two arrays follow vertically 
def stack_arrays_vertically(use_case):
    data1 = np.arange(10).reshape(2, -1)
    data2 = np.repeat(4,10).reshape(2, -1)
    if use_case == 1: 
        out1 = np.concatenate([data1, data2], axis=0)
    elif use_case == 2: 
        out1 = np.vstack([data1, data2])
    else: 
        out1 = np.r_[data1, data2] 
    return out1 

# 6. Stack two arrays follow horizontally 
def stack_arrays_horizontally(use_case):
    data1 = np.arange(10).reshape(2, -1)
    data2 = np.repeat(4,10).reshape(2, -1)
    if use_case == 1: 
        out2 = np.concatenate([data1, data2], axis=1) 
    elif use_case == 2:
        out2 = np.hstack([data1, data2])
    else:
        out2 = np.c_[data1, data2]
    return out2

# 7. Create 2D array of shape 5x3 to contain random decimal numbers between 5 and 10 
def create_random_array():
    return np.random.uniform(5, 10, size=(5, 3))

# 8. Get the intersection of two arrays 
def get_intersection():
    data1 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    data2 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 6])
    return np.intersect1d(data1, data2)

# 9. Remove from one array those items that exist in another
def remove_from_array():
    data1 = np.array([1, 2, 3, 4, 5])
    data2 = np.array([1,5,9])
    return np.setdiff1d(data1, data2)

# 10. Get the positions where elements of two arrays match
def get_positions():
    data1 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    data2 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 6])
    return np.where(data1 == data2)

# 11. Convert lines values in array 
def convert_line_values():
    data = np.arange(9).reshape(3, 3)
    out = data[[1, 0, 2], :]
    return out

# 12. Convert column values in array
def convert_column_values():
    data = np.arange(9).reshape(3, 3)
    out = data[:, [1, 0, 2]]
    return out

# 13. Calculate the length of a vector 
def calculate_length_vector():
    data = np.array([1,2,4,2])
    return np.linalg.norm(data)

# 14. Hadamard product of two arrays 
def hadamard_product():
    data1 = np.array([1, 2, 3, 4])
    data2 = np.array([5, 6, 7, 8])
    return data1 * data2

# 15. Dot product of two arrays 
def dot_product():
    data1 = np.array([1, 2, 3, 4])
    data2 = np.array([5, 6, 7, 8])
    return np.dot(data1, data2) 

# 16. Transpose the matrix 
def transpose_matrix():
    data = np.arange(9).reshape(3, 3)
    return data.T

if __name__ == "__main__":
    print(create_array())
    print(create_matrix())
    print(create_boolean_matrix())
    print(replace_odd_numbers(2))
    print(stack_arrays_vertically(1))
    print(stack_arrays_horizontally(1))
    print(create_random_array())
    print(get_intersection())
    print(remove_from_array())
    print(get_positions())
    print(convert_line_values())
    print(convert_column_values())
    print(calculate_length_vector())
    print(hadamard_product())
    print(dot_product())
    print(transpose_matrix())