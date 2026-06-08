import heapq
from sortedcontainers import SortedList



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
            next_node.word = None  # avoid duplicate

        # Mark visited cell
        board[x][y] = "#"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != "#":
                dfs(nx, ny, next_node)
        board[x][y] = ch  # restore after DFS

    for i in range(m):
        for j in range(n):
            dfs(i, j, root)
    return result
