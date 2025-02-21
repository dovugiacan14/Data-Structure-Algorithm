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
        if start == len(s): # when split all string s 
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
    if not s or s[0] == '0': 
        return 0 
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1     # setting base case 

    for i in range(2, n + 1): 
        one_digit = int(s[i - 1])
        two_digit = int(s[i -2 : i])

        if 1 <= one_digit <= 9: 
            dp[i] += dp[i -1]
        
        if 10 <= two_digit <= 26: 
            dp[i] += dp[i-2]
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
    def __init__(self, val=0, next= None): 
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
        
        for length in range(1,4): 
            if start + length > len(s):  # Tránh lỗi IndexError
                break  
            part = s[start:start + length]

            # check condition 
            if (part.startswith('0') and len(part) > 1) or int(part) > 255: 
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

"""
class TreeNode(object):
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val 
        self.left = left
        self.right = right 

def inorder_traversal(root): 
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    if not root: 
        return []
    
    
        
