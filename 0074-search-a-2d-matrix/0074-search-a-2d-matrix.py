class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n*m - 1
        while left <= right:
            mid = (left + right)//2
            if matrix[mid//m][mid%m] == target: return True
            elif matrix[mid//m][mid%m] < target: left = mid +1
            else: right = mid -1
        return False
        
        