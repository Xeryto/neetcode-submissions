class Solution:
    def totalNQueens(self, n: int) -> int:
        placements = [-1]*n
        
        ans = 0

        def safe(i):
            val = placements[i]
            for j in range(i):
                if placements[j] == val or ((i-j) == abs(val-placements[j])):
                    return False
        
            return True

        def dfs(i):
            nonlocal placements
            nonlocal ans
            if i == n:
                ans+=1
                return

            for j in range(n):
                placements[i] = j
                if safe(i):
                    dfs(i+1)
                placements[i] = -1
        
        dfs(0)

        return ans