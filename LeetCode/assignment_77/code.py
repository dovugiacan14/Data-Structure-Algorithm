def combinations(n, k):
    def backtrack(start, sub_arr): 
        if len(sub_arr) == k: 
            result.append(sub_arr[:])
            return 
        
        for i in range(start, n+1): 
            sub_arr.append(i)
            backtrack(i + 1, sub_arr)
            sub_arr.pop()

    result = []
    backtrack(1, [])
    return result
