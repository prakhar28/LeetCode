class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem not in maps.keys():
                maps[nums[i]] = i
            
            else:
                return [maps[rem], i]
        

