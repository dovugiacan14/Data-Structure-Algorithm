from typing import Optional
from collections import defaultdict, deque

"""Assignment 201: Binary Tree Right Side View
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:
- Input: left = 5, right = 7
- Output: 4

Example 2:
- Input: left= 0 , right= 0
- Output: 0

Example 3:
- Input: left = 1, right = 2147483647
- Output: 0
"""


def range_bitwise_and(left: int, right: int):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift


left = 5
right = 7
print(range_bitwise_and(left, right))

"""Assignment 202: Happy Number
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in are happy
Return true if n is a happy number, and false if not.

Example 1: 
- Input: n = 19
- Output: True
- Explaination: 
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68 
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

Example 2: 
- Input: n = 2 
- Output: False

"""


def is_happy(n):
    def calculate_sum_square(number):
        return sum(int(c) ** 2 for c in str(number))

    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = calculate_sum_square(n)
    return True


"""Assignment 203: Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1: 
- Input head = [1,2,6,3,4,5,6], val = 6
- Output: [1,2,3,4,5]

Example 2: 
- Input: head = [7,7,7,7], val = 7
- Output: 7

"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int):
    if not head:
        return None

    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    # delete
    new_list = [x for x in arr if x != val]
    if not new_list:
        return None

    new_head = ListNode(new_list[0])
    cur = new_head
    for val in new_list[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head


"""Assignment 204: Count Primes
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1: 
- Input: n = 10
- Output: 4 
- Explaination: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2: 
- Input: n = 0
- Output: 0

Example 3: 
- Input: n = 1 
- Output: 0 

"""


# O(N^2)
def count_primes(n):
    if n < 2:
        return 0
    count = 0
    for i in range(2, n):
        check = 0
        for j in range(2, i):
            if i % j == 0:
                check += 1
        if check == 0:
            count += 1
    return count


# O(N.log(N))
def count_primes(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)


n = 10
print(count_primes(n))

"""Assignment 205: Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1: 
- Input: s = "egg", t = "add"
- Output: True
- Explaination: The strings s and t can be made identical by:
    + Mapping 'e' to 'a'.
    + Mapping 'g' to 'd'.

Example 2: 
- Input: s = "foo", t = "bar"
- Output: Fasle

Example 3: 
- Input: s = "paper", t = "title"
- Output: True

"""


def isormophic_string(s, t):
    if len(s) != len(t):
        return False
    data_dict = {}
    list_val = []
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        if s_char in data_dict:
            if data_dict[s_char] != t_char:
                return False
        else:
            if t[i] in list_val:
                return False
            data_dict[s_char] = t[i]
            list_val.append(t_char)
    return True


s = "paper"
t = "title"
print(isormophic_string(s, t))

"""Assignment 206: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: 
- Input: head = [1,2,3,4,5]
- Output: [5,4,3,2,1]

Example 2: 
- Input: head = [1,2]
- Output:[2,1]

"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    if not head:
        return None

    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    new_arr = arr[::-1]

    new_head = ListNode(new_arr[0])
    cur = new_head
    for val in new_arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return new_head


"""Assignment 207: Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
    - Input: numCourses = 2, prerequisites = [[1,0]]
    - Output: true
    - Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    - Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    - Output: false
    - Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""


def can_finish(numCourses, prerequisites):
    """Quy về bài toán đồ thị.
    - Nếu đồ thị có chu trình thì bạn không thể hoàn thành khóa học -> False
    - Nếu đồ thị không có chun trình thì bạn có thể hoàn thành khóa học -> True
    """
    # Build graph: edges from b -> a (b must be before a)
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    visited = [0] * numCourses

    def dfs(course):
        if visited[course] == 1:
            return False
        if visited[course] == 2:  # already visited
            return True

        visited[course] = 1  # mark as visiting
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        visited[course] = 2  # mask as visited
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True


"""Assignment 208: Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker

Implement the Trie class: 
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
    - Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    - Output: [null, null, true, false, true, null, true]
    - Explanation: 
        + Trie trie = new Trie();
        + trie.insert("apple");
        + trie.search("apple");  
        + trie.search("app"); 
        + trie.startsWith("app"); 
        + trie.insert("app");
        + trie.search("app");  
"""


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

"""Assignment 209: Minimum Size Subarray Sum 
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:
    - Input: target = 7, nums = [2,3,1,2,4,3]
    - Output: 2
    - Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2: 
    - Input: target = 4, nums = [1,4,4]
    - Output: 1 

Example 3: 
    - Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    - Output: 0
"""

def min_subarray_len(target, nums): 
    left = 0 
    total = 0 
    min_len = float("inf")

    for right in range(len(nums)):
        total += nums[right]

        while total >= target: 
            min_len = min(min_len, right - left + 1) 
            total -= nums[left]
            left += 1 
    return 0 if min_len == float("inf") else min_len

target = 11
nums  = [1,1,1,1,1,1,1,1]
print(min_subarray_len(target, nums))

"""Assignment 210: Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
    - Input: numCourses = 2, prerequisites = [[1,0]]
    - Output: [0, 1]
    - Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2: 
    - Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    - Output: [0,2,1,3]
    - Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
                So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""
def course_schedule_II(numCourses, prerequisites): 
    """
    Main Idea 
        - Mỗi môn học là một đỉnh (node) trong đồ thị 
        - Mỗi quan hệ [a, b] (phải học b trước a) là một cạnh có hướng từ b đến a. 
        - Bài toán trở thành: liệt kê thứ tự topo (topological ordering) của các đỉnh trong đồ thị. 
        - Nếu có chu trình, thì không thể hoàn thành tất cả các môn học, trả về []. 

    Cách giải: 
        B1: Xây dựng đồ thị & đếm số bậc vào (indegree)
        B2: BFS - Topological Sort (Kahn's Algorithm)
            - Tạo một hàng đợi (queue) chứa các môn có indegree = 0 (không có môn nào cần học trước).
            - Lặp: 
                + Lấy môn ra khỏi queue, thêm vào kết quả 
                + Với mỗi môn học phụ thuộc vào nó: giảm indegree, nếu bằng 0 thì cho vào queue. 
            - Cuối cùng, nếu kết quả đủ numCourses, trả về thứ tự đó. Nếu không -> có chu trình -> trả về []
         
    """
    graph = defaultdict(list)
    indegree = [0] * numCourses

    # Build graph & indegree 
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1 
    
    # Start with nodes with no prerequisites 
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    while queue: 
        course = queue.popleft()
        order.append(course)

        for neighbor in graph[course]: 
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0: 
                queue.append(neighbor)
    return order if len(order) == numCourses else []