class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set1 = set(arr)
        return len(set1) == len(arr)