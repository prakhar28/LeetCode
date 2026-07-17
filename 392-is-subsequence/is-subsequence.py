class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0

        while r < len(t):
            if s[l] == t[r]:
                if l == len(s) - 1:
                    return True
                l += 1
                r += 1
            else: 
                r += 1
            
        return False
            