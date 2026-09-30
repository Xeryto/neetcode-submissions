class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        pivots = [0]

        dp[0] = dp[0] in wordDict

        for i in range(len(s)):
            for pivot in pivots:
                if s[pivot:i+1] in wordDict and (dp[pivot-1] or pivot == 0):
                    dp[i] = True
                    pivots.append(i+1)
                    break
        
        return dp[-1]