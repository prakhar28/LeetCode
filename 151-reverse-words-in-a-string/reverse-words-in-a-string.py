class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        s = list(s)
        
        for i in range(len(s)):
            tempWord = ""
            if s[i] != " ":
                tempWord += s[i]
            else:
                arr.append(tempWord)
                tempWord = ""
            i += 1
        
        return " ".join(arr[::-1])