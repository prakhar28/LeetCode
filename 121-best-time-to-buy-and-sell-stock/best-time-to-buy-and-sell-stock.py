class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxPro = 0
        while right < len(prices):
            currPro = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxPro = max(currPro, maxPro)
            else:
                left = right
            right = right + 1
        return maxPro
        