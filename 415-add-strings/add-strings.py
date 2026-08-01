class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ind1 = len(num1) - 1
        ind2 = len(num2) - 1
        carry = 0
        res = []

        while ind1 >= 0 or ind2 >= 0:
            digit1 = ord(num1[ind1]) - ord('0') if ind1 >= 0 else 0;
            digit2 = ord(num2[ind2]) - ord('0') if ind2 >= 0 else 0;

            total = digit1 + digit2 + carry
            carry = total // 10

            res.append(chr(total% 10 + ord('0')))

            ind1 -= 1
            ind2 -= 1
        
        return ''.join(res[::-1])





        