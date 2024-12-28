def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high: 
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target: 
            low = mid + 1 
        else: 
            high = mid - 1 
    return -1 

if __name__ == "__main__":
    A = [1, 5, 7, 8 , 14, 17, 24, 29, 31, 34, 42]
    x = 8 
    print(binary_search(A, x))
        
        