class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1,0), (0, 1)]
        n,m = len(grid), len(grid[0])
        ans = 0
        def dfs(i,j):
            nonlocal grid
            nonlocal ans
            for r,c in directions:
                ri, cj = r+i, c+j
                
                if ri >= 0 and cj >= 0 and ri < n and cj < m:
                    if grid[ri][cj] == 0:
                        grid[ri][cj] = -1
                        dfs(ri, cj)
                    elif grid[ri][cj] == 1:
                        ans+=1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                    dfs(i,j)
                elif grid[i][j] == 1:
                    if i == 0:
                        ans+=1
                    if j == 0:
                        ans+=1
                    if i == n-1:
                        ans+=1
                    if j == m-1:
                        ans+=1

        return ans
