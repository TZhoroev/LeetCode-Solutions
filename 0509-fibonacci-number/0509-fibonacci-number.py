class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n==0: return 0
        if n==1: return 1
        for _ in range(n-1):
            a, b = b, a+b
        return b
        