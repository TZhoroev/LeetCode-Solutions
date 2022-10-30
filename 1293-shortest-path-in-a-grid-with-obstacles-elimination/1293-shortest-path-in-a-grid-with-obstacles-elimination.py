from collections import deque, defaultdict
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(0,0,k,0)])
        visited = defaultdict(lambda:False)
        while q:
            x, y, left, steps = q.popleft()
            if visited[(x,y, left)] or left<0:
                continue
            if (x, y) == (m-1, n-1):
                return steps
            visited[(x,y, left)] = True
            if grid[x][y] == 1:
                left-=1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n:
                    q.append((new_x, new_y, left, steps+1))
        return -1
        
        
    
        