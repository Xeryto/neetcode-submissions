class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 3:
            return max(0, prices[-1]-prices[0])
        
        buyPrice = prices[0]
        profit = prices[1]-prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-buyPrice)
            buyPrice = min(buyPrice, prices[i])
        
        return max(0, profit)