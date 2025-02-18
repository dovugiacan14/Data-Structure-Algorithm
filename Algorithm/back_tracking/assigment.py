"""
BT1: Hãy liệt kê tất cả các dãy nhị phân có độ dài n, là dãy n ký tự và chỉ gồm cá ký tự 0, 1

Example: 
- Input: n = 3 

- Output: 000, 001, 010, 011, 100, 101, 110, 111
"""
def generate_string(start_pos, n, res_string, result):
    # Base case 
    if start_pos > n: 
        result.append(res_string)
        return 
    
    # Recursive 
    for i in ["0", "1"]:
        generate_string(start_pos + 1, n, res_string + i, result)

    return result

"""
BT2: Cho tập S = {1, 2, 3, ..., n}. Hãy in ra tất cả các tập con có chính xác k phần tử của S. 
Hai tập con là hoán vị của nhau thì chỉ tính là 1. 

"""
def create_arr(n):
    return [f"{i + 1}" for i in range(n)] 

def generate_subset(arr, pos, k, res_string, result):
    # base case 
    if len(res_string) == k: 
        result.append(res_string)
        return  
    
    # recursive 
    for i in arr:
        res_string += i
        generate_subset(arr, pos + 1, k, res_string, result)
        res_string = res_string[: -1]
    
    return result

"""
BT3: Bài toán phân tích số 

Ở một quốc gia có n loại tiền gồm các mệnh giá a1, a2, ... , an (n < 11). 
Có những cách nào để lấy các tờ tiền sao cho tổng mệnh giá của chúng là S. 
Biết rằng mỗi mệnh giá tiền có thể được lấy nhiều lần và hai cách lấy là hoán vị của nhau chỉ tính là một.

Example:
- Input:  
    - Với 3 mệnh giá tờ tiền: 10, 20, 50
    - Và tổng target là 100

- Output: 
    - Có 10 cách lấy
"""
def get_money_set(money_lst, target_total, index, cur_total, result):
    # base case 
    if sum(cur_total) == target_total: 
        result.append(list(cur_total))
        return 
    
    if sum(cur_total) > target_total: 
        return 
    
    # recursive 
    for i in range(index, len(money_lst)):
        cur_total.append(money_lst[i])
        get_money_set(money_lst, target_total, i, cur_total, result)
        cur_total.pop()
    
    return result

"""
BT4: Bài toán xếp hậu 

Tìm tất cả các cách xếp n (n <= 12) quân Hậu lên bàn cờ n x n sao cho không quân hậu nào có thể ăn được nhau. 
Nếu có hai cách là hoán vị của nhau (về vị trí) thì chỉ tính là một.

Điều kiện hai quân hậu A và B ăn nhau: 
- Khi A và B nằm cùng hàng: x_A = x_B 
- Khi A và B nằm cùng cột: y_A = y_B 
- Khi A và B nằm trên cùng đường chéo: 
    - x_A + y_A = x_B + y_B 
    - x_A - y_A = x_B - y_B

Ý tưởng: 
"""
def queen_set(n_queen):
    def is_safe(board, row, col):
        """
        Args: 
        - board: bàn cờ 
        - row: tọa độ hàng 
        - col: tọa độ cột 

        Return: True / False 
        """
        # Kiểm tra cột 
        for i in range(row):
            if board[i] == col: 
                return False 
        
        # Kiểm tra đường chéo chính 
        for i in range(row):
            if board[i] - i == col - row: 
                return False 
        
        # Kiểm tra đường chéo phụ 
        for i in range(row):
            if board[i] + i == col + row: 
                return False 
        return True 

    def solve(board, row, result):
        # base case 
        if row == n_queen:
            normalized_solution = tuple(sorted((r, board[r]) for r in range(n_queen)))
            result.add(normalized_solution)
            return 
        
        # recursive 
        for col in range(n_queen):
            if is_safe(board, row, col):
                board[row] = col 
                solve(board, row + 1, result)
                board[row] = -1

    board = [-1] * n_queen # save the position of each queen in each row
    result = set()
    solve(board, 0, result)
    return result


"""Assignment 22: Generate Parentheses 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1: 
- Input: n = 3 
- Ouput: ["((()))","(()())","(())()","()(())","()()()"]
"""
def generate_parenthesis(n):
    result = []
    def back_track(s, open, close): 
        if len(s) == 2*n:
            result.append(s)
            return 

        if open < n: 
            back_track(s + "(", open + 1, close)
        if close < open: 
            back_track(s + ")", open, close + 1)
    back_track("", 0, 0)
    return result 


"""Assignment 39: Combination Sum 

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example: 
- Input: candidates = [2,3,6,7], target = 7
- Ouput: [[2,2,3],[7]]
- Explaination: 
    + 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    + 7 is a candidate, and 7 = 7. These are the only two combinations.
"""
def combination_sum(candidates, target):
    def get_candidates(candidates, target, index, cur_total, result):
        if sum(cur_total) == target:
            result.append(list(cur_total))
            return 
        
        if sum(cur_total) > target: 
            return 
        
        for i in range(index, len(candidates)):
            cur_total.append(candidates[i])
            get_candidates(candidates, target, i, cur_total, result)
            cur_total.pop()
        return result 
    res = get_candidates(candidates, target, 0, [], [])
    return res

"""Assignment 40: Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example: 
- Input: candidates = [10,1,2,7,6,1,5], target = 8
- Ouput:[
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6]
        ]
"""
def combination_sum_2(candidates, target):
    def get_candidates(start, target, cur_total):
        if target == 0: 
            result.append(cur_total[:])
            return 

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]: 
                continue 
            if candidates[i] > target:
                break 
            cur_total.append(candidates[i])
            get_candidates(i + 1, target - candidates[i], cur_total)
            cur_total.pop()
    
    candidates.sort()
    result = []
    get_candidates(0, target, [])
    return result

"""Assignment 77: Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1: 
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
def combinations(n, k):
    def backtrack(start, sub_arr): 
        if len(sub_arr) == k: 
            result.append(sub_arr[:])
            return 
        
        for i in range(start, n+1): 
            sub_arr.append(i)
            backtrack(i + 1, sub_arr)
            sub_arr.pop()

    result = []
    backtrack(1, [])
    return result


"""Assignment 78: Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1: 
Input: [1,2,3]
Output:[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
def subsets(nums):
    def backtrack(pos, subset):
        result.append(subset[:])
        
        if len(subset) == len(nums):
            return 

        for i in range(pos, len(nums)):
            subset.append(nums[i]) 
            backtrack(i + 1, subset)
            subset.pop()
    result = []
    backtrack(0, [])
    return result 


"""Assignment 90: Subsets II  

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

- Input: nums = [1,2,2]
- Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""

def subset_version2(nums): 
    def backtrack(pos, subset): 
        result.append(subset[:])
        
        if len(subset) == len(nums): 
            return 
        
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]: 
                continue 
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

    nums.sort()
    result = []
    backtrack(0, [])
    return result  

if __name__ == "__main__": 
    # BT1 
    res = generate_string(1, 4, "", [])

    # BT2 
    arr = create_arr(5)
    res = generate_subset(
        arr= arr, 
        pos= 1, 
        k = 3, 
        res_string= "",
        result= []
    )

    # BT3 
    res = get_money_set(
        money_lst= [10, 20, 50],
        target_total= 100, 
        index= 0, 
        cur_total= [],
        result= []
    )
    print(res)
    print(len(res))

    # BT4 
    solutions = queen_set(2)
    print(0)