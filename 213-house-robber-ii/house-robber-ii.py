class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        

        def house_line(houses):
            boxA, boxB = 0, 0
            for i in range(len(houses) - 1, -1, -1):
                ans = max(houses[i] + boxB, boxA)
                boxB = boxA
                boxA = ans
                return boxA
        
        return max(house_line(nums[:-1]), house_line(nums[1:]))
