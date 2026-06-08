from typing import Optional
from collections import defaultdict, deque



class TrieNode:
    def __init__(self):
        self.children = {}  # dictionary to store child node
        self.is_end = False  # True if the node represents the end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize root node

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True  # mark the end of word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end  # return True only if it's end of a word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()
trie.insert("apple")

print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
