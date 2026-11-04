class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2))] for j in range(len(text1))]

        def dfs(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if dp[i][j] != 0:
                return dp[i][j]
            
            if text1[i] == text2[j]:
                dp[i][j] = 1+dfs(i+1, j+1)
            else:
                dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            
            return dp[i][j]
        
        return dfs(0,0)
