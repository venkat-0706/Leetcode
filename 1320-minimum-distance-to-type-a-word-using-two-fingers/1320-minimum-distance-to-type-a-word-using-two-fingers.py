class Solution(object):
    def cal(self, a, b):
        return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

    def minimumDistance(self, word):
        n = len(word)
        dp = [[[0] * 26 for _ in range(26)] for _ in range(n + 1)]

        for i in range(n):
            t = ord(word[i]) - ord('A')

            for j in range(26):
                for k in range(26):
                    dp[i + 1][j][k] = 1000000

            for j in range(26):
                for k in range(26):
                    dp[i + 1][j][t] = min(dp[i + 1][j][t], dp[i][j][k] + self.cal(k, t))
                    dp[i + 1][t][k] = min(dp[i + 1][t][k], dp[i][j][k] + self.cal(j, t))

        ans = 100000
        for j in range(26):
            for k in range(26):
                ans = min(ans, dp[n][j][k])

        return ans