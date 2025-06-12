import heapq

"""Assignment 211: Design Add and Search Words Data Structure.
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:

WordDictionary(): Initializes the object.
void addWord(word): Adds word to the data structure, it can be matched later.
bool search(word): Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._search_recursive(word, 0, self.root)

    def _search_recursive(self, word, index, node):
        if index == len(word):
            return node.is_end

        char = word[index]
        if char == ".":
            for child in node.children.values():
                if self._search_recursive(word, index + 1, child):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self._search_recursive(word, index + 1, node.children[char])

"""Assignment 212: Word Search II 
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

- Input: board = [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ],

        words = ["oath","pea","eat","rain"]

- Output: ["eat","oath"]
"""
class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.word = None 

def word_search(board, words):
    """Hướng làm: 
    1. Xây dựng một Trie để lưu danh sách các từ (words) -> giúp kiểm tra prefix nhanh. 
    2. Duyệt từng ô trên bảng (board) và thực hiện DFS nếu ô đó là ký tự bắt đầu của bất kỳ từ nào trong Trie. 
    3. Trong quá trình DFS, đánh dấu những ô đã đi qua (để tránh dùng lại). 
    4. Nếu đến một node của Trie có word != None -> Thêm từ đó vào ô kết quả
    """
    # Build a Trie to save list words in words 
    root = TrieNode()
    for word in words: 
        node = root 
        for ch in word: 
            if ch not in node.children: 
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word
    
    m, n = len(board), len(board[0])
    result = []

    def dfs(x, y, node):
        ch = board[x][y]
        if ch not in node.children: 
            return 
        
        next_node = node.children[ch]
        if next_node.word: 
            result.append(next_node.word)
            next_node.word = None # avoid duplicate 
        
        # Mark visited cell 
        board[x][y] = "#"
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != "#":
                dfs(nx, ny, next_node)
        board[x][y] = ch   # restore after DFS 
    
    for i in range(m): 
        for j in range(n): 
            dfs(i, j, root)
    return result

"""Assignment 213: House Robber II 
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.


Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1: 
- Input: nums = [2,3,2]
- Output: 3
- Explaination: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2: 
- Input: nums = [1,2,3,1]
- Output: 4 
- Explaination: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4

"""

# Use Dynamic Programming 
def rob(nums): 
    """Phân tích
    Vì không thể cướp cả nhà đầu tiên và nhà cuối cùng cùng lúc, ta chia bài toán thành hai trường hợp: 
    1. Không cướp nhà đầu tiên -> Xét dãy nums[1:]
    2. Không cướp nhà cuối cùng -> Xét dãy nums[:-1]
    Sau đó, với mỗi trường hợp, ta dùng thuật toán House Robber I để tìm ta số tiền tối đa,
    và cuối cùng lấy giá trị lớn nhất giữa hai trường hợp đó. 
    """
    if not nums: 
        return 0 
    if len(nums) == 1: 
        return nums[0]
    
    def rob_linear(houses): 
        prev1, prev2 = 0, 0 
        for amount in houses: 
            curr = max(prev1, prev2 + amount)
            prev2 = prev1 
            prev1 = curr
        return prev1
    
    case1 = rob_linear(nums[:-1])
    case2 = rob_linear(nums[1:])

    return max(case1, case2)

"""Assignment 214: House Robber II 
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solvw it without sorting ? 

Example 1: 
- Input: nums = [3,2,1,5,6,4], k = 2
- Output: 5

Example 2: 
- Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
- Output: 4 

"""
def find_kth_largest(nums, k):
    max_k = 0 
    for i in range(k): 
        max_k = max(nums)
        nums.remove(max_k)
    return max_k

def find_kth_largest(nums, k):
    """Ý tưởng: 
    - Sử dụng min-heap kích thước k để giữ k phần tử lớn nhất. 
    - Phần tử nhỏ nhất trong heap này chính là k-th largest. 
    """
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    return min_heap[0]

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(find_kth_largest(nums, k))

"""Assignment 216: Combination Sum III
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    - Only numbers 1 through 9 are used.
    - Each number is used at most once

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1: 
- Input: k = 3, n = 7
- Output: [[1,2,4]]
- Explaination: 1 + 2 + 4 = 7 
There are no other valid combinations.

Example 2: 
- Input: k = 3, n = 9
- Output: [[1,2,6],[1,3,5],[2,3,4]] 
- Explaination: 
    1 + 2 + 6 = 9
    1 + 3 + 5 = 9
    2 + 3 + 4 = 9
There are no other valid combinations.

"""
def combination_sum_III(k, n):
    def backtrack(start, target, path): 
        if len(path) == k: 
            if target == 0: 
                results.append(path[:])
            return 

        for i in range(start, 10):
            if i > target: 
                break 
            path.append(i)
            backtrack(i + 1, target - i, path)
            path.pop()

    results = []
    backtrack(1, n, [])
    return results

k = 3
n= 9 
print(combination_sum_III(k, n))

"""Assignment 217: Constains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1: 
- Input: nums = [1, 2, 3, 1]
- Output: True
- Explaination: The element 1 occurs at the indices 0 and 3. 

Example 2: 
- Input: nums = [1,2,3,4]
- Output: False
- Explaination: All elements are distinct.

"""
def contain_duplicates(nums):
    format_nums = list(set(nums))
    return True if len(format_nums) != len(nums) else False

"""Assignment 219: Constains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1: 
- Input: nums = [1,2,3,1], k = 3
- Output: True

Example 2: 
- Input: nums = [1,2,3,1,2,3], k = 2
- Output: False

Example 3: 
- Input: nums = [1, 0, 1, 1], k = 1
- Output: True

"""
def contain_duplicate_II(nums, k): 
    def contain_duplicates(nums):
        format_nums = list(set(nums))
        return True if len(format_nums) != len(nums) else False

    for i in range(len(nums) - k): 
        consider_nums = nums[i : i+k+1]
        if contain_duplicates(consider_nums): 
            return True 
    return False 

def contain_duplicate_II(nums, k): 
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen: 
            return True 
        seen.add(nums[i])
        if len(seen) > k: 
            seen.remove(nums[i - k])
    return False 

nums = [1,2,3,1,2,3]
k = 2
print(contain_duplicate_II(nums, k))