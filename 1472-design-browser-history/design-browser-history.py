class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = []
        self.currInd = 0

    def visit(self, url: str) -> None:
        self.arr = self.arr[self.currInd:]
        self.arr.append(url)
        self.currInd = len(self.arr) - 1
        

    def back(self, steps: int) -> str:
        return self.arr[0] if steps > self.currInd else self.arr[self.currInd - steps]
        

    def forward(self, steps: int) -> str:
        return self.arr[-1] if steps + self.currInd > len(self.arr) -1 else self.arr[self.currInd + steps]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)