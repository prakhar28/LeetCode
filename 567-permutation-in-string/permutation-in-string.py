class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}
        l = 0
        r = len(s1)
        for i in range(len(s1)):
            countS1[s1[i]] = countS1.get(s1[i], 0) + 1
        
        while r <= len(s2):
            for j in range(l, r):
                countS2[s2[j]] = countS2.get(s2[j], 0) + 1
            
            if countS1 == countS2:
                return True
            else:
                countS2 = {}
                l += 1
                r += 1
        return False
