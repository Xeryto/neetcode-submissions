class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def bfs(startI, startJ):
            q = deque([(startI, startJ)])
            grid[startI][startJ] = "0"

            while q:
                i,j = q.popleft()
                
                for r,c in directions:
                    nr,nc = i+r, j+c
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] == '0':
                        continue
                    
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i,j)
                    ans+=1

        return ans
                    
