class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        if len(nums) == 1:
            if nums[l] == target:
                return l
            else:
                return -1
        while l < r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif target > nums[l]:
                l +=1
            elif target < nums[r]:
                r -= 1
        return -1