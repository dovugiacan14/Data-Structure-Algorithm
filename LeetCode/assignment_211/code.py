import heapq
from sortedcontainers import SortedList



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
