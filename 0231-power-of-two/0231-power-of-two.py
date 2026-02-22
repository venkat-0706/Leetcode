class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        while n!=0:
            if n&1==0:
                return True
            n //= 2
        return False
        