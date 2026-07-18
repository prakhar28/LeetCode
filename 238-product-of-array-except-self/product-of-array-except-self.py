class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        lp = 1
        for i in range(len(nums)- 1):
            answer[i] = lp
            lp *= nums[i]
        
        rp = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= rp
            rp *= nums[i]

        return answer 