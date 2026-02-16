class Solution:
    def reverseBits(self, n: int) -> int:
        if n==0: return 0
        ans=0
        while n>0:
            ans+=1<<(32-(n&-n).bit_length())
            n&=(n-1)
        return ans
        