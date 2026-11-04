class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 2 or n < 2:
            return 1
        dp = [[0 for i in range(n)] for j in range(m)]

        dp[0][0] = 1
        dp[0][1] = 1
        dp[1][0] = 1

        for i in range(m):
            for j in range(n):
                if i+j < 2:
                    continue

                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]
