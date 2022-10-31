class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        a = [1 for _ in range(n)]
        for i in range(1, n):
            if obstacleGrid[0][i] or a[i-1]==0:
                a[i] = 0
        b = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(0, n):
                if j==0:
                    if obstacleGrid[i][j] or a[j]==0: b[j] = 0
                    else: b[j] = a[j]         
                else:
                    if obstacleGrid[i][j] or (a[j]==0 and b[j-1]==0): b[j] = 0
                    elif a[j]==0: b[j] = b[j-1]
                    elif b[j-1]==0: b[j] = a[j]
                    else: b[j] = b[j-1]+ a[j]
            a, b = b, [1 for _ in range(n)]
        return a[-1]
        