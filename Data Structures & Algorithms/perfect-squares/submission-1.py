from math import floor, sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        biggest = floor(sqrt(n))

        dp = [0]*(n+1)

        for i in range(1,n+1):
            mn = float('inf')
            for num in range(1, biggest+1):
                if i-num**2>=0:
                    mn = min(mn, dp[i-num**2])
            
            if mn != float('inf'):
                dp[i] = mn+1

        return dp[n]