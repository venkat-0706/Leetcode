# Added using AI
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = [0] * n
        mn[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            mn[i] = min(nums[i], mn[i+1])
        mxi = float('-inf')
        for i in range(n):
            mxi = max(mxi, nums[i])
            if mxi - mn[i] <= k:
                return i
        return -1