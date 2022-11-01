class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        return [self.dfs(grid, 0, i, m, n)  for i in range(n)] 
        
    def dfs(self, grid, cr, cc, m, n):
        if cr == m: return cc  
        if grid[cr][cc] ==1:
            if cc + 1 == n: return -1
            elif grid[cr][cc+1]==-1: return -1
            else: return self.dfs(grid, cr + 1, cc + 1, m, n)     
        else:
            if cc == 0: return -1
            elif grid[cr][cc-1]==1: return -1
            else: return self.dfs(grid, cr + 1, cc - 1, m, n)  
        