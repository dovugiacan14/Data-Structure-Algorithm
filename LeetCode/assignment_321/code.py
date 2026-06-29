def maxNumber(nums1, nums2, k):
    # get max subsequence with length k 
    def max_subsequence(nums, k): 
        drop = len(nums) - k 
        stack = []

        for num in nums: 
            while drop and stack and stack[-1] < num: 
                stack.pop()
                drop -= 1 
            stack.append(num)
        return stack[:k]
    
    # merge two sebsequence 
    def merge(a, b): 
        res = []
        while a or b: 
            if a > b: 
                res.append(a[0])
                a = a[1:]
            else: 
                res.append(b[0])
                b = b[1:]
        return res 
    
    # try each k 
    best = []
    start = max(0, k - len(nums2))
    end = min(k, len(nums1))

    for i in range(start, end + 1):
        part1 = max_subsequence(nums1, i)
        part2 = max_subsequence(nums2, k - i)

        candidate = merge(part1, part2)
        if candidate > best:
            best = candidate

    return best

if __name__=="__main__": 
    nums1 = [3, 4, 6, 5] 
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5 
    print(maxNumber(nums1, nums2, k))
    