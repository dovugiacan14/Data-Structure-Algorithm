from collections import defaultdict 

def find_median_two_array(arr1, arr2):
    merged_lst = sorted(arr1 + arr2)
    n_len = len(merged_lst)

    if n_len % 2 == 0: 
        mid = int(n_len / 2)
        return float((merged_lst[mid] + merged_lst[mid - 1]) / 2.0)
    else: 
        mid = int((n_len - 1) / 2)
        return merged_lst[mid]
