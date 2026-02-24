class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        while left < right:
            left >>= 1
            right >>= 1
            res += 1
        return left << res

        