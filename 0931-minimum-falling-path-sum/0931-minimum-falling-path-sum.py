class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1: return min(matrix[0])
        prev_row = matrix[0]
        for i in range(1, n):
            curr_row = []
            for j in range(n):
                #left edge case
                if j == 0:
                    prev_min = min(prev_row[j], prev_row[j + 1])
                # right edge case
                elif j == n - 1:
                    prev_min = min(prev_row[j-1], prev_row[j])
                else:
                    prev_min = min(prev_row[j-1], prev_row[j], prev_row[j + 1])
                curr_row.append(prev_min + matrix[i][j])
            #update previous row
            prev_row = curr_row
        return min(curr_row)


        