from collections import OrderedDict, defaultdict

def max_points(points):
    if len(points) <= 2: 
        return len(points)
    
    def gcd(a, b): 
        """find UCLN between a and b"""
        while b: 
            a, b = b, a % b
        return a 
    
    max_result = 0 
    for i in range(len(points)): 
        slope_count = defaultdict(list)
        overlap = 0 
        curr_max = 0 
        x1, y1 = points[i]

        for j in range(i + 1, len(points)): 
            x2, y2 = points[j]
            dx = x2 - x1 
            dy = y2 - y1 

            if dx == 0 and dy ==0: 
                overlap += 1 
                continue 

            g = gcd(dx, dy)
            dx //= g 
            dy //= g 
            if dx < 0: 
                dx, dy = -dx, -dy 
            
            slope = (dy, dx)
            slope_count[slope] += 1 
            curr_max = max(curr_max, slope_count[slope])
        max_result = max(max_result, curr_max + overlap + 1)
    return max_result
