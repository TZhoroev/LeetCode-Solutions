class Solution:
    def numTilings(self, n: int) -> int:
        if n ==1: return 1
        elif n==2: return 2
        elif n==3: return 5
        a, b, c = 5, 2, 1
        for i in range(4, n + 1):
            a, b, c = 2 * a + c, a, b
        return a % (10 ** 9 + 7)