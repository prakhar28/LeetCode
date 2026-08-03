class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        l = 0
        r = 1
        cok = 0

        while l < r and r < len(s):
            if s[l] != s[r]:
                cok += 1
            l += 1
            r += 1
        return cok



        
