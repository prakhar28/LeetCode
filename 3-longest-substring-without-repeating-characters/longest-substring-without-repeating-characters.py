class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p = 0
        res = ""
        s = list(s)
        while p < len(s) - 1:
            tempStr = ""
            for i in s:
                if i in d:
                    d.clear()
                    p += 1
                    if len(res) < len(tempStr):
                        res = tempStr
                    break
                else:
                    d[i] = 1
                    tempStr += i
        
        return res



        