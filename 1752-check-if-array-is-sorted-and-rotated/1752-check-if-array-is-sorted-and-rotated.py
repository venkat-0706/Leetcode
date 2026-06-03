class Solution:
    def check(self, nums: List[int]) -> bool:
        breaks = 0 
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%n]:
                breaks += 1 
        return breaks <= 1
        