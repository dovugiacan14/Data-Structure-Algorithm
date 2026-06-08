
def is_anagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t
