def combination_sum_2(candidates, target):
    def get_candidates(start, target, cur_total):
        if target == 0: 
            result.append(cur_total[:])
            return 

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]: 
                continue 
            if candidates[i] > target:
                break 
            cur_total.append(candidates[i])
            get_candidates(i + 1, target - candidates[i], cur_total)
            cur_total.pop()
    
    candidates.sort()
    result = []
    get_candidates(0, target, [])
    return result


combination_sum_2([10,1,2,7,6,1,5], 8)
