def firstBadVersion(n): 
    left = 0 
    right = n 
    anwser = -1 

    while left <= right: 
        mid = left + (right - left) // 2 
        if isBadVersion(mid): 
            right = mid - 1 
            answer = mid 
        else: 
            left = mid + 1 
    return answer
    