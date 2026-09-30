class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        prefRow = [matrix[0][0]]
        for j in range(1,self.m):
            prefRow.append(prefRow[j-1]+matrix[0][j])
        self.pref = [prefRow]
        for i in range(1,self.n):
            prefRow = [matrix[i][0]+self.pref[i-1][0]]
            for j in range(1,self.m):
                prefRow.append(prefRow[j-1]+self.pref[i-1][j]-self.pref[i-1][j-1]+matrix[i][j])
            self.pref.append(prefRow)

        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.pref[row2][col2]
        if row1 != 0:
            answer -= self.pref[row1-1][col2]
        if col1 != 0:
            answer -= self.pref[row2][col1-1]
        if row1 != 0 and col1 != 0:
            answer += self.pref[row1-1][col1-1]
        return answer


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)