class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:
            if i + nums[i] < target:
                i -= 1
            
            else:
                target = i
                i -= 1
        if target == 0:
            return True
        return False




        
        