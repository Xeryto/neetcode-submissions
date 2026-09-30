class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        directions = [(-1,0), (0,1), (1, 0), (0,-1)]
        n,m = len(grid), len(grid[0])

        def bfs(I, J):
            cur = 1
            q = deque([(I,J)])
            grid[I][J] = 0

            while q:
                i,j = q.popleft()

                for r,c in directions:
                    nr,nc = i+r, j+c
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] == 0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    cur+=1
            
            return cur
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, bfs(i,j))
        
        return ans