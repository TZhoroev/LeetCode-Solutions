class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [1 for i in range(n)]
        b = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                b[j] = b[j-1]+ a[j]
            a, b = b, [1 for _ in range(n)]
        return a[-1]
        
        