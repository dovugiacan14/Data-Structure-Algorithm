from itertools import permutations 
def permute(nums):
    res = []
    for word in permutations(nums):
        word_lst = list(word)
        if word_lst in res: 
            continue
        res.append(word_lst)
    return res

def permute(nums):
    res = set()
    for word in permutations(nums):
        if word not in res: 
            res.add(word)
    return list(res)

res = permute([1,1,2]) 
print(res)
