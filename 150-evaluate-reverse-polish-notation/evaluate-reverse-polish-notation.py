class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i.isnumeric() or (i[0] == "-" and i[1:].isnumeric()):
                stack.append(int(i))
            else:
                n = stack.pop()
                m = stack.pop()
                if i == "+":
                    stack.append(m + n)
                elif i == "-":
                    stack.append(m - n)
                elif i == "*":
                    stack.append(m * n)
                elif i == "/":
                    stack.append(int(m / n))
        
        return stack[0]
