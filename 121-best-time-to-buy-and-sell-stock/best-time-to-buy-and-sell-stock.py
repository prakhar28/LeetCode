class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = prices[0]
        minPrice = float('inf')

        for i in range(len(prices) - 1):
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            else:
                currProfit = prices[i] - minPrice
                maxProfit = max(maxProfit, currProfit)
        print(maxProfit)
        return maxProfit
            
                


        