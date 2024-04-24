class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}
        l = 0
        r = len(s1)
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            countS1[s1[i]] = countS1.get(s1[i], 0) + 1
        for j in range(l, r):
            countS2[s2[j]] = countS2.get(s2[j], 0) + 1

        while r <= len(s2): 
            if countS1 == countS2:
                return True
            else:
                if r < len(s2):
                    countS2[s2[l]] -= 1
                    if countS2[s2[l]] == 0:
                        del countS2[s2[l]]
                    countS2[s2[r]] = countS2.get(s2[r], 0) + 1
                l += 1
                r += 1
        return False
