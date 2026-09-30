class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0,1), (1, 0), (0, -1)]
        n,m = len(grid), len(grid[0])
        minutes = [[-1]*m for i in range(n)]
        def bfs(I,J):
            q = deque([((I,J), 1)])
            minutes[I][J] = 0

            while q:
                (i,j),dist = q.popleft()

                for r, c in directions:
                    nr,nc = i+r, j+c
                    
                    if nr < 0 or nc < 0 or nr>=n or nc >= m or grid[nr][nc] != 1:
                        continue
                    if not (minutes[nr][nc] == -1 or dist < minutes[nr][nc]):
                        continue
                    minutes[nr][nc] = dist
                    q.append(((nr,nc), dist+1))
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    bfs(i,j)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and minutes[i][j] == -1:
                    return -1
                ans = max(ans, minutes[i][j])
        
        return ans
        
