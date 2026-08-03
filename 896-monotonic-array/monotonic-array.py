class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isInc = True
        isDec = True

        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                isDec = False
            if nums[i] <= nums[i-1]:
                isInc = False
        
        return isInc or isDec