class Solution(object):
    def reverse(self, x):
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev

    def minMirrorPairDistance(self, nums):
        mpp = {}
        n = len(nums)
        ans = 10 ** 6

        for i in range(n):
            if nums[i] in mpp:
                ans = min(ans, i - mpp[nums[i]])
            mpp[self.reverse(nums[i])] = i

        return -1 if ans == 10 ** 6 else ans