class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        index = 0 
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index] = num 
                index += 1 
        return index

        