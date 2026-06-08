class MinStack(object): 
    def __init__(self): 
        self.arr = []
        self.minStack = []

    def push(self, val: int): 
        self.arr.append(val)
        if not self.minStack or val <= self.minStack[-1]: 
            self.minStack.append(val)
    
    def pop(self): 
        if self.arr[-1] == self.minStack[-1]: 
            self.minStack.pop()
        self.arr.pop()
    
    def top(self):
        return self.arr[-1]
    
    def getMin(self): 
        return self.minStack[-1]
    
class MinStack(object): 
    def __init__(self): 
        self.stack = []
    
    def push(self, val): 
        return self.stack.append(val)

    def pop(self): 
        return self.stack.pop()

    def top(self): 
        return self.stack[-1]

    def getMin(self): 
        return min(self.stack)
