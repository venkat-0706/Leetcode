class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev =  int(str(n)[::-1])
        return abs(rev-n)