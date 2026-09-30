class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]*len(coins) for _ in range(amount+1)]

        coins.sort()

        def dfs(curSum, prevCoinIndex):
            if curSum >= amount:
                return 1 if curSum == amount else 0

            ans = 0
            
            for i in range(prevCoinIndex, len(coins)):
                if curSum+coins[i] <= amount:
                    if dp[curSum+coins[i]][i] == -1:
                        dp[curSum+coins[i]][i] = dfs(curSum+coins[i], i)
                    ans += dp[curSum+coins[i]][i]
            
            return ans

        return dfs(0, 0)

            