class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (0,1), (1, 0), (0, -1)]
        n,m = len(grid), len(grid[0])
        def bfs(I,J):
            q = deque([((I,J), 1)])

            while q:
                (i,j),dist = q.popleft()

                for r, c in directions:
                    nr,nc = i+r, j+c
                    
                    if nr < 0 or nc < 0 or nr>=n or nc >= m or grid[nr][nc] <= dist:
                        continue
                    grid[nr][nc] = dist
                    q.append(((nr,nc), dist+1))
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    bfs(i,j)
        
