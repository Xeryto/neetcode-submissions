class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0

        smallest = min(coins)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(smallest*2,amount+1):
            for coin in coins:
                if coin <= i and (dp[i-coin] != -1 and (dp[i] == -1 or dp[i-coin]+1 < dp[i])):
                    dp[i] = dp[i-coin]+1
        
        return dp[amount]
