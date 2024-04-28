class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = 5000
        for i in nums:
            if i < n:
                n = i
        
        return n