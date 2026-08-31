from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        
        def house_line(houses):
            @cache
            def f(i):
                if i >= len(houses):
                    return 0
                return max(houses[i] + f(i+2), f(i+1))
            return f(0)
        
        return max(house_line(nums[:-1]), house_line(nums[1:]))
