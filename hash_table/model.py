def hash_function(key, table_size):
    hash_value = 0 

    for char in key: 
        hash_value += ord(char)
    
    return hash_value % table_size 

if __name__ == "__main__":
    key = "example_key"
    table_size = 10 
    hash_value = hash_function(key, table_size= table_size)
    print(hash_value)