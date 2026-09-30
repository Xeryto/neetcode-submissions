class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        directions = [(0,-1), (1,0), (0, 1), (-1, 0)]
        n, m = len(grid), len(grid[0])

        def dfs(i,j):
            grid[i][j] = '0'
            for x,y in directions:
                ix, jy = i+x, j+y
                if ix < 0 or jy < 0 or ix >= n or jy >= m or grid[ix][jy] == '0':
                    continue
                dfs(ix, jy)
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans+=1
                    dfs(i,j)
        
        return ans