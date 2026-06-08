def three_sum(nums):
    results_set = set()
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum3 = nums[left] + nums[i] + nums[right]
            if sum3 == 0:
                results_set.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum3 > 0:
                right -= 1
            else:
                left += 1
    results = []
    for elm in results_set:
        results.append(list(elm))
    return results
