class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        max_freq = 0
        max_len = 0
        freq = {}

        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return max_len