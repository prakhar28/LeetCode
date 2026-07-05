class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vow = set("AEIOUaeiou")
        l = 0
        r = len(s_list) - 1
        while l < r:
            if(s_list[l] in vow and s_list[r] in vow):
                s_list[l], s_list[r] = s_list[r], s_list[l]                
                l += 1
                r -= 1
                continue
            elif s_list[r] not in vow:
                r -= 1
                continue
            elif s_list[l] not in vow:
                l += 1
                continue
            else:
                l += 1
                r -= 1
        return "".join(s_list)
        