def add_binary(a, b): 
    int_a = int(a, 2)
    int_b = int(b, 2)
    total = int_a + int_b
    binary_total = bin(total)[2:]
    return binary_total
