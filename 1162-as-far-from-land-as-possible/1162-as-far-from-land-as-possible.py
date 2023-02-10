class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        Q, m, n = deque(), len(grid), len(grid[0])
        seen, res, cond = set(), -1, True
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    Q.append([row, col, 0])
                    seen.add((row, col))
                else:
                    cond = False
        if cond or not Q:
            return -1
        while Q:
            row, col, length = Q.popleft()
            res = max(res, length)
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                x, y = row + dy, col + dx
                if 0<=x<m and 0<=y<n and (x, y) not in seen:
                    seen.add((x, y))
                    Q.append([x, y, length + 1])
        return res
            
            
        
        