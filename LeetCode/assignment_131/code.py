def partition(s): 
    def is_palindrome(text): 
        return text == text[::-1]
    
    def generate_partition(start, path): 
        if start == len(s):
            subsets.append(path[:])
            return 
        
        for i in range(start + 1, len(s) + 1): 
            substring = s[start:i]
            if is_palindrome(substring): 
                path.append(s[start:i])
                generate_partition(i, path)
                path.pop()
        
    subsets = []
    generate_partition(0, [])
    
    return subsets
