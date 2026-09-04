class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            min_value = max_value = nums[i]
            for j in range(i):
                max_value = max(max_value , nums[j])
            for j in range(i+1, n):
                min_value = min(min_value , nums[j])
            if max_value - min_value <= k:
                return i 
        return -1

        