class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums) 
        temp = [0]*(n+1)
        index = 0 
        for num in nums : 
            if num != 0 :
                temp[index] = num 
                index += 1
        for i in range(n) :
            nums[i] = temp[i]
        
        return nums


        