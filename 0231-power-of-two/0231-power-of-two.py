class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and pow(2, 31, n) == 0
        