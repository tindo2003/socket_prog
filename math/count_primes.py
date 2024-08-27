class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1] * n
        for i in range(2, n):
            if primes[i] != 0:
                for j in range(2*i, n, i):
                    primes[j] = 0
        return sum(primes)