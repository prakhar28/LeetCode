class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 1
        minInd = len(nums) 
        currSum = nums[l] + nums[r]
        while l < len(nums) and r < len(nums) -1 :
            if currSum < target :
                print("r, cu", r, currSum) 
                r += 1
                currSum += nums[r]
            else:
                minInd = min(r - l + 1, minInd)
                l += 1
                print("elif", l, minInd, currSum)
                currSum -= nums[l]
        return minInd






