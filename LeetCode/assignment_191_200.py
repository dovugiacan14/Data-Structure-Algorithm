import pandas as pd
from collections import deque, Counter

"""Assignment 191: Number of 1 Bits
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

Example 1: 
    - Input: n = 11
    - Output: 3
    - Explaination: The input binary string 1011 has a total of three set bits.

Example 2: 
    - Input: n = 128
    - Output: 1
    - Explaination: The input binary string 10000000 has a total of one set bit. 

Example 3: 
    - Input: n = 2147483645
    - Output: 30
    - Explaination: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
"""


def hamming_weight(n: int) -> int:
    binary_bits = bin(n)[2:]
    freq = Counter(binary_bits)
    return freq.get("1", 0)


"""Assignment 196: Delete Duplicate Emails
Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
For Pandas users, please note that you are supposed to modify Person in place.
After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. 
The final order of the Person table does not matter.

"""


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)


"""Assignment 197: Rising Temperature
Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.
"""


def rising_temperature(weather: pd.DataFrame):
    if weather.empty:
        return pd.DataFrame(columns=["id"])

    prev_day = weather.copy()
    prev_day["recordDate"] = prev_day["recordDate"] + pd.Timedelta(days=1)
    prev_day = prev_day.rename(columns={"temperature": "prev_temp", "id": "prev_id"})

    merged = weather.merge(prev_day, on="recordDate")
    result = merged[merged["temperature"] > merged["prev_temp"]][["id"]]
    return result.reset_index(drop=True)


data = {
    "id": [1, 2, 3, 4, 5, 6, 7],
    "recordDate": [
        "2023-01-01",
        "2023-01-02",
        "2023-01-03",
        "2023-01-04",
        "2023-01-05",
        "2023-01-06",
        "2023-01-07",
    ],
    "temperature": [10, 15, 14, 20, 20, 19, 25],
}

df = pd.DataFrame(data)
df["recordDate"] = pd.to_datetime(df["recordDate"])
print(rising_temperature(df))

"""Assignment 198: House Robber
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1: 
    - Input: nums = [1,2,3,1]
    - Output: 4 
    - Explaination:  Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2: 
    - Input: nums = [2,7,9,3,1]
    - Output: 12 
    - Explaination: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
"""


# Use Dynamic Programming
def house_robber(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    return dp[-1]


"""Assignment 199: Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it.
Return the values of the nodes you can see ordered from top to bottom.

Example 1: 
- Input: root = [1,2,3,null,5,null,4] 
- Output: [1,3,4]

Example 2: 
- Input: root = [1,2,3,4,null,null,null,5]
- Output: [1,3,4,5]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def rightSideView(self, root):
        """Idea: Use BFS to apply level-order traversal.
        Each level we get last node in list node of this level
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


"""Assignment 200: Number of Islands.
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1: 
- Input: grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
- Output: 1

Example 2: 
- Input: grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
- Output: 3
"""
def number_of_islands(grid):
    # Use Depth-First Search (DFS) to solve this problem. 
    if not grid: 
        return 0 

    rows, cols = len(grid), len(grid[0])
    count = 0 

    def dfs(r,c):
        # stopping condition
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return 
        grid[r][c] = "0"  # mark as visited 

        # recursion to 4 directions 
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows): 
        for j in range(cols): 
            if grid[i][j] == "1":
                count += 1 
                dfs(i, j)
    return count 