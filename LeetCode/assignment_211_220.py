
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