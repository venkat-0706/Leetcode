class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        index = 0 
        for num in range(nums[0], nums[-1]+1):
            if index < len(nums) and nums[index] == num:
                index += 1 
            else:
                res.append(num)
        return res




        