class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        
        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= x + dx < n and 0 <= y + dy < m and heights[x + dx][y + dy] >= heights[x][y]: 
                    if (x + dx, y + dy) not in visited:
                        dfs(visited, x + dx, y + dy)
        a_visited, p_visited = set(), set()
        
        for i in range(n):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, m - 1)
        
        for i in range(m):
            dfs(p_visited, 0, i)
            dfs(a_visited, n - 1, i)
        return list(a_visited.intersection(p_visited))
        