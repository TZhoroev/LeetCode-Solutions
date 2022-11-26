class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        onesRow = [0 for _ in range(n)]
        onesCol = [0 for _ in range(m)]
        zerosRow = [0 for _ in range(n)]
        zerosCol = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    onesRow[i] +=1
                    onesCol[j] +=1
                else:
                    zerosRow[i] +=1
                    zerosCol[j] +=1
        diff = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                diff[i][j] = onesRow[i]+ onesCol[j] - zerosRow[i] - zerosCol[j]
        return diff
        