class Solution:
    def maxDistance(self, A: List[int], B: List[int]) -> int:
        i = j = 0

        while i < len(A) and j < len(B):
            i += A[i] > B[j]
            j += 1

        return max(0, j - i - 1)