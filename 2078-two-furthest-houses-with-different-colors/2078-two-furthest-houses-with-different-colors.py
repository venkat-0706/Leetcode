class Solution:
    def maxDistance(self, A: List[int]) -> int:
        j = len(A)

        for i in range(j):
            if (A[i] ^ A[-1]) | (A[-1 - i] ^ A[0]):
                return j - 1 - i

        return 0