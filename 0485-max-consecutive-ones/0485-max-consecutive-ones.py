
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count , max_count = 0 ,0 
        curr = 0
        while curr < len(nums):
            if nums[curr] == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0
            curr += 1
        return max_count
        
        