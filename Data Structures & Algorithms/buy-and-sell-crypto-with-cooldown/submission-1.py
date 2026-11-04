class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for j in range(3)] for i in range(len(prices))]
        # buy, sell, hold
        dp[0][0] = -prices[0]
        dp[0][1] = -float("inf")

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])

            dp[i][1] = dp[i-1][0]+prices[i]

            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        
        return max(dp[-1])
