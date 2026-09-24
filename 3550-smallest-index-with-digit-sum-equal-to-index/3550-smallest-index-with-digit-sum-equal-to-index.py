class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            num = n 
            total = 0 
            while num > 0 : 
                total += num % 10 
                num //= 10 
            if total == i : 
                return  i 
        return  -1

        