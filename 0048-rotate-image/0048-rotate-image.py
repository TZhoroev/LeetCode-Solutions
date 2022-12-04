class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n > 1:        
            for i in range(n):
                for j in range(max(i+1, n-i-1)):
                    matrix[i][j], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[i][j]
            
        """
        Do not return anything, modify matrix in-place instead.
        """
        