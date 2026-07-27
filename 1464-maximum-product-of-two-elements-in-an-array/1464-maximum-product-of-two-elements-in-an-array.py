class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = 0
        for num in nums:
            if num > first:
                second = first 
                first  = num 
            elif num > second :
                second = num 

        return (second-1) * (first-1)
        