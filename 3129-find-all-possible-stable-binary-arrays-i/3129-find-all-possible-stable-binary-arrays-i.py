class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000007
        maxN = zero + one
        
        fact = [0] * (maxN + 1)
        invFact = [0] * (maxN + 1)
        
        fact[0] = 1
        invFact[0] = 1
        for i in range(1, maxN + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            
        invFact[maxN] = pow(fact[maxN], MOD - 2, MOD)
        for i in range(maxN - 1, 0, -1):
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
            
        def C(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD

        def F(N, K, L):
            if K <= 0 or K > N:
                return 0
            ans = 0
            maxJ = (N - K) // L
            for j in range(maxJ + 1):
                term = C(K, j) * C(N - j * L - 1, K - 1) % MOD
                if j & 1:
                    ans = (ans - term + MOD) % MOD
                else:
                    ans = (ans + term) % MOD
            return ans

        maxK = min(zero, one + 1)
        fOne = [0] * (maxK + 2)
        for k in range(1, maxK + 2):
            fOne[k] = F(one, k, limit)
            
        ans = 0
        for k in range(1, maxK + 1):
            fz = F(zero, k, limit)
            if fz == 0:
                continue
            fo = (fOne[k - 1] + 2 * fOne[k] + fOne[k + 1]) % MOD
            ans = (ans + fz * fo) % MOD
            
        return ans