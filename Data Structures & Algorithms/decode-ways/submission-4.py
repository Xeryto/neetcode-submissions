class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range (len(s)+1)]
        
        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            dp[i] = dp[i+1] if s[i] != '0' else 0

            if i+1 < len(s) and 10 <= int(s[i]+s[i+1]) <= 26:
                dp[i]+=dp[i+2]
        
        return dp[0]

            