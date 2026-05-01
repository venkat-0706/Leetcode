class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = sum(nums)
        F = sum(i * nums[i] for i in range(n))

        ans = F

        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            ans = max(ans, F)

        return ans