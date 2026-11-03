class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range (amount+1)]

        dp[0] = 0

        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1
        
        for total in range(1, amount+1):
            if dp[total] != -1:
                for coin in coins:
                    if total+coin > amount:
                        continue
                    if dp[total+coin] == -1 or dp[total+coin] > dp[total]+1:
                        dp[total+coin] = dp[total]+1
        
        return dp[amount]
