class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 1
        minInd = 0
        while l < r and r < len(nums) -1:
            currSum = nums[l]
            if currSum + nums[r] < target:
                r += 1
                currSum += nums[r]
                print("r, cu", r, currSum) 
            elif currSum + nums[r] >= target:
                minInd = min(r - l + 1, minInd)
                l += 1
                print("elif", l)
                currSum -= nums[l]
        return minInd






