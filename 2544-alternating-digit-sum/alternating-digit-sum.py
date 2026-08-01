class Solution:
    def alternateDigitSum(self, n: int) -> int:
        curr = "+"
        total = 0
        n = str(n)
        print("n", n)
        for i in range(len(n)):
            if curr == "+":
                total += int(n[i])
                curr = "-"
            else:
                total -= int(n[i])
                curr = "+"
        
        return total
            


