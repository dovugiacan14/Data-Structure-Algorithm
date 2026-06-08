from itertools import permutations

def get_permutate(n, k): 
    arr = [str(i) for i in range(1, n + 1)]
    permute = [] 
    for word in permutations(arr):
        word_str = ''.join(word)
        permute.append(word_str)
    return permute[k-1]

res= get_permutate(4,9)
print(res)
