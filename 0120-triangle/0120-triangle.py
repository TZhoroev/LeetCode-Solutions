class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        a = triangle[0]
        for paths in triangle[1:]:
            b = [a[0]+paths[0]]
            for i in range(1, len(paths) - 1):
                b.append(min(a[i-1], a[i]) + paths[i])
            b.append(a[-1] + paths[-1])
            a, b = b, []
        return min(a)