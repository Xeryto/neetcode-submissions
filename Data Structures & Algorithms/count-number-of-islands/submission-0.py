class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(startI, startJ):
            q = deque([(startI, startJ)])

            while q:
                i,j = q.popleft()
                grid[i][j] = "0"
                if i-1 >= 0 and grid[i-1][j] == "1":
                    q.append((i-1, j))
                if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                    q.append((i, j+1))
                if i+1 < len(grid) and grid[i+1][j] == "1":
                    q.append((i+1, j))
                if j-1 >= 0 and grid[i][j-1] == "1":
                    q.append((i, j-1))
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans+=1
                    bfs(i,j)

        return ans
                    
