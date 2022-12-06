class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            res = 0
            while n != 0:
                res += (n % 10)**2
                n = n//10
            return res
        numbers = set()
        while n != 1:
            n = sum_of_squares(n)
            if n in numbers:
                return False
            numbers.add(n)
        return True
        