def ceil(x, y):
    return (x + y - 1) // y


class Solution:
    def minOperations(self, S, K):
        N = len(S)
        Z = S.count("0")

        if N == K:
            return 0 if Z == 0 else 1 if Z == N else -1

        ans = inf
        if Z % 2 == 0:
            M = max(ceil(Z, K), ceil(Z, N - K))
            M += M & 1
            ans = min(ans, M)
        if Z % 2 == K % 2:
            M = max(ceil(Z, K), ceil(N - Z, N - K))
            M += M & 1 == 0
            ans = min(ans, M)

        return ans if ans < inf else -1