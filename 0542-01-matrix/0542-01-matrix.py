class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        visited, q = set(), deque()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    q.append((row, col))
        while q:
            row, col = q.popleft()
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                r, c = row + dy, col + dx
                if 0<=r<m and 0<=c<n and (r, c) not in visited:
                    visited.add((r, c))
                    q.append((r, c))
                    mat[r][c] = mat[row][col] + 1

        return mat
        