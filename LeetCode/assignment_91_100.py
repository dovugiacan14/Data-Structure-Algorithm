"""Assignment 90: Decode Ways 

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1: 
- Input: s = "12"
- Output: 2 
- Explaination: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2: 
- Input: s = "226"
- Output: 3 
- Explaination: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3: 
- Input: s = "06" 
- Output: 0
- Explaination: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

"""


# Use Brute-Force solution --> Too Long
def decode_ways(s):
    def generate_subsets(start, path):
        if start == len(s):  # when split all string s
            subsets.append(path[:])
            return

        for i in range(start + 1, len(s) + 1):
            # only keep partition has lenght < 2
            if i - start > 2:
                break
            path.append(s[start:i])
            generate_subsets(i, path)
            path.pop()

    subsets = []
    generate_subsets(0, [])

    valid_ways = 0
    valid_string = [str(i) for i in range(1, 27)]
    for ways in subsets:
        if set(ways).issubset(set(valid_string)):
            valid_ways += 1

    return valid_ways


# Use Dynamic-Programing
def decode_ways(s):
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # setting base case

    for i in range(2, n + 1):
        one_digit = int(s[i - 1])
        two_digit = int(s[i - 2 : i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]

        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    return dp[n]


s = "11106"
print(decode_ways(s))

"""Assignment 92: Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

The solution set must not contain duplicate subsets. Return the solution in any order.

- Input: head = [1,2,3,4,5], left = 2, right = 4
- Output: [1,4,3,2,5]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head  # Không cần đảo nếu danh sách rỗng hoặc left == right

    dummy = ListNode(0)  # Tạo node giả để xử lý dễ hơn khi left = 1
    dummy.next = head
    prev = dummy

    # Bước 1: Di chuyển đến node trước vị trí `left`
    for _ in range(left - 1):
        prev = prev.next

    # Bước 2: Bắt đầu đảo ngược đoạn từ left -> right
    curr = prev.next
    next_node = None
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp  # Cập nhật node đầu của đoạn bị đảo
    return dummy.next


"""Assignment 93: Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

- Input:s = "25525511135"
- Output: ["255.255.11.135","255.255.111.35"]

Idea: 
- Split s into 4 part 
- Check each part is valid ? If invalid then backtrack to previous step
"""


def restore_ip_address(s):
    result = []
    if len(s) < 3 or len(s) > 12:
        return result

    def backtrack(start, path):
        # if enough 4 part or reach the length s
        if len(path) == 4 and start == len(s):
            result.append(".".join(path))
            return

        if len(path) == 4 or start == len(s):
            return

        for length in range(1, 4):
            if start + length > len(s):  # Tránh lỗi IndexError
                break
            part = s[start : start + length]

            # check condition
            if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start + length, path + [part])

    backtrack(0, [])
    return result


"""Assignment 94: Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1: 
- Input: root = [1,null,2,3]
- Output: [1,3,2]

Example 2: 
- Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
- Output: [4,2,6,5,7,1,3,9,8]

**General Rules: 
The input list represents the tree in level-order traversal, meaning it is arranged level by level 
from top -> bottom, left -> right 
    + root[0] is the root. 
    + for each root[i]:
        ++ The left child is at root[2*i + 1]
        ++ The right child is at root[2*i + 2]
    + null indicates that the node does not exist. 

** Method 1: Use Recursive 
B1: If root is None -> Return []
B2: Call recursive with root.left and get the value of left child node  -> get root.val
B3: Call recursive with root.right and get the value of right child node -> get root.val 
B4: Return the list follow the order Left -> Root -> Right.

**Method 2: Use Stack 
B1: Traverse all the left branches and push them onto the stack
B2: Retrieve the value of the top node from the stack (root node)
B3: Continue traversing the right branch 
B4: Repeat until the stack is empty and there are no more nodes to traverse. 

"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Use Recursive
def inorder_traversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    if not root:
        return []

    left_subtree = inorder_traversal(root.left)
    current_value = [root.val]
    right_subtree = inorder_traversal(root.right)

    return left_subtree + current_value + right_subtree


# Use Stack
def inorder_traversal_iter(root):
    stack = []
    result = []
    current_node = root

    while current_node or stack:
        # 1. Push all left node to stack
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        # 2. Get the node on the top of the stack
        current_node = stack.pop()
        result.append(current_node.val)

        # 3. Traversal the right branch
        current_node = current_node.right

    return result


"""Assignment 95: Unique Binary Search Trees II
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. 
Return the answer in any order.

Example 1: 
    - Input: n = 3
    - Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Idea: 
    - Create a recursive function to generate all BST from start to end 
"""


class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def generate_trees(n):
    def generate_subtrees(start, end):
        if start > end:
            return [None]

        all_trees = []
        for i in range(start, end + 1):
            left_trees = generate_subtrees(start, i - 1)  # left node
            right_trees = generate_subtrees(i + 1, end)  # right node

            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i, left, right)
                    all_trees.append(root)
        return all_trees

    if n == 0:
        return []
    return generate_subtrees(1, n)


# # Helper function to print the tree in preorder traversal
# def preorder_traversal(root):
#     if not root:
#         return "None"
#     return f"{root.val}, {preorder_traversal(root.left)}, {preorder_traversal(root.right)}"

# # Test with n = 3
# trees = generate_trees(3)

# # Print all generated trees
# for i, tree in enumerate(trees, 1):
#     print(f"Tree {i}: {preorder_traversal(tree)}")

"""Assignment 96: Unique Binary Search Trees 
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1: 
    - Input: n = 3
    - Output: 5

Idea: 
    - Create a recursive function to generate all BST from start to end 
"""


def unique_binary_tree(n):
    def generate_tree(start, end):
        if start > end:
            return [None]

        all_trees = []
        for i in range(start, end + 1):
            left_trees = generate_tree(start, i - 1)
            right_trees = generate_tree(i + 1, end)

            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i, left, right)
                    all_trees.append(root)
        return all_trees

    if n == 0:
        return 0
    return len(generate_tree(1, n))


def unique_binary_tree(n):
    """
    :type n: int
    :rtype: int
    """

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Với 0 hoặc 1 node thì chỉ có 1 cách tạo cây BST

    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]

    return dp[n]


"""Assignment 97: Interleaving String 
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings respectively, such that:
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1: 
    - Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    - Output: True

Example 2: 
    - Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    - Output: false
"""
import queue


def interleaving_string(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    q = queue.Queue()
    q.put((0, 0))
    visited = set()
    while not q.empty():
        i, j = q.get()

        if i == len(s1) and j == len(s2):
            return True  # done to visit s1 and s2, s3 is valid

        if i < len(s1) and s1[i] == s3[i + j] and (i + 1, j) not in visited:
            q.put((i + 1, j))
            visited.add((i + 1, j))

        if j < len(s2) and s2[j] == s3[i + j] and (i, j + 1) not in visited:
            q.put((i, j + 1))
            visited.add((i, j + 1))
    return False


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(interleaving_string(s1, s2, s3))

"""Assignment 98: Validate Binary Search Tree 
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:

    + The left subtree of a node contains only nodes with keys less than the node's key.
    + The right subtree of a node contains only nodes with keys greater than the node's key.
    + Both the left and right subtrees must also be binary search trees.

Example 1: 
    - Input: root = [2,1,3]
    - Output: True

Example 2: 
    - Input: root = [5,1,4,null,null,3,6]
    - Output: False
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_binary_search_tree(root):
    if not root:
        return True

    def check(node, min_val, max_val):
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        return check(node.left, min_val, node.val) and check(
            node.right, node.val, max_val
        )

    return check(root, float("-inf"), float("inf"))


"""Assignment 99: Recover Binary Search Tree 

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.

Example 1: 
    - Input: root = [1,3,null,null,2]
    - Output: [3,1,null,null,2]
    - Explaination: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2: 
    - Input: root = [3,1,4,null,null,2]
    - Output: [2,1,4,null,null,3]
    - Explaination: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

"""
class TreeNode(object): 
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val
        self.left = left 
        self.right = right 

def recover_tree(root): 
    """
    :type root: Optional[TreeNode]
    :rtype: None Do not return anything, modify root in-place instead.
    """
    first = None 
    second = None 
    prev = None 

    def inoder_traversal(node):
        nonlocal first, second, prev
        if not node: 
            return 
        
        inoder_traversal(node.left) # visit left subtree

        if prev and prev.val > node.val: 
            if not first: 
                first = prev # mark the first error 
            second = node  # mark the second error 
        prev = node 

        inorder_traversal(node.right)

    inoder_traversal(root)
    
    # swap two errors node 
    if first and second: 
        first.val, second.val = second.val, first.val  

"""Assignment 100: Recover Binary Search Tree 

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1: 
    - Input: p = [1,2,3], q = [1,2,3]
    - Output: True

Example 2: 
    - Input: p = [1,2], q = [1,null,2]
    - Output: False

"""
class TreeNode(object): 
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val
        self.left = left 
        self.right = right 
    
def is_sametree(p, q):
    def inorder_traversal(root): 
        stack = []
        result = []
        current_node = root

        while current_node or stack:
            while current_node: 
                stack.append(current_node)
                current_node = current_node.left 
        
            current_node = stack.pop()
            result.append(current_node.val)

            current_node = current_node.right

        return result 
    
    p_traversaled = inorder_traversal(p)
    q_traversaled = inorder_traversal(q)
    return p_traversaled == q_traversaled

def isSameTree(p, q): 
    if not p and not q: 
        return True 
    
    if not p or not q or p.val != q.val: 
        return False 
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)