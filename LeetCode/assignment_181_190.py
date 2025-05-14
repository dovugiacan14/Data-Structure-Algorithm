import pandas as pd
from collections import Counter

"""Assignment 181: Employees Earning More Than Their Managers"""


def find_employees(employee: pd.DataFrame):
    df = employee.merge(right=employee, how="inner", left_on="managerId", right_on="id")
    emp = df[df["salary_x"] > df["salary_y"]]["name_x"]
    return pd.DataFrame({"Employee": emp})


data = {
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "salary": [5000, 7000, 6000, 8000],
    "managerId": [None, 1, 1, 2],
}
employee_df = pd.DataFrame(data)
result = find_employees(employee_df)

"""Assignment 182: Duplicate Emails"""


def duplicate_emails(person: pd.DataFrame):
    emails = person["email"].to_list()
    email_freq = Counter(emails)
    duplicate_emails = set()
    for email, freq in email_freq.items():
        if freq >= 2:
            duplicate_emails.add(email)
    duplicate_emails = list(duplicate_emails)
    df_result = pd.DataFrame({"Email": duplicate_emails})
    return df_result


"""Assignment 183: Customers Who Never Order"""


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    need_order_name = []
    ordered_id = orders["customerId"].to_list()
    customers_dict = customers.set_index("id")["name"].to_dict()
    for id, name in customers_dict.items():
        if id not in ordered_id:
            need_order_name.append(name)
    df_result = pd.DataFrame({"Customers": need_order_name})
    return df_result


"""Assignment 184: Department Highest Salary"""


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    duplicate = employee.drop_duplicates(["salary", "departmentId"])
    df_sorted = duplicate.sort_values(by=["salary"], ascending=False)
    df_groupby = df_sorted.groupby("departmentId").head(3)
    df = employee.merge(department, how="left", left_on="departmentId", right_on="id")
    merging = df.merge(
        df_groupby[["salary", "departmentId"]],
        how="inner",
        on=["departmentId", "salary"],
    )
    merging = merging.rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
    return merging[["Department", "Employee", "Salary"]]


"""Assignment 187: Repeat DNA Sequences
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
You may return the answer in any order.
"""


def find_repeat_dna_sequences(s):
    """Idea:
    - Traversal all input s, get all sub string has lenght = 10
    - Use Dictionary (hash map) to count the existence of each substring
    - Return list substring that occur more than 1.
    """
    seen = set()
    repeated = set()
    for i in range(len(s) - 9):
        sequence = s[i : i + 10]
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)
    return list(sequence)


"""Assignment 189: Rotate Array 
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example: 
    - Input: nums = [1,2,3,4,5,6,7], k = 3
    - Output: [5, 6, 7, 1, 2, 3, 4]
"""


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]


"""Assignment 190: Reverse Bits 
Reverse bits of a given 32 bits unsigned integer.

Example 1: 
    - Input: n = 00000010100101000001111010011100
    - Output: 964176192 (00111001011110000010100101000000)

Example 2: 
    - Input: n = 11111111111111111111111111111101
    - Output: 3221225471 (10111111111111111111111111111111)
"""
def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

n = 0b00000010100101000001111010011100
print(reverseBits(n))