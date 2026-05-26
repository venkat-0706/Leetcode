class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =  len(nums)
        actual_sum = (n*(n+1)) // 2
        curr_sum = 0 
        for i in range(n):
            curr_sum += nums[i]

        return actual_sum - curr_sum

        