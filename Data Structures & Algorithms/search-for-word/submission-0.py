class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] == "#" or board[i][j] != word[k]:
                return False
            
            if k == len(word)-1:
                return True
            
            board[i][j], temp = "#", board[i][j]
            ans = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = temp

            return ans
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False
            