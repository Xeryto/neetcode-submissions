class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) < 2:
            return 1 if s[0] != '0' else 0

        dp = [0]*len(s)
        dp[-1] = 1 if s[-1] != '0' else 0
        dp[-2] = (s[-2] != '0' and dp[-1]) + (10 <= int(s[len(s)-2:len(s)]) <= 26)

        for i in range(len(s)-3, -1, -1):
            if 10 <= int(s[i:i+2]) <= 26 and dp[i+2]:
                dp[i]+=dp[i+2]
            if s[i] != '0' and dp[i+1]:
                dp[i]+=dp[i+1]
        
        return dp[0]