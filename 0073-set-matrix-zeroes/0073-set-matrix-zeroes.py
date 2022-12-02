class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cond = all(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][0] == 0  or  matrix[0][j] == 0:
                    matrix[i][j] = 0
        if not cond:
            matrix[0][:] = [0 for x in matrix[0]]
        """
        Do not return anything, modify matrix in-place instead.
        """
        