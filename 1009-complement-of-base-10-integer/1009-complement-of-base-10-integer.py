class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if n==0 else n^((1<<n.bit_length())-1)