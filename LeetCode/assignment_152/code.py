def max_product_subarray(nums): 
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_product * curr, min_product * curr)
        min_product = min(curr, max_product * curr, min_product * curr)
        max_product = temp_max 
        result = max(result, max_product)
    return result

def max_product_subarray(nums):
    reversed = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        reversed[i] *= reversed[i-1] or 1
    return max(nums + reversed)
nums = [2,0,3,-2,4]
print(max_product_subarray(nums))
