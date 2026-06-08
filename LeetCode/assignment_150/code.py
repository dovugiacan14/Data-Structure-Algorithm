from collections import OrderedDict, defaultdict

def evalRPN(tokens): 
    stack = []
    for t in tokens: 
        if t not in "+-*/":
            stack.append(int(t))
        else: 
            r, l = stack.pop(), stack.pop()
            if t == "+":
                stack.append(l + r)
            elif t == "-": 
                stack.append(l - r)
            elif t == "*":
                stack.append(l * r)
            else: 
                stack.append(int(float(l)/r))
    return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
out = evalRPN(tokens)
