class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying, selling, ans = prices[0],prices[0],0

        for i in range(len(prices)):
            print(prices[i], buying,selling)
            if prices[i] < buying:
                ans = max(ans, selling-buying)
                buying = prices[i]
                selling = prices[i]
            elif prices[i] > selling:
                selling = prices[i]
        
        return max(ans, selling-buying)