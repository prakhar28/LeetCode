class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        lcp = 0

        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10

        print("pre", prefixes)

        for num in arr2:
            while num > 0:
                if num in prefixes:
                    lcp = max(lcp, len(str(num)))
                    break
                num //= 10
        
        return lcp


