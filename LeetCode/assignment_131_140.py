
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


"""Assignment 132. Palindrome Partitioning II.

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
    - Input: s = "aab"
    - Output: 1
    - Explaination: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
    - Input: s = "ab"
    - Output: 1
"""
# ĐPT: (O(2^n))
def min_cut(s): 
    def is_palindrome(text): 
        return text == text[::-1]
    
    def partition(str):
        def generate_partition(start, path): 
            if start == len(str):
                subsets.append(path[:])
                return 

            for i in range(start + 1, len(s) + 1): 
                substring = str[start:i]
                if is_palindrome(substring): 
                    path.append(substring)
                    generate_partition(i, path)
                    path.pop()

        subsets = [] 
        generate_partition(0, [])
        return subsets

    subsets = partition(s)
    min_len = min(len(arr) for arr in subsets)
    return min_len - 1 



# ĐPT: n^2
def min_cut_palindrome(s): 
    n = len(s)
    # palindrome checking. 
    is_palindrome = [[False] * n for _ in range(n)]

    for right in range(n): 
        for left in range(right + 1): 
            if s[left] == s[right] and (right - left <= 2 or is_palindrome[left + 1][right - 1]):
                is_palindrome[left][right] = True 
    
    # DP to calculate the miminum cut times. 
    dp = [float("inf")] * n
    for i in range(n): 
        if is_palindrome[0][i]: 
            dp[i] = 0 
        else: 
            for j in range(i): 
                if is_palindrome[j + 1][i]: 
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]

s = "aab"
print(min_cut_palindrome(s))

