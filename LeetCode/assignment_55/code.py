def can_jump(nums):
    farthest = 0 
    for idx, elm in enumerate(nums):
        if idx > farthest: 
            return False 
        farthest = max(farthest, idx + elm)

        if farthest >= len(nums) - 1: 
            return True 
