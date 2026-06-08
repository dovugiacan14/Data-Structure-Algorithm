import pandas as pd
from collections import Counter



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
