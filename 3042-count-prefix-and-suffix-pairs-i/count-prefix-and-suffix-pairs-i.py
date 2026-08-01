class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        total = 0

        for i in range(len(words) - 1):
            for j in range(i+1, len(words) - 1):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    total += 1
        
        return total


        