class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        right = 0

        while right < len(nums):
            if nums[right] in freq:
                dis = right - freq[nums[right]]
                if dis <= k:
                    return True
                freq[nums[right]] = right
            else:
                freq[nums[right]] = right
        
        return False

