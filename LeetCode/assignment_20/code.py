def isValid(s): 
    if len(s) % 2 == 1: 
        return False 

    solution = []
    for bracket in s: 
        if bracket in ["(", "{", "["]:
            solution.append(bracket)
            continue 

        if not solution: 
            return False 

        if bracket == ")" and not solution[-1] == "(":
            return False 
        if bracket == "]" and not solution[-1] == "[": 
            return False 
        if bracket == "}" and not solution[-1] == "{": 
            return False 
        
        solution = solution[:-1]
    return len(solution) == 0
