def maximal_rectangle(matrix): 
    if not matrix or not matrix[0]:
        return 0 
    
    n_cols = len(matrix[0])
    heights = [0] * n_cols  # initialize zero-matrix 
    result = 0 

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
    for row in matrix: 
        for col in range(n_cols): 
            heights[col] = heights[col] + 1 if row[col] == "1" else 0 
        result = max(result, largest_rectangle(heights))

    return result 
