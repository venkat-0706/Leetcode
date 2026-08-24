class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp = [0]*len(nums)
        index = 0 
        for num in nums : 
            if num != 0 : 
                temp[index] = num 
                index += 1
        for i in range(len(nums)) : 
            nums[i] = temp[i]
        return nums
