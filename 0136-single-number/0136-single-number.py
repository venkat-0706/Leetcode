class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for i in range(len(nums)):
            res ^= nums[i]
        return res