class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            if text1[i] == text2[0]:
                dp[i][0] = 1

        idx = text2.find(text1[0])
        if idx != -1:
            for i in range(idx, len(text2)):
                dp[0][i] = 1
        for i in range(1, len(text1)):
            dp[i][0] = max(dp[i][0], dp[i-1][0])
            for j in range(1, len(text2)):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        return dp[-1][-1]

        
