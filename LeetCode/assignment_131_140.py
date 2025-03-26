
"""Assignment 131. Palindrome Partitioning 

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
    - Input: s = "aab"
    - Output: [["a","a","b"],["aa","b"]]
    - Explaination: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    - Input: s = "a"
    - Output: [["a"]]
"""
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

s = "aab"
print(partition(s))