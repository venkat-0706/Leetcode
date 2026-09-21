class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            nxt = [0] * k
            nxt[x] += 1

            for r in range(k):
                new_r = (r * x) % k
                nxt[new_r] += dp[r]

            for r in range(k):
                ans[r] += nxt[r]
            dp = nxt

        return ans