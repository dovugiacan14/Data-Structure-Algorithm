from collections import deque 

def removeInvalidParentheses(s): 
    def is_valid(f): 
        count = 0 

        for ch in f: 
            if ch == "(": 
                count += 1 
            elif ch == ")":
                count -= 1 

                if count < 0: 
                    return False 
        return count == 0 

    queue = deque([s])
    visited = {s}   
    ans = []
    found = False 

    while queue: 
        curr = queue.popleft()

        if is_valid(curr): 
            ans.append(curr)
            found = True 
        
        if found: 
            continue

        for i in range(len(curr)): 
            if curr[i] not in "()": 
                continue 

            nxt = curr[:i] + curr[i+1:] 

            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return ans
    
if __name__ == "__main__":
    print(removeInvalidParentheses("()())()"))
    print(removeInvalidParentheses("(a)())()"))
