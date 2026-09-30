class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cur = ["."*n]*n
        ans = []

        
        def dfs(i):
            if i == n:
                ans.append(cur.copy())
            
            for j in range(n):
                if check(i, j):
                    cur[i] = '.'*(j)+'Q'+'.'*(n-j-1)
                    dfs(i+1)
                    cur[i] = '.'*n
            
        def check(i,j):
            # no need to check row

            # check column
            for k in range(n):
                if cur[k][j] == "Q":
                    return False
                
            # check top-left diagonal
            k, l = i-1, j-1
            while k > -1 and l > -1:
                if cur[k][l] == "Q":
                    return False
                k-=1
                l-=1
            # check top-right diagonal
            k, l = i-1, j+1
            while k > -1 and l < n:
                if cur[k][l] == "Q":
                    return False
                k-=1
                l+=1
            
            return True
        
        dfs(0)
        return ans
