import pandas as pd
from collections import Counter

def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

n = 0b00000010100101000001111010011100
print(reverseBits(n))
