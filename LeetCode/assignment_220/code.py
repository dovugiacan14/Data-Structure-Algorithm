import heapq
from sortedcontainers import SortedList

def combination_duplicate_III(nums, indexDiff, valueDiff):
    """Idea: Dùng Sorted List
    Ta cần kiểm tra trong mỗi cửa sổ Sliding Window có độ dài indexDiff, xem có phần tử nào 
    chênh lệch không quá valueDifff hay không ? 
        - Duyệt từng phần tử nums[i]
        - Trong mỗi bước, ta duy trì một cửa số các phần tử trong khoảng i - indexDiff đến i - 1 (cửa sổ trượt).
        - Với mỗi nums[i], ta cần tìm xem có tồn tại phần tử x trong cửa sổ sao cho: 
            |nums[i] - x| <= valueDiff
            <=>nums[i] - valueDiff <= x <= nums[i] + valueDiff
    """
    if valueDiff < 0 or indexDiff <= 0:
        return False 
    
    bucket_size = valueDiff + 1    # avoid division by zero 
    buckets = dict()
    
    for i, num in enumerate(nums):
        bucket_id = num // bucket_size if num >= 0 else (num + 1) // bucket_size

        if bucket_id in buckets:
            return True 
        
        if (bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff):
            return True 
        if (bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff):
            return True 
        
        # add to bucket 
        buckets[bucket_id] = num 

        # remove element too far indexDiff
        if i >= indexDiff:
            old_bucket_id = nums[i - indexDiff] // bucket_size if nums[i - indexDiff] >= 0 else (nums[i - indexDiff] + 1) // bucket_size - 1
            del buckets[old_bucket_id]

    return False


def combination_duplicate_III(nums, indexDiff, valueDiff):
    if valueDiff < 0: 
        return False 
    
    bucket = {}
    size = valueDiff + 1 

    for i, num in enumerate(nums):
        idx = num //size 

        if idx in bucket:
            return True 
        if (idx -1 in bucket and abs(num - bucket[idx - 1]) < size): 
            return True 
        if (idx + 1 in bucket and abs(num - bucket[idx + 1]) < size):
            return True 
        
        bucket[idx] = num 

        if i >= k: 
            del bucket[nums[i - k] // size]
    return False 
