class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =  len(nums)
        total = sum(nums)
        ans = (n*(n+1)) // 2
        return ans - total

        