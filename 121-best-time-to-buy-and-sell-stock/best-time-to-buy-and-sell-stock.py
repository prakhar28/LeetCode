class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxprofit = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, prices[r] - prices[l])
            else:
                l = r
        
        return maxprofit

        