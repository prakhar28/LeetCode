class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupMap = {}
        for i in nums:
            if i in dupMap:
                dupMap[i] += 1
            else:
                dupMap[i] = 1

        for key in dupMap:
            if dupMap[key] > 1:
                return key
