def compare_version(version1, version2): 
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    # make both versions the same length by padding with 0 
    max_len = max(len(v1), len(v2))
    v1 += [0] * (max_len - len(v1))
    v2 += [0] * (max_len - len(v2))

    for a, b in zip(v1, v2): 
        if a > b: 
            return 1 
        elif a < b: 
            return -1
    return 0
