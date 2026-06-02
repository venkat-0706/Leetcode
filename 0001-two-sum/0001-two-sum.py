class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict  = {}
        for i in range(0,len(nums)):
            ele = target - nums[i]
            if ele in dict:
                return [i, dict[ele]]
            else:
                dict[nums[i]] =  i       