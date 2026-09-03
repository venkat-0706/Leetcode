class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        smallest_odd = float('inf')
        for num in nums:
            if num%2  == 1:
                smallest_odd = min(smallest_odd , num)
        if smallest_odd == float('inf') : 
            return True 
        
        for num in nums:
            if num %2 == 0 and  num <= smallest_odd : 
                return False 
        return True

        