class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listLen = len(nums)
        prodNums = [1] * listLen
        preFix = 1
        postFix = 1
        for i in range(listLen):
            prodNums[i] *= preFix
            preFix = preFix*nums[i]
            prodNums[listLen - i - 1] *= postFix
            postFix = postFix*nums[listLen - i - 1]
        return prodNums


        
            