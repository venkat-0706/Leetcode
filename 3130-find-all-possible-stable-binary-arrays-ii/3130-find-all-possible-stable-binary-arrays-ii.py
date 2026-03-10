class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base cases: only 0s or only 1s
        for i in range(1, min(limit, zero) + 1):
            dp0[i][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp1[0][j] = 1

        for z in range(1, zero + 1):
            for o in range(1, one + 1):
                # Append a 0: came from any array ending in 0 or 1
                dp0[z][o] = dp0[z-1][o] + dp1[z-1][o]
                # Subtract arrays that would have limit+1 trailing 0s
                if z > limit:
                    dp0[z][o] -= dp1[z-limit-1][o]

                # Append a 1: came from any array ending in 0 or 1
                dp1[z][o] = dp1[z][o-1] + dp0[z][o-1]
                # Subtract arrays that would have limit+1 trailing 1s
                if o > limit:
                    dp1[z][o] -= dp0[z][o-limit-1]

        return (dp0[zero][one] + dp1[zero][one]) % MOD