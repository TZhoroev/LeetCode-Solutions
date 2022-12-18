class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            new_n = self.factorization(n)
            if new_n == n:
                return new_n
            n = new_n
    def factorization(self, n):
        factors = 0
        i = 2
        while n > 1:
            while n % i == 0:
                n = n//i
                factors +=i
            i += 1
        return factors
        
        