class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print("nums", nums)
        arr = []
        
        for i in range(len(nums)):
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



