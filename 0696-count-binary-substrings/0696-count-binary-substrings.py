class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(sum(1 for _ in g) for _,g in groupby(s))))