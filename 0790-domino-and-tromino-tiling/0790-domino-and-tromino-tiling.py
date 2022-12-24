class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def dp(n):
            if n ==1: return 1
            elif n==2: return 2
            elif n==3: return 5
            else: return (2*dp(n-1)+dp(n-3)) % (10 ** 9 + 7)
        return dp(n)
