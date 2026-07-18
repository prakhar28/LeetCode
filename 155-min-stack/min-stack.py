class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = float('inf')
        

    def push(self, value: int) -> None:
        if(self.currMin > value):
            self.currMin = value
        
        self.stack.append((value, self.currMin))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.currMin = self.stack[-1][1]
        else:
            self.currMin = float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()