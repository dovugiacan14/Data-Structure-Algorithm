# ĐPT: O(n^2)
def largest_rectangle(heights): 
    area_arr = []
    len_heights = len(heights)
    for i in range(len_heights): 
        j = i + 1 
        nums_left = 1
        nums_right = 1  
        while j < len_heights:
            if  heights[j] >= heights[i]: 
                nums_right += 1 
            else: 
                break  
            j += 1
        
        k = i - 1 
        while k >= 0: 
            if heights[k] >= heights[i]: 
                nums_left += 1 
            else: 
                break 
            k -= 1
        
        total_nums = nums_left + nums_right - 1
        cur_area = heights[i] * total_nums
        area_arr.append(cur_area)
    return max(area_arr)

# ĐPT: O(n)
def largest_rectangle(heights):
    stack = []
    max_area = 0 
    heights.append(0)  # padding zero
    for i in range(len(heights)): 
        while stack and heights[i] < heights[stack[-1]]: 
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1 
            max_area = max(max_area , height * width)
        stack.append(i)
    return max_area

# heights = [2,1,5,6,2,3]
# print(largest_rectangle(heights))
