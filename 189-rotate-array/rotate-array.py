class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverseArr(nums, 0, len(nums) -1)
        self.reverseArr(nums, 0, k)
        self.reverseArr(nums, k+1, len(nums) -1)


    

    def reverseArr(self, arr: List[int], l: int, r: int) -> None:

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
                