class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print("slow, fast", slow, fast)
            if slow == fast:
                break
        
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print("fast, slow", fast, slow)

        return slow