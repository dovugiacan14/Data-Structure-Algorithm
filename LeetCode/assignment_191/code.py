import pandas as pd
from collections import deque, Counter



def hamming_weight(n: int) -> int:
    binary_bits = bin(n)[2:]
    freq = Counter(binary_bits)
    return freq.get("1", 0)
