def four_sum(nums, target):
    results_set = set()
    n = len(nums)
    nums.sort()
    for i in range(n-3):
        for j in range(i+1, n-2):
            left = j + 1 
            right = n - 1 
            while left < right: 
                sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                if sum4 == target:
                    results_set.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1 
                    right -= 1 
                elif sum4 > target: 
                    right -= 1 
                else: 
                    left += 1
    result = []
    for elem in results_set:
        result.append(list(elem))
    return result
