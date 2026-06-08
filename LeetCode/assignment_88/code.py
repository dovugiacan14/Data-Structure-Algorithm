def merge(nums1, m, nums2, n): 
    del nums1[m:]
    nums1.extend(nums2)
    return nums1.sort()
