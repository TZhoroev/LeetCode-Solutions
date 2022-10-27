class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1": 
                    self.dfs(grid, r, c)
                    count +=1
        return count
    
    
    
    def dfs(self, grid, sr, sc):
        if sr<0 or sc<0 or sr >=len(grid) or sc>=len(grid[0]) or grid[sr][sc]!="1":
            return
        grid[sr][sc] = "$"
        self.dfs(grid, sr-1, sc), self.dfs(grid, sr+1, sc), self.dfs(grid, sr, sc+1), self.dfs(grid, sr, sc-1)
        