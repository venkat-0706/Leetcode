class Solution:
    def sieve(self,n:int)->bool:
        primes = [True] * (n+1)
        primes[0] = primes[1] = False
        p = 2
        while p*p<= n:
            if primes[p]:
                for i in range(p*p ,(n+1),p):
                    primes[i] = False
            p += 1
        return primes

    def countPrimes(self, n: int) -> int:
        if n<= 1:
            return 0

        count = self.sieve(n-1)
        return sum(count)
        

    