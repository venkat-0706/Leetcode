class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right =  0 , len(numbers)-1
        while left <= right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum < target:
                left += 1 
            else:
                right -= 1
        return [left,right]

        