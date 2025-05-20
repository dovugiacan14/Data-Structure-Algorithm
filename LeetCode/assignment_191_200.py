import pandas as pd 
from collections import Counter

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
    person.sort_values(by= "id", inplace= True)
    person.drop_duplicates(subset= "email", keep= "first", inplace= True)
    pass

