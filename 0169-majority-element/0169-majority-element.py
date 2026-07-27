class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_ele = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if(count == 0):
                count += 1
                max_ele = nums[i]
            elif max_ele == nums[i]:
                count += 1
            else:
                count -= 1 
        return max_ele
        