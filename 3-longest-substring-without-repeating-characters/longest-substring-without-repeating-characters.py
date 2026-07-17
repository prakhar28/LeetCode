class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        maxLen = 0
        for r in range(len(s)):
            if s[r] in seen:
                while l in range(len(s)):
                    if s[l] == s[r]:
                        maxLen = r-l+1 if r-l+1 > maxLen else maxLen
                        break
                    else:
                        l += 1
            else: 
                seen.add(s[r])
            
        return maxLen
                    



        