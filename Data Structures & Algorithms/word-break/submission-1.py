class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s))]

        for word in wordDict:
            n = len(word)
            if s[:n] == word:
                dp[n-1] = True
        
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                n = len(word)
                if i+1+n > len(s):
                    continue
                if s[i+1:i+1+n] == word:
                    dp[i+1+n-1] = True
        return dp[-1]