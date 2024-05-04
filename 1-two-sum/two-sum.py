class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            numMap[nums[i]] = i
        
        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in numMap and numMap[rem] != i:
                return [i, numMap[rem]]

        return []
            

    