class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cur = []
        ans = []
        n = len(s)
        def dfs(i):
            if i == n:
                ans.append(' '.join(cur))
            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    cur.append(s[i:j])
                    dfs(j)
                    cur.pop(-1)
        
        dfs(0)
        return ans
