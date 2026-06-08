def combination_sum(candidates, target):
    def get_candidates(candidates, target, index, cur_total, result):
        if sum(cur_total) == target:
            result.append(list(cur_total))
            return 
        
        if sum(cur_total) > target: 
            return 
        
        for i in range(index, len(candidates)):
            cur_total.append(candidates[i])
            get_candidates(candidates, target, i, cur_total, result)
            cur_total.pop()
        return result 
    res = get_candidates(candidates, target, 0, [], [])
    return res
