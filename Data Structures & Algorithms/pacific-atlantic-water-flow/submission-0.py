class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_pac = set()
        visited_atl = set()
        directions = [(-1,0), (0,1), (1, 0), (0, -1)]
        n,m = len(heights), len(heights[0])
        def dfs(i,j, pac, atl, visit):
            for r,c in directions:
                nr,nc = i+r, j+c
                if nr < 0 or nc < 0 or nr == n or nc == m or (nr,nc) in visit or heights[nr][nc] < heights[i][j]:
                    continue
                if pac:
                    visited_pac.add((nr,nc))
                if atl:
                    visited_atl.add((nr,nc))
                visit.add((nr,nc))
                dfs(nr,nc, pac, atl, visit)
        
        

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    pac, atl = False, False
                    if i == 0 or j == 0:
                        pac = True
                        visited_pac.add((i,j))
                    if i == n-1 or j == m-1:
                        atl = True
                        visited_atl.add((i,j))
                    dfs(i,j,pac,atl, set([(i,j)]))

        return [[i,j] for i,j in visited_pac & visited_atl]

                
            
