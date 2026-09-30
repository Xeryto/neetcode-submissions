class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1,0), (0,1), (1, 0), (0, -1)]
        uncapturable = set()

        n,m = len(board), len(board[0])

        def bfs(i, j):
            q = deque([(i,j)])
            uncapturable.add((i,j))

            while q:
                r,c = q.popleft()
                print(r,c)
                for a,b in directions:
                    nr,nc = r+a, c+b
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or (nr,nc) in uncapturable or board[nr][nc] != 'O':
                        continue
                    
                    q.append((nr,nc))
                    uncapturable.add((nr,nc))
            

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    if (i,j) not in uncapturable and board[i][j] == 'O':
                        bfs(i,j)
        
        for i in range(n):
            for j in range(m):
                if (i,j) not in uncapturable and board[i][j] == 'O':
                    board[i][j] = 'X'
        
        return