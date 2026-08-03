class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

        for i, num in enumerate(nums):
            rem = target - num

            if rem in maps:
                return [maps[rem], i]
            maps[num] = i
        

