class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('1' if x[i]=='0' else '0' for i, x in enumerate(nums))