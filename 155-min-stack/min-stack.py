class MinStack:

    def __init__(self):
        self.minStack = []
        self.min = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.min:
            val = min(self.min[-1],val)
        self.min.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.min[-1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()