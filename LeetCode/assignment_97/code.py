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
