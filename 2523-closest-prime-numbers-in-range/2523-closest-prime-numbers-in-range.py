class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes, is_prime = [], [True] * (right + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, right + 1):
            if is_prime[i]:
                if i >=left:
                    primes.append(i)
                for j in range(2 * i, right + 1, i):
                    is_prime[j] = False  
        min_diff, num1, num2 = float('inf'), -1, -1
        for i in range(len(primes) - 1):
            if primes[i+1] - primes[i] <= min_diff:
                min_diff, num1, num2 = primes[i+1]-primes[i], primes[i], primes[i+1]
            if min_diff <= 2:
                break
        return [num1, num2] 
        