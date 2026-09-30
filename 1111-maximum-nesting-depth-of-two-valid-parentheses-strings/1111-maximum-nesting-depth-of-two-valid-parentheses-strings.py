class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []

        for i in range(len(seq)):
            res.append((i ^ ord(seq[i])) & 1)

        return res