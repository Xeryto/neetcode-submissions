class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            m = l + ((r - l) // 2)  
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m + 1
            else:
                return True

        l = l+((r-l)//2)
        rowL, rowR = 0, len(matrix[l])-1
        while rowL <= rowR:
            center = rowL + (rowR-rowL)//2
            if matrix[l][center] < target:
                rowL = center+1
            elif matrix[l][center] > target:
                rowR = center-1
            else:
                return True
        else:
            return False
