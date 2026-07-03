class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        newStr = ""
        while p <= len(word1) -1:
            newStr += word1[p]
            if p <= len(word2)-1:
                newStr += word2[p]
            p += 1
        
        if (len(word2) > len(word1)):
            rem = len(word2) - len(word1)
            newStr += word2[-rem:] 

        return newStr
                

            