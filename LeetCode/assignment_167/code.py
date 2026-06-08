def two_sum(numbers, target): 
    for i in range(len(numbers) - 1): 
        for j in range(i + 1, len(numbers)): 
            if numbers[i] + numbers[j] == target: 
                return i+1, j+1
            elif numbers[i] + numbers[j] > target: 
                break 
        continue

    return -1, -1

def two_sum(numbers, target): 
    num_map = {}
    for i, num in enumerate(numbers): 
        complement = target - num
        if complement in num_map: 
            return num_map[complement] + 1, i + 1 
        num_map[num] = i
    return -1, -1 
