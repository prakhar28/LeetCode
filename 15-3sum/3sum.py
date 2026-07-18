class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print("nums", nums)
        arr = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    arr.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                else:
                    if nums[l] + nums[r] + nums[i] > 0:
                        r -= 1
                    if nums[l] + nums[r] + nums[i] < 0:
                        l += 1
        return arr



