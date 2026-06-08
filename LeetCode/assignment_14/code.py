def longestCommonPrefix(strs):
    strs = sorted(strs)
    head = strs[0]
    tail = strs[-1]
    min_word = min(len(head), len(tail))
    res = ""
    for i in range(min_word):
        if head[i] != tail[i]:
            return res
        else:
            res += head[i]
    return res


res = longestCommonPrefix(["flower", "flow", "flight"])
