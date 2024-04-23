class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr = set()
        longSub = 0
        for r in range(len(s)):
            if s[r] not in curr:
                curr.add(s[r])
                longSub = max(longSub, r - l +1)
            
            else:
                while s[r] in curr:
                    curr.remove(s[l])
                    l +=1
                curr.add(s[r])

        return longSub  
            
            
                

