class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2

        if len(nums) < 2:
            return len(nums)

        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                continue
            
            else:
                print(k, i, nums)
                nums[k] = nums[i]
                k += 1
        
        return k
        