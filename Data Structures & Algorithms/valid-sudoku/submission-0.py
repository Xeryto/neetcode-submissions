class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            st = set(board[i])
            n = 9-board[i].count(".")
            if len(st) !=  n+1:
                return False
            colSt = set()
            colN = 0
            for j in range(9):
                colSt.add(board[j][i])
                colN+=(board[j][i] != ".")
                if i%3 == 0 and j%3 == 0:
                    boxSt = set(board[i][j:j+3])
                    boxN = 3-board[i][j:j+3].count(".")
                    for k in range(1,3):
                        boxSt.update(board[i+k][j:j+3])
                        boxN+=3-board[i+k][j:j+3].count(".")
                    if len(boxSt) !=  boxN+1:
                        return False
            if len(colSt) !=  colN+1:
                return False
        return True