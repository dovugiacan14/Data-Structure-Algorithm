def generate_parenthesis(n):
    result = []
    def back_track(s, open, close): 
        if len(s) == 2*n:
            result.append(s)
            return 

        if open < n: 
            back_track(s + "(", open + 1, close)
        if close < open: 
            back_track(s + ")", open, close + 1)
    back_track("", 0, 0)
    return result 
